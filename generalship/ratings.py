"""Commander residual ratings (docs/commander-ratings.md §§3–7): partially pooled, gated.

A residual rating summarises how a commander's battles went relative to what force size
predicts. It is not command skill, a causal effect or replacement value. The run is refused
unless an owner authorization names the reviewed ledgers' hashes; outputs never enter
artifacts/baseline.json.
"""

from collections import Counter, defaultdict
from itertools import product
import math
import random

from .baseline import advantage, fit_logistic, scores, sigmoid
from .command import DEFAULT_LEDGER as COMMAND_LEDGER, DEFAULT_REGISTRY, check as check_command
from .dataset import build_dataset
from .estimates import DEFAULT_LEDGER as STRENGTH_LEDGER, SIDES, check as check_estimates, nested_sets
from .estimates_v2 import DEFAULT_LEDGER as STRENGTH_LEDGER_V2, check as check_estimates_v2
from .sources import digest, read_json, safe_path

DEFAULT_AUTHORIZATION = 'data/command/rating-authorization-v1.json'
# Each run binds its own authorization, ledgers, cohort and evaluation; v1 stays exactly as first run.
# The temporal split is descriptive only (design §5): v1 trains on 1862 and tests 1863; v2 trains on
# 1861-1863 and tests 1864-1865.
RUNS = {1: {'authorization': DEFAULT_AUTHORIZATION, 'strength': STRENGTH_LEDGER, 'command': COMMAND_LEDGER,
            'registry': DEFAULT_REGISTRY, 'check_strength': check_estimates, 'cohort': 'data/pilot/cohort.json',
            'evaluation': 'artifacts/estimate-evaluation.json', 'temporal': (('1862',), ('1863',)),
            'views': ('outcome_only_37', 'outcome_only_91'), 'output': 'artifacts/commander-ratings'},
        2: {'authorization': 'data/command/rating-authorization-v2.json', 'strength': STRENGTH_LEDGER_V2,
            'command': 'data/command/responsibility-v2.json', 'registry': 'data/command/commanders-v2.json',
            'check_strength': check_estimates_v2, 'cohort': 'data/pilot/cohort-v2.json',
            'evaluation': 'artifacts/estimate-evaluation-v2.json', 'temporal': (('1861', '1862', '1863'), ('1864', '1865')),
            'views': ('outcome_only_primary', 'outcome_only_all'), 'output': 'artifacts/commander-ratings-v2'}}
TAU = 0.5
DRAWS = 20000
SEED = 20260925
Z80, Z95 = 1.2815515655446004, 1.959963984540054
FLAGS = ['whole_engagement_leakage', 'conditional_on_source_availability', 'not_causal', 'side_relative']


class RatingError(ValueError):
    """Refused or malformed rating run."""


# ---------- linear algebra (standard library) ----------

def cholesky(a):
    n = len(a)
    low = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = a[i][j] - sum(low[i][k] * low[j][k] for k in range(j))
            if i == j:
                if s <= 0:
                    raise RatingError('Hessian is not positive definite')
                low[i][i] = math.sqrt(s)
            else:
                low[i][j] = s / low[j][j]
    return low


def chol_solve(low, b):
    n = len(b)
    y = [0.0] * n
    for i in range(n):
        y[i] = (b[i] - sum(low[i][k] * y[k] for k in range(i))) / low[i][i]
    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(low[k][i] * x[k] for k in range(i + 1, n))) / low[i][i]
    return x


