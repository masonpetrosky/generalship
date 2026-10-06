"""Research packets for Napoleonic first passes: one per campaign group of cohort v1 (docs/napoleonic-frame.md).

A packet holds the research brief, each assigned entry's frame record and its printed Bodart entry, the
Napoleonic sources already registered and any existing drafts. It performs no network call and runs no model.
"""

import json
import re

from .napoleonic import COHORT, FOOTNOTE, FRAME, TRANSCRIPTION, blocks, entries, pages, split_header
from .evidence import NAPOLEONIC_EVIDENCE
from .sources import read_json, safe_path

BRIEF = 'prompts/napoleonic-first-pass.md'
OUTPUT = 'artifacts/research/napoleonic'
RECORD_FIELDS = ('id', 'start_date', 'end_date', 'date_printed', 'type_printed', 'place', 'alternative_names', 'location',
                 'war', 'campaign_group', 'winner_text', 'winner_commander_text', 'loser_text', 'loser_commander_text',
                 'winner_nations', 'loser_nations', 'french_side', 'side_a_basis', 'outcome_side_a',
                 'indecisive_printed', 'no_combat_printed', 'override_reason')


def printed_entries(text):
    """{frame ID: (page sections, printed lines)} with the IDs entries() assigns. A page's footnotes are added
    to the entries on it whose text carries the note's marker."""
    out, last, notes = {}, None, {}
    for n, body in pages(text):
        bl = blocks(body)
        head = bl[0] if bl and not split_header(bl[0][0]) and bl[0][0] != '[continued]' else []
        notes[f'p{n}'] = [l for b in (bl[1:] if head else bl) for l in b if FOOTNOTE.match(l)]
        letter = 0
        for b in (bl[1:] if head else bl):
            b = [l for l in b if not FOOTNOTE.match(l)]
            if not b:
                continue
            if b[0] == '[continued]' or split_header(b[0]) is None:
                if last is None:
                    continue
                sections, lines = out[last]
                if f'p{n}' not in sections:
                    sections.append(f'p{n}')
                lines.extend(b[1:] if b[0] == '[continued]' else b)
                continue
            last = f'B{n:03d}{chr(97 + letter)}'
            out[last] = ([f'p{n}'], list(b))
            letter += 1
    expected = [e['id'] for e in entries(text)]
    if list(out) != expected:
        raise ValueError('Printed entries do not match the frame IDs')
    for sections, lines in out.values():
        body = '\n'.join(lines)
        lines += [note for sec in sections for note in notes[sec] if FOOTNOTE.match(note).group(0).strip() in body]
    return out


def slug(group):
    return re.sub(r'[^a-z0-9]+', '-', group.lower()).strip('-')


def packet(root, group):
    frame = read_json(safe_path(root, FRAME))
    cohort = read_json(safe_path(root, COHORT))
    if group not in cohort['campaign_groups']:
        raise ValueError(f'Not a cohort v1 campaign group: {group!r}')
    ids = [i for i in cohort['battle_ids'] if next(r for r in frame['entries'] if r['id'] == i)['campaign_group'] == group]
    records = {r['id']: r for r in frame['entries'] if r['id'] in ids}
    printed = printed_entries(safe_path(root, TRANSCRIPTION).read_text(encoding='utf-8'))
    registry = read_json(safe_path(root, 'data/sources.json'))['sources']
    napoleonic_sources = [s for s in registry if s['path'].startswith('data/raw/napoleonic-') or s['id'] == 'bodart-1908-transcription-v1']
    parts = [f'# Napoleonic first pass: {group}\n',
             f'Assigned entries: {len(ids)} ({", ".join(ids)}). Cohort v1 rule: {cohort["rule"]}.\n',
             safe_path(root, BRIEF).read_text(encoding='utf-8'),
             '\n## Assigned entries\n']
    for i in ids:
        sections, lines = printed[i]
        r = records[i]
        parts += [f'\n### {i}: {r["type_printed"]} {r["connector"]} {r["place"]} ({r["date_printed"]} {r["start_year"]})\n',
                  f'Bodart entry: source `bodart-1908-transcription-v1`, section(s) {", ".join(sections)}, as printed:\n',
                  '```text\n' + '\n'.join(lines) + '\n```\n',
                  'Frame record (mechanical extract; the printed entry above is authoritative):\n',
                  '```json\n' + json.dumps({k: r[k] for k in RECORD_FIELDS}, ensure_ascii=False, indent=1) + '\n```\n']
        draft = safe_path(root, f'{NAPOLEONIC_EVIDENCE}/{i}.json')
        if draft.is_file():
            parts += ['Existing draft (not verified history; extend or correct it):\n',
                      '```json\n' + draft.read_text(encoding='utf-8') + '```\n']
    parts += ['\n## Napoleonic sources already registered\n',
              'Reuse these where relevant before registering new ones (`data/sources.json` holds full metadata).\n']
    parts += [f'- `{s["id"]}`: {s["title"]}; group `{s["independence_group"]}`; {s["path"]}' for s in napoleonic_sources]
    return '\n'.join(parts) + '\n'


def write_packet(root, group):
    path = safe_path(root, f'{OUTPUT}/{slug(group)}.md')
    path.parent.mkdir(parents=True, exist_ok=True)
    text = packet(root, group)
    path.write_text(text, encoding='utf-8')
    return {'packet': str(path.relative_to(root)), 'entries': text.count('\n### B'), 'status': 'prepared_only_no_model_called'}

