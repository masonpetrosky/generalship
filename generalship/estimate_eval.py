"""Locked estimate-layer evaluation (docs/strength-estimates.md §6).

Runs only when an owner authorization record names the current ledger's SHA-256.
Outputs are diagnostics beside the frozen baseline: they never enter
artifacts/baseline.json, admit a feature or rank commanders.
"""

from collections import Counter
from fractions import Fraction
from itertools import product

from .baseline import advantage, feature, fit_logistic, scores
from .dataset import build_dataset
from .estimates import (DEFAULT_LEDGER, OPPONENT_FACTOR, SIDES, EstimateError, check, estimate_row,
                        estimate_side, nested_sets, upper_median)
from .estimates_v2 import DEFAULT_LEDGER as LEDGER_V2, check as check_v2
from .sources import digest, read_json, safe_path

DEFAULT_AUTHORIZATION = 'data/estimates/evaluation-authorization-v1.json'
# Each run binds its own authorization, ledger, checker and cohort; v1 stays exactly as first run.
RUNS = {1: {'authorization': DEFAULT_AUTHORIZATION, 'ledger': DEFAULT_LEDGER, 'check': check,
            'cohort': 'data/pilot/cohort.json', 'output': 'artifacts/estimate-evaluation'},
        2: {'authorization': 'data/estimates/evaluation-authorization-v2.json', 'ledger': LEDGER_V2, 'check': check_v2,
            'cohort': 'data/pilot/cohort-v2.json', 'output': 'artifacts/estimate-evaluation-v2'}}
SETS = ('set1_A', 'set2_AB', 'set3_ABC')
MODELS = (('strength_logistic', 'diagnostic_union_score'), ('equal_odds', 'p_equal_odds'),
          ('training_prior', 'p_training_prior'))
EXCLUSION_LABELS = ('opponent_estimate_point', 'applicability_unresolved', 'derivation_unknown', 'bound_conflict')
ALT_BASIS_ORDER = ('reported_effective', 'present_for_duty', 'reported_present', 'reported_engaged', 'unknown')
FLAGS = ['whole_engagement_leakage', 'conditional_on_source_availability']
FROZEN_REFERENCE = {'battle_weighted_brier': 0.2768816348133779, 'campaign_weighted_brier': 0.2765271817053925}


def variant_estimates(ledger, **params):
    """Re-estimate every side with changed §4 parameters; the primary variant uses the stored estimates."""
    out = {}
    for e in ledger['engagements']:
        if params:
            est = estimate_row({s: estimate_side(e['sides'][s]['inputs'], **params) for s in SIDES})
        else:
            est = {s: e['sides'][s]['estimate'] for s in SIDES}
        out[e['battle_id']] = est
    return out


def assemble(estimates, records):
    """Rows per set, with post-start rows removed and counted (§6 leakage exclusion)."""
    by_id = {r['battle_id']: r for r in records}
    rows = {k: [] for k in SETS}
    excluded = {k: [] for k in SETS}
    excluded_any = []
    for bid, est in sorted(estimates.items()):
        n = nested_sets(est)
        if n['excluded_post_start_information']:
            excluded_any.append(bid)
        for k in n['sets']:
            if n['excluded_post_start_information']:
                excluded[k].append(bid)
                continue
            r = by_id[bid]
            rows[k].append({'battle_id': bid, 'name': r['name'], 'campaign': r['campaign'],
                            'union_outcome': int(r['source_result'] == 'Union'), 'estimate': est,
                            'baseline_eligible': r['baseline_eligible'], 'frozen': r})
    return rows, excluded, sorted(excluded_any)


def evaluable(rows):
    campaigns = {r['campaign'] for r in rows}
    ok = len(rows) >= 6 and len(campaigns) >= 3 and len({r['union_outcome'] for r in rows}) == 2
    return ok, {'rows': len(rows), 'campaigns': len(campaigns),
                'union_wins': sum(r['union_outcome'] for r in rows)}


def point_feature(row, ends=('point', 'point')):
    est = row['estimate']
    return advantage(est['US'][ends[0]], est['Confederate'][ends[1]])


