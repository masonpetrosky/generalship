"""Direct, provisional whole-volume Bodart extraction. Offline; no model fit or commander credit."""

import argparse
from collections import Counter, defaultdict
import csv
import gzip
import io
import json
from pathlib import Path
import re
import unicodedata
import xml.etree.ElementTree as ET

from . import napoleonic
from .napoleonic_benchmark import encode_strength, number
from .sources import digest, read_json, safe_path, source_registry, text_sections, validate_source_metadata, write_json

BASE = 'data/raw/bodart-bulk-v1/'
LAYOUT = BASE + 'layout.xml.gz'
SOURCE = 'bodart-1908-layout-xml-v1'
MANUAL_SOURCE = 'bodart-1908-transcription-v1'
FRAME = 'data/napoleonic/frame-v1.json'
CHECKS = 'data/bodart/image-checks-v1.json'
ADDITIONS = 'data/bodart/sources-v1.json'
CSV = 'artifacts/bodart-bulk-v1.csv'
META = 'artifacts/bodart-bulk-v1.json'
REPORT = 'artifacts/bodart-bulk-v1.md'
FIRST, LAST = 49, 600
TYPES = ('SEESCHLACHTEN', 'SEESCHLACHT', 'SEETREFFEN', 'SEEGEFECHT', 'SCHLACHTEN', 'SCHLACHT',
         'REITERGEFECHT', 'GEFECHTE', 'GEFECHT', 'TREFFEN', 'BELAGERUNG', 'BELAGERUNO', 'ERSTÜRMUNG',
         'ERSTÜRMUNO', 'ERSTURMUNG', 'EINNAHME', 'KAPITULATION', 'BOMBARDEMENT', 'KANONADE',
         'BESCHIESSUNG', 'KONVENTION', 'CONVENTION', 'STURM', 'ÜBERFALL', 'BLOKADE', 'EINSCHLIESSUNG',
         'SCHLIESSUNG', 'BESTÜRMUNG', 'ANGRIFF', 'KÄMPFE', 'ÜBERGANG')
TYPE = re.compile(r'\b(?:' + '|'.join(TYPES) + r')\b')
DATE = re.compile(r'[0-9OoÖöIl]{1,2}\.?\s*/\s*[0-9OoÖöIl]{1,2}')
LOSS = re.compile(r'\b(?:Verl\.?|Verlust\w*|Offiziersverlust\w*)\s*[:.]?', re.I)
GEO = re.compile(r'^[\W_]*(?:i\s+)?(?:[Kk]leine[rs]?\s+)?(?:Stadt|Dorf|Ort|Festung|Fluß|Markt\w*|Insel|Hafen\w*|Gebirg\w*|Berg|Kap|See|Bai|Burg|Schloß|Kloster|Gegend|Provinz|Dep\.)\b')
PROSE_START = re.compile(r'^(?:Sieg|Die|Der|Das|Vor|Nach|Unentschieden\w*|Siegreiche|Infolge)\s')
COLUMNS = ('id', 'page', 'pages', 'year', 'year_reading', 'date_reading', 'type_reading', 'place',
           'running_head', 'naval', 'record_status', 'side_method', 'winner_text', 'loser_text',
           'winner_commander_text', 'loser_commander_text', 'winner_personnel', 'loser_personnel',
           'winner_strength_reading', 'loser_strength_reading', 'winner_strength_flags', 'loser_strength_flags',
           'indecisive_printed', 'no_combat_printed', 'flags', 'source_id', 'source_sha256', 'locator', 'scan_url', 'source_quote',
           'image_check_id', 'image_source_id', 'image_source_sha256', 'image_checked_fields')


def require(condition, message):
    if not condition:
        raise ValueError('Bodart bulk: ' + message)


def clean(text):
    return ' '.join(text.split())


def fold(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text).lower() if not unicodedata.combining(c))


def source_registry_with_bulk(root):
    """The new table has a companion registry; old studies keep their exact registry bytes."""
    registry = source_registry(root)
    path = Path(root) / ADDITIONS
    if path.is_file():
        sources = read_json(path)['sources']
        require(len({s['id'] for s in sources}) == len(sources), 'duplicate added source ID')
        require(not set(registry).intersection(s['id'] for s in sources), 'added source replaces an old record')
        registry.update({s['id']: s for s in sources})
    return registry


