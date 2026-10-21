"""Explicit, standalone provisional paired-comparison experiment on our Bodart table."""

import argparse
from collections import Counter, defaultdict
import csv
import io
import json
import math
from pathlib import Path
import re
import subprocess
import unicodedata

from .sources import digest, read_json, write_json

TABLE = 'artifacts/bodart-bulk-v1.csv'
META = 'artifacts/bodart-bulk-v1.json'
RESERVATION = 'data/napoleonic/methods-v1/evaluation.json'
DESIGN = 'docs/bodart-ratings-v1.md'
CODE = 'generalship/bodart_ratings.py'
COHORT = 'data/bodart/ratings-v1/cohort.json'
RUN = 'artifacts/bodart-ratings-v1.json'
REPORT = 'artifacts/bodart-ratings-v1.md'
CSV = 'artifacts/bodart-ratings-v1.csv'
TYPES = {'SCHLACHT', 'TREFFEN', 'GEFECHT', 'REITERGEFECHT'}
RANK = re.compile(r'^(?:Gen\. d\. (?:Kav|Inf|Art)\.|Div\.-Gen\.|Gen\.-(?:Lt|Maj|Kpt)\.|'
                  r'Brig\.-Gen\.|Lt\.-Gen\.|D\.-G\.|Genliss\.|Gen\.|FML\.|FZM\.|FM\.|GM\.|'
                  r'Marschall|Feldmarschall)\s+', re.I)
INNER_RANK = re.compile(r'\b' + RANK.pattern[1:], re.I)
PROSE = re.compile(r'\b(?:und|u|unter|seit|sich|wurde|gegen|über|nach|sowie|beide|m|inft|reiter|gesch)\b', re.I)
Z95 = 1.959963984540054


def require(ok, message):
    if not ok:
        raise ValueError('Bodart ratings: ' + message)


def label(raw):
    text = unicodedata.normalize('NFC', raw).strip().strip('.')
    if not text:
        return None, 'missing_command_label'
    if len(text) > 80 or re.search(r'[()\d,;/&]', text) or PROSE.search(text):
        return None, 'joint_or_complex_command_label'
    while RANK.match(text):
        text = RANK.sub('', text, count=1)
    if INNER_RANK.search(text):
        return None, 'joint_or_complex_command_label'
    key = ' '.join(''.join(c if c.isalnum() else ' ' for c in text.casefold()).split())
    if not key or len(key) < 3:
        return None, 'unusable_command_label'
    return key, None


def bindings(root, paths):
    return {p: digest(root / p) for p in paths}


