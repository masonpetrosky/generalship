"""Prepare a compiler-description dataset; never fit historical outcomes."""

import argparse
from collections import Counter
import csv
import hashlib
import io
import json
from pathlib import Path
import re

from . import napoleonic
from .evidence import citation_text
from .sources import digest, read_json, source_metadata_digest, text_sections, write_json

BASE = 'data/napoleonic/benchmark-v1'
SCOPE, PROTOCOL, SNAPSHOT = (BASE + '/' + name + '.json' for name in ('scope', 'protocol', 'source-snapshot'))
OWNER, PROPOSAL = BASE + '/owner-decision.json', BASE + '/run-proposal.json'
CONTEXT = BASE + '/context.json'
DESIGN = 'docs/napoleonic-benchmark-v1.md'
ARTIFACT = 'artifacts/napoleonic-benchmark-v1'
CODE = 'generalship/napoleonic_benchmark.py'
RUN_CODE = 'generalship/napoleonic_benchmark_run.py'
SOURCE = 'bodart-1908-transcription-v1'
NUMBER = r'\d+(?:[. ]\d+)*'
QUALIFIED = rf'(?:ca\.?\s*)?{NUMBER}'
GUN = r'(?:Gesch(?:ütze[n]?)?\.?|Kanonen)'
UNITS = r'M\.?|Inft\.?|Kav\.?-?|Art\.?|Genie|Reiter|Geschütze[n]?|Gesch\.?|Kanonen|Kan\.?|Btln\.?|Btl\.?|Esk\.?|Offz\.?|Streitbare'
TOKENS = re.compile(rf'(?<![\d.])(?P<literal>(?:ca\.?\s*)?{NUMBER})\s*(?P<unit>{UNITS})(?!\w)')
PHASE = re.compile(r'\b(?:urspr|ursprünglich|noch|Beginn|Schluß|Schluss|Schlusse|Ende|während|anfangs|mehr)\b', re.I)


def require(condition, message):
    if not condition:
        raise ValueError('Napoleonic benchmark: ' + message)


def number(literal):
    clean = re.sub(r'^ca\.?\s*', '', literal).strip()
    require(re.fullmatch(r'\d+|\d{1,3}(?:\.\d{3})+|\d{1,3}(?: \d{3})+', clean),
            'unresolved numeric notation: ' + literal)
    return int(clean.replace('.', '').replace(' ', ''))


def quantity(literal, unit, basis):
    try:
        value = number(literal)
    except ValueError:
        value = None
    return {'literal': literal, 'value': value, 'unit': unit, 'basis': basis,
            'precision': 'approximate' if literal.startswith('ca') else 'reported_point'}


