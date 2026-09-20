"""Offline passage/provenance/preservation checks; not historical adjudication."""
from html.parser import HTMLParser
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from generalship.admission import validate_proposal
from generalship.evidence import citation_text
from generalship.sources import digest, source_document_date, source_metadata_digest, text_sections, verify_sources


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, text):
        self.parts.append(text)


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
    added = [sources[x['source_id']] for x in record['new_sources']]
    # Check every selected HTML passage, including passages without an assertion.
    for source in added:
        if source.get('parent_source_id'):
            parent = sources[source['parent_source_id']]
            assert parent['format'] == 'html'
            assert parent['sha256'] == source['parent_sha256']
            parser = VisibleText()
            parser.feed((ROOT / parent['path']).read_text())
            normalized = ' '.join(' '.join(parser.parts).split())
            for section, body in text_sections((ROOT / source['path']).read_text()).items():
                if section != 'transcription-note':
                    assert ' '.join(body.split()) in normalized, (source['id'], section)
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
            assert bool(c['visually_checked_facsimile_ids']) != bool(c['html_parent_source_id'])
            for sid in c['visually_checked_facsimile_ids']:
                assert sid in visual
                assert sources[sid]['format'] == 'png'
                assert sources[sid]['parent_sha256'] == source['parent_sha256']
            anchors.append(c)
    cov = record['coverage']
    assert len(record['assertions']) == cov['assertions'] == 7
    assert len(anchors) == cov['passage_anchors'] == 14
    assert len({(c['source_id'], c['section']) for c in anchors}) == cov['source_section_pairs'] == 14
    assert len(visual) == cov['visually_inspected_pages'] == 12
    assert len(added) == cov['new_source_entries'] == 21
    for fmt, key, count in [('text', 'new_text_sources', 7), ('png', 'new_page_images', 11), ('html', 'new_html_snapshots', 3)]:
        assert sum(s['format'] == fmt for s in added) == cov[key] == count
    prior = set(record['preserved_source_metadata_sha256'])
    bound = prior | {s['id'] for s in added}
    assert len(prior) == cov['prior_source_entries_preserved'] == 112
    assert len({sources[s]['path'] for s in prior}) == cov['prior_raw_paths_preserved'] == 109
    assert len(bound) == cov['registry_entries'] == 133
    assert len({sources[s]['path'] for s in bound}) == cov['raw_paths'] == 130
    assert len(record['preserved_files']) == cov['preserved_files'] == 96
    conclusion = record['conclusion']
    assert conclusion['segmentation'] == 'unresolved'
    assert all(conclusion[k] is None for k in ['candidate_overlap', 'reed_incident_match', 'termination_of_all_saturday_contact', 'continuity_into_sunday', 'earliest_qualifying_contact', 'exact_timestamp', 'area'])
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
