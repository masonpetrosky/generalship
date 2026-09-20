import copy
import math
import unittest
from pathlib import Path

from generalship.baseline import advantage, evaluate, fit_logistic, scores, sigmoid
from generalship.dataset import build_dataset

ROOT = Path(__file__).resolve().parents[1]


class BaselineTests(unittest.TestCase):
    def test_equal_strength_balanced_results(self):
        model = fit_logistic([0, 0, 0, 0], [0, 1, 0, 1])
        self.assertAlmostEqual(model.predict(0), .5)
        self.assertEqual(model.slope, 0)

    def test_more_strength_predicts_win_in_controlled_data(self):
        model = fit_logistic([-0.8, -0.5, -0.2, 0.2, 0.5, 0.8], [0, 0, 0, 1, 1, 1])
        self.assertGreater(model.slope, 0)
        self.assertLess(model.predict(-.5), model.predict(.5))
        self.assertAlmostEqual(model.predict(-.5), 1-model.predict(.5))

    def test_side_relabeling_is_equivariant(self):
        xs, ys = [-.7, -.3, .1, .4, .9], [0, 1, 1, 0, 1]
        original = fit_logistic(xs, ys)
        swapped = fit_logistic([-x for x in xs], [1-y for y in ys])
        for x in xs:
            self.assertAlmostEqual(original.predict(x), 1-swapped.predict(-x), places=9)

    def test_fit_satisfies_penalized_score_equations(self):
        xs, ys = [-.8, -.5, .1, .3, .7, .9], [0, 1, 0, 1, 1, 1]
        model = fit_logistic(xs, ys)
        self.assertAlmostEqual(sum(model.predict(x)-y for x,y in zip(xs,ys))+model.intercept, 0, places=7)
        self.assertAlmostEqual(sum((model.predict(x)-y)*x for x,y in zip(xs,ys))+model.slope, 0, places=7)

    def test_single_class_training_remains_finite(self):
        model = fit_logistic([0, .2, .4], [1, 1, 1])
        self.assertTrue(.5 < model.predict(.3) < 1)
        self.assertEqual(sigmoid(-1000), 0)
        self.assertEqual(sigmoid(1000), 1)

    def test_missing_zero_nonfinite_strength_rejected(self):
        for own in [0, -1, float('nan'), float('inf')]:
            with self.assertRaises(ValueError): advantage(own, 100)

    def test_proper_scores_known_values(self):
        result = scores([{'p': .5, 'union_outcome': 0}, {'p': .5, 'union_outcome': 1}], 'p')
        self.assertEqual(result['brier'], .25)
        self.assertAlmostEqual(result['log_loss'], math.log(2))

    def test_invalid_fit_inputs_rejected(self):
        for xs, ys, penalty in [([], [], 1), ([0], [], 1), ([float('nan')], [1], 1),
                                ([0], [.5], 1), ([0], [1], 0), ([0], [1], float('inf'))]:
            with self.assertRaises(ValueError): fit_logistic(xs, ys, penalty)

    def test_complete_campaign_holdout_and_one_prediction_per_battle(self):
        records, _ = build_dataset(ROOT)
        result = evaluate(records)
        eligible = {r['battle_id']:r for r in records if r['baseline_eligible']}
        ids = [p['battle_id'] for p in result['predictions']]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), set(eligible))
        for fold in result['folds']:
            train, test = set(fold['train_battle_ids']), set(fold['test_battle_ids'])
            self.assertFalse(train & test)
            self.assertEqual(train | test, set(eligible))
            self.assertEqual({eligible[x]['campaign'] for x in test}, {fold['held_out_campaign']})
            self.assertNotIn(fold['held_out_campaign'], {eligible[x]['campaign'] for x in train})
        for p in result['predictions']:
            self.assertAlmostEqual(p['union_residual']+p['confederate_residual'], 0)
            self.assertLessEqual(p['strength_sensitivity_p_min'], p['p_union_win'])
            self.assertLessEqual(p['p_union_win'], p['strength_sensitivity_p_max'])

    def test_heldout_outcome_cannot_change_own_prediction(self):
        records, _ = build_dataset(ROOT)
        original = evaluate(records)
        target = next(r for r in records if r['baseline_eligible'])
        changed = copy.deepcopy(records)
        for r in changed:
            if r['campaign'] == target['campaign'] and r['baseline_eligible']:
                r['source_result'] = 'Union' if r['source_result'] == 'Confederate' else 'Confederate'
        amended = evaluate(changed)
        for key in ['p_union_win', 'p_training_prior']:
            before = {p['battle_id']:p[key] for p in original['predictions'] if p['campaign']==target['campaign']}
            after = {p['battle_id']:p[key] for p in amended['predictions'] if p['campaign']==target['campaign']}
            self.assertEqual(before, after)

    def test_insufficient_campaigns_fail(self):
        with self.assertRaises(ValueError): evaluate([])


if __name__ == '__main__':
    unittest.main()
