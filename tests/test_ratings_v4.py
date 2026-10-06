"""Run 4 (docs/commander-ratings-v4.md): the generalized fit, the evidence, the held-out mechanics and the verdict rule."""

import json
import math
import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest import mock

from generalship import ratings_v4 as r4
from generalship.baseline import sigmoid
from generalship.ratings import fit, predict
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]


def synthetic(m=2, context=True):
    """Six campaigns in two theaters and two periods, five commanders, m imputations whose force ratios differ."""
    plan = [('A', 'u1', 'c1', 1), ('A', 'u2', 'c2', 0), ('B', 'u1', 'c2', 1), ('B', 'u3', 'c1', 0),
            ('C', 'u2', 'c1', 1), ('C', 'u3', None, 0), ('D', 'u1', 'c2', 0), ('D', None, 'c1', 1),
            ('E', 'u2', 'c2', 1), ('E', 'u3', 'c1', 1), ('F', 'u1', 'c1', 0), ('F', 'u2', None, 1)]
    out = []
    for mi in range(m):
        rows = []
        for i, (c, a, b, y) in enumerate(plan):
            th, per = ('East' if c in 'ACE' else 'West'), ('early' if c in 'ABC' else 'late')
            rows.append({'battle_id': f'B{i}', 'campaign': c, 'year': '1863' if c in 'ABC' else '1864',
                         'ctx': [f'theater={th}', f'period={per}', f'cell={th}|{per}'] if context else [],
                         'x': ((i * 37 + mi * 11) % 13 - 6) / 10, 'y': y, 'a': a, 'b': b})
        out.append(rows)
    return out


def as_run3(rows):
    return [{**r, 'us': r['a'], 'cs': r['b']} for r in rows]


class FitTests(unittest.TestCase):
    def test_without_context_the_fit_is_run_3s_exactly(self):
        rows = synthetic(1, context=False)[0]
        for params in ({}, {'tau': 0.25}, {'alpha_sd': 3.0}, {'use_force': False}):
            with self.subTest(**params):
                old = fit(as_run3(rows), **params)
                new = r4.fit4(rows, use_context=False, out='covariance', **params)
                for k in ('alpha', 'beta', 'theta', 'sd', 'mode', 'cov', 'index', 'commanders'):
                    self.assertEqual(new[k], old[k], k)
                for r, r3 in zip(rows, as_run3(rows)):
                    self.assertEqual(r4.predict4(new, r), predict(old, r3))

    def test_tau_zero_is_the_context_model(self):
        model = r4.fit4(synthetic(1)[0], tau=0.0)
        self.assertEqual(model['theta'], {})
        self.assertEqual(model['commanders'], [])
        self.assertEqual(len(model['context']), 8)  # 2 theaters, 2 periods and the 4 cells that occur
        self.assertEqual(len(model['mode']), 2 + 8)

    def test_context_effects_take_the_sign_of_the_data(self):
        rows = [{'battle_id': f'B{i}', 'campaign': f'C{i}', 'year': '1863', 'x': 0.0, 'a': None, 'b': None,
                 'ctx': ['theater=East' if i % 2 else 'theater=West'], 'y': int(i % 2 == 1 or i % 6 == 0)} for i in range(60)]
        model = r4.fit4(rows, tau=0.0)
        self.assertGreater(model['context']['theater=East'], 0)
        self.assertLess(model['context']['theater=West'], 0)

    def test_laplace_evidence_matches_quadrature_for_one_parameter(self):
        # x = 0 everywhere, no context, no commanders: only α is free; β's terms cancel exactly.
        ys = [1] * 14 + [0] * 6
        rows = [{'battle_id': f'B{i}', 'campaign': 'C', 'year': '1863', 'x': 0.0, 'a': None, 'b': None, 'ctx': [], 'y': y}
                for i, y in enumerate(ys)]
        laplace = r4.fit4(rows, tau=0.0, use_context=False, out='evidence')['log_evidence']
        h = 1e-3
        grid = [-8 + h * k for k in range(int(16 / h) + 1)]
        log_f = [sum(math.log(sigmoid(a)) if y else math.log(sigmoid(-a)) for y in ys) - a * a / 2 - math.log(2 * math.pi) / 2
                 for a in grid]
        top = max(log_f)
        quad = top + math.log(math.fsum(math.exp(v - top) for v in log_f) * h)
        self.assertAlmostEqual(laplace, quad, delta=0.01)

    def test_a_tie_in_evidence_goes_to_the_smaller_tau(self):
        self.assertEqual(r4.select_tau({0.0: -3.0, 0.3: -2.5, 0.5: -2.5}), 0.3)


