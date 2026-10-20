"""Primary verification and reporting of the saved temporal run; never fit."""

import argparse
from collections import Counter, defaultdict
import json
import math
from pathlib import Path
from statistics import fmean

from . import napoleonic_temporal_calibration as prep
from .sources import digest, read_json, write_json

RESULT = prep.RESULT
RESULT_SHA = '39213035280b48ffa6ef10031ba6631715dba58b6bdcb0d95e034e17585067a2'
PROPOSAL_SHA = 'b6b58138ba1b396160a0d9185e18a3b756f83788fb89da5f3431000a9d84b5f7'
AUTH = prep.BASE + 'owner-run-authorization.json'
REPORT = 'docs/research/napoleonic-temporal-calibration-run-v1.md'
VERIFICATION = 'artifacts/napoleonic-temporal-calibration-run-v1-verification.json'
CODE = 'generalship/napoleonic_temporal_calibration_report.py'
MODELS = prep.MODELS
WEIGHTINGS = ('battle', 'equal_campaign')
REGIONS = ('decision', 'reused_1813_secondary')


def require(condition, message):
    if not condition:
        raise ValueError('Napoleonic saved temporal-run verification: ' + message)


def near(actual, expected):
    require(type(actual) in (int, float) and math.isfinite(actual)
            and math.isclose(actual, expected, rel_tol=0, abs_tol=2e-12), f'{actual} != {expected}')


def compare(actual, expected, locator):
    """Check every field, retaining the distinction between empty values and zero."""
    if isinstance(expected, dict):
        require(isinstance(actual, dict) and actual.keys() == expected.keys(), locator + ' fields')
        for key, value in expected.items():
            compare(actual[key], value, locator + '.' + key)
    elif isinstance(expected, list):
        require(isinstance(actual, list) and len(actual) == len(expected), locator + ' length')
        for i, (a, b) in enumerate(zip(actual, expected, strict=True)):
            compare(a, b, f'{locator}[{i}]')
    elif type(expected) is float:
        near(actual, expected)
    else:
        require(type(actual) is type(expected) and actual == expected, locator + ' value')


def sigmoid(z):
    return 1 / (1 + math.exp(-z)) if z >= 0 else math.exp(z) / (1 + math.exp(z))


def loss(probability, y, metric):
    if metric == 'brier':
        return (probability - y) ** 2
    p = max(1e-15, min(1 - 1e-15, probability))
    return -math.log(p if y else 1 - p)


def summary(records, edges):
    """Average group losses directly, separately from the runner's row weights."""
    groups = sorted({p['campaign_group'] for p in records})
    sizes = Counter(p['campaign_group'] for p in records)
    result = {'entries': len(records), 'campaign_groups': len(groups), 'metrics': {}, 'calibration': {}}
    for weighting in WEIGHTINGS:
        result['metrics'][weighting] = {}
        result['calibration'][weighting] = {}
        weights = [1.0 if weighting == 'battle' else 1 / sizes[p['campaign_group']] for p in records]
        for model in MODELS:
            scores = None
            if records:
                scores = {}
                for metric in ('brier', 'log_loss'):
                    blocks = [[loss(p[model], p['y'], metric) for p in records if p['campaign_group'] == g]
                              for g in groups]
                    scores[metric] = (fmean(x for block in blocks for x in block) if weighting == 'battle'
                                      else fmean(fmean(block) for block in blocks))
            result['metrics'][weighting][model] = scores
            bins = []
            for i, (low, high) in enumerate(zip(edges[:-1], edges[1:], strict=True)):
                bucket = [(p, w) for p, w in zip(records, weights, strict=True)
                          if low <= p[model] < high or (i == len(edges) - 2 and p[model] == high)]
                denominator = math.fsum(w for _, w in bucket)
                bins.append({'lower': low, 'upper': high, 'n': len(bucket),
                             'mean_probability': math.fsum(p[model] * w for p, w in bucket) / denominator if bucket else None,
                             'recorded_a_win_share': math.fsum(p['y'] * w for p, w in bucket) / denominator if bucket else None})
            result['calibration'][weighting][model] = bins
    return result


def select(rows, population):
    selected = [r for r in rows if r['eligible']]
    if population == 'exclude_indecisive':
        selected = [r for r in selected if not r['indecisive_printed']]
    elif population == 'exclude_no_combat':
        selected = [r for r in selected if not r['no_combat_printed']]
    elif population == 'unqualified_totals':
        selected = [r for r in selected if not any(s['approximate'] or s['footnote_markers']
                                                  or s['context_footnote_markers'] for s in r['sides'].values())]
    return selected


