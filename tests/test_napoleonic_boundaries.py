"""Measurement failure modes; no model jobs, source fetching or invented review."""

from copy import deepcopy
import unittest
from unittest.mock import patch

from generalship import napoleonic_boundaries as n
from generalship.sources import read_json


class BoundaryContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bundle = read_json(n.ROOT / n.RECORDS)

    def changed(self):
        return deepcopy(self.bundle)

    def reject(self, bundle, message):
        with self.assertRaisesRegex(ValueError, message):
            n.validate(n.ROOT, bundle)

    def case(self, bundle, key):
        return next(r for r in bundle['membership_cases'] if r['id'] == key)

    def test_frozen_specification_has_all_eight_sides_and_no_force_pair(self):
        report = n.check(n.ROOT)
        self.assertEqual((report['engagements'], report['sides'], report['prior_strength_observations_indexed']), (4, 8, 43))
        self.assertEqual((report['unresolved_joint_opening_sides'], report['complete_candidate_engagements']), (8, 0))
        self.assertEqual(report['emitted_model_rows'], [])
        self.assertEqual(report['status'], 'primary-verified specification')

    def test_missing_side_cannot_improve_coverage(self):
        b = self.changed()
        b['sides'].pop()
        self.reject(b, 'side coverage')

    def test_duplicate_side_is_rejected(self):
        b = self.changed()
        b['sides'].append(deepcopy(b['sides'][0]))
        self.reject(b, 'side coverage')

    def test_old_strength_alternative_cannot_disappear(self):
        b = self.changed()
        b['sides'][0]['prior_strength_ids'].pop()
        self.reject(b, 'side accounting')

    def test_no_boundary_strength_person_or_army_can_be_selected(self):
        for field in ('selected_boundary', 'selected_strength', 'army_id', 'responsible_person_id'):
            with self.subTest(field=field):
                b = self.changed()
                b['sides'][0][field] = 'unsupported-selection'
                self.reject(b, 'cannot select model inputs')

    def test_no_model_rows_or_calibration_judgments(self):
        for field, value in [('emitted_model_rows', [{'invented': True}]),
                             ('historical_outcomes_fitted', True), ('calibration', 'scored')]:
            with self.subTest(field=field):
                b = self.changed()
                b[field] = value
                self.reject(b, 'cannot promote, fit or score')

    def test_altered_quote_is_rejected(self):
        b = self.changed()
        b['passages'][0]['citation']['quote'] = 'unsupported invented passage'
        self.reject(b, 'quote absent')

    def test_document_date_cannot_borrow_a_historical_event_date(self):
        b = self.changed()
        b['passages'][0]['document_date'] = '1806-03-09'
        self.reject(b, 'section document date')

    def test_transcript_cannot_claim_a_different_page_image(self):
        b = self.changed()
        b['passages'][0]['facsimile_source_id'] = b['passages'][-1]['facsimile_source_id']
        b['passages'][0]['facsimile_sha256'] = b['passages'][-1]['facsimile_sha256']
        self.reject(b, 'facsimile binding')

    def test_source_ordering_cycles_are_rejected(self):
        b = self.changed()
        edge = deepcopy(b['orderings'][0])
        edge['id'] = 'constructed-reverse-edge'
        edge['before'], edge['after'] = edge['after'], edge['before']
        b['orderings'].append(edge)
        self.reject(b, 'ordering cycle')

    def test_cross_account_clock_is_not_inferred(self):
        b = self.changed()
        b['orderings'].append({'id': 'constructed-cross-account', 'battle_id': 'B370c',
                              'before': 'ct-recon', 'after': 'ct-damas', 'basis': 'narrative_sequence',
                              'note': 'Constructed invalid ordering.', 'evidence': ['ct-damas']})
        self.reject(b, 'mixes source clocks')

    def test_a_timing_path_cannot_switch_source_families_at_a_shared_event(self):
        b = self.changed()
        later = deepcopy(next(r for r in b['events'] if r['id'] == 'g-opening'))
        later.update(id='constructed-later-colletta', kind='later_presence', evidence=['g-colletta'])
        b['events'].append(later)
        for before, after, evidence in [('g-rifles', 'g-opening', ['g-rifles', 'g-preopening-fire']),
                                        ('g-opening', later['id'], ['g-colletta'])]:
            b['orderings'].append({'id': 'constructed-' + before + '--' + after,
                                  'battle_id': 'B371a', 'before': before, 'after': after,
                                  'basis': 'narrative_sequence', 'note': 'Constructed path test only.',
                                  'evidence': evidence})
        row = self.case(b, 'g-b-july')
        row.update(scenario_id='g-initial', timing='later_presence_only',
                   time_event_id=later['id'], evidence=['g-rifles', 'g-colletta'])
        self.reject(b, 'unsupported later ordering')

    def test_investment_cannot_be_relabelled_first_contact(self):
        b = self.changed()
        next(r for r in b['scenarios'] if r['id'] == 'a-investment')['contact_status'] = 'source_relative_candidate'
        self.reject(b, 'noncontact cannot become first contact')

    def test_missing_evidence_reference_is_rejected(self):
        b = self.changed()
        b['events'][0]['evidence'] = ['unknown-passage']
        self.reject(b, 'evidence reference')

    def test_later_departure_exclusion_needs_a_source_ordering(self):
        b = self.changed()
        b['orderings'] = [r for r in b['orderings'] if r['id'] != 'a-invest--a-verdier']
        self.reject(b, 'unsupported later ordering')

    def test_prior_presence_does_not_prove_continued_availability(self):
        b = self.changed()
        row = self.case(b, 'g-a-local-july')
        row['timing'], row['decision'] = 'present_by_anchor', 'candidate_component'
        self.reject(b, 'prior presence alone')

    def test_later_presence_does_not_become_a_late_departure(self):
        b = self.changed()
        row = self.case(b, 'm-b-ross')
        row['timing'], row['decision'] = 'departure_after_anchor', 'excluded_timing'
        self.reject(b, 'not proof of later departure')

    def test_scenario_cannot_cross_engagements(self):
        b = self.changed()
        self.case(b, 'm-b-ross')['scenario_id'] = 'ct-approach'
        self.reject(b, 'membership reference')

    def test_declared_candidate_must_follow_the_membership_rule(self):
        b = self.changed()
        self.case(b, 'ct-a-cavalry')['decision'] = 'candidate_component'
        self.reject(b, 'incorrect conditional membership decision')

    def test_worked_cases_keep_inconvenient_distinctions(self):
        report = n.validate(n.ROOT)
        decisions = report['membership_decisions']
        self.assertEqual(decisions['ct-a-cavalry'], 'unresolved')
        self.assertEqual(decisions['m-b-light-company'], 'unresolved')
        self.assertEqual(decisions['m-b-ross'], 'unresolved')
        self.assertEqual(decisions['g-a-posts'], 'unresolved')
        self.assertEqual(decisions['a-a-verdier'], 'excluded_timing')
        self.assertEqual(decisions['a-b-inhabitants'], 'excluded_population')

    def test_unresolved_relations_remain_absent(self):
        edges = self.bundle['orderings']
        self.assertFalse(n.reaches(edges, 'ct-recon', 'ct-damas'))
        self.assertFalse(n.reaches(edges, 'g-state', 'g-fire'))
        self.assertFalse(n.reaches(edges, 'a-reynier', 'a-formal'))
        self.assertTrue(n.reaches(edges, 'm-artillery', 'm-ross'))

    def test_verification_cannot_claim_an_independent_review(self):
        original = n.read_json

        def reader(path):
            value = original(path)
            if path == n.ROOT / n.VERIFICATION:
                value['independent_review'] = True
            return value

        with patch.object(n, 'read_json', side_effect=reader):
            with self.assertRaisesRegex(ValueError, 'primary verification identity'):
                n.check(n.ROOT)

    def test_primary_binding_detects_changed_executed_code(self):
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as folder:
            fake_code = n.ROOT.__class__(folder)
            for path in n.CODE:
                target = fake_code / path
                target.parent.mkdir(exist_ok=True, parents=True)
                target.write_bytes((n.ROOT / path).read_bytes())
            (fake_code / n.CODE[0]).write_text('# altered code\n', encoding='utf-8')
            with patch.object(n, 'ROOT', fake_code):
                with self.assertRaisesRegex(ValueError, 'stale primary verification bindings'):
                    n.check(DATA_ROOT)


# Data root stays real in the changed-code test; executed-code bindings use n.ROOT.
DATA_ROOT = n.ROOT


if __name__ == '__main__':
    unittest.main()