class AttributionTests(unittest.TestCase):
    def rows(self):
        side = lambda c, labels=(): {'commander_id': c, 'labels': list(labels), 'grade': 'C', 'candidates': ['x-alt'],
                                     'superior': None, 'successor': None}
        spec = {'grade': 'A', 'point': 1000, 'low': 900, 'high': 1100}
        return [{'battle_id': 'B1', 'campaign': 'C', 'year': '1863', 'ctx': [], 'y': 1, 'labels': [],
                 'sides': {'US': side('us-a', ['joint_command']), 'Confederate': side('cs-b')},
                 'spec': {'US': spec, 'Confederate': {**spec, 'point': 500}}}]

    def test_a_joint_command_side_gets_no_commander_term_unless_a_view_credits_it(self):
        profile = r4.PROFILE
        self.assertEqual([(r['a'], r['b']) for r in r4.with_x(self.rows(), profile, None)], [(None, 'cs-b')])
        self.assertEqual([(r['a'], r['b']) for r in r4.with_x(self.rows(), profile, None, credit_joint=True)], [('us-a', 'cs-b')])
        alt = r4.with_x(self.rows(), profile, None, alt=('B1', 'US', 'x-alt'))
        self.assertEqual((alt[0]['a'], alt[0]['b']), ('x-alt', 'cs-b'))
        self.assertAlmostEqual(alt[0]['x'], 500 / 1500)

    def test_a_commander_takes_the_sign_of_the_side_commanded_in_each_row(self):
        rows = [{'battle_id': 'B1', 'campaign': 'C1', 'year': '1813', 'ctx': [], 'x': 0.0, 'y': 1, 'a': 'k', 'b': 'o1'},
                {'battle_id': 'B2', 'campaign': 'C2', 'year': '1814', 'ctx': [], 'x': 0.0, 'y': 0, 'a': 'o2', 'b': 'k'}]
        model = r4.fit4(rows, use_context=False)
        self.assertGreater(model['theta']['k'], 0)  # won both battles, once on each side


class HeldoutTests(unittest.TestCase):
    def test_serial_and_parallel_folds_are_identical(self):
        shared = {'primary': synthetic(), 'bridge': synthetic()}
        tasks = [('primary', 'A'), ('bridge', 'B'), ('grid', (1, None)), ('grid', (0, (('1863',), ('1864',))))]
        with mock.patch.dict(os.environ, {'GENERALSHIP_WORKERS': '1'}):
            serial = r4.pmap(r4._phase1, tasks, shared=shared)
        with mock.patch.dict(os.environ, {'GENERALSHIP_WORKERS': '3'}):
            parallel = r4.pmap(r4._phase1, tasks, shared=shared)
        self.assertEqual(serial, parallel)

    def test_a_held_out_outcome_moves_neither_its_prediction_nor_tau_hat(self):
        rows = synthetic()
        before, _, tau_before = r4._primary_fold('A', rows)
        for by in rows:
            by[0]['y'] = 1 - by[0]['y']  # B0 is in campaign A
        after, _, tau_after = r4._primary_fold('A', rows)
        self.assertEqual(before, after)
        self.assertEqual(tau_before, tau_after)
        self.assertEqual(set(before), {'B0', 'B1'})
        self.assertEqual(set(before['B0']), set(r4.MODELS))
        self.assertEqual(len(before['B0']['commander']), 2)  # one probability per imputation

    def test_the_commander_model_uses_the_fold_tau_hat(self):
        rows = synthetic()
        preds, _, info = r4._primary_fold('B', rows)
        tau = info['tau_hat']
        train = [r for r in rows[1] if r['campaign'] != 'B']
        test = next(r for r in rows[1] if r['battle_id'] == 'B2')
        expected = r4.predict4(r4.fit4(train, tau=tau), test)
        self.assertEqual(preds['B2']['commander'][1], expected)
        self.assertEqual(preds['B2']['context'][1], r4.predict4(r4.fit4(train, tau=0.0), test))


