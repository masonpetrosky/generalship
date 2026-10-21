"""Saved-forecast arithmetic, common attribution, coverage and ordering limits."""

import copy
from pathlib import Path
import unittest
from unittest.mock import patch

from generalship import commander_comparison as cc
from generalship.sources import read_csv, read_json

ROOT = Path(__file__).resolve().parents[1]


class CommanderComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.saved_run = read_json(ROOT / cc.RUN)
        cls.command = read_json(ROOT / cc.COMMAND)
        cls.battles = {r['battle']: r for r in read_csv(ROOT / cc.BATTLES)}
        cls.cohort = read_json(ROOT / cc.COHORT)['battle_ids']
        cls.result = cc.build(ROOT)

    def test_common_rows_and_missingness_are_explicit(self):
        d = self.result
        self.assertEqual(d['coverage']['scored_battles'], 301)
        self.assertEqual(d['coverage']['ordered_by_side'], {'US': 49, 'Confederate': 42})
        self.assertEqual(d['coverage']['battles_with_modelled_strength'], 120)
        self.assertEqual(len(d['coverage']['outside_ledger']), 79)
        self.assertEqual(d['coverage']['single_battle_commanders'], 211)
        self.assertEqual(d['coverage']['zero_battle_commanders'], 11)
        self.assertEqual(d['original_verdict'], self.saved_run['verdict'])
        for r in d['commanders']:
            self.assertEqual(r['ordered'], r['battles'] >= 2)
            if not r['ordered']:
                self.assertIsNone(r['model_order'])
                self.assertIsNone(r['raw_order'])
            if not r['battles']:
                self.assertIsNone(r['raw_total'])
                self.assertIsNone(r['raw_per_battle'])
                self.assertIsNone(r['theta'])

    def test_complementary_residuals_and_joint_command(self):
        by = {r['id']: r for r in self.result['commanders']}
        ledger = {e['battle_id']: e for e in self.command['engagements']}
        for battle in self.result['battles']:
            a, b = (battle['sides'][s] for s in cc.SIDES)
            self.assertAlmostEqual(a['residual'], -b['residual'])
            for side in cc.SIDES:
                s = battle['sides'][side]
                joint = 'joint_command' in ledger[battle['battle_id']]['sides'][side]['labels']
                if joint:
                    self.assertIsNone(s['commander'])
                    self.assertEqual(s['uncredited_reason'], 'joint_command')
                if s['commander']:
                    self.assertIn(battle['battle_id'], by[s['commander']]['battle_ids'])
        for r in by.values():
            residuals = [s['residual'] for b in self.result['battles'] for s in b['sides'].values()
                         if s['commander'] == r['id']]
            if residuals:
                self.assertAlmostEqual(r['raw_total'], sum(residuals))

    def test_weightings_and_tied_ranks(self):
        rows = [{'campaign': c, 'outcome': 1, **{k: p for k in cc.MODELS}}
                for c, p in [('large', .9), ('large', .9), ('small', .1)]]
        metrics = cc.score(rows)
        self.assertAlmostEqual(metrics['battle_weighted']['strength_only']['brier'], (.01 + .01 + .81) / 3)
        self.assertAlmostEqual(metrics['campaign_weighted']['strength_only']['brier'], (.01 + .81) / 2)
        ranks = cc.ranks([{'id': 'a', 'side': 'US', 's': 2}, {'id': 'b', 'side': 'US', 's': 2},
                          {'id': 'c', 'side': 'US', 's': 1}, {'id': 'd', 'side': 'Confederate', 's': 9}], 's')
        self.assertEqual(ranks, {'a': 1, 'b': 1, 'c': 3, 'd': 1})

    def test_saved_forecast_corruption_is_rejected(self):
        for change in ('duplicate', 'missing', 'orientation', 'probability', 'campaign'):
            with self.subTest(change=change):
                run = copy.deepcopy(self.saved_run)
                preds = run['heldout']['predictions']
                if change == 'duplicate':
                    preds.append(preds[0])
                elif change == 'missing':
                    preds.pop()
                elif change == 'orientation':
                    preds[0]['outcome'] = 1 - preds[0]['outcome']
                elif change == 'probability':
                    preds[0]['strength_only'] = float('nan')
                else:
                    preds[0]['campaign'] = 'wrong campaign'
                with self.assertRaises(ValueError):
                    cc.summarize(run, self.command, self.battles, self.cohort)

    def test_build_uses_saved_outputs_without_fit_or_fetch(self):
        with patch('generalship.baseline.fit_logistic', side_effect=AssertionError('no fit')), \
                patch('urllib.request.urlopen', side_effect=AssertionError('no fetch')):
            self.assertEqual(cc.build(ROOT), self.result)
        text = cc.report(self.result)
        self.assertIn('not a reproduction of his published rankings', text)
        self.assertIn('a better ranking is not demonstrated', text)
        self.assertEqual(text.count('https://masonpetrosky.github.io/generalship/commanders/'), 91)


if __name__ == '__main__':
    unittest.main()
