"""No promotion, complete denominators, source lineage and arithmetic regression checks."""

import copy
from pathlib import Path
import unittest
from unittest.mock import patch

from generalship import napoleonic_measurement as m

ROOT = Path(__file__).resolve().parents[1]


class MeasurementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = m.read_json(ROOT / m.RECORDS)

    def proposal(self):
        return copy.deepcopy(self.original)

    def rejects(self, data, text):
        with self.assertRaisesRegex(ValueError, text):
            m.validate(ROOT, data)

    def test_complete_campaign_and_source_local_progress(self):
        report = m.build(ROOT)
        self.assertEqual(report['counts'], {
            'entries': 8, 'sides': 16, 'indexed_claims': 59, 'passages': 56, 'images': 28,
            'source_metadata_records': 68, 'strength_observations': 39,
            'known_strength_observations': 32, 'explicit_strength_unknowns': 7,
            'authority_appearances': 43, 'source_local_co_reports': 6, 'arithmetic_checks': 7,
            'blocked_sides': 16, 'complete_opening_pairs': 0, 'emitted_model_rows': 0})

    def test_final_dossiers_never_opened(self):
        original = m.read_json
        final = set(original(ROOT / m.PARTITION)['reserved_final'])

        def read(path):
            path = Path(path)
            if path.parent.name == 'evidence' and path.stem in final:
                raise AssertionError('Final dossier opened')
            return original(path)

        with patch.object(m, 'read_json', side_effect=read):
            m.validate(ROOT)

    def test_rows_cannot_be_emitted(self):
        d = self.proposal(); d['emitted_model_rows'] = [{'battle_id': 'B431a'}]
        self.rejects(d, 'cannot promote or fit')

    def test_historical_fit_not_authorized(self):
        d = self.proposal(); d['historical_outcomes_fitted'] = True
        self.rejects(d, 'cannot promote or fit')

    def test_unknown_strength_cannot_become_zero(self):
        d = self.proposal(); next(o for o in d['observations'] if o['source_role'] == 'explicit_unknown')['value'] = 0
        self.rejects(d, 'invalid strength/precision')

    def test_unknown_cannot_acquire_invented_support(self):
        d = self.proposal(); next(o for o in d['observations'] if o['source_role'] == 'explicit_unknown')['evidence'] = ['p001']
        self.rejects(d, 'unknown must stay null')

    def test_nonfinite_or_boolean_strength_rejected(self):
        for value in (float('nan'), float('inf'), True):
            d = self.proposal(); d['observations'][0]['value'] = value
            self.rejects(d, 'invalid strength/precision')

    def test_guns_not_people(self):
        d = self.proposal(); d['observations'][0]['unit'] = 'guns'
        self.rejects(d, 'people/authority type confusion')

    def test_person_identity_not_inferred(self):
        d = self.proposal(); d['observations'][1]['resolved_person_id'] = 'wellington'
        self.rejects(d, 'global identity')

    def test_co_report_does_not_select_a_side(self):
        d = self.proposal(); d['side_records'][0]['selected_strength'] = 1738
        self.rejects(d, 'cannot select or impute')

    def test_sixteen_side_denominator_cannot_shrink(self):
        d = self.proposal(); d['side_records'].pop()
        self.rejects(d, 'sixteen-side denominator')

    def test_duplicate_side_not_a_second_engagement(self):
        d = self.proposal(); d['side_records'][-1] = copy.deepcopy(d['side_records'][0])
        self.rejects(d, 'sixteen-side denominator')

    def test_missing_claim_stays_in_denominator(self):
        d = self.proposal(); d['claim_index'].pop()
        self.rejects(d, 'claim denominator incomplete')

    def test_source_local_pair_cannot_cross_side_or_page(self):
        d = self.proposal(); d['co_reports'][0]['authority_id'] = 'B430b-B-a02'
        self.rejects(d, 'co-report force/entry mismatch')
        d = self.proposal(); d['co_reports'][0]['authority_id'] = 'B430b-A-a01'
        self.rejects(d, 'cannot cross source page')

    def test_diagnostic_residual_cannot_become_feature(self):
        d = self.proposal(); d['arithmetic_checks'][1]['opening_feature'] = 1738
        self.rejects(d, 'cannot become an opening feature')

    def test_arithmetic_error_not_hidden(self):
        d = self.proposal(); d['arithmetic_checks'][0]['result'] = 1938
        self.rejects(d, 'arithmetic mismatch')

    def test_phase_marker_not_a_selected_boundary(self):
        d = self.proposal(); d['entries'][0]['boundary_candidates'][0]['status'] = 'selected'
        self.rejects(d, 'unjustified selected/synchronized boundary')

    def test_parent_context_raw_range_is_replayed(self):
        d = self.proposal(); next(p for p in d['passages'] if p['origins'][0]['kind'] == 'existing_parent_context')['origins'][0]['start'] += 1
        self.rejects(d, 'context substring drift')

    def test_document_date_not_inferred_from_event(self):
        d = self.proposal(); d['passages'][0]['document_date'] = '1812-01-07'
        self.rejects(d, 'document date is not event time')

    def test_original_citation_and_page_remain_bound(self):
        d = self.proposal(); d['passages'][0]['citation']['quote'] = 'Invented quotation'
        self.rejects(d, 'quote/locator missing')

    def test_effective_appointments_cannot_replace_frozen_interval(self):
        d = self.proposal(); d['entries'][0]['frozen_interval']['start'] = '1812-01-08'
        self.rejects(d, 'changed frozen entry/interval')


if __name__ == '__main__':
    unittest.main()
