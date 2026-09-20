"""Offline source binding and preservation checks, not historical adjudication."""
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
    for b in record['new_sources']:
        s = sources[b['source_id']]
        assert (s['path'], s['sha256'], source_metadata_digest(s)) == (b['path'], b['sha256'], b['metadata_sha256'])
    added = [sources[b['source_id']] for b in record['new_sources']]
    visual = set(record['visually_inspected_facsimile_ids'])
    sections = []
    for s in added:
        if s['format'] != 'text':
            continue
        selected = set(text_sections((ROOT / s['path']).read_text())) - {'transcription-note'}
        assert selected == set(s['document_dates_by_section']) == set(s['section_facsimile_ids'])
        for sec in selected:
            expected = '1862-04-09'
            assert source_document_date(s, sec) == expected
            for sid in s['section_facsimile_ids'][sec]:
                assert sid in visual and sources[sid]['format'] == 'png'
                assert sources[sid]['parent_sha256'] == s['parent_sha256']
                assert sources[sid]['independence_group'] == s['independence_group']
            sections.append((s['id'], sec))
    anchors = []
    for a in record['assertions']:
        assert a['status'] == 'source_attributed_unadjudicated' and a['limit']
        assert set(a['context_facsimile_ids']) <= visual
        for c in a['citations']:
            s = sources[c['source_id']]
            assert s['sha256'] == c['raw_sha256'] and source_metadata_digest(s) == c['source_metadata_sha256']
            assert c['historical_knowledge_at'] is None
            if c['inspection_method'] == 'facsimile':
                assert c['quote'] in citation_text(ROOT, sources, c)
                assert c['document_date'] == source_document_date(s, c['section'])
                assert c['visually_checked_facsimile_ids'] == s['section_facsimile_ids'][c['section']]
                assert set(c['visually_checked_facsimile_ids']) <= visual
            else:
                raise AssertionError('Only facsimile citations admitted in this packet')
            anchors.append(c)
    assert set(sections) <= {(c['source_id'], c.get('section')) for c in anchors}
    cov = record['coverage']
    prior = set(record['preserved_source_metadata_sha256'])
    bound = prior | {s['id'] for s in added}
    actual = dict(assertions=len(record['assertions']), passage_anchors=len(anchors),
                  source_locator_pairs=len({(c['source_id'], c['locator']) for c in anchors}),
                  new_source_entries=len(added), new_text_sources=sum(s['format'] == 'text' for s in added),
                  new_text_sections=len(sections),
                  new_page_images=sum(s['format'] == 'png' for s in added), visually_inspected_pages=len(visual),
                  prior_source_entries_preserved=len(prior), prior_raw_paths_preserved=len({sources[s]['path'] for s in prior}),
                  registry_entries=len(bound), raw_paths=len({sources[s]['path'] for s in bound}),
                  preserved_files=len(record['preserved_files']))
    assert actual == cov
    assert (cov['assertions'], cov['passage_anchors'], cov['source_locator_pairs'], cov['visually_inspected_pages']) == (5, 16, 12, 11)
    assert (cov['prior_source_entries_preserved'], cov['registry_entries'], cov['raw_paths']) == (164, 176, 173)
    assert record['conclusion']['original_newspaper_issue_inspected'] is False
    assert all(value is None for key, value in record['conclusion'].items() if key not in {'members_by_side', 'original_newspaper_issue_inspected'})
    assert record['conclusion']['members_by_side'] == {'US': None, 'CS': None}
    assert all(record[k] == 0 for k in ['historical_features_admitted', 'emitted_rows', 'promoted_rows'])
    for version, statuses in [('v1', {'blocked': 18, 'excluded': 22}), ('v2', {'blocked': 7, 'excluded': 33})]:
        report = validate_proposal(ROOT, f'data/admission/shiloh-opening-{version}.json')
        assert report['coverage']['status_counts'] == statuses
        assert (report['coverage']['frame_engagements'], report['coverage']['frame_campaigns']) == (127, 36)
        assert report['coverage']['complete_candidate_engagements'] == 0
        assert report['emitted_rows'] == [] and report['promoted_rows'] == 0
    print(json.dumps({'status': 'passed', 'coverage': cov, 'promoted_rows': 0}, indent=2))


if __name__ == '__main__':
    main()