def prepare(root):
    reserved = set(read_json(root / RESERVATION)['reserved_final'])
    with (root / TABLE).open(encoding='utf-8', newline='') as f:
        table = list(csv.DictReader(f))
    require(len({r['id'] for r in table}) == len(table), 'duplicate source row')
    require(reserved <= {r['id'] for r in table}, 'reserved IDs absent from parent table')
    ledger, rows = [], []
    for r in table:
        reasons = []
        # Do not inspect reserved outcomes, strengths or command labels here.
        if r['id'] in reserved:
            ledger.append({'id': r['id'], 'included': False, 'reasons': ['reserved_final']})
            continue
        for field, reason in [('naval', 'naval'), ('indecisive_printed', 'indecisive'),
                              ('no_combat_printed', 'no_combat')]:
            if r[field] == 'True':
                reasons.append(reason)
        if r['type_reading'] not in TYPES:
            reasons.append('outside_single_field_engagement_types')
        year = int(r['year']) if r['year'] else None
        if year is None:
            reasons.append('unknown_year')
        units = {}
        for side in ('winner', 'loser'):
            units[side], reason = label(r[side + '_commander_text'])
            if reason:
                reasons.append(side + ':' + reason)
            value = int(r[side + '_personnel']) if r[side + '_personnel'] else None
            if value is None or value <= 0:
                reasons.append(side + ':missing_positive_personnel')
            flags = r[side + '_strength_flags'].split(';')
            corrected = any(f.startswith('primary_image_reading:') for f in flags)
            if not corrected and any(f not in ('', 'ocr_candidate') for f in flags):
                reasons.append(side + ':ambiguous_personnel_flags')
        if units['winner'] and units['winner'] == units['loser']:
            reasons.append('same_opposing_command_label')
        decision = {'id': r['id'], 'included': not reasons, 'reasons': reasons}
        ledger.append(decision)
        if reasons:
            continue
        a, b = sorted(units.values())
        sa = 'winner' if a == units['winner'] else 'loser'
        sb = 'loser' if sa == 'winner' else 'winner'
        pa, pb = int(r[sa + '_personnel']), int(r[sb + '_personnel'])
        checked = r['record_status'] == 'existing_image_checked_transcription' or all(
            s + '_personnel' in json.loads(r['image_checked_fields'] or '[]') for s in ('winner', 'loser'))
        rows.append({'id': r['id'], 'year': year, 'decade': year // 10 * 10, 'place': r['place'],
                     'a': a, 'b': b, 'a_raw': r[sa + '_commander_text'], 'b_raw': r[sb + '_commander_text'],
                     'personnel_a': pa, 'personnel_b': pb, 'x': math.log(pa / pb), 'y': int(sa == 'winner'),
                     'personnel_checked': checked, 'record_status': r['record_status'],
                     'source_id': r['source_id'], 'source_sha256': r['source_sha256'],
                     'locator': r['locator'], 'scan_url': r['scan_url']})
    years = defaultdict(list)
    for r in rows:
        for u in (r['a'], r['b']):
            years[u].append(r['year'])
    wide = {u for u, yy in years.items() if max(yy) - min(yy) > 60}
    removed = {r['id'] for r in rows if r['a'] in wide or r['b'] in wide}
    for d in ledger:
        if d['id'] in removed:
            d.update(included=False, reasons=['command_label_span_over_60_years'])
    rows = sorted((r for r in rows if r['id'] not in removed), key=lambda r: r['id'])
    return {'kind': 'bodart-ratings-v1-cohort', 'input_sha256': bindings(root, (
                TABLE, META, RESERVATION, DESIGN, CODE, 'tests/test_bodart_ratings.py')),
            'parent_entries': len(table), 'reserved_final': len(reserved), 'rows': rows, 'ledger': ledger,
            'excluded_wide_span_labels': sorted(wide)}


def sigmoid(x):
    if x >= 0:
        return 1 / (1 + math.exp(-x))
    e = math.exp(x)
    return e / (1 + e)


def dot(a, b):
    return math.fsum(x * y for x, y in zip(a, b))


def cg(multiply, rhs, diagonal, tol=1e-11):
    """Preconditioned conjugate gradients for a strictly positive definite Hessian."""
    n = len(rhs)
    x, r = [0.] * n, list(rhs)
    z = [v / d for v, d in zip(r, diagonal)]
    p, rz = list(z), dot(r, z)
    target = tol * max(1., math.sqrt(dot(rhs, rhs)))
    for _ in range(max(20, 4 * n)):
        if math.sqrt(dot(r, r)) <= target:
            return x
        hp = multiply(p)
        alpha = rz / dot(p, hp)
        x = [v + alpha * q for v, q in zip(x, p)]
        r = [v - alpha * q for v, q in zip(r, hp)]
        z = [v / d for v, d in zip(r, diagonal)]
        new = dot(r, z)
        p = [v + new / rz * q for v, q in zip(z, p)]
        rz = new
    raise ValueError('Bodart ratings: conjugate gradients did not converge')


def system(rows, labels, theta_sd):
    index = {u: i + 1 for i, u in enumerate(labels)}
    features = [[(0, r['x'])] + ([(index[r['a']], 1.), (index[r['b']], -1.)] if labels else []) for r in rows]
    precision = [.25] + [1 / theta_sd ** 2] * len(labels)
    return features, precision


