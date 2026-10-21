"""Toy numerical checks and source-cohort contracts; no historical fitting jobs."""

import math
from pathlib import Path
import unittest
from unittest.mock import patch

from generalship import bodart_ratings as br
from generalship.ratings import cholesky, chol_solve
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]


def toy():
    return [{'id': str(i), 'year': 1700 + i, 'decade': 1700 + 10 * (i // 10),
             'a': 'alpha', 'b': 'beta' if i % 2 else 'gamma',
             'a_raw': 'Gen. Alpha', 'b_raw': 'Gen. Beta' if i % 2 else 'Gen. Gamma',
             'x': (i - 6) / 4, 'y': int(i % 3 != 0), 'personnel_checked': i % 2 == 0}
            for i in range(12)]


class BodartRatingsTests(unittest.TestCase):
    def test_labels_strip_fixed_ranks_but_keep_aliases_and_qualifiers(self):
        self.assertEqual(br.label('Div.-Gen. Masséna')[0], br.label('Marschall Masséna')[0])
        self.assertEqual(br.label('Gen. d. Kav. Fh. v. Melas')[0], 'fh v melas')
        self.assertEqual(br.label('FM. Erzhz. Karl v. Österreich')[0], 'erzhz karl v österreich')
        self.assertNotEqual(br.label('Gen. Bonaparte')[0], br.label('Napoleon I.')[0])
        self.assertEqual(br.label('Friedrich II.')[0], 'friedrich ii')
        for text in ['', 'Gen. Foo und Gen. Bar', 'Foo (seit 1800)', 'Foo; Bar', 'Foo, Bar', 'unter Foo', 'Foo/Bar',
                     'FM. Lord Raglan D.-G. Canrobert', 'Gen. Foo Gen. Bar']:
            self.assertIsNotNone(br.label(text)[1], text)

    def test_gradient_and_hessian_match_finite_differences(self):
        rows = toy()
        ff, pp = br.system(rows, ['alpha', 'beta', 'gamma'], 1.)
        c = [.7, -.2, .1, .3]
        _, g, diagonal, mul = br.derivatives(rows, ff, pp, c)
        eps = 1e-5
        for j in range(len(c)):
            plus, minus = list(c), list(c)
            plus[j] += eps
            minus[j] -= eps
            op, gp, _, _ = br.derivatives(rows, ff, pp, plus)
            om, gm, _, _ = br.derivatives(rows, ff, pp, minus)
            self.assertAlmostEqual(g[j], (op - om) / (2 * eps), places=8)
            basis = [float(i == j) for i in range(len(c))]
            column = mul(basis)
            self.assertAlmostEqual(diagonal[j], column[j], places=12)
            for i in range(len(c)):
                self.assertAlmostEqual(column[i], (gp[i] - gm[i]) / (2 * eps), places=8)

    def test_cg_matches_dense_cholesky_and_marginal_intervals(self):
        rows = toy()
        model = br.fit(rows)
        labels = sorted(model['theta'])
        ff, pp = br.system(rows, labels, 1.)
        _, _, dd, mul = br.derivatives(rows, ff, pp, [model['beta']] + [model['theta'][u] for u in labels])
        n = len(dd)
        matrix = [[mul([float(k == j) for k in range(n)])[i] for j in range(n)] for i in range(n)]
        lower = cholesky(matrix)
        ee = {e['unit']: e for e in br.estimates(rows, model, intervals=True)}
        for i in range(n):
            rhs = [float(i == j) for j in range(n)]
            actual, expected = br.cg(mul, rhs, dd), chol_solve(lower, rhs)
            for a, b in zip(actual, expected):
                self.assertAlmostEqual(a, b, places=10)
            if i:
                e = ee[labels[i - 1]]
                self.assertAlmostEqual(e['interval_95'][1] - e['theta'], br.Z95 * math.sqrt(expected[i]), places=10)

    def test_side_swap_preserves_symmetric_fit_and_flips_predictions(self):
        rows = toy()
        swapped = [{**r, 'a': r['b'], 'b': r['a'], 'x': -r['x'], 'y': 1 - r['y']} for r in rows]
        first, second = br.fit(rows), br.fit(swapped)
        self.assertAlmostEqual(first['beta'], second['beta'], places=10)
        for u in first['theta']:
            self.assertAlmostEqual(first['theta'][u], second['theta'][u], places=10)
        for a, b in zip(rows, swapped):
            self.assertAlmostEqual(br.predict(first, a), 1 - br.predict(second, b), places=12)

    def test_force_only_and_unseen_label_prior(self):
        rows = toy()
        model = br.fit(rows, commanders=False)
        self.assertEqual(model['theta'], {})
        br.verify_model(rows, model)
        self.assertEqual(br.predict({'beta': 0, 'theta': {'other': 5}}, rows[0]), .5)

    def test_components_and_minimum_exposure_for_order(self):
        rows = toy() + [{**toy()[0], 'id': 'isolated', 'a': 'delta', 'b': 'epsilon'}]
        ee = br.estimates(rows, br.fit(rows))
        by = {e['unit']: e for e in ee}
        self.assertEqual(by['alpha']['component'], by['beta']['component'])
        self.assertNotEqual(by['alpha']['component'], by['delta']['component'])
        self.assertIsNone(by['delta']['rank'])
        self.assertIsNone(by['epsilon']['rank'])
        self.assertEqual(sorted(e['rank'] for e in ee if e['rank'] is not None), [1, 2, 3])

    def test_metrics_weight_decades_equally_and_handle_extreme_probabilities(self):
        rows = [{'decade': 1700, 'y': 1, 'commander': .9, 'force_only': .5, 'equal_odds': .5},
                {'decade': 1710, 'y': 0, 'commander': 1., 'force_only': .5, 'equal_odds': .5},
                {'decade': 1710, 'y': 1, 'commander': .8, 'force_only': .5, 'equal_odds': .5}]
        m = br.metrics(rows)
        self.assertAlmostEqual(m['battle_weighted']['equal_odds']['log_loss'], math.log(2))
        self.assertNotEqual(m['battle_weighted']['commander']['brier'], m['decade_weighted']['commander']['brier'])
        self.assertTrue(math.isfinite(m['battle_weighted']['commander']['log_loss']))

    def test_preparation_is_offline_and_protects_reserved_entries(self):
        with patch.object(br, 'fit', side_effect=AssertionError('no historical fit')), \
                patch('urllib.request.urlopen', side_effect=AssertionError('no network')):
            cohort = br.prepare(ROOT)
        self.assertEqual(cohort, read_json(ROOT / br.COHORT))
        reserved = set(read_json(ROOT / br.RESERVATION)['reserved_final'])
        self.assertEqual(len(cohort['ledger']), 1682)
        self.assertEqual(sum(d['included'] for d in cohort['ledger']), len(cohort['rows']))
        self.assertFalse(reserved & {r['id'] for r in cohort['rows']})
        self.assertEqual([d for d in cohort['ledger'] if d['id'] in reserved],
                         [{'id': d['id'], 'included': False, 'reasons': ['reserved_final']}
                          for d in cohort['ledger'] if d['id'] in reserved])
        for r in cohort['rows']:
            self.assertLess(r['a'], r['b'])
            self.assertAlmostEqual(r['x'], math.log(r['personnel_a'] / r['personnel_b']))
            self.assertTrue(r['source_id'] and r['locator'] and len(r['source_sha256']) == 64)
        self.assertTrue(any(r['y'] == 0 for r in cohort['rows']))
        self.assertTrue(any(r['y'] == 1 for r in cohort['rows']))


if __name__ == '__main__':
    unittest.main()