def visual_lines(lines):
    """Join OCR column blocks at the same height; preserve all original XML LINE IDs.

    XML reading order sometimes lists an entire left column before its central labels
    and right column. Personnel totals must be matched by position, not that order.
    """
    groups = []
    for line in sorted(lines, key=lambda l: (sum(l['box'][1::2]) / 2, l['box'][0])):
        y, bottom = line['box'][1], line['box'][3]
        group = groups[-1] if groups else None
        if group and min(bottom, group['box'][3]) - max(y, group['box'][1]) > min(bottom - y, group['box'][3] - group['box'][1]) * .5:
            group['words'].extend(line['words'])
            group['line_ids'].append(line['line'])
            group['box'] = (min(group['box'][0], line['box'][0]), min(group['box'][1], y),
                            max(group['box'][2], line['box'][2]), max(group['box'][3], bottom))
        else:
            groups.append({**line, 'words': list(line['words']), 'line_ids': [line['line']]})
    for group in groups:
        group['words'].sort(key=lambda w: w['box'][0])
        group['line_ids'].sort()
        group['line'] = min(group['line_ids'])
        group['text'] = clean(' '.join(w['text'] for w in group['words']))
    return groups


def layout_pages(root):
    """OCR WORDs retain source line IDs, bounding boxes and recognition confidence."""
    pages = []
    with gzip.open(Path(root) / LAYOUT, 'rb') as source:
        for _, obj in ET.iterparse(source, events=('end',)):
            if obj.tag != 'OBJECT':
                continue
            lines = []
            for i, line in enumerate(obj.iter('LINE')):
                words = []
                for w in line.iter('WORD'):
                    x, bottom, right, y = map(int, w.attrib['coords'].split(','))
                    words.append({'text': w.text or '', 'box': (x, y, right, bottom),
                                  'confidence': int(w.attrib.get('x-confidence', 0))})
                if words:
                    lines.append({'line': i, 'text': clean(' '.join(w['text'] for w in words)), 'words': words,
                                  'box': (min(w['box'][0] for w in words), min(w['box'][1] for w in words),
                                          max(w['box'][2] for w in words), max(w['box'][3] for w in words))})
            pages.append({'leaf': len(pages), 'width': int(obj.attrib['width']),
                          'height': int(obj.attrib['height']), 'lines': visual_lines(lines)})
            obj.clear()
    require(len(pages) == 962, 'unexpected scan page count')
    mapping = read_json(Path(root) / 'data/raw/bodart-1908-v1/page-numbers.json')['pages']
    for page in range(FIRST, LAST + 1):
        require(any(str(x['pageNumber']) == str(page) and x['leafNum'] == page + 1 for x in mapping),
                f'printed-page/scan-leaf mapping changed at {page}')
    return pages


