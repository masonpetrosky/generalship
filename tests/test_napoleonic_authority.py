"""Source/authority/continuity failure modes; no network, model job or separate review."""

from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from generalship import napoleonic_authority as n
from generalship.sources import read_json

DATA_ROOT = n.ROOT


class AuthorityMappingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = read_json(DATA_ROOT / n.MAPPINGS)

    def changed(self):
        return deepcopy(self.data)

    def reject(self, data, message):
        with self.assertRaisesRegex(ValueError, message):
            n.validate(DATA_ROOT, data)

    def identity(self, data, key):
        return next(r for r in data['identity_links'] if r['id'] == key)

    def test_committed_mapping_retains_denominators_and_no_model_rows(self):
        report = n.check(DATA_ROOT)
        self.assertEqual((report['engagements'], report['sides'], report['original_roles_indexed'], report['additional_roles']), (4, 8, 28, 2))
        self.assertEqual((report['continuity_pairs'], report['established_continuity_pairs']), (12, 0))
        self.assertEqual((report['unresolved_opening_sides'], report['complete_candidate_engagements']), (8, 0))
        self.assertEqual(report['emitted_model_rows'], [])

    def test_source_local_links_are_not_global_people(self):
        report = n.validate(DATA_ROOT)
        self.assertEqual(report['identity_status_counts'], {'source_local_coreference': 4, 'unresolved': 8})
        self.assertTrue(all(r['resolved_person_id'] is None for r in self.data['roles']))

    def test_same_operation_name_similarity_cannot_be_source_local_identity(self):
        data = self.changed()
        row = self.identity(data, 'stuart-stewart')
        row.update(status='source_local_coreference', basis='continuous_episode')
        self.reject(data, 'source-local identity crosses')

    def test_repeated_commander_name_cannot_link_entries_as_one_episode(self):
        data = self.changed()
        self.identity(data, 'reynier-cross-entry').update(status='source_local_coreference', basis='continuous_episode')
        self.reject(data, 'source-local identity crosses')

    def test_episode_link_is_not_same_document_proof(self):
        data = self.changed()
        self.identity(data, 'damas-within-koch')['basis'] = 'same_document'
        self.reject(data, 'same-document identity crosses')

    def test_unread_fullname_cannot_replace_a_literal_mention(self):
        data = self.changed()
        data['identity_links'][0]['mentions'][0]['label'] = 'Invented complete biographical identity'
        self.reject(data, 'identity label absent')

    def test_hotz_storz_hypothesis_cannot_be_silently_merged(self):
        data = self.changed()
        self.identity(data, 'hotz-storz')['resolved_person_id'] = 'invented-merged-person'
        self.reject(data, 'identity status/person')

    def test_an_unresolved_identity_question_cannot_disappear(self):
        data = self.changed()
        data['identity_links'] = [r for r in data['identity_links'] if r['id'] != 'franceschi-role-identity']
        self.reject(data, 'identity question coverage')

    def test_original_role_name_and_scope_remain_immutable(self):
        data = self.changed()
        data['roles'][0]['actor_label'] = 'silently normalized actor'
        self.reject(data, 'original role altered')

    def test_original_role_citation_must_still_be_present(self):
        data = self.changed()
        row = next(r for r in data['roles'] if r['id'] == 'B371a-B-command-koch-hotz')
        row['evidence'].pop(0)
        self.reject(data, 'original role evidence omitted')

    def test_no_extra_role_outside_the_two_declared_examples(self):
        data = self.changed()
        role = deepcopy(data['roles'][-1])
        role['id'] = 'unscoped-extra-role'
        data['roles'].append(role)
        self.reject(data, 'additional role scope changed')

    def test_document_date_cannot_become_an_appointment_or_transfer_clock(self):
        for field in ('appointment_start', 'appointment_end', 'effective_transfer_at'):
            with self.subTest(field=field):
                data = self.changed()
                data['roles'][-1][field] = '1806-07-18T23:00:00'
                self.reject(data, 'invented appointment/transfer')

    def test_reconciliation_does_not_manufacture_exclusive_handover(self):
        data = self.changed()
        data['reconciliations'][2]['effective_transfer_at'] = '1806-05-18'
        self.reject(data, 'unfounded handover')

    def test_complete_side_mapping_cannot_select_person_strength_or_army(self):
        for field in ('selected_boundary', 'selected_strength', 'selected_person_id', 'army_id'):
            with self.subTest(field=field):
                data = self.changed()
                data['forces'][0][field] = 'unsupported-selection'
                self.reject(data, 'force mapping cannot select')

    def test_missing_side_and_duplicate_side_are_rejected(self):
        data = self.changed()
        data['forces'].pop()
        self.reject(data, 'force side coverage')
        data = self.changed()
        data['forces'].append(deepcopy(data['forces'][0]))
        self.reject(data, 'duplicate record ID')

    def test_no_continuity_pair_can_be_omitted_or_duplicated(self):
        data = self.changed()
        data['continuity_pairs'].pop()
        self.reject(data, 'continuity pair coverage')
        data = self.changed()
        row = deepcopy(data['continuity_pairs'][0])
        row['id'] = 'duplicate-pair-different-id'
        data['continuity_pairs'].append(row)
        self.reject(data, 'continuity pair coverage')

    def test_same_commander_cannot_establish_an_army(self):
        data = self.changed()
        data['continuity_pairs'][0].update(status='established', army_id='reynier-army')
        self.reject(data, 'continuity cannot merge')

    def test_staff_office_cannot_identify_the_whole_army(self):
        data = self.changed()
        data['organization_context'][-1]['army_id'] = 'first-corps-as-army'
        self.reject(data, 'organization context cannot establish army')

    def test_quote_and_document_date_bindings_are_checked(self):
        data = self.changed()
        data['passages'][0]['citation']['quote'] = 'fabricated authority'
        self.reject(data, 'quote absent')
        data = self.changed()
        data['passages'][0]['document_date'] = '1806-03-09'
        self.reject(data, 'section document date')

    def test_fitting_promotion_and_calibration_scoring_are_rejected(self):
        for field, value in [('emitted_model_rows', [{'invented': True}]),
                             ('historical_outcomes_fitted', True), ('calibration', 'scored')]:
            with self.subTest(field=field):
                data = self.changed()
                data[field] = value
                self.reject(data, 'cannot promote, fit or score')

    def test_primary_verification_binds_executed_code(self):
        with TemporaryDirectory() as folder:
            code_root = Path(folder)
            for path in n.CODE:
                target = code_root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((DATA_ROOT / path).read_bytes())
            (code_root / n.CODE[0]).write_text('# changed checker\n', encoding='utf-8')
            with patch.object(n, 'ROOT', code_root):
                with self.assertRaisesRegex(ValueError, 'stale verification bindings'):
                    n.check(DATA_ROOT)


if __name__ == '__main__':
    unittest.main()
