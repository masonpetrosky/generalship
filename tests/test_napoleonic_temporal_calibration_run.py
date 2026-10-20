"""Constructed calibration/decision cases and authorization rejection only."""

import copy
import math
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from generalship import napoleonic_temporal_calibration as prep
from generalship import napoleonic_temporal_calibration_run as run
from generalship.baseline import sigmoid
from generalship.sources import digest, write_json
from test_napoleonic_temporal_calibration import constructed

ROOT = Path(__file__).resolve().parents[1]


class OffsetTests(unittest.TestCase):
    def test_convex_offset_score_objective_and_complement(self):
        zs, ys = [-2., -1., 1., 2.], [0, 0, 0, 1]
        fit = run.fit_offset(zs, ys); delta = fit['offset']
        self.assertLess(delta, 0)
        self.assertLess(abs(delta + sum(sigmoid(z + delta) - y for z, y in zip(zs, ys))), 1e-9)
        objective = lambda d: .5*d*d + sum(max(z+d, 0) + math.log1p(math.exp(-abs(z+d))) - y*(z+d)
                                          for z, y in zip(zs, ys))
        self.assertLess(objective(delta), objective(0))
        complement = run.fit_offset([-z for z in zs], [1-y for y in ys])
        self.assertAlmostEqual(complement['offset'], -delta)
        for constant in (0, 1):
            result = run.fit_offset([0.] * 10, [constant] * 10)
            self.assertTrue(math.isfinite(result['offset']))
            self.assertLess(abs(result['score_equation']), 1e-9)

    def test_invalid_offset_inputs_are_rejected(self):
        for zs, ys, ridge in [([], [], 1), ([0.], [0, 1], 1), ([math.nan], [1], 1),
                              ([0.], [.5], 1), ([0.], [1], 0)]:
            with self.subTest(zs=zs, ys=ys), self.assertRaises(ValueError):
                run.fit_offset(zs, ys, ridge)

    def test_test_labels_and_provenance_never_enter_fits(self):
        rows, labels = constructed(); protocol = prep.fixed_protocol()
        plan = {'folds': prep.folds(rows, rows, protocol)}
        first = run.evaluate(rows, labels, plan, protocol)
        changed = dict(labels, **{f'T{i}': 1-labels[f'T{i}'] for i in range(10)})
        second = run.evaluate(rows, changed, plan, protocol)
        self.assertEqual(first['parameters'], second['parameters'])
        self.assertEqual([{m:p[m] for m in prep.MODELS} for p in first['predictions']],
                         [{m:p[m] for m in prep.MODELS} for p in second['predictions']])
        poisoned = copy.deepcopy(rows)
        for row in poisoned:
            row['future_outcome_text'] = 'not a feature'
            row['sides']['A']['printed'] = 'not a numeric feature'
        self.assertEqual(first, run.evaluate(poisoned, labels, plan, protocol))
        fold = next(f for f in first['parameters'] if f['target_year'] == 1808)
        self.assertAlmostEqual(fold['expanding_prior'], 13/22)
        self.assertAlmostEqual(fold['recent_prior'], 8/12)
        self.assertGreater(fold['offset'], 0)
        ordered = sorted(first['predictions'], key=lambda p:p['same_base_force'])
        self.assertEqual([p['offset_force'] for p in ordered], sorted(p['offset_force'] for p in ordered))


def decision_fixture():
    metrics = {w:{m:{'log_loss': .5 if m == 'offset_force' else .6, 'brier': .2 if m == 'offset_force' else .25}
                  for m in prep.MODELS} for w in ('battle', 'equal_campaign')}
    p = {'regions': {'decision': {'metrics': metrics}, 'reused_1813_secondary': 'must not be inspected'},
         'per_year': {str(y): {'entries': 10, 'metrics': copy.deepcopy(metrics)} for y in range(1808, 1813)}}
    return {'primary': p, 'unqualified_totals': copy.deepcopy(p)}