def encode_strength(printed, column, table=False):
    """Column is transcription layout, not a model feature or outcome criterion."""
    result = {'printed': printed, 'quantities': [], 'total_value': None, 'primary_value': None,
              'phase': 'entry_state_unspecified', 'footnote_markers': [], 'approximate': False,
              'disposition': 'missing_extract', 'reasons': ['missing_frame_extract']}
    if printed is None:
        return result
    result['footnote_markers'] = re.findall(r'\[(\d+)\]', printed)
    clean = re.sub(r'\[\d+\]', '', printed).strip()
    result['disposition'], result['reasons'] = 'ambiguous', []
    chosen = None
    if table:
        patterns = ([rf'(?P<gun>{QUALIFIED})\s*{GUN}\s*(?P<people>{QUALIFIED})'] if column == 'left' else
                    [rf'(?P<people>{QUALIFIED})\s*{GUN}\s*(?P<gun>{QUALIFIED})',
                     rf'(?P<people>{QUALIFIED})\s+(?P<gun>{QUALIFIED})\s*{GUN}'])
        patterns.append(rf'(?P<people>{QUALIFIED})')
        matches = [m for pattern in patterns if (m := re.fullmatch(pattern, clean))]
        if len(matches) == 1:
            m = matches[0]
            chosen = quantity(m['people'], 'people', 'compiler_total')
            result['quantities'].append(chosen)
            if m.groupdict().get('gun'):
                result['quantities'].append(quantity(m['gun'], 'guns', 'equipment'))
        else:
            result['reasons'].append('unresolved_strength_table_cell')
    else:
        matches = list(TOKENS.finditer(clean))
        total_matches = []
        for m in matches:
            u = m['unit']
            if u in ('M.', 'M', 'Streitbare'):
                basis, unit = ('unspecified_personnel' if u != 'Streitbare' else 'reported_effectives'), 'people'
            elif u.startswith(('Inft', 'Kav', 'Art', 'Genie')) or u == 'Reiter':
                basis, unit = u.rstrip('.-'), 'people'
            elif u.startswith(('Gesch', 'Kan')):
                basis, unit = 'equipment', 'guns'
            elif u.startswith('Offz'):
                basis, unit = 'officer_subset', 'people'
            else:
                basis, unit = 'organizational_units', 'formations'
            q = quantity(m['literal'], unit, basis)
            q['position'] = [m.start(), m.end()]
            result['quantities'].append(q)
            suffix = clean[m.end():]
            if u in ('M.', 'M') and not re.match(r'\s*(?:Inft|Kav|Art|Genie)', suffix):
                if m.start() == 0 or re.search(r'(?:=|\bzus\.)\s*$', clean[:m.start()]):
                    total_matches.append(q)
        if total_matches:
            # The last explicitly printed aggregate subsumes earlier components.
            # Multiple unaggregated temporal totals are excluded below, never selected by size.
            chosen = total_matches[-1]
        else:
            result['reasons'].append('no_unambiguous_whole_side_personnel_total')
        if PHASE.search(clean) or re.search(r'\bvon\s+\d', clean):
            result['phase'] = 'explicit_phase_or_multiple_states'
            result['reasons'].append('explicit_phase_or_multiple_states')
    if chosen:
        result['total_value'] = chosen['value']
        result['approximate'] = chosen['precision'] == 'approximate'
        if chosen['value'] is None:
            result['reasons'].append('malformed_numeric_notation')
        elif chosen['value'] <= 0:
            result['reasons'].append('nonpositive_personnel_total')
    if not result['reasons'] and chosen:
        result.update(disposition='eligible', primary_value=chosen['value'])
    return result


def load_inputs(root):
    scope, protocol = read_json(root / SCOPE), read_json(root / PROTOCOL)
    for path, sha in scope['bindings'].items():
        require(digest(root / path) == sha, 'changed frozen input: ' + path)
    evaluation = read_json(root / 'data/napoleonic/methods-v1/evaluation.json')
    require(scope['development_ids'] == evaluation['development'] and scope['reserved_final_ids'] == evaluation['reserved_final'],
            'changed development/final partition')
    require(len(scope['development_ids']) == 273 and len(set(scope['development_ids'])) == 273
            and len(scope['reserved_final_ids']) == 52 and not set(scope['development_ids']) & set(scope['reserved_final_ids']),
            'partition counts/overlap')
    require(not scope['authorizes_historical_fit'] and not protocol['authorizes_historical_fit'], 'preparation scope permits a fit')
    require(protocol == fixed_protocol(), 'changed fixed protocol')
    frame = {r['id']: r for r in read_json(root / napoleonic.FRAME)['entries']}
    require(scope['development_groups'] == {g: ids for g, ids in evaluation['frozen_groups'].items()
                                           if set(ids) <= set(scope['development_ids'])}, 'split/changed campaign groups')
    raw = {r['id']: r for r in napoleonic.entries((root / napoleonic.TRANSCRIPTION).read_text())}
    registry = {s['id']: s for s in read_json(root / 'data/sources.json')['sources']}
    return scope, protocol, frame, raw, registry