def chol_inverse(low):
    n = len(low)
    cols = [chol_solve(low, [1.0 if i == j else 0.0 for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


# ---------- model ----------

def fit(rows, *, tau=TAU, alpha_sd=1.0, beta_sd=1.0, use_force=True):
    """Posterior mode and Laplace covariance of logit P(US) = α + β·x + θ_US − θ_CS.

    rows: dicts with 'x' (force ratio), 'y' (1 for a Union win), 'us' and 'cs' (commander IDs or None).
    """
    commanders = sorted({r[s] for r in rows for s in ('us', 'cs') if r[s]})
    index = {c: 2 + i for i, c in enumerate(commanders)}
    n = 2 + len(commanders)
    prec = [1 / alpha_sd ** 2, (1 / beta_sd ** 2) if use_force else 1e12] + [1 / tau ** 2] * len(commanders)
    design = []
    for r in rows:
        v = {0: 1.0}
        if use_force:
            v[1] = r['x']
        if r['us']:
            v[index[r['us']]] = v.get(index[r['us']], 0.0) + 1.0
        if r['cs']:
            v[index[r['cs']]] = v.get(index[r['cs']], 0.0) - 1.0
        design.append((v, r['y']))
    w = [0.0] * n

    def objective(w):
        total = sum(p * wi * wi for p, wi in zip(prec, w)) / 2
        for v, y in design:
            z = sum(w[j] * c for j, c in v.items())
            total += max(z, 0) + math.log1p(math.exp(-abs(z))) - y * z
        return total

    for _ in range(200):
        grad = [p * wi for p, wi in zip(prec, w)]
        hess = [[0.0] * n for _ in range(n)]
        for i in range(n):
            hess[i][i] = prec[i]
        for v, y in design:
            z = sum(w[j] * c for j, c in v.items())
            p = sigmoid(z)
            q = p * (1 - p)
            for j, cj in v.items():
                grad[j] += (p - y) * cj
                for k, ck in v.items():
                    hess[j][k] += q * cj * ck
        low = cholesky(hess)
        d = chol_solve(low, grad)
        decrement = sum(g * di for g, di in zip(grad, d))
        if decrement < 1e-12:
            w = [wi - di for wi, di in zip(w, d)]
            return _result(w, cholesky(_hessian(w, design, prec, n)), commanders, index)
        step, current = 1.0, objective(w)
        while objective([wi - step * di for wi, di in zip(w, d)]) > current - 1e-4 * step * decrement:
            step /= 2
            if step < 1e-12:
                raise RatingError('Line search failed')
        w = [wi - step * di for wi, di in zip(w, d)]
    raise RatingError('Newton iteration did not converge')


def _hessian(w, design, prec, n):
    hess = [[0.0] * n for _ in range(n)]
    for i in range(n):
        hess[i][i] = prec[i]
    for v, _ in design:
        p = sigmoid(sum(w[j] * c for j, c in v.items()))
        for j, cj in v.items():
            for k, ck in v.items():
                hess[j][k] += p * (1 - p) * cj * ck
    return hess


def _result(w, low, commanders, index):
    cov = chol_inverse(low)
    return {'alpha': w[0], 'beta': w[1], 'theta': {c: w[index[c]] for c in commanders},
            'sd': {c: math.sqrt(cov[index[c]][index[c]]) for c in commanders},
            'mode': w, 'cov': cov, 'index': index, 'commanders': commanders}


def predict(model, row):
    z = model['alpha'] + model['beta'] * row['x']
    z += model['theta'].get(row['us'], 0.0) if row['us'] else 0.0
    z -= model['theta'].get(row['cs'], 0.0) if row['cs'] else 0.0
    return sigmoid(z)


def rank_intervals(model, ranked_by_side, draws=DRAWS, seed=SEED):
    """Central 80% and 95% within-side rank intervals from draws of the Laplace approximation (rank 1 = highest θ)."""
    idx = [model['index'][c] for side in ranked_by_side.values() for c in side]
    if not idx:
        return {}
    sub = [[model['cov'][i][j] for j in idx] for i in idx]
    low = cholesky([[sub[i][j] + (1e-12 if i == j else 0.0) for j in range(len(idx))] for i in range(len(idx))])
    mean = [model['mode'][i] for i in idx]
    pos = {model['commanders'][i - 2]: k for k, i in enumerate(idx)}
    rng = random.Random(seed)
    ranks = defaultdict(list)
    for _ in range(draws):
        e = [rng.gauss(0, 1) for _ in idx]
        v = [mean[i] + sum(low[i][k] * e[k] for k in range(i + 1)) for i in range(len(idx))]
        for side in ranked_by_side.values():
            order = sorted(side, key=lambda c: -v[pos[c]])
            for r, c in enumerate(order, 1):
                ranks[c].append(r)

    def q(xs, p):
        xs = sorted(xs)
        return xs[min(len(xs) - 1, max(0, int(math.floor(p * len(xs)))))]
    return {c: {'rank_median': q(r, 0.5), 'rank_80': [q(r, 0.1), q(r, 0.9)], 'rank_95': [q(r, 0.025), q(r, 0.975)]}
            for c, r in ranks.items()}


def components(rows):
    parent = {}

    def find(a):
        parent.setdefault(a, a)
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for r in rows:
        for c in (r['us'], r['cs']):
            if c:
                find(c)
        if r['us'] and r['cs']:
            parent[find(r['us'])] = find(r['cs'])
    groups = defaultdict(list)
    for c in parent:
        groups[find(c)].append(c)
    return {c: min(g) for g in groups.values() for c in g}


def summarize(rows, model, side_of):
    """Per-commander estimates, intervals and within-side ranks for one fitted view."""
    battles = Counter(r[s] for r in rows for s in ('us', 'cs') if r[s])
    ranked = {side: sorted(c for c in model['commanders'] if side_of[c] == side and battles[c] >= 2) for side in SIDES}
    ranks = rank_intervals(model, ranked)
    comp = components(rows)
    out = {}
    for c in model['commanders']:
        t, sd = model['theta'][c], model['sd'][c]
        same = [o for o in ranked[side_of[c]] if o != c and comp.get(o) == comp.get(c)]
        out[c] = {'battles_modelled': battles[c], 'theta_mode': t, 'sd': sd,
                  'interval_80': [t - Z80 * sd, t + Z80 * sd], 'interval_95': [t - Z95 * sd, t + Z95 * sd],
                  'component': comp.get(c), 'ranked': c in ranks, **ranks.get(c, {}),
                  'labels': (['not_connected'] if c in ranks and not same else [])}
    return out


# ---------- rows and views ----------

def attribution(side, view=None, alt=None):
    """The commander credited for one ledger side under a view."""
    if alt is not None:
        return alt
    if view == 'grades_ab' and side['grade'] not in {'A', 'B'}:
        return None
    if view == 'superior' and side.get('superior'):
        return side['superior']
    if view == 'successor' and 'command_changed' in side['labels'] and side['successor']:
        return side['successor']
    return side['commander_id']


def primary_rows(strength, command, records, ends=('point', 'point')):
    by = {r['battle_id']: r for r in records}
    rows = []
    for e in strength['engagements']:
        est = {s: e['sides'][s]['estimate'] for s in SIDES}
        n = nested_sets(est)
        if 'set3_ABC' not in n['sets'] or n['excluded_post_start_information']:
            continue
        rec = by[e['battle_id']]
        rows.append({'battle_id': e['battle_id'], 'campaign': rec['campaign'], 'year': rec['start_date'][:4],
                     'x': advantage(est['US'][ends[0]], est['Confederate'][ends[1]]),
                     'y': int(rec['source_result'] == 'Union'),
                     'sides': command[e['battle_id']]['sides']})
    return rows


def attach(rows, view=None, alt=None):
    out = []
    for r in rows:
        a = alt if alt and alt[0] == r['battle_id'] else None
        out.append({**r, 'us': attribution(r['sides']['US'], view, a[2] if a and a[1] == 'US' else None),
                    'cs': attribution(r['sides']['Confederate'], view, a[2] if a and a[1] == 'Confederate' else None)})
    return out


def heldout(rows, **params):
    """Leave-one-campaign-out: the commander model against the strength-only model (design §5)."""
    preds, effective = [], []
    for camp in sorted({r['campaign'] for r in rows}):
        train = [r for r in rows if r['campaign'] != camp]
        test = [r for r in rows if r['campaign'] == camp]
        model = fit(train, **params)
        base = fit_logistic([r['x'] for r in train], [r['y'] for r in train])
        seen = set(model['theta'])
        for r in test:
            known = [c for c in (r['us'], r['cs']) if c in seen]
            if known:
                effective.append({'battle_id': r['battle_id'], 'commanders': known})
            preds.append({'battle_id': r['battle_id'], 'campaign': camp, 'union_outcome': r['y'],
                          'commander_model': predict(model, r), 'strength_only': base.predict(r['x'])})
    models = (('commander_model', 'commander_model'), ('strength_only', 'strength_only'))
    battle = {n: scores(preds, k) for n, k in models}
    camps = sorted({p['campaign'] for p in preds})
    campaign = {n: {m: sum(scores([p for p in preds if p['campaign'] == c], k)[m] for c in camps) / len(camps)
                    for m in ('brier', 'log_loss')} for n, k in models}
    wins = Counter()
    for c in camps:
        ps = [p for p in preds if p['campaign'] == c]
        a, b = scores(ps, 'commander_model')['log_loss'], scores(ps, 'strength_only')['log_loss']
        wins['commander_model' if a < b else 'strength_only' if b < a else 'tie'] += 1
    improved = all(w['commander_model']['log_loss'] < w['strength_only']['log_loss'] for w in (battle, campaign))
    return {'improved': improved, 'battle_weighted': battle, 'campaign_weighted': campaign,
            'campaigns_better': dict(wins), 'effective_rows': effective, 'n_rows': len(preds), 'predictions': preds}


def temporal(rows, years=(('1862',), ('1863',)), **params):
    train = [r for r in rows if r['year'] in years[0]]
    test = [r for r in rows if r['year'] in years[1]]
    if not train or not test or len({r['y'] for r in train}) < 2:
        return {'evaluable': False}
    model = fit(train, **params)
    base = fit_logistic([r['x'] for r in train], [r['y'] for r in train])
    preds = [{'union_outcome': r['y'], 'commander_model': predict(model, r), 'strength_only': base.predict(r['x'])} for r in test]
    return {'evaluable': True, 'n_train': len(train), 'n_test': len(test), 'verdict': None,
            'commander_model': scores(preds, 'commander_model'), 'strength_only': scores(preds, 'strength_only')}


def outcome_rows_91(command, records):
    """All decisive in-scope engagements, dropping contained records of nested pairs (design §2 rule 7)."""
    by = {r['battle_id']: r for r in records}
    nested = {n['contained'] for n in command['nesting'] if n['outcome'] == 'nested'}
    unresolved = {n['contained'] for n in command['nesting'] if n['outcome'] == 'nesting_unresolved'}
    rows = [{'battle_id': b, 'campaign': by[b]['campaign'], 'year': by[b]['start_date'][:4], 'x': 0.0,
             'y': int(by[b]['source_result'] == 'Union'), 'sides': e['sides']}
            for b, e in sorted(command['by_id'].items()) if b not in nested]
    return rows, sorted(nested), sorted(unresolved - nested)


# ---------- gate and run ----------

def authorize(root, path=DEFAULT_AUTHORIZATION, run=None):
    run = run or RUNS[1]
    auth = read_json(safe_path(root, path))
    require = {'strength_ledger': run['strength'], 'command_ledger': run['command'], 'registry': run['registry']}
    if auth.get('kind') != 'commander_rating_authorization':
        raise RatingError('Authorization record kind')
    for key, p in require.items():
        b = auth.get(key) or {}
        if b.get('path') != p or b.get('sha256') != digest(safe_path(root, p)):
            raise RatingError(f'Authorization names a different {key}; no fit runs')
    if auth.get('admits_feature') is not False or auth.get('changes_baseline') is not False:
        raise RatingError('A rating run admits no feature and leaves the baseline unchanged')
    return auth


def rate(root, version=1):
    run = RUNS[version]
    auth = authorize(root, run['authorization'], run)
    run['check_strength'](root, run['strength'])
    check_command(root, run['command'])
    strength = read_json(safe_path(root, run['strength']))
    command_ledger = read_json(safe_path(root, run['command']))
    if not strength['status'].startswith('reviewed') or not command_ledger['status'].startswith('reviewed'):
        raise RatingError('Both ledgers must be reviewed and reconciled')
    registry = {c['id']: c for c in read_json(safe_path(root, run['registry']))['commanders']}
    side_of = {c: registry[c]['side'] for c in registry}
    records, _ = build_dataset(root, run['cohort'])
    v_primary, v_all = run['views']
    command = {e['battle_id']: e for e in command_ledger['engagements']}
    base = primary_rows(strength, command, records)
    primary = attach(base)
    model = fit(primary)
    ratings = summarize(primary, model, side_of)
    test = heldout(primary)
    views = {}

    def view(name, rows, **params):
        m = fit(rows, **params)
        views[name] = {'rows': len(rows), 'params': {k: v for k, v in params.items()}, 'ratings': summarize(rows, m, side_of)}
    view('tau_0.25', primary, tau=0.25)
    view('tau_1.0', primary, tau=1.0)
    view('alpha_sd_3', primary, alpha_sd=3.0)
    view('grades_ab', attach(base, 'grades_ab'))
    view('superior_directing', attach(base, 'superior'))
    view('command_changed_excluded', [r for r in primary if not any('command_changed' in r['sides'][s]['labels'] for s in SIDES)])
    view('command_changed_successor', attach(base, 'successor'))
    for us_end, cs_end in product(('low', 'high'), repeat=2):
        view(f'endpoint_us_{us_end}_cs_{cs_end}', attach(primary_rows(strength, command, records, (us_end, cs_end))))
    for r in base:
        for s in SIDES:
            for cand in r['sides'][s]['candidates']:
                if cand != r['sides'][s]['commander_id']:
                    view(f'alternative_{r["battle_id"]}_{s}_{cand}', attach(base, alt=(r['battle_id'], s, cand)))
    robustness = list(views)
    view(v_primary, primary, use_force=False)
    command_ledger['by_id'] = command
    rows91, dropped, unresolved = outcome_rows_91(command_ledger, records)
    view(v_all, attach(rows91), use_force=False)
    views[v_all].update({'dropped_as_nested': dropped, 'labels': ['includes_force_size_advantage', 'expanded_rows']})
    views[v_primary]['labels'] = ['includes_force_size_advantage']
    for u in unresolved:
        view(f'{v_all}_without_{u}', attach([r for r in rows91 if r['battle_id'] != u]), use_force=False)
    # view_sensitive (design §6)
    for c, pr in ratings.items():
        pr['view_sensitive'] = []
        pr['unranked_in_view'] = []
        if pr['battles_modelled'] < 2:
            continue
        for name in robustness:
            v = views[name]['ratings'].get(c)
            if v is None or not v['ranked']:
                pr['unranked_in_view'].append(name)
            if v is None:
                continue
            opposite = (v['interval_80'][0] > 0 and pr['theta_mode'] < 0) or (v['interval_80'][1] < 0 and pr['theta_mode'] > 0)
            disjoint = v['ranked'] and pr['ranked'] and (v['rank_80'][1] < pr['rank_80'][0] or v['rank_80'][0] > pr['rank_80'][1])
            if opposite or disjoint:
                pr['view_sensitive'].append(name)
    # coverage and raw residuals
    evaluation = read_json(root / run['evaluation'])
    p_by = {p['battle_id']: p['diagnostic_union_score'] for p in evaluation['row_sets']['set3_ABC']['predictions']}
    attributed = defaultdict(list)
    for b, e in command.items():
        for s in SIDES:
            if e['sides'][s]['commander_id']:
                attributed[e['sides'][s]['commander_id']].append((b, s, e['sides'][s]))
    in_model = {r['battle_id'] for r in primary}
    strength_by = {e['battle_id']: {s: e['sides'][s]['estimate'] for s in SIDES} for e in strength['engagements']}

    def out_reasons(b):
        est = strength_by[b]
        reasons = []
        if any(est[s]['grade'] == 'D' for s in SIDES):
            reasons.append('strength_grade_D')
        if any('post_start_information' in est[s]['labels'] for s in SIDES):
            reasons.append('post_start_information')
        return reasons
    out = {}
    for c in sorted(set(attributed) | set(ratings)):
        rows_c = [(r, s) for r in primary for s, k in (('US', 'us'), ('Confederate', 'cs')) if r[k] == c]
        resid = sum((r['y'] - p_by[r['battle_id']]) * (1 if s == 'US' else -1) for r, s in rows_c)
        wins = sum((r['y'] == 1) == (s == 'US') for r, s in rows_c)
        out[c] = {'name': registry[c]['name'], 'side': side_of[c],
                  'battles_attributed': len(attributed[c]), 'battles_modelled': len(rows_c),
                  'wins_in_model': wins, 'losses_in_model': len(rows_c) - wins,
                  'out_of_model': sorted(b for b, _, _ in attributed[c] if b not in in_model),
                  'out_of_model_reasons': {b: out_reasons(b) for b, _, _ in attributed[c] if b not in in_model},
                  f'dropped_as_nested_in_{v_all}': sorted(b for b, _, _ in attributed[c] if b in dropped),
                  'raw_residual_sum': resid,
                  'echelons': sorted({x['echelon'] for _, _, x in attributed[c]}),
                  'attribution_grades': dict(Counter(x['grade'] for _, _, x in attributed[c])),
                  'attribution_labels': sorted({l for _, _, x in attributed[c] for l in x['labels']}),
                  **ratings.get(c, {'ranked': False}),
                  'posterior_prior_sd_ratio': ratings[c]['sd'] / TAU if c in ratings else None,
                  'views': {n: (dict(v['ratings'][c], theta_mode_minus_primary=v['ratings'][c]['theta_mode'] - ratings[c]['theta_mode'])
                                if c in v['ratings'] and c in ratings else v['ratings'].get(c)) for n, v in views.items()}}
        if not test['improved'] and c in ratings:
            out[c].setdefault('labels', []).append('no_heldout_signal')
    return {'kind': 'commander_residual_ratings', 'status': 'exploratory_diagnostic_not_skill_not_ranking_of_record',
            'authorization': {'path': run['authorization'], 'sha256': digest(safe_path(root, run['authorization'])),
                              'decision_date': auth['decision_date']},
            'ledgers': {k: {'path': run[k], 'sha256': digest(safe_path(root, run[k]))} for k in ('strength', 'command', 'registry')},
            'raw_residual_input': {'path': run['evaluation'], 'sha256': digest(root / run['evaluation'])},
            **({} if version == 1 else {'run_version': version, 'cohort': {'path': run['cohort'], 'sha256': digest(safe_path(root, run['cohort']))}}),
            'model': {'tau': TAU, 'alpha_sd': 1.0, 'beta_sd': 1.0, 'alpha': model['alpha'], 'beta': model['beta'],
                      'draws': DRAWS, 'seed': SEED, 'rows': len(primary), 'campaigns': len({r['campaign'] for r in primary})},
            'heldout_test': test, 'temporal_split': ({**temporal(primary, run['temporal']), **({} if version == 1 else {'years': run['temporal']})}),
            'commanders': out,
            'views': {n: {k: v for k, v in x.items() if k != 'ratings'} for n, x in views.items()},
            'flags': FLAGS}


def report_text(result):
    """Markdown summary. Without a held-out improvement it gives no ordered ranking (design §5)."""
    t = result['heldout_test']
    f = lambda m: f"{m['log_loss']:.4f}"
    lines = ['# Commander residual ratings (diagnostic)', '',
             '**A residual rating is not command skill, a causal effect or a ranking of record.** It summarises how a '
             "commander's battles went relative to what force size predicts, pulled towards zero, relative to their own side.", '',
             f"Rows: {result['model']['rows']} battles in {result['model']['campaigns']} campaigns. Pooling τ = {result['model']['tau']}. "
             f"Every result carries {', '.join('`' + x + '`' for x in result['flags'])}.", '',
             '## Held-out test (the verdict)', '',
             '| Model | Log loss, battle-weighted | Log loss, campaign-weighted |', '|---|---:|---:|',
             f"| Commander model | {f(t['battle_weighted']['commander_model'])} | {f(t['campaign_weighted']['commander_model'])} |",
             f"| Strength only | {f(t['battle_weighted']['strength_only'])} | {f(t['campaign_weighted']['strength_only'])} |", '',
             f"Effective denominator: {len(t['effective_rows'])} of {t['n_rows']} held-out rows had a commander seen in another campaign "
             f"({', '.join(sorted({result['commanders'][c]['name'] for e in t['effective_rows'] for c in e['commanders']}))}). "
             f"Campaigns where each model had lower log loss: commander model {t['campaigns_better'].get('commander_model', 0)}, "
             f"strength only {t['campaigns_better'].get('strength_only', 0)}, ties {t['campaigns_better'].get('tie', 0)}.", '']
    ts = result['temporal_split']
    if ts.get('evaluable'):
        yrs = ts.get('years', (('1862',), ('1863',)))
        span = lambda y: y[0] if len(y) == 1 else f'{y[0]}–{y[-1]}'
        lines += [f"Descriptive {span(yrs[0])}→{span(yrs[1])} split (no verdict): trained on {ts['n_train']}, tested on {ts['n_test']}; log loss "
                  f"{f(ts['commander_model'])} (commander model) against {f(ts['strength_only'])} (strength only).", '']
    if not t['improved']:
        lines += ['**No improvement under the both-weightings rule (a lower held-out log loss was required under both '
                  'weightings, and it was not lower under both): commander identity adds no detectable predictive signal in '
                  'these data. No ordered ranking is given.** The JSON keeps every estimate, labelled `no_heldout_signal`.', '']
    else:
        lines += ['Held-out log loss was lower under both weightings on these rows. This is not evidence of a persistent '
                  'commander effect or of skill (design §5).', '']
    for side in ('US', 'Confederate'):
        cs = [c for c in result['commanders'].values() if c['side'] == side and c.get('ranked')]
        if t['improved']:
            cs.sort(key=lambda c: (c['rank_median'], -c['theta_mode']))
        else:
            cs.sort(key=lambda c: c['name'])
        lines += [f"## {side} commanders with two or more modelled battles" + ('' if t['improved'] else ' (alphabetical)'), '',
                  '| Commander | Battles | W–L | θ mode | 80% interval | 95% interval | Rank 80% | SD ratio | Labels |',
                  '|---|---:|---:|---:|---:|---:|---:|---:|---|']
        for c in cs:
            labels = sorted(set(c.get('labels', [])) | ({'view_sensitive'} if c.get('view_sensitive') else set()))
            lines.append(f"| {c['name']} | {c['battles_modelled']} | {c['wins_in_model']}–{c['losses_in_model']} | {c['theta_mode']:+.2f} | "
                         f"{c['interval_80'][0]:+.2f} to {c['interval_80'][1]:+.2f} | {c['interval_95'][0]:+.2f} to {c['interval_95'][1]:+.2f} | "
                         f"{c['rank_80'][0]}–{c['rank_80'][1]} | {c['posterior_prior_sd_ratio']:.2f} | {', '.join(labels)} |")
            if c.get('unranked_in_view'):
                lines.append(f"|  | unranked in: {', '.join(c['unranked_in_view'])} | | | | | | | |")
        lines.append('')
    lines += ['Outcome-only views (no force term, `includes_force_size_advantage`) estimate a different quantity; each '
              "commander's view results and differences from the primary rating are in the JSON.", '',
              'Commanders with one modelled battle are in the JSON with their estimate, which is almost entirely the prior. '
              'Commanders outside the model are listed there with coverage only.', '']
    return '\n'.join(lines)