def verify_roles(rows, selected, planned, fold, protocol):
    """Reconcile whole-group time roles using every member, not eligible rows alone."""
    members = defaultdict(list)
    for row in rows:
        members[row['campaign_group']].append(row)
    end, start, cohort = {}, {}, {}
    for group, values in members.items():
        require(len({r['start_year'] for r in values}) == 1, 'one frozen year per group')
        cohort[group] = values[0]['start_year']
        end[group] = max(r['end_date'] for r in values) if all(r['end_date'] for r in values) else None
        start[group] = min(r['start_date'] for r in values) if all(r['start_date'] for r in values) else None
    year = fold['target_year']; cutoff = f'{year}-01-01'
    available = {g for g in members if cohort[g] < year and end[g] is not None and end[g] < cutoff}
    latest = max((int(end[g][:4]) for g in available), default=None)
    calibration = {g for g in available if int(end[g][:4]) == latest}
    base = available - calibration
    test = {g for g in members if cohort[g] == year}
    deferred = {g for g in members if cohort[g] < year} - available
    calibration_start = min(start[g] for g in calibration) if calibration and all(start[g] for g in calibration) else None
    eligible = {r['battle_id'] for r in selected}
    all_ids = lambda gs: {r['battle_id'] for g in gs for r in members[g]}
    roles = {'base_ids': sorted(all_ids(base) & eligible), 'calibration_ids': sorted(all_ids(calibration) & eligible),
             'expanding_ids': sorted(all_ids(available) & eligible), 'test_ids': sorted(all_ids(test) & eligible)}
    reasons = []
    if not roles['test_ids']:
        reasons.append('empty_eligible_test')
    if len(roles['base_ids']) < protocol['minimum_base_rows']:
        reasons.append('insufficient_base_rows')
    if len(roles['calibration_ids']) < protocol['minimum_calibration_rows']:
        reasons.append('insufficient_calibration_rows')
    if calibration and calibration_start is None:
        reasons.append('unknown_calibration_start')
    elif calibration_start and any(end[g] >= calibration_start for g in base):
        reasons.append('base_not_complete_before_calibration_start')
    region = 'decision' if year in protocol['decision_years'] else 'reused_1813_secondary' if year == 1813 else 'warmup'
    metadata = {'target_year': year, 'cutoff': cutoff, 'calibration_start': calibration_start,
                'region': region, 'reasons': reasons, **roles}
    for key, value in metadata.items():
        compare(planned[key], value, 'planned temporal role.' + key)
        compare(fold[key], value, 'saved temporal role.' + key)
    for key, groups in (('base_groups', base), ('calibration_groups', calibration), ('test_groups', test),
                        ('deferred_earlier_groups', deferred)):
        require(planned[key] == sorted(groups), 'whole-group temporal role: ' + key)
    require(planned['latest_available_completion_year'] == latest
            and planned['all_test_ids'] == sorted(all_ids(test))
            and planned['excluded_test_ids'] == sorted(all_ids(test) - eligible)
            and planned['deferred_earlier_ids'] == sorted(all_ids(deferred) & eligible), 'temporal exclusions')
    require(planned['status'] == ('not_estimable' if reasons else 'planned')
            and fold['status'] == ('not_estimable' if reasons else 'scored'), 'temporal estimability')


def continuation(populations, protocol):
    """Recompute the frozen decision from verified main-region scores only."""
    require(protocol['decision_years'] == [1808, 1809, 1810, 1811, 1812]
            and protocol['secondary_years'] == [1813], 'decision excludes 1813')
    years = [str(y) for y in protocol['decision_years']]
    primary, screen = (populations[p] for p in ('primary', 'unqualified_totals'))
    for population in (primary, screen):
        for year in years:
            annual = population['per_year'].get(year)
            if not annual or not annual['entries'] or any(annual['metrics']['battle'].get(m) is None
                                                         for m in ('offset_force', 'expanding_force')):
                return {'status': 'not_assessable', 'reason': 'missing_required_decision_year', '1813_used': False}
    comparisons = []; tolerance = protocol['decision_tolerance']
    for weighting in WEIGHTINGS:
        main = primary['regions']['decision']['metrics'][weighting]
        sensitivity = screen['regions']['decision']['metrics'][weighting]
        if any(main[m] is None for m in MODELS) or any(sensitivity[m] is None for m in ('offset_force', 'expanding_force')):
            return {'status': 'not_assessable', 'reason': 'missing_required_scores', '1813_used': False}
        for population, scores, comparators in (('primary', main, MODELS[1:]),
                                                ('unqualified_totals', sensitivity, ('expanding_force',))):
            for comparator in comparators:
                dll = scores['offset_force']['log_loss'] - scores[comparator]['log_loss']
                db = scores['offset_force']['brier'] - scores[comparator]['brier']
                comparisons.append({'population': population, 'weighting': weighting, 'comparator': comparator,
                                    'log_loss_difference': dll, 'brier_difference': db,
                                    'satisfied': (dll < -tolerance if population == 'primary' else dll <= tolerance)
                                                 and db <= tolerance})
    improved = [int(y) for y in years if primary['per_year'][y]['metrics']['battle']['offset_force']['log_loss']
                < primary['per_year'][y]['metrics']['battle']['expanding_force']['log_loss'] - tolerance]
    passed = all(c['satisfied'] for c in comparisons) and len(improved) >= 3
    return {'status': 'passes_exploratory_continuation_rule' if passed else 'does_not_pass',
            'comparisons': comparisons, 'improved_years_against_expanding_force': improved,
            '1813_used': False, 'authorizes_final_use_or_feature_admission': False}


