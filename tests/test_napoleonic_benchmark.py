"""Preparation integrity and constructed evaluation only; no historical fit."""

import copy
import csv
import io
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

from generalship import napoleonic_benchmark as b
from generalship import napoleonic_benchmark_run as run
from generalship.sources import digest, read_json, write_json

ROOT = Path(__file__).resolve().parents[1]


class EncodingTests(unittest.TestCase):
    def test_same_number_in_a_loss_line_is_not_strength_provenance(self):
        record = {'text': ['Die X (4.000 M.) unter A über Y (8.000 M.).', 'Verluste: 4.000 M.'], 'pages': [1]}
        frame = {'id': 'T1', 'pages': [1]}
        sections = {'p1': '\n'.join(record['text'])}
        cites, table = b.passages_for('4.000 M.', 'left', record, sections, frame)
        self.assertFalse(table)
        self.assertEqual([c['quote'] for c in cites], [record['text'][0]])

    def test_artillery_position_is_structural_and_not_a_magnitude_heuristic(self):
        left = b.encode_strength('282 Gesch. 65.000', 'left', True)
        right = b.encode_strength('83.000 [1] Gesch. 300', 'right', True)
        self.assertEqual(left['primary_value'], 65000)
        self.assertEqual(right['primary_value'], 83000)
        self.assertEqual(right['footnote_markers'], ['1'])
        # Contrived reversed magnitudes prove this does not just choose the large number.
        self.assertEqual(b.encode_strength('900 Gesch. 100', 'left', True)['primary_value'], 100)
        self.assertEqual(b.encode_strength('100 Gesch. 900', 'right', True)['primary_value'], 100)
        self.assertEqual(b.encode_strength('175.000 [4] 717 Gesch.', 'right', True)['primary_value'], 175000)

    def test_unknowns_components_and_extraction_artifacts_never_become_totals(self):
        for text in (None, '7.000 Reiter', '4.800 Inft.', '5 Stürme', '58 Offz.', '36 Stck.', 'wor. 400 Offz.',
                     'wov. ca. 4.000 M. Kavallerie', '5.500 Inft., 1.500 Kav., 12 Kan.'):
            self.assertIsNone(b.encode_strength(text, 'left')['primary_value'], text)
        self.assertEqual(b.encode_strength(None, 'left')['disposition'], 'missing_extract')
        partial = b.encode_strength('7.000 Reiter', 'left')
        self.assertEqual(partial['quantities'][0]['value'], 7000)
        self.assertEqual(partial['quantities'][0]['basis'], 'Reiter')

    def test_phase_and_typographic_ambiguity_are_preserved(self):
        for text in ('urspr. 3.000 M.', 'noch 9.000 M. von 21.000 zu Beginn', '19.400 M. von 33.000',
                     'während der Blokade 3.000 M., gegen Ende der Belagerung 12.000 M.'):
            r = b.encode_strength(text, 'left')
            self.assertIsNone(r['primary_value'])
            self.assertEqual(r['phase'], 'explicit_phase_or_multiple_states')
            self.assertEqual(r['printed'], text)
        r = b.encode_strength('ca. 10.0000 M.', 'left')
        self.assertIsNone(r['primary_value'])
        self.assertIn('malformed_numeric_notation', r['reasons'])
        self.assertIsNone(r['quantities'][0]['value'])

    def test_explicit_total_does_not_add_components_again_or_invent_an_error_band(self):
        r = b.encode_strength('4.000 Inft., 300 Kav. = 4.300 M.', 'right')
        self.assertEqual(r['primary_value'], 4300)
        self.assertEqual([q['value'] for q in r['quantities']], [4000, 300, 4300])
        approx = b.encode_strength('ca. 12.000 M.', 'left')
        self.assertEqual(approx['primary_value'], 12000)
        self.assertTrue(approx['approximate'])
        self.assertNotIn('standard_error', approx)