def derivatives(rows, features, precision, coef):
    gradient = [p * c for p, c in zip(precision, coef)]
    diagonal = list(precision)
    weights, terms = [], []
    for r, ff in zip(rows, features):
        eta = math.fsum(coef[i] * v for i, v in ff)
        p = sigmoid(eta)
        w = p * (1 - p)
        weights.append(w)
        terms.append(max(eta, 0) + math.log1p(math.exp(-abs(eta))) - r['y'] * eta)
        for i, v in ff:
            gradient[i] += (p - r['y']) * v
            diagonal[i] += w * v * v
    objective = math.fsum(terms) + .5 * math.fsum(p * c * c for p, c in zip(precision, coef))

    def multiply(vector):
        out = [p * v for p, v in zip(precision, vector)]
        for ff, w in zip(features, weights):
            v = w * math.fsum(vector[i] * x for i, x in ff)
            for i, x in ff:
                out[i] += v * x
        return out
    return objective, gradient, diagonal, multiply


def fit(rows, theta_sd=1., commanders=True):
    labels = sorted({r[s] for r in rows for s in ('a', 'b')}) if commanders else []
    ff, precision = system(rows, labels, theta_sd)
    coef = [0.] * len(precision)
    for iteration in range(60):
        obj, grad, diagonal, multiply = derivatives(rows, ff, precision, coef)
        if max(map(abs, grad), default=0) < 1e-8:
            return {'beta': coef[0], 'theta': dict(zip(labels, coef[1:])), 'theta_sd': theta_sd,
                    'max_gradient': max(map(abs, grad), default=0), 'iterations': iteration, 'objective': obj}
        step = cg(multiply, grad, diagonal)
        rate = 1.
        while rate >= 2 ** -24:
            candidate = [c - rate * s for c, s in zip(coef, step)]
            value = derivatives(rows, ff, precision, candidate)[0]
            if value <= obj - 1e-4 * rate * dot(grad, step) + 1e-12:
                coef = candidate
                break
            rate /= 2
        else:
            raise ValueError('Bodart ratings: Newton line search failed')
    raise ValueError('Bodart ratings: fit did not converge')


def predict(model, row):
    t = model['theta']
    return sigmoid(model['beta'] * row['x'] + t.get(row['a'], 0) - t.get(row['b'], 0))


def components(rows):
    graph = defaultdict(set)
    for r in rows:
        graph[r['a']].add(r['b'])
        graph[r['b']].add(r['a'])
    groups, seen = [], set()
    for u in sorted(graph):
        if u in seen:
            continue
        group, todo = set(), [u]
        while todo:
            v = todo.pop()
            if v in group:
                continue
            group.add(v)
            todo.extend(graph[v] - group)
        seen.update(group)
        groups.append(sorted(group))
    groups.sort(key=lambda g: (-len(g), g))
    return {u: i + 1 for i, group in enumerate(groups) for u in group}


def estimates(rows, model, intervals=False):
    counts, names, battles, years, checked = Counter(), defaultdict(set), defaultdict(list), defaultdict(list), Counter()
    wins = Counter()
    for r in rows:
        for side in ('a', 'b'):
            u = r[side]
            counts[u] += 1
            names[u].add(r[side + '_raw'])
            battles[u].append(r['id'])
            years[u].append(r['year'])
            checked[u] += int(r['personnel_checked'])
            wins[u] += r['y'] if side == 'a' else 1 - r['y']
    cc = components(rows)
    out = [{'unit': u, 'raw_labels': sorted(names[u]), 'component': cc[u], 'battles': counts[u],
            'wins': wins[u], 'years': [min(years[u]), max(years[u])], 'checked_personnel_battles': checked[u],
            'theta': model['theta'][u], 'rank': None, 'interval_95': None, 'battle_ids': sorted(battles[u])}
           for u in sorted(counts)]
    ranked = [r for r in out if r['battles'] >= 3]
    for r in ranked:
        r['rank'] = 1 + sum(o['theta'] > r['theta'] for o in ranked if o['component'] == r['component'])
    if intervals:
        labels = sorted(counts)
        ff, precision = system(rows, labels, model['theta_sd'])
        coef = [model['beta']] + [model['theta'][u] for u in labels]
        _, _, diagonal, multiply = derivatives(rows, ff, precision, coef)
        for r in ranked:
            i = labels.index(r['unit']) + 1
            rhs = [0.] * len(coef)
            rhs[i] = 1.
            solution = cg(multiply, rhs, diagonal)
            radius = Z95 * math.sqrt(solution[i])
            r['interval_95'] = [r['theta'] - radius, r['theta'] + radius]
            r['inverse_solve_max_residual'] = max(abs(a - b) for a, b in zip(multiply(solution), rhs))
    return out


