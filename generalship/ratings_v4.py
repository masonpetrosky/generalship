"""Commander residual ratings, run 4 (docs/commander-ratings-v4.md).

Run 3's partially pooled residual model and multiple imputation, with the changes the design fixed before
the run:

- a context comparator: theater, period and theater-by-period effects on the odds of a side A win;
- the commander spread tau estimated by Laplace marginal likelihood, within each training fold;
- leakage handling: the pre-start strength view, and no commander term for a side whose commander rule 5
  chose by the force compelling the result;
- a pre-registered uncertainty rule: a campaign bootstrap must put the 95th percentile of the log-loss
  difference below zero under both weightings;
- a war profile in place of Civil War constants, and a commander's sign taken from the side they
  commanded in each row, not from a fixed registry side.

Rows hold side A's and side B's commanders in the slots 'a' and 'b' (profile['sides'] order). The run is
refused unless an owner authorization names the exact files and code; outputs never enter
artifacts/baseline.json.
"""

from collections import Counter, defaultdict
from itertools import product
import math
from operator import mul
import platform
import random

from .baseline import advantage, fit_logistic, sigmoid
from .command import check as check_command
from .estimates_v3 import check as check_strength
from .frame import CIVIL_WAR, battles as frame_battles, outcome, period as frame_period, theaters as frame_theaters
from .imputation import quantile as tn_quantile
from .imputation_v2 import build as build_imputation, impute, prestart_view
from .parallel import pmap
from .ratings import RatingError, attribution, chol_inverse, chol_solve, cholesky
from .replay import bound_view
from .sources import digest, read_json, safe_path
from .uncertainty import bootstrap, log_loss, quantile, sign_test, weighted

PROFILE = CIVIL_WAR
AUTHORIZATION = 'data/command/rating-authorization-v4.json'
DESIGN = 'docs/commander-ratings-v4.md'
IMPUTATION = 'artifacts/strength-imputation-v2.json'
OUTPUT = 'artifacts/commander-ratings-v4'
# Every package module the run imports (tests/test_ratings_v4.py checks the list against the import closure).
CODE = tuple(f'generalship/{m}.py' for m in (
    '__init__', 'baseline', 'command', 'dataset', 'estimates', 'estimates_v2', 'estimates_v3', 'evidence', 'frame',
    'imputation', 'imputation_v2', 'parallel', 'ratings', 'ratings_v4', 'replay', 'sources', 'uncertainty'))
TAU = 0.5  # the fixed convention of runs 1-3: the bridge and the tau_0.5 comparison
KAPPA = 0.5  # prior SD of each context effect
TAU_GRID = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.25, 1.5)  # 0 is the context model
CHI2_95_HALF = 1.92  # half the 95% point of chi-square(1): the approximate profile interval
M = 20
SEED = 20261006  # imputation draws
RANK_SEED = 20261007  # Laplace draws for intervals and ranks
BOOTSTRAP_SEED = 20261008
SIM_SEED = 20261009  # outcomes simulated under the context model (the tau = 0 calibration)
SIMULATIONS = 100
M_SIM = 5  # imputations used by the tau = 0 calibration, observed and simulated alike
RESAMPLES = 20000
DRAWS = 20000  # rank draws of a single-fit view
DRAWS_PER = 1000  # Laplace draws per imputation in a pooled fit
Z80, Z95 = 1.2815515655446004, 1.959963984540054
FLAGS = ['whole_engagement_leakage', 'conditional_on_source_availability', 'not_causal', 'side_relative']
MODELS = ('commander', 'context', 'commander_tau_0.5', 'commander_no_context', 'strength_only')
SLOTS = ('a', 'b')


def bound_files(profile=PROFILE):
    return {'design': DESIGN, 'imputation': IMPUTATION, 'strength_ledger': profile['strength_ledger'],
            'command_ledger': profile['command_ledger'], 'registry': profile['registry'],
            'campaigns': profile['campaigns'], 'battles': profile['battles']}


def authorize(root, path=AUTHORIZATION, profile=PROFILE):
    """The owner's authorization must bind every input file and every module the run executes."""
    auth = read_json(safe_path(root, path))
    if auth.get('kind') != 'commander_rating_authorization' or auth.get('run_version') != 4:
        raise RatingError('Authorization record kind')
    for key, p in bound_files(profile).items():
        b = auth.get('files', {}).get(key)
        if not isinstance(b, dict) or b.get('path') != p or b.get('sha256') != digest(safe_path(root, p)):
            raise RatingError(f'Authorization names a different {key}; no fit runs')
    code = auth.get('code', {})
    if sorted(code) != sorted(CODE) or any(code[p] != digest(safe_path(root, p)) for p in CODE):
        raise RatingError('Authorization binds different code; no fit runs')
    if auth.get('admits_feature') is not False or auth.get('changes_baseline') is not False:
        raise RatingError('A rating run admits no feature and leaves the baseline unchanged')
    return auth


# ---------- rows ----------

def base_rows(root, profile, imputation, prestart=True):
    """Every in-scope engagement less contained nested records (design §3), with each side's strength spec."""
    strength = read_json(safe_path(root, profile['strength_ledger']))
    command = read_json(safe_path(root, profile['command_ledger']))
    battles = frame_battles(root, profile)
    theater = frame_theaters(root, profile)
    view = prestart_view(strength) if prestart else {}
    nested = {n['contained'] for n in command['nesting'] if n['outcome'] == 'nested'}
    unresolved = sorted({n['contained'] for n in command['nesting'] if n['outcome'] == 'nesting_unresolved'} - nested)
    cmd = {e['battle_id']: e for e in command['engagements']}
    grade_e = {(s['battle_id'], s['side']): s for s in imputation['sides']}
    rows = []
    for e in strength['engagements']:
        b = e['battle_id']
        if b in nested:
            continue
        spec, labels = {}, set()
        for s in profile['sides']:
            est = view[(b, s)]['estimate'] if (b, s) in view else e['sides'][s]['estimate']
            if (b, s) in view:
                labels.add('post_start_in_ledger')
            if est['grade'] == 'D':
                g = grade_e[(b, s)]
                spec[s] = {'grade': 'E', **{k: g[k] for k in ('mu_log', 'sd_log', 'lower_bound', 'upper_bound', 'fixed',
                                                             'point', 'low', 'high')}}
                labels.add('modelled_strength')
                labels |= {x for x in g['labels'] if x in {'bound_conflict', 'naval_side', 'post_start_modelled'}}
            else:
                spec[s] = {'grade': est['grade'], 'point': est['point'], 'low': est['low'], 'high': est['high']}
                if 'post_start_information' in est['labels']:
                    labels.add('post_start_information')
            if 'joint_command' in cmd[b]['sides'][s]['labels']:
                labels.add('joint_command')
        y = outcome(profile, battles[b]['result'])
        if y is None:
            raise RatingError(f"{b}: result {battles[b]['result']!r} is not a decisive outcome under the profile")
        th, per = theater[battles[b]['campaign']], frame_period(profile, battles[b]['start_date'])
        rows.append({'battle_id': b, 'campaign': battles[b]['campaign'], 'year': battles[b]['start_date'][:4],
                     'ctx': [f'theater={th}', f'period={per}', f'cell={th}|{per}'], 'y': y,
                     'sides': cmd[b]['sides'], 'spec': spec, 'labels': sorted(labels),
                     'graded_row': all(spec[s]['grade'] in 'ABC' for s in profile['sides'])
                     and 'post_start_information' not in labels})
    return rows, sorted(nested), unresolved