def fixed_protocol():
    return {'kind': 'napoleonic_compiler_benchmark_protocol', 'version': 1, 'profile': 'compiler_personnel_total_v1',
            'feature': '(A-B)/(A+B)', 'ridge': 1.0, 'comparators': ['equal_odds', 'training_laplace_prior'],
            'evaluations': ['leave_campaign_out', 'leave_war_out', 'forward_1813'],
            'populations': ['primary', 'exclude_indecisive', 'exclude_no_combat', 'unqualified_totals'],
            'bootstrap': {'draws': 10000, 'seed': 20261020, 'interval': [0.025, 0.975],
                          'unit': 'held_out_campaign_group', 'evaluations': ['leave_campaign_out']},
            'calibration_edges': [0.0, 0.2, 0.4, 0.6, 0.8, 1.0], 'minimum_training_rows': 2,
            'model_selection': False, 'reserved_final_numerical_use': False, 'authorizes_historical_fit': False}


def source_snapshot(root, scope, frame, registry):
    ids = {SOURCE}
    pages = {45, 46, 47} | {p for b in scope['development_ids'] for p in frame[b]['pages']}
    ids.update(f'bodart-1908-p{p:03d}-image-v1' for p in pages)
    while True:
        parents = {registry[s]['parent_source_id'] for s in ids if registry[s].get('parent_source_id')}
        if parents <= ids:
            break
        ids |= parents
    return {'kind': 'benchmark_source_snapshot', 'sources': [registry[s] for s in sorted(ids)]}


def passages_for(printed, column, entry, sections, frame):
    if printed is None:
        # A locator is retained; absence of an extract is not a claim that a literature is silent.
        return [], False
    lines = entry['text']
    table_rows = [line for line in lines if ' | ' in line and re.search(r'Gesamt\s*-\s*Stärke', line)]
    index = 0 if column == 'left' else 2
    is_table = any(line.split(' | ')[index].strip() == printed for line in table_rows)
    selected = [line for line in table_rows if line.split(' | ')[index].strip() == printed] if is_table else [
        lines[0]] if printed in lines[0] else []
    require(selected, 'strength extract absent from entry ' + frame['id'])
    out = []
    for line in dict.fromkeys(selected):
        for page in frame['pages']:
            if line in sections[f'p{page}']:
                out.append({'source_id': SOURCE, 'section': f'p{page}', 'quote': line,
                            'locator': f'Bodart (1908), p. {page}, entry {frame["id"]}; {column} printed side field'})
    require(out, 'strength passage absent from pinned page: ' + frame['id'])
    return out, is_table


