"""Source-measurement integrity, missingness and subset checks; no model jobs."""

import contextlib
import copy
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

from generalship import baseline
from generalship import napoleonic_losses as pilot
from generalship import napoleonic_temporal_calibration_run as model_job

ROOT = Path(__file__).resolve().parents[1]


class LossPilotTests(unittest.TestCase):
    def reject_parsed_change(self, path, change, message):
        read = pilot.read_json
        changed = copy.deepcopy(read(ROOT / path))
        change(changed)
        with patch.object(pilot, 'read_json', side_effect=lambda p: changed if p == ROOT / path else read(p)):
            with self.assertRaisesRegex(ValueError, message):
                pilot.build(ROOT)

    def test_complete_source_audit_reconciles_without_any_fitter(self):
        with patch.object(baseline, 'fit_logistic') as base, patch.object(model_job, 'fit_logistic') as force, \
                patch.object(model_job, 'fit_offset') as offset, patch.object(model_job, 'load_outcomes') as outcomes:
            data = pilot.build(ROOT)
        for function in (base, force, offset, outcomes):
            function.assert_not_called()
        p = data['profile']
        self.assertEqual((p['entries'], p['sides'], p['quantities']), (22, 44, 140))
        self.assertEqual((p['entry_passages'], p['convention_passages'], p['images_inspected']), (72, 7, 11))
        self.assertEqual((p['numeric_personnel_sides'], p['any_numeric_pairs']), (35, 14))
        self.assertEqual([(p['category_coverage'][c]['sides'], p['category_coverage'][c]['pairs'])
                          for c in pilot.ALL_RANKS], [(0, 0), (0, 0), (16, 6), (15, 1), (0, 0), (28, 10)])
        self.assertEqual(p['declared_composition_total_pairs'], ['B365c'])
        self.assertEqual(len(p['source_sum_checks']), 10)
        self.assertTrue(all(r['difference_people'] == 0 for r in p['source_sum_checks']))
        self.assertEqual(len(p['percent_checks']), 19)
        self.assertEqual(data['decision']['status'], 'no_go_for_one_whole_group_loss_grade')
        self.assertEqual(data['decision']['reserved_final_entries_used'], 0)

    def test_changed_frozen_record_rejects_before_loading(self):
        digest = pilot.digest
        with patch.object(pilot, 'digest', side_effect=lambda p: '0'*64 if p == ROOT / pilot.OBSERVATIONS else digest(p)), \
                patch.object(pilot, 'read_json') as read:
            with self.assertRaisesRegex(ValueError, 'changed frozen pilot record'):
                pilot.build(ROOT)
        read.assert_not_called()

    def test_undeclared_or_final_entry_cannot_change_the_frozen_group(self):
        final = pilot.read_json(ROOT / 'data/napoleonic/methods-v1/evaluation.json')['reserved_final'][0]
        self.reject_parsed_change(pilot.SCOPE, lambda d: d['entry_ids'].__setitem__(0, final), 'whole frozen development group')
        self.reject_parsed_change(pilot.OBSERVATIONS, lambda d: d['entries'].pop(), 'complete entry order')

    def test_empty_category_is_distinct_from_explicit_zero(self):
        blank = {'quantities': []}
        self.assertIsNone(pilot.whole_value(blank, 'killed'))
        quantity = {'id': 'fixture', 'category': 'killed', 'value': 0, 'unit': 'people', 'literal': '0 M.',
                    'population': 'whole_side', 'qualifier': 'reported_point', 'basis': 'printed_loss', 'evidence': ['fixture']}
        pilot.validate_quantity(quantity, {'fixture': {'quote': '0 M. tot'}}, ['killed'])
        self.assertEqual(pilot.whole_value({'quantities': [quantity]}, 'killed'), 0)
        self.assertIsNone(pilot.whole_value({'quantities': [quantity]}, 'wounded'))
        with self.assertRaisesRegex(ValueError, 'duplicate whole-side category'):
            pilot.whole_value({'quantities': [quantity, quantity]}, 'killed')

    def test_literal_unit_and_unknown_list_mutations_are_rejected(self):
        def literal(d):
            d['entries'][0]['sides']['A']['quantities'][0]['value'] += 1
        def unit(d):
            q = next(q for q in d['entries'][0]['sides']['B']['quantities'] if q['category'] == 'guns')
            q['unit'] = 'people'
        def unknown(d):
            d['entries'][0]['sides']['A']['unstated_all_ranks_categories'].remove('captured')
        for change, message in ((literal, 'literal/value mismatch'), (unit, 'material is not personnel'), (unknown, 'missing stays null')):
            with self.subTest(change=change.__name__):
                self.reject_parsed_change(pilot.OBSERVATIONS, change, message)

    def test_wrong_side_or_entry_quote_is_rejected(self):
        def side(d):
            d['entries'][2]['sides']['A']['source_column'] = 'winner'
        def quote(d):
            d['passages']['B363a:L2']['section'] = 'p364'
        self.reject_parsed_change(pilot.OBSERVATIONS, side, 'frozen side orientation')
        self.reject_parsed_change(pilot.OBSERVATIONS, quote, 'entry-anchored quotation')

    def test_nested_figures_are_not_added_or_promoted_to_whole_side(self):
        data = pilot.build(ROOT); entries = {e['battle_id']: e for e in data['observations']['entries']}
        hollabrunn = entries['B369a']['sides']['B']
        self.assertEqual(pilot.whole_value(hollabrunn, 'reported_personnel_total'), 3000)
        self.assertEqual(pilot.whole_value(hollabrunn, 'captured'), 1800)
        self.assertIsNone(pilot.whole_value(hollabrunn, 'killed_and_wounded'))
        self.assertEqual(pilot.whole_value(entries['B369c']['sides']['B'], 'reported_personnel_total'), 36000)
        self.assertIsNone(pilot.whole_value(entries['B368d']['sides']['B'], 'captured'))
        self.assertEqual(data['profile']['explicit_zero_all_ranks_observations'], 0)

    def test_capitulation_does_not_automatically_mean_captivity(self):
        q = {'id': 'fixture', 'category': 'captured', 'value': 4000, 'unit': 'people', 'literal': '4.000 M.',
             'population': 'whole_side', 'qualifier': 'reported_point', 'basis': 'narrative_explicit_captivity',
             'evidence': ['fixture']}
        with self.assertRaisesRegex(ValueError, 'captivity needs an explicit'):
            pilot.validate_quantity(q, {'fixture': {'quote': 'Kapitulation von 4.000 M.; frei abzuziehen.'}}, ['captured'])

    def test_direct_denominator_must_match_the_source_side(self):
        def wrong_column(d):
            entry = next(e for e in d['entries'] if e['battle_id'] == 'B368c')
            q = next(q for q in entry['sides']['A']['quantities'] if 'direct_source_denominator' in q)
            q['direct_source_denominator'].update(value=25000, literal='25.000')
        self.reject_parsed_change(pilot.OBSERVATIONS, wrong_column, 'direct denominator source column')
        data = pilot.build(ROOT)
        row = next(r for r in data['profile']['percent_checks'] if r['battle_id'] == 'B368c'
                   and r['side'] == 'A' and r['category'] == 'reported_personnel_total')
        self.assertEqual((row['printed_percent'], row['implied_percent'], row['printed_minus_implied_pp']), (88., 82.5, 5.5))

    def test_notebook_format_saved_outputs_and_top_to_bottom_execution(self):
        notebook = pilot.read_json(ROOT / pilot.NOTEBOOK)
        self.assertEqual((notebook['nbformat'], notebook['nbformat_minor']), (4, 5))
        self.assertEqual(notebook['metadata']['pilot_inputs'], pilot.build(ROOT)['input_sha256'])
        self.assertEqual(len(notebook['cells']), len({c['id'] for c in notebook['cells']}))
        namespace = {}; count = 0; previous_path = list(sys.path)
        try:
            with patch.object(baseline, 'fit_logistic') as fit, patch.object(model_job, 'fit_offset') as offset:
                for cell in notebook['cells']:
                    self.assertIn(cell['cell_type'], ('markdown', 'code'))
                    self.assertIsInstance(cell['metadata'], dict)
                    if cell['cell_type'] != 'code':
                        continue
                    count += 1; stdout = io.StringIO()
                    with contextlib.redirect_stdout(stdout):
                        exec(compile(''.join(cell['source']), 'loss-audit-notebook', 'exec'), namespace)
                    self.assertEqual(cell['execution_count'], count)
                    self.assertEqual(cell['outputs'], [{'output_type': 'stream', 'name': 'stdout',
                                                        'text': stdout.getvalue().splitlines(keepends=True)}])
            fit.assert_not_called(); offset.assert_not_called()
        finally:
            sys.path[:] = previous_path
        self.assertEqual(count, 4)


if __name__ == '__main__':
    unittest.main()