def attributions(root, profile):
    """{commander: [(battle_id, side, joint)]} over every in-scope ledger side, nested records included."""
    out = defaultdict(list)
    for e in read_json(safe_path(root, profile['command_ledger']))['engagements']:
        for s in profile['sides']:
            c = e['sides'][s]['commander_id']
            if c:
                out[c].append((e['battle_id'], s, 'joint_command' in e['sides'][s]['labels']))
    return out


def e_value(spec, u, sd_scale=1.0):
    if spec['fixed'] is not None:
        return spec['fixed']
    return tn_quantile(spec['mu_log'], spec['sd_log'] * sd_scale, u, spec['lower_bound'], spec['upper_bound'])


def imputations(rows, profile, m=M, seed=SEED, sd_scale=1.0):
    """M imputed strength sets: one random.Random(seed) stream, imputation by imputation, grade E sides
    sorted by battle and side order."""
    sides = profile['sides']
    order = sorted((r['battle_id'], sides.index(s)) for r in rows for s in sides if r['spec'][s]['grade'] == 'E')
    by = {r['battle_id']: r for r in rows}
    rng = random.Random(seed)
    out = []
    for _ in range(m):
        vals = {}
        for b, i in order:
            vals[(b, sides[i])] = e_value(by[b]['spec'][sides[i]], rng.random(), sd_scale)
        out.append(vals)
    return out


def with_x(rows, profile, strengths, view=None, alt=None, ends=None, credit_joint=False):
    """Rows with x from one strength set and the credited commanders in slots a and b.

    ends picks ledger low/high and grade E 10th/90th percentiles. A joint_command side gets no commander unless
    credit_joint is set or alt names a candidate for that side."""
    out = []
    for r in rows:
        v = []
        for k, s in enumerate(profile['sides']):
            spec = r['spec'][s]
            if ends:
                v.append(spec[ends[k]])
            elif spec['grade'] == 'E':
                v.append(strengths[(r['battle_id'], s)] if strengths is not None else spec['point'])
            else:
                v.append(spec['point'])
        a = alt if alt and alt[0] == r['battle_id'] else None
        slots = {}
        for slot, s in zip(SLOTS, profile['sides']):
            side = r['sides'][s]
            on_side = a is not None and a[1] == s
            c = attribution(side, view, a[2] if on_side else None)
            if 'joint_command' in side['labels'] and not credit_joint and not on_side:
                c = None
            slots[slot] = c
        out.append({**r, 'x': advantage(v[0], v[1]), **slots})
    return out


def slim(rows):
    """The fields a fit, prediction or score reads."""
    return [{k: r[k] for k in ('battle_id', 'campaign', 'year', 'ctx', 'x', 'y', 'a', 'b')} for r in rows]


# ---------- the model ----------

def fit4(rows, *, tau=TAU, kappa=KAPPA, alpha_sd=1.0, beta_sd=1.0, use_force=True, use_context=True,
         out='mode'):
    """Posterior mode of logit P(side A wins) = α + β·x + Σ context effects + θ[a] − θ[b] (design §4).

    Parameters are ordered α, β, context effects (sorted), commanders (sorted); tau = 0 drops the commander
    terms (the context model). Without context terms the arithmetic is ratings.fit's, term for term, so the
    two agree exactly (tests/test_ratings_v4.py). out: 'mode' (enough to predict), 'evidence' (adds the
    Laplace log marginal likelihood) or 'covariance' (adds the Laplace covariance and the θ SDs).
    """
    ctx = sorted({f for r in rows for f in r['ctx']}) if use_context else []
    commanders = sorted({r[s] for r in rows for s in SLOTS if r[s]}) if tau > 0 else []
    cindex = {f: 2 + i for i, f in enumerate(ctx)}
    index = {c: 2 + len(ctx) + i for i, c in enumerate(commanders)}
    n = 2 + len(ctx) + len(commanders)
    prec = ([1 / alpha_sd ** 2, (1 / beta_sd ** 2) if use_force else 1e12] + [1 / kappa ** 2] * len(ctx)
            + ([1 / tau ** 2] * len(commanders) if commanders else []))
    design = []
    for r in rows:
        v = {0: 1.0}
        if use_force:
            v[1] = r['x']
        for f in (r['ctx'] if use_context else ()):
            v[cindex[f]] = 1.0
        if commanders:
            if r['a']:
                v[index[r['a']]] = v.get(index[r['a']], 0.0) + 1.0
            if r['b']:
                v[index[r['b']]] = v.get(index[r['b']], 0.0) - 1.0
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
            model = {'alpha': w[0], 'beta': w[1], 'context': {f: w[cindex[f]] for f in ctx},
                     'theta': {c: w[index[c]] for c in commanders}, 'mode': w, 'index': index,
                     'commanders': commanders, 'tau': tau}
            if out == 'mode':
                return model
            low = cholesky(_hessian(w, design, prec, n))
            if out == 'evidence':
                # log p(y) ≈ −objective(ŵ) + ½ Σ log prior precision − ½ log det H (the 2π terms cancel)
                model['log_evidence'] = (-objective(w) + math.fsum(math.log(p) for p in prec) / 2
                                         - math.fsum(math.log(low[i][i]) for i in range(n)))
                return model
            cov = chol_inverse(low)
            model['cov'] = cov
            model['sd'] = {c: math.sqrt(cov[index[c]][index[c]]) for c in commanders}
            return model
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


def predict4(model, row):
    """P(side A wins); a context effect or commander unseen in training contributes 0 (its prior mean)."""
    z = model['alpha'] + model['beta'] * row['x']
    for f in row['ctx']:
        z += model['context'].get(f, 0.0)
    z += model['theta'].get(row['a'], 0.0) if row['a'] else 0.0
    z -= model['theta'].get(row['b'], 0.0) if row['b'] else 0.0
    return sigmoid(z)


def select_tau(mean_evidence):
    """The grid value with the highest mean log evidence; a tie goes to the smaller tau."""
    best = max(mean_evidence.values())
    return min(t for t, v in mean_evidence.items() if v == best)


def components(rows):
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for r in rows:
        for c in (r['a'], r['b']):
            if c:
                find(c)
        if r['a'] and r['b']:
            parent[find(r['a'])] = find(r['b'])
    groups = defaultdict(list)
    for c in parent:
        groups[find(c)].append(c)
    return {c: min(g) for g in groups.values() for c in g}


def q(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, max(0, int(math.floor(p * len(xs)))))]


def ranked_sets(rows, commanders, side_of, sides):
    battles = Counter(r[s] for r in rows for s in SLOTS if r[s])
    return battles, {side: sorted(c for c in commanders if side_of[c] == side and battles[c] >= 2) for side in sides}


