"""Saved-result verification, including adversarial arithmetic checks; no fits."""

import copy
from pathlib import Path
import unittest
from unittest.mock import patch

from generalship import napoleonic_benchmark_report as report
from generalship import napoleonic_benchmark_run as runner

ROOT = Path(__file__).resolve().parents[1]


class SavedRunTests(unittest.TestCase):
    def reject_in_memory_change(self, change, message):
        read = report.read_json
        changed = copy.deepcopy(read(ROOT / report.RESULT))
        change(changed['populations']['primary']['leave_campaign_out'])
        # The on-disk hash guard is retained. Replacing just the parsed result
        # exercises the separate arithmetic checks without changing pinned files.
        with patch.object(report, 'read_json', side_effect=lambda path: changed if path == ROOT / report.RESULT else read(path)):
            with self.assertRaisesRegex(ValueError, message):
                report.verify(ROOT)

    def test_saved_run_reconciles_without_any_optimizer_call(self):
        with patch.object(runner, 'fit_logistic') as fit:
            *_, verification = report.verify(ROOT)
        fit.assert_not_called()
        self.assertEqual(verification['checks'], {
            'folds_checked': 80, 'optimizer_stationarity_checks': 80, 'predictions_checked': 1629,
            'summary_metric_values_checked': 144, 'calibration_bins_checked': 360,
            'per_group_metric_values_checked': 480, 'bootstrap_interval_endpoints_checked': 32})
        self.assertEqual(verification['reserved_final_entries_used'], 0)

    def test_contaminated_training_membership_is_rejected(self):
        def contaminate(result):
            result['folds'][0]['train_ids'].append(result['folds'][0]['test_ids'][0])
        self.reject_in_memory_change(contaminate, 'fold membership')

    def test_probability_and_metric_changes_are_rejected_by_recomputation(self):
        def probability(result):
            result['predictions'][0]['force'] += 0.01
        def metric(result):
            result['metrics']['battle']['force']['log_loss'] += 0.01
        for change in (probability, metric):
            with self.subTest(change=change.__name__):
                self.reject_in_memory_change(change, '!=')

    def test_changed_bootstrap_endpoint_is_rejected(self):
        def change(result):
            result['bootstrap']['training_prior']['force_minus_comparator_log_loss']['equal_group'][1] += 0.01
        self.reject_in_memory_change(change, '!=')


if __name__ == '__main__':
    unittest.main()
