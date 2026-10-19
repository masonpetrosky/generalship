"""Constructed-data checks, not the checkpoint's model job."""

import unittest

from generalship import recovery
from generalship.ratings_v4 import fit4, predict4


def rows():
    return [{'battle_id': str(i), 'campaign': f'g{i % 3}', 'war': f'w{i % 2}', 'year': 1812 + i % 2,
             'a': f'a{i % 2}', 'b': f'b{i % 3}', 'x': (i % 7 - 3) / 5,
             'y': int(i % 5 < 3), 'ctx': []} for i in range(24)]


class RecoveryTests(unittest.TestCase):
    def test_sparse_solution_agrees_with_frozen_solver(self):
        data = rows()
        sparse = recovery.fit(data, tau=0.6)
        frozen = fit4(data, tau=0.6, use_context=False)
        self.assertLess(sparse['max_gradient'], 1e-7)
        for row in data:
            self.assertAlmostEqual(recovery.predict(sparse, row), predict4(frozen, row), places=7)
        for key, value in frozen['theta'].items():
            self.assertAlmostEqual(sparse['coef']['commander:' + key], value, places=6)

    def test_permanent_army_pairing_has_identical_predictions_under_reallocation(self):
        row = {**rows()[0], 'army_a': 'aa', 'army_b': 'bb'}
        first = {'coef': {'commander:a0': 0.8, 'commander:b0': -0.2}}
        second = {'coef': {'army:aa': 0.8, 'army:bb': -0.2}}
        self.assertEqual(recovery.predict(first, row, armies=True), recovery.predict(second, row, armies=True))

    def test_simulation_ignores_supplied_real_response_and_is_deterministic(self):
        p = {'seed': 1, 'scenarios': ['null', 'commander', 'stable_army_alias', 'switching_armies', 'source_bias'],
             'commander_sd': .6, 'army_sd': .8, 'source_bias_sd': .4, 'group_sd': .35, 'army_pools_per_side': 8}
        schedule = [{k: r[k] for k in ('battle_id', 'campaign', 'war', 'year', 'a', 'b')} for r in rows()]
        first, truth = recovery.generate(schedule, 'stable_army_alias', 0, p)
        second, other = recovery.generate([{**r, 'y': 999, 'outcome_side_a': object()} for r in schedule],
                                          'stable_army_alias', 0, p)
        self.assertEqual(first, second)
        self.assertEqual(truth, other)
        self.assertTrue(all(v == 0 for v in truth.values()))
        self.assertTrue(all(r['army_a'] == 'permanent:' + r['a'] for r in first))

    def test_folds_preserve_groups_and_forward_direction(self):
        for strategy, field in [('war_year', 'campaign'), ('whole_war', 'war')]:
            tests = []
            for train, test in recovery.folds(rows(), strategy):
                self.assertFalse({r[field] for r in train} & {r[field] for r in test})
                tests += [r['battle_id'] for r in test]
            self.assertEqual(sorted(tests), sorted(r['battle_id'] for r in rows()))
        train, test = recovery.folds(rows(), 'forward_time')[0]
        self.assertLess(max(r['year'] for r in train), min(r['year'] for r in test))


if __name__ == '__main__':
    unittest.main()