def rank_draws(model, ranked, rng, draws):
    """Within-side ranks (1 = highest θ) from joint draws of the Laplace approximation over the ranked commanders."""
    rc = [c for side in ranked.values() for c in side]
    ranks = defaultdict(list)
    if not rc:
        return ranks
    idx = [model['index'][c] for c in rc]
    sub = [[model['cov'][i][j] + (1e-12 if i == j else 0.0) for j in idx] for i in idx]
    low = cholesky(sub)
    mean = [model['mode'][i] for i in idx]
    pos = {c: k for k, c in enumerate(rc)}
    for _ in range(draws):
        e = [rng.gauss(0, 1) for _ in idx]
        v = [mean[i] + sum(map(mul, low[i][:i + 1], e[:i + 1])) for i in range(len(idx))]
        for side in ranked.values():
            for r_, c in enumerate(sorted(side, key=lambda c: -v[pos[c]]), 1):
                ranks[c].append(r_)
    return ranks


def summarize(rows, model, side_of, sides, ranks):
    """Per-commander estimate, intervals, component and rank summary of one fit or pooled set."""
    battles, ranked = ranked_sets(rows, model['commanders'], side_of, sides)
    comp = components(rows)
    out = {}
    for c in model['commanders']:
        same = [o for o in ranked[side_of[c]] if o != c and comp.get(o) == comp.get(c)]
        rk = ranks.get(c)
        out[c] = {'battles_modelled': battles[c], 'component': comp.get(c), 'ranked': rk is not None,
                  **({'rank_median': q(rk, 0.5), 'rank_80': [q(rk, 0.1), q(rk, 0.9)], 'rank_95': [q(rk, 0.025), q(rk, 0.975)]}
                     if rk is not None else {}),
                  'labels': ['not_connected'] if rk is not None and not same else []}
    return out


# ---------- held-out comparisons ----------

def _primary_fold(camp, rows_by_m):
    """One held-out campaign: the tau grid with context, the no-context commander model and strength only,
    fitted on the other campaigns in every imputation; tau-hat chosen on the training rows alone."""
    evidence, preds, effective = defaultdict(list), {}, []
    for mi, rows in enumerate(rows_by_m):
        train = [r for r in rows if r['campaign'] != camp]
        test = [r for r in rows if r['campaign'] == camp]
        for tau in TAU_GRID:
            model = fit4(train, tau=tau, out='evidence')
            evidence[tau].append(model['log_evidence'])
            for r in test:
                preds.setdefault(r['battle_id'], defaultdict(list))[tau].append(predict4(model, r))
            if mi == 0 and tau == TAU:
                seen = set(model['theta'])
                effective += [{'battle_id': r['battle_id'], 'commanders': [c for c in (r['a'], r['b']) if c in seen]}
                              for r in test if any(c in seen for c in (r['a'], r['b']) if c)]
        nc = fit4(train, use_context=False)
        logit = fit_logistic([r['x'] for r in train], [r['y'] for r in train])
        for r in test:
            preds[r['battle_id']]['commander_no_context'].append(predict4(nc, r))
            preds[r['battle_id']]['strength_only'].append(logit.predict(r['x']))
    mean_ev = {t: math.fsum(v) / len(v) for t, v in evidence.items()}
    tau_hat = select_tau(mean_ev)
    out = {b: {'commander': p[tau_hat], 'context': p[0.0], 'commander_tau_0.5': p[TAU],
               'commander_no_context': p['commander_no_context'], 'strength_only': p['strength_only']}
           for b, p in preds.items()}
    return out, effective, {'campaign': camp, 'tau_hat': tau_hat, 'mean_log_evidence': {str(t): v for t, v in mean_ev.items()}}


def _bridge_fold(camp, rows_by_m):
    """Run 3's configuration on one held-out campaign: commander terms at tau 0.5, no context, and strength only."""
    preds = {}
    for rows in rows_by_m:
        train = [r for r in rows if r['campaign'] != camp]
        model = fit4(train, use_context=False)
        logit = fit_logistic([r['x'] for r in train], [r['y'] for r in train])
        for r in rows:
            if r['campaign'] == camp:
                p = preds.setdefault(r['battle_id'], {'commander': [], 'strength_only': []})
                p['commander'].append(predict4(model, r))
                p['strength_only'].append(logit.predict(r['x']))
    return preds


def _grid_task(item, shared):
    """The tau grid on one imputation of a row set (all rows, or a temporal split's training years)."""
    mi, years = item
    rows = shared[mi]
    train = [r for r in rows if years is None or r['year'] in years[0]]
    test = [] if years is None else [r for r in rows if r['year'] in years[1]]
    evidence, preds = {}, defaultdict(dict)
    for tau in TAU_GRID:
        model = fit4(train, tau=tau, out='evidence')
        evidence[tau] = model['log_evidence']
        for r in test:
            preds[r['battle_id']][tau] = predict4(model, r)
    if test:
        nc = fit4(train, use_context=False)
        logit = fit_logistic([r['x'] for r in train], [r['y'] for r in train])
        for r in test:
            preds[r['battle_id']]['commander_no_context'] = predict4(nc, r)
            preds[r['battle_id']]['strength_only'] = logit.predict(r['x'])
    return evidence, dict(preds)


def _simulation_task(k, shared):
    """One outcome set drawn from the context model's probabilities; the tau grid's largest mean evidence gain."""
    rng = random.Random(SIM_SEED + k)
    ys = [int(rng.random() < p) for p in shared['p_context']]
    evidence = []
    for rows in shared['primary'][:M_SIM]:
        sim = [{**r, 'y': y} for r, y in zip(rows, ys)]
        evidence.append({tau: fit4(sim, tau=tau, out='evidence')['log_evidence'] for tau in TAU_GRID})
    return evidence_gain(evidence)


def evidence_gain(evidence_by_m):
    """max over the grid of the mean log evidence minus the context model's (0 when tau-hat is 0)."""
    mean_ev = {t: math.fsum(e[t] for e in evidence_by_m) / len(evidence_by_m) for t in TAU_GRID}
    return max(mean_ev.values()) - mean_ev[0.0]


def _phase1(task, shared):
    kind, item = task
    if kind == 'primary':
        return _primary_fold(item, shared['primary'])
    if kind == 'bridge':
        return _bridge_fold(item, shared['bridge'])
    if kind == 'simulation':
        return _simulation_task(item, shared)
    return _grid_task(item, shared['primary'])


def mean(xs):
    return math.fsum(xs) / len(xs)


def metrics(preds, key):
    """Battle-weighted Brier score and log loss (the clipped log loss of every scored run)."""
    return {'brier': math.fsum((p[key] - p['outcome']) ** 2 for p in preds) / len(preds),
            'log_loss': math.fsum(log_loss(p['outcome'], p[key]) for p in preds) / len(preds)}


def score(preds, models):
    battle = {k: metrics(preds, k) for k in models}
    camps = sorted({p['campaign'] for p in preds})
    by = {c: [p for p in preds if p['campaign'] == c] for c in camps}
    campaign = {k: {m: math.fsum(metrics(by[c], k)[m] for c in camps) / len(camps) for m in ('brier', 'log_loss')}
                for k in models}
    return {'battle_weighted': battle, 'campaign_weighted': campaign}