def segment(pages):
    flat, heads = [], {}
    for page in range(FIRST, LAST + 1):
        p = pages[page + 1]
        heads[page] = clean(' '.join(l['text'] for l in p['lines']
                                   if l['box'][1] < p['height'] * .09 and not TYPE.search(l['text'])))
        for line in p['lines']:
            if 'Digitized' in line['text'] and 'Google' in line['text']:
                continue
            if line['box'][1] < p['height'] * .09 and not TYPE.search(line['text']):
                continue
            flat.append({**line, 'page': page, 'width': p['width']})
    starts, last_type = [], None
    for i, line in enumerate(flat):
        if not TYPE.search(line['text']) or len(line['text']) > 190:
            continue
        if last_type is not None and i - last_type <= 5 and not DATE.search(line['text']):
            between = flat[last_type + 1:i]
            if not any(l['text'].startswith('(') or re.search(r'\b(?:Sieg|Die|Streitkräfte|Verluste)\b', l['text'])
                       for l in between):
                continue  # BELAGERUNG / und / EINNAHME is one entry.
        start = i
        if TYPE.match(line['text']) or re.match(r'^\d{4}\s', line['text']):
            for j in range(max(starts[-1] + 1 if starts else 0, i - 3), i):
                if DATE.search(flat[j]['text']) and len(flat[j]['text']) < 100 and not TYPE.search(flat[j]['text']):
                    # Only adjacent header fragments, never a casualty or body sentence.
                    if all(not (PROSE_START.match(l['text']) or '(' in l['text'] or LOSS.search(l['text']))
                           for l in flat[j:i]):
                        start = j
                        break
        require(not starts or start > starts[-1], 'overlapping entry starts')
        starts.append(start)
        last_type = i
    out = []
    for k, start in enumerate(starts):
        lines = flat[start:starts[k + 1] if k + 1 < len(starts) else len(flat)]
        location = next((i for i, l in enumerate(lines[:14]) if i and GEO.match(l['text'])), None)
        prose = next((i for i, l in enumerate(lines) if i and PROSE_START.match(l['text'])), None)
        # Parenthesized aliases are still header text; geographical prose is not a side label.
        if location is None:
            location = next((i for i, l in enumerate(lines[:prose if prose is not None else 12])
                             if i and l['text'].startswith('(')), None)
        stop = location if location is not None else prose if prose is not None else min(3, len(lines))
        header = clean(' '.join(l['text'] for l in lines[:stop]))
        types = list(TYPE.finditer(header))
        require(bool(types), 'entry without event token')
        prefix = header[:types[0].start()].strip()
        yr = re.match(r'^(\S+)\s*(.*)', prefix)
        year_reading = yr[1] if yr else ''
        year = int(year_reading) if re.fullmatch(r'\d{4}', year_reading) and 1618 <= int(year_reading) <= 1905 else None
        rest = header[types[-1].end():].strip()
        tail_date = re.match(r'^(1\d{3}\s+' + DATE.pattern + r'\.?)\s*', rest)
        if tail_date:
            rest = rest[tail_date.end():]
        place = re.sub(r'^(?:(?:bei|von|vor|beim|am|an|auf|zu|um|in|im|der|des|nach)\s+)+', '', rest)
        place = re.sub(r'\s*\([1-6Il]\.\)', '', place).strip()
        if location is not None:
            end = location
            while end + 1 < len(lines) and not re.search(r'\)\W*$', lines[end]['text']):
                if PROSE_START.match(lines[end + 1]['text']):
                    break
                end += 1
            body = lines[end + 1:]
        else:
            body = lines[stop:] if prose is not None else []
        flags = []
        if not year:
            flags.append('unresolved_year_reading')
        if not place or location is None:
            flags.append('unresolved_header')
        if len(place) > 150 or PROSE_START.search(place):
            place = None
            flags.append('unresolved_place_reading')
        if 'BELAGERUNO' in header or 'ERSTÜRMUNO' in header:
            flags.append('ocr_event_spelling')
        if len(re.findall(r'\b1\d{3}\b', header)) > 1:
            flags.append('multiple_year_header_start_year_selected')
        out.append({'id': f'BL{lines[0]["page"]:03d}-{lines[0]["line"]:03d}', 'page': lines[0]['page'],
                    'pages': sorted({l['page'] for l in lines}), 'year': year, 'year_reading': year_reading,
                    'date_reading': clean((yr[2] if yr else '') + (' ' + tail_date[1] if tail_date else '')),
                    'type_reading': ' / '.join(t[0] for t in types),
                    'place': place, 'running_head': heads[lines[0]['page']], 'lines': lines, 'body': body,
                    'header': header, 'flags': flags})
    return out


def parenthetical_strength(clause):
    payloads = [m[1] for m in re.finditer(r'\(([^()]*)\)', clause or '')]
    candidates = [(p, encode_strength(p, 'left')) for p in payloads]
    candidates = [(p, q) for p, q in candidates if q['quantities']]
    usable = [(p, q) for p, q in candidates if q['primary_value'] is not None]
    if len(usable) == 1:
        return usable[0]
    if len(usable) > 1:
        return ' ; '.join(p for p, _ in usable), {'primary_value': None, 'reasons': ['multiple_personnel_readings']}
    return (candidates[0] if len(candidates) == 1 else
            (None, {'primary_value': None, 'reasons': ['no_unambiguous_personnel_reading']}))


def table_value(line, label):
    """Nearest printed numeric token on each side of a central personnel-total label.

    No components are summed. A malformed token remains a literal with a null value.
    """
    words = line['words']
    lo, hi = label
    numeric = []
    for i, w in enumerate(words):
        if not line['width'] * .24 < (w['box'][0] + w['box'][2]) / 2 < line['width'] * .76:
            continue  # Outer equipment columns cannot be personnel totals.
        literal = w['text'].strip()
        if not re.match(r'^\d', literal):
            continue
        try:
            value = number(literal)
        except ValueError:
            value = None
        numeric.append((i, literal, value))
    left = [x for x in numeric if x[0] < lo]
    right = [x for x in numeric if x[0] > hi]
    pair = [left[-1] if left else None, right[0] if right else None]
    for side, cell in enumerate(pair):
        if cell and ((cell[0] > 0 and re.fullmatch(r'\d+', words[cell[0] - 1]['text'].strip())) or
                     (cell[0] + 1 < len(words) and re.fullmatch(r'\d+', words[cell[0] + 1]['text'].strip()))):
            # Split digit groups could be a headcount or adjacent counts: retain unknown.
            pair[side] = (cell[0], cell[1], None)
    return pair