def metrics(predictions):
    def calc(rows, key):
        def loss(r):
            p = min(1 - 1e-15, max(1e-15, r[key]))
            return -math.log(p if r['y'] else 1 - p)
        return {'log_loss': math.fsum(loss(r) for r in rows) / len(rows),
                'brier': math.fsum((r[key] - r['y']) ** 2 for r in rows) / len(rows)}
    groups = [[r for r in predictions if r['decade'] == d] for d in sorted({r['decade'] for r in predictions})]
    return {'battle_weighted': {k: calc(predictions, k) for k in ('commander', 'force_only', 'equal_odds')},
            'decade_weighted': {k: {m: math.fsum(calc(g, k)[m] for g in groups) / len(groups)
                                    for m in ('log_loss', 'brier')} for k in ('commander', 'force_only', 'equal_odds')}}


def execute(root, cohort):
    require(not (root / RUN).exists(), 'saved run already exists; do not overwrite')
    status = subprocess.check_output(['git', 'status', '--porcelain'], cwd=root, text=True)
    require(not status, 'commit the specification and implementation before running')
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
    rows = cohort['rows']
    model = fit(rows)
    print(f'Full fit: {len(rows)} battles, {len(model["theta"])} labels', flush=True)
    folds, predictions = [], []
    for decade in sorted({r['decade'] for r in rows}):
        train = [r for r in rows if r['decade'] != decade]
        test = [r for r in rows if r['decade'] == decade]
        joint, force = fit(train), fit(train, commanders=False)
        folds.append({'decade': decade, 'train_ids': [r['id'] for r in train],
                      'test_ids': [r['id'] for r in test], 'commander': joint, 'force_only': force})
        for r in test:
            predictions.append({'id': r['id'], 'decade': decade, 'y': r['y'], 'commander': predict(joint, r),
                                'force_only': predict(force, r), 'equal_odds': .5,
                                'seen_labels': sum(u in joint['theta'] for u in (r['a'], r['b']))})
    sensitivity = {}
    for name, rr, sd in [('prior_sd_0.5', rows, .5), ('prior_sd_2', rows, 2.),
                         ('checked_personnel_only', [r for r in rows if r['personnel_checked']], 1.)]:
        fitted = fit(rr, theta_sd=sd)
        sensitivity[name] = {'rows': len(rr), 'ids': [r['id'] for r in rr], 'model': fitted,
                             'estimates': estimates(rr, fitted)}
    return {'kind': 'bodart-provisional-ratings', 'version': 1, 'status': 'primary_verified_exploratory',
            'prefit_commit': commit, 'input_sha256': {**cohort['input_sha256'], COHORT: digest(root / COHORT)},
            'model': model, 'estimates': estimates(rows, model, intervals=True), 'folds': folds,
            'predictions': sorted(predictions, key=lambda r: r['id']), 'metrics': metrics(predictions),
            'sensitivities': sensitivity}


def verify_model(rows, model):
    labels = sorted(model['theta'])
    require(set(labels) == {r[s] for r in rows for s in ('a', 'b')} or not labels, 'model label population')
    ff, precision = system(rows, labels, model['theta_sd'])
    obj, grad, _, _ = derivatives(rows, ff, precision, [model['beta']] + [model['theta'][u] for u in labels])
    require(max(map(abs, grad), default=0) < 2e-7, 'saved model is not stationary')
    require(math.isclose(obj, model['objective'], abs_tol=1e-9), 'saved objective mismatch')


