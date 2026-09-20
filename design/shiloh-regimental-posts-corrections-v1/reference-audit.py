"""Replay exact source/citation corrections while retaining the reviewed packet."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from generalship.evidence import citation_text
from generalship.sources import digest, source_document_date, source_metadata_digest, verify_sources


def main():
    manifest = json.loads(Path(__file__).with_name('source-corrections.json').read_text())
    sources = verify_sources(ROOT)
    for sid, expected in manifest['preserved_source_metadata_sha256'].items():
        assert source_metadata_digest(sources[sid]) == expected, sid
    for item in manifest['review_inputs']:
        assert digest(ROOT / item['path']) == item['sha256'], item['path']
    review_path = next(i['path'] for i in manifest['review_inputs'] if i['path'].endswith('/review-result.json'))
    findings = {f['id']: f for f in json.loads((ROOT / review_path).read_text())['required_findings']}
    substitutions = {}
    for correction in manifest['corrections']:
        before = sources[correction['source_before']]
        after = sources[correction['source_after']]
        assert correction['review_finding_ids']
        assert set(correction['review_finding_ids']) <= findings.keys()
        for fid in correction['review_finding_ids']:
            finding = findings[fid]
            assert finding['affected_source']['source_id'] == before['id']
            assert finding['affected_source']['raw_sha256'] == before['sha256']
            assert finding['affected_source']['source_metadata_sha256'] == source_metadata_digest(before)
            expected = finding['current_quote']
            for replacement in correction['replacements']:
                expected = expected.replace(replacement['old'], replacement['new'])
            assert expected == finding['replacement_quote']
        text = (ROOT / before['path']).read_text()
        for replacement in correction['replacements']:
            assert text.count(replacement['old']) == replacement['occurrences']
            text = text.replace(replacement['old'], replacement['new'])
        assert text == (ROOT / after['path']).read_text()
        assert digest(ROOT / after['path']) == after['sha256'] == correction['raw_sha256_after']
        assert source_metadata_digest(after) == correction['metadata_sha256_after']
        assert after['correction_of'] == {'source_id': before['id'], 'raw_sha256': before['sha256'], 'metadata_sha256': source_metadata_digest(before)}
        changed = {'id', 'title', 'path', 'sha256', 'correction_of', 'correction_note'}
        assert {k: v for k, v in before.items() if k not in changed} == {k: v for k, v in after.items() if k not in changed}
        scan = sources[correction['primary_visual_check']['source_id']]
        assert scan['sha256'] == correction['primary_visual_check']['sha256']
        assert scan['parent_sha256'] == after['parent_sha256']
        substitutions[before['id']] = after['id']
    binding = manifest['packet']
    assert digest(ROOT / binding['path']) == binding['sha256']
    packet = json.loads((ROOT / binding['path']).read_text())
    overlays = {(c['assertion_id'], c['source_before'], c['section']): c for c in manifest['citation_corrections']}
    count = changed_anchors = 0
    for assertion in packet['assertions']:
        for old in assertion['citations']:
            citation = dict(old)
            citation['source_id'] = substitutions.get(old['source_id'], old['source_id'])
            overlay = overlays.get((assertion['id'], old['source_id'], old['section']))
            if overlay:
                assert old['quote'] == overlay['quote_before']
                assert citation['source_id'] == overlay['source_after']
                expected = old['quote']
                correction = next(c for c in manifest['corrections'] if c['source_before'] == old['source_id'])
                for replacement in correction['replacements']:
                    expected = expected.replace(replacement['old'], replacement['new'])
                assert overlay['quote_after'] == expected
                citation['quote'] = expected
                changed_anchors += 1
            assert citation['quote'] in citation_text(ROOT, sources, citation)
            assert source_document_date(sources[citation['source_id']], citation['section']) == old['document_date']
            count += 1
    assert len(substitutions) == 1
    assert len(manifest['preserved_source_metadata_sha256']) == 151
    bound = set(manifest['preserved_source_metadata_sha256']) | set(substitutions.values())
    assert len(bound) == manifest['registry_entries_after'] == 152
    assert len({sources[s]['path'] for s in bound}) == manifest['raw_paths_after'] == 149
    assert count == 21 and changed_anchors == len(overlays) == 2
    assert manifest['interpretation_changed'] is False and manifest['dates_changed'] is False
    assert manifest['new_historical_features'] == 0
    print(json.dumps({'status': 'passed', 'preserved_source_entries': 151,
                      'new_corrected_versions': 1, 'exact_replacements': 3,
                      'replayed_anchors': count, 'changed_quote_anchors': changed_anchors,
                      'registry_entries_at_correction': 152, 'raw_paths_at_correction': 149,
                      'promoted_rows': 0}, indent=2))


if __name__ == '__main__':
    main()
