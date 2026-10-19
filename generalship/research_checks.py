"""Reproducible research triage and an unscored, frozen calibration sample."""

from collections import Counter, defaultdict
import json
import random
import re
from pathlib import Path

from .evidence import citation_text
from .sources import digest, read_json

BASE = 'data/napoleonic/methods-v1'
POPULATION = BASE + '/calibration-population.json'
CONVENTIONS = BASE + '/research-conventions.json'
DIGITS = re.compile(r'(?<!\w)\d+(?:[,. \u00a0\u202f]\d{3})*(?!\w)')


def bound_dossier(root, path, sha256):
    """Replay a calibration/pilot binding; revisions must preserve the old bytes in history."""
    root = Path(root)
    target = root / path
    if target.is_file() and digest(target) == sha256:
        return read_json(target)
    folder = target.parent / 'history'
    for archived in sorted(folder.glob(target.stem + '*.json')) if folder.is_dir() else []:
        if digest(archived) == sha256:
            return read_json(archived)
    raise ValueError(f'Bound research dossier is not reachable: {path}; archive its original bytes before revision')


def numbers(text):
    return {re.sub(r'\D', '', n).lstrip('0') or '0' for n in DIGITS.findall(text)}


def completion(dossier, sources):
    """Version-3 first-pass checklist; claim references do not establish their historical meaning."""
    record = dossier.get('research_completion')
    if not isinstance(record, dict) or record.get('brief_version') != 3:
        raise ValueError(f"{dossier['battle_id']}: a new first pass requires the brief-v3 completion record")
    claims = {c['id']: c for c in dossier['claims']}
    if set(record.get('sides', {})) != {'A', 'B'}:
        raise ValueError('Completion record requires both sides')
    for side in record['sides'].values():
        for key, dimension in (('strength_claim_ids', 'strength'), ('command_claim_ids', 'responsibility')):
            refs = side.get(key)
            if not isinstance(refs, list) or not refs or any(r not in claims or claims[r]['dimension'] != dimension for r in refs):
                raise ValueError(f'Completion record has missing or invalid {key}')
        for key in ('strength_population_and_time', 'command_scope', 'army_continuity'):
            if not isinstance(side.get(key), str) or not side[key].strip():
                raise ValueError(f'Completion record requires {key}, including an explicit unknown when needed')
    checked = record.get('additional_source_ids_checked')
    if not isinstance(checked, list) or any(s not in sources for s in checked):
        raise ValueError('Completion record must index additional inspected sources; cited sources are included automatically')
    follow = record.get('targeted_follow_up')
    if not isinstance(follow, dict) or not isinstance(follow.get('performed'), bool):
        raise ValueError('Completion record requires one explicit follow-up disposition')
    if follow['performed'] and not all(isinstance(follow.get(k), str) and follow[k].strip()
                                       for k in ('decision_it_could_change', 'result')):
        raise ValueError('A follow-up requires its decision and result')
    if not isinstance(record.get('stopping_reason'), str) or not record['stopping_reason'].strip():
        raise ValueError('Completion record requires a stopping reason')
    if not isinstance(record.get('deferred_decision_relevant_gaps'), list):
        raise ValueError('Completion record requires a deferred-gap list')
    return record


