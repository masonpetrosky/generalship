import collections, hashlib, json, re, subprocess
from pathlib import Path
from generalship.sources import digest, source_registry, source_metadata_digest, source_document_date
from generalship.evidence import citation_text
r=Path.cwd();p=r/'design/feature-admission-v1/shiloh-examples.json';x=json.loads(p.read_text());s=source_registry(r);d=json.loads((r/'data/evidence/TN003.json').read_text())
for path,h in x['file_bindings'].items():assert digest(r/path)==h,path
for sid,b in x['source_bindings'].items():
 assert b['source_entry_sha256']==source_metadata_digest(s[sid]),sid
 assert b['raw_sha256']==digest(r/b['path'])==s[sid]['sha256'],sid
 assert b['path']==s[sid]['path'] and b['independence_group']==s[sid]['independence_group']
 assert b['facsimile_source_id']==s[sid].get('facsimile_source_id')
for e in x['evidence_references']:
 records=d['claims'] if e['record_type']=='claim' else d['quantities']
 record=next(q for q in records if q['id']==e['record_id'])
 key='citations' if e['record_type']=='claim' else 'estimation_citations'
 c=e['citation']; assert record[key][e['citation_index']]==c
 assert c['quote'] in citation_text(r,s,c)
 assert source_document_date(s[c['source_id']],c.get('section'))==e['document_date']
 assert e['source_entry_sha256']==source_metadata_digest(s[c['source_id']]) and e['raw_sha256']==s[c['source_id']]['sha256']
sets={field:{k for c in x['cases'] for k in c[field]} for field in ['claim_ids','quantity_ids','event_ids']}
for field,group in [('claim_ids','claims'),('quantity_ids','quantities'),('event_ids','events')]:assert sets[field] <= {v['id'] for v in d[group]}
for q in d['quantities']:
 if q['id'] in sets['quantity_ids']:assert q['claim_id'] in sets['claim_ids']
for e in d['events']:
 if e['id'] in sets['event_ids']:assert set(e['claim_ids'])<=sets['claim_ids']
assert all(c['admitted_value'] is None and c['emitted_rows']==[] for c in x['cases'])
assert len({c['id'] for c in x['cases']})==len(x['cases'])
expected=collections.Counter((e['record_type'],e['record_id'],e['citation_index']) for e in x['evidence_references'])
actual=collections.Counter()
for q in d['claims']:
 if q['id'] in sets['claim_ids']:
  for i in range(len(q['citations'])):actual[('claim',q['id'],i)]+=1
for q in d['quantities']:
 if q['id'] in sets['quantity_ids']:
  for i in range(len(q['estimation_citations'])):actual[('quantity_estimation',q['id'],i)]+=1
assert expected==actual
coverage={'cases':len(x['cases']),'selected_claims':len(sets['claim_ids']),'all_dossier_claims':len(d['claims']),'selected_quantities':len(sets['quantity_ids']),'all_dossier_quantities':len(d['quantities']),'selected_events':len(sets['event_ids']),'all_dossier_events':len(d['events']),'citation_occurrences_checked':sum(actual.values()),'unique_cited_source_locators':len({(e['citation']['source_id'],e['citation'].get('section',e['citation'].get('locator')),json.dumps(e['citation'].get('row_key'),sort_keys=True),e['citation'].get('column')) for e in x['evidence_references']}),'bound_source_entries_including_linked_facsimiles':len(x['source_bindings']),'admitted_features':0,'emitted_rows':0}
for k,v in coverage.items():assert x['coverage'][k]==v,k
links=0
for path in ['docs/feature-admission.md','docs/research/shiloh-admission-examples.md']:
 f=r/path
 for url in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if '://' in url or url.startswith('#'):continue
  assert (f.parent/url.split('#')[0]).resolve().exists(),(path,url)
  links+=1
unchanged=['data/evidence/TN003.json','data/sources.json','data/pilot/cohort.json','artifacts/baseline.json','artifacts/battles.json','artifacts/quality.json','artifacts/evidence-checks.json','artifacts/research-queue.json']
for path in unchanged:assert (r/path).read_bytes()==subprocess.check_output(['git','show',x['evidence_commit']+':'+path])
print(json.dumps({'status':'passed','coverage':coverage,'status_counts':dict(collections.Counter(c['expected_status'] for c in x['cases'])),'local_links_resolve':links,'byte_identical_to_evidence_snapshot':unchanged,'scope':'Reference and isolation audit only; not an admission evaluator or evidence-use approval.'},indent=2))
