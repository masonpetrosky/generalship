"""Best-estimate rules (docs/strength-estimates.md) on invented inputs, plus the real ledger replay."""

import copy
from fractions import Fraction
from pathlib import Path
import unittest

from generalship.estimates import EstimateError, check, classify, estimate_row, estimate_side, nested_sets
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]


def inp(iid, value, basis='reported_engaged', codes=(), loss='none', group='other', doc=None, hi=None, bound=None, **extra):
    x = {'id': iid, 'source_id': f'src-{iid}', 'printed': {'lower': value, 'upper': hi or value}, 'basis': basis,
         'codes': list(codes), 'loss_timing': loss, 'adjustments': [], 'bound': bound,
         'document_key': doc or f'doc-{iid}', 'independence_group': group}
    x.update(extra)
    return x


class ClassificationTests(unittest.TestCase):
    def test_partial_and_one_sided_are_bound_only_before_opponent_rows(self):
        # S1: an opponent's partial or one-sided figure never becomes a candidate.
        self.assertEqual(classify(inp('a', 100, codes=['adversary_or_hearsay_estimate', 'partial_scope']))[0], 'bound')
        self.assertEqual(classify(inp('a', 100, codes=['adversary_or_hearsay_estimate', 'one_sided_bound']))[0], 'bound')
        self.assertEqual(classify(inp('a', 100, codes=['other_engagement', 'partial_scope']))[0], 'unusable')

    def test_rows_in_order(self):
        self.assertEqual(classify(inp('a', 1, codes=['adversary_or_hearsay_estimate'], loss='not_prior')), ('C', 'opponent_or_hearsay'))
        self.assertEqual(classify(inp('a', 1, loss='not_prior')), ('C', 'post_start_information'))
        self.assertEqual(classify(inp('a', 1, codes=['scope_unresolved'])), ('C', 'applicability_unresolved'))
        self.assertEqual(classify(inp('a', 1, basis='unknown', loss='prior_engagements_only')), ('C', 'multiple_adjustments'))
        self.assertEqual(classify(inp('a', 1, loss='prior_engagements_only')), ('B', 'prior_engagements_only'))
        self.assertEqual(classify(inp('a', 1, basis='unknown')), ('B', 'basis_unknown'))
        self.assertEqual(classify(inp('a', 1, codes=['derivation_unknown'])), ('A', None))


class RuleTests(unittest.TestCase):
    def test_grade_a_median_range_and_rounding(self):
        e = estimate_side([inp('a', 1000), inp('b', 1200)])
        self.assertEqual((e['grade'], e['point'], e['low'], e['high']), ('A', 1000, 950, 1260))
        self.assertEqual(e['exact']['point'], '1000')

    def test_basis_order_and_other_bases_excluded_from_range(self):
        e = estimate_side([inp('pfd', 1000, basis='present_for_duty'), inp('eff', 900, basis='reported_effective')])
        self.assertEqual((e['point'], e['point_basis'], e['low'], e['high']), (900, 'reported_effective', 860, 950))

    def test_opponent_only_rule4_and_basis_filter(self):
        e = estimate_side([inp('o1', 2000, codes=['adversary_or_hearsay_estimate'], basis='unknown'),
                           inp('o2', 4000, codes=['adversary_or_hearsay_estimate'], basis='unknown')])
        self.assertEqual((e['point'], e['low'], e['high']), (1500, 1000, 4000))
        self.assertIn('opponent_estimate_point', e['labels'])

    def test_opponent_raises_high_but_never_sets_point(self):
        e = estimate_side([inp('own', 1000, basis='unknown'), inp('o', 5000, codes=['adversary_or_hearsay_estimate'], basis='unknown')])
        self.assertEqual((e['grade'], e['point'], e['low'], e['high']), ('B', 1000, 850, 5000))

    def test_compiled_copies_group_and_take_restrictive_class(self):
        # S4: an NPS/CWSAC figure equal to a loss-derived Livermore figure groups with it.
        e = estimate_side([inp('cw', 57018, group='nps-cwsac'),
                           inp('lv', 57018, basis='reported_effective', loss='not_prior', group='livermore-numbers-losses')])
        self.assertEqual((e['grade'], e['point_basis']), ('C', 'unknown'))
        self.assertIn('post_start_information', e['labels'])
        self.assertIn('compiled_dependence', e['labels'])
        self.assertTrue(nested_sets(estimate_row({'US': e, 'Confederate': e}))['excluded_post_start_information'])

    def test_same_document_different_basis_stay_separate(self):
        # A merged group would take the unknown basis and grade B (engine review A4).
        e = estimate_side([inp('a', 100, doc='d'), inp('b', 90, basis='reported_effective', doc='d')])
        self.assertEqual((e['grade'], e['point_basis'], e['point_groups']), ('A', 'reported_engaged', ['a']))

    def test_bounds_apply_only_on_point_basis_and_flag_conflict(self):
        e = estimate_side([inp('a', 1000), inp('cap', 1020, codes=['one_sided_bound'], bound='upper')])
        self.assertEqual(e['high'], 1020)
        e = estimate_side([inp('a', 1000), inp('cap', 900, codes=['one_sided_bound'], bound='upper')])
        self.assertIn('bound_conflict', e['labels'])
        e = estimate_side([inp('a', 1000), inp('cap', 900, basis='unknown', codes=['one_sided_bound'], bound='upper')])
        self.assertNotIn('bound_conflict', e['labels'])

    def test_lower_bounds_apply_or_conflict(self):
        e = estimate_side([inp('a', 1000), inp('lb', 980, codes=['partial_scope'], bound='lower')])
        self.assertEqual((e['low'], e['labels']), (980, ['single_input', 'whole_engagement_leakage']))
        e = estimate_side([inp('a', 1000), inp('lb', 1100, codes=['partial_scope'], bound='lower')])
        self.assertEqual(e['low'], 950)
        self.assertIn('bound_conflict', e['labels'])

    def test_bound_with_residual_class_c_is_not_applied(self):
        cap = inp('cap', 900, codes=['one_sided_bound'], bound='upper', loss='not_prior')
        self.assertEqual(classify(cap)[0], 'bound')
        e = estimate_side([inp('a', 1000), cap])
        self.assertEqual((e['high'], e['labels']), (1050, ['single_input', 'whole_engagement_leakage']))

    def test_post_start_candidates_enter_hull_only_when_used(self):
        e = estimate_side([inp('a', 1000), inp('ps', 2000, loss='not_prior')])
        self.assertEqual((e['point'], e['high']), (1000, 1050))
        self.assertNotIn('post_start_information', e['labels'])
        e = estimate_side([inp('p1', 1000, loss='not_prior'), inp('p2', 2000, loss='not_prior')])
        self.assertEqual((e['grade'], e['point'], e['low'], e['high']), ('C', 1000, 700, 2600))
        self.assertIn('post_start_information', e['labels'])

    def test_opponent_that_sets_high_carries_its_labels(self):
        # Engine review R1: a post-start opponent figure that sets high excludes the row.
        own = estimate_side([inp('own', 1000), inp('o', 5000, basis='unknown', loss='not_prior',
                                                    codes=['adversary_or_hearsay_estimate'])])
        self.assertEqual((own['high'], own['range_groups']), (5000, ['o', 'own']))
        self.assertIn('post_start_information', own['labels'])
        self.assertNotIn('single_input', own['labels'])
        row = estimate_row({'US': own, 'Confederate': estimate_side([inp('b', 900)])})
        self.assertTrue(nested_sets(row)['excluded_post_start_information'])

    def test_floor_applied(self):
        e = estimate_side([inp('o', 8, basis='unknown', codes=['adversary_or_hearsay_estimate'])])
        self.assertEqual((e['point'], e['low']), (10, 10))
        self.assertIn('floor_applied', e['labels'])

    def test_completed_sum_and_grade_d(self):
        parts = [inp('p1', 600, basis='unknown', codes=['partial_scope']), inp('p2', 400, basis='unknown', codes=['partial_scope'])]
        total = inp('sum', 1000, basis='unknown', adjustments=[{'kind': 'completed_sum', 'operands': ['p1', 'p2']}])
        e = estimate_side(parts + [total])
        self.assertEqual((e['grade'], e['point']), ('C', 1000))
        self.assertIn('partial_completed', e['labels'])
        d = estimate_side([inp('cap', 900, codes=['one_sided_bound'], bound='upper')])
        self.assertEqual((d['grade'], d['point']), ('D', None))

    def test_exact_rational_arithmetic(self):
        e = estimate_side([inp('a', 1001, basis='unknown')])
        self.assertEqual(Fraction(e['exact']['low']), Fraction(1001) * Fraction(17, 20))