def printed_parts(clause):
    """Keep the whole printed force description; do not trim it to a modern nation lexicon."""
    end = napoleonic.at_depth0(clause, napoleonic.SIDE_END)
    force = (clause[:end.start()] if end else clause).strip(' ,.;') or None
    commander = None
    if end and end[0].strip() == 'unter':
        rest = re.sub(r'^(?:dem|den)\s+', '', clause[end.end():])
        stop = napoleonic.at_depth0(rest, napoleonic.COMMANDER_END)
        commander = (rest[:stop.start()] if stop else rest).strip(' ,.;')
        commander = re.sub(r'\([^()]*\d[^()]*\)', '', commander).strip(' ,.;') or None
    return force, commander


def ocr_sides(entry):
    result = {k: None for k in ('winner_text', 'loser_text', 'winner_commander_text', 'loser_commander_text',
                                'winner_personnel', 'loser_personnel', 'winner_strength_reading', 'loser_strength_reading')}
    result.update(side_method='unparsed', winner_strength_flags='missing', loser_strength_flags='missing')
    body = entry['body']
    before_loss = []
    for line in body:
        if LOSS.search(line['text']):
            break
        before_loss.append(line)
    text = clean(' '.join(l['text'] for l in before_loss))
    # Losses, survivors and officer-loss tables cannot supply strength readings.
    strength_text = LOSS.split(text, maxsplit=1)[0]
    normalized = re.sub(r'\b(der|die|den)(?=[A-ZÄÖÜ])', r'\1 ', strength_text)
    for name, rx in napoleonic.PROSE:
        m = rx.search(normalized)
        if not m:
            continue
        w, l = m['w'], m['l']
        if name in napoleonic.LOSER_FIRST and napoleonic.WINNER_VERB.search(l):
            continue
        result['side_method'] = name
        for key, clause in (('winner', w), ('loser', l)):
            force, commander = printed_parts(clause)
            literal, q = parenthetical_strength(clause)
            result[key + '_text'] = force
            result[key + '_commander_text'] = commander
            result[key + '_strength_reading'] = literal
            result[key + '_personnel'] = q['primary_value']
            result[key + '_strength_flags'] = ';'.join(q['reasons']) or 'ocr_candidate'
            if clause.count('(') != clause.count(')'):
                result[key + '_strength_flags'] += ';unbalanced_ocr_parentheses'
        return result
    marker = next((i for i, l in enumerate(body) if 'streitkrafte' in fold(l['text']).replace(' ', '')), None)
    if marker is None:
        return result
    headers = body[:marker + 1]
    # The two printed columns are descriptions, not resolved person identities.
    cells_by_side = [[], []]
    for line in headers:
        cells = [clean(' '.join(w['text'] for w in line['words']
                               if 'streitkrafte' not in fold(w['text']) and
                               (sum(w['box'][::2]) / 2 < line['width'] / 2) == left))
                 for left in (True, False)]
        for j, cell in enumerate(cells):
            if cell:
                cells_by_side[j].append(cell)
    for key, cells in zip(('winner', 'loser'), cells_by_side):
        if cells:
            result[key + '_text'] = cells[0]
            commander = ' '.join(c for c in cells[1:] if not c.startswith('(')).strip(' :')
            result[key + '_commander_text'] = re.sub(r'^.*?\)\s*(?=Gen\.|FM\.|FML\.)', '', commander) or None
    result['side_method'] = 'table_left_winner_by_bodart_p46'
    for line in body[marker + 1:]:
        if LOSS.search(line['text']):
            break
        tokens = [fold(w['text']) for w in line['words']]
        total = next((i for i, t in enumerate(tokens) if 'gesamt' in t), None)
        crew = next((i for i, t in enumerate(tokens) if 'bemannung' in t or 'mannschaft' in t), None)
        if total is not None and 'starke' in fold(line['text']):
            end = next((i for i in range(total, len(tokens)) if 'starke' in tokens[i]), total)
            pair = table_value(line, (total, end))
        elif crew is not None:
            pair = table_value(line, (crew, crew))
        else:
            continue
        for key, cell in zip(('winner', 'loser'), pair):
            if cell:
                _, literal, value = cell
                result[key + '_strength_reading'] = literal
                result[key + '_personnel'] = value if value is not None and value > 0 else None
                result[key + '_strength_flags'] = 'ocr_candidate' if value else 'malformed_numeric_reading'
        break
    return result


