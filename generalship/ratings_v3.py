"""Commander residual ratings, run 3: all battles with grade E strengths (docs/strength-imputation.md §§3–7).

The rating model, priors, attribution and Laplace approximation are those of `ratings.py`, unchanged.
Grade E uncertainty is carried by multiple imputation; the held-out test on all in-scope battles is the
single verdict. The run is refused unless an owner authorization names the exact files; outputs never
enter artifacts/baseline.json.
"""

from collections import Counter, defaultdict
from itertools import product
import math
import random

from .baseline import advantage, fit_logistic, scores
from .command import check as check_command
from .estimates import SIDES
from .estimates_v2 import check as check_strength
from .imputation import (BATTLES, CAMPAIGNS, COMMAND, DESIGN, STRENGTH, build as build_imputation, impute, quantile)
from .ratings import TAU, RatingError, attach, cholesky, components, fit, predict, summarize
from .sources import digest, read_csv, read_json, safe_path

AUTHORIZATION = 'data/command/rating-authorization-v3.json'
IMPUTATION = 'artifacts/strength-imputation-v1.json'
REGISTRY = 'data/command/commanders-v2.json'
RUN2 = 'artifacts/commander-ratings-v2.json'
M = 20
SEED = 20260926
DRAWS_PER = 1000
RANK_SEED = 20260925
FLAGS = ['whole_engagement_leakage', 'conditional_on_source_availability', 'not_causal', 'side_relative']
BOUND_FILES = {'design': DESIGN, 'imputation': IMPUTATION, 'strength_ledger': STRENGTH, 'command_ledger': COMMAND,
               'registry': REGISTRY, 'campaigns': CAMPAIGNS}


def authorize(root, path=AUTHORIZATION):
    auth = read_json(safe_path(root, path))
    if auth.get('kind') != 'commander_rating_authorization':
        raise RatingError('Authorization record kind')
    for key, p in BOUND_FILES.items():
        b = auth.get(key)
        if not isinstance(b, dict) or b.get('path') != p or b.get('sha256') != digest(safe_path(root, p)):
            raise RatingError(f'Authorization names a different {key}; no fit runs')
    if auth.get('admits_feature') is not False or auth.get('changes_baseline') is not False:
        raise RatingError('A rating run admits no feature and leaves the baseline unchanged')
    return auth


# ---------- rows and imputations ----------

def base_rows(root, imputation):
    """The 301 all-battles rows (§3) with each side's strength specification."""
    strength = read_json(safe_path(root, STRENGTH))
    command = read_json(safe_path(root, COMMAND))
    battles = {r['battle']: r for r in read_csv(safe_path(root, BATTLES))}
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
        for s in SIDES:
            est = e['sides'][s]['estimate']
            if est['grade'] == 'D':
                g = grade_e[(b, s)]
                spec[s] = {'grade': 'E', **{k: g[k] for k in ('mu_log', 'sd_log', 'lower_bound', 'upper_bound', 'fixed',
                                                             'point', 'low', 'high', 'labels')}}
                labels.add('modelled_strength')
                labels |= {l for l in g['labels'] if l in {'bound_conflict', 'naval_side'}}
            else:
                spec[s] = {'grade': est['grade'], 'point': est['point'], 'low': est['low'], 'high': est['high']}
                if 'post_start_information' in est['labels']:
                    labels.add('post_start_information')
        rows.append({'battle_id': b, 'campaign': battles[b]['campaign'], 'year': battles[b]['start_date'][:4],
                     'y': int(battles[b]['result'] == 'Union'), 'sides': cmd[b]['sides'], 'spec': spec,
                     'labels': sorted(labels),
                     'graded_row': all(spec[s]['grade'] in 'ABC' for s in SIDES) and 'post_start_information' not in labels})
    return rows, sorted(nested), unresolved


def e_value(spec, u, sd_scale=1.0):
    if spec['fixed'] is not None:
        return spec['fixed']
    return quantile(spec['mu_log'], spec['sd_log'] * sd_scale, u, spec['lower_bound'], spec['upper_bound'])


