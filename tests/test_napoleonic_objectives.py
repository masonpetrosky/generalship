"""Objective provenance, source accounting and non-scoring measurement contracts."""

import contextlib
import copy
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

from generalship import baseline
from generalship import napoleonic_objectives as pilot
from generalship import napoleonic_temporal_calibration_run as model_job

ROOT = Path(__file__).resolve().parents[1]


class ObjectivePilotTests(unittest.TestCase):
    def reject_change(self, path, change, message):
        read = pilot.read_json
        changed = copy.deepcopy(read(ROOT / path))
        change(changed)
        with patch.object(pilot, 'read_json', side_effect=lambda p: changed if p == ROOT / path else read(p)):
            with self.assertRaisesRegex(ValueError, message):
                pilot.build(ROOT)

    def test_complete_group_and_source_profile_without_fitters(self):
        with patch.object(baseline, 'fit_logistic') as base, patch.object(model_job, 'fit_logistic') as force, \
                patch.object(model_job, 'fit_offset') as offset, patch.object(model_job, 'load_outcomes') as outcomes:
            data = pilot.build(ROOT)
        for function in (base, force, offset, outcomes):
            function.assert_not_called()
        p = data['profile']
        self.assertEqual((p['entries'], p['sides'], p['duplicate_side_keys'], p['components']), (4, 8, 0, 19))
        self.assertEqual((p['passages'], p['images_inspected'], p['image_checked_passages']), (39, 26, 33))
        self.assertEqual(len(p['adopted_source_families']), 4)
        self.assertEqual((p['reported_before_action_sides'], p['reported_before_later_phase_only_sides'],
                          p['inferred_only_sides'], p['pre_action_document_sides']), (7, 0, 1, 0))
        self.assertEqual(len(p['missing_success_criteria']), 8)
        self.assertEqual(p['prior_citation_dispositions'], {'prior_reference_only': 27, 'used_for_bounded_pilot': 22})
        self.assertEqual(data['decision']['common_numerical_grade'], 'not_supported_by_this_pilot')
        self.assertEqual(data['decision']['reserved_final_entries_used'], 0)

    def test_frozen_bytes_reject_before_parsing(self):
        digest = pilot.digest
        with patch.object(pilot, 'digest', side_effect=lambda p: '0'*64 if p == ROOT / pilot.OBSERVATIONS else digest(p)), \
                patch.object(pilot, 'read_json') as read:
            with self.assertRaisesRegex(ValueError, 'changed frozen pilot record'):
                pilot.build(ROOT)
        read.assert_not_called()

    def test_scope_and_missing_side_cannot_change_the_denominator(self):
        final = pilot.read_json(ROOT / 'data/napoleonic/methods-v1/evaluation.json')['reserved_final'][0]
        self.reject_change(pilot.SCOPE, lambda d: d['entry_ids'].__setitem__(0, final), 'whole frozen development group')
        self.reject_change(pilot.OBSERVATIONS, lambda d: d['components'].pop(), 'complete eight-side coverage')

    def test_quote_ranges_and_bound_images_reject_tampering(self):
        self.reject_change(pilot.OBSERVATIONS,
                           lambda d: d['passages']['campo-conquest']['character_range'].__setitem__(0, 1),
                           'section-anchored quotation')
        self.reject_change(pilot.OBSERVATIONS,
                           lambda d: d['passages']['campo-conquest']['images'][0].__setitem__('sha256', '0'*64),
                           'bound image and source family')
        self.reject_change(pilot.OBSERVATIONS,
                           lambda d: d['passages']['campo-conquest'].__setitem__('metadata_sha256', '0'*64),
                           'source metadata binding')

    def test_documents_scores_durations_and_unknown_criteria_are_not_invented(self):
        self.reject_change(pilot.OBSERVATIONS, lambda d: d.__setitem__('common_grade', 0), 'no grade, promotion')
        self.reject_change(pilot.OBSERVATIONS,
                           lambda d: d['components'][0].__setitem__('pre_action_document_evidence', ['campo-attack-order']),
                           'no invented pre-action document')
        self.reject_change(pilot.OBSERVATIONS,
                           lambda d: d['components'][0].__setitem__('grade', 1), 'no added scores or weights')
        self.reject_change(pilot.OBSERVATIONS,
                           lambda d: d['components'][0].__setitem__('normalized_duration_days', 0),
                           'no invented normalized duration')
        self.reject_change(pilot.OBSERVATIONS,
                           lambda d: d['components'][0].__setitem__('success_criterion', None),
                           'determinate component needs its explicit criterion')

    def test_commentary_and_resistance_cannot_become_prior_mandates(self):
        def commentary(d):
            next(c for c in d['components'] if c['id'] == 'campo-counterfactual')['reported_precedence'] = 'before_relevant_action'
        def resistance(d):
            d['components'][-1]['reported_precedence'] = 'before_relevant_action'
        self.reject_change(pilot.OBSERVATIONS, commentary, 'commentary is not a prior mandate')
        self.reject_change(pilot.OBSERVATIONS, resistance, 'resistance does not establish a prior objective')

    def test_all_legacy_citations_are_honestly_accounted_for(self):
        self.reject_change(pilot.OBSERVATIONS, lambda d: d['prior_objective_claims'][0]['citations'].pop(),
                           'all prior citations accounted for')
        def mark_uninspected(d):
            row = next(c for r in d['prior_objective_claims'] for c in r['citations'] if not c['adopted_passages'])
            row['disposition'] = 'used_for_bounded_pilot'
        self.reject_change(pilot.OBSERVATIONS, mark_uninspected, 'prior pointer is not new verification')

    def test_extra_rows_and_cross_final_references_are_rejected(self):
        self.reject_change(pilot.OBSERVATIONS, lambda d: d['components'].append(copy.deepcopy(d['components'][0])),
                           'unique component IDs')
        final = pilot.read_json(ROOT / 'data/napoleonic/methods-v1/evaluation.json')['reserved_final'][0]
        self.reject_change(pilot.OBSERVATIONS, lambda d: d['components'][0]['related_entries'].append(final),
                           'bounded cross-entry references')

    def test_material_partial_and_unknown_cases_remain_visible(self):
        data = pilot.build(ROOT)
        rows = {r['id']: r for r in data['observations']['components']}
        self.assertEqual(rows['campo-junction']['attainment'], 'reported_incomplete_or_mixed')
        self.assertEqual(rows['maida-catanzaro']['attainment'], 'reported_incomplete_or_mixed')
        self.assertEqual(rows['maida-gaeta']['related_entries'], ['B371a'])
        self.assertEqual(rows['maida-gaeta']['attainment'], 'reported_effect_not_observed')
        self.assertEqual(rows['gaeta-early-defence']['reported_precedence'], 'before_relevant_action')
        self.assertIsNone(rows['gaeta-early-defence']['success_criterion'])
        self.assertIsNone(rows['gaeta-hold']['success_criterion'])
        self.assertIsNone(rows['gaeta-hold']['normalized_duration_days'])
        self.assertEqual(rows['gaeta-hold']['criterion_literal'], 'dix4iait jours*')
        self.assertEqual(rows['amantea-peace']['attainment'], 'not_established')
        self.assertEqual(rows['amantea-hold']['statement_kind'], 'inferred_disposition')
        self.assertEqual({r['id'] for r in rows.values() if r['attainment'] == 'reported_effect_observed'},
                         {'gaeta-capture', 'amantea-capture'})

    def test_notebook_structure_saved_outputs_and_fresh_execution(self):
        notebook = pilot.read_json(ROOT / pilot.NOTEBOOK)
        self.assertEqual((notebook['nbformat'], notebook['nbformat_minor']), (4, 5))
        self.assertEqual(notebook['metadata']['pilot_inputs'], pilot.build(ROOT)['input_sha256'])
        self.assertEqual(len(notebook['cells']), len({c['id'] for c in notebook['cells']}))
        namespace = {}; count = 0; previous_path = list(sys.path)
        try:
            with patch.object(baseline, 'fit_logistic') as fit, patch.object(model_job, 'load_outcomes') as outcomes:
                for cell in notebook['cells']:
                    self.assertIn(cell['cell_type'], ('markdown', 'code'))
                    self.assertIsInstance(cell['metadata'], dict)
                    if cell['cell_type'] != 'code':
                        continue
                    count += 1; stdout = io.StringIO()
                    with contextlib.redirect_stdout(stdout):
                        exec(compile(''.join(cell['source']), 'objective-audit-notebook', 'exec'), namespace)
                    self.assertEqual(cell['execution_count'], count)
                    self.assertEqual(cell['outputs'], [{'output_type': 'stream', 'name': 'stdout',
                                                        'text': stdout.getvalue().splitlines(keepends=True)}])
            fit.assert_not_called(); outcomes.assert_not_called()
        finally:
            sys.path[:] = previous_path
        self.assertEqual(count, 4)


if __name__ == '__main__':
    unittest.main()
