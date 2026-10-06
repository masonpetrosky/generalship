"""Run 3 (docs/strength-imputation.md): coverage, held-out mechanics and the parallel path."""

from collections import Counter
import math
import os
from pathlib import Path
import unittest
from unittest import mock

from generalship import ratings_v3 as r3
from generalship.parallel import pmap
from generalship.ratings import fit
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]


def synthetic(m=2):
    """Four campaigns, five commanders, two imputations whose force ratios differ."""
    plan = [('A', 'u1', 'c1', 1), ('A', 'u2', 'c2', 0), ('B', 'u1', 'c2', 1), ('B', 'u3', 'c1', 0),
            ('C', 'u2', 'c1', 1), ('C', 'u3', None, 0), ('D', 'u1', 'c2', 0), ('D', None, 'c1', 1)]
    out = []
    for mi in range(m):
        out.append([{'battle_id': f'B{i}', 'campaign': c, 'year': '1863' if c in 'AB' else '1864',
                     'x': ((i * 37 + mi * 11) % 13 - 6) / 10, 'y': y, 'us': us, 'cs': cs}
                    for i, (c, us, cs, y) in enumerate(plan)])
    return out


class HeldoutTests(unittest.TestCase):
    def test_serial_and_parallel_runs_are_identical(self):
        rows = synthetic()
        with mock.patch.dict(os.environ, {'GENERALSHIP_WORKERS': '1'}):
            serial = r3.heldout(rows)
        with mock.patch.dict(os.environ, {'GENERALSHIP_WORKERS': '3'}):
            parallel = r3.heldout(rows)
        self.assertEqual(serial, parallel)

    def test_a_held_out_outcome_cannot_move_its_own_prediction(self):
        rows = synthetic()
        with mock.patch.dict(os.environ, {'GENERALSHIP_WORKERS': '1'}):
            before = {p['battle_id']: p for p in r3.heldout(rows)['predictions']}
            for by in rows:
                by[0]['y'] = 1 - by[0]['y']  # B0 is in campaign A
            after = {p['battle_id']: p for p in r3.heldout(rows)['predictions']}
        for b in ('B0', 'B1'):  # campaign A is held out together
            self.assertEqual(before[b]['commander_model'], after[b]['commander_model'])
            self.assertEqual(before[b]['strength_only'], after[b]['strength_only'])
        self.assertNotEqual(before['B2']['commander_model'], after['B2']['commander_model'])

    def test_probabilities_are_averaged_over_imputations(self):
        rows = synthetic()
        with mock.patch.dict(os.environ, {'GENERALSHIP_WORKERS': '1'}):
            both = r3.heldout(rows)['predictions']
            single = [r3.heldout([by])['predictions'] for by in rows]
        for k, p in enumerate(both):
            for model in ('commander_model', 'strength_only'):
                self.assertAlmostEqual(p[model], (single[0][k][model] + single[1][k][model]) / 2, places=15)


class ScoreTests(unittest.TestCase):
    def preds(self, cm, so):
        return [{'battle_id': f'B{i}', 'campaign': 'AB'[i % 2], 'union_outcome': i % 2,
                 'commander_model': a, 'strength_only': b} for i, (a, b) in enumerate(zip(cm, so))]

    def test_campaign_weighting_is_the_mean_over_campaigns(self):
        s = r3.score(self.preds([0.2, 0.7, 0.4], [0.5, 0.5, 0.5]))
        ll = lambda y, p: -(y * math.log(p) + (1 - y) * math.log(1 - p))
        a = (ll(0, 0.2) + ll(0, 0.4)) / 2
        b = ll(1, 0.7)
        self.assertAlmostEqual(s['campaign_weighted']['commander_model']['log_loss'], (a + b) / 2, places=12)

    def test_improvement_needs_both_weightings(self):
        # Better in campaign A (two rows), worse in campaign B: battle-weighted lower, campaign-weighted higher.
        s = r3.score(self.preds([0.2, 0.3, 0.2], [0.5, 0.5, 0.5]))
        self.assertLess(s['battle_weighted']['commander_model']['log_loss'], s['battle_weighted']['strength_only']['log_loss'])
        self.assertGreater(s['campaign_weighted']['commander_model']['log_loss'], s['campaign_weighted']['strength_only']['log_loss'])
        self.assertFalse(s['improved'])
        self.assertTrue(r3.score(self.preds([0.3, 0.7, 0.3], [0.5, 0.5, 0.5]))['improved'])


class TemporalTests(unittest.TestCase):
    def test_degenerate_splits_are_not_evaluable(self):
        rows = synthetic()
        self.assertFalse(r3.temporal(rows, years=(('1850',), ('1864',)))['evaluable'])
        self.assertFalse(r3.temporal(rows, years=(('1863',), ('1850',)))['evaluable'])
        one_class = [[{**r, 'y': 1} for r in by] for by in rows]
        self.assertFalse(r3.temporal(one_class, years=(('1863',), ('1864',)))['evaluable'])
        self.assertTrue(r3.temporal(rows, years=(('1863',), ('1864',)))['evaluable'])


class FitTests(unittest.TestCase):
    def test_mode_only_fit_gives_the_same_mode(self):
        rows = synthetic()[0]
        full, mode = fit(rows), fit(rows, covariance=False)
        self.assertEqual((full['alpha'], full['beta'], full['theta']), (mode['alpha'], mode['beta'], mode['theta']))
        self.assertNotIn('cov', mode)

    def test_pmap_matches_a_serial_map(self):
        self.assertEqual(pmap(_square_plus, range(7), shared=3, n=3), [_square_plus(x, 3) for x in range(7)])


def _square_plus(x, k):
    return x * x + k


class CommittedRunTests(unittest.TestCase):
    def test_coverage_counts_every_ledger_attribution(self):
        path = ROOT / 'artifacts/commander-ratings-v3.json'
        if not path.is_file():
            self.skipTest('run 3 output not present')
        result = read_json(path)
        ledger = read_json(ROOT / r3.COMMAND)
        nested = set(result['model']['dropped_as_nested'])
        credited, dropped = Counter(), {}
        for e in ledger['engagements']:
            for s in ('US', 'Confederate'):
                c = e['sides'][s]['commander_id']
                if c:
                    credited[c] += 1
                    if e['battle_id'] in nested:
                        dropped.setdefault(c, []).append(e['battle_id'])
        self.assertEqual(set(result['commanders']), set(credited))
        for c, n in credited.items():
            entry = result['commanders'][c]
            self.assertEqual(entry['battles_attributed'], n, c)
            self.assertEqual(entry['dropped_as_nested'], sorted(dropped.get(c, [])), c)
            if entry['battles_modelled'] == 0:
                self.assertIn('coverage_only', entry['labels'], c)
