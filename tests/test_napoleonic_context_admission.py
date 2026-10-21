"""Boundary use, source accounting and non-promotion in the 1805 context audit."""

import contextlib
import copy
import io
from pathlib import Path
import unittest
from unittest.mock import patch

from generalship import baseline
from generalship import napoleonic_context_admission as audit
from generalship import napoleonic_temporal_calibration_run as model_job

ROOT = Path(__file__).resolve().parents[1]


class ContextAdmissionTests(unittest.TestCase):
    def reject_change(self, path, change, message):
        read = audit.read_json
        changed = copy.deepcopy(read(ROOT / path)); change(changed)
        with patch.object(audit, 'read_json', side_effect=lambda p: changed if p == ROOT / path else read(p)):
            with self.assertRaisesRegex(ValueError, message):
                audit.build(ROOT)

    def test_complete_group_and_exact_denominators_without_fitters(self):
        with patch.object(baseline, 'fit_logistic') as base, patch.object(model_job, 'fit_logistic') as force, \
                patch.object(model_job, 'fit_offset') as offset, patch.object(model_job, 'load_outcomes') as outcomes:
            bundle = audit.build(ROOT)
        for function in (base, force, offset, outcomes):
            function.assert_not_called()
        p = bundle['profile']
        self.assertEqual((p['entries'], p['engagement_fields'], p['source_claims']), (22, 44, 51))
        self.assertEqual((p['prior_citation_occurrences'], p['unique_prior_passages'], p['extra_context_passages']),
                         (405, 374, 5))
        self.assertEqual((p['text_sources'], p['registered_facsimiles'], p['images_reinspected']), (91, 77, 10))
        self.assertEqual(p['field_status_counts'], {'eligible_candidate': 6, 'blocked': 16, 'excluded': 22})
        self.assertEqual(p['claim_status_counts'], {'eligible_candidate': 6, 'blocked': 20, 'excluded': 25})
        self.assertEqual(p['complete_joint_entry_ids'], [])
        self.assertEqual(p['fortification_candidate_entry_ids'], ['B365b', 'B365c', 'B367a', 'B368a', 'B369c', 'B370a'])

    def test_changed_frozen_record_rejected_before_parsing(self):
        digest = audit.digest
        with patch.object(audit, 'digest', side_effect=lambda p: '0'*64 if p == ROOT / audit.OBSERVATIONS else digest(p)), \
                patch.object(audit, 'read_json') as read:
            with self.assertRaisesRegex(ValueError, 'changed frozen record'):
                audit.build(ROOT)
        read.assert_not_called()

    def test_reserved_final_entry_or_missing_claim_cannot_change_denominator(self):
        final = audit.read_json(ROOT / 'data/napoleonic/methods-v1/evaluation.json')['reserved_final'][0]
        self.reject_change(audit.SCOPE, lambda d: d['entry_ids'].__setitem__(0, final), 'whole frozen development group')
        self.reject_change(audit.OBSERVATIONS, lambda d: d['claims'].pop(), 'unique complete source-claim coverage')

    def test_raw_metadata_ranges_and_legacy_citation_identity_are_bound(self):
        self.reject_change(audit.OBSERVATIONS,
                           lambda d: d['passages']['p001']['character_range'].__setitem__(0, 0),
                           'section-anchored quotation')
        self.reject_change(audit.SNAPSHOT,
                           lambda d: next(iter(d['sources'].values()))['record'].__setitem__('publication_year', 2000),
                           'source metadata binding')
        self.reject_change(audit.OBSERVATIONS, lambda d: d['claims'][0]['citations'][0].__setitem__('passage_id', 'p002'),
                           'literal prior citation identity')

    def test_document_date_cannot_be_borrowed_from_adjacent_letter(self):
        self.reject_change(audit.OBSERVATIONS,
                           lambda d: d['passages']['parsdorf-no-blow'].__setitem__('document_date', '1805-10-12'),
                           'document date is not event or receipt date')

    def test_prior_image_binding_is_not_a_new_visual_inspection(self):
        def relabel(d):
            p = next(p for p in d['passages'].values() if p['registered_facsimile_source_id']
                     and not p['facsimile_reinspected'])
            p['facsimile_reinspected'] = True
        self.reject_change(audit.OBSERVATIONS, relabel, 'honest facsimile coverage')

    def test_realized_action_cannot_become_pre_contact_intent(self):
        self.reject_change(audit.OBSERVATIONS,
                           lambda d: d['claims'][0].__setitem__('audit_status', 'eligible_candidate'),
                           'realized posture cannot become prior intent')

    def test_none_named_requires_both_positions_and_never_means_two_zeroes(self):
        def lose_coverage(d):
            next(e for e in d['entries'] if e['battle_id'] == 'B365b')['position_coverage'] = 'named_positive_side'
        self.reject_change(audit.OBSERVATIONS, lose_coverage, 'none_named needs both position descriptions')
        self.reject_change(audit.OBSERVATIONS, lambda d: d['claims'][0]['physical_absence'].__setitem__('A', True),
                           'no invented physical absence')

    def test_earlier_works_need_scope_and_source_relative_precedence(self):
        def lose_ordering(d):
            next(e for e in d['entries'] if e['battle_id'] == 'B367a')['fortification_basis'] = 'permanent_building_only'
        self.reject_change(audit.OBSERVATIONS, lose_ordering, 'eligible works require sourced pre-contact scope')

    def test_all_prior_occurrences_and_honest_inspection_counts_are_required(self):
        self.reject_change(audit.OBSERVATIONS, lambda d: d['claims'][0]['citations'].pop(),
                           'all prior citation occurrences accounted for')
        self.reject_change(audit.OBSERVATIONS,
                           lambda d: d['inspection'].__setitem__('prior_citation_occurrences_inspected', 404),
                           'exact inspection denominators')

    def test_alternatives_are_not_votes_or_extra_rows(self):
        claim = lambda cid, status, code='B_fortified': {
            'battle_id': 'one', 'dimension': 'fortification', 'claim_id': cid,
            'audit_status': status, 'original_code': code}
        posture = {**claim('posture', 'excluded', 'A_attacked'), 'dimension': 'posture'}
        rows = [posture, claim('one-source', 'eligible_candidate'), claim('copied-source', 'eligible_candidate'),
                claim('unresolved', 'blocked', 'none_named')]
        fields = audit.field_rows(rows, ['one'])
        self.assertEqual(len(fields), 2)
        self.assertEqual(fields[1]['audit_status'], 'blocked')
        self.assertIsNone(fields[1]['candidate_code'])
        rows[-1]['audit_status'] = 'excluded'
        self.assertEqual(audit.field_rows(rows, ['one'])[1]['audit_status'], 'eligible_candidate')
        rows[-1]['audit_status'] = 'eligible_candidate'
        self.assertEqual(audit.field_rows(rows, ['one'])[1]['audit_status'], 'blocked')

    def test_material_cases_and_non_promotion_remain_visible(self):
        b = audit.build(ROOT); data = b['observations']
        claims = {(c['battle_id'], c['claim_id']): c for c in data['claims']}
        fields = {(f['battle_id'], f['dimension']): f for f in b['profile']['fields']}
        self.assertEqual(claims['B368b', 'fortification-schoenhals']['reason_codes'], ['known_postcontact_occupation'])
        self.assertEqual(fields['B368b', 'fortification']['audit_status'], 'blocked')
        self.assertEqual(claims['B368d', 'fortification-moriggl']['audit_status'], 'blocked')
        self.assertIn('parsdorf-no-blow', data['passages'])
        self.assertIn('caldiero-before-opening', data['passages'])
        self.assertIn('verona-preoccupied-works', data['passages'])
        self.reject_change(audit.OBSERVATIONS, lambda d: d.__setitem__('features_admitted', 6), 'no model, release')
        self.reject_change(audit.OBSERVATIONS, lambda d: d.__setitem__('commander_credit', 1), 'no model, release')

    def test_saved_artifact_and_report_match_verifier(self):
        b = audit.build(ROOT)
        self.assertEqual(audit.read_json(ROOT / audit.ARTIFACT), b)
        self.assertEqual((ROOT / audit.REPORT).read_text(), audit.report(b))

    def test_notebook_structure_execution_and_saved_outputs(self):
        nb = audit.read_json(ROOT / audit.NOTEBOOK)
        self.assertEqual((nb['nbformat'], nb['nbformat_minor']), (4, 5))
        self.assertEqual(nb['metadata']['audit_inputs'], audit.build(ROOT)['input_sha256'])
        self.assertEqual(len(nb['cells']), len({c['id'] for c in nb['cells']}))
        namespace = {}; count = 0
        with patch.object(baseline, 'fit_logistic') as fit, patch.object(model_job, 'load_outcomes') as outcomes:
            for cell in nb['cells']:
                self.assertIsInstance(cell['metadata'], dict)
                self.assertIsInstance(cell['source'], list)
                if cell['cell_type'] == 'markdown':
                    continue
                self.assertEqual(cell['cell_type'], 'code')
                count += 1; stdout = io.StringIO()
                with contextlib.redirect_stdout(stdout):
                    exec(compile(''.join(cell['source']), 'context-admission-notebook', 'exec'), namespace)
                self.assertEqual(cell['execution_count'], count)
                self.assertEqual(cell['outputs'], [{'output_type': 'stream', 'name': 'stdout',
                                                    'text': stdout.getvalue().splitlines(keepends=True)}])
        fit.assert_not_called(); outcomes.assert_not_called()
        self.assertEqual(count, 4)


if __name__ == '__main__':
    unittest.main()
