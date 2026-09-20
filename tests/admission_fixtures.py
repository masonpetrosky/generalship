"""Explicitly invented, test-only evidence. Never a historical review or release."""

from copy import deepcopy
from pathlib import Path
import shutil

from generalship.admission import (IMPLEMENTATION, SCOPE, canonical_hash,
                                  review_bindings, validate_proposal)
from generalship.sources import read_json, write_json, digest, source_metadata_digest

ROOT = Path(__file__).resolve().parents[1]


def ref(root, path):
    return {'path': path, 'sha256': digest(root / path)}


def fixture(root):
    for p in IMPLEMENTATION:
        dest = root / p; dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / p, dest)
    (root / 'data').mkdir(exist_ok=True)
    shutil.copyfile(ROOT / 'docs/feature-admission.md', root / 'data/contract.md')
    raw = '# SYNTHETIC TEST DATA\n'
    values = [('us-a', 40), ('us-b', 60), ('cs-a', 80)]
    for name, value in values:
        raw += f'\n## {name}\nSYNTHETIC {name}: {value} people before contact.\n'
    raw += '\n## outcome\nSYNTHETIC recorded Union victory.\n\n## diary\nSYNTHETIC diary composition date unknown.\n'
    (root / 'data/raw.txt').write_text(raw)
    source = {'id': 'synthetic-return', 'path': 'data/raw.txt', 'sha256': digest(root/'data/raw.txt'),
              'format': 'text', 'sectioned': True, 'source_kind': 'test_only_invented',
              'independence_group': 'synthetic-single-document', 'document_date': None,
              'document_dates_by_section': {name: '2000-01-10' for name in ['us-a','us-b','cs-a','outcome']} | {'diary': None},
              'document_date_note': 'Synthetic report and undated diary.', 'retrieved_at': '2026-09-20'}
    citations = [{'source_id': source['id'], 'section': name, 'locator': name,
                  'quote': f'SYNTHETIC {name}: {value} people before contact.'} for name, value in values]
    outcome = {'source_id': source['id'], 'section': 'outcome', 'locator': 'outcome', 'quote': 'SYNTHETIC recorded Union victory.'}
    claims = [{'id': 'strength', 'dimension': 'strength', 'value': 'Synthetic counts', 'status': 'supported',
               'phase': 'inherited', 'rationale': 'Only test data.', 'citations': citations},
              {'id': 'outcome', 'dimension': 'outcome', 'value': 'Union', 'status': 'supported',
               'phase': 'post_outcome', 'rationale': 'Only test data.', 'citations': [outcome]}]
    for dim in ['terrain','logistics','information','objectives','responsibility']:
        claims.append({'id': dim, 'dimension': dim, 'value': None, 'status': 'unknown',
                       'phase': 'unresolved', 'rationale': 'Not supplied in this synthetic test.', 'citations': []})
    quantities = []
    for i, (name, value) in enumerate(values):
        quantities.append({'id': name, 'claim_id': 'strength', 'citation_index': i,
                           'entity_id': name, 'unit': 'people', 'lower': value, 'upper': value,
                           'basis': 'present_for_duty', 'estimate_kind': 'reported_exact',
                           'period': {'start':'2000-01-01','end':'2000-01-01','label':'Synthetic prior state'},
                           'location':'Synthetic area','scope':'Synthetic partition', 'recorded_at':'2000-01-10',
                           'note':'Synthetic later report of earlier state.',
                           'estimation_status':'reported_without_explicit_estimation_qualifier',
                           'estimation_note':'Synthetic test.', 'estimation_citations':[citations[i]]})
    dossier = {'schema_version':3,'battle_id':'SYN001','status':'draft','tactical_replacement_at':None,
               'campaign_replacement_at':None,'boundary_note':'Synthetic boundary only.',
               'claims':claims,'open_questions':['Synthetic fixture is not historical evidence.'],
               'entities':[{'id':name,'name':name,'kind':'formation','side':'US' if name.startswith('us') else 'CS'} for name,_ in values],
               'events':[{'id':'precontact','date':'2000-01-01','time_label':'Before contact',
                          'entity_ids':['us-a'],'claim_ids':['strength'],'note':'Synthetic.'}],
               'quantities':quantities}
    snapshot = {'schema_version':1,'test_only':True,'cohort':{'battle_ids':['SYN001','SYN002']},
                'frame':[{'id':'SYN001','campaign':'SYN-C1','outcome':'Union','operation':False,'baseline_eligible':True},
                         {'id':'SYN002','campaign':'SYN-C2','outcome':'Union','operation':False,'baseline_eligible':False}],
                'registry':{'sources':[source]},'dossiers':[dossier],
                'source_bindings':{source['id']:{'metadata_sha256':source_metadata_digest(source),'raw_sha256':source['sha256']}}}
    write_json(root/'data/snapshot.json',snapshot)
    profile = deepcopy(read_json(ROOT/'data/admission/shiloh-opening-v1.json')['profile'])
    profile['contract'] = ref(root,'data/contract.md')
    boundary = {'id':'synthetic-boundary','battle_id':'SYN001','profile_id':profile['id'],'date':'2000-01-02',
                'contact_definition':'Synthetic first hostile contact including pickets.','area':'Synthetic defined area.',
                'availability_rule':'Synthetic physical availability, no offsite units.',
                'members_by_side':{'US':['us-a','us-b'],'Confederate':['cs-a']},'citations':citations,
                'rationale':'Invented only to test the engine.'}
    def mapping(members):
        return {'time':'before','population':'compatible','derivation':'pre_state','members':members,
                'rationale':'SYNTHETIC TEST MAPPING; no historical claim.','citations':citations,'source_choices':{}}
    def leaf(name):
        return {'id':name,'kind':'quantity','reference':name,'inputs':[],'mapping':mapping([name])}
    candidates = [{'id':'us','battle_id':'SYN001','side':'US','entity_id':'us-a','boundary_id':boundary['id'],'root_node':'total',
                   'nodes':[leaf('us-a'),leaf('us-b'),{'id':'total','kind':'sum','reference':None,'inputs':['us-a','us-b'],'mapping':mapping(['us-a','us-b'])}]},
                  {'id':'cs','battle_id':'SYN001','side':'Confederate','entity_id':'cs-a','boundary_id':boundary['id'],'root_node':'cs-a','nodes':[leaf('cs-a')]}]
    p = {'schema_version':1,'kind':'admission_proposal','test_only':True,'profile':profile,
         'snapshot':ref(root,'data/snapshot.json'),'boundaries':[boundary],'candidates':candidates,
         'scenarios':[{'id':'base','assignments':{'SYN001':{'US':'us','Confederate':'cs'},'SYN002':{'US':None,'Confederate':None}},'rationale':'Synthetic complete scenario.'}]}
    save(root,p,snapshot)
    return p,snapshot