def imputations(rows, m=M, seed=SEED, sd_scale=1.0):
    """M imputed strength sets, drawn in the declared order (§5)."""
    order = sorted((r['battle_id'], SIDES.index(s)) for r in rows for s in SIDES if r['spec'][s]['grade'] == 'E')
    by = {r['battle_id']: r for r in rows}
    rng = random.Random(seed)
    out = []
    for _ in range(m):
        vals = {}
        for b, i in order:
            s = SIDES[i]
            vals[(b, s)] = e_value(by[b]['spec'][s], rng.random(), sd_scale)
        out.append(vals)
    return out


def with_x(rows, strengths, view=None, alt=None, ends=None):
    """Rows with x from one strength set; ends picks ledger low/high and grade E 10th/90th percentiles."""
    out = []
    for r in rows:
        v = []
        for k, s in enumerate(SIDES):
            spec = r['spec'][s]
            if ends:
                v.append(spec[ends[k]])
            elif spec['grade'] == 'E':
                v.append(strengths[(r['battle_id'], s)] if strengths is not None else spec['point'])
            else:
                v.append(spec['point'])
        out.append({**r, 'x': advantage(v[0], v[1])})
    return attach(out, view, alt)


# ---------- pooled estimates ----------

def pooled(rows_by_m, side_of, tau=TAU, alpha_sd=1.0, use_force=True):
    """Pooled point estimates, intervals and ranks over imputations (§5 Estimates).

    Each imputation contributes DRAWS_PER draws: marginal normal draws per commander for the intervals,
    and joint Laplace draws over the ranked commanders for the within-side ranks.
    """
    battles = Counter(r[s] for r in rows_by_m[0] for s in ('us', 'cs') if r[s])
    ranked = {side: sorted(c for c in battles if side_of[c] == side and battles[c] >= 2) for side in SIDES}
    rng = random.Random(RANK_SEED)
    draws, modes, alphas, betas, ranks = defaultdict(list), defaultdict(list), [], [], defaultdict(list)
    for rows in rows_by_m:
        model = fit(rows, tau=tau, alpha_sd=alpha_sd, use_force=use_force)
        alphas.append(model['alpha'])
        betas.append(model['beta'])
        for c in model['commanders']:
            modes[c].append(model['theta'][c])
            draws[c] += [rng.gauss(model['theta'][c], model['sd'][c]) for _ in range(DRAWS_PER)]
        rc = [c for side in ranked.values() for c in side]
        idx = [model['index'][c] for c in rc]
        sub = [[model['cov'][i][j] for j in idx] for i in idx]
        low = cholesky([[sub[i][j] + (1e-12 if i == j else 0.0) for j in range(len(idx))] for i in range(len(idx))])
        mode = [model['mode'][i] for i in idx]
        pos = {c: k for k, c in enumerate(rc)}
        for _ in range(DRAWS_PER):
            e = [rng.gauss(0, 1) for _ in idx]
            v = [mode[i] + sum(low[i][k] * e[k] for k in range(i + 1)) for i in range(len(idx))]
            for side in ranked.values():
                for r_, c in enumerate(sorted(side, key=lambda c: -v[pos[c]]), 1):
                    ranks[c].append(r_)

    def q(xs, p):
        xs = sorted(xs)
        return xs[min(len(xs) - 1, max(0, int(math.floor(p * len(xs)))))]
    comp = components(rows_by_m[0])
    out = {}
    for c in modes:
        d = draws[c]
        mean_d = sum(d) / len(d)
        sd = math.sqrt(sum((x - mean_d) ** 2 for x in d) / (len(d) - 1))
        is_ranked = c in ranked.get(side_of[c], [])
        same = [o for o in ranked.get(side_of[c], []) if o != c and comp.get(o) == comp.get(c)]
        out[c] = {'battles_modelled': battles[c], 'theta_pooled': sum(modes[c]) / len(modes[c]), 'sd_pooled': sd,
                  'interval_80': [q(d, 0.1), q(d, 0.9)], 'interval_95': [q(d, 0.025), q(d, 0.975)],
                  'component': comp.get(c), 'ranked': is_ranked,
                  **({'rank_median': q(ranks[c], 0.5), 'rank_80': [q(ranks[c], 0.1), q(ranks[c], 0.9)],
                      'rank_95': [q(ranks[c], 0.025), q(ranks[c], 0.975)]} if is_ranked else {}),
                  'labels': (['not_connected'] if is_ranked and not same else [])}
    return {'alpha': sum(alphas) / len(alphas), 'beta': sum(betas) / len(betas), 'ratings': out}