def differences(preds, first, second):
    return [{'battle_id': p['battle_id'], 'campaign': p['campaign'],
             'd': log_loss(p['outcome'], p[first]) - log_loss(p['outcome'], p[second])} for p in preds]


def compare(preds, first, second, resamples=RESAMPLES):
    """Log loss of first minus second (negative favours first): both weightings, campaign bootstrap, sign test."""
    rows = differences(preds, first, second)
    b, c = weighted(rows)
    s = sign_test(rows)
    return {'first': first, 'second': second, 'rows': len(rows), 'campaigns': len({r['campaign'] for r in rows}),
            'battle_weighted': b, 'campaign_weighted': c,
            'bootstrap': {'resamples': resamples, 'seed': BOOTSTRAP_SEED, 'unit': 'campaign',
                          **bootstrap(rows, resamples, BOOTSTRAP_SEED)},
            'sign_test': {'first_better': s['commander_model_better'], 'second_better': s['strength_only_better'],
                          'ties': s['ties'], 'two_sided_p': s['two_sided_p']}}


def verdict(comparison):
    """Design §6: an improvement only if the bootstrap 95th percentile is below zero under both weightings."""
    bs = comparison['bootstrap']
    return {'improved': bs['battle_weighted']['q0.95'] < 0 and bs['campaign_weighted']['q0.95'] < 0,
            'rule': 'campaign-bootstrap 95th percentile of the log-loss difference (commander minus context) below '
                    'zero under both the battle and the campaign weighting',
            'q95': {w: bs[w]['q0.95'] for w in ('battle_weighted', 'campaign_weighted')},
            'point_lower_both': comparison['battle_weighted'] < 0 and comparison['campaign_weighted'] < 0}


def concentration(preds, credited, names, top=10):
    """Leave one commander out, from the stored held-out predictions (no refit): who carries the verdict gain."""
    rows = differences(preds, 'commander', 'context')
    total = -math.fsum(r['d'] for r in rows)
    gain = defaultdict(list)
    for r in rows:
        for c in credited[r['battle_id']]:
            gain[c].append(-r['d'])
    contrib = sorted(({'commander': c, 'name': names[c], 'rows': len(g), 'net_gain': math.fsum(g),
                       'share_of_total': math.fsum(g) / total if total else None} for c, g in gain.items()),
                     key=lambda x: (-x['net_gain'], x['commander']))
    drop_one = []
    for c, g in gain.items():
        if len(g) < 2:
            continue
        b, w = weighted([r for r in rows if c not in credited[r['battle_id']]])
        drop_one.append({'commander': c, 'name': names[c], 'rows_dropped': len(g), 'battle_weighted': b, 'campaign_weighted': w})
    drop_one.sort(key=lambda x: (-x['battle_weighted'], x['commander']))
    out = {'total_net_gain': total, 'top_contributors': contrib[:top], 'bottom_contributors': contrib[-5:],
           'drop_one_least_favourable': drop_one[:top]}
    if contrib and contrib[0]['net_gain'] > 0:
        c0 = contrib[0]['commander']
        kept = [p for p in preds if c0 not in credited[p['battle_id']]]
        cmp = compare(kept, 'commander', 'context')
        out['without_top_contributor'] = {'commander': c0, 'name': names[c0], 'rows': len(kept),
                                          'battle_weighted': cmp['battle_weighted'], 'campaign_weighted': cmp['campaign_weighted'],
                                          'q95': {w: cmp['bootstrap'][w]['q0.95'] for w in ('battle_weighted', 'campaign_weighted')}}
    return out


# ---------- pooled estimates and views ----------

def _pooled_task(item, shared):
    """One imputation of a pooled set: the fit, DRAWS_PER marginal draws per commander and joint rank draws."""
    name, mi = item
    rows_by_m, params, ranked = shared['sets'][name]
    model = fit4(rows_by_m[mi], out='covariance', **params)
    rng = random.Random(RANK_SEED + 1 + mi)
    draws = {c: [rng.gauss(model['theta'][c], model['sd'][c]) for _ in range(DRAWS_PER)] for c in model['commanders']}
    ranks = rank_draws(model, ranked, rng, DRAWS_PER)
    return {'alpha': model['alpha'], 'beta': model['beta'], 'context': model['context'], 'theta': model['theta'],
            'draws': draws, 'ranks': dict(ranks)}


def pooled(results, rows, side_of, sides, tau):
    """Pooled point estimates (mean of modes) and intervals and ranks from the pooled draws (§5)."""
    draws, ranks, modes = defaultdict(list), defaultdict(list), defaultdict(list)
    for res in results:
        for c, d in res['draws'].items():
            draws[c] += d
            modes[c].append(res['theta'][c])
        for c, r_ in res['ranks'].items():
            ranks[c] += r_
    commanders = sorted(modes)
    summary = summarize(rows, {'commanders': commanders}, side_of, sides, ranks)
    out = {}
    for c in commanders:
        d = draws[c]
        md = math.fsum(d) / len(d)
        sd = math.sqrt(math.fsum((x - md) ** 2 for x in d) / (len(d) - 1))
        out[c] = {'theta': mean(modes[c]), 'sd': sd, 'interval_80': [q(d, 0.1), q(d, 0.9)],
                  'interval_95': [q(d, 0.025), q(d, 0.975)], 'posterior_prior_sd_ratio': sd / tau, **summary[c]}
    ctx = sorted({f for res in results for f in res['context']})
    return {'alpha': mean([res['alpha'] for res in results]), 'beta': mean([res['beta'] for res in results]),
            'context': {f: mean([res['context'].get(f, 0.0) for res in results]) for f in ctx}, 'ratings': out}


def _single_task(item, shared):
    """One view fitted once: analytic intervals and DRAWS rank draws."""
    rows, params = item
    side_of, sides = shared
    model = fit4(rows, out='covariance', **params)
    _, ranked = ranked_sets(rows, model['commanders'], side_of, sides)
    summary = summarize(rows, model, side_of, sides, rank_draws(model, ranked, random.Random(RANK_SEED), DRAWS))
    out = {}
    for c in model['commanders']:
        t, sd = model['theta'][c], model['sd'][c]
        out[c] = {'theta': t, 'sd': sd, 'interval_80': [t - Z80 * sd, t + Z80 * sd],
                  'interval_95': [t - Z95 * sd, t + Z95 * sd], **summary[c]}
    return {'alpha': model['alpha'], 'beta': model['beta'], 'context': model['context'], 'ratings': out}


def tau_summary(evidence_by_m):
    """Mean log evidence over imputations per grid value, relative to tau = 0; tau-hat and the profile interval."""
    mean_ev = {t: math.fsum(e[t] for e in evidence_by_m) / len(evidence_by_m) for t in TAU_GRID}
    tau_hat = select_tau(mean_ev)
    top = mean_ev[tau_hat]
    inside = [t for t in TAU_GRID if mean_ev[t] >= top - CHI2_95_HALF]
    per_m = Counter(select_tau(e) for e in evidence_by_m)
    return {'grid': list(TAU_GRID), 'tau_hat': tau_hat,
            'log_evidence_minus_context': {str(t): mean_ev[t] - mean_ev[0.0] for t in TAU_GRID},
            'profile_interval_95': [min(inside), max(inside)], 'zero_inside_interval': 0.0 in inside,
            'at_grid_edge': tau_hat == TAU_GRID[-1],
            'tau_hat_by_imputation': {str(t): per_m[t] for t in TAU_GRID if per_m[t]}}