def source_row(entry, source):
    lines = entry['lines']
    locators = '; '.join(f'p{p}: XML OBJECT {p + 1}, LINE ' + ','.join(str(i) for l in lines if l['page'] == p for i in l['line_ids'])
                         for p in entry['pages'])
    sides = ocr_sides(entry)
    return {**{k: entry[k] for k in ('id', 'page', 'pages', 'year', 'year_reading', 'date_reading', 'type_reading',
                                    'place', 'running_head', 'flags')}, **sides,
            'naval': any(t.startswith('SEE') for t in entry['type_reading'].split(' / ')),
            'record_status': 'ocr_candidate_not_image_verified',
            'indecisive_printed': 'unentschieden' in fold(entry['header'] + ' '.join(l['text'] for l in entry['body'][:2])),
            'no_combat_printed': bool(re.search(r'ohne\s+(?:Schwertstreich|Kampf)|kampflos',
                                               ' '.join(l['text'] for l in entry['body']), re.I)),
            'source_id': SOURCE, 'source_sha256': source['sha256'], 'locator': locators,
            'scan_url': f'https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n{entry["page"] + 1}/mode/1up',
            'source_quote': clean(entry['header'] + ' ' + LOSS.split(clean(' '.join(l['text'] for l in entry['body'])), 1)[0]),
            'image_check_id': None, 'image_source_id': None, 'image_source_sha256': None, 'image_checked_fields': []}


def checked_row(raw, frame, source, sections):
    row = {k: raw[k] for k in ('id', 'page', 'pages', 'place', 'running_head')}
    row.update(id=frame['id'], year=frame['start_year'], year_reading=frame['year_printed'],
               date_reading=frame['date_printed'], type_reading=frame['type_printed'], naval=frame['naval'],
               record_status='existing_image_checked_transcription', side_method=frame['side_method'],
               indecisive_printed=frame['indecisive_printed'], flags=list(frame['date_flags']),
               no_combat_printed=frame['no_combat_printed'],
               source_id=MANUAL_SOURCE, source_sha256=source['sha256'],
               locator='; '.join(f'p{p:03d}, entry {frame["id"]}' for p in raw['pages']),
               scan_url=f'https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n{raw["page"] + 1}/mode/1up',
               source_quote=clean(' '.join(raw['text'][:3])))
    for key, column in (('winner', 'left'), ('loser', 'right')):
        literal = frame[key + '_strength_printed']
        index = 0 if column == 'left' else 2
        table = any(' | ' in line and re.search(r'Gesamt\s*-\s*Stärke', line) and
                    line.split(' | ')[index].strip() == literal for line in raw['text'])
        q = encode_strength(literal, column, table=table)
        row.update({key + '_text': frame[key + '_text'], key + '_commander_text': frame[key + '_commander_text'],
                    key + '_personnel': q['primary_value'], key + '_strength_reading': literal,
                    key + '_strength_flags': ';'.join(q['reasons'])})
    row.update(image_check_id=None, image_source_id=None, image_source_sha256=None, image_checked_fields=[])
    if frame.get('override_reason'):
        row['flags'].append('existing_frame_override: ' + frame['override_reason'])
    require(all(f'p{p:03d}' in sections for p in raw['pages']), 'manual source page absent')
    return row


def apply_image_checks(root, rows, registry):
    checks = read_json(root / CHECKS)
    by_id = {r['id']: r for r in rows}
    comparison, counts = [], Counter()
    seen = set()
    for check in checks['entries']:
        row = by_id[check['row_id']]
        require(row['id'] not in seen and row['page'] == check['page'], 'duplicate or misplaced image check')
        seen.add(row['id'])
        source = registry[check['source_id']]
        require(source['sha256'] == check['source_sha256'] == digest(root / source['path']), 'changed sample image')
        fields = check['checked_fields']
        require(set(fields) == {'year', 'place', 'winner_personnel', 'loser_personnel'}, 'unexpected image-check scope')
        require(row['record_status'] == 'ocr_candidate_not_image_verified', 'sample cannot overwrite checked transcription')
        differences = {}
        for name, value in fields.items():
            status = ('not_comparable' if value is None else 'missing' if row[name] is None else
                      'agree' if row[name] == value else 'disagree')
            if name.endswith('_personnel'):
                counts[status] += 1
            differences[name] = {'ocr': row[name], 'image_reading': value, 'status': status}
            row[name] = value
        row.update(record_status='ocr_candidate_with_checked_fields', image_check_id=check['id'],
                   image_source_id=source['id'], image_source_sha256=source['sha256'],
                   image_checked_fields=list(fields))
        row['flags'].append('only_header_year_place_and_personnel_image_checked')
        for side in ('winner', 'loser'):
            row[side + '_strength_flags'] += ';primary_image_reading:' + check['id']
        comparison.append({'check_id': check['id'], 'row_id': row['id'], 'fields': differences})
    require(sorted({by_id[c['row_id']]['page'] for c in checks['entries']}) == checks['selection']['pages'],
            'sample page coverage changed')
    require(all(r['id'] in seen for r in rows if r['page'] in checks['selection']['pages']),
            'sample omits a detected entry on a selected page')
    return {'use': checks['selection']['purpose'], 'scope': checks['scope'], 'pages': checks['selection']['pages'],
            'entries': len(seen), 'personnel_fields_before_image_corrections': dict(counts), 'rows': comparison}


