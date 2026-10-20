"""Contract examples use real pinned passages; positive gate fixtures below are synthetic."""

from copy import deepcopy
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

from generalship import napoleonic_ledger_design as ledger
from generalship.sources import digest, read_json, write_json

ROOT = Path(__file__).resolve().parents[1]


class LedgerDesignTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bundle = read_json(ROOT / ledger.EXAMPLES)

    def fixture(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        paths = {ledger.SCOPE, ledger.EXAMPLES, ledger.SNAPSHOT, ledger.DESIGN, ledger.VERIFICATION}
        paths.update(read_json(ROOT / ledger.SCOPE)['bindings'])
        paths.update(s['path'] for s in read_json(ROOT / ledger.SNAPSHOT)['sources'])
        for path in paths:
            (root / path).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / path, root / path)
        return root

    def synthetic_strength(self, key='synthetic-component'):
        # Pure-gate fixture only. No source, identity or historical verification is invented.
        row = deepcopy(self.bundle['strength_records'][0])
        row.update(id=key, basis='all_arms', population='whole_side',
                   boundary_relation='before', derivation='direct_reported')
        row['amount'].update(kind='point', lower=100, upper=100)
        return row

    def test_committed_bundle_coverage_and_primary_bindings(self):
        report = ledger.check(ROOT)
        self.assertEqual((report['engagements'], report['sides'], report['indexed_claims']), (4, 8, 31))
        self.assertEqual((report['strength_observations'], report['command_observations']), (43, 28))
        self.assertEqual(report['strength_status_counts'], {'blocked': 18, 'excluded': 25})
        self.assertEqual(report['command_status_counts'], {'blocked': 28})
        self.assertEqual((report['distinct_cited_passages'], len(report['inspected_image_ids'])), (46, 26))
        self.assertEqual((report['unknown_army_ids'], report['unresolved_opening_boundaries']), (8, 8))
        self.assertEqual(report['emitted_model_rows'], [])
        self.assertFalse(report['historical_outcomes_fitted'])
        self.assertEqual(report['calibration'], 'prepared_unscored')
        self.assertTrue(all(r['opening_strength'] == r['opening_responsibility'] == 'blocked'
                            for r in report['side_coverage']))

    def test_selection_ignores_outcomes_and_strength_availability(self):
        entries = read_json(ROOT / ledger.FRAME)['entries']
        development = set(read_json(ROOT / ledger.EVALUATION)['development'])
        expected = ledger.selected_group(entries, development)
        changed = deepcopy(entries)
        for row in changed:
            row.update(outcome_side_a='invented-test-value', winner_strength_printed=None,
                       loser_strength_printed='999999999', winner_commander_text='famous-test-name')
        self.assertEqual(ledger.selected_group(changed, development), expected)
        self.assertEqual(expected, ('third-coalition 1806', ['B370c', 'B370d', 'B371a', 'B379c']))

    def test_read_only_cli_reports_zero_emitted_rows(self):
        paths = [ledger.SCOPE, ledger.EXAMPLES, ledger.SNAPSHOT, ledger.VERIFICATION]
        before = {p: digest(ROOT / p) for p in paths}
        process = subprocess.run([sys.executable, '-m', 'generalship', 'napoleonic-ledger-design-check'],
                                 cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(process.returncode, 0, process.stderr)
        result = json.loads(process.stdout)
        self.assertEqual(result['emitted_model_rows'], [])
        self.assertEqual(result['unresolved_opening_boundaries'], 8)
        self.assertEqual(before, {p: digest(ROOT / p) for p in paths})

    def test_bound_partition_and_sample_cannot_migrate(self):
        root = self.fixture()
        scope = read_json(root / ledger.SCOPE)
        scope['battle_ids'][0] = 'B487a'  # reserved final-set entry, never a design case
        write_json(root / ledger.SCOPE, scope)
        with self.assertRaises(ValueError):
            ledger.validate(root)

    def test_missing_or_duplicate_side_and_omitted_claim_fail(self):
        for field in ('side_records', 'claim_index'):
            bundle = deepcopy(self.bundle)
            bundle[field].pop()
            with self.subTest(field=field), self.assertRaises(ValueError):
                ledger.validate(ROOT, bundle)
        bundle = deepcopy(self.bundle)
        bundle['side_records'].append(deepcopy(bundle['side_records'][0]))
        with self.assertRaises(ValueError):
            ledger.validate(ROOT, bundle)

    def test_frozen_cross_year_interval_preserved(self):
        bundle = deepcopy(self.bundle)
        row = next(r for r in bundle['side_records'] if r['battle_id'] == 'B379c')
        self.assertEqual((row['frozen_start_date'], row['frozen_end_date']), ('1806-12-18', '1807-02-06'))
        row['frozen_end_date'] = '1806-12-31'
        with self.assertRaisesRegex(ValueError, 'frozen interval'):
            ledger.validate(ROOT, bundle)

    def test_colletta_initial_assault_month_is_not_an_invented_pre18_date(self):
        strength = next(r for r in self.bundle['strength_records'] if r['id'] == 'B379c-A-colletta-initial-attempt')
        role = next(r for r in self.bundle['command_records'] if r['id'] == 'B379c-A-command-colletta-verdier')
        self.assertEqual((strength['population'], role['population']), ('unresolved', 'unresolved'))
        self.assertEqual((strength['boundary_relation'], role['boundary_relation']), ('unestablished', 'unestablished'))
        self.assertIn('qualifies the bound dossier', strength['note'])

    def test_old_replay_does_not_read_latest_registry(self):
        root = self.fixture()
        expected = ledger.check(root)
        write_json(root / 'data/sources.json', {'sources': [{'id': 'unrelated-later-entry'}]})
        self.assertEqual(ledger.check(root), expected)

    def test_changed_raw_bytes_fail(self):
        root = self.fixture()
        source = read_json(root / ledger.SNAPSHOT)['sources'][0]
        path = root / source['path']
        path.write_bytes(path.read_bytes() + b'\n')
        with self.assertRaisesRegex(ValueError, 'source raw checksum'):
            ledger.validate(root)

    def test_changed_metadata_with_same_raw_hash_fails(self):
        root = self.fixture()
        snapshot = read_json(root / ledger.SNAPSHOT)
        sid = self.bundle['strength_records'][0]['evidence'][0]['citation']['source_id']
        source = next(s for s in snapshot['sources'] if s['id'] == sid)
        source['dependency_note'] = 'Changed metadata with original raw bytes'
        write_json(root / ledger.SNAPSHOT, snapshot)
        bundle = deepcopy(self.bundle)
        bundle['source_snapshot']['sha256'] = digest(root / ledger.SNAPSHOT)
        with self.assertRaisesRegex(ValueError, 'metadata/raw binding'):
            ledger.validate(root, bundle)

    def test_citation_cannot_borrow_another_claim_or_section(self):
        bundle = deepcopy(self.bundle)
        ref = bundle['strength_records'][0]['evidence'][0]
        ref['citation']['section'] = 'p371'
        with self.assertRaisesRegex(ValueError, 'citation differs'):
            ledger.validate(ROOT, bundle)

    def test_null_document_date_cannot_borrow_dated_capitulation(self):
        bundle = deepcopy(self.bundle)
        ref = next(e for r in bundle['strength_records'] for e in r['evidence']
                   if e['citation']['source_id'] == 'koch-massena-t5-p223-figures-v1')
        self.assertIsNone(ref['document_date'])
        ref['document_date'] = '1806-07-18'
        with self.assertRaisesRegex(ValueError, 'section document date'):
            ledger.validate(ROOT, bundle)
        dated = next(e for r in self.bundle['command_records'] for e in r['evidence']
                     if e['citation']['source_id'] == 'koch-massena-t5-p422-figures-v1')
        self.assertEqual(dated['document_date'], '1806-07-18')

    def test_quantity_edit_invalidates_actual_primary_record(self):
        root = self.fixture()
        bundle = deepcopy(self.bundle)
        bundle['strength_records'][0]['amount'].update(lower=999, upper=999)
        write_json(root / ledger.EXAMPLES, bundle)
        # Quote matching cannot establish numerical entailment; an altered proposal
        # must not inherit the primary's verification of the original bytes.
        with self.assertRaisesRegex(ValueError, 'stale input/code bindings'):
            ledger.check(root)

    def test_no_boundary_identity_selection_promotion_or_calibration_escape(self):
        variants = []
        for field, value in [('emitted_rows', [{'invented': True}]), ('status', 'admitted'),
                             ('calibration', 'scored'), ('historical_outcomes_fitted', True)]:
            bundle = deepcopy(self.bundle)
            bundle[field] = value
            variants.append(bundle)
        for field, value in [('opening_boundary', '1806-03-09'), ('selected_strength_id', 'anything'),
                             ('army_id', 'same-general-same-army'), ('responsible_person_id', 'highest-rank')]:
            bundle = deepcopy(self.bundle)
            bundle['side_records'][0][field] = value
            variants.append(bundle)
        for bundle in variants:
            with self.subTest(), self.assertRaises(ValueError):
                ledger.validate(ROOT, bundle)

    def test_one_sided_bounds_and_approximate_precision_preserved(self):
        rows = {r['id']: r for r in self.bundle['strength_records']}
        self.assertEqual(rows['B371a-A-koch-lacour-bound']['amount']['upper'], 2400)
        self.assertTrue(rows['B371a-A-koch-lacour-bound']['amount']['upper_inclusive'])
        self.assertIsNone(rows['B371a-A-koch-lacour-bound']['amount']['lower'])
        self.assertFalse(rows['B371a-B-koch-garrison-bound']['amount']['upper_inclusive'])
        self.assertFalse(rows['B370d-A-bunbury-more-than']['amount']['lower_inclusive'])
        for key, change in [('B371a-A-koch-lacour-bound', {'lower': 1, 'lower_inclusive': True}),
                            ('B370d-A-bunbury-engaged', {'lower': 6000, 'upper': 6600})]:
            row = deepcopy(rows[key])
            row['amount'].update(change)
            with self.subTest(key=key), self.assertRaises(ValueError):
                ledger.validate_amount(row['amount'])

    def test_bad_numeric_values_and_unit_substitution_fail(self):
        for value in [True, float('nan'), -1]:
            row = self.synthetic_strength()
            row['amount'].update(lower=value, upper=value)
            with self.subTest(value=value), self.assertRaises(ValueError):
                ledger.validate_amount(row['amount'])
        bundle = deepcopy(self.bundle)
        row = next(r for r in bundle['strength_records'] if r['basis'] == 'guns')
        row['unit'] = 'people'
        with self.assertRaisesRegex(ValueError, 'unit/basis mismatch'):
            ledger.validate(ROOT, bundle)

    def test_synthetic_technical_eligibility_is_not_admission(self):
        row = self.synthetic_strength()
        # A late document can refer to clean earlier state; no gate uses its date as state.
        row['evidence'][0]['document_date'] = '1854-01-01'
        result = ledger.strength_decision(row, {'synthetic_contact': 'test-only'})
        self.assertEqual(result['status'], 'eligible_candidate')
        self.assertNotIn('admitted', result.values())
        self.assertEqual(ledger.strength_decision(row, None)['status'], 'blocked')

    def test_leakage_and_partial_basis_remain_excluded_with_all_reasons(self):
        for updates in [{'derivation': 'post_state'}, {'basis': 'reported_engaged'},
                        {'basis': 'rank_and_file'}, {'boundary_relation': 'after'},
                        {'derivation': 'illustrative'}]:
            row = self.synthetic_strength()
            row.update(updates)
            result = ledger.strength_decision(row, None)
            self.assertEqual(result['status'], 'excluded')
            self.assertIn('opening_boundary_unestablished', result['blocked_reasons'])

    def test_arithmetic_does_not_establish_concurrent_or_complete_population(self):
        report = ledger.validate(ROOT)
        self.assertEqual(report['sum_proposals']['amantea-columns']['arithmetic_sum'], 4700)
        self.assertEqual(report['sum_proposals']['amantea-columns']['status'], 'blocked')
        self.assertIn('common_state_time_unestablished', report['sum_proposals']['amantea-columns']['blocked_reasons'])
        maida = report['sum_proposals']['maida-missing-artillery-personnel']
        self.assertEqual((maida['arithmetic_sum'], maida['status']), (4800, 'excluded'))
        self.assertIn('incomplete_target_population', maida['excluded_reasons'])

    def test_synthetic_sum_allows_disjoint_components_but_rejects_overlap_and_leakage(self):
        left, right = self.synthetic_strength('synthetic-left'), self.synthetic_strength('synthetic-right')
        for row in (left, right):
            row['population'] = 'component'
        records = {r['id']: r for r in (left, right)}
        proposal = {'battle_id': left['battle_id'], 'side': left['side'], 'input_ids': list(records),
                    'arithmetic_sum': 200, 'disjoint_membership': 'established',
                    'same_state_time': 'established', 'complete_target': 'complete'}
        self.assertEqual(ledger.sum_decision(proposal, records, {'synthetic': True})['status'], 'eligible_candidate')
        proposal['disjoint_membership'] = 'overlap'
        self.assertEqual(ledger.sum_decision(proposal, records, {'synthetic': True})['status'], 'excluded')
        proposal['disjoint_membership'] = 'established'
        left['derivation'] = 'post_state'
        self.assertEqual(ledger.sum_decision(proposal, records, {'synthetic': True})['status'], 'excluded')

    def test_sum_cannot_hide_nested_graphs_cross_sides_or_invent_results(self):
        for change in [{'input_ids': ['amantea-columns', 'B379c-A-koch-verdier']},
                       {'input_ids': ['B379c-A-koch-huard', 'B379c-B-bodart']},
                       {'arithmetic_sum': 4800}]:
            proposal = deepcopy(self.bundle['sum_proposals'][0])
            proposal.update(change)
            with self.subTest(change=change), self.assertRaises(ValueError):
                ledger.sum_decision(proposal, ledger.indexed(self.bundle['strength_records']), None)

    def test_command_labels_cannot_automatically_resolve_authority(self):
        row = deepcopy(self.bundle['command_records'][0])
        result = ledger.command_decision(row, {'synthetic': True})
        self.assertEqual(result['status'], 'blocked')
        self.assertIn('person_identity_unresolved', result['blocked_reasons'])
        self.assertIn('target_authority_unestablished', result['blocked_reasons'])
        bundle = deepcopy(self.bundle)
        bundle['command_records'][0]['resolved_person_id'] = 'famous-commander'
        with self.assertRaisesRegex(ValueError, 'does not resolve identities'):
            ledger.validate(ROOT, bundle)


if __name__ == '__main__':
    unittest.main()
