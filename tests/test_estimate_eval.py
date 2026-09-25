"""Estimate-layer evaluation gate and row assembly (docs/strength-estimates.md §6), on invented rows."""

import json
from pathlib import Path
import tempfile
import unittest

from generalship.baseline import fit_logistic
from generalship.estimate_eval import DEFAULT_AUTHORIZATION, FROZEN_REFERENCE, assemble, authorize, evaluable, fit_set
from generalship.estimates import DEFAULT_LEDGER, EstimateError
from generalship.sources import digest


def side(grade, point, labels=()):
    if point is None:
        return {'grade': grade, 'point': None, 'low': None, 'high': None, 'labels': list(labels), 'exact': None}
    return {'grade': grade, 'point': point, 'low': point - 10, 'high': point + 10, 'labels': list(labels),
            'exact': {'point': str(point)}}


def record(bid, campaign, winner='Union'):
    return {'battle_id': bid, 'name': bid, 'campaign': campaign, 'source_result': winner, 'baseline_eligible': False}


class GateTests(unittest.TestCase):
    def write(self, root, ledger_hash, option='a_exploratory_estimate_layer_diagnostic'):
        (root / 'data/estimates').mkdir(parents=True)
        (root / DEFAULT_LEDGER).write_text('{}\n')
        auth = {'kind': 'estimate_evaluation_authorization', 'ledger_path': DEFAULT_LEDGER,
                'ledger_sha256': ledger_hash or digest(root / DEFAULT_LEDGER), 'option': option,
                'admits_feature': False, 'changes_baseline': False}
        (root / DEFAULT_AUTHORIZATION).write_text(json.dumps(auth))

    def test_authorization_must_name_the_current_ledger(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write(root, None)
            self.assertEqual(authorize(root)[1], digest(root / DEFAULT_LEDGER))
            (root / DEFAULT_LEDGER).write_text('{"changed": true}\n')
            with self.assertRaisesRegex(EstimateError, 'different ledger hash'):
                authorize(root)

    def test_record_must_disclaim_admission_and_baseline_change(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write(root, None)
            auth = json.loads((root / DEFAULT_AUTHORIZATION).read_text())
            (root / DEFAULT_AUTHORIZATION).write_text(json.dumps(auth | {'changes_baseline': True}))
            with self.assertRaisesRegex(EstimateError, 'baseline'):
                authorize(root)

    def test_only_option_a_is_implemented(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write(root, None, option='b_admission_profile')
            with self.assertRaisesRegex(EstimateError, 'option'):
                authorize(root)


class RowTests(unittest.TestCase):
    def test_post_start_rows_are_counted_not_fitted(self):
        estimates = {'X1': {'US': side('A', 100), 'Confederate': side('B', 90)},
                     'X2': {'US': side('A', 100, ['post_start_information']), 'Confederate': side('A', 90)},
                     'X3': {'US': side('D', None), 'Confederate': side('A', 90)}}
        rows, excluded, any_excluded = assemble(estimates, [record('X1', 'c1'), record('X2', 'c1'), record('X3', 'c2')])
        self.assertEqual([r['battle_id'] for r in rows['set2_AB']], ['X1'])
        self.assertEqual(rows['set1_A'], [])
        self.assertEqual((excluded['set1_A'], any_excluded), (['X2'], ['X2']))

    def test_evaluability_needs_six_rows_three_campaigns_and_both_outcomes(self):
        rows = [{'campaign': f'c{i % 3}', 'union_outcome': i % 2, 'estimate': {}} for i in range(6)]
        self.assertTrue(evaluable(rows)[0])
        self.assertFalse(evaluable(rows[:5])[0])
        self.assertFalse(evaluable([dict(r, union_outcome=1) for r in rows])[0])
        self.assertFalse(evaluable([dict(r, campaign='c0') for r in rows])[0])

    def test_fit_set_scores_every_row_once_out_of_campaign(self):
        rows = [{'battle_id': f'B{i}', 'name': '', 'campaign': f'c{i % 3}', 'union_outcome': int(i < 4),
                 'estimate': {'US': side('A', 1000 + 100 * i), 'Confederate': side('A', 1500)}} for i in range(8)]
        result = fit_set(rows)
        self.assertEqual(sorted(p['battle_id'] for p in result['predictions']), sorted(r['battle_id'] for r in rows))
        self.assertEqual(len(result['folds']), 3)
        self.assertIn('diagnostic_union_score', result['predictions'][0])
        self.assertNotIn('p_union_win', result['predictions'][0])


class ReferenceTests(unittest.TestCase):
    def test_frozen_reference_matches_the_committed_baseline(self):
        baseline = json.loads((Path(__file__).resolve().parents[1] / 'artifacts/baseline.json').read_text())
        self.assertEqual(FROZEN_REFERENCE['battle_weighted_brier'], baseline['battle_weighted_metrics']['strength_logistic']['brier'])
        self.assertEqual(FROZEN_REFERENCE['campaign_weighted_brier'], baseline['campaign_weighted_metrics']['strength_logistic']['brier'])
        self.assertEqual(baseline['n_battles'], 23)


class OptimizerTests(unittest.TestCase):
    def test_converges_where_the_line_search_only_sees_rounding(self):
        # A held-out fold of the estimate evaluation: before the Newton-decrement stop, the
        # line search stalled at the optimum and the fit raised "did not converge".
        xs = [0.14093959731543623, 0.42857142857142855, 0.16451463074779377, -0.21739130434782608,
              -0.5151515151515151, -0.4583333333333333, -0.4925373134328358, 0.15946901628891078,
              0.3821138211382114, 0.04, -0.47783251231527096, -0.4222222222222222, 0.32947976878612717,
              -0.2631578947368421, -0.28205128205128205]
        ys = [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]
        model = fit_logistic(xs, ys)
        ga = model.intercept + sum(model.predict(x) - y for x, y in zip(xs, ys))
        gb = model.slope + sum((model.predict(x) - y) * x for x, y in zip(xs, ys))
        self.assertLess(max(abs(ga), abs(gb)), 1e-9)  # the ridge-penalized gradient vanishes
        self.assertAlmostEqual(model.intercept, -0.08619521973923545, places=12)
        self.assertAlmostEqual(model.slope, 0.2471571457725098, places=12)


if __name__ == '__main__':
    unittest.main()