def verify(root, cohort, run):
    require(run['kind'] == 'bodart-provisional-ratings' and run['version'] == 1, 'run identity')
    require(run['model']['theta_sd'] == 1., 'primary prior changed')
    require(set(run['model']['theta']) == {r[s] for r in cohort['rows'] for s in ('a', 'b')},
            'primary command population')
    require(run['input_sha256'] == {**cohort['input_sha256'], COHORT: digest(root / COHORT)}, 'binding population')
    for path, sha in run['input_sha256'].items():
        require(digest(root / path) == sha, 'changed bound file: ' + path)
    rows = cohort['rows']
    by = {r['id']: r for r in rows}
    require(not (set(by) & set(read_json(root / RESERVATION)['reserved_final'])), 'reserved final entered run')
    verify_model(rows, run['model'])
    require(estimates(rows, run['model']) == [{k: v for k, v in r.items() if k != 'inverse_solve_max_residual'}
                                             | {'interval_95': None} for r in run['estimates']], 'estimate accounting')
    labels = sorted(run['model']['theta'])
    ff, precision = system(rows, labels, run['model']['theta_sd'])
    coef = [run['model']['beta']] + [run['model']['theta'][u] for u in labels]
    _, _, diagonal, multiply = derivatives(rows, ff, precision, coef)
    for e in run['estimates']:
        if e['rank'] is None:
            require(e['interval_95'] is None, 'unranked interval policy')
            continue
        i = labels.index(e['unit']) + 1
        rhs = [0.] * len(coef)
        rhs[i] = 1.
        sol = cg(multiply, rhs, diagonal)
        radius = Z95 * math.sqrt(sol[i])
        require(all(math.isclose(a, b, abs_tol=1e-9) for a, b in zip(e['interval_95'],
                    [e['theta'] - radius, e['theta'] + radius])), 'marginal interval mismatch')
        require(e['inverse_solve_max_residual'] < 1e-8, 'inverse solve residual')
    predictions, heldout = [], []
    for fold in run['folds']:
        decade = fold['decade']
        train = [r for r in rows if r['decade'] != decade]
        test = [r for r in rows if r['decade'] == decade]
        require(fold['train_ids'] == [r['id'] for r in train] and fold['test_ids'] == [r['id'] for r in test],
                'fold membership mismatch')
        require(set(fold['commander']['theta']) == {r[s] for r in train for s in ('a', 'b')},
                'fold command population')
        require(not fold['force_only']['theta'], 'force-only contains command coefficients')
        require(all(fold[k]['theta_sd'] == 1. for k in ('commander', 'force_only')), 'fold prior changed')
        for key in ('commander', 'force_only'):
            verify_model(train, fold[key])
        for r in test:
            heldout.append(r['id'])
            predictions.append({'id': r['id'], 'decade': decade, 'y': r['y'],
                                'commander': predict(fold['commander'], r),
                                'force_only': predict(fold['force_only'], r), 'equal_odds': .5,
                                'seen_labels': sum(u in fold['commander']['theta'] for u in (r['a'], r['b']))})
    require(sorted(heldout) == sorted(by), 'held-out rows missing or duplicated')
    require(sorted(predictions, key=lambda r: r['id']) == run['predictions'], 'predictions differ')
    require(metrics(predictions) == run['metrics'], 'metrics differ')
    for name, sd in [('prior_sd_0.5', .5), ('prior_sd_2', 2.), ('checked_personnel_only', 1.)]:
        rr = rows if name != 'checked_personnel_only' else [r for r in rows if r['personnel_checked']]
        s = run['sensitivities'][name]
        require(s['ids'] == [r['id'] for r in rr] and s['rows'] == len(rr), 'sensitivity population')
        require(s['model']['theta_sd'] == sd, 'sensitivity prior')
        require(set(s['model']['theta']) == {r[x] for r in rr for x in ('a', 'b')}, 'sensitivity command population')
        verify_model(rr, s['model'])
        require(estimates(rr, s['model']) == s['estimates'], 'sensitivity accounting')


def csv_text(run):
    fields = ['unit', 'component', 'rank', 'battles', 'wins', 'years', 'checked_personnel_battles',
              'theta', 'interval_95', 'raw_labels', 'battle_ids']
    f = io.StringIO(newline='')
    writer = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    for r in sorted(run['estimates'], key=lambda e: (e['component'], e['rank'] or 10 ** 9, e['unit'])):
        writer.writerow({k: json.dumps(r[k], ensure_ascii=False) if isinstance(r[k], list) else r[k] for k in fields})
    return f.getvalue()


