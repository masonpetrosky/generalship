"""Best-estimate rules (docs/strength-estimates.md) on invented inputs, plus the real ledger replay."""

from fractions import Fraction
from pathlib import Path
import unittest

from generalship.estimates import check, classify, estimate_row, estimate_side, nested_sets

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
        e = estimate_side([inp('a', 100, doc='d'), inp('b', 90, basis='reported_effective', doc='d')])
        self.assertEqual(len(e['point_groups']) + len(e['range_groups']), 2)

    def test_bounds_apply_only_on_point_basis_and_flag_conflict(self):
        e = estimate_side([inp('a', 1000), inp('cap', 1020, codes=['one_sided_bound'], bound='upper')])
        self.assertEqual(e['high'], 1020)
        e = estimate_side([inp('a', 1000), inp('cap', 900, codes=['one_sided_bound'], bound='upper')])
        self.assertIn('bound_conflict', e['labels'])
        e = estimate_side([inp('a', 1000), inp('cap', 900, basis='unknown', codes=['one_sided_bound'], bound='upper')])
        self.assertNotIn('bound_conflict', e['labels'])

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


class LedgerTests(unittest.TestCase):
    def test_committed_ledger_reproduces(self):
        result = check(ROOT)
        self.assertEqual((result['in_scope'], result['out_of_scope']), (91, 36))
        self.assertFalse(result['fitted'])
        self.assertEqual(result['promoted_rows'], 0)


if __name__ == '__main__':
    unittest.main()