def build(root):
    scope, protocol, frame, raw, registry = load_inputs(root)
    snapshot = read_json(root / SNAPSHOT)
    require(snapshot == source_snapshot(root, scope, frame, registry), 'changed source snapshot/metadata')
    for source in snapshot['sources']:
        require(digest(root / source['path']) == source['sha256'], 'changed raw source: ' + source['id'])
    sections = text_sections((root / napoleonic.TRANSCRIPTION).read_text())
    context = read_json(root / CONTEXT)
    for item in context['conventions'] + context['footnotes']:
        cite, source = item['citation'], registry[item['citation']['source_id']]
        image = registry[item['facsimile_source_id']]
        require(item['raw_sha256'] == source['sha256'] and item['facsimile_sha256'] == image['sha256']
                and cite['quote'] in citation_text(root, registry, cite), 'context/translation source binding')
    footnote_renderings = {r['id']: r['interpretation_en'] for r in context['footnotes']}
    rows = []
    for b in scope['development_ids']:
        e = frame[b]
        row = {key: e[key] for key in ('id', 'place', 'campaign_group', 'war', 'start_year', 'start_date', 'end_date',
                                       'indecisive_printed', 'no_combat_printed')}
        row['battle_id'] = row.pop('id')
        row['sides'] = {}
        for side, key in [('A', e['french_side']), ('B', 'loser' if e['french_side'] == 'winner' else 'winner')]:
            column = 'left' if key == 'winner' else 'right'
            printed = e[key + '_strength_printed']
            cites, table = passages_for(printed, column, raw[b], sections, e) if printed is not None else ([], False)
            record = encode_strength(printed, column, table)
            record['context_footnote_markers'] = sorted(set(marker for c in cites
                for marker in re.findall(r'\[(\d+)\]', c['quote'])))
            footnotes = []
            for marker in sorted(set(record['footnote_markers'] + record['context_footnote_markers'])):
                found = []
                for page in e['pages']:
                    for line in sections[f'p{page}'].splitlines():
                        if line.startswith(f'[{marker}] '):
                            found.append({'source_id': SOURCE, 'section': f'p{page}', 'quote': line,
                                          'locator': f'Bodart (1908), p. {page}, note [{marker}]; applicability retained as printed'})
                require(found, 'footnote locator missing for ' + b)
                for cite in found:
                    cite['interpretation_en'] = footnote_renderings[cite['section'] + ':' + marker]
                    cite['association_scope'] = 'entry strength passage; individual side applicability is not newly adjudicated'
                footnotes.extend(found)
            for cite in cites + footnotes:
                require(cite['quote'] in citation_text(root, registry, cite), 'quote absent from source section')
            record.update(source_column=column, citations=cites, footnotes=footnotes,
                          primary_unit='people' if record['primary_value'] is not None else None,
                          source_id=SOURCE, raw_sha256=registry[SOURCE]['sha256'],
                          metadata_sha256=source_metadata_digest(registry[SOURCE]),
                          page_images=[{'source_id': f'bodart-1908-p{p:03d}-image-v1',
                                        'sha256': registry[f'bodart-1908-p{p:03d}-image-v1']['sha256']} for p in e['pages']],
                          population='compiler_reported_personnel; complete combatant/all-ranks coverage unestablished',
                          reported_period=f'{e["start_date"]} to {e["end_date"]}; ' + record['phase'],
                          interpretation_en='Primary English rendering of the encoding: '
                          + (f'compiler personnel total {"about " if record["approximate"] else ""}{record["primary_value"]}; '
                             'exact state time and all-ranks coverage unestablished.'
                             if record['primary_value'] is not None else
                             'no eligible whole-side total in this frozen extract under the descriptive profile; retain literal figures and reasons.'))
            row['sides'][side] = record
        row['eligible'] = all(r['disposition'] == 'eligible' for r in row['sides'].values())
        row['exclusions'] = [f'{s}:{reason}' for s, r in row['sides'].items() for reason in r['reasons']]
        rows.append(row)
    return {'kind': 'napoleonic_compiler_benchmark_dataset', 'version': 1, 'status': 'prepared_not_authorized_for_fit',
            'profile': protocol['profile'], 'historical_outcomes_fitted': False,
            'structured_target_column_included': False, 'provenance_can_reveal_outcomes': True,
            'feature_whitelist': ['sides.A.primary_value', 'sides.B.primary_value'],
            'input_sha256': {p: digest(root / p) for p in [SCOPE, PROTOCOL, SNAPSHOT, OWNER, CONTEXT, DESIGN, CODE]},
            'source_conventions': context['conventions'],
            'entries': rows}


def flat_csv(data):
    out = io.StringIO(newline='')
    columns = ['battle_id', 'campaign_group', 'side', 'printed', 'disposition', 'total_value', 'primary_value',
               'primary_unit', 'quantities', 'approximate', 'phase', 'population', 'reported_period', 'reasons',
               'source_column', 'source_id', 'raw_sha256', 'metadata_sha256', 'citations', 'page_images',
               'footnote_markers', 'context_footnote_markers', 'footnotes', 'interpretation_en']
    writer = csv.DictWriter(out, fieldnames=columns, lineterminator='\n')
    writer.writeheader()
    for row in data['entries']:
        for side, record in row['sides'].items():
            flat = {k: record[k] for k in columns if k in record}
            flat.update(battle_id=row['battle_id'], campaign_group=row['campaign_group'], side=side)
            for k, value in flat.items():
                if isinstance(value, (list, dict)):
                    flat[k] = json.dumps(value, ensure_ascii=False, sort_keys=True)
            writer.writerow(flat)
    return out.getvalue()


