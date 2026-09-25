"""Grade E strength model and run-3 machinery (docs/strength-imputation.md); synthetic data except the replay."""

import math
from pathlib import Path
import unittest

from generalship import imputation as imp
from generalship import ratings_v3 as r3
from generalship.ratings import RatingError
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]


def row(y, echelon='unknown', side='US', period='1863', theater='Eastern'):
    return {'y': y, 'echelon': echelon, 'side': side, 'period': period, 'theater': theater}


class ModelTests(unittest.TestCase):
    def test_intercept_is_unpenalized_and_level_effects_are_shrunk(self):
        rows = [row(math.log(1000 + 10 * i)) for i in range(40)]
        m = imp.Model(rows, {'echelon': [], 'side': [], 'period': [], 'theater': []})
        self.assertAlmostEqual(m.beta[0], sum(r['y'] for r in rows) / len(rows), places=9)
        rows += [row(math.log(8000), 'army') for _ in range(40)]
        m = imp.Model(rows, {'echelon': ['army'], 'side': [], 'period': [], 'theater': []})
        # closed form with 40 rows per level and ridge 1: b = (20/21)(mean2 - mean1), a = mean2 - (41/40) b
        m1 = sum(math.log(1000 + 10 * i) for i in range(40)) / 40
        b = 20 / 21 * (math.log(8000) - m1)
        self.assertAlmostEqual(m.beta[1], b, places=9)
        self.assertAlmostEqual(m.beta[0], math.log(8000) - 41 / 40 * b, places=9)

    def test_truncated_quantiles_respect_bounds(self):
        for q in (0.0, 0.1, 0.5, 0.9, 1.0):
            v = imp.quantile(math.log(2000), 1.0, q, lo=1500, hi=2500)
            self.assertGreaterEqual(v, 1500 * (1 - 1e-9))
            self.assertLessEqual(v, 2500 * (1 + 1e-9))

    def test_bound_eligibility_follows_rule_7(self):
        base = {'bound': 'lower', 'codes': ['partial_scope'], 'loss_timing': 'none', 'adjustments': [], 'basis': 'unknown'}
        self.assertTrue(imp.eligible_bound(base)[0])
        self.assertFalse(imp.eligible_bound(dict(base, codes=['partial_scope', 'adversary_or_hearsay_estimate']))[0])
        self.assertFalse(imp.eligible_bound(dict(base, codes=['post_engagement_state']))[0])
        self.assertFalse(imp.eligible_bound(dict(base, bound=None))[0])

    def test_period_boundaries(self):
        self.assertEqual(imp.period('1862-12-31'), '1861-1862')
        self.assertEqual(imp.period('1863-07-01'), '1863')
        self.assertEqual(imp.period('1865-04-09'), '1864-1865')


class RunThreeTests(unittest.TestCase):
    def rows(self):
        spec_e = {'grade': 'E', 'mu_log': math.log(3000), 'sd_log': 1.0, 'lower_bound': None, 'upper_bound': None,
                  'fixed': None, 'point': 3000, 'low': 1000, 'high': 9000, 'labels': []}
        spec_a = {'grade': 'A', 'point': 5000, 'low': 4750, 'high': 5250}
        return [{'battle_id': f'B{i:02d}', 'spec': {'US': spec_a, 'Confederate': dict(spec_e)}} for i in range(5)]

    def test_imputations_are_deterministic_and_ordered(self):
        a, b = r3.imputations(self.rows(), m=3), r3.imputations(self.rows(), m=3)
        self.assertEqual(a, b)
        self.assertEqual(len(a), 3)
        self.assertEqual(sorted(a[0]), [(f'B{i:02d}', 'Confederate') for i in range(5)])
        self.assertNotEqual(a[0], a[1])

    def test_wider_imputation_spreads_draws(self):
        narrow = r3.imputations(self.rows(), m=20)
        wide = r3.imputations(self.rows(), m=20, sd_scale=2.0)
        spread = lambda s: max(v for d in s for v in d.values()) / min(v for d in s for v in d.values())
        self.assertGreater(spread(wide), spread(narrow))

    def test_run_is_refused_without_an_authorization_naming_the_files(self):
        with self.assertRaises((RatingError, OSError, ValueError)):
            r3.authorize(ROOT, 'data/command/rating-authorization-v2.json')


class ReplayTests(unittest.TestCase):
    def test_committed_imputation_reproduces(self):
        path = ROOT / 'artifacts/strength-imputation-v1.json'
        if path.is_file():
            self.assertEqual(imp.build(ROOT, verify=False), read_json(path))


if __name__ == '__main__':
    unittest.main()