class PreparedTests(unittest.TestCase):
    def test_reproduces_exact_scope_and_all_denominators(self):
        result = b.check(ROOT)
        self.assertEqual(result['development_entries'], 273)
        self.assertEqual(result['sides'], 546)
        data = read_json(ROOT / (b.ARTIFACT + '.json'))
        scope = read_json(ROOT / b.SCOPE)
        self.assertEqual([r['battle_id'] for r in data['entries']], scope['development_ids'])
        self.assertFalse(set(scope['reserved_final_ids']) & {r['battle_id'] for r in data['entries']})
        self.assertEqual(len({r['campaign_group'] for r in data['entries']}), 13)
        for row in data['entries']:
            self.assertEqual(set(row['sides']), {'A', 'B'})
            self.assertNotIn('outcome_side_a', row)
            self.assertNotIn('y', row)
            self.assertEqual(row['eligible'], all(r['primary_value'] is not None for r in row['sides'].values()))
        csv_rows = list(csv.DictReader(io.StringIO(b.flat_csv(data))))
        self.assertEqual(len(csv_rows), 546)
        self.assertEqual(len({(r['battle_id'], r['side']) for r in csv_rows}), 546)
        self.assertEqual(sum(r['disposition'] == 'eligible' for r in csv_rows), 432)
        self.assertTrue(all(r['primary_unit'] == 'people' for r in csv_rows if r['disposition'] == 'eligible'))
        self.assertTrue(all(r['primary_value'] == '' for r in csv_rows if r['disposition'] != 'eligible'))
        self.assertFalse(result['historical_outcomes_fitted'])
        self.assertTrue(data['provenance_can_reveal_outcomes'])
        self.assertEqual(data['feature_whitelist'], ['sides.A.primary_value', 'sides.B.primary_value'])
        before = [(ROOT / p).exists() for p in (b.BASE + '/owner-run-authorization.json', run.OUTPUT)]
        with patch.object(run, 'load_outcomes') as labels, patch.object(run, 'fit_logistic') as fit:
            b.check(ROOT)
            labels.assert_not_called(); fit.assert_not_called()
        self.assertEqual(before, [(ROOT / p).exists() for p in (b.BASE + '/owner-run-authorization.json', run.OUTPUT)])

    def test_sensitivity_filters_change_population_without_changing_values(self):
        data = read_json(ROOT / (b.ARTIFACT + '.json'))
        original = copy.deepcopy(data)
        for pop in b.fixed_protocol()['populations']:
            selected = b.population_rows(data, pop)
            self.assertTrue(all(r['eligible'] for r in selected))
            self.assertTrue({r['battle_id'] for r in selected} <= {r['battle_id'] for r in data['entries']})
        self.assertEqual(data, original)

    def test_external_strength_notes_are_retained_without_selecting_engaged_counts(self):
        data = read_json(ROOT / (b.ARTIFACT + '.json'))
        rows = {r['battle_id']: r for r in data['entries']}
        for battle, expected in [('B434a', 33000), ('B435a', 40000)]:
            row = rows[battle]
            self.assertTrue(row['eligible'])
            selected = next(s for s in row['sides'].values() if s['primary_value'] == expected)
            self.assertEqual(selected['footnote_markers'], [])
            self.assertIn('1', selected['context_footnote_markers'])
            self.assertTrue(selected['footnotes'])
            self.assertNotIn(battle, {r['battle_id'] for r in b.population_rows(data, 'unqualified_totals')})

    def test_changed_proposal_binding_fails_closed(self):
        actual = read_json(ROOT / b.PROPOSAL)
        bad = copy.deepcopy(actual)
        bad['bindings'][b.CODE] = '0' * 64
        with patch.object(b, 'read_json', return_value=bad):
            with self.assertRaisesRegex(ValueError, 'changed proposal'):
                b.validate_proposal(ROOT)

    def test_reproduction_restores_only_the_exact_frozen_output_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            proposal = read_json(ROOT / b.PROPOSAL)
            scope = read_json(ROOT / b.SCOPE)
            snapshot = read_json(ROOT / b.SNAPSHOT)
            paths = set(proposal['bindings']) | set(scope['bindings']) | {b.PROPOSAL, 'data/sources.json'}
            paths |= {s['path'] for s in snapshot['sources']}
            paths -= {b.ARTIFACT + suffix for suffix in ('.json', '.csv', '.md')}
            for path in paths:
                (root / path).parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / path, root / path)
            b.write_artifacts(root)
            self.assertEqual(b.check(root)['eligible_pairs'], 194)
            report = root / (b.ARTIFACT + '.md')
            report.write_text('corrupt generated output')
            b.write_artifacts(root)
            self.assertEqual(digest(report), proposal['bindings'][b.ARTIFACT + '.md'])
            with patch.object(b, 'flat_csv', return_value='wrong new dataset'):
                with self.assertRaisesRegex(ValueError, 'differs from frozen proposal'):
                    b.write_artifacts(root)
            self.assertEqual(digest(report), proposal['bindings'][b.ARTIFACT + '.md'])


def constructed():
    rows = []
    for i in range(9):
        group = f'war-{i // 3} {1811 + i // 3}'
        rows.append({'battle_id': f'T{i}', 'campaign_group': group, 'war': f'war-{i // 3}',
                     'start_year': 1811 + i // 3, 'sides': {'A': {'primary_value': 100 + 20 * i},
                                                        'B': {'primary_value': 180}}, 'eligible': True})
    scope = {'development_groups': {r['campaign_group']: [s['battle_id'] for s in rows
                                                        if s['campaign_group'] == r['campaign_group']] for r in rows}}
    labels = {f'T{i}': i % 2 for i in range(9)}
    return rows, labels, scope