def single(rows, side_of, **params):
    """One fit summarized exactly as run 2 does (analytic intervals, 20,000 rank draws)."""
    model = fit(rows, **params)
    out = summarize(rows, model, side_of)
    for v in out.values():
        v['theta_pooled'], v['sd_pooled'] = v['theta_mode'], v['sd']
    return {'alpha': model['alpha'], 'beta': model['beta'], 'ratings': out}


# ---------- held-out verdict ----------

def heldout(rows_by_m):
    """Leave one campaign out; probabilities averaged over imputations, then scored (§5)."""
    base = rows_by_m[0]
    camps = sorted({r['campaign'] for r in base})
    probs = defaultdict(lambda: {'commander_model': [], 'strength_only': []})
    effective = []
    for camp in camps:
        for mi, rows in enumerate(rows_by_m):
            train = [r for r in rows if r['campaign'] != camp]
            test = [r for r in rows if r['campaign'] == camp]
            model = fit(train)
            logit = fit_logistic([r['x'] for r in train], [r['y'] for r in train])
            for r in test:
                probs[r['battle_id']]['commander_model'].append(predict(model, r))
                probs[r['battle_id']]['strength_only'].append(logit.predict(r['x']))
            if mi == 0:
                seen = set(model['theta'])
                effective += [{'battle_id': r['battle_id'], 'commanders': [c for c in (r['us'], r['cs']) if c in seen]}
                              for r in test if any(c in seen for c in (r['us'], r['cs']) if c)]
    preds = [{'battle_id': r['battle_id'], 'campaign': r['campaign'], 'union_outcome': r['y'],
              'commander_model': sum(probs[r['battle_id']]['commander_model']) / len(rows_by_m),
              'strength_only': sum(probs[r['battle_id']]['strength_only']) / len(rows_by_m),
              'per_imputation': probs[r['battle_id']]} for r in base]
    result = score(preds)
    # Monte Carlo check (descriptive): imputations 1-10 and 11-20
    halves = {}
    for name, sl in (('imputations_1_10', slice(0, len(rows_by_m) // 2)), ('imputations_11_20', slice(len(rows_by_m) // 2, None))):
        ps = [{**p, 'commander_model': mean(p['per_imputation']['commander_model'][sl]),
               'strength_only': mean(p['per_imputation']['strength_only'][sl])} for p in preds]
        s = score(ps)
        halves[name] = {w: s[w]['commander_model']['log_loss'] - s[w]['strength_only']['log_loss']
                        for w in ('battle_weighted', 'campaign_weighted')}
    for p in preds:
        del p['per_imputation']
    return {**result, 'effective_rows': effective, 'n_rows': len(preds), 'predictions': preds,
            'monte_carlo_check': halves}


def mean(xs):
    return sum(xs) / len(xs)


def score(preds):
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
    return {'improved': improved, 'battle_weighted': battle, 'campaign_weighted': campaign, 'campaigns_better': dict(wins)}


def temporal(rows_by_m, years=(('1861', '1862', '1863'), ('1864', '1865'))):
    preds = defaultdict(lambda: [[], []])
    for rows in rows_by_m:
        train = [r for r in rows if r['year'] in years[0]]
        test = [r for r in rows if r['year'] in years[1]]
        model = fit(train)
        logit = fit_logistic([r['x'] for r in train], [r['y'] for r in train])
        for r in test:
            preds[r['battle_id']][0].append(predict(model, r))
            preds[r['battle_id']][1].append(logit.predict(r['x']))
    ys = {r['battle_id']: r['y'] for r in rows_by_m[0]}
    ps = [{'union_outcome': ys[b], 'commander_model': mean(a), 'strength_only': mean(c)} for b, (a, c) in preds.items()]
    return {'evaluable': True, 'verdict': None, 'years': years, 'n_train': sum(r['year'] in years[0] for r in rows_by_m[0]),
            'n_test': len(ps), 'commander_model': scores(ps, 'commander_model'), 'strength_only': scores(ps, 'strength_only')}


# ---------- the run ----------

def rate3(root, m=M):
    auth = authorize(root)
    check_strength(root, STRENGTH)
    check_command(root, COMMAND)
    stored = read_json(safe_path(root, IMPUTATION))
    rebuilt = build_imputation(root, verify=False)
    if rebuilt != stored:
        raise RatingError('The imputation output does not reproduce from the reviewed ledgers')
    registry = {c['id']: c for c in read_json(safe_path(root, REGISTRY))['commanders']}
    side_of = {c: registry[c]['side'] for c in registry}
    rows, nested, unresolved = base_rows(root, stored)
    imps = imputations(rows, m)
    primary_by_m = [with_x(rows, s) for s in imps]
    test = heldout(primary_by_m)
    primary = pooled(primary_by_m, side_of)
    median_rows = with_x(rows, None)
    views = {'median_imputation': {'rows': len(median_rows), **single(median_rows, side_of)}}
    robust = []

    def view(name, vrows, robustness=False, **params):
        views[name] = {'rows': len(vrows), 'params': params, **single(vrows, side_of, **params)}
        if robustness:
            robust.append(name)
    view('tau_0.25', median_rows, True, tau=0.25)
    view('tau_1.0', median_rows, True, tau=1.0)
    view('alpha_sd_3', median_rows, True, alpha_sd=3.0)
    view('grades_ab', with_x(rows, None, 'grades_ab'), True)
    view('superior_directing', with_x(rows, None, 'superior'), True)
    view('command_changed_excluded', [r for r in median_rows if not any('command_changed' in r['sides'][s]['labels'] for s in SIDES)], True)
    view('command_changed_successor', with_x(rows, None, 'successor'), True)
    for us_end, cs_end in product(('low', 'high'), repeat=2):
        view(f'endpoint_us_{us_end}_cs_{cs_end}', with_x(rows, None, ends=(us_end, cs_end)), True)
    for r in rows:
        for s in SIDES:
            for cand in r['sides'][s]['candidates']:
                if cand != r['sides'][s]['commander_id']:
                    view(f'alternative_{r["battle_id"]}_{s}_{cand}', with_x(rows, None, alt=(r['battle_id'], s, cand)), True)
    graded = [r for r in median_rows if r['graded_row']]
    view('strength_graded_only', graded)
    run2 = read_json(safe_path(root, RUN2))
    diffs = [abs(views['strength_graded_only']['ratings'][c]['theta_pooled'] - v['theta_mode'])
             for c, v in run2['commanders'].items() if 'theta_mode' in v and c in views['strength_graded_only']['ratings']]
    views['strength_graded_only']['reproduces_run2'] = {'max_abs_theta_difference': max(diffs), 'reproduces': max(diffs) < 1e-9,
                                                        'rows_run2': run2['model']['rows']}
    view('no_post_start', [r for r in median_rows if 'post_start_information' not in r['labels']])
    view('no_bound_conflict', [r for r in median_rows if 'bound_conflict' not in r['labels']])
    view('no_naval_grade_e', [r for r in median_rows if 'naval_side' not in r['labels']])
    view('drop_nesting_unresolved', [r for r in median_rows if r['battle_id'] not in unresolved])
    view('outcome_only_all', median_rows, use_force=False)

    def mi_view(name, imputation=None, sd_scale=1.0):
        vrows = rows if imputation is None else base_rows(root, imputation)[0]
        by_m = [with_x(vrows, s) for s in imputations(vrows, m, sd_scale=sd_scale)]
        views[name] = {'rows': len(vrows), 'multiple_imputation': True, **pooled(by_m, side_of)}
    mi_view('wide_imputation', sd_scale=2.0)
    mi_view('train_graded_ab', impute(root, train_grades='AB', verify=False))
    mi_view('all_bounds', impute(root, all_bounds=True, verify=False))
    mi_view('ledger_echelon_joint', impute(root, joint_ledger_echelon=True, verify=False))
    ref = views['median_imputation']['ratings']
    out = {}
    p_by = {p['battle_id']: p['strength_only'] for p in test['predictions']}
    attributed = defaultdict(list)
    for r in rows:
        for s in SIDES:
            if r['sides'][s]['commander_id']:
                attributed[r['sides'][s]['commander_id']].append((r['battle_id'], s, r['sides'][s]))
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
                opposite = (v['interval_80'][0] > 0 and base_ref['theta_pooled'] < 0) or (v['interval_80'][1] < 0 and base_ref['theta_pooled'] > 0)
                disjoint = v['ranked'] and base_ref['ranked'] and (v['rank_80'][1] < base_ref['rank_80'][0] or v['rank_80'][0] > base_ref['rank_80'][1])
                if opposite or disjoint:
                    sens.append(name)
        rows_c = [(r, s) for r in primary_by_m[0] for s, k in (('US', 'us'), ('Confederate', 'cs')) if r[k] == c]
        wins = sum((r['y'] == 1) == (s == 'US') for r, s in rows_c)
        labels = list(pr['labels'])
        if not test['improved']:
            labels.append('no_heldout_signal')
        out[c] = {'name': registry[c]['name'], 'side': side_of[c], **pr, 'labels': labels,
                  'battles_attributed': len(attributed[c]), 'wins_in_model': wins, 'losses_in_model': len(rows_c) - wins,
                  'modelled_strength_rows': sum('modelled_strength' in r['labels'] for r, _ in rows_c),
                  'raw_residual_sum': sum((r['y'] - p_by[r['battle_id']]) * (1 if s == 'US' else -1) for r, s in rows_c),
                  'view_sensitive': sens, 'unranked_in_view': unranked,
                  'posterior_prior_sd_ratio': pr['sd_pooled'] / TAU,
                  'views': {n: (dict(v['ratings'][c], theta_minus_primary=v['ratings'][c]['theta_pooled'] - pr['theta_pooled'])
                                if c in v['ratings'] else None) for n, v in views.items()}}
    return {'kind': 'commander_residual_ratings', 'run_version': 3,
            'status': 'exploratory_diagnostic_not_skill_not_ranking_of_record',
            'authorization': {'path': AUTHORIZATION, 'sha256': digest(safe_path(root, AUTHORIZATION)),
                              'decision_date': auth['decision_date']},
            'bindings': {k: {'path': p, 'sha256': digest(safe_path(root, p))} for k, p in BOUND_FILES.items()},
            'model': {'tau': TAU, 'alpha_sd': 1.0, 'beta_sd': 1.0, 'alpha_pooled': primary['alpha'], 'beta_pooled': primary['beta'],
                      'imputations': m, 'seed': SEED, 'draws_per_imputation': DRAWS_PER, 'rank_seed': RANK_SEED,
                      'rows': len(rows), 'campaigns': len({r['campaign'] for r in rows}),
                      'rows_with_modelled_strength': sum('modelled_strength' in r['labels'] for r in rows),
                      'rows_post_start': sum('post_start_information' in r['labels'] for r in rows),
                      'dropped_as_nested': nested, 'nesting_unresolved': unresolved},
            'heldout_test': test, 'temporal_split': temporal(primary_by_m), 'commanders': out,
            'views': {n: {k: v for k, v in x.items() if k != 'ratings'} for n, x in views.items()},
            'robustness_views': robust, 'flags': FLAGS + ['modelled_strength']}


def report_text(result):
    """Markdown summary; without a held-out improvement it gives no ordered ranking."""
    t, mo = result['heldout_test'], result['model']
    f = lambda x: f"{x['log_loss']:.4f}"
    lines = ['# Commander residual ratings, run 3: all battles (diagnostic)', '',
             '**A residual rating is not command skill, a causal effect or a ranking of record.** It summarises how a '
             "commander's battles went relative to what force size predicts, pulled towards zero, relative to their own side.", '',
             f"Rows: {mo['rows']} battles in {mo['campaigns']} campaigns, {mo['rows_with_modelled_strength']} with a modelled "
             f"(grade E) side and {mo['rows_post_start']} with a post-start side. Grade E uncertainty is carried by "
             f"{mo['imputations']} imputations. Pooling τ = {mo['tau']}. Every result carries "
             f"{', '.join('`' + x + '`' for x in result['flags'])}.", '',
             '## Held-out test (the verdict)', '',
             '| Model | Log loss, battle-weighted | Log loss, campaign-weighted |', '|---|---:|---:|',
             f"| Commander model | {f(t['battle_weighted']['commander_model'])} | {f(t['campaign_weighted']['commander_model'])} |",
             f"| Strength only | {f(t['battle_weighted']['strength_only'])} | {f(t['campaign_weighted']['strength_only'])} |", '',
             f"Effective denominator: {len(t['effective_rows'])} of {t['n_rows']} held-out rows had a commander seen in another "
             f"campaign. Descriptive, not part of the verdict: campaigns where each model had lower log loss, commander model "
             f"{t['campaigns_better'].get('commander_model', 0)}, strength only {t['campaigns_better'].get('strength_only', 0)}, "
             f"ties {t['campaigns_better'].get('tie', 0)}; Monte Carlo check of the log-loss difference (commander minus strength) "
             + '; '.join(f"{k.replace('_', ' ')}: {v['battle_weighted']:+.4f} battle, {v['campaign_weighted']:+.4f} campaign"
                         for k, v in t['monte_carlo_check'].items()) + '.', '']
    ts = result['temporal_split']
    lines += [f"Descriptive {ts['years'][0][0]}–{ts['years'][0][-1]}→{ts['years'][1][0]}–{ts['years'][1][-1]} split "
              f"(no verdict): trained on {ts['n_train']}, tested on {ts['n_test']}; log loss {f(ts['commander_model'])} "
              f"(commander model) against {f(ts['strength_only'])} (strength only).", '']
    if not t['improved']:
        lines += ['**No improvement under the both-weightings rule: commander identity adds no detectable predictive signal '
                  'in these data. No ordered ranking is given.** The JSON keeps every estimate, labelled `no_heldout_signal`.', '']
    else:
        lines += ['Held-out log loss was lower under both weightings on these rows. This is not evidence of a persistent '
                  'commander effect or of skill (design §5).', '',
                  'Within each side, commanders are listed by median within-side rank over the pooled rank draws (ties by '
                  'the pooled point estimate). The order is a point summary under the design, not a finding that one commander '
                  'did better than another; read it with the 80% rank intervals.', '']
    g = result['views']['strength_graded_only'].get('reproduces_run2', {})
    lines += [f"The view `strength_graded_only` {'reproduces' if g.get('reproduces') else 'does not reproduce'} run 2's primary "
              f"fit (largest θ difference {g.get('max_abs_theta_difference', float('nan')):.2e}).", '']
    for side in ('US', 'Confederate'):
        cs = [c for c in result['commanders'].values() if c['side'] == side and c.get('ranked')]
        cs.sort(key=(lambda c: (c['rank_median'], -c['theta_pooled'])) if t['improved'] else (lambda c: c['name']))
        lines += [f"## {side} commanders with two or more modelled battles" + ('' if t['improved'] else ' (alphabetical)'), '',
                  '| Commander | Battles | Modelled-strength rows | W–L | Pooled θ | 80% interval | 95% interval | Rank 80% | SD ratio | Labels |',
                  '|---|---:|---:|---:|---:|---:|---:|---:|---:|---|']
        for c in cs:
            labels = sorted(set(c.get('labels', [])) | ({'view_sensitive'} if c.get('view_sensitive') else set()))
            lines.append(f"| {c['name']} | {c['battles_modelled']} | {c['modelled_strength_rows']} | {c['wins_in_model']}–{c['losses_in_model']} | "
                         f"{c['theta_pooled']:+.2f} | {c['interval_80'][0]:+.2f} to {c['interval_80'][1]:+.2f} | "
                         f"{c['interval_95'][0]:+.2f} to {c['interval_95'][1]:+.2f} | {c['rank_80'][0]}–{c['rank_80'][1]} | "
                         f"{c['posterior_prior_sd_ratio']:.2f} | {', '.join(labels)} |")
        lines.append('')
    lines += ['Views, per-commander view results and every held-out prediction are in the JSON. Commanders with one modelled '
              'battle are there with their estimate, which is almost entirely the prior.', '']
    return '\n'.join(lines)