def loco(rows, feature_fn):
    """Leave one campaign out over the campaigns present in the rows."""
    predictions, folds = [], []
    for campaign in sorted({r['campaign'] for r in rows}):
        train = [r for r in rows if r['campaign'] != campaign]
        ys = [r['union_outcome'] for r in train]
        model = fit_logistic([feature_fn(r) for r in train], ys)
        prior = (sum(ys) + 1) / (len(ys) + 2)
        folds.append({'held_out_campaign': campaign, 'n_train': len(train),
                      'intercept': model.intercept, 'slope': model.slope})
        for r in rows:
            if r['campaign'] == campaign:
                predictions.append({'battle_id': r['battle_id'], 'name': r['name'], 'campaign': campaign,
                                    'union_outcome': r['union_outcome'],
                                    'diagnostic_union_score': model.predict(feature_fn(r)),
                                    'p_equal_odds': 0.5, 'p_training_prior': prior})
    return sorted(predictions, key=lambda p: p['battle_id']), folds


def metrics(predictions, models=MODELS):
    campaigns = sorted({p['campaign'] for p in predictions})
    battle = {name: scores(predictions, key) for name, key in models}
    campaign = {name: {m: sum(scores([p for p in predictions if p['campaign'] == c], key)[m] for c in campaigns)
                       / len(campaigns) for m in ('brier', 'log_loss')} for name, key in models}
    return {'n_rows': len(predictions), 'n_campaigns': len(campaigns),
            'battle_weighted': battle, 'campaign_weighted': campaign}


def describe(rows):
    sides = [r['estimate'][s] for r in rows for s in SIDES]
    return {'grade_mix_sides': dict(sorted(Counter(e['grade'] for e in sides).items())),
            'label_counts_sides': dict(sorted(Counter(l for e in sides for l in e['labels']).items()))}


def fit_set(rows, feature_fn=point_feature):
    ok, counts = evaluable(rows)
    result = {'evaluable': ok, **counts, **describe(rows), 'flags': FLAGS}
    if ok:
        predictions, folds = loco(rows, feature_fn)
        result.update({'metrics': metrics(predictions), 'folds': folds, 'predictions': predictions})
    return result


def frozen_value(record, side):
    s = record['strengths'][side]
    return (Fraction(s['low']) + Fraction(s['high'])) / 2


def common_comparison(rows):
    """Both models fit on the same common training rows and scored on the same held-out rows (§6)."""
    common = [r for r in rows if r['baseline_eligible']]
    ok, counts = evaluable(common)
    identical = sorted(r['battle_id'] for r in common
                       if all(Fraction(r['estimate'][s]['exact']['point']) == frozen_value(r['frozen'], s)
                              for s in SIDES))
    result = {'evaluable': ok, **counts, **describe(common), 'flags': FLAGS, 'identical_by_construction': identical,
              'note': 'Identical rows differ from the frozen inputs only by rounding to 10.'}
    if ok:
        est, _ = loco(common, point_feature)
        frozen, _ = loco(common, lambda r: feature(r['frozen']))
        by = {p['battle_id']: p for p in frozen}
        for p in est:
            p['frozen_baseline_score'] = by[p['battle_id']]['diagnostic_union_score']
        result['metrics'] = metrics(est, MODELS + (('frozen_baseline_refit', 'frozen_baseline_score'),))
        result['predictions'] = est
    return result


def new_rows_comparison(primary_predictions, rows):
    new = [r for r in rows if not r['baseline_eligible']]
    preds = [p for p in primary_predictions if p['battle_id'] in {r['battle_id'] for r in new}]
    if not preds:
        return {'n_rows': 0}
    return {**metrics(preds), **describe(new), 'flags': FLAGS}


def sensitivity(ledger, records):
    out = {}
    base_rows, base_excluded, _ = assemble(variant_estimates(ledger), records)
    for us_end, cs_end in product(('low', 'high'), repeat=2):
        out[f'endpoint_refit_us_{us_end}_cs_{cs_end}'] = {
            k: {**summary(fit_set(base_rows[k], lambda r, e=(us_end, cs_end): point_feature(r, e))),
                'excluded_post_start_information': len(base_excluded[k])} for k in SETS}
    for label in EXCLUSION_LABELS:
        out[f'exclude_{label}'] = {
            k: {**summary(fit_set([r for r in base_rows[k]
                                   if not any(label in r['estimate'][s]['labels'] for s in SIDES)])),
                'excluded_post_start_information': len(base_excluded[k])} for k in SETS}
    for name, params in (('rule4_factor_1', {'factor': Fraction(1)}),
                         ('alternative_basis_order', {'basis_order': ALT_BASIS_ORDER}),
                         ('upper_middle_median', {'median': upper_median})):
        rows, excluded, _ = assemble(variant_estimates(ledger, **params), records)
        out[name] = {k: {**summary(fit_set(rows[k])), 'excluded_post_start_information': len(excluded[k])} for k in SETS}
    return out


