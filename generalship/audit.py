"""Review-record index and the extraction audit (docs/extraction-audit.md).

The index normalizes every historical review record into one controlled disposition vocabulary
so that outcomes can be counted. The audit draws a seeded random sample of cited dossier claims,
records a verdict for each against its inspected passages, and estimates the share of claims
still wrong after review. Nothing here changes a dossier, ledger or model input.
"""

from collections import Counter, defaultdict
import math
from pathlib import Path
import random

from .evidence import citation_text
from .sources import digest, read_json, safe_path

REVIEWS = 'artifacts/review-results'
AUDIT = 'data/audit/extraction-audit-v1.json'
# Every disposition string used in the historical records, mapped to the controlled vocabulary.
DISPOSITIONS = {
    'accepted_applied': 'applied', 'accepted_and_applied_exactly': 'applied',
    'accepted_and_corrected_by_primary': 'applied', 'accepted_verified_and_staged': 'applied',
    'accepted_verified_and_staged_with_wording_change': 'applied', 'adopted': 'applied',
    'recommendation_adopted_by_primary': 'applied',
    'partly_adopted': 'partly_applied',
    'found_and_corrected_by_primary': 'primary_found_applied', 'primary_found_and_corrected': 'primary_found_applied',
    'not_adopted': 'not_applied', 'kept_as_is': 'not_applied', 'kept_or_recorded': 'not_applied',
    'no_change': 'not_applied', 'no_dossier_change': 'not_applied',
    'deferred': 'deferred',
    'primary_decision': 'decided_by_primary',
}
VOCABULARY = ('applied', 'partly_applied', 'primary_found_applied', 'not_applied', 'deferred', 'decided_by_primary')
VERDICTS = ('correct', 'minor', 'material')
CHECKS = ('quote_supports_claim', 'attribution', 'scope_and_time', 'status')
CHECK_VALUES = ('yes', 'partly', 'no', 'not_applicable')
SAMPLE_SIZE = 150
SEED = 20261006
Z95 = 1.959963984540054


class AuditError(ValueError):
    pass


# ---------- review index ----------

def findings(record):
    """The findings of a correction record in either historical shape."""
    if 'findings' in record:
        return record['findings']
    if 'finding_id' in record:
        return [record]
    raise AuditError('Unrecognized correction record shape')


def review_index(root):
    root = Path(root)
    reviews = []
    folder = root / REVIEWS
    for d in sorted(p for p in folder.iterdir() if p.is_dir()) if folder.is_dir() else []:
        dispatch = read_json(d / 'dispatch.json') if (d / 'dispatch.json').is_file() else {}
        model = dispatch.get('model') or ('gpt-6-astra' if 'astra' in d.name else 'claude-opus-5-5' if 'opus' in d.name else None)
        entry = {'id': d.name, 'reviewer_model': model, 'effort': dispatch.get('reasoning_effort'),
                 'dispatched_at': dispatch.get('dispatched_at_utc'), 'has_review': (d / 'review.md').is_file()}
        corr = d / 'correction.json'
        if corr.is_file():
            raw = [f.get('disposition') for f in findings(read_json(corr))]
            unknown = sorted({x for x in raw if x not in DISPOSITIONS})
            if unknown:
                raise AuditError(f'{d.name}: disposition outside the controlled vocabulary: {unknown}')
            entry['findings'] = len(raw)
            entry['dispositions'] = dict(sorted(Counter(DISPOSITIONS[x] for x in raw).items()))
        reviews.append(entry)
    totals = Counter()
    by_model = defaultdict(Counter)
    for r in reviews:
        for k, v in r.get('dispositions', {}).items():
            totals[k] += v
            by_model[r['reviewer_model']][k] += v
    return {'kind': 'review_index', 'version': 1, 'vocabulary': list(VOCABULARY), 'mapping': DISPOSITIONS,
            'reviews': reviews, 'totals': dict(sorted(totals.items())),
            'by_reviewer_model': {m: dict(sorted(c.items())) for m, c in sorted(by_model.items(), key=lambda kv: str(kv[0]))},
            'note': 'Historical separate-review records, normalized. Counts include design, ledger and run reviews as well '
                    'as dossier reviews; a finding may be advisory. Since 2026-10-06 the primary verifies its own work.'}


# ---------- extraction audit ----------

def cited_claims(root):
    """Every supported or disputed claim with citations, in a fixed order."""
    out = []
    for path in sorted((Path(root) / 'data/evidence').glob('*.json')):
        d = read_json(path)
        for c in d['claims']:
            if c['status'] in {'supported', 'disputed'} and c['citations']:
                out.append({'battle_id': d['battle_id'], 'claim_id': c['id'], 'dimension': c['dimension'],
                            'status': c['status'], 'dossier': f'data/evidence/{path.name}'})
    return out