# ---------- the run ----------

def rate4(root, m=M, profile=PROFILE):
    """The authorized run: refuse unless the files and code match, replay both ledgers, then compute."""
    auth = authorize(root, profile=profile)
    with bound_view(root, profile['strength_ledger'], profile['command_ledger']) as replay_root:  # docs/ledger-replay.md
        check_strength(replay_root, profile['strength_ledger'])
        check_command(replay_root, profile['command_ledger'])
    stored = read_json(safe_path(root, IMPUTATION))
    if build_imputation(root, profile) != stored:
        raise RatingError('The grade E output does not reproduce from the ledgers')
    return {'kind': 'commander_residual_ratings', 'run_version': 4, 'profile': profile['name'],
            'status': 'exploratory_diagnostic_not_skill_not_ranking_of_record',
            'authorization': {'path': AUTHORIZATION, 'sha256': digest(safe_path(root, AUTHORIZATION)),
                              'decision_date': auth['decision_date']},
            'bindings': {'files': {k: {'path': p, 'sha256': digest(safe_path(root, p))} for k, p in bound_files(profile).items()},
                         'code': {p: digest(safe_path(root, p)) for p in CODE}},
            'environment': {'python': platform.python_version(), 'implementation': platform.python_implementation()},
            **compute(root, profile, stored, m)}