class VerdictTests(unittest.TestCase):
    def preds(self, gain):
        out = []
        for c in range(12):
            for i in range(3):
                y = (c + i) % 2
                ctx = 0.6 if y else 0.4
                out.append({'battle_id': f'B{c}-{i}', 'campaign': f'C{c}', 'outcome': y, 'context': ctx,
                            'commander': ctx + (gain if y else -gain) * (1 if (c, i) != (0, 0) else -1)})
        return out

    def test_a_consistent_gain_passes_and_a_noisy_one_does_not(self):
        self.assertTrue(r4.verdict(r4.compare(self.preds(0.1), 'commander', 'context', resamples=2000))['improved'])
        mixed = self.preds(0.0)
        for p in mixed:  # better in even campaigns, worse in odd ones
            sign = 1 if int(p['campaign'][1:]) % 2 == 0 else -1
            p['commander'] = p['context'] + sign * (0.1 if p['outcome'] else -0.1)
        v = r4.verdict(r4.compare(mixed, 'commander', 'context', resamples=2000))
        self.assertFalse(v['improved'])
        self.assertTrue(v['q95']['battle_weighted'] > 0 and v['q95']['campaign_weighted'] > 0)

    def test_both_weightings_are_required(self):
        comparison = {'battle_weighted': -0.01, 'campaign_weighted': 0.001,
                      'bootstrap': {'battle_weighted': {'q0.95': -0.001}, 'campaign_weighted': {'q0.95': 0.002}}}
        self.assertFalse(r4.verdict(comparison)['improved'])
        comparison['bootstrap']['campaign_weighted']['q0.95'] = -0.0001
        self.assertTrue(r4.verdict(comparison)['improved'])

    def test_scores_weight_battles_and_campaigns(self):
        preds = [{'battle_id': 'B1', 'campaign': 'A', 'outcome': 1, 'm': 0.8},
                 {'battle_id': 'B2', 'campaign': 'A', 'outcome': 0, 'm': 0.4},
                 {'battle_id': 'B3', 'campaign': 'B', 'outcome': 1, 'm': 0.5}]
        s = r4.score(preds, ('m',))
        ll = [-math.log(0.8), -math.log(0.6), -math.log(0.5)]
        self.assertAlmostEqual(s['battle_weighted']['m']['log_loss'], sum(ll) / 3, places=12)
        self.assertAlmostEqual(s['campaign_weighted']['m']['log_loss'], ((ll[0] + ll[1]) / 2 + ll[2]) / 2, places=12)


class AuthorizationTests(unittest.TestCase):
    def test_a_record_binding_other_code_is_refused(self):
        auth = {'kind': 'commander_rating_authorization', 'run_version': 4, 'admits_feature': False, 'changes_baseline': False,
                'files': {k: {'path': p, 'sha256': 'x'} for k, p in r4.bound_files().items()},
                'code': {p: 'x' for p in r4.CODE}}
        with mock.patch.object(r4, 'read_json', return_value=auth), mock.patch.object(r4, 'digest', return_value='x'):
            self.assertEqual(r4.authorize(ROOT), auth)
            auth['code'][r4.CODE[0]] = 'y'
            with self.assertRaises(r4.RatingError):
                r4.authorize(ROOT)
            auth['code'][r4.CODE[0]] = 'x'
            auth['files']['design']['sha256'] = 'y'
            with self.assertRaises(r4.RatingError):
                r4.authorize(ROOT)


class CodeBindingTests(unittest.TestCase):
    def test_the_bound_code_is_the_runs_import_closure(self):
        out = subprocess.run([sys.executable, '-c', 'import json, sys, generalship.ratings_v4; '
                              'print(json.dumps(sorted(m for m in sys.modules if m.startswith("generalship"))))'],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout
        modules = json.loads(out)
        expected = sorted('generalship/' + ('__init__' if m == 'generalship' else m.split('.', 1)[1]) + '.py' for m in modules)
        self.assertEqual(sorted(r4.CODE), expected)


class CommittedRunTests(unittest.TestCase):
    """The committed run-4 output and its report agree (skipped until the run exists)."""

    def test_the_report_regenerates_from_the_committed_output(self):
        path = ROOT / f'{r4.OUTPUT}.json'
        if not path.is_file():
            self.skipTest('run 4 has not been run')
        result = read_json(path)
        self.assertEqual(r4.report_text(result), (ROOT / f'{r4.OUTPUT}.md').read_text(encoding='utf-8'))
        self.assertEqual(result['verdict']['improved'], r4.verdict(result['verdict']['comparison'])['improved'])


if __name__ == '__main__':
    unittest.main()
