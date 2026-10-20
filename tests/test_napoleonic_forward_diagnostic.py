"""Diagnostic arithmetic, denominator integrity and passage tampering; no fits."""

import copy
from pathlib import Path
import unittest
from unittest.mock import patch

from generalship import napoleonic_benchmark_run as runner
from generalship import napoleonic_forward_diagnostic as diagnostic

ROOT = Path(__file__).resolve().parents[1]


class ArithmeticTests(unittest.TestCase):
    def test_record_comparison_allows_only_tiny_arithmetic_rounding(self):
        record = {'n': 37, 'hash': 'abc', 'value': [.25]}
        diagnostic.compare_records(record, {'n': 37, 'hash': 'abc', 'value': [.25 + 1e-13]})
        for other in [{'n': 37.0, 'hash': 'abc', 'value': [.25]},
                      {'n': 37, 'hash': 'changed', 'value': [.25]},
                      {'n': 37, 'hash': 'abc', 'value': [.25 + 1e-6]}]:
            with self.subTest(other=other), self.assertRaises(ValueError):
                diagnostic.compare_records(record, other)

    def test_auc_counts_ties_and_retains_undefined_single_class(self):
        result = diagnostic.auc_pairs([.9, .4, .4, .1], [1, 1, 0, 0])
        self.assertEqual(result, {'positive': 2, 'negative': 2, 'pairs': 4,
                                  'concordant': 3, 'tied': 1, 'auc': .875})
        self.assertIsNone(diagnostic.auc_pairs([.9, .8], [1, 1])['auc'])
        self.assertIsNone(diagnostic.auc_pairs([], [])['auc'])
        with self.assertRaises(ValueError):
            diagnostic.auc_pairs([.9], [1, 0])

    def test_brier_identity_on_constructed_forecasts(self):
        result = diagnostic.brier_accounting([{'force': p, 'y': y}
                                              for p, y in zip([.9, .6, .4, .2], [1, 0, 1, 0])])
        self.assertAlmostEqual(result['brier'], .1925)
        self.assertAlmostEqual(result['force_minus_equal_brier'], -.0575)
        self.assertAlmostEqual(result['brier'], result['mean_bias_squared'] + result['prediction_variance']
                               + result['outcome_variance'] - 2 * result['covariance'])

    def test_paired_scores_separate_case_removal_and_saved_model_changes(self):
        primary = [{'battle_id': b, 'force': p, 'y': y} for b, p, y in
                   [('a', .8, 1), ('b', .7, 0), ('c', .2, 0)]]
        sensitivity = [{'battle_id': b, 'force': p, 'y': y} for b, p, y in
                       [('a', .75, 1), ('b', .6, 0)]]
        result = diagnostic.paired_sensitivity(primary, sensitivity)
        self.assertEqual(result['removed_ids'], ['c'])
        for metric, terms in result['differences'].items():
            self.assertAlmostEqual(terms['total_difference'], terms['case_removal_difference']
                                   + terms['same_row_saved_model_difference'])
            self.assertAlmostEqual(result['primary_all'][metric],
                                   (2 * result['primary_common'][metric] + result['primary_removed'][metric]) / 3)
        sensitivity[0]['y'] = 0
        with self.assertRaisesRegex(ValueError, 'paired labels'):
            diagnostic.paired_sensitivity(primary, sensitivity)

    def test_largest_error_rule_covers_unrepresented_campaign(self):
        rows = [{'battle_id': str(i), 'campaign_group': 'one', 'force': .9 - i * .01, 'y': 0}
                for i in range(6)]
        rows.append({'battle_id': 'other', 'campaign_group': 'two', 'force': .1, 'y': 0})
        self.assertEqual(diagnostic.selected_errors(rows), ['0', '1', '2', '3', '4', 'other'])


class SavedDiagnosticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch.object(runner, 'fit_logistic') as fit:
            cls.result = diagnostic.build(ROOT)
        fit.assert_not_called()

    def test_saved_diagnostic_reconciles_and_reserves_final_entries(self):
        d = self.result
        diagnostic.compare_records(d, diagnostic.read_json(ROOT / diagnostic.OUTPUT))
        self.assertEqual(diagnostic.report(d), (ROOT / diagnostic.REPORT).read_text(encoding='utf-8'))
        self.assertEqual((len(d['all_37_saved_predictions_by_loss']), len(d['all_27_exclusions'])), (37, 27))
        self.assertEqual((d['coverage']['through_1812']['all']['n'], d['coverage']['1813']['all']['n']), (209, 64))
        self.assertEqual(d['discrimination']['concordant'], 247)
        self.assertEqual(d['discrimination']['pairs'], 312)
        self.assertAlmostEqual(d['discrimination']['auc'], 247 / 312)
        self.assertAlmostEqual(d['brier_accounting']['brier'], .2510568809916732)
        self.assertEqual(d['historical_refits_performed'], 0)
        self.assertEqual(d['reserved_final_entries_used'], 0)
        self.assertEqual(d['reserved_final_entries'], 52)

    def test_changed_frozen_input_binding_is_rejected(self):
        read = diagnostic.read_json
        scope = copy.deepcopy(read(ROOT / diagnostic.SCOPE))
        scope['bindings'][diagnostic.saved.RESULT] = '0' * 64
        with patch.object(diagnostic, 'read_json', side_effect=lambda p: scope if p == ROOT / diagnostic.SCOPE else read(p)):
            with self.assertRaisesRegex(ValueError, 'changed frozen diagnostic input'):
                diagnostic.build(ROOT)

    def test_altered_passage_figures_quotation_and_image_are_rejected(self):
        record = diagnostic.read_json(ROOT / diagnostic.EVIDENCE)
        indexed = {r['battle_id']: r for r in diagnostic.read_json(ROOT / 'artifacts/napoleonic-benchmark-v1.json')['entries']}
        predictions = diagnostic.read_json(ROOT / diagnostic.saved.RESULT)['populations']['primary']['forward_1813']['predictions']
        changes = [lambda c: c['personnel_totals'].update(A=1),
                   lambda c: c['citation'].update(quote='An invented passage'),
                   lambda c: c['page_image'].update(sha256='0' * 64)]
        for change in changes:
            altered = copy.deepcopy(record)
            change(altered['checks'][0])
            with self.subTest(change=change), self.assertRaises(ValueError):
                diagnostic.verify_passages(ROOT, altered, None, indexed, predictions)


if __name__ == '__main__':
    unittest.main()