def compute(root, profile, imputation, m=M):
    """Every fit, comparison, view and summary of the run (design §§3-9), from a grade E output."""
    sides = profile['sides']
    registry = {c['id']: c for c in read_json(safe_path(root, profile['registry']))['commanders']}
    side_of = {c: registry[c]['side'] for c in registry}
    names = {c: registry[c]['name'] for c in registry}
    rows, nested, unresolved = base_rows(root, profile, imputation)
    imps = imputations(rows, profile, m)
    primary_by_m = [slim(with_x(rows, profile, s)) for s in imps]
    bridge_imp = impute(root, profile, prestart=False)
    bridge_rows = base_rows(root, profile, bridge_imp, prestart=False)[0]
    bridge_by_m = [slim(with_x(bridge_rows, profile, s, credit_joint=True)) for s in imputations(bridge_rows, profile, m)]
    camps = sorted({r['campaign'] for r in rows})
    split = profile['temporal_split']

    # Phase 1: every held-out fit, tau grid and calibration draw, in one pool (longest tasks first).
    m_sim = min(M_SIM, m)
    context_fits = [fit4(rows_m, tau=0.0) for rows_m in primary_by_m[:m_sim]]
    p_context = [mean([predict4(f, rows_m[i]) for f, rows_m in zip(context_fits, primary_by_m)])
                 for i in range(len(primary_by_m[0]))]
    tasks = ([('primary', c) for c in camps] + [('simulation', k) for k in range(SIMULATIONS)] + [('bridge', c) for c in camps]
             + [('grid', (mi, None)) for mi in range(m)] + [('grid', (mi, split)) for mi in range(m)])
    results = pmap(_phase1, tasks, shared={'primary': primary_by_m, 'bridge': bridge_by_m, 'p_context': p_context})
    n1 = len(camps) + SIMULATIONS
    folds, simulated = results[:len(camps)], results[len(camps):n1]
    bridge_parts = results[n1:n1 + len(camps)]
    grids_all, grids_split = results[n1 + len(camps):n1 + len(camps) + m], results[n1 + len(camps) + m:]

    base = primary_by_m[0]
    probs, effective, fold_tau = {}, [], []
    for p, e, t in folds:
        probs.update(p)
        effective += e
        fold_tau.append(t)
    preds = [{'battle_id': r['battle_id'], 'campaign': r['campaign'], 'outcome': r['y'],
              **{k: mean(probs[r['battle_id']][k]) for k in MODELS}} for r in base]
    halves = {}
    for name, sl in (('imputations_1_10', slice(0, m // 2)), ('imputations_11_20', slice(m // 2, None))):
        ps = [{**p, **{k: mean(probs[p['battle_id']][k][sl]) for k in ('commander', 'context')}} for p in preds]
        b, w = weighted(differences(ps, 'commander', 'context'))
        halves[name] = {'battle_weighted': b, 'campaign_weighted': w}
    main = compare(preds, 'commander', 'context')
    decision = verdict(main)
    bprobs = {}
    for part in bridge_parts:
        bprobs.update(part)
    bpreds = [{'battle_id': r['battle_id'], 'campaign': r['campaign'], 'outcome': r['y'],
               'commander': mean(bprobs[r['battle_id']]['commander']),
               'strength_only': mean(bprobs[r['battle_id']]['strength_only'])} for r in bridge_by_m[0]]
    credited = {r['battle_id']: [c for c in (r['a'], r['b']) if c] for r in base}
    leak_free = {r['battle_id'] for r in rows if not {'post_start_in_ledger', 'joint_command'} & set(r['labels'])}
    lf = compare([p for p in preds if p['battle_id'] in leak_free], 'commander', 'context')
    tau_all = tau_summary([g[0] for g in grids_all])
    observed_gain = evidence_gain([g[0] for g in grids_all[:m_sim]])
    tau_all['calibration'] = {'method': 'parametric bootstrap under the context model (no commander terms)',
                              'simulations': SIMULATIONS, 'seed': SIM_SEED, 'imputations_used': m_sim,
                              'statistic': 'largest mean log-evidence gain over the tau grid against the context model',
                              'observed': observed_gain, 'simulated_quantiles': {f'q{p:g}': quantile(simulated, p) for p in (0.5, 0.9, 0.95, 0.99)},
                              'simulated_tau_hat_zero': sum(g == 0 for g in simulated),
                              'p_value': (1 + sum(g >= observed_gain for g in simulated)) / (SIMULATIONS + 1)}
    split_ev = tau_summary([g[0] for g in grids_split])
    tpreds = []
    base_by = {r['battle_id']: r for r in base}
    for b in sorted({b for g in grids_split for b in g[1]}):
        row = base_by[b]
        ps = [g[1][b] for g in grids_split]
        tpreds.append({'battle_id': b, 'campaign': row['campaign'], 'outcome': row['y'], 'year': row['year'],
                       'commander': mean([p[split_ev['tau_hat']] for p in ps]), 'context': mean([p[0.0] for p in ps]),
                       'commander_tau_0.5': mean([p[TAU] for p in ps]),
                       'commander_no_context': mean([p['commander_no_context'] for p in ps]),
                       'strength_only': mean([p['strength_only'] for p in ps])})
    if tpreds:
        tb, tw = weighted(differences(tpreds, 'commander', 'context'))
        temporal = {'evaluable': True, 'verdict': None, 'years': [list(split[0]), list(split[1])],
                    'n_train': sum(r['year'] in split[0] for r in base), 'n_test': len(tpreds),
                    'tau_hat_train': split_ev['tau_hat'], **score(tpreds, MODELS),
                    'commander_minus_context': {'battle_weighted': tb, 'campaign_weighted': tw}}
    else:
        temporal = {'evaluable': False, 'verdict': None, 'years': [list(split[0]), list(split[1])]}

    # Phase 2: pooled estimates (the primary and the multiple-imputation views) and the single-fit views.
    tau_r = tau_all['tau_hat'] if tau_all['tau_hat'] > 0 else TAU
    tau_basis = 'tau_hat' if tau_all['tau_hat'] > 0 else 'tau_hat_zero_convention_0.5'
    mi_specs = [('wide_imputation', rows, 2.0),
                ('train_graded_ab', base_rows(root, profile, impute(root, profile, train_grades='AB'))[0], 1.0),
                ('all_bounds', base_rows(root, profile, impute(root, profile, all_bounds=True))[0], 1.0),
                ('ledger_echelon_joint', base_rows(root, profile, impute(root, profile, joint_ledger_echelon=True))[0], 1.0)]
    by_set = {'primary': primary_by_m}
    for name, vrows, sd in mi_specs:
        by_set[name] = [slim(with_x(vrows, profile, s)) for s in imputations(vrows, profile, m, sd_scale=sd)]
    sets = {name: (by_m, {'tau': tau_r},
                   ranked_sets(by_m[0], sorted({r[s] for r in by_m[0] for s in SLOTS if r[s]}), side_of, sides)[1])
            for name, by_m in by_set.items()}
    pooled_tasks = [(name, mi) for name in sets for mi in range(m)]
    median_rows = with_x(rows, profile, None)
    specs = [('median_imputation', median_rows, False, {})]

    def view(name, vrows, robustness=False, **params):
        specs.append((name, vrows, robustness, params))
    view('tau_half', median_rows, True, tau=tau_r / 2)
    view('tau_double', median_rows, True, tau=tau_r * 2)
    view('kappa_0.25', median_rows, True, kappa=0.25)
    view('kappa_1.0', median_rows, True, kappa=1.0)
    view('alpha_sd_3', median_rows, True, alpha_sd=3.0)
    view('grades_ab', with_x(rows, profile, None, 'grades_ab'), True)
    view('superior_directing', with_x(rows, profile, None, 'superior'), True)
    view('command_changed_excluded', [r for r in median_rows if not any('command_changed' in r['sides'][s]['labels'] for s in sides)], True)
    view('command_changed_successor', with_x(rows, profile, None, 'successor'), True)
    view('joint_command_credited', with_x(rows, profile, None, credit_joint=True), True)
    for ea, eb in product(('low', 'high'), repeat=2):
        view(f'endpoint_{sides[0]}_{ea}_{sides[1]}_{eb}', with_x(rows, profile, None, ends=(ea, eb)), True)
    for r in rows:
        for s in sides:
            for cand in r['sides'][s]['candidates']:
                if cand != r['sides'][s]['commander_id']:
                    view(f'alternative_{r["battle_id"]}_{s}_{cand}', with_x(rows, profile, None, alt=(r['battle_id'], s, cand)), True)
    view('tau_convention_0.5', median_rows, tau=TAU)
    view('no_context', median_rows, use_context=False)
    view('strength_graded_only', [r for r in median_rows if r['graded_row']])
    view('no_post_start_rows', [r for r in median_rows if 'post_start_in_ledger' not in r['labels']])
    view('no_bound_conflict', [r for r in median_rows if 'bound_conflict' not in r['labels']])
    view('no_naval_grade_e', [r for r in median_rows if 'naval_side' not in r['labels']])
    view('drop_nesting_unresolved', [r for r in median_rows if r['battle_id'] not in unresolved])
    view('outcome_only_all', median_rows, use_force=False)
    single_items = [(slim(vrows), {'tau': tau_r, **params}) for _, vrows, _, params in specs]
    out2 = pmap(_phase2, [('pooled', t) for t in pooled_tasks] + [('single', i) for i in single_items],
                shared={'sets': sets, 'single': (side_of, sides)})
    pooled_res, singles = out2[:len(pooled_tasks)], out2[len(pooled_tasks):]
    pooled_sets = {}
    for name in sets:
        res = [pooled_res[k] for k, (n_, _) in enumerate(pooled_tasks) if n_ == name]
        pooled_sets[name] = pooled(res, sets[name][0][0], side_of, sides, tau_r)
    primary = pooled_sets['primary']
    views, robust = {}, []
    for (name, vrows, robustness, params), res in zip(specs, singles):
        views[name] = {'rows': len(vrows), 'params': {'tau': tau_r, **params}, 'robustness': robustness, **res}
        if robustness:
            robust.append(name)
    for name, vrows, sd in mi_specs:
        views[name] = {'rows': len(vrows), 'params': {'tau': tau_r, 'sd_scale': sd}, 'robustness': False,
                       'multiple_imputation': True, **pooled_sets[name]}

    # Per commander.
    ref = views['median_imputation']['ratings']
    p_ctx = {p['battle_id']: p['context'] for p in preds}
    labels_of = {r['battle_id']: r['labels'] for r in rows}
    attributed = attributions(root, profile)
    table_for = sorted(c for c, v in primary['ratings'].items() if v['battles_modelled'] >= 2)
    out = {}
    for c, pr in primary['ratings'].items():
        sens, unranked = [], []
        base_ref = ref.get(c)
        if pr['battles_modelled'] >= 2 and base_ref:
            for name in robust:
                v = views[name]['ratings'].get(c)
                if v is None or not v['ranked']:
                    unranked.append(name)
                if v is None:
                    continue
                opposite = ((v['interval_80'][0] > 0 and base_ref['theta'] < 0)
                            or (v['interval_80'][1] < 0 and base_ref['theta'] > 0))
                disjoint = (v['ranked'] and base_ref['ranked']
                            and (v['rank_80'][1] < base_ref['rank_80'][0] or v['rank_80'][0] > base_ref['rank_80'][1]))
                if opposite or disjoint:
                    sens.append(name)
        rows_c = [(r, slot) for r in base for slot in SLOTS if r[slot] == c]
        wins = sum((r['y'] == 1) == (slot == 'a') for r, slot in rows_c)
        labels = list(pr['labels']) + ([] if decision['improved'] else ['no_heldout_signal'])
        out[c] = {'name': names[c], 'side': side_of[c], **pr, 'labels': labels,
                  'battles_attributed': len(attributed[c]),
                  'dropped_as_nested': sorted(b for b, _, _ in attributed[c] if b in nested),
                  'joint_command_not_credited': sorted(b for b, _, j in attributed[c] if j and b not in nested),
                  'wins_in_model': wins, 'losses_in_model': len(rows_c) - wins,
                  'modelled_strength_rows': sum('modelled_strength' in labels_of[r['battle_id']] for r, _ in rows_c),
                  'residual_sum_vs_context': math.fsum((r['y'] - p_ctx[r['battle_id']]) * (1 if slot == 'a' else -1)
                                                       for r, slot in rows_c),
                  'view_sensitive': sens, 'unranked_in_view': unranked}
    for c in sorted(set(attributed) - set(out)):  # credited only on battles outside the model
        out[c] = {'name': names[c], 'side': side_of[c], 'ranked': False, 'battles_modelled': 0,
                  'battles_attributed': len(attributed[c]),
                  'dropped_as_nested': sorted(b for b, _, _ in attributed[c] if b in nested),
                  'joint_command_not_credited': sorted(b for b, _, j in attributed[c] if j and b not in nested),
                  'labels': ['coverage_only']}
    view_table = {name: {c: [v['ratings'][c]['theta'], *v['ratings'][c]['interval_80'],
                             *(v['ratings'][c]['rank_80'] if v['ratings'][c]['ranked'] else [None, None])]
                         for c in table_for if c in v['ratings']} for name, v in views.items()}
    rows_meta = {'rows': len(rows), 'campaigns': len(camps),
                 'rows_with_modelled_strength': sum('modelled_strength' in r['labels'] for r in rows),
                 'rows_post_start_in_ledger': sum('post_start_in_ledger' in r['labels'] for r in rows),
                 'rows_post_start_modelled': sum('post_start_modelled' in r['labels'] for r in rows),
                 'rows_joint_command': sum('joint_command' in r['labels'] for r in rows),
                 'dropped_as_nested': nested, 'nesting_unresolved': unresolved}
    return {'model': {'tau_ratings': tau_r, 'tau_basis': tau_basis, 'tau_convention': TAU, 'kappa': KAPPA,
                      'alpha_sd': 1.0, 'beta_sd': 1.0, 'tau_grid': list(TAU_GRID), 'imputations': m, 'seed': SEED,
                      'rank_seed': RANK_SEED, 'draws_per_imputation': DRAWS_PER, 'bootstrap_seed': BOOTSTRAP_SEED,
                      'resamples': RESAMPLES, 'alpha_pooled': primary['alpha'], 'beta_pooled': primary['beta'],
                      'context_pooled': primary['context'], **rows_meta},
            'verdict': {**decision, 'comparison': main},
            'heldout': {'models': list(MODELS), **score(preds, MODELS),
                        'comparisons': {f'{a}_minus_{b}': compare(preds, a, b) for a, b in
                                        (('commander_tau_0.5', 'context'), ('commander_no_context', 'strength_only'),
                                         ('context', 'strength_only'), ('commander', 'strength_only'))},
                        'without_leakage_rows_no_refit': {'rows_kept': len(leak_free), 'battle_weighted': lf['battle_weighted'],
                                                          'campaign_weighted': lf['campaign_weighted'],
                                                          'q95': {w: lf['bootstrap'][w]['q0.95'] for w in ('battle_weighted', 'campaign_weighted')}},
                        'monte_carlo_check': halves, 'effective_rows': effective, 'n_rows': len(preds),
                        'fold_tau_hat': fold_tau, 'fold_tau_hat_counts': dict(sorted(Counter(str(t['tau_hat']) for t in fold_tau).items())),
                        'concentration_no_refit': concentration(preds, credited, names),
                        'predictions': preds},
            'bridge_run3_configuration': {'description': 'v3 ledger; post-start sides at their ledger estimates; rule-5 '
                                                         'commanders credited; no context; tau 0.5 (run 3 settings)',
                                          'grade_e_sides': len(bridge_imp['sides']), 'rows': len(bpreds),
                                          **score(bpreds, ('commander', 'strength_only')),
                                          'commander_minus_strength_only': compare(bpreds, 'commander', 'strength_only')},
            'tau_profile': {'all_rows': tau_all, 'temporal_training_rows': split_ev},
            'temporal_split': temporal, 'commanders': out,
            'views': {n: {k: v for k, v in x.items() if k not in {'ratings'}} for n, x in views.items()},
            'view_table': {'columns': ['theta', 'interval_80_low', 'interval_80_high', 'rank_80_low', 'rank_80_high'],
                           'commanders': 'every commander with two or more modelled battles in the primary fit',
                           'views': view_table},
            'robustness_views': robust, 'flags': FLAGS + ['modelled_strength']}


def _phase2(task, shared):
    kind, item = task
    if kind == 'pooled':
        return _pooled_task(item, shared)
    return _single_task(item, shared['single'])


def report_text(result):
    """Markdown summary, verdict first; without an improvement it gives no ordered ranking."""
    v, h, mo = result['verdict'], result['heldout'], result['model']
    cmp_, bs = v['comparison'], v['comparison']['bootstrap']
    f4 = lambda x: f'{x:+.4f}'
    ll = lambda w, k: f"{h[w][k]['log_loss']:.4f}"
    sides = sorted({c['side'] for c in result['commanders'].values()}, key=lambda s: s != 'US')
    names = {'commander': 'Commander + context (τ estimated in each fold)', 'context': 'Context only',
             'commander_tau_0.5': 'Commander + context (τ = 0.5)', 'commander_no_context': 'Commander, no context (τ = 0.5)',
             'strength_only': 'Strength only'}
    lines = ['# Commander residual ratings, run 4 (diagnostic)', '',
             '**A residual rating is not command skill, a causal effect or a ranking of record.** It summarises how a '
             "commander's battles went relative to what force size and the theater and period predict, pulled towards "
             'zero, relative to their own side.', '',
             f"Rows: {mo['rows']} battles in {mo['campaigns']} campaigns; {mo['rows_with_modelled_strength']} with a modelled "
             f"(grade E) side, of which {mo['rows_post_start_modelled']} because their only figures were post-start; "
             f"{mo['rows_joint_command']} with a joint-command side, which gets no commander term. "
             f"{mo['imputations']} imputations. Every result carries {', '.join('`' + x + '`' for x in result['flags'])}.", '',
             '## The verdict (pre-registered)', '',
             f"Rule: {v['rule']}.", '',
             '| Model | Log loss, battle-weighted | Log loss, campaign-weighted |', '|---|---:|---:|']
    for k in h['models']:
        lines.append(f"| {names[k]} | {ll('battle_weighted', k)} | {ll('campaign_weighted', k)} |")
    lines += ['', '| Commander minus context | Difference | 95th percentile (the rule) | 95% interval | Resamples ≥ 0 |',
              '|---|---:|---:|---:|---:|']
    for w, label in (('battle_weighted', 'Battle-weighted'), ('campaign_weighted', 'Campaign-weighted')):
        lines.append(f"| {label} | {f4(cmp_[w])} | {f4(bs[w]['q0.95'])} | {f4(bs[w]['q0.025'])} to {f4(bs[w]['q0.975'])} | "
                     f"{bs[w]['share_at_or_above_zero']:.1%} |")
    lines += ['', ('**Improvement under the pre-registered rule.** Held-out log loss was lower than the context model\'s, '
                   'with the campaign bootstrap\'s 95th percentile below zero under both weightings. This is not evidence of '
                   'a persistent commander effect or of skill.') if v['improved'] else
              ('**No improvement under the pre-registered rule: commander identity adds no detectable predictive signal '
               'beyond force size and context in these data. No ordered ranking is given.** The JSON keeps every '
               'estimate, labelled `no_heldout_signal`.'), '']
    s = cmp_['sign_test']
    mc = h['monte_carlo_check']
    lines += [f"Descriptive, not part of the verdict: the commander model did better in {s['first_better']} campaigns and "
              f"worse in {s['second_better']} (ties {s['ties']}; exact two-sided sign-test p = {s['two_sided_p']:.3f}); "
              f"{len(h['effective_rows'])} of {h['n_rows']} held-out rows had a commander seen in another campaign; "
              'Monte Carlo check of the difference: ' + '; '.join(
                  f"{k.replace('imputations_', 'imputations ').replace('_', '–')}: {f4(x['battle_weighted'])} battle, "
                  f"{f4(x['campaign_weighted'])} campaign" for k, x in mc.items()) + '.', '',
              '## Other held-out comparisons (descriptive)', '',
              '| Comparison | Battle-weighted | Campaign-weighted | 95% interval, battle | 95% interval, campaign |',
              '|---|---:|---:|---:|---:|']
    for c in h['comparisons'].values():
        b2 = c['bootstrap']
        lines.append(f"| {names[c['first']]} − {names[c['second']]} | {f4(c['battle_weighted'])} | {f4(c['campaign_weighted'])} | "
                     f"{f4(b2['battle_weighted']['q0.025'])} to {f4(b2['battle_weighted']['q0.975'])} | "
                     f"{f4(b2['campaign_weighted']['q0.025'])} to {f4(b2['campaign_weighted']['q0.975'])} |")
    br = result['bridge_run3_configuration']['commander_minus_strength_only']
    lf = h['without_leakage_rows_no_refit']
    lines.append(f"| Bridge: run 3's configuration on the v3 ledger, commander − strength only | {f4(br['battle_weighted'])} | "
                 f"{f4(br['campaign_weighted'])} | {f4(br['bootstrap']['battle_weighted']['q0.025'])} to "
                 f"{f4(br['bootstrap']['battle_weighted']['q0.975'])} | {f4(br['bootstrap']['campaign_weighted']['q0.025'])} to "
                 f"{f4(br['bootstrap']['campaign_weighted']['q0.975'])} |")
    lines += ['', f"Without the rows that had a post-start side or a joint-command side ({lf['rows_kept']} kept; stored "
              f"predictions, no refit), commander minus context is {f4(lf['battle_weighted'])} battle-weighted and "
              f"{f4(lf['campaign_weighted'])} campaign-weighted (95th percentiles {f4(lf['q95']['battle_weighted'])} and "
              f"{f4(lf['q95']['campaign_weighted'])}).", '']
    con = h['concentration_no_refit']
    if 'without_top_contributor' in con:
        t = con['without_top_contributor']
        lines += [f"Concentration (no refit): the net gain over all rows is {con['total_net_gain']:.3f}; "
                  f"{con['top_contributors'][0]['name']}'s {con['top_contributors'][0]['rows']} rows carry "
                  f"{con['top_contributors'][0]['net_gain']:.3f}. Without them, commander minus context is "
                  f"{f4(t['battle_weighted'])} battle-weighted and {f4(t['campaign_weighted'])} campaign-weighted "
                  f"(95th percentiles {f4(t['q95']['battle_weighted'])} and {f4(t['q95']['campaign_weighted'])}).", '']
    ta = result['tau_profile']['all_rows']
    lines += ['## How much do commanders differ? (τ, descriptive)', '',
              f"On all rows, the Laplace marginal likelihood (mean over imputations) peaks at τ = {ta['tau_hat']} on the grid "
              f"{', '.join(str(x) for x in ta['grid'])}; grid values within {CHI2_95_HALF} log units of the peak run from "
              f"{ta['profile_interval_95'][0]} to {ta['profile_interval_95'][1]} (an approximate 95% profile interval; "
              f"{'it includes' if ta['zero_inside_interval'] else 'it excludes'} τ = 0, no commander spread). "
              f"In the held-out folds, τ-hat was {', '.join(f'{k} in {n}' for k, n in h['fold_tau_hat_counts'].items())} of "
              f"{len(h['fold_tau_hat'])} folds. Ratings below use τ = {mo['tau_ratings']} ({mo['tau_basis'].replace('_', ' ')}).", '',
              f"Calibration: with outcomes simulated {ta['calibration']['simulations']} times from the context model (no commander "
              f"differences; first {ta['calibration']['imputations_used']} imputations), the largest log-evidence gain over the "
              f"grid had median {ta['calibration']['simulated_quantiles']['q0.5']:.2f} and 95th percentile "
              f"{ta['calibration']['simulated_quantiles']['q0.95']:.2f}; the observed gain on the same imputations is "
              f"{ta['calibration']['observed']:.2f} (p = {ta['calibration']['p_value']:.3f}).", '',
              '| τ | Log evidence minus context model |', '|---:|---:|']
    for t, x in ta['log_evidence_minus_context'].items():
        lines.append(f'| {t} | {x:+.2f} |')
    ts = result['temporal_split']
    if ts['evaluable']:
        lines += ['', f"Descriptive {ts['years'][0][0]}–{ts['years'][0][-1]}→{ts['years'][1][0]}–{ts['years'][1][-1]} split (no "
                  f"verdict): trained on {ts['n_train']}, tested on {ts['n_test']}, τ-hat {ts['tau_hat_train']} on the training "
                  'years; log loss ' + ', '.join(f"{names[k].lower()} {ts['battle_weighted'][k]['log_loss']:.4f}" for k in h['models'])
                  + '.']
    lines += ['']
    for side in sides:
        cs = [c for c in result['commanders'].values() if c['side'] == side and c.get('ranked')]
        cs.sort(key=(lambda c: (c['rank_median'], -c['theta'])) if v['improved'] else (lambda c: c['name']))
        lines += [f"## {side} commanders with two or more modelled battles" + ('' if v['improved'] else ' (alphabetical)'), '',
                  '| Commander | Battles | Modelled-strength rows | W–L | Pooled θ | 80% interval | 95% interval | Rank 80% | SD ratio | Labels |',
                  '|---|---:|---:|---:|---:|---:|---:|---:|---:|---|']
        for c in cs:
            labels = sorted(set(c.get('labels', [])) | ({'view_sensitive'} if c.get('view_sensitive') else set()))
            lines.append(f"| {c['name']} | {c['battles_modelled']} | {c['modelled_strength_rows']} | {c['wins_in_model']}–{c['losses_in_model']} | "
                         f"{c['theta']:+.2f} | {c['interval_80'][0]:+.2f} to {c['interval_80'][1]:+.2f} | "
                         f"{c['interval_95'][0]:+.2f} to {c['interval_95'][1]:+.2f} | {c['rank_80'][0]}–{c['rank_80'][1]} | "
                         f"{c['posterior_prior_sd_ratio']:.2f} | {', '.join(labels)} |")
        lines.append('')
    lines += ['Views, the per-view table, every held-out prediction and the per-fold τ are in the JSON. Commanders with one '
              'modelled battle are there with their estimate, which is almost entirely the prior.', '']
    return '\n'.join(lines)