def screen(root):
    """Flags are navigation aids, never automated judgments of historical entailment."""
    root = Path(root)
    sources = {s['id']: s for s in read_json(root / 'data/sources.json')['sources']}
    aliases = read_json(root / CONVENTIONS)['family_aliases']
    legacy = {Path(b['path']).stem for b in read_json(root / POPULATION)['dossiers']}
    texts = {}
    rows = []
    for path in sorted((root / 'data/napoleonic/evidence').glob('*.json')):
        d = read_json(path)
        record = completion(d, sources) if d['battle_id'] not in legacy or 'research_completion' in d else None
        issues, families, cited = [], set(), set()
        for c in d['claims']:
            image_numbers = set()
            for citation in c['citations']:
                source = sources[citation['source_id']]
                cited.add(source['id'])
                families.add(aliases.get(source['independence_group'], source['independence_group']))
                cache_key = (source['id'], citation.get('section'))
                if cache_key not in texts:
                    texts[cache_key] = citation_text(root, sources, citation)
                if citation['quote'] not in texts[cache_key]:
                    issues.append({'claim_id': c['id'], 'kind': 'quote_missing', 'source_id': source['id']})
                if source.get('facsimile_source_id') or source['id'] == 'bodart-1908-transcription-v1':
                    image_numbers |= numbers(citation['quote'])
                sec = citation.get('section', '')
                page = re.fullmatch(r'p0*(\d+)', sec)
                pages = re.search(r'\bpp?\.\s*(\d+)(?:[–-](\d+))?', citation.get('locator', ''))
                if page and pages:
                    lo, hi = int(pages[1]), int(pages[2] or pages[1])
                    if not lo <= int(page[1]) <= hi:
                        issues.append({'claim_id': c['id'], 'kind': 'locator_page_mismatch',
                                       'source_id': source['id'], 'section': sec, 'locator': citation['locator']})
            unsupported = sorted(numbers(str(c['value'])) - image_numbers)
            if unsupported:
                issues.append({'claim_id': c['id'], 'kind': 'value_digits_without_same_claim_image_quote',
                               'digits': unsupported, 'dimension': c['dimension']})
        if record:
            for source_id in record['additional_source_ids_checked']:
                source = sources[source_id]
                families.add(aliases.get(source['independence_group'], source['independence_group']))
        if len(families) > 3:
            if record is not None:
                raise ValueError(f"{d['battle_id']}: new first pass exceeds the three-family ceiling")
            issues.append({'kind': 'source_family_ceiling', 'families': sorted(families)})
        rows.append({'battle_id': d['battle_id'], 'dossier_sha256': digest(path), 'claims': len(d['claims']),
                     'citations': sum(len(c['citations']) for c in d['claims']),
                     'source_families': sorted(families), 'source_ids': sorted(cited),
                     'completion_brief_version': 3 if record else None, 'flags': issues})
    counts = Counter(f['kind'] for row in rows for f in row['flags'])
    return {'kind': 'napoleonic_research_screen', 'version': 1, 'drafts': len(rows),
            'flag_counts': dict(sorted(counts.items())), 'dossiers': rows,
            'meaning': 'Screening flags require primary inspection. Shared digits do not prove entailment; arithmetic, '
                       'spelled-out numbers, OCR context and source dependence need judgment. Earlier drafts are not '
                       'silently migrated to a stricter brief. No historical error rate is estimated.'}


def stratum(claim):
    if claim['status'] == 'unknown':
        return 'unknown'
    if claim['dimension'] in ('strength', 'responsibility'):
        return claim['dimension']
    if claim['dimension'] in ('posture', 'fortification'):
        return 'coding'
    return 'other_known'


