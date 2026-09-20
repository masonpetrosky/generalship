"""Offline reference/preservation audit for this immutable research proposal.

Run from any directory. Writes nothing; does not establish historical entailment.
"""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from generalship.admission import canonical_hash, validate_proposal  # noqa: E402
from generalship.evidence import citation_text  # noqa: E402
from generalship.sources import digest, source_document_date, source_metadata_digest  # noqa: E402


def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def main():
    record = load('design/shiloh-opening-boundary-v1/research-record.json')
    for binding in (record['proposal'], record['snapshot'], record['comparison_proposal'], record['report']):
        assert digest(ROOT / binding['path']) == binding['sha256'], binding['path']
    for path, expected in record['preserved_input_sha256'].items():
        assert digest(ROOT / path) == expected, path
    snapshot = load(record['snapshot']['path'])
    sources = {s['id']: s for s in snapshot['registry']['sources']}
    for anchor in record['anchors'].values():
        c = anchor['citation']
        source = sources[c['source_id']]
        assert c['quote'] in citation_text(ROOT, sources, c), c
        assert source['path'] == anchor['raw_path']
        assert source['sha256'] == anchor['raw_sha256'] == digest(ROOT / source['path'])
        assert source_metadata_digest(source) == anchor['source_metadata_sha256']
        assert source_document_date(source, c['section']) == anchor['document_date']
        assert anchor['historical_knowledge_at'] is None
    proposal = load(record['proposal']['path'])
    original = load(record['comparison_proposal']['path'])
    assert proposal['profile'] == original['profile']
    assert proposal['snapshot'] == original['snapshot']
    assert canonical_hash(proposal['profile']) == record['profile_sha256']
    assert canonical_hash(proposal['boundaries']) == record['boundaries_sha256']
    boundary, = proposal['boundaries']
    assert boundary['area'] is None
    assert boundary['members_by_side'] == {'US': None, 'Confederate': None}
    report = validate_proposal(ROOT, record['proposal']['path'])
    assert report == load(record['report']['path'])
    assert report['candidate_hashes'] == record['candidate_hashes']
    before = {c['id']: c for c in original['candidates']}
    after = {c['id']: c for c in proposal['candidates']}
    assert before.keys() == after.keys()
    old_decisions = {d['candidate_id']: d for d in load('artifacts/admission-check.json')['decisions']}
    decisions = {d['candidate_id']: d for d in report['decisions']}
    changes = {c['candidate_id']: c for c in record['mapping_changes']}
    assert len(changes) == len(record['mapping_changes']) == 18
    assert set(changes) == {cid for cid, d in old_decisions.items() if d['status'] == 'blocked'}
    dossier = next(d for d in snapshot['dossiers'] if d['battle_id'] == 'TN003')
    quantities = {q['id']: q for q in dossier['quantities']}
    assert len(before) == len(quantities) == 40
    references = []
    for cid, candidate in after.items():
        node, = candidate['nodes']
        references.append(node['reference'])
        assert node['kind'] == 'quantity' and node['inputs'] == []
        assert node['mapping']['members'] is None and node['mapping']['source_choices'] == {}
        assert candidate['boundary_id'] == boundary['id']
        assert {k:v for k,v in before[cid].items() if k not in ('boundary_id','nodes')} == {k:v for k,v in candidate.items() if k not in ('boundary_id','nodes')}
        assert {k:v for k,v in before[cid]['nodes'][0].items() if k != 'mapping'} == {k:v for k,v in node.items() if k != 'mapping'}
        if cid in changes:
            change = changes[cid]
            q = quantities[node['reference']]
            assert q['id'] == change['quantity_id'] and q['claim_id'] == change['claim_id']
            assert canonical_hash(q) == change['quantity_sha256']
            assert canonical_hash(node['mapping']) == change['mapping_sha256']
            assert old_decisions[cid]['status'] == change['previous_status']
            assert decisions[cid]['status'] == change['proposed_status']
        else:
            assert node['mapping'] == before[cid]['nodes'][0]['mapping']
            assert decisions[cid]['status'] == old_decisions[cid]['status'] == 'excluded'
    assert len(set(references)) == 40 and set(references) == set(quantities)
    coverage = report['coverage']
    assert {k:v for k,v in coverage.items() if k != 'ledger'} == record['coverage']
    assert coverage['frame_engagements'] == len(coverage['ledger']) == 127
    assert coverage['frame_campaigns'] == 36
    assert coverage['status_counts'] == {'blocked': 7, 'excluded': 33}
    assert coverage['complete_candidate_engagements'] == 0
    assert report['emitted_rows'] == [] and report['promoted_rows'] == 0
    assert not report['scenario_issues']
    for scenario in proposal['scenarios']:
        assert all(v is None for row in scenario['assignments'].values() for v in row.values())
    print(json.dumps({'status':'passed', 'passage_anchors':len(record['anchors']),
                      'source_sections':len({(a['citation']['source_id'],a['citation']['section']) for a in record['anchors'].values()}),
                      'revisited_mappings':len(changes), 'candidate_observations':40,
                      'frame_engagements':127,'frame_campaigns':36,
                      'status_counts':coverage['status_counts'], 'promoted_rows':0}, indent=2))


if __name__ == '__main__':
    main()