class RowTests(unittest.TestCase):
    def test_basis_mixed_and_nested_sets(self):
        row = estimate_row({'US': estimate_side([inp('a', 1000)]),
                            'Confederate': estimate_side([inp('b', 900, basis='reported_effective')])})
        self.assertIn('basis_mixed', row['US']['labels'])
        self.assertEqual(nested_sets(row)['sets'], ['set1_A', 'set2_AB', 'set3_ABC'])
        row = estimate_row({'US': estimate_side([inp('a', 1000)]), 'Confederate': estimate_side([inp('b', 900, basis='unknown')])})
        self.assertIn('basis_mixed', row['Confederate']['labels'])
        self.assertEqual(nested_sets(row)['sets'], ['set2_AB', 'set3_ABC'])
        row = estimate_row({'US': estimate_side([inp('a', 1000)]), 'Confederate': estimate_side([])})
        self.assertNotIn('basis_mixed', row['US']['labels'])
        self.assertEqual(nested_sets(row), {'sets': [], 'excluded_post_start_information': False})


class LedgerTests(unittest.TestCase):
    def test_committed_ledger_reproduces(self):
        result = check(ROOT)
        self.assertEqual((result['in_scope'], result['out_of_scope']), (91, 36))
        self.assertFalse(result['fitted'])
        self.assertEqual(result['promoted_rows'], 0)

    def test_tampered_ledger_fails(self):
        base = read_json(ROOT / 'data/estimates/side-strength-v1.json')

        def tampered(message, change):
            ledger = copy.deepcopy(base)
            change(ledger, {e['battle_id']: e for e in ledger['engagements']})
            with self.assertRaisesRegex(EstimateError, message):
                check(ROOT, ledger=ledger)

        def first(e, side='Confederate'):
            return e['sides'][side]['inputs'][0]
        tampered('printed value', lambda L, E: first(E['TN003'])['printed'].update(lower=40336, upper=40336))
        tampered('does not reproduce', lambda L, E: first(E['TN003']).update(basis='reported_present'))
        tampered('does not reproduce', lambda L, E: E['TN003']['sides']['US']['estimate'].update(point=70000))
        tampered('nested-set', lambda L, E: E['TN003']['nested'].update(sets=[]))
        tampered('interval', lambda L, E: E['TN003'].update(interval=['1862-04-06', '1862-04-06']))
        tampered('unknown inputs', lambda L, E: E['TN003']['inventory']['dossier_claims'][0]['use'].append('us-missing'))
        tampered('constants', lambda L, E: L['constants'].update(opponent_factor='1/2'))
        tampered('Coverage', lambda L, E: L['engagements'].pop())


if __name__ == '__main__':
    unittest.main()
