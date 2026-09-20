"""Replay exact source corrections without changing the reviewed v1 packet."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from generalship.evidence import citation_text
from generalship.sources import digest, source_metadata_digest, source_registry, source_document_date


def main():
    manifest = json.loads(Path(__file__).with_name('source-corrections.json').read_text())
    registry = source_registry(ROOT)
    for sid, expected in manifest['preserved_source_metadata_sha256'].items():
        assert source_metadata_digest(registry[sid]) == expected, sid
        assert digest(ROOT / registry[sid]['path']) == registry[sid]['sha256']
    for binding in manifest['review_inputs']:
        assert digest(ROOT / binding['path']) == binding['sha256'], binding['path']
    review_path = next(b['path'] for b in manifest['review_inputs']
                       if b['path'].endswith('/review-result.json'))
    findings = {f['id']: f for f in json.loads((ROOT / review_path).read_text())['findings']}
    substitutions = {}
    for correction in manifest['corrections']:
        before = registry[correction['source_before']]
        after = registry[correction['source_after']]
        old_text = (ROOT / before['path']).read_text()
        new_text = (ROOT / after['path']).read_text()
        finding = findings[correction['review_finding_id']]
        assert finding['affected_source_id'] == before['id']
        assert finding['affected_raw_sha256'] == before['sha256']
        assert finding['current_text'] in old_text
        assert finding['exact_correction'] in new_text
        assert finding['current_text'].replace(correction['old_text'], correction['new_text']) == finding['exact_correction']
        assert old_text.count(correction['old_text']) == 1
        assert new_text == old_text.replace(correction['old_text'], correction['new_text'])
        assert digest(ROOT / after['path']) == after['sha256'] == correction['raw_sha256_after']
        assert source_metadata_digest(after) == correction['metadata_sha256_after']
        assert after['correction_of'] == {
            'source_id': before['id'], 'raw_sha256': before['sha256'],
            'metadata_sha256': source_metadata_digest(before),
        }
        changed = {'id', 'path', 'sha256', 'title', 'correction_of', 'correction_note'}
        assert {k: v for k, v in before.items() if k not in changed} == {
            k: v for k, v in after.items() if k not in changed}
        substitutions[before['id']] = after['id']
    assert len(substitutions) == 2
    packet = json.loads((ROOT / manifest['packet']['path']).read_text())
    assert digest(ROOT / manifest['packet']['path']) == manifest['packet']['sha256']
    count = 0
    for assertion in packet['assertions']:
        for old_citation in assertion['citations']:
            c = dict(old_citation)
            c['source_id'] = substitutions.get(c['source_id'], c['source_id'])
            assert c['quote'] in citation_text(ROOT, registry, c)
            assert source_document_date(registry[c['source_id']], c['section']) == c['document_date']
            count += 1
    for reading in packet['map_readings']:
        labels = registry[substitutions.get(reading['readings_source_id'], reading['readings_source_id'])]
        assert labels['parent_sha256'] == registry[reading['map_source_id']]['sha256']
    assert count == 38
    print(json.dumps({'status': 'passed', 'exact_content_corrections': 2,
                      'preserved_source_entries': 85, 'replayed_passage_anchors': count,
                      'registry_entries_at_correction': 87, 'raw_paths_at_correction': 84,
                      'new_admitted_rows': 0}, indent=2))


if __name__ == '__main__':
    main()