def calibration(root, protocol):
    root = Path(root)
    population = read_json(root / POPULATION)
    sources = {s['id']: s for s in read_json(root / 'data/sources.json')['sources']}
    texts = {}
    by_stratum, documents = defaultdict(list), {}
    for binding in population['dossiers']:
        dossier = bound_dossier(root, binding['path'], binding['sha256'])
        documents[dossier['battle_id']] = (dossier, binding)
        for c in dossier['claims']:
            by_stratum[stratum(c)].append((dossier['battle_id'], c['id']))
    rng = random.Random(protocol['seed'])
    selected, denominators = [], {}
    for name in sorted(by_stratum):
        values = sorted(by_stratum[name])
        n = len(values) if name == 'unknown' else min(len(values), protocol['known_sample_per_stratum'])
        selected += [(name, *x) for x in sorted(rng.sample(values, n))]
        denominators[name] = {'population': len(values), 'sample': n}
    # Opaque IDs are shuffled independently of the row order; the key is kept in a separate artifact.
    rng.shuffle(selected)
    tasks, key, translations = [], [], []
    for i, (name, battle, claim_id) in enumerate(selected, 1):
        dossier, binding = documents[battle]
        claim = next(c for c in dossier['claims'] if c['id'] == claim_id)
        token = f'C{i:03d}'
        contexts = []
        for j, citation in enumerate(claim['citations']):
            source = sources[citation['source_id']]
            cache_key = (source['id'], citation.get('section'))
            if cache_key not in texts:
                texts[cache_key] = citation_text(root, sources, citation)
            text = texts[cache_key]
            at = text.index(citation['quote'])
            contexts.append({'source_id': source['id'], 'source_sha256': source['sha256'],
                             'section': citation.get('section'), 'locator': citation.get('locator'),
                             'original_quote': citation['quote'],
                             'context': text[max(0, at - 350):at + len(citation['quote']) + 350]})
            translations.append((token, j))
        # Unknowns have no supporting citation: supply a bounded index of the sections already read,
        # rather than inventing a passage or accepting the author's assertion of silence.
        search = sorted({(x['source_id'], x.get('section'), x.get('locator'))
                         for c in dossier['claims'] for x in c['citations']}) if name == 'unknown' else []
        tasks.append({'sample_id': token, 'stratum': name, 'dimension': claim['dimension'],
                      'source_contexts': contexts, 'unknown_search_sections': [
                          {'source_id': s, 'section': sec, 'locator': loc,
                           'source_sha256': sources[s]['sha256']} for s, sec, loc in search],
                      'first_reading': {'extracted_observation': None, 'english_rendering': None,
                                        'unknown_search_record': None},
                      'judgment': {'verdict': None, 'quote_supports_claim': None, 'attribution': None,
                                   'scope_and_time': None, 'status': None, 'note': None}})
        key.append({'sample_id': token, 'battle_id': battle, 'claim_id': claim_id,
                    'dossier': binding, 'claim_value': claim['value'], 'status': claim['status'],
                    'author_rationale': claim['rationale']})
    translation_sample = sorted(random.Random(protocol['seed'] + 1).sample(
        sorted(translations), min(protocol['translation_sample_size'], len(translations))))
    sample = {'kind': 'calibration_sample', 'version': 1, 'status': 'prepared_unscored',
              'seed': protocol['seed'], 'strata': denominators, 'tasks': tasks,
              'translation_subsample': [{'sample_id': t, 'citation_index': i} for t, i in translation_sample],
              'reviewer': None, 'independent_review_performed': False,
              'limits': 'First reading excludes claim values, author rationales and supplied English renderings. '
                        'The separate key is public, so procedural blinding requires not opening it first. '
                        'Stratified/all-unknown sampling does not support an unweighted corpus error rate. '
                        'There is no reviewer or completed judgment; unknown searches cover the inspected sections only.'}
    return sample, {'kind': 'calibration_key', 'version': 1, 'entries': key}


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + '\n', encoding='utf-8')


def write_artifacts(root, protocol):
    root = Path(root)
    sample, key = calibration(root, protocol)
    outputs = {'artifacts/napoleonic-research-screen.json': screen(root),
               'artifacts/napoleonic-calibration-v1.json': sample,
               'artifacts/napoleonic-calibration-key-v1.json': key}
    for path, value in outputs.items():
        write_json(root / path, value)
    return outputs


def check_artifacts(root, protocol):
    root = Path(root)
    sample, key = calibration(root, protocol)
    expected = {'artifacts/napoleonic-research-screen.json': screen(root),
                'artifacts/napoleonic-calibration-v1.json': sample,
                'artifacts/napoleonic-calibration-key-v1.json': key}
    for path, value in expected.items():
        if read_json(root / path) != value:
            raise ValueError(f'Stale research preparation artifact: {path}; run make reproduce')
    return list(expected)
