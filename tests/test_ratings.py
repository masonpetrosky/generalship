"""Commander residual-rating model (docs/commander-ratings.md §§4–7) on invented rows only."""

import json
import math
from pathlib import Path
import tempfile
import unittest

from generalship.ratings import (DEFAULT_AUTHORIZATION, RatingError, attribution, authorize, components, fit,
                                 heldout, predict, report_text, summarize)
from generalship.sources import digest


def row(us, cs, y, x=0.0, campaign='c1', bid=None):
    return {'battle_id': bid or f'{us}-{cs}-{campaign}-{y}', 'campaign': campaign, 'year': '1862', 'x': x, 'y': y,
            'us': us, 'cs': cs}


class ModelTests(unittest.TestCase):
    def test_winning_commander_gets_positive_theta_and_pooling_shrinks_it(self):
        rows = [row('us-a', 'cs-b', 1, bid=f'r{i}') for i in range(3)] + [row('us-c', 'cs-d', 0, bid=f's{i}') for i in range(3)]
        m = fit(rows)
        self.assertGreater(m['theta']['us-a'], 0)
        self.assertLess(m['theta']['cs-b'], 0)
        self.assertLess(fit(rows, tau=0.25)['theta']['us-a'], m['theta']['us-a'])
        self.assertAlmostEqual(m['theta']['us-a'], -m['theta']['cs-b'], places=9)

    def test_laplace_interval_matches_quadrature_for_one_theta(self):
        # With α and β pinned near zero, the posterior of the one θ is one-dimensional.
        rows = [row('us-a', None, 1, bid='a'), row('us-a', None, 1, bid='b'), row('us-a', None, 0, bid='c')]
        m = fit(rows, alpha_sd=1e-6, use_force=False)
        grid = [i / 1000 for i in range(-4000, 4001)]
        logp = [sum(math.log(1 / (1 + math.exp(-t))) if r['y'] else math.log(1 / (1 + math.exp(t))) for r in rows)
                - t * t / (2 * 0.25) for t in grid]
        top = max(logp)
        w = [math.exp(v - top) for v in logp]
        mean = sum(t * wi for t, wi in zip(grid, w)) / sum(w)
        sd = math.sqrt(sum((t - mean) ** 2 * wi for t, wi in zip(grid, w)) / sum(w))
        self.assertAlmostEqual(m['theta']['us-a'], mean, delta=0.02)
        self.assertAlmostEqual(m['sd']['us-a'], sd, delta=0.02)

    def test_unseen_commander_contributes_nothing_to_a_heldout_prediction(self):
        rows = [row('us-a', 'cs-b', 1, x=0.1, campaign='c1', bid='1'), row('us-a', 'cs-b', 0, x=-0.1, campaign='c2', bid='2'),
                row('us-z', 'cs-b', 1, x=0.2, campaign='c3', bid='3')]
        m = fit(rows[:2])
        self.assertEqual(predict(m, rows[2]), predict(m, {**rows[2], 'us': None}))
        result = heldout(rows)
        self.assertEqual({e['battle_id'] for e in result['effective_rows']}, {'1', '2', '3'})
        self.assertIn('improved', result)

    def test_components_and_not_connected(self):
        rows = [row('us-a', 'cs-b', 1, bid='1'), row('us-a', 'cs-b', 0, bid='2'), row('us-c', 'cs-d', 1, bid='3'),
                row('us-c', 'cs-d', 0, bid='4')]
        comp = components(rows)
        self.assertEqual(comp['us-a'], comp['cs-b'])
        self.assertNotEqual(comp['us-a'], comp['us-c'])
        out = summarize(rows, fit(rows), {'us-a': 'US', 'us-c': 'US', 'cs-b': 'Confederate', 'cs-d': 'Confederate'})
        self.assertIn('not_connected', out['us-a']['labels'])
        self.assertIn('rank_80', out['us-a'])


class AttributionTests(unittest.TestCase):
    side = {'commander_id': 'us-a', 'grade': 'C', 'labels': ['command_changed', 'superior_directing'],
            'successor': 'us-b', 'superior': 'us-s', 'candidates': ['us-c']}

    def test_views(self):
        self.assertEqual(attribution(self.side), 'us-a')
        self.assertIsNone(attribution(self.side, 'grades_ab'))
        self.assertEqual(attribution(self.side, 'superior'), 'us-s')
        self.assertEqual(attribution(self.side, 'successor'), 'us-b')
        self.assertEqual(attribution(self.side, alt='us-c'), 'us-c')


class ReportTests(unittest.TestCase):
    def result(self, improved):
        m = {'brier': 0.2, 'log_loss': 0.6}
        c = {'name': 'A', 'side': 'US', 'ranked': True, 'battles_modelled': 2, 'wins_in_model': 1, 'losses_in_model': 1,
             'theta_mode': 0.1, 'interval_80': [-0.5, 0.7], 'interval_95': [-0.9, 1.1], 'rank_80': [1, 2], 'rank_median': 1,
             'posterior_prior_sd_ratio': 0.95, 'labels': []}
        return {'model': {'rows': 3, 'campaigns': 2, 'tau': 0.5}, 'temporal_split': {'evaluable': False}, 'flags': ['not_causal'], 'commanders': {'us-a': c, 'us-b': {**c, 'name': 'B', 'rank_median': 2}},
                'heldout_test': {'improved': improved, 'battle_weighted': {'commander_model': m, 'strength_only': m},
                                 'campaign_weighted': {'commander_model': m, 'strength_only': m}, 'effective_rows': [], 'n_rows': 3,
                                 'campaigns_better': {}}}

    def test_no_signal_gives_no_ordered_ranking(self):
        text = report_text(self.result(False))
        self.assertIn('No ordered ranking is given', text)
        self.assertIn('(alphabetical)', text)
        self.assertNotIn('(alphabetical)', report_text(self.result(True)))


class GateTests(unittest.TestCase):
    def test_authorization_must_name_every_bound_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            paths = {'strength_ledger': 'data/estimates/side-strength-v1.json', 'command_ledger': 'data/command/responsibility-v1.json',
                     'registry': 'data/command/commanders-v1.json'}
            for p in paths.values():
                (root / p).parent.mkdir(parents=True, exist_ok=True)
                (root / p).write_text('{}\n')
            auth = {'kind': 'commander_rating_authorization', 'decision_date': 'x', 'admits_feature': False, 'changes_baseline': False,
                    **{k: {'path': p, 'sha256': digest(root / p)} for k, p in paths.items()}}
            (root / DEFAULT_AUTHORIZATION).write_text(json.dumps(auth))
            self.assertEqual(authorize(root)['kind'], 'commander_rating_authorization')
            (root / paths['command_ledger']).write_text('{"changed": 1}\n')
            with self.assertRaisesRegex(RatingError, 'command_ledger'):
                authorize(root)


if __name__ == '__main__':
    unittest.main()