def build(root):
    root = Path(root)
    registry = source_registry_with_bulk(root)
    additions = read_json(root / ADDITIONS)
    require(additions['kind'] == 'bodart_bulk_source_additions' and additions['version'] == 1, 'source manifest identity')
    added = {s['id']: s for s in additions['sources']}
    validate_source_metadata(root, added)
    for s in added.values():
        require(s['independence_group'] == 'bodart-kriegs-lexikon-1908', 'source family changed')
        require(digest(safe_path(root, s['path'])) == s['sha256'], 'changed bulk raw source: ' + s['id'])
        require(s['parent_sha256'] == registry[s['parent_source_id']]['sha256'], 'source parent binding')
    source, manual = registry[SOURCE], registry[MANUAL_SOURCE]
    require(digest(root / LAYOUT) == source['sha256'], 'changed layout source')
    require(digest(root / napoleonic.TRANSCRIPTION) == manual['sha256'], 'changed checked transcription')
    pages = layout_pages(root)
    detected = segment(pages)
    raw = napoleonic.entries((root / napoleonic.TRANSCRIPTION).read_text(encoding='utf-8'))
    frames = read_json(root / FRAME)['entries']
    sections = text_sections((root / napoleonic.TRANSCRIPTION).read_text(encoding='utf-8'))
    by_page, old_by_page = defaultdict(list), defaultdict(list)
    for e in detected:
        by_page[e['page']].append(e)
    for e in raw:
        old_by_page[e['page']].append(e)
    frame_by = {e['id']: e for e in frames}
    rows = [source_row(e, source) for e in detected if not 268 <= e['page'] <= 490]
    replay, counts = [], Counter()
    for page, entries in old_by_page.items():
        candidates = by_page[page]
        require(len(candidates) == len(entries), f'entry detection disagrees with checked p{page}')
        for candidate, old in zip(candidates, entries):
            f = frame_by[old['id']]
            row = checked_row(old, f, manual, sections)
            rows.append(row)
            test = source_row(candidate, source)
            fields = {}
            for field in ('winner_personnel', 'loser_personnel'):
                expected, actual = row[field], test[field]
                status = ('not_comparable' if expected is None else 'missing' if actual is None else
                          'agree' if expected == actual else 'disagree')
                counts[status] += 1
                fields[field] = {'checked': expected, 'ocr': actual, 'status': status}
            replay.append({'checked_id': old['id'], 'ocr_id': candidate['id'], 'fields': fields})
    image_checks = apply_image_checks(root, rows, registry)
    rows.sort(key=lambda r: (r['page'], int(re.search(r'\d+$', r['id'])[0]) if r['id'].startswith('BL') else
                             ord(r['id'][-1]) - ord('a')))
    require(len({r['id'] for r in rows}) == len(rows), 'duplicate row identity')
    require(all(r[k] is None or r[k] > 0 for r in rows for k in ('winner_personnel', 'loser_personnel')),
            'nonpositive personnel reading')
    return rows, {'kind': 'bodart_whole_volume_extraction', 'version': 1,
                  'status': 'provisional_source_table_not_model_input', 'historical_outcomes_fitted': False,
                  'independent_of_arsht_inputs_and_code': True,
                  'source_sha256': {SOURCE: source['sha256'], MANUAL_SOURCE: manual['sha256']},
                  'conventions_source_sha256': {k: registry[k]['sha256'] for k in
                                               ('bodart-1908-p045-image-v1', 'bodart-1908-p046-image-v1',
                                                'bodart-1908-p047-image-v1')},
                  'input_sha256': {p: digest(root / p) for p in (LAYOUT, FRAME, napoleonic.TRANSCRIPTION,
                                                               'data/raw/bodart-1908-v1/page-numbers.json', CHECKS, ADDITIONS)},
                  'coverage': {'detail_pages': LAST - FIRST + 1, 'page_range': [FIRST, LAST], 'entries': len(rows),
                               'new_ocr_candidates': sum(r['record_status'].startswith('ocr') for r in rows),
                               'existing_checked_entries': len(raw),
                               'new_entries_with_sample_field_checks': image_checks['entries'],
                               'source_status': dict(Counter(r['record_status'] for r in rows)),
                               'naval': sum(r['naval'] for r in rows),
                               'paired_personnel_readings': sum(all(r[k] is not None for k in
                                                                  ('winner_personnel', 'loser_personnel')) for r in rows),
                               'both_commanders_named': sum(bool(r['winner_commander_text'] and r['loser_commander_text'])
                                                            for r in rows),
                               'unresolved_years': sum(r['year'] is None for r in rows),
                               'by_century': dict(Counter(str((r['year'] - 1) // 100 + 1) if r['year'] else 'unknown'
                                                          for r in rows))},
                  'primary_image_checks': image_checks,
                  'extraction_replay': {'use': 'development comparison, not blind validation',
                                       'entries': len(raw), 'personnel_fields': dict(counts), 'rows': replay}}


def table_csv(rows):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fieldnames=COLUMNS, lineterminator='\n')
    writer.writeheader()
    for r in rows:
        writer.writerow({k: json.dumps(r[k], ensure_ascii=False) if isinstance(r[k], list) else r[k] for k in COLUMNS})
    return out.getvalue()