class ContinuationTests(unittest.TestCase):
    def test_fixed_rule_and_1813_cannot_rescue_a_failure(self):
        protocol = prep.fixed_protocol(); results = decision_fixture()
        self.assertEqual(run.continuation(results, protocol)['status'], 'passes_exploratory_continuation_rule')
        results['primary']['regions']['decision']['metrics']['equal_campaign']['recent_prior']['log_loss'] = .4
        self.assertEqual(run.continuation(results, protocol)['status'], 'does_not_pass')
        results = decision_fixture()
        results['primary']['regions']['decision']['metrics']['battle']['same_base_force']['log_loss'] = .5 + 5e-13
        self.assertEqual(run.continuation(results, protocol)['status'], 'does_not_pass')
        bad = copy.deepcopy(protocol); bad['decision_years'][-1] = 1813
        with self.assertRaisesRegex(ValueError, '1813 cannot enter'):
            run.continuation(results, bad)
        results['primary']['regions']['reused_1813_secondary'] = {'arbitrary': 'excellent or terrible'}
        self.assertEqual(run.continuation(results, protocol)['status'], 'does_not_pass')

    def test_sensitivity_veto_year_consistency_and_missing_support(self):
        p = prep.fixed_protocol()
        results = decision_fixture()
        results['unqualified_totals']['regions']['decision']['metrics']['battle']['offset_force']['brier'] = .3
        self.assertEqual(run.continuation(results, p)['status'], 'does_not_pass')
        results = decision_fixture()
        for year in ('1808', '1809', '1810'):
            results['primary']['per_year'][year]['metrics']['battle']['offset_force']['log_loss'] = .7
        self.assertEqual(run.continuation(results, p)['status'], 'does_not_pass')
        del results['primary']['per_year']['1808']
        self.assertEqual(run.continuation(results, p)['status'], 'not_assessable')
        results = decision_fixture()
        results['primary']['regions']['decision']['metrics']['battle']['offset_force'] = None
        self.assertEqual(run.continuation(results, p)['status'], 'not_assessable')
        results = decision_fixture()
        results['primary']['per_year']['1808']['metrics']['battle']['offset_force'] = None
        self.assertEqual(run.continuation(results, p)['status'], 'not_assessable')


class AuthorizationTests(unittest.TestCase):
    def test_missing_authorization_rejects_before_outcome_access_and_every_fit(self):
        with patch.object(run, 'load_outcomes') as labels, patch.object(run, 'fit_logistic') as force, \
                patch.object(run, 'fit_offset') as offset:
            with self.assertRaisesRegex(ValueError, 'authorization required'):
                run.run(ROOT, None, prep.RESULT)
        labels.assert_not_called(); force.assert_not_called(); offset.assert_not_called()

    def test_bound_parser_and_invalid_approvals_use_only_constructed_temp_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_json(root / prep.PROPOSAL, {'fixture': 'No historical inputs exist in this root'})
            proposal = {'command': 'constructed-command', 'scope': 'constructed-only'}
            auth = {'kind': 'napoleonic_temporal_calibration_owner_run_authorization', 'approved': True,
                    'proposal_sha256': digest(root / prep.PROPOSAL), **proposal,
                    'owner_request': 'Constructed fixture, never an owner approval of historical work'}
            path = root / 'fixture.json'; write_json(path, auth)
            with patch.object(prep, 'validate_proposal', return_value=proposal):
                self.assertEqual(run.authorize(root, path), auth)
                for key, value in [('approved', False), ('proposal_sha256', '0'*64), ('command', 'wrong'),
                                   ('scope', 'wrong'), ('owner_request', '')]:
                    write_json(path, dict(auth, **{key: value}))
                    with patch.object(run, 'load_outcomes') as labels, patch.object(run, 'fit_logistic') as force, \
                            patch.object(run, 'fit_offset') as offset:
                        with self.assertRaisesRegex(ValueError, 'mismatched exact owner'):
                            run.run(root, path, prep.RESULT)
                    labels.assert_not_called(); force.assert_not_called(); offset.assert_not_called()
                write_json(path, auth)
                write_json(root / prep.RESULT, {'fixture': 'existing result must not be overwritten'})
                with patch.object(run, 'load_outcomes') as labels:
                    with self.assertRaisesRegex(ValueError, 'must not exist'):
                        run.run(root, path, prep.RESULT)
                    labels.assert_not_called()


if __name__ == '__main__':
    unittest.main()