def save(root, proposal, snapshot=None):
    if snapshot is not None:
        snapshot['source_bindings'] = {s['id']:{'metadata_sha256':source_metadata_digest(s),'raw_sha256':s['sha256']} for s in snapshot['registry']['sources']}
        write_json(root/'data/snapshot.json',snapshot)
        proposal['snapshot'] = ref(root,'data/snapshot.json')
    write_json(root/'data/proposal.json',proposal)


def release(root):
    report = validate_proposal(root,'data/proposal.json',allow_test_only=True)
    (root/'data/response.md').write_text('# SYNTHETIC TEST-ONLY REVIEW STUB\nNo real person or historical review is represented.\n')
    review = {'kind':'separate_evidence_use_review','test_only':True,'bindings':review_bindings(report),
              'scope':sorted(SCOPE),'reviewer':{'identity':'synthetic-test-reviewer','kind':'test_stub','model':None,'effort':None},
              'date':'2026-09-20','verdict':'accept','findings':[],'response':ref(root,'data/response.md')}
    write_json(root/'data/review.json',review)
    primary = {'kind':'primary_evidence_use_reconciliation','test_only':True,'proposal_sha256':report['proposal_sha256'],
               'review_sha256':digest(root/'data/review.json'),'actor':'synthetic-test-primary','date':'2026-09-20',
               'decision':'accept','unresolved_findings':[],'rationale':'Synthetic test stub, not a historical admission.'}
    write_json(root/'data/primary.json',primary)
    m = {'schema_version':1,'kind':'admission_release_audit','test_only':True,'proposal':ref(root,'data/proposal.json'),
         'implementation_sha256':{p:digest(root/p) for p in IMPLEMENTATION},'review':ref(root,'data/review.json'),
         'reconciliation':ref(root,'data/primary.json'),'rows_sha256':canonical_hash(report['preview_rows_by_scenario']),
         'coverage_sha256':canonical_hash(report['coverage'])}
    write_json(root/'data/release.json',m)
    return m,review,primary