def population_rows(data, population):
    rows = [r for r in data['entries'] if r['eligible']]
    if population == 'exclude_indecisive':
        return [r for r in rows if not r['indecisive_printed']]
    if population == 'exclude_no_combat':
        return [r for r in rows if not r['no_combat_printed']]
    if population == 'unqualified_totals':
        return [r for r in rows if not any(s['approximate'] or s['footnote_markers'] or s['context_footnote_markers']
                                         for s in r['sides'].values())]
    require(population == 'primary', 'unknown population')
    return rows


def report(data):
    rows = data['entries']; sides = [s for r in rows for s in r['sides'].values()]
    eligible = [r for r in rows if r['eligible']]
    out = ['# Napoleonic compiler-strength benchmark v1: prepared dataset', '',
           'Primary-verified preparation only. No historical outcome fitted or source dispute resolved.', '',
           f'**{len(rows)} development entries / {len(sides)} sides / 13 intact campaign groups**; '
           f'**{len(eligible)}/{len(rows)} eligible compiler-total pairs ({len(eligible)/len(rows):.1%})**.',
           'All 52 final-evaluation entries remain reserved. No separate target column is supplied. '
           'Source columns and quotations reveal outcomes; preparation is not historically blind.', '',
           'Missing extracts are not absent historical headcounts. The table encodes the unchanged frame fields only.', '',
           '## Side dispositions', '', '| Disposition | Sides / 546 | Share |', '| --- | ---: | ---: |']
    for key, n in sorted(Counter(s['disposition'] for s in sides).items()):
        out.append(f'| {key} | {n} | {n/len(sides):.1%} |')
    out += ['', '## Complete-group coverage', '', '| Campaign group | All entries | Eligible pairs | Share |', '| --- | ---: | ---: | ---: |']
    for group in sorted({r['campaign_group'] for r in rows}):
        group_rows = [r for r in rows if r['campaign_group'] == group]
        n = sum(r['eligible'] for r in group_rows)
        out.append(f'| {group} | {len(group_rows)} | {n} | {n/len(group_rows):.1%} |')
    out += ['', '## Fixed sensitivity populations', '', '| Population | Eligible entries / 273 | Groups with rows |', '| --- | ---: | ---: |']
    for pop in fixed_protocol()['populations']:
        selected = population_rows(data, pop)
        out.append(f'| {pop} | {len(selected)} | {len({r["campaign_group"] for r in selected})} |')
    out += ['', 'The indecisive exclusion removes '
            f'{len(eligible) - len(population_rows(data, "exclude_indecisive"))} eligible rows. '
            'If zero, it is a no-op, not evidence that unmarked labels are independent of strength.']
    out += ['', '## Every entry and retained exclusion', '', '| Entry | A compiler total | B compiler total | Eligible pair | Reasons (overlap) |',
            '| --- | ---: | ---: | --- | --- |']
    for r in rows:
        values = [str(r['sides'][s]['primary_value']) if r['sides'][s]['primary_value'] is not None else '—' for s in ('A', 'B')]
        out.append(f'| {r["battle_id"]} | {values[0]} | {values[1]} | {r["eligible"]} | {"; ".join(r["exclusions"]) or "—"} |')
    out += ['', '## Interpretation and run gate', '',
            'These are source-reported entry totals, not selected opening combatants. Unknowns are not zero.',
            'No commander, army, causal contribution, new predictor admission or final-set numerical evaluation is supplied.',
            'Bodart selection, rounding, mixed populations and strength-dependent winner labels remain limitations.',
            'The indecisive sensitivity cannot prove that all other labels are independent of strength.', '',
            '[Design](../docs/napoleonic-benchmark-v1.md), [dataset JSON](napoleonic-benchmark-v1.json), '
            '[side table CSV](napoleonic-benchmark-v1.csv), '
            '[exact run proposal](../data/napoleonic/benchmark-v1/run-proposal.json).',
            'A separate exact owner authorization is required before the historical runner can execute.', '']
    out += ['## Inspected source conventions', '']
    for item in data['source_conventions']:
        cite = item['citation']
        out += [item['interpretation_en'], '', f'> {cite["quote"].replace(chr(10), " ")}', '',
                f'{cite["source_id"]}, {cite["section"]}; raw SHA-256 `{item["raw_sha256"]}`; '
                f'image `{item["facsimile_source_id"]}` SHA-256 `{item["facsimile_sha256"]}`.', '']
    return '\n'.join(out)