def summary(result):
    keep = ('evaluable', 'rows', 'campaigns', 'union_wins', 'grade_mix_sides', 'label_counts_sides', 'flags', 'metrics')
    out = {k: result[k] for k in keep if k in result}
    if 'metrics' in out:
        out['metrics'] = {k: out['metrics'][k] for k in ('n_rows', 'n_campaigns', 'battle_weighted', 'campaign_weighted')}
    return out


def authorize(root, path=DEFAULT_AUTHORIZATION, ledger_path=DEFAULT_LEDGER):
    auth = read_json(safe_path(root, path))
    current = digest(safe_path(root, ledger_path))
    if auth.get('kind') != 'estimate_evaluation_authorization' or auth.get('ledger_path') != ledger_path:
        raise EstimateError('Authorization record kind or ledger path')
    if auth.get('ledger_sha256') != current:
        raise EstimateError('Authorization names a different ledger hash; no fit runs')
    if auth.get('option') != 'a_exploratory_estimate_layer_diagnostic':
        raise EstimateError('Only design §6 option (a) is implemented')
    if auth.get('admits_feature') is not False or auth.get('changes_baseline') is not False:
        raise EstimateError('An option (a) diagnostic admits no feature and leaves the baseline unchanged')
    return auth, current


def evaluate_estimates(root, version=1):
    run = RUNS[version]
    auth, ledger_sha = authorize(root, run['authorization'], run['ledger'])
    run['check'](root, run['ledger'])
    ledger = read_json(safe_path(root, run['ledger']))
    records, _ = build_dataset(root, run['cohort'])
    if version != 1:  # strength design §6: common rows are rows of the frozen 23-engagement baseline
        frozen_ids = {r['battle_id'] for r in build_dataset(root)[0] if r['baseline_eligible']}
        records = [{**r, 'baseline_eligible': r['baseline_eligible'] and r['battle_id'] in frozen_ids} for r in records]
    rows, excluded, excluded_any = assemble(variant_estimates(ledger), records)
    results = {}
    for k in SETS:
        r = fit_set(rows[k])
        r['excluded_post_start_information'] = excluded[k]
        if r['evaluable']:
            r['common_rows'] = common_comparison(rows[k])
            r['newly_covered_rows'] = new_rows_comparison(r['predictions'], rows[k])
        results[k] = r
    extra = {} if version == 1 else {'run_version': version, 'cohort': {'path': run['cohort'], 'sha256': digest(safe_path(root, run['cohort']))},
                                     'output': run['output'] + '.json'}
    return {'kind': 'estimate_layer_evaluation', 'model_id': 'strength-logistic-v1',
            'status': 'exploratory_estimate_layer_diagnostic_not_baseline',
            'authorization': {'path': run['authorization'], 'sha256': digest(safe_path(root, run['authorization'])),
                              'owner_decision_date': auth['decision_date'], 'option': auth['option']},
            'ledger': {'path': run['ledger'], 'sha256': ledger_sha}, **extra,
            'validation': 'leave_one_campaign_out', 'ridge': 1.0, 'rule4_factor_primary': str(OPPONENT_FACTOR),
            'rows_excluded_post_start_information': excluded_any,
            'frozen_baseline_reference': {**FROZEN_REFERENCE, 'rows': 23, 'campaigns': 13, 'equal_odds_brier': 0.25},
            'row_sets': results, 'sensitivity': sensitivity(ledger, records), 'flags': FLAGS,
            'limitations': [
                'Predictions are diagnostic_union_score values, not win probabilities or command effects.',
                'Which sides have figures, and so which rows and grades exist, may depend on the outcome, size and fame.',
                'Results from different row sets, grades or sensitivity variants are not improvements over one another.',
                'No significance test was run; at these row counts no difference is presented as significant or as evidence that the estimates are accurate.',
                'No commander attribution, ranking or causal effect is produced.']}


def _fmt(m, name):
    return f"{m['battle_weighted'][name]['brier']:.4f} / {m['campaign_weighted'][name]['brier']:.4f}"


