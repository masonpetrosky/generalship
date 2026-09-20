from copy import deepcopy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from generalship.admission import (AdmissionError, audit_release, canonical_hash, check,
                                  validate_proposal)
from generalship.sources import digest, read_json, write_json
from admission_fixtures import ROOT, fixture, save, release, ref


class AdmissionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.p,self.s = fixture(self.root)

    def run_proposal(self):
        save(self.root,self.p,self.s)
        return validate_proposal(self.root,'data/proposal.json',allow_test_only=True)

    def decision(self, result, cid='us'):
        return next(d for d in result['decisions'] if d['candidate_id']==cid)

    def codes(self, result, cid='us'):
        return {r['code'] for r in self.decision(result,cid)['reasons']}

    def test_positive_candidate_and_test_only_release_replay(self):
        r=self.run_proposal()
        self.assertEqual(self.decision(r)['status'],'eligible_candidate')
        self.assertEqual(self.decision(r)['preview_bounds'],[100,100])
        self.assertEqual(r['emitted_rows'],[])
        self.assertEqual(r['coverage']['frame_engagements'],2)
        self.assertEqual(r['coverage']['complete_candidate_engagements'],1)
        release(self.root)
        a=audit_release(self.root,'data/release.json',allow_test_only=True)
        self.assertEqual(a['release_status'],'verified')
        self.assertEqual(self.decision(a)['status'],'admitted')
        self.assertEqual(a['audited_rows_by_scenario']['base'],[{
            'battle_id':'SYN001','campaign':'SYN-C1','profile_id':'opening_available_combatants_v1',
            'boundary_id':'synthetic-boundary','strength_bounds':{'US':[100,100],'Confederate':[80,80]}}])
        self.assertEqual(a['promoted_rows'],0)
        self.assertEqual(a,audit_release(self.root,'data/release.json',allow_test_only=True))

    def test_production_rejects_synthetic_proposal_and_release(self):
        self.run_proposal();release(self.root)
        for path in ('data/proposal.json','data/release.json'):
            with self.subTest(path=path),self.assertRaisesRegex(AdmissionError,'Test-only'):
                check(self.root,path)
        self.p['test_only']=False
        save(self.root,self.p)
        with self.assertRaisesRegex(AdmissionError,'Test-only snapshot'):
            check(self.root,'data/proposal.json')

    def test_later_report_prestate_and_null_section_date_are_distinct(self):
        r=self.run_proposal()
        ob=self.decision(r)['observations'][0]
        self.assertEqual(ob['quantity']['period']['start'],'2000-01-01')
        self.assertEqual(ob['document_dates'][0]['document_date'],'2000-01-10')
        self.assertIsNone(ob['historical_knowledge_at'])
        self.s['registry']['sources'][0]['document_dates_by_section']['us-a']=None
        r=self.run_proposal()
        self.assertIsNone(self.decision(r)['observations'][0]['document_dates'][0]['document_date'])
        self.assertEqual(self.decision(r)['status'],'eligible_candidate')

    def test_explicit_estimate_keeps_integer_and_bounds(self):
        q=self.s['dossiers'][0]['quantities'][0]
        q['estimation_status']='explicit_estimate'
        r=self.run_proposal()
        self.assertEqual(self.decision(r)['preview_bounds'],[100,100])
        self.assertEqual(self.decision(r)['observations'][0]['quantity']['estimation_status'],'explicit_estimate')

    def test_transitive_post_state_and_target_leakage(self):
        for change in ('post_state','outcome','recorded_participation','later_period'):
            with self.subTest(change=change):
                self.p,self.s=fixture(self.root)
                n=self.p['candidates'][0]['nodes'][0]
                if change=='post_state':n['mapping']['derivation']='post_state'
                elif change=='outcome':n.update(kind='claim',reference='outcome')
                elif change=='recorded_participation':self.s['dossiers'][0]['quantities'][0]['basis']='reported_engaged'
                else:self.s['dossiers'][0]['quantities'][0]['period'].update(start='2000-01-03',end='2000-01-03')
                # Wrap the contaminated sum in another identity with clean labels.
                rootnode=deepcopy(self.p['candidates'][0]['nodes'][-1]);rootnode.update(id='wrapper',kind='identity',inputs=['total'])
                self.p['candidates'][0]['nodes'].append(rootnode);self.p['candidates'][0]['root_node']='wrapper'
                r=self.run_proposal()
                self.assertEqual(self.decision(r)['status'],'excluded')
                self.assertEqual(r['preview_rows_by_scenario']['base'],[])

    def test_unknowns_are_blocked_and_null_never_zero(self):
        n=self.p['candidates'][0]['nodes'][0]
        n.update(kind='claim',reference='logistics')
        n['mapping'].update(time='unknown',population='unknown',derivation='unknown',members=None,citations=[])
        r=self.run_proposal()
        self.assertEqual(self.decision(r)['status'],'blocked')
        self.assertIsNone(self.decision(r)['preview_bounds'])
        self.assertIn('missing_observation',self.codes(r))
        self.assertEqual(r['coverage']['frame_engagements'],2)

    def test_missing_boundary_and_crossing_state_interval_block(self):
        self.p['boundaries'][0]['contact_definition']=None
        self.s['dossiers'][0]['quantities'][0]['period']['end']='2000-01-03'
        r=self.run_proposal()
        self.assertIn('boundary_unresolved',self.codes(r))
        self.assertIn('state_interval_crosses_boundary',self.codes(r))

    def test_overlap_cycle_unknown_members_and_wrong_population(self):
        for fault,expected in [('overlap','excluded'),('cycle','invalid'),('unknown','blocked'),('wrong','excluded')]:
            with self.subTest(fault=fault):
                self.p,self.s=fixture(self.root)
                nodes=self.p['candidates'][0]['nodes']
                if fault=='overlap':nodes[1]['mapping']['members']=['us-a'];nodes[-1]['mapping']['members']=['us-a']
                elif fault=='cycle':nodes[-1]['inputs']=['us-a','total']
                elif fault=='unknown':nodes[1]['mapping']['members']=None
                else:nodes[1]['mapping']['population']='incompatible'
                r=self.run_proposal()
                self.assertEqual(self.decision(r)['status'],expected)
                self.assertEqual(r['emitted_rows'],[])

    def test_subtraction_requires_nested_members_and_correct_interval(self):
        nodes=self.p['candidates'][0]['nodes']
        # (40+60)-60 is valid only for a target comprising A, not the whole army.
        nodes.append({'id':'difference','kind':'subtract','reference':None,'inputs':['total','us-b'],
                      'mapping':deepcopy(nodes[0]['mapping'])})
        self.p['candidates'][0]['root_node']='difference'
        self.p['boundaries'][0]['members_by_side']['US']=['us-a']
        r=self.run_proposal();self.assertEqual(self.decision(r)['preview_bounds'],[40,40])
        nodes[-1]['inputs']=['us-a','us-b']
        nodes.remove(next(n for n in nodes if n['id']=='total'))
        r=self.run_proposal();self.assertIn('subtraction_not_nested',self.codes(r))

    def test_bad_binding_metadata_omission_and_changed_review_fail_closed(self):
        self.run_proposal()
        s=read_json(self.root/'data/snapshot.json');s['registry']['sources'][0]['document_date_note']='changed'
        write_json(self.root/'data/snapshot.json',s)
        self.p['snapshot']=ref(self.root,'data/snapshot.json');write_json(self.root/'data/proposal.json',self.p)
        with self.assertRaisesRegex(AdmissionError,'Source metadata'):
            validate_proposal(self.root,'data/proposal.json',allow_test_only=True)
        self.run_proposal();m,rv,pr=release(self.root)
        self.p['candidates'][0]['nodes'][0]['mapping']['rationale']='New interpretation, same numerical value.'
        self.run_proposal();m['proposal']=ref(self.root,'data/proposal.json');write_json(self.root/'data/release.json',m)
        with self.assertRaisesRegex(AdmissionError,'Review does not bind'):
            audit_release(self.root,'data/release.json',allow_test_only=True)
        self.s['source_bindings']={};write_json(self.root/'data/snapshot.json',self.s)
        self.p['snapshot']=ref(self.root,'data/snapshot.json');write_json(self.root/'data/proposal.json',self.p)
        with self.assertRaisesRegex(AdmissionError,'source-entry bindings'):
            validate_proposal(self.root,'data/proposal.json',allow_test_only=True)

    def test_duplicate_json_keys_frame_omission_and_duplicate_candidates(self):
        save(self.root,self.p)
        path=self.root/'data/proposal.json';path.write_text('{"kind": "a", "kind": "b"}')
        with self.assertRaisesRegex(AdmissionError,'Duplicate JSON key'):check(self.root,'data/proposal.json')
        self.s['frame'].pop()
        with self.assertRaisesRegex(AdmissionError,'every cohort ID'):self.run_proposal()
        self.p,self.s=fixture(self.root);self.p['candidates'].append(deepcopy(self.p['candidates'][0]))
        with self.assertRaisesRegex(AdmissionError,'duplicate ID'):self.run_proposal()

    def test_missing_side_stays_in_denominator(self):
        self.p['candidates'].pop();self.p['scenarios'][0]['assignments']['SYN001']['Confederate']=None
        r=self.run_proposal()
        self.assertEqual(r['coverage']['frame_engagements'],2)
        self.assertEqual(r['coverage']['complete_candidate_engagements'],0)
        self.assertEqual(r['coverage']['ledger'][0]['sides']['Confederate']['candidate_ids'],[])

    def test_unsupported_causal_and_information_profiles_excluded(self):
        for use in ('historical_information_set_forecast','campaign_contribution','battle_execution_effect'):
            with self.subTest(use=use):
                self.p['profile']['use']=use;r=self.run_proposal()
                self.assertEqual(self.decision(r)['status'],'excluded')
                self.assertIn('unsupported_profile',self.codes(r))

    def test_review_scope_or_adverse_finding_blocks_release(self):
        self.run_proposal()
        for fault in ('transcription_only','adverse','missing_scope','primary_unresolved'):
            with self.subTest(fault=fault):
                m,rv,pr=release(self.root)
                if fault=='transcription_only':rv['kind']='source_transcription_review'
                elif fault=='adverse':rv['verdict']='corrections_needed';rv['findings']=['Synthetic unresolved finding.']
                elif fault=='missing_scope':rv['scope'].remove('population')
                else:pr['unresolved_findings']=['Synthetic unresolved primary concern.']
                write_json(self.root/'data/review.json',rv);pr['review_sha256']=digest(self.root/'data/review.json')
                write_json(self.root/'data/primary.json',pr)
                m['review']=ref(self.root,'data/review.json');m['reconciliation']=ref(self.root,'data/primary.json')
                write_json(self.root/'data/release.json',m)
                r=audit_release(self.root,'data/release.json',allow_test_only=True)
                self.assertEqual(r['release_status'],'blocked')
                self.assertEqual(r['audited_rows_by_scenario'],{})
                self.assertEqual(self.decision(r)['status'],'blocked')

    def test_release_rows_coverage_and_implementation_hashes_bound(self):
        self.run_proposal()
        for field in ('rows_sha256','coverage_sha256','implementation_sha256'):
            m,_,_=release(self.root)
            if field=='implementation_sha256':m[field]['generalship/admission.py']='0'*64
            else:m[field]='0'*64
            write_json(self.root/'data/release.json',m)
            with self.subTest(field=field),self.assertRaises(AdmissionError):
                audit_release(self.root,'data/release.json',allow_test_only=True)

    def test_coherent_scenarios_no_extra_battle_weight_or_silent_selection(self):
        alt=deepcopy(self.p['candidates'][0]);alt['id']='us-alt'
        # Alternate supported quantity, same membership; source alternatives are
        # mutually exclusive, not two observations added together.
        for n in self.p['candidates'][0]['nodes']:n['mapping']['source_choices']={'return-choice':'A'}
        for n in alt['nodes']:n['mapping']['source_choices']={'return-choice':'B'}
        self.p['candidates'].append(alt)
        r=self.run_proposal()
        self.assertIn('applicable_alternative_not_represented',{i['code'] for i in r['scenario_issues']})
        scenario=deepcopy(self.p['scenarios'][0]);scenario['id']='alternative';scenario['assignments']['SYN001']['US']='us-alt'
        self.p['scenarios'].append(scenario)
        r=self.run_proposal();self.assertEqual(r['scenario_issues'],[])
        self.assertEqual(r['coverage']['complete_candidate_engagements'],1)
        self.assertEqual(r['coverage']['scenario_rows'],{'alternative':1,'base':1})
        # Shared source choice cannot be silently mixed across the two sides.
        self.p['candidates'][1]['nodes'][0]['mapping']['source_choices']={'return-choice':'A'}
        r=self.run_proposal()
        self.assertIn('incompatible_joint_choices',{i['code'] for i in r['scenario_issues']})
        self.assertEqual(r['preview_rows_by_scenario']['alternative'],[])

    def test_wrong_scope_cannot_be_rescued_by_scenario(self):
        self.p['candidates'][0]['nodes'][0]['mapping']['population']='incompatible'
        r=self.run_proposal()
        self.assertEqual(self.decision(r)['status'],'excluded')
        self.assertIn('inapplicable_candidate',{i['code'] for i in r['scenario_issues']})
        self.assertEqual(r['preview_rows_by_scenario']['base'],[])

    def test_snapshot_replay_ignores_later_current_registry(self):
        before=self.run_proposal()
        (self.root/'data/sources.json').write_text('{"sources": ["unrelated invalid current metadata"]}')
        (self.root/'data/pilot').mkdir(exist_ok=True)
        (self.root/'data/pilot/cohort.json').write_text('{"battle_ids": []}')
        after=validate_proposal(self.root,'data/proposal.json',allow_test_only=True)
        self.assertEqual(before,after)

    def test_research_cutoff_and_outcome_based_selection_are_rejected(self):
        self.p['profile']['evaluation_plan']['research_cutoff']='2026-09-19'
        with self.assertRaisesRegex(AdmissionError,'research cutoff'):self.run_proposal()
        self.p['profile']['evaluation_plan']['research_cutoff']='2026-09-20'
        self.p['profile']['selection_policy']='best_brier'
        with self.assertRaisesRegex(AdmissionError,'Selection policy'):self.run_proposal()

    def test_alias_citations_do_not_add_values_or_votes(self):
        alias=deepcopy(self.s['registry']['sources'][0]);alias['id']='synthetic-alias'
        self.s['registry']['sources'].append(alias)
        ct=deepcopy(self.p['candidates'][0]['nodes'][0]['mapping']['citations'][0]);ct['source_id']=alias['id']
        self.p['candidates'][0]['nodes'][0]['mapping']['citations'].append(ct)
        r=self.run_proposal()
        self.assertEqual(self.decision(r)['preview_bounds'],[100,100])
        self.assertEqual(r['coverage']['candidate_observations'],2)
        representations=self.decision(r)['observations'][0]['source_representations']
        self.assertEqual(representations['synthetic-return']['same_document_key'],
                         representations['synthetic-alias']['same_document_key'])
        self.assertFalse(representations['synthetic-alias']['independence_established'])

    def test_invalid_precedence_retains_already_evaluated_exclusions(self):
        self.p['candidates'][0]['nodes'][0]['mapping']['derivation']='post_state'
        extra=deepcopy(self.p['candidates'][0]['nodes'][0]);extra['id']='unreachable'
        self.p['candidates'][0]['nodes'].append(extra)
        r=self.run_proposal()
        self.assertEqual(self.decision(r)['status'],'invalid')
        self.assertIn('post_boundary_dependency',self.codes(r))
        self.assertIn('Unreachable nodes are not allowed',self.codes(r))

    def test_target_channel_and_profile_changes_cannot_be_relabelled(self):
        self.p['profile']['target']='commander_wins_caused'
        r=self.run_proposal()
        self.assertEqual(self.decision(r)['status'],'excluded')
        self.assertNotIn('outcome',r['preview_rows_by_scenario'])
        self.assertEqual(r['target_channel']['SYN001'],'Union')

    def test_production_cohort_and_frame_cannot_be_silently_changed(self):
        p=read_json(ROOT/'data/admission/shiloh-opening-v1.json')
        snapshot=read_json(ROOT/p['snapshot']['path'])
        snapshot['cohort']['battle_ids'].pop()
        write_json(self.root/'data/snapshot.json',snapshot)
        p['snapshot']=ref(self.root,'data/snapshot.json');write_json(self.root/'data/proposal.json',p)
        with self.assertRaisesRegex(AdmissionError,'Frozen v1 cohort changed'):
            check(self.root,'data/proposal.json')

    def test_release_checks_executing_code_not_other_checkout_files(self):
        self.run_proposal();m,_,_=release(self.root)
        (self.root/'generalship/admission.py').write_text('# unrelated code in another checkout\n')
        m['implementation_sha256']['generalship/admission.py']=digest(self.root/'generalship/admission.py')
        write_json(self.root/'data/release.json',m)
        with self.assertRaisesRegex(AdmissionError,'Implementation hash mismatch'):
            audit_release(self.root,'data/release.json',allow_test_only=True)

    def test_production_ledger_covers_all_40_quantities_without_admission(self):
        with patch('urllib.request.urlopen',side_effect=AssertionError('offline')):
            r=check(ROOT)
        self.assertEqual(r['coverage']['frame_engagements'],127)
        self.assertEqual(r['coverage']['frame_campaigns'],36)
        self.assertEqual(r['coverage']['candidate_observations'],40)
        self.assertEqual(r['coverage']['status_counts'],{'blocked':18,'excluded':22})
        self.assertEqual(r['coverage']['complete_candidate_engagements'],0)
        self.assertEqual(r['emitted_rows'],[])
        self.assertEqual(r['promoted_rows'],0)
        self.assertEqual({x['battle_id'] for x in r['coverage']['ledger']},set(read_json(ROOT/'data/pilot/cohort.json')['battle_ids']))

    def test_expanded_and_common_coverage_are_separate(self):
        self.s['frame'][0]['baseline_eligible']=False
        r=self.run_proposal()
        self.assertEqual(r['coverage']['paired_common_ids'],[])
        self.assertEqual(r['coverage']['newly_covered_ids'],['SYN001'])

    def test_cli_rejects_test_artifact_without_traceback(self):
        result=subprocess.run([sys.executable,'-m','generalship','--root',str(self.root),'admission-check','data/proposal.json'],cwd=ROOT,capture_output=True,text=True)
        self.assertEqual(result.returncode,1)
        self.assertNotIn('Traceback',result.stderr)