def proposal(root, artifact_sha256=None):
    inputs = [SCOPE, PROTOCOL, SNAPSHOT, OWNER, CONTEXT, DESIGN, CODE, RUN_CODE,
              'generalship/baseline.py', 'generalship/napoleonic.py', 'generalship/sources.py',
              'generalship/evidence.py', 'generalship/__init__.py',
              ARTIFACT + '.json', ARTIFACT + '.csv', ARTIFACT + '.md']
    return {'kind': 'napoleonic_compiler_benchmark_run_proposal', 'version': 1,
            'status': 'prepared_awaiting_exact_owner_authorization', 'authorizes_historical_fit': False,
            'bindings': {p: artifact_sha256[p] if artifact_sha256 and p in artifact_sha256 else digest(root / p) for p in inputs},
            'command': 'python3 -m generalship.napoleonic_benchmark_run --authorization '
                       'data/napoleonic/benchmark-v1/owner-run-authorization.json --out artifacts/napoleonic-benchmark-run-v1.json',
            'scope': 'development_only_all_fixed_populations_and_evaluations_no_model_selection',
            'required_authorization': {'kind': 'napoleonic_benchmark_owner_run_authorization', 'approved': True,
                                       'proposal_sha256': 'SHA-256 of this exact proposal file',
                                       'command': 'exact command above', 'scope': 'exact scope above',
                                       'owner_request': 'verbatim later owner authorization; no record created during preparation'}}


def validate_proposal(root):
    actual = read_json(root / PROPOSAL)
    require(actual == proposal(root), 'changed proposal inputs/code; new exact proposal and authorization required')
    return actual


def write_artifacts(root):
    pinned = read_json(root / PROPOSAL) if (root / PROPOSAL).exists() else None
    outputs = [ARTIFACT + suffix for suffix in ('.json', '.csv', '.md')]
    if pinned:
        # Reproduction may restore missing/corrupt generated outputs, but never
        # accept changed inputs/code or silently rebind a released proposal.
        expected_outputs = {p: pinned['bindings'][p] for p in outputs}
        require(pinned == proposal(root, expected_outputs), 'changed preparation inputs/code')
    data = build(root)
    payloads = dict(zip(outputs, [json.dumps(data, indent=2, ensure_ascii=False, allow_nan=False) + '\n',
                                 flat_csv(data), report(data)]))
    if pinned:
        require(all(hashlib.sha256(text.encode('utf-8')).hexdigest() == pinned['bindings'][p]
                    for p, text in payloads.items()), 'regenerated output differs from frozen proposal')
    for path, text in payloads.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text, encoding='utf-8')
    return data


def check(root):
    data = build(root)
    require(data == read_json(root / (ARTIFACT + '.json')), 'dataset does not reproduce')
    require(flat_csv(data) == (root / (ARTIFACT + '.csv')).read_text(), 'CSV does not reproduce')
    require(report(data) == (root / (ARTIFACT + '.md')).read_text(), 'report does not reproduce')
    validate_proposal(root)
    return {'development_entries': len(data['entries']), 'sides': 2 * len(data['entries']),
            'eligible_pairs': sum(r['eligible'] for r in data['entries']), 'historical_outcomes_fitted': False,
            'owner_authorization_created': False}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--write', action='store_true')
    p.add_argument('--freeze-proposal', action='store_true')
    args = p.parse_args()
    if args.write:
        write_artifacts(args.root)
    if args.freeze_proposal:
        require(not (args.root / PROPOSAL).exists(), 'proposal is immutable; do not overwrite v1')
        write_json(args.root / PROPOSAL, proposal(args.root))
    print(json.dumps(check(args.root), indent=2))


if __name__ == '__main__':
    main()