def verify(root):
    require(digest(root / RESULT) == RESULT_SHA, 'immutable executed result changed')
    require(digest(root / prep.PROPOSAL) == PROPOSAL_SHA, 'exact proposal changed')
    prep.check(root)  # Metadata-only; checks every bound preparation input/output.
    run, auth, proposal = (read_json(root / path) for path in (RESULT, AUTH, prep.PROPOSAL))
    require(run['kind'] == 'napoleonic_temporal_calibration_run' and run['version'] == 1
            and run['status'] == 'exploratory_compiler_record_prediction_not_command_effect', 'run identity')
    require(run['proposal_sha256'] == PROPOSAL_SHA and run['authorization_sha256'] == digest(root / AUTH), 'run bindings')
    require(auth['kind'] == 'napoleonic_temporal_calibration_owner_run_authorization' and auth['approved'] is True
            and auth['proposal_sha256'] == PROPOSAL_SHA and auth['command'] == proposal['command']
            and auth['scope'] == proposal['scope'] and auth['owner_request'] == run['owner_request'], 'owner authorization')
    require(run['executed_bindings'] == proposal['bindings'], 'executed input/code bindings')
    for path, sha in run['executed_bindings'].items():
        require(digest(root / path) == sha, 'changed executing input/code: ' + path)
    scope, protocol, data, plan = (read_json(root / path) for path in
                                  (prep.SCOPE, prep.PROTOCOL, prep.DATA, prep.ARTIFACT + '.json'))
    rows = data['entries']; reserved = set(scope['reserved_final_ids'])
    require([r['battle_id'] for r in rows] == scope['development_ids'] and len(rows) == 273
            and len(reserved) == 52 and not reserved & set(scope['development_ids'])
            and run['reserved_final_used'] is False, 'development/final separation')
    frame = {r['id']: r for r in read_json(root / 'data/napoleonic/frame-v1.json')['entries']}
    labels = {b: frame[b]['outcome_side_a'] for b in scope['development_ids']}
    require(all(type(y) is int and y in (0, 1) for y in labels.values()), 'binary development labels')
    require(tuple(run['populations']) == prep.POPULATIONS, 'all fixed populations')
    original = read_json(root / 'artifacts/napoleonic-benchmark-run-v1.json')
    counts = Counter()
    for population, result in run['populations'].items():
        selected = select(rows, population); indexed = {r['battle_id']: r for r in selected}
        require(result['eligible_entries'] == len(selected), 'eligible denominator')
        predictions = result['predictions']
        require([p['battle_id'] for p in predictions] == sorted({p['battle_id'] for p in predictions})
                and set(p['battle_id'] for p in predictions) <= indexed.keys(), 'prediction grain/membership')
        require(result['unscored_ids'] == sorted(indexed.keys() - {p['battle_id'] for p in predictions}), 'unscored IDs')
        planned_folds = plan['populations'][population]['folds']
        parameters = result['parameters']
        require([f['target_year'] for f in parameters] == protocol['target_years'], 'complete annual design')
        by_year = {y: [p for p in predictions if p['target_year'] == y] for y in protocol['target_years']}
        require(sum(map(len, by_year.values())) == len(predictions), 'prediction year membership')
        def feature(b):
            a, c = (indexed[b]['sides'][s]['primary_value'] for s in ('A', 'B'))
            require(a > 0 and c > 0 and math.isfinite(a + c), 'positive personnel input')
            return (a - c) / (a + c)
        for planned, fold in zip(planned_folds, parameters, strict=True):
            verify_roles(rows, selected, planned, fold, protocol)
            counts['annual_role_assignments_checked'] += 1
            for role in ('base_ids', 'calibration_ids', 'expanding_ids', 'test_ids'):
                require(not reserved & set(fold[role]), 'reserved-final leakage')
            test = by_year[fold['target_year']]
            if fold['status'] != 'scored':
                require(not test and not any(k in fold for k in ('base_intercept', 'offset', 'expanding_intercept')),
                        'unestimable fold predictions/parameters')
                continue
            require(sorted(p['battle_id'] for p in test) == fold['test_ids'], 'complete outer predictions')
            base, calibration, expanding = (fold[key] for key in ('base_ids', 'calibration_ids', 'expanding_ids'))
            require(not set(base) & set(calibration) and not (set(base) | set(calibration)) & set(fold['test_ids'])
                    and set(expanding) == set(base) | set(calibration), 'training/test separation')
            for ids, prefix in ((base, 'base'), (expanding, 'expanding')):
                a, b = (fold[prefix + suffix] for suffix in ('_intercept', '_slope'))
                require(math.isfinite(a) and math.isfinite(b), 'finite force parameters')
                residuals = [sigmoid(a + b * feature(battle)) - labels[battle] for battle in ids]
                score_a = protocol['force_ridge'] * a + math.fsum(residuals)
                score_b = protocol['force_ridge'] * b + math.fsum(r * feature(battle) for r, battle in zip(residuals, ids, strict=True))
                error = max(abs(score_a), abs(score_b))
                require(error < 1e-7, 'force score equations')
                counts['force_stationarity_checks'] += 1
            a, b, delta = (fold[k] for k in ('base_intercept', 'base_slope', 'offset'))
            offset_gradient = protocol['offset_ridge'] * delta + math.fsum(
                sigmoid(a + b * feature(battle) + delta) - labels[battle] for battle in calibration)
            require(math.isfinite(delta) and abs(delta) <= len(calibration) / protocol['offset_ridge']
                    and 1 <= fold['iterations'] <= 200 and abs(offset_gradient) <= 1e-9, 'offset score equation')
            near(fold['score_equation'], offset_gradient)
            counts['offset_stationarity_checks'] += 1
            prior = (sum(labels[battle] for battle in expanding) + 1) / (len(expanding) + 2)
            recent = (sum(labels[battle] for battle in calibration) + 1) / (len(calibration) + 2)
            near(fold['expanding_prior'], prior); near(fold['recent_prior'], recent)
            for p in test:
                battle = p['battle_id']; x = feature(battle)
                require(p['y'] == labels[battle] and p['region'] == fold['region']
                        and p['campaign_group'] == p['held_out_group'] == indexed[battle]['campaign_group'], 'prediction provenance')
                near(p['force_balance'], x)
                expected = {'offset_force': sigmoid(a + b*x + delta), 'same_base_force': sigmoid(a + b*x),
                            'expanding_force': sigmoid(fold['expanding_intercept'] + fold['expanding_slope']*x),
                            'expanding_prior': prior, 'recent_prior': recent, 'equal_odds': .5}
                for model, probability in expected.items():
                    require(type(p[model]) in (int, float) and 0 <= p[model] <= 1, 'probability range')
                    near(p[model], probability); counts['probability_values_checked'] += 1
                counts['prediction_rows_checked'] += 1
        require(tuple(result['regions']) == REGIONS
                and list(result['per_year']) == [str(y) for y in protocol['target_years']]
                and list(result['per_group']) == sorted({p['campaign_group'] for p in predictions}), 'summary populations')
        summaries = [(result['regions'][g], [p for p in predictions if p['region'] == g]) for g in REGIONS]
        summaries += [(result['per_year'][str(y)], by_year[y]) for y in protocol['target_years']]
        summaries += [(result['per_group'][g], [p for p in predictions if p['campaign_group'] == g]) for g in result['per_group']]
        for actual, records in summaries:
            compare(actual, summary(records, protocol['calibration_edges']), 'scores/calibration')
            counts['summaries_checked'] += 1
            counts['metric_values_checked'] += 24 if records else 0
            counts['calibration_bins_checked'] += 60
        expected_contributions, expected_concentration = {}, {}
        for comparator in MODELS[1:]:
            values = [{'battle_id': p['battle_id'], 'target_year': p['target_year'], 'region': p['region'],
                       'log_loss_difference': loss(p['offset_force'], p['y'], 'log_loss') - loss(p[comparator], p['y'], 'log_loss'),
                       'brier_difference': loss(p['offset_force'], p['y'], 'brier') - loss(p[comparator], p['y'], 'brier')}
                      for p in predictions]
            values.sort(key=lambda p: (-abs(p['log_loss_difference']), p['battle_id']))
            expected_contributions[comparator] = values
            expected_concentration[comparator] = {}
            for region in REGIONS:
                amounts = [abs(v['log_loss_difference']) for v in values if v['region'] == region]
                total = math.fsum(amounts)
                expected_concentration[comparator][region] = {'sum_absolute_log_loss_differences': total,
                    'top_shares': {str(n): math.fsum(amounts[:n]) / total if total else None for n in (1, 5, 10)}}
            counts['paired_case_contributions_checked'] += len(values)
        compare(result['paired_loss_contributions'], expected_contributions, 'paired contributions')
        compare(result['absolute_loss_concentration'], expected_concentration, 'absolute concentration')
        old = original['populations'][population]['forward_1813']
        current = next(f for f in parameters if f['target_year'] == 1813)
        require(current['expanding_ids'] == old['folds'][0]['train_ids']
                and current['test_ids'] == old['folds'][0]['test_ids'], 'original forward membership')
        for p, q in zip(by_year[1813], old['predictions'], strict=True):
            require(p['battle_id'] == q['battle_id'] and p['y'] == q['y'], 'original forward rows')
            for model, old_model in (('expanding_force', 'force'), ('expanding_prior', 'training_prior'), ('equal_odds', 'equal_odds')):
                near(p[model], q[old_model])
            counts['original_forward_prediction_rows_matched'] += 1
    require(run['populations']['primary'] == run['populations']['exclude_indecisive'], 'indecisive no-op')
    compare(run['continuation'], continuation(run['populations'], protocol), 'fixed continuation decision')
    require(counts['force_stationarity_checks'] == 48 and counts['offset_stationarity_checks'] == 24
            and counts['prediction_rows_checked'] == 589 and counts['probability_values_checked'] == 3534,
            'planned fit/prediction totals')
    verification = {'kind': 'napoleonic_temporal_calibration_primary_arithmetic_verification', 'version': 1,
                    'status': 'share_with_caveats_failed_continuation', 'separate_review': False,
                    'historical_refits_performed': 0, 'reserved_final_entries_used': 0,
                    'bindings': {path: digest(root / path) for path in (RESULT, AUTH, prep.PROPOSAL, CODE)},
                    # Computed residuals can differ in their last bits by Python/libm.
                    # Persist the checked tolerances/counts, not machine-specific residuals.
                    'checks': dict(counts),
                    'absolute_force_score_tolerance': 1e-7, 'absolute_offset_score_tolerance': 1e-9,
                    'absolute_arithmetic_tolerance': 2e-12, 'continuation': run['continuation']['status']}
    return run, data, plan, verification


