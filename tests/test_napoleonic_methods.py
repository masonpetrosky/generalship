"""Outcome-unused contracts and preparation checks; no experiment is run here."""

import copy
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from generalship import napoleonic_methods as methods
from generalship.research_checks import calibration, completion, numbers, write_json
from generalship.sources import read_json, digest

ROOT = Path(__file__).resolve().parents[1]


class MethodsTests(unittest.TestCase):
    def test_recorded_outcomes_and_strengths_cannot_change_the_schedule(self):
        frame, cohort = read_json(ROOT / methods.FRAME), read_json(ROOT / methods.COHORT)
        original = methods.schedule(frame['entries'], cohort['battle_ids'])
        for entry in frame['entries']:
            for key in ('outcome_side_a', 'winner_strength_printed', 'loser_strength_printed',
                        'winner_loss_printed', 'loser_loss_printed'):
                entry[key] = {'poison': 'must not be consumed'}
        self.assertEqual(methods.schedule(frame['entries'], cohort['battle_ids']), original)
        allowed = {'battle_id', 'campaign', 'war', 'year', 'a', 'b', 'a_issue', 'b_issue', 'a_printed', 'b_printed'}
        self.assertTrue(all(set(r) == allowed for r in original))

    def test_printed_orientation_swap_preserves_the_schedule(self):
        frame, cohort = read_json(ROOT / methods.FRAME), read_json(ROOT / methods.COHORT)
        original = methods.schedule(frame['entries'], cohort['battle_ids'])
        for entry in frame['entries']:
            entry['winner_commander_text'], entry['loser_commander_text'] = entry['loser_commander_text'], entry['winner_commander_text']
            entry['french_side'] = 'loser' if entry['french_side'] == 'winner' else 'winner'
        self.assertEqual(methods.schedule(frame['entries'], cohort['battle_ids']), original)

    def test_joint_labels_stay_uncredited_and_aliases_are_not_assumed(self):
        self.assertIsNone(methods.label('Marschällen Bernadotte und Soult')[0])
        self.assertIsNone(methods.label('Napoleon I. (80.000 M.)')[0])
        self.assertEqual(methods.label('Napoleon I.')[0], methods.label('Napoleon I')[0])
        self.assertNotEqual(methods.label('Lord Wellington')[0], methods.label('Gen.-Lt. Sir Wellesley')[0])

    def test_partitions_preserve_the_frozen_cohort_and_groups(self):
        frame, cohort = read_json(ROOT / methods.FRAME), read_json(ROOT / methods.COHORT)
        result = methods.evaluation(frame['entries'], cohort['battle_ids'], digest(ROOT / methods.FRAME), digest(ROOT / methods.COHORT))
        self.assertEqual(result, read_json(ROOT / methods.EVALUATION))
        a, b = set(result['development']), set(result['reserved_final'])
        self.assertEqual((len(a), len(b)), (273, 52))
        self.assertFalse(a & b)
        self.assertEqual(a | b, set(cohort['battle_ids']))
        self.assertTrue(all(set(ids) <= a or set(ids) <= b for ids in result['frozen_groups'].values()))
        self.assertFalse(result['authorizes_historical_outcome_fit'])

    def test_pilot_and_input_bindings_replay(self):
        _, _, _, pilot = methods.inputs(ROOT)
        self.assertFalse(pilot['estimable'])
        self.assertIsNone(pilot['replacement_at'])
        self.assertIsNone(pilot['eligible_replacements'])
        self.assertEqual(len(pilot['observations']), 3)

    def test_calibration_stays_unscored_and_keeps_stratum_denominators(self):
        sample, key = calibration(ROOT, read_json(ROOT / methods.PROTOCOL))
        self.assertEqual(len(sample['tasks']), 47)
        self.assertEqual(sample['strata']['unknown'], {'population': 15, 'sample': 15})
        self.assertTrue(all(x['sample'] == 8 for name, x in sample['strata'].items() if name != 'unknown'))
        self.assertEqual(len(sample['translation_subsample']), 8)
        self.assertIsNone(sample['reviewer'])
        self.assertFalse(sample['independent_review_performed'])
        for task in sample['tasks']:
            self.assertNotIn('claim_value', task)
            self.assertNotIn('author_rationale', task)
            self.assertTrue(all(v is None for v in task['judgment'].values()))
        self.assertEqual({t['sample_id'] for t in sample['tasks']}, {k['sample_id'] for k in key['entries']})

    def test_completion_requires_both_side_scopes_and_valid_claim_references(self):
        d = {'battle_id': 'test', 'claims': [{'id': 'strength', 'dimension': 'strength'},
                                           {'id': 'command', 'dimension': 'responsibility'}]}
        side = {'strength_claim_ids': ['strength'], 'command_claim_ids': ['command'],
                'strength_population_and_time': 'unknown', 'command_scope': 'unresolved', 'army_continuity': 'unknown'}
        d['research_completion'] = {'brief_version': 3, 'sides': {'A': copy.deepcopy(side), 'B': copy.deepcopy(side)},
                                    'additional_source_ids_checked': [], 'targeted_follow_up': {'performed': False},
                                    'stopping_reason': 'Sources exhausted', 'deferred_decision_relevant_gaps': []}
        completion(d, {})
        d['research_completion']['sides']['B']['command_claim_ids'] = ['missing']
        with self.assertRaisesRegex(ValueError, 'command_claim_ids'):
            completion(d, {})
        self.assertEqual(numbers('2,340 and 2.340; B363a; 9th'), {'2340'})

    def test_changed_execution_bindings_are_refused_before_an_experiment(self):
        protocol, frame, cohort, pilot = methods.inputs(ROOT)
        data = {'bindings': {'code': 'old'}, 'protocol': protocol}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_json(root / methods.RESULT, data)
            with patch.object(methods, 'inputs', return_value=(protocol, frame, cohort, pilot)), \
                    patch.object(methods, 'bindings', return_value={'code': 'new'}), \
                    patch('generalship.recovery.experiment') as experiment:
                with self.assertRaisesRegex(ValueError, 'different code or inputs'):
                    methods.run(root)
                experiment.assert_not_called()


if __name__ == '__main__':
    unittest.main()
