"""Saved historical arithmetic and tamper rejection, without any refitting."""

import copy
from pathlib import Path
import unittest
from unittest.mock import patch

from generalship import baseline
from generalship import napoleonic_benchmark_run as original_runner
from generalship import napoleonic_temporal_calibration_report as report
from generalship import napoleonic_temporal_calibration_run as runner

ROOT = Path(__file__).resolve().parents[1]


class SavedTemporalRunTests(unittest.TestCase):
    def reject_change(self, change, message):
        read = report.read_json
        changed = copy.deepcopy(read(ROOT / report.RESULT))
        change(changed)
        # Preserve the on-disk hash guard while exercising arithmetic on an
        # altered parsed record. No immutable file is written or rebound.
        with patch.object(report, 'read_json', side_effect=lambda p: changed if p == ROOT / report.RESULT else read(p)):
            with self.assertRaisesRegex(ValueError, message):
                report.verify(ROOT)

    def test_all_saved_values_reconcile_without_fitting_or_runner_label_access(self):
        with patch.object(baseline, 'fit_logistic') as base, \
                patch.object(original_runner, 'fit_logistic') as old, \
                patch.object(runner, 'fit_logistic') as force, patch.object(runner, 'fit_offset') as offset, \
                patch.object(runner, 'load_outcomes') as labels:
            *_, verification = report.verify(ROOT)
        for function in (base, old, force, offset, labels):
            function.assert_not_called()
        self.assertEqual(verification['checks'], {
            'annual_role_assignments_checked': 36, 'force_stationarity_checks': 48,
            'offset_stationarity_checks': 24, 'probability_values_checked': 3534,
            'prediction_rows_checked': 589, 'summaries_checked': 80, 'metric_values_checked': 1632,
            'calibration_bins_checked': 4800, 'paired_case_contributions_checked': 2945,
            'original_forward_prediction_rows_matched': 141})
        self.assertEqual(verification['reserved_final_entries_used'], 0)
        self.assertEqual(verification['historical_refits_performed'], 0)
        self.assertEqual(verification['continuation'], 'does_not_pass')

    def test_changed_result_hash_rejects_before_parsing(self):
        digest = report.digest
        with patch.object(report, 'digest', side_effect=lambda p: '0'*64 if p == ROOT / report.RESULT else digest(p)), \
                patch.object(report, 'read_json') as read:
            with self.assertRaisesRegex(ValueError, 'immutable executed result'):
                report.verify(ROOT)
        read.assert_not_called()

    def test_training_leakage_and_wrong_time_roles_are_rejected(self):
        def leakage(record):
            f = record['populations']['primary']['parameters'][3]
            f['base_ids'].append(f['test_ids'][0])
        def cutoff(record):
            record['populations']['primary']['parameters'][3]['cutoff'] = '1809-01-01'
        for change in (leakage, cutoff):
            with self.subTest(change=change.__name__):
                self.reject_change(change, 'saved temporal role')

    def test_saved_force_and_offset_parameters_must_satisfy_training_equations(self):
        def force(record):
            record['populations']['primary']['parameters'][3]['base_slope'] += .1
        def offset(record):
            record['populations']['primary']['parameters'][3]['offset'] += .1
        self.reject_change(force, 'force score equations')
        self.reject_change(offset, 'offset score equation')

    def test_probability_and_both_weightings_are_recomputed(self):
        def probability(record):
            record['populations']['primary']['predictions'][0]['offset_force'] += .01
        def battle(record):
            record['populations']['primary']['regions']['decision']['metrics']['battle']['offset_force']['log_loss'] += .01
        def campaign(record):
            record['populations']['primary']['regions']['decision']['metrics']['equal_campaign']['offset_force']['brier'] += .01
        for change in (probability, battle, campaign):
            with self.subTest(change=change.__name__):
                self.reject_change(change, '!=')

    def test_calibration_unknowns_and_case_concentration_are_preserved(self):
        def unknown(record):
            record['populations']['primary']['regions']['decision']['calibration']['battle']['offset_force'][0]['mean_probability'] = 0.
        def paired_loss(record):
            record['populations']['primary']['paired_loss_contributions']['expanding_force'][0]['log_loss_difference'] += .01
        def concentration(record):
            record['populations']['primary']['absolute_loss_concentration']['expanding_force']['decision']['top_shares']['5'] += .01
        self.reject_change(unknown, 'value')
        self.reject_change(paired_loss, '!=')
        self.reject_change(concentration, '!=')

    def test_decision_cannot_be_relabelled_as_success(self):
        self.reject_change(lambda r: r['continuation'].update(status='passes_exploratory_continuation_rule'),
                           'fixed continuation decision.status')

    def test_secondary_scores_cannot_change_separate_decision_recomputation(self):
        run = report.read_json(ROOT / report.RESULT)
        protocol = report.read_json(ROOT / report.prep.PROTOCOL)
        expected = report.continuation(run['populations'], protocol)
        for population in run['populations'].values():
            population['regions']['reused_1813_secondary'] = 'never read by decision'
            population['per_year']['1813'] = 'never read by decision'
        self.assertEqual(report.continuation(run['populations'], protocol), expected)
        del run['populations']['primary']['per_year']['1808']
        self.assertEqual(report.continuation(run['populations'], protocol)['status'], 'not_assessable')


if __name__ == '__main__':
    unittest.main()
