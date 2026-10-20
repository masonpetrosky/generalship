"""Missingness, provenance, complete groups and outcome/final-set exclusion."""

from pathlib import Path
import unittest
from unittest.mock import patch

from generalship import napoleonic_inventory as inv

ROOT = Path(__file__).resolve().parents[1]


class InventoryUnitTests(unittest.TestCase):
    def partition(self):
        return ({'entries': [{'id': 'd1', 'start_year': 1812, 'campaign_group': 'dev'},
                             {'id': 'd2', 'start_year': 1812, 'campaign_group': 'dev'},
                             {'id': 'f1', 'start_year': 1814, 'campaign_group': 'final'}]},
                {'battle_ids': ['d1', 'd2', 'f1']},
                {'development': ['d1', 'd2'], 'reserved_final': ['f1'],
                 'frozen_groups': {'dev': ['d1', 'd2'], 'final': ['f1']}})

    def test_complete_development_campaign_only(self):
        self.assertEqual(inv.groups_for_partition(*self.partition()), {'dev': ['d1', 'd2']})

    def test_missing_partition_entry_rejected(self):
        f, c, p = self.partition()
        p['development'].pop()
        with self.assertRaisesRegex(ValueError, 'partition coverage'):
            inv.groups_for_partition(f, c, p)

    def test_duplicate_partition_entry_rejected(self):
        f, c, p = self.partition()
        p['development'].append('d1')
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            inv.groups_for_partition(f, c, p)

    def test_group_cannot_cross_final_boundary(self):
        f, c, p = self.partition()
        f['entries'][-1]['campaign_group'] = 'dev'
        p['frozen_groups'] = {'dev': ['d1', 'd2', 'f1']}
        with self.assertRaisesRegex(ValueError, 'campaign split'):
            inv.groups_for_partition(f, c, p)

    def test_null_absent_and_recorded_are_distinct(self):
        self.assertEqual(inv.field_state({}, 'x'), 'absent')
        self.assertEqual(inv.field_state({'x': None}, 'x'), 'null')
        self.assertEqual(inv.field_state({'x': 'date'}, 'x'), 'recorded')
        self.assertEqual(inv.typed_field({}, 'quantities'), {'state': 'absent', 'records': 0})
        self.assertEqual(inv.typed_field({'quantities': []}, 'quantities'), {'state': 'recorded', 'records': 0})

    def test_null_typed_array_is_not_an_empty_array(self):
        with self.assertRaisesRegex(ValueError, 'typed field'):
            inv.typed_field({'quantities': None}, 'quantities')

    def rows(self):
        return [{'battle_id': b, 'claims': 3, 'statuses': {'unknown': 1, 'disputed': 1},
                 'completion_brief_version': None,
                 'boundaries': {'tactical_replacement_at': 'null', 'campaign_replacement_at': 'null'},
                 'typed': {'quantities': {'state': 'absent', 'records': 0}},
                 'sides': [{'pilot_mapping': None}, {'pilot_mapping': None}],
                 'relevant_citations': [{'dimension': dim, 'frame_family': False,
                                        'family': 'one-family',
                                        'image': {'source_id': 'page1', 'sha256': 'same-bytes'}}
                                       for dim in inv.RELEVANT]}
                for b in ('d1', 'd2')]

    def test_page_reuse_deduplicates_claims_and_entries(self):
        g = inv.summarize_group('dev', self.rows(), inv.SELECTION)
        self.assertEqual((g['non_frame_citation_references'], g['non_frame_image_ids'],
                          g['non_frame_images_shared_across_entries']), (4, 1, 1))
        self.assertEqual(g['non_frame_family_entry_counts'], {'one-family': 2})
        self.assertTrue(g['eligible_next_batch'])

    def test_identical_image_bytes_under_different_ids_disclosed(self):
        rows = self.rows()
        rows[1]['relevant_citations'][0]['image']['source_id'] = 'page-copy'
        g = inv.summarize_group('dev', rows, inv.SELECTION)
        self.assertEqual(g['non_frame_distinct_image_hashes'], 1)
        self.assertEqual(g['duplicate_image_hash_ids'], [['page-copy', 'page1']])

    def test_missing_image_not_treated_as_zero_cost(self):
        rows = self.rows()
        rows[0]['relevant_citations'][0]['image'] = None
        g = inv.summarize_group('dev', rows, inv.SELECTION)
        self.assertEqual(g['non_frame_missing_image_references'], 1)
        self.assertFalse(g['eligible_next_batch'])

    def test_bodart_does_not_fill_non_frame_dimension(self):
        rows = self.rows()
        rows[0]['relevant_citations'][0]['frame_family'] = True
        g = inv.summarize_group('dev', rows, inv.SELECTION)
        self.assertEqual(g['entries_with_non_frame_citations_in_both_dimensions'], 1)
        self.assertFalse(g['eligible_next_batch'])

    def test_stopped_pilot_and_large_campaign_excluded(self):
        self.assertIn('stopped_pilot', inv.summarize_group('third-coalition 1806', self.rows(), inv.SELECTION)['selection_exclusions'])
        self.assertIn('above_12_entry_batch_bound', inv.summarize_group('large', self.rows() * 7, inv.SELECTION)['selection_exclusions'])

    def test_selection_uses_pages_then_entries_then_name(self):
        groups = [{'campaign': name, 'non_frame_image_ids': pages, 'entries': entries,
                   'eligible_next_batch': eligible}
                  for name, pages, entries, eligible in
                  [('excluded', 0, 1, False), ('more-pages', 8, 2, True),
                   ('larger', 7, 10, True), ('z', 7, 8, True), ('a', 7, 8, True)]]
        self.assertEqual(inv.select_campaign(groups), 'a')
        self.assertIsNone(inv.select_campaign([groups[0]]))


class InventoryRepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = inv.build(ROOT)

    def test_exact_denominators_and_missingness(self):
        self.assertEqual(self.data['denominators'], {
            'development_entries': 273, 'development_sides': 546, 'development_groups': 13,
            'reserved_final_entries': 52, 'reserved_final_groups': 3, 'final_dossiers_opened': 0})
        self.assertEqual(self.data['totals']['boundary_states']['tactical_replacement_at'], {'null': 273})
        self.assertEqual(self.data['totals']['indexed_pilot_sides'], 8)
        self.assertEqual(self.data['totals']['sides_without_indexed_mapping'], 538)
        self.assertEqual(self.data['emitted_model_rows'], [])
        self.assertFalse(self.data['historical_outcomes_fitted'])

    def test_final_dossiers_and_outcome_values_never_read(self):
        original = inv.read_json
        final = set(original(ROOT / inv.PARTITION)['reserved_final'])

        class NoInterpretation(dict):
            def __getitem__(self, key):
                if key in {'value', 'rationale', 'winner_text', 'loser_text', 'outcome_side_a',
                           'winner_commander_text', 'loser_commander_text'}:
                    raise AssertionError('Inventory read interpretation/outcome/name: ' + key)
                return super().__getitem__(key)

        def read(path):
            path = Path(path)
            if path.parent.name == 'evidence' and path.stem in final:
                raise AssertionError('Opened a reserved-final dossier')
            d = original(path)
            if path.parent.name == 'evidence':
                d['claims'] = [NoInterpretation(c) for c in d['claims']]
            if path == ROOT / inv.FRAME:
                d['entries'] = [NoInterpretation(r) for r in d['entries']]
            return d

        with patch.object(inv, 'read_json', side_effect=read):
            self.assertEqual(inv.build(ROOT), self.data)

    def test_bound_input_drift_rejected(self):
        original = inv.digest

        def changed(path):
            return '0' * 64 if Path(path) == ROOT / inv.AUTHORITY else original(path)

        with patch.object(inv, 'digest', side_effect=changed):
            with self.assertRaisesRegex(ValueError, 'changed bound input'):
                inv.build(ROOT)

    def test_every_relevant_reference_has_provenance(self):
        for row in self.data['dossiers']:
            self.assertEqual(len(row['dossier_sha256']), 64)
            for cite in row['relevant_citations']:
                for field in ('quote_sha256', 'raw_sha256', 'metadata_sha256'):
                    self.assertEqual(len(cite[field]), 64)
                self.assertTrue(cite['locator'])
                self.assertIn(cite['dimension'], inv.RELEVANT)

    def test_deterministic_group_denominators_and_selection(self):
        groups = self.data['groups']
        self.assertEqual(sum(g['entries'] for g in groups), 273)
        selected = next(g for g in groups if g['campaign'] == self.data['selected_campaign'])
        self.assertTrue(selected['eligible_next_batch'])
        self.assertLessEqual(selected['entries'], 12)
        self.assertNotEqual(selected['campaign'], 'third-coalition 1806')
        self.assertEqual(inv.select_campaign(list(reversed(groups))), selected['campaign'])


if __name__ == '__main__':
    unittest.main()