def report_text(result):
    """Markdown summary; artifacts/estimate-evaluation.json holds every fold and prediction."""
    lines = ['# Estimate-layer evaluation (diagnostic)', '',
             '**Exploratory estimate-layer diagnostic under design §6 option (a). Not the baseline, not an admitted '
             'feature, not a ranking of commanders.**', '',
             f"Ledger `{result['ledger']['path']}` (SHA-256 `{result['ledger']['sha256']}`), authorized by the owner "
             f"on {result['authorization']['owner_decision_date']} ([record](../{result['authorization']['path']})).",
             'Model `strength-logistic-v1`, unchanged: ridge 1.0 logistic regression on the rounded point strengths, '
             'leave one campaign out. Scores are `diagnostic_union_score` values, not win probabilities.',
             f"Rows with a `post_start_information` side: {len(result['rows_excluded_post_start_information'])} "
             f"({', '.join(result['rows_excluded_post_start_information'])}); excluded from fits: "
             + ', '.join(f"{k} {len(v['excluded_post_start_information'])}" for k, v in result['row_sets'].items()) + '.', '',
             '## Row sets', '', 'Brier score, battle-weighted / campaign-weighted. Lower is better; equal odds scores 0.2500.', '',
             '| Row set | Rows | Campaigns | Union wins | Side grades | Strength model | Equal odds | Training prior |',
             '|---|---:|---:|---:|---|---:|---:|---:|']
    for k, r in result['row_sets'].items():
        grades = ' '.join(f'{g} {n}' for g, n in r['grade_mix_sides'].items())
        if not r['evaluable']:
            lines.append(f"| {k} | {r['rows']} | {r['campaigns']} | {r['union_wins']} | {grades} | not evaluable | | |")
            continue
        m = r['metrics']
        lines.append(f"| {k} | {r['rows']} | {r['campaigns']} | {r['union_wins']} | {grades} | {_fmt(m, 'strength_logistic')} "
                     f"| {_fmt(m, 'equal_odds')} | {_fmt(m, 'training_prior')} |")
    ref = result['frozen_baseline_reference']
    out_name = result.get('output', 'artifacts/estimate-evaluation.json').split('/')[-1]
    lines += ['', f'Per-set §5 label counts, folds and every prediction are in `{out_name}`.', '',
              f"Frozen baseline reference ({ref['rows']} rows, {ref['campaigns']} campaigns{'' if 'run_version' not in result else '; cohort v1, not these rows'}): "
              f"{ref['battle_weighted_brier']:.4f} / {ref['campaign_weighted_brier']:.4f}.", '',
              '## Common and newly covered rows', '',
              'Common rows have both a frozen baseline row and an estimate row; both models are refit on the same common '
              'training rows in each fold. Newly covered rows are compared only with equal odds and the prior.', '',
              '| Row set | Common rows | Identical by construction | Estimates | Frozen refit | Equal odds | Prior | New rows | Estimates | Equal odds | Prior |',
              '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    for k, r in result['row_sets'].items():
        if not r['evaluable']:
            continue
        c, n = r['common_rows'], r['newly_covered_rows']
        cm = c.get('metrics')
        common = (f"{_fmt(cm, 'strength_logistic')} | {_fmt(cm, 'frozen_baseline_refit')} | {_fmt(cm, 'equal_odds')} | "
                  f"{_fmt(cm, 'training_prior')}") if cm else 'not evaluable | | |'
        new = (f"{_fmt(n, 'strength_logistic')} | {_fmt(n, 'equal_odds')} | {_fmt(n, 'training_prior')}"
               if n.get('n_rows') else '| |')
        lines.append(f"| {k} | {c['rows']} | {len(c['identical_by_construction'])} | {common} | {n.get('n_rows', 0)} | {new} |")
    lines += ['', '## Sensitivity refits', '', 'Strength-model Brier, battle-weighted, with rows used. "NE" is not evaluable '
              '(fewer than 6 rows, 3 campaigns or both outcomes).', '', '| Variant | set1_A | set2_AB | set3_ABC |', '|---|---:|---:|---:|']
    for name, sets in result['sensitivity'].items():
        cells = [f"{v['metrics']['battle_weighted']['strength_logistic']['brier']:.4f} ({v['rows']})" if v['evaluable']
                 else f"NE ({v['rows']})" for v in sets.values()]
        lines.append(f"| {name} | " + ' | '.join(cells) + ' |')
    lines += ['', '## Limits', ''] + [f'- {x}' for x in result['limitations']] + [
        f"- Every result carries {', '.join(f'`{x}`' for x in result['flags'])}.", '']
    return '\n'.join(lines)