class RunnerTests(unittest.TestCase):
    def test_missing_authorization_stops_before_labels_and_fit(self):
        with patch.object(run, 'load_outcomes') as labels, patch.object(run, 'fit_logistic') as fit:
            with self.assertRaisesRegex(ValueError, 'authorization required'):
                run.run(ROOT, None, run.OUTPUT)
            labels.assert_not_called(); fit.assert_not_called()

    def test_false_or_wrong_authorization_cannot_reach_labels(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'unapproved-test-only.json'
            proposal = read_json(ROOT / b.PROPOSAL)
            template = {'kind': 'napoleonic_benchmark_owner_run_authorization', 'approved': True,
                        'proposal_sha256': digest(ROOT / b.PROPOSAL), 'command': proposal['command'],
                        'scope': proposal['scope'], 'owner_request': 'Constructed invalid test fixture only'}
            for field, value in [('approved', False), ('proposal_sha256', '0' * 64), ('command', 'wrong'),
                                 ('scope', 'wrong'), ('owner_request', '')]:
                body = dict(template, **{field: value})
                write_json(path, body)
                with patch.object(run, 'load_outcomes') as labels, patch.object(run, 'fit_logistic') as fit:
                    with self.assertRaisesRegex(ValueError, 'mismatched exact owner'):
                        run.run(ROOT, path, run.OUTPUT)
                    labels.assert_not_called(); fit.assert_not_called()

    def test_authorization_parser_accepts_only_a_bound_constructed_fixture(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); proposal = root / b.PROPOSAL
            write_json(proposal, {'fixture': 'No historical inputs exist in this temporary root'})
            auth = {'kind': 'napoleonic_benchmark_owner_run_authorization', 'approved': True,
                    'proposal_sha256': digest(proposal), 'command': 'constructed-command', 'scope': 'constructed-only',
                    'owner_request': 'Constructed fixture, never used to run or approve historical data'}
            path = root / 'fixture.json'; write_json(path, auth)
            with patch.object(b, 'validate_proposal', return_value={'command': auth['command'], 'scope': auth['scope']}):
                self.assertEqual(run.authorize(root, path), auth)

    def test_constructed_folds_are_held_out_and_use_training_only_prior(self):
        rows, labels, scope = constructed()
        protocol = b.fixed_protocol(); protocol['bootstrap']['draws'] = 30
        for evaluation in protocol['evaluations']:
            result = run.evaluate(rows, labels, scope, protocol, evaluation)
            for fold in result['folds']:
                self.assertFalse(set(fold['train_ids']) & set(fold['test_ids']))
                if fold['status'] == 'scored':
                    self.assertEqual(fold['training_prior'], (sum(labels[i] for i in fold['train_ids']) + 1)
                                     / (len(fold['train_ids']) + 2))
            self.assertEqual(result['scored_entries'], 3 if evaluation == 'forward_1813' else 9)
        # Metadata is not a numeric feature, even if it contains an outcome-like value.
        expected = run.evaluate(rows, labels, scope, protocol, 'leave_campaign_out')
        poisoned = copy.deepcopy(rows)
        for row in poisoned:
            row['source_result'] = 'future outcome text'
            row['sides']['A']['printed'] = 'Do not use text as a feature'
            row['sides']['A']['source_column'] = 'outcome-bearing provenance, never a feature'
        self.assertEqual(expected, run.evaluate(poisoned, labels, scope, protocol, 'leave_campaign_out'))

    def test_unequal_groups_keep_weightings_and_bootstrap_distinct(self):
        predictions = [{'held_out_group': 'small', 'force': 0.9, 'training_prior': 0.5, 'y': 1}] + [
            {'held_out_group': 'large', 'force': 0.9, 'training_prior': 0.5, 'y': 0} for i in range(9)]
        self.assertNotEqual(run.metrics(predictions, 'force', 'battle'), run.metrics(predictions, 'force', 'equal_group'))
        design = b.fixed_protocol()['bootstrap']; design['draws'] = 60
        self.assertEqual(run.bootstrap(predictions, 'training_prior', design), run.bootstrap(predictions, 'training_prior', design))
        self.assertEqual(sum(r['n'] for r in run.calibration(predictions, 'force', 'battle', [0, 0.5, 1])), 10)
        self.assertEqual(run.bootstrap(predictions[:1], 'training_prior', design)['status'], 'not_estimable')


if __name__ == '__main__':
    unittest.main()