def report(rows, meta):
    c, replay = meta['coverage'], meta['extraction_replay']
    lines = ['# Bodart: a direct table across 1618–1905', '',
             f'**{c["entries"]:,} candidate entries across all {c["detail_pages"]} battle-description pages '
             '(pp. 49–600).** This expands directly from Gaston Bodart’s 1908 compilation. '
             'No Arsht dataset, code or ranking supplies the table.', '',
             '[Download the complete CSV](bodart-bulk-v1.csv) · [Extraction counts and checks](bodart-bulk-v1.json)', '',
             '## What is ready', '',
             f'- {c["existing_checked_entries"]} entries reuse our image-checked Napoleonic-period transcription, '
             'including entries outside the French land cohort. Frozen cohorts and model inputs stay unchanged.',
             f'- {c["new_ocr_candidates"]} additional entries come from layout-aware OCR. '
             f'{c["new_entries_with_sample_field_checks"]} have scoped image checks and corrections; '
             f'{c["new_ocr_candidates"] - c["new_entries_with_sample_field_checks"]} remain '
             'machine readings. Commander names and identities are provisional throughout the new section.',
             f'- {c["paired_personnel_readings"]} entries have two numerical personnel readings; '
             f'{c["both_commanders_named"]} have two printed commander strings. Unknown values stay blank. '
             'A printed string is not a resolved identity or an allocation of credit.',
             f'- {c["naval"]} naval entries remain visible, with naval/personnel distinctions. '
             f'{c["unresolved_years"]} year readings remain unresolved rather than silently corrected.', '',
             '## What the figures mean', '',
             'This is a source extraction table, not a new ratings run. No model was fitted and no '
             'predictor admitted. Counts describe detected entries, not complete historical coverage. '
             'Bodart selects consequential or high-loss engagements, says he excludes colonial wars from this '
             'section, rounds figures, includes available forces beyond those actually engaged, and '
             'assigns a winner even to some indecisive battles. His table convention puts that winner '
             'on the left ([explanatory notes, pp. 45–47](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n46/mode/1up)). '
             'These conventions limit future modelling.', '',
             'The selection is not all wars or all engagements. Overseas engagements within the listed '
             'European wars still occur, such as Cuddalore. Multiple commanders, overlapping operations, '
             'indecisive results and no-combat capitulations require explicit treatment before any fit.', '',
             'The OCR’s word positions keep opposing columns separate. Only an explicitly printed '
             'personnel total is selected; components, guns, ships, casualties and survivors are not '
             'mechanically turned into a whole-side force. OCR errors remain possible even at high '
             'recognition confidence. New OCR rows retain their candidate status and are not automatically '
             'eligible for a model.', '',
             '## Check against existing work', '',
             f'The detector recovers all {replay["entries"]} existing entry starts with the same counts per '
             'printed page. This is a development check: the detector vocabulary was adjusted using these '
             'pages. It is not an independent review or proof of recall elsewhere.', '',
             '| Personnel field comparison | Fields |', '| --- | ---: |']
    lines += [f'| {k} | {v} |' for k, v in sorted(replay['personnel_fields'].items())]
    lines += ['', 'The final table uses the checked transcription on these pages, not the OCR values. '
              'The JSON retains every agreement, disagreement and missing reading. Matching an OCR number '
              'to a checked transcription does not establish that Bodart’s historical figure is correct.', '',
              '## Small page-image check', '',
              f'The primary inspected {meta["primary_image_checks"]["entries"]} entry headers and personnel fields '
              f'on {len(meta["primary_image_checks"]["pages"])} fixed pages outside the existing transcription. '
              'This is a small spread across the volume used to check and refine extraction, not a blind accuracy '
              'estimate. The original OCR, initial readings, current parser differences, image hashes and scoped '
              'corrections remain visible in the [check record](../data/bodart/image-checks-v1.json) and JSON.', '',
              '| Personnel comparison before scoped image corrections | Fields |', '| --- | ---: |']
    lines += [f'| {k} | {v} |' for k, v in sorted(meta['primary_image_checks']['personnel_fields_before_image_corrections'].items())]
    lines += ['', 'Lagoulin (p. 595) illustrates the risk: the scan prints **20,000 / 24,000**, while OCR '
              'reads **90,000 / 84,000**. The sampled table fields use the scan readings, with explicit field '
              'provenance. This does not verify every field in those rows or the remaining OCR rows.', '',
              'The CSV keeps the original strength literal alongside the corrected numerical field. '
              '`image_checked_fields`, `image_check_id` and the image source ID/hash identify the exact '
              'override; the check record supplies its reading and locator. Other fields retain OCR status.', '',
              '## Coverage by century', '', '| Century | Entries |', '| --- | ---: |']
    lines += [f'| {k} | {v} |' for k, v in sorted(c['by_century'].items())]
    lines += ['', '## A few entries to inspect', '',
              '| Page | Year reading | Place | Winner personnel | Loser personnel | Source status |',
              '| ---: | --- | --- | ---: | ---: | --- |']
    shown = set()
    for row in rows:
        century = (row['year'] - 1) // 100 if row['year'] else None
        if century is None or century in shown:
            continue
        shown.add(century)
        lines.append(f'| {row["page"]} | {row["year_reading"]} | [{row["place"]}]({row["scan_url"]}) | '
                     f'{row["winner_personnel"] if row["winner_personnel"] is not None else "unknown"} | '
                     f'{row["loser_personnel"] if row["loser_personnel"] is not None else "unknown"} | '
                     f'{row["record_status"]} |')
    lines += ['', '## Reproduce', '',
              '`python3 -m generalship.bodart_bulk --write` rebuilds the CSV, metadata and this report '
              'offline. With no flag it checks them. `--inspect ID` prints a structured record with its quoted '
              'source text. Every row retains source ID, SHA-256, printed pages, scan link and XML line IDs or '
              'transcription locator. Source quotes normalize OCR whitespace; they are not facsimile '
              'transcriptions unless explicitly labelled as checked.', '',
              'The new XML snapshot is the original Internet Archive OCR layout, checked against the '
              'SHA-1 in our previously pinned item metadata, then gzip-compressed losslessly with a fixed '
              'timestamp. It is one source family with the existing Bodart scan and transcription. '
              'Frozen Napoleonic development/final reservations and all old model records remain intact.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--inspect')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    rows, meta = build(root)
    if args.inspect:
        row = next(r for r in rows if r['id'] == args.inspect)
        print(json.dumps(row, ensure_ascii=False, indent=2))
        return
    text, csv_text = report(rows, meta), table_csv(rows)
    if args.write:
        (root / CSV).write_text(csv_text, encoding='utf-8')
        write_json(root / META, meta)
        (root / REPORT).write_text(text, encoding='utf-8')
    else:
        require((root / CSV).read_text(encoding='utf-8') == csv_text, 'CSV differs; regenerate')
        require(read_json(root / META) == meta, 'metadata differs; regenerate')
        require((root / REPORT).read_text(encoding='utf-8') == text, 'report differs; regenerate')
    print(f'Bodart bulk: {len(rows)} entries; no model fit; new OCR readings remain candidates.')


if __name__ == '__main__':
    main()