def report(run, data, plan, verification):
    populations = run['populations']; primary = populations['primary']
    out = ['# Napoleonic temporal probability-correction run v1', '',
           'Primary-verified. The owner authorized the exact frozen proposal. No separate review occurred.', '',
           '**The correction fails the fixed exploratory continuation rule. Retain the uncorrected force '
           'baseline and close this correction branch.** In the main 1808–1812 region, corrected log loss '
           'is 0.663652 versus 0.632991 for expanding force, and Brier is 0.234834 versus 0.223525 '
           '(battle weighted; lower is better). Equal-campaign scores and the unqualified-total sensitivity '
           'also worsen. Only two of five decision years improve in log loss. The reused 1813 scores improve '
           'but cannot affect or rescue the decision.', '',
           'This is an exploratory prediction of compiler records, not a commander, tactical or '
           'campaign-contribution effect. No feature is admitted and all 52 final entries remain unused numerically.', '',
           '## Fixed scope, coverage and method', '',
           'The [frozen design](../napoleonic-temporal-calibration-v1.md), '
           '[protocol](../../data/napoleonic/temporal-calibration-v1/protocol.json) and '
           '[complete plan](../../artifacts/napoleonic-temporal-calibration-plan-v1.md) remain unchanged. '
           'Their preparation-only status records the earlier task; the later actual authorization is a separate record. '
           'All 273 development entries / 13 source groups remain in the denominator. '
           'No source, dossier, outcome, personnel total, original grouping or exclusion is changed.', '',
           '| Population | Eligible / 273 | Warmup eligible / 68 | Main scored / 141 | Main excluded | Secondary scored / 64 | Secondary excluded |',
           '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    for population, result in populations.items():
        main, secondary = (result['regions'][r]['entries'] for r in REGIONS)
        out.append(f'| {population} | {result["eligible_entries"]} | {len(result["unscored_ids"])} | {main} | '
                   f'{141-main} | {secondary} | {64-secondary} |')
    out += ['', 'The 1805–1807 warmup has no outer predictions. Main scores use five annual folds/seven source '
            'groups; secondary 1813 uses one annual fold/two groups. The primary 273-entry denominator is '
            '68 warmup + 141 main + 64 secondary. Printed-indecisive exclusion is a no-op; '
            'non-combat exclusion removes one warmup row, which can change later training fits. '
            'Unqualified totals screen approximate figures or numeric notes anywhere in the cited passage; '
            'this does not adjudicate a note’s applicability.', '',
            'Each target year uses only whole groups ending before January 1. The base contains earlier '
            'completed groups; calibration contains all groups in the latest available completion year. '
            'Every base group must finish before every calibration member starts. Availability uses every '
            'member, including numerically excluded rows. Unknown dates, overlap or fewer than ten eligible '
            'rows in either training block cause no score and no fallback. Original roles/exclusions and '
            'controlling entry/date locators remain in the plan.', '',
            'One ridge-1 force fit on base rows uses `(A-B)/(A+B)`, with A = France and its allies. Its '
            'intercept and slope stay frozen while one ridge-1 logit offset is fitted on the disjoint '
            'calibration block. Comparators are that same base with zero offset, force refitted on base '
            'plus calibration, Laplace priors on expanding/recent training labels, and equal odds. '
            'No penalty, time window or model is selected after the result. Within each fold the offset '
            'retains the same base ordering.', '',
            '## All fixed population and model scores', '',
            'Lower is better; log loss uses natural logarithms. Battle weighting gives each scored entry '
            'equal weight. Equal-campaign weighting averages the original source-group means within the '
            'stated region. Each model uses exactly the same test rows in a population. '
            'Cross-population differences are not paired effects of qualifiers.', '']
    for region, title in (('decision', 'Main: 1808–1812'), ('reused_1813_secondary', 'Secondary: reused 1813')):
        out += [f'### {title}', '',
                '| Population | Model | Log loss, battle | Brier, battle | Log loss, campaign | Brier, campaign |',
                '| --- | --- | ---: | ---: | ---: | ---: |']
        for population, result in populations.items():
            for model in MODELS:
                metrics = result['regions'][region]['metrics']
                cells = [metrics[w][model][m] for w in WEIGHTINGS for m in ('log_loss', 'brier')]
                out.append(f'| {population} | {model} | ' + ' | '.join(f'{x:.6f}' for x in cells) + ' |')
        out.append('')
    out += ['The secondary primary correction improves battle-weighted log loss from 0.691122 to 0.601049 '
            'and Brier from 0.251057 to 0.207721 against expanding force. These cases motivated the test '
            'and were already inspected. They are neither a fresh validation set nor a reason to override '
            'the main failure. The 1813 expanding probabilities match the original saved benchmark '
            'within absolute tolerance 2e-12 in every population. Its earlier forward report treated the whole '
            'year as one held-out group; this report’s equal-campaign view instead gives its two original '
            'source groups equal weight, so those aggregate scores differ.', '',
            '## Fixed continuation decision', '',
            'Candidate minus comparator: negative favors correction. Primary comparisons require strictly '
            'lower log loss and nonhigher Brier under both weightings; the sensitivity permits no worsening '
            'of either. Absolute decision tolerance is 1e-12.', '',
            '| Population | Weighting | Comparator | Log-loss difference | Brier difference | Satisfied |',
            '| --- | --- | --- | ---: | ---: | --- |']
    for c in run['continuation']['comparisons']:
        out.append(f'| {c["population"]} | {c["weighting"]} | {c["comparator"]} | '
                   f'{c["log_loss_difference"]:+.6f} | {c["brier_difference"]:+.6f} | {"yes" if c["satisfied"] else "no"} |')
    out += ['', 'The primary correction fails against both force comparators under battle weighting. '
            'Against the same base, equal-campaign log loss improves by only 0.000232 while Brier worsens '
            'by 0.002456; that comparison also fails. Against expanding force, both scores worsen under '
            'equal-campaign weighting, and the unqualified-total veto fails under both weightings. '
            'Primary log loss improves against expanding force in **1810 and 1811 only (2/5; required ≥3)**. '
            'The result is **does_not_pass**. The decision function never reads 1813 scores.', '',
            '## Training support, offsets and annual variation', '',
            'Primary population. Repeated blocks are deliberate: no newer complete group becomes available '
            'in 1809 or 1811–1812. Small support and shared fits limit replication.', '',
            '| Target year | Base n | Calibration n | Test eligible / scored | Base intercept | Base slope | Offset | Expanding intercept | Expanding slope |',
            '| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |']
    for f in primary['parameters']:
        values = [f.get(k) for k in ('base_intercept', 'base_slope', 'offset', 'expanding_intercept', 'expanding_slope')]
        out.append(f'| {f["target_year"]} | {len(f["base_ids"])} | {len(f["calibration_ids"])} | '
                   f'{len(f["test_ids"])} / {len(f["test_ids"]) if f["status"] == "scored" else 0} | '
                   + ' | '.join('not estimable' if v is None else f'{v:+.6f}' for v in values) + ' |')
    out += ['', '| Year | Region | Scored n | Corrected log loss | Expanding log loss | Difference | Corrected Brier | Expanding Brier |',
            '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    for year, s in primary['per_year'].items():
        if not s['entries']:
            continue
        a, b = (s['metrics']['battle'][m] for m in ('offset_force', 'expanding_force'))
        out.append(f'| {year} | {"secondary" if year == "1813" else "main"} | {s["entries"]} | '
                   f'{a["log_loss"]:.6f} | {b["log_loss"]:.6f} | {a["log_loss"]-b["log_loss"]:+.6f} | '
                   f'{a["brier"]:.6f} | {b["brier"]:.6f} |')
    out += ['', '## Source-group variation and paired loss concentration', '',
            '| Source group | Scored n | Corrected log loss | Expanding log loss | Difference |',
            '| --- | ---: | ---: | ---: | ---: |']
    for group, s in primary['per_group'].items():
        a, b = (s['metrics']['battle'][m]['log_loss'] for m in ('offset_force', 'expanding_force'))
        out.append(f'| {group} | {s["entries"]} | {a:.6f} | {b:.6f} | {a-b:+.6f} |')
    out += ['', 'The correction has lower log loss in three of seven main source groups and higher loss in '
            'four. The annual 1812 aggregate worsens slightly even though its small Peninsular group improves. '
            'Every model’s year/group scores, bins and every signed case difference in all populations '
            'remain in the raw result and are checked during reproduction.', '',
            'The concentration denominator is the sum of absolute paired log-loss differences, retaining '
            'gains and losses without cancellation. These shares are not shares of net gain or command credit.', '',
            '| Region | Comparator | Absolute-difference total | Largest one | Largest five | Largest ten |',
            '| --- | --- | ---: | ---: | ---: | ---: |']
    for comparator, regions in primary['absolute_loss_concentration'].items():
        for region, record in regions.items():
            shares = [record['top_shares'][str(n)] for n in (1, 5, 10)]
            out.append(f'| {region} | {comparator} | {record["sum_absolute_log_loss_differences"]:.6f} | '
                       + ' | '.join('unknown' if v is None else f'{v:.2%}' for v in shares) + ' |')
    out += ['', '## Probability bins', '',
            'Primary correction and expanding force. Counts are unweighted; means use the stated weights. '
            'Bins are left-closed/right-open with 1 included in the last bin. Empty bins remain unknown. '
            'All six models’ bins in every population/year/group are retained in the raw result.', '',
            '| Region | Model | Bin | n | Mean p, battle | Recorded A-win share, battle | Mean p, campaign | Recorded A-win share, campaign |',
            '| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |']
    for region in REGIONS:
        s = primary['regions'][region]['calibration']
        for model in ('offset_force', 'expanding_force'):
            for a, b in zip(s['battle'][model], s['equal_campaign'][model], strict=True):
                cells = [a['mean_probability'], a['recorded_a_win_share'], b['mean_probability'], b['recorded_a_win_share']]
                out.append(f'| {region} | {model} | {a["lower"]:.1f}–{a["upper"]:.1f} | {a["n"]} | '
                           + ' | '.join('unknown' if v is None else f'{v:.6f}' for v in cells) + ' |')
    out += ['', '## Interpretation and stopping disposition', '',
            'This fixed correction does not transfer consistently across the earlier development years. '
            'Retain the expanding uncorrected comparator as the descriptive baseline. The failure ends '
            'this correction branch; it does not trigger a window search, another correction, final-set '
            'evaluation, commander model or wider evidence extraction.', '',
            'The design was frozen before this execution, but all development outcomes were historically '
            'familiar and 1813 had motivated the question. Five main years/seven groups, repeated calibration '
            'blocks, overlapping training sets, long operations and one compiler family provide limited '
            'replication. No significance test, bootstrap interval or confirmatory generalization claim is made.', '',
            'Event completion is a retrospective training-availability proxy, not a publication or contemporary '
            'information date. Whole-entry forces still lack an established opening clock/population. '
            'Compiler selection, rounded/qualified strength totals, strength-dependent winner coding and '
            'missing pairs remain the [prepared source-context limits](../../data/napoleonic/benchmark-v1/context.json), '
            'not repaired by a probability offset. The six convention passages were rechecked against '
            '`bodart-1908-transcription-v1`, printed pp. 45–47, and the three pinned page images. '
            'Raw SHA-256: `bf12437b6d19226ce127ce5d81e59d20358a5b1999ffe00f5ac6a8f8c20ef986`. '
            'The unchanged context retains exact quotes, locators and image hashes. '
            'Date roles retain the plan’s original raw/frame SHA-256 bindings '
            'and entry/field locators; no new historical adjudication occurs.', '',
            'The frozen baseline inputs, all previous numerical results, draft evidence and packets remain '
            'unchanged. The 52-entry final reservation remains intact; the two 1813 operations that finish '
            'in 1814 retain their original development IDs. Wider opening research and the appointment '
            'branch stay stopped. Extraction-review calibration remains prepared and unscored. '
            'No second-opinion prompt, separate review or subagent ran.', '',
            '## Execution and primary verification', '',
            f'- Immutable [raw result](../../{RESULT}), SHA-256 `{RESULT_SHA}`; '
            f'[exact proposal](../../{prep.PROPOSAL}), SHA-256 `{PROPOSAL_SHA}`.',
            f'- [Actual owner run authorization](../../{AUTH}), SHA-256 `{run["authorization_sha256"]}`, '
            'records the owner’s verbatim reply accepting execution. It binds the proposal, exact command '
            'and development-only scope. The 16 executing input/code/plan bindings are retained in the raw result.',
            '- The exact proposal command ran once with CPython ' + run['environment']['python'] + ': '
            '`python3 -m generalship.napoleonic_temporal_calibration_run --authorization '
            'data/napoleonic/temporal-calibration-v1/owner-run-authorization.json --out '
            'artifacts/napoleonic-temporal-calibration-run-v1.json`. The runner refuses overwrite.',
            '- The run performed 72 parameter fits across 24 scorable population/year folds: 48 force '
            'fits and 24 offsets, including deliberate repeated blocks and the indecisive no-op. '
            'These are fit calls, not 72 independent replications. There are 589 population-entry prediction '
            'rows / 3,534 probability values, with repeated entries across sensitivities.',
            f'- [Primary arithmetic verification](../../{VERIFICATION}) checks all 36 annual role assignments, '
            'every force/offset score equation, all 589 rows and 3,534 probabilities, '
            f'{verification["checks"]["summaries_checked"]} summaries / '
            f'{verification["checks"]["metric_values_checked"]} score values / '
            f'{verification["checks"]["calibration_bins_checked"]} bins, '
            'all paired losses/concentration and the continuation decision. It matches 141 original forward '
            'prediction rows across four populations. Arithmetic uses a second implementation with no fitting; '
            'this is primary verification, not a separate historical review.',
            '- Absolute tolerances are 2e-12 for saved arithmetic, 1e-7 for force score equations and '
            '1e-9 for offset score equations. The strictly convex penalized objectives make the stationary '
            'parameters sufficient to check the saved fits without rerunning optimization.',
            '- `python3 -m generalship.napoleonic_temporal_calibration_report` verifies this saved result. '
            '`--write` regenerates only this memo and its verification record. `make check` and '
            '`make reproduce` use the metadata planner and saved-result verifier; neither executes the '
            'historical job. Tests fit constructed cases only.', '']
    return '\n'.join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    run, data, plan, verification = verify(args.root)
    text = report(run, data, plan, verification)
    if args.write:
        (args.root / REPORT).write_text(text, encoding='utf-8')
        write_json(args.root / VERIFICATION, verification)
    require((args.root / REPORT).read_text(encoding='utf-8') == text, 'stale report')
    require(read_json(args.root / VERIFICATION) == verification, 'stale verification record')
    print(json.dumps(verification, indent=2))


if __name__ == '__main__':
    main()
