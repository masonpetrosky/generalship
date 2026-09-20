"""Offline provenance audit; passage presence is not historical entailment."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from generalship.admission import validate_proposal
from generalship.evidence import citation_text
from generalship.sources import (
    digest, source_document_date, source_metadata_digest, source_registry,
    verify_sources,
)


def main():
    record = json.loads((Path(__file__).with_name('research-record.json')).read_text())
    sources = source_registry(ROOT)
    verify_sources(ROOT)
    for sid, expected in record['preserved_source_metadata_sha256'].items():
        assert source_metadata_digest(sources[sid]) == expected, sid
    for binding in record['new_sources']:
        source = sources[binding['source_id']]
        assert source['path'] == binding['path']
        assert digest(ROOT / source['path']) == source['sha256'] == binding['sha256']
        assert source_metadata_digest(source) == binding['metadata_sha256']
    for path, expected in record['preserved_files'].items():
        assert digest(ROOT / path) == expected, path
    context = record['context_ocr']
    assert digest(ROOT / context['path']) == context['sha256']
    ocr = json.loads((ROOT / context['path']).read_text())
    assert sorted(map(int, ocr['pages'])) == context['printed_pages']
    assert len(ocr['reports']) == context['full_reports_read'] == 9
    assert len(context['printed_pages']) == 16
    assert len(context['visual_pages']) == 12
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
            for sid in c['visually_checked_facsimile_ids']:
                scan = sources[sid]
                assert scan['format'] == 'png'
                assert scan['parent_sha256'] == source['parent_sha256']
                assert scan['independence_group'] == source['independence_group']
            anchors.append(c)
    coverage = record['coverage']
    assert len(record['assertions']) == coverage['assertions'] == 14
    assert len(anchors) == coverage['passage_anchors'] == 38
    assert len({(c['source_id'], c['section']) for c in anchors}) == coverage['source_section_pairs'] == 19
    assert len(record['new_sources']) == coverage['new_source_entries'] == 32
    assert len(record['preserved_source_metadata_sha256']) == 53
    for reading in record['map_readings']:
        source = sources[reading['map_source_id']]
        labels = sources[reading['readings_source_id']]
        assert labels['parent_sha256'] == source['sha256']
        catalog = json.loads((ROOT / sources[reading['catalog_source_id']]['path']).read_text())
        full = next(f for f in catalog['resources'][0]['files'][0] if f['mimetype'] == 'image/jp2')
        for x0, y0, x1, y1 in reading['inspection_windows_xyxy'].values():
            assert 0 <= x0 < x1 <= full['width'] and 0 <= y0 < y1 <= full['height']
        assert not reading['georeferenced']
        assert reading['production_date'] is None
        assert reading['historical_knowledge_at'] is None
    assert len(record['map_readings']) == coverage['maps_inspected'] == 2
    assert all(gate['state'] == 'unresolved' for gate in record['open_gates'])
    assert record['contact_decision'] == {
        'earliest_qualifying_contact': None, 'exact_timestamp': None,
        'area': None, 'members_by_side': {'US': None, 'CS': None}, 'status': 'unresolved',
    }
    for version, statuses in [('v1', {'blocked': 18, 'excluded': 22}), ('v2', {'blocked': 7, 'excluded': 33})]:
        report = validate_proposal(ROOT, f'data/admission/shiloh-opening-{version}.json')
        assert report['coverage']['status_counts'] == statuses
        assert report['coverage']['frame_engagements'] == 127
        assert report['coverage']['frame_campaigns'] == 36
        assert report['coverage']['complete_candidate_engagements'] == 0
        assert report['emitted_rows'] == [] and report['promoted_rows'] == 0
    print(json.dumps({'status': 'passed', 'coverage': coverage,
                      'prior_source_entries_preserved': 53,
                      'admission_v1': {'blocked': 18, 'excluded': 22},
                      'admission_v2': {'blocked': 7, 'excluded': 33},
                      'frame_engagements': 127, 'frame_campaigns': 36,
                      'promoted_rows': 0}, indent=2))


if __name__ == '__main__':
    main()
