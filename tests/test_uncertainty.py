"""The verdict-uncertainty analysis (generalship/uncertainty.py) refits nothing and is deterministic."""

import math
from pathlib import Path
import unittest

from generalship import uncertainty as u

ROOT = Path(__file__).resolve().parents[1]


def rows(ds):
    return [{'battle_id': f'B{i}', 'campaign': c, 'd': d} for i, (c, d) in enumerate(ds)]


class UnitTests(unittest.TestCase):
    def test_weightings(self):
        b, c = u.weighted(rows([('A', -0.3), ('A', -0.1), ('B', 0.2)]))
        self.assertAlmostEqual(b, -0.2 / 3, places=15)
        self.assertAlmostEqual(c, (-0.2 + 0.2) / 2, places=15)

    def test_bootstrap_is_deterministic_and_degenerate_without_spread(self):
        rs = rows([('A', -0.1), ('B', -0.1), ('C', -0.1)])
        first, second = u.bootstrap(rs, resamples=200), u.bootstrap(rs, resamples=200)
        self.assertEqual(first, second)
        for w in ('battle_weighted', 'campaign_weighted'):
            self.assertAlmostEqual(first[w]['q0.025'], -0.1, places=15)
            self.assertAlmostEqual(first[w]['q0.975'], -0.1, places=15)
            self.assertEqual(first[w]['share_at_or_above_zero'], 0.0)

    def test_sign_test_is_exact(self):
        s = u.sign_test(rows([('A', -1), ('B', -1), ('C', -1), ('D', 1), ('E', 0)]))
        self.assertEqual((s['commander_model_better'], s['strength_only_better'], s['ties']), (3, 1, 1))
        self.assertAlmostEqual(s['two_sided_p'], 2 * 5 / 16, places=15)  # P(X >= 3 | n = 4) = 5/16

    def test_log_loss_matches_the_scored_runs(self):
        self.assertAlmostEqual(u.log_loss(1, 0.8), -math.log(0.8), places=15)
        self.assertAlmostEqual(u.log_loss(0, 0.8), -math.log(0.2), places=12)
        self.assertLess(u.log_loss(1, 1.0), 1e-12)


class CommittedRunTests(unittest.TestCase):
    def test_run_three_point_reproduces_and_the_artifact_matches(self):
        if not (ROOT / 'artifacts/commander-ratings-v3.json').is_file():
            self.skipTest('run 3 output not present')
        result = u.analyse(ROOT, 3)
        self.assertEqual(result['rows'], 301)
        self.assertLess(result['point']['battle_weighted'], 0)
        stored = ROOT / 'artifacts/commander-ratings-v3-uncertainty.json'
        if stored.is_file():  # exact structure; floats to 1e-9 (log loss uses the platform's maths library)
            from generalship.compare import differences
            from generalship.sources import read_json
            self.assertEqual(differences(read_json(stored), result), [])
