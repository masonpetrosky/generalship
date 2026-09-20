"""Offline binding and preservation checks, not historical adjudication."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from generalship.admission import validate_proposal
from generalship.evidence import citation_text
from generalship.sources import digest, source_document_date, source_metadata_digest, text_sections, verify_sources


def main():
    record = json.loads(Path(__file__).with_name('research-record.json').read_text())
    sources = verify_sources(ROOT)
    assert digest(ROOT / record['search_log']['path']) == record['search_log']['sha256']
    for sid, expected in record['preserved_source_metadata_sha256'].items():
        assert source_metadata_digest(sources[sid]) == expected, sid
    for path, expected in record['preserved_files'].items():
        assert digest(ROOT / path) == expected, path
    for binding in record['new_sources']:
        source = sources[binding['source_id']]
        assert source['path'] == binding['path']
        assert source['sha256'] == binding['sha256']
        assert source_metadata_digest(source) == binding['metadata_sha256']
    added = [sources[b['source_id']] for b in record['new_sources']]
    visual = set(record['visually_inspected_facsimile_ids'])
    sections = []
    for source in added:
        if source['format'] != 'text':
            continue
        selected = set(text_sections((ROOT / source['path']).read_text())) - {'transcription-note'}
        assert selected == set(source['document_dates_by_section']) == set(source['section_facsimile_ids'])
        for section in selected:
            assert source_document_date(source, section) is None
            for sid in source['section_facsimile_ids'][section]:
                assert sid in visual
                assert sources[sid]['format'] == 'png'
                assert sources[sid]['parent_sha256'] == source['parent_sha256']
                assert sources[sid]['independence_group'] == source['independence_group']
            sections.append((source['id'], section))
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
            assert c['visually_checked_facsimile_ids'] == source['section_facsimile_ids'][c['section']]
            assert set(c['visually_checked_facsimile_ids']) <= visual
            anchors.append(c)
    pairs = {(c['source_id'], c['section']) for c in anchors}
    assert set(sections) <= pairs
    cov = record['coverage']
    assert len(record['assertions']) == cov['assertions'] == 7
    assert len(anchors) == cov['passage_anchors'] == 21
    assert len(pairs) == cov['source_section_pairs'] == 19
    assert len(sections) == cov['new_text_sections'] == 17
    assert len(visual) == cov['visually_inspected_pages'] == 16
    assert len(added) == cov['new_source_entries'] == 18
    assert sum(s['format'] == 'text' for s in added) == cov['new_text_sources'] == 5
    assert sum(s['format'] == 'png' for s in added) == cov['new_page_images'] == 13
    prior = set(record['preserved_source_metadata_sha256'])
    bound = prior | {s['id'] for s in added}
    assert len(prior) == cov['prior_source_entries_preserved'] == 133
    assert len({sources[s]['path'] for s in prior}) == cov['prior_raw_paths_preserved'] == 130
    assert len(bound) == cov['registry_entries'] == 151
    assert len({sources[s]['path'] for s in bound}) == cov['raw_paths'] == 148
    assert len(record['preserved_files']) == cov['preserved_files'] == 109
    conclusion = record['conclusion']
    assert conclusion['segmentation'] == 'unresolved'
    assert all(conclusion[k] is None for k in ['same_post_match', 'reed_incident_match', 'termination_of_all_saturday_contact', 'continuity_into_sunday', 'earliest_qualifying_contact', 'exact_timestamp', 'area'])
    assert all(value is None for value in conclusion['post_coordinates'].values())
    assert conclusion['members_by_side'] == {'US': None, 'CS': None}
    assert all(record[k] == 0 for k in ['historical_features_admitted', 'emitted_rows', 'promoted_rows'])
    for version, statuses in [('v1', {'blocked': 18, 'excluded': 22}), ('v2', {'blocked': 7, 'excluded': 33})]:
        report = validate_proposal(ROOT, f'data/admission/shiloh-opening-{version}.json')
        assert report['coverage']['status_counts'] == statuses
        assert report['coverage']['frame_engagements'] == 127
        assert report['coverage']['frame_campaigns'] == 36
        assert report['coverage']['complete_candidate_engagements'] == 0
        assert report['emitted_rows'] == [] and report['promoted_rows'] == 0
    print(json.dumps({'status': 'passed', 'coverage': cov, 'promoted_rows': 0}, indent=2))


if __name__ == '__main__':
    main()
