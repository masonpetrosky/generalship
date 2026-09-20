"""Bounded offline provenance/preservation audit, not historical adjudication."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from generalship.admission import validate_proposal
from generalship.evidence import citation_text
from generalship.sources import digest, source_document_date, source_metadata_digest, verify_sources


def main():
    record = json.loads(Path(__file__).with_name('research-record.json').read_text())
    sources = verify_sources(ROOT)
    for sid, expected in record['preserved_source_metadata_sha256'].items():
        assert source_metadata_digest(sources[sid]) == expected, sid
    for path, expected in record['preserved_files'].items():
        assert digest(ROOT / path) == expected, path
    for binding in record['new_sources']:
        source = sources[binding['source_id']]
        assert source['path'] == binding['path']
        assert source['sha256'] == binding['sha256']
        assert source_metadata_digest(source) == binding['metadata_sha256']
    context = record['context_ocr']
    assert digest(ROOT / context['path']) == context['sha256']
    visual = set(record['visually_inspected_facsimile_ids'])
    anchors = []
    for assertion in record['assertions']:
        assert assertion['status'] == 'source_attributed_unadjudicated'
        assert assertion['limit'] and assertion['citations']
        for c in assertion['citations']:
            source = sources[c['source_id']]
            assert c['quote'] in citation_text(ROOT, sources, c), c
            assert source['sha256'] == c['raw_sha256']
            assert source_metadata_digest(source) == c['source_metadata_sha256']
            assert source_document_date(source, c['section']) == c['document_date']
            assert c['historical_knowledge_at'] is None
            assert c['visually_checked_facsimile_ids']
            for sid in c['visually_checked_facsimile_ids']:
                assert sid in visual
                scan = sources[sid]
                assert scan['format'] == 'png'
                assert scan['parent_sha256'] == source['parent_sha256']
            anchors.append(c)
    coverage = record['coverage']
    assert len(record['assertions']) == coverage['assertions'] == 10
    assert len(anchors) == coverage['passage_anchors'] == 24
    assert len({(c['source_id'], c['section']) for c in anchors}) == coverage['source_section_pairs'] == 24
    assert len(visual) == coverage['visually_inspected_pages'] == 19
    added = [sources[b['source_id']] for b in record['new_sources']]
    assert len(added) == coverage['new_source_entries'] == 24
    assert sum(s['format'] == 'text' for s in added) == coverage['new_text_sources'] == 9
    assert sum(s['format'] == 'png' for s in added) == coverage['new_page_images'] == 15
    assert len(record['preserved_source_metadata_sha256']) == coverage['prior_source_entries_preserved'] == 87
    # Coverage describes this packet's preparation, permitting later additions.
    bound = set(record['preserved_source_metadata_sha256']) | {s['id'] for s in added}
    assert len(bound) == coverage['registry_entries'] == 111
    assert len({sources[s]['path'] for s in bound}) == coverage['raw_paths'] == 108
    rule = record['segmentation_recommendation']
    assert rule['status'] == 'working_research_recommendation_not_feature_admission'
    assert rule['april5_howell']['classification'] == 'unresolved'
    assert all(rule[k] is None for k in ['earliest_qualifying_contact', 'exact_timestamp', 'area'])
    assert rule['members_by_side'] == {'US': None, 'CS': None}
    assertion_ids = {a['id'] for a in record['assertions']}
    for encounter in ['april3', 'april4', 'april5_howell', 'april6']:
        assert set(rule[encounter]['support']) <= assertion_ids
    assert all(record[k] == 0 for k in ['historical_features_admitted', 'emitted_rows', 'promoted_rows'])
    for version, statuses in [('v1', {'blocked': 18, 'excluded': 22}), ('v2', {'blocked': 7, 'excluded': 33})]:
        report = validate_proposal(ROOT, f'data/admission/shiloh-opening-{version}.json')
        assert report['coverage']['status_counts'] == statuses
        assert report['coverage']['frame_engagements'] == 127
        assert report['coverage']['frame_campaigns'] == 36
        assert report['coverage']['complete_candidate_engagements'] == 0
        assert report['emitted_rows'] == [] and report['promoted_rows'] == 0
    print(json.dumps({'status': 'passed', 'coverage': coverage,
                      'preserved_files': len(record['preserved_files']),
                      'promoted_rows': 0}, indent=2))


if __name__ == '__main__':
    main()