def report(cohort, run):
    rows, ee, mm = cohort['rows'], run['estimates'], run['metrics']
    ordered = [e for e in ee if e['rank'] is not None]
    source_counts = Counter(r['record_status'] for r in rows)
    lines = ['# Bodart: broader provisional command-label ratings', '',
             f'**{len(rows)} field engagements · {len(ee)} command labels · {len(ordered)} ordered labels.** '
             'A first exploratory ranking from our own source table and model. '
             'Primary-verified; printed labels are not resolved historical identities.', '',
             '[Download estimates](bodart-ratings-v1.csv) · [Saved run, folds and sensitivities](bodart-ratings-v1.json) · '
             '[Every inclusion/exclusion](../data/bodart/ratings-v1/cohort.json) · '
             '[Fixed design](../docs/bodart-ratings-v1.md) · [Source table](bodart-bulk-v1.csv)', '',
             '## Does command information help held-out prediction?', '',
             'Each calendar decade is excluded from training in turn. Lower scores are better. '
             'This is a development diagnostic, not a final or forward test; campaigns can cross decade boundaries.', '',
             '| Model | Battle log loss | Equal-decade log loss | Battle Brier | Equal-decade Brier |',
             '| --- | ---: | ---: | ---: | ---: |']
    for key, title in [('equal_odds', 'Equal odds'), ('force_only', 'Force only'), ('commander', 'Force + command labels')]:
        b, d = mm['battle_weighted'][key], mm['decade_weighted'][key]
        lines.append(f'| {title} | {b["log_loss"]:.6f} | {d["log_loss"]:.6f} | {b["brier"]:.6f} | {d["brier"]:.6f} |')
    delta = {w: mm[w]['commander']['log_loss'] - mm[w]['force_only']['log_loss'] for w in mm}
    seen = Counter(p['seen_labels'] for p in run['predictions'])
    lines += ['', f'Command-label minus force-only log loss: **{delta["battle_weighted"]:+.6f} per battle**, '
              f'**{delta["decade_weighted"]:+.6f} per decade**. '
              'These point differences do not establish correct skill rankings or isolate AI’s benefit. '
              'No uncertainty-adjusted claim of predictive superiority is made.', '',
              f'Held-out label availability: both previously seen {seen[2]}/{len(rows)}, '
              f'one seen {seen[1]}/{len(rows)}, neither seen {seen[0]}/{len(rows)}. '
              'Unseen labels receive prior mean zero, not an invented career rating.', '',
              '## Provisional orders', '',
              'Orders compare only labels within the same connected opponent component and require three '
              'included engagements. θ is the shrunk conditional log-odds association. The 95% intervals '
              'are approximate marginal Laplace intervals conditional on this model and its inputs; '
              'they do not include OCR, identity, source, army or campaign uncertainty. '
              'Adjacent orders with overlapping intervals should not be read as settled differences. '
              'No cross-component or causal wins-above-replacement ranking is supplied.', '']
    sensitivity = {k: {e['unit']: e for e in s['estimates']} for k, s in run['sensitivities'].items()}
    for component in sorted({e['component'] for e in ordered}):
        group = sorted((e for e in ordered if e['component'] == component), key=lambda e: (e['rank'], e['unit']))
        n = sum(e['component'] == component for e in ee)
        lines += [f'### Opponent component {component}', '', f'{len(group)} ordered labels out of {n} estimated labels.', '',
                  '| Order | Normalized printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior sensitivity orders |',
                  '| ---: | --- | --- | ---: | ---: | --- | --- |']
        for e in group:
            lo, hi = e['interval_95']
            prior = [sensitivity[k][e['unit']]['rank'] for k in ('prior_sd_0.5', 'prior_sd_2')]
            lines.append(f'| {e["rank"]} | {e["unit"]} | {e["years"][0]}–{e["years"][1]} | '
                         f'{e["battles"]} ({e["wins"]}) | {e["checked_personnel_battles"]} | '
                         f'{e["theta"]:+.3f} ({lo:+.3f}, {hi:+.3f}) | {prior[0]} / {prior[1]} |')
    c = run['sensitivities']['checked_personnel_only']
    lines += ['', '## Coverage and fixed sensitivities', '',
              f'The parent table has {cohort["parent_entries"]} entries; {len(rows)} enter this experiment and '
              f'{cohort["parent_entries"] - len(rows)} do not. All {cohort["reserved_final"]} reserved-final entries '
              'are excluded before numerical use. Exclusion reasons overlap:', '', '| Reason | Entries |', '| --- | ---: |']
    counts = Counter(reason for d in cohort['ledger'] for reason in d['reasons'])
    lines += [f'| {k} | {v} |' for k, v in sorted(counts.items())]
    lines += ['', 'Included source status:', '', '| Status | Entries |', '| --- | ---: |']
    lines += [f'| {k} | {v} |' for k, v in sorted(source_counts.items())]
    lines += ['', f'There are {len(set(e["component"] for e in ee))} disconnected opponent components; '
              f'{len(ee) - len(ordered)} labels have fewer than three appearances and receive no order. '
              'Rank removal normalizes titles, not biographical aliases or every spelling error. '
              'Bonaparte and Napoleon I can remain separate; homonyms can remain. No label is verified by reputation.', '',
              'Unchecked OCR years can place a record in the wrong evaluation decade. Embedded rank text is '
              'excluded conservatively, including some valid single names with nationality prefixes. '
              'Only the listed fields of sampled images were checked; other OCR readings remain candidates.', '',
              'The prior columns use fixed θ prior SD 0.5 / 2 on the same rows (primary SD 1). '
              'They are sensitivity orders, not confidence bounds. '
              f'The personnel-checked subset has **{c["rows"]}/{len(rows)} engagements**, '
              f'**{len(c["model"]["theta"])} labels** and '
              f'**{sum(e["rank"] is not None for e in c["estimates"])} ordered labels**. '
              'It is a different cohort, not an equal-coverage accuracy comparison; scoped personnel '
              'checks do not verify the OCR command names. Full subset estimates remain in the saved JSON.', '',
              '## What was fitted and verified', '',
              '`logit(p_A) = beta * log(personnel_A/personnel_B) + theta_A - theta_B`, with labels sorted '
              'before assigning the outcome. No intercept, no winner-first orientation, no imported ratings. '
              'Gaussian priors: beta SD 2, theta SD 1. '
              f'Estimated beta = {run["model"]["beta"]:.6f}; maximum penalized gradient = '
              f'{run["model"]["max_gradient"]:.2g}. '
              'A force coefficient is an association in a selected historical compilation; force advantages '
              'may be commander-created mediators. Army quality, appointment selection and source bias '
              'can drive apparent command effects.', '',
              f'Protocol/code/cohort were committed before fitting at `{run["prefit_commit"]}`. '
              'The saved run binds their SHA-256 hashes. Verification checks every fold membership and saved '
              'prediction, selection denominator, penalized gradient, marginal inverse-Hessian solve and '
              'reported metric without refitting historical outcomes. Toy tests check the numerical methods. '
              'The source table retains quoted passages, locators, raw readings and source/image hashes. '
              'No original frozen model or final evaluation set changes.', '',
              '`python3 -m generalship.bodart_ratings --write` regenerates this page and CSV from the saved '
              'run. The default verifies them. `make reproduce` does not run the historical fitting job.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument('--prepare', action='store_true')
    action.add_argument('--run', action='store_true')
    action.add_argument('--write', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    cohort = prepare(root)
    if args.prepare:
        if (root / RUN).exists():
            require(read_json(root / COHORT) == cohort, 'cannot revise a fitted cohort in place')
        (root / COHORT).parent.mkdir(parents=True, exist_ok=True)
        write_json(root / COHORT, cohort)
        print(f'Prepared {len(cohort["rows"])}/{cohort["parent_entries"]} rows; no fit.')
        return
    require(read_json(root / COHORT) == cohort, 'prepared cohort differs')
    if args.run:
        write_json(root / RUN, execute(root, cohort))
    run = read_json(root / RUN)
    verify(root, cohort, run)
    md, csv_data = report(cohort, run), csv_text(run)
    if args.write or args.run:
        (root / REPORT).write_text(md, encoding='utf-8')
        (root / CSV).write_text(csv_data, encoding='utf-8')
    else:
        require((root / REPORT).read_text(encoding='utf-8') == md, 'report differs')
        require((root / CSV).read_text(encoding='utf-8') == csv_data, 'CSV differs')
    print(f'Bodart ratings: {len(cohort["rows"])} rows; saved results primary-verified.')


if __name__ == '__main__':
    main()