def draw_sample(root, n=SAMPLE_SIZE, seed=SEED):
    population = cited_claims(root)
    picked = sorted(random.Random(seed).sample(range(len(population)), n))
    return population, [population[i] for i in picked]


def context(root, sources, citation, width=450):
    """The cited passage with surrounding text, for reading a sampled claim against its source."""
    text = citation_text(root, sources, citation)
    q = citation['quote']
    i = text.find(q)
    if i < 0:
        return None
    a, b = max(0, i - width), min(len(text), i + len(q) + width)
    return ('…' if a else '') + text[a:i] + '⟦' + q + '⟧' + text[i + len(q):b] + ('…' if b < len(text) else '')


def wilson(k, n, z=Z95):
    if n == 0:
        return None
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return [0.0 if k == 0 else max(0.0, centre - half), 1.0 if k == n else min(1.0, centre + half)]


def check_audit(root, audit=None):
    """Validate the frozen sample and the recorded verdicts, then score them."""
    root = Path(root)
    audit = audit or read_json(safe_path(root, AUDIT))
    population, sample = draw_sample(root, audit['sample_size'], audit['seed'])
    if audit['population'] != len(population):
        raise AuditError('Population size differs from the frozen sample')
    keys = [(s['battle_id'], s['claim_id']) for s in sample]
    if [(j['battle_id'], j['claim_id']) for j in audit['judgments']] != keys:
        raise AuditError('Judgments do not match the seeded sample')
    for j in audit['judgments']:
        b = j['dossier_sha256']
        live = digest(safe_path(root, f"data/evidence/{j['battle_id']}.json"))
        if b != live and not any(h.get('sha256') == b for h in _history(root, j['battle_id'])):
            raise AuditError(f"{j['battle_id']}: audited dossier version not found")
        if j['verdict'] not in VERDICTS or set(j['checks']) != set(CHECKS) or not set(j['checks'].values()) <= set(CHECK_VALUES):
            raise AuditError(f"{j['battle_id']} {j['claim_id']}: verdict or checks outside the vocabulary")
        if j['verdict'] != 'correct' and not j.get('note'):
            raise AuditError(f"{j['battle_id']} {j['claim_id']}: a minor or material verdict needs a note")
    return score(audit)


def _history(root, battle):
    out = []
    for p in sorted((Path(root) / 'data/evidence/history').glob(f'{battle}.v*.json')):
        out.append({'path': str(p.relative_to(root)), 'sha256': digest(p)})
    return out


def score(audit):
    js = audit['judgments']
    n = len(js)
    counts = Counter(j['verdict'] for j in js)
    by_dim = defaultdict(Counter)
    for j in js:
        by_dim[j['dimension']][j['verdict']] += 1
    material, any_issue = counts['material'], counts['material'] + counts['minor']
    return {'kind': 'extraction_audit_score', 'audited': n, 'population': audit['population'],
            'verdicts': {v: counts[v] for v in VERDICTS},
            'material_error_rate': material / n, 'material_error_rate_95': wilson(material, n),
            'any_issue_rate': any_issue / n, 'any_issue_rate_95': wilson(any_issue, n),
            'by_dimension': {d: {v: c[v] for v in VERDICTS} for d, c in sorted(by_dim.items())},
            'auditor': audit['auditor'], 'independence': audit['independence']}


def report_text(audit, s):
    pct = lambda x: f'{100 * x:.1f}%'
    ci = lambda x: f'{pct(x[0])}–{pct(x[1])}'
    lines = ['# Extraction audit v1', '',
             f"A seeded random sample of {s['audited']} of the {s['population']} cited dossier claims (seed {audit['seed']}), "
             f"each read against its cited passages. Auditor: {audit['auditor']}. {audit['independence']}", '',
             '| Verdict | Claims |', '|---|---:|'] + [f"| {v} | {s['verdicts'][v]} |" for v in VERDICTS] + [
             '', f"- Material errors: {pct(s['material_error_rate'])} (Wilson 95% interval {ci(s['material_error_rate_95'])}).",
             f"- Any issue, material or minor: {pct(s['any_issue_rate'])} ({ci(s['any_issue_rate_95'])}).", '',
             '| Dimension | Correct | Minor | Material |', '|---|---:|---:|---:|']
    lines += [f"| {d} | {c['correct']} | {c['minor']} | {c['material']} |" for d, c in s['by_dimension'].items()]
    lines += ['', '## Claims with issues', '']
    for j in audit['judgments']:
        if j['verdict'] != 'correct':
            lines.append(f"- **{j['battle_id']} `{j['claim_id']}`** ({j['dimension']}, {j['verdict']}): {j['note']}"
                         + (f" Correction: {j['correction']}" if j.get('correction') else ''))
    lines += ['', '## Protocol and limits', ''] + [f'- {x}' for x in audit['protocol']] + [''] + [f'- {x}' for x in audit['limits']] + ['']
    return '\n'.join(lines)
