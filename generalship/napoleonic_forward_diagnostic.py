"""Exploratory 1813 arithmetic from saved forecasts; never fit or recalibrate."""

import argparse
from collections import Counter
import json
import math
from pathlib import Path
from statistics import fmean, median

from . import napoleonic_benchmark_report as saved
from .sources import digest, read_json, source_metadata_digest, source_registry, text_sections, write_json

BASE = 'data/napoleonic/forward-diagnostic-v1/'
SCOPE = BASE + 'scope.json'
EVIDENCE = BASE + 'evidence-checks.json'
CODE = 'generalship/napoleonic_forward_diagnostic.py'
OUTPUT = 'artifacts/napoleonic-forward-diagnostic-v1.json'
REPORT = 'docs/research/napoleonic-forward-diagnostic-v1.md'


def require(condition, message):
    if not condition:
        raise ValueError('Napoleonic forward diagnostic: ' + message)


def near(a, b):
    require(math.isclose(a, b, rel_tol=0, abs_tol=2e-12), f'{a} != {b}')


def compare_records(actual, expected, path='diagnostic'):
    """Allow only arithmetic rounding; retain exact structure, types and bindings."""
    require(type(actual) is type(expected), 'record type: ' + path)
    if isinstance(actual, float):
        near(actual, expected)
    elif isinstance(actual, dict):
        require(actual.keys() == expected.keys(), 'record keys: ' + path)
        for key in actual:
            compare_records(actual[key], expected[key], path + '.' + key)
    elif isinstance(actual, list):
        require(len(actual) == len(expected), 'record length: ' + path)
        for i, (a, b) in enumerate(zip(actual, expected)):
            compare_records(a, b, path + f'[{i}]')
    else:
        require(actual == expected, 'record value: ' + path)


def auc_pairs(scores, outcomes):
    """Count positive/negative pairs explicitly, with half credit for exact ties."""
    pairs = list(zip(scores, outcomes, strict=True))
    require(all(y in (0, 1) and math.isfinite(x) for x, y in pairs), 'finite binary AUC inputs')
    positive = [x for x, y in pairs if y == 1]
    negative = [x for x, y in pairs if y == 0]
    concordant = sum(a > b for a in positive for b in negative)
    tied = sum(a == b for a in positive for b in negative)
    total = len(positive) * len(negative)
    return {'positive': len(positive), 'negative': len(negative), 'pairs': total,
            'concordant': concordant, 'tied': tied,
            'auc': (concordant + tied / 2) / total if total else None}


def brier_accounting(predictions):
    require(bool(predictions), 'nonempty Brier population')
    p, y = ([r[k] for r in predictions] for k in ('force', 'y'))
    pbar, ybar = fmean(p), fmean(y)
    vp = fmean((v - pbar) ** 2 for v in p)
    vy = fmean((v - ybar) ** 2 for v in y)
    covariance = fmean((a - pbar) * (b - ybar) for a, b in zip(p, y))
    bias_squared = (pbar - ybar) ** 2
    equal_bias_squared = (0.5 - ybar) ** 2
    actual = fmean((a - b) ** 2 for a, b in zip(p, y))
    near(actual, bias_squared + vp + vy - 2 * covariance)
    near(actual - 0.25, bias_squared - equal_bias_squared + vp - 2 * covariance)
    return {'n': len(p), 'mean_probability': pbar, 'recorded_a_win_share': ybar,
            'mean_bias': pbar - ybar, 'mean_bias_squared': bias_squared,
            'prediction_variance': vp, 'outcome_variance': vy, 'covariance': covariance,
            'equal_odds_bias_squared': equal_bias_squared,
            'bias_cost_difference': bias_squared - equal_bias_squared,
            'spread_covariance_difference': vp - 2 * covariance,
            'brier': actual, 'force_minus_equal_brier': actual - 0.25}


def scores(predictions):
    require(bool(predictions), 'nonempty score population')
    return {m: fmean(saved.loss(r['force'], r['y'], m) for r in predictions)
            for m in ('log_loss', 'brier')}


def coverage(rows, labels):
    result = {}
    for key, subset in [('all', rows), ('eligible', [r for r in rows if r['eligible']]),
                        ('excluded', [r for r in rows if not r['eligible']])]:
        wins = sum(labels[r['battle_id']] for r in subset)
        result[key] = {'n': len(subset), 'recorded_a_wins': wins,
                       'recorded_a_win_share': wins / len(subset) if subset else None}
    result['paired_coverage'] = result['eligible']['n'] / len(rows) if rows else None
    result['side_dispositions'] = dict(sorted(Counter(s['disposition'] for r in rows
                                                     for s in r['sides'].values()).items()))
    return result


def balance(row):
    a, b = (row['sides'][s]['primary_value'] for s in ('A', 'B'))
    require(row['eligible'] and a > 0 and b > 0, 'eligible positive force pair')
    return (a - b) / (a + b)


def force_summary(rows, labels):
    values = [balance(r) for r in rows]
    strata = {}
    for name, sign in [('smaller', -1), ('equal', 0), ('larger', 1)]:
        subset = [r for r, x in zip(rows, values) if (x > 0) - (x < 0) == sign]
        wins = sum(labels[r['battle_id']] for r in subset)
        strata[name] = {'n': len(subset), 'recorded_a_wins': wins,
                        'recorded_a_win_share': wins / len(subset) if subset else None}
    return {'n': len(rows), 'mean': fmean(values), 'median': median(values),
            'minimum': min(values), 'maximum': max(values), 'strata': strata,
            'force_auc': auc_pairs(values, [labels[r['battle_id']] for r in rows])}


def paired_sensitivity(primary, sensitivity):
    common_ids = {r['battle_id'] for r in sensitivity}
    primary_ids = {r['battle_id'] for r in primary}
    require(len(common_ids) == len(sensitivity) and common_ids <= primary_ids, 'sensitivity subset')
    common = [r for r in primary if r['battle_id'] in common_ids]
    removed = [r for r in primary if r['battle_id'] not in common_ids]
    by_id = {r['battle_id']: r for r in common}
    require(all(r['y'] == by_id[r['battle_id']]['y'] for r in sensitivity), 'paired labels')
    all_scores, common_scores, removed_scores, sensitivity_scores = map(scores, (primary, common, removed, sensitivity))
    deltas = {}
    for metric in all_scores:
        near(all_scores[metric], (len(common) * common_scores[metric] + len(removed) * removed_scores[metric]) / len(primary))
        composition = common_scores[metric] - all_scores[metric]
        same_rows = sensitivity_scores[metric] - common_scores[metric]
        total = sensitivity_scores[metric] - all_scores[metric]
        near(total, composition + same_rows)
        deltas[metric] = {'case_removal_difference': composition,
                          'same_row_saved_model_difference': same_rows, 'total_difference': total}
    return {'common_ids': sorted(common_ids), 'removed_ids': sorted(primary_ids - common_ids),
            'primary_all': {'n': len(primary), **all_scores},
            'primary_common': {'n': len(common), **common_scores},
            'primary_removed': {'n': len(removed), **removed_scores},
            'unqualified_saved_common': {'n': len(sensitivity), **sensitivity_scores}, 'differences': deltas}


def selected_errors(predictions):
    ordered = sorted(predictions, key=lambda r: (-saved.loss(r['force'], r['y'], 'log_loss'), r['battle_id']))
    selected = ordered[:5]
    for group in sorted({r['campaign_group'] for r in predictions} - {r['campaign_group'] for r in selected}):
        selected.append(next(r for r in ordered if r['campaign_group'] == group))
    return [r['battle_id'] for r in selected]


def verify_passages(root, record, scope, indexed, predictions):
    require(record['scope_sha256'] == digest(root / SCOPE), 'passage scope binding')
    require(record['status'] == 'primary_verified' and record['separate_review'] is False
            and record['new_sources'] == 0 and record['source_families'] == 1, 'passage check status')
    require([r['battle_id'] for r in record['checks']] == selected_errors(predictions), 'largest-error selection')
    registry = source_registry(root)
    sections = {}
    outcomes = {r['battle_id']: r['y'] for r in predictions}
    for check in record['checks']:
        row = indexed[check['battle_id']]
        require(check['outcome_side_a'] == outcomes[check['battle_id']]
                and check['personnel_totals'] == {s: row['sides'][s]['primary_value'] for s in ('A', 'B')}
                and check['source_columns'] == {s: row['sides'][s]['source_column'] for s in ('A', 'B')}
                and check['place'] == row['place'] and check['campaign_group'] == row['campaign_group'], 'passage figures/outcome')
        citation = check['citation']
        source = registry[citation['source_id']]
        require(citation['raw_sha256'] == source['sha256'] == digest(root / source['path'])
                and citation['metadata_sha256'] == source_metadata_digest(source), 'passage source hash')
        if source['id'] not in sections:
            sections[source['id']] = text_sections((root / source['path']).read_text(encoding='utf-8'))
        require(' '.join(citation['quote'].split()) in ' '.join(sections[source['id']][citation['section']].split()), 'inspected quotation')
        require(all(any(c['quote'] == citation['quote'] and c['section'] == citation['section']
                        and c['source_id'] == citation['source_id'] for c in row['sides'][s]['citations'])
                    for s in ('A', 'B')), 'passage linked to both source sides')
        image = check['page_image']; image_source = registry[image['source_id']]
        require(image['sha256'] == image_source['sha256'] == digest(root / image_source['path'])
                and image['path'] == image_source['path'] and image['metadata_sha256'] == source_metadata_digest(image_source)
                and all({'source_id': image['source_id'], 'sha256': image['sha256']} in row['sides'][s]['page_images']
                        for s in ('A', 'B')), 'inspected image hash/link')
        require(check['correction_required'] is False and bool(check['interpretation_en'])
                and bool(check['note_check']) and len(check['remaining_limits']) == 2, 'passage disposition/limits')


def build(root):
    scope = read_json(root / SCOPE)
    require(scope['authorizes_refit'] is False and scope['authorizes_future_run'] is False
            and scope['reserved_final_numerical_use'] is False, 'diagnostic-only scope')
    for path, sha in scope['bindings'].items():
        require(digest(root / path) == sha, 'changed frozen diagnostic input: ' + path)
    run, data, labels, verification = saved.verify(root)
    rows = data['entries']; indexed = {r['battle_id']: r for r in rows}
    before = [r for r in rows if r['start_year'] <= 1812]
    after = [r for r in rows if r['start_year'] == 1813]
    training = [r for r in before if r['eligible']]
    eligible = [r for r in after if r['eligible']]
    excluded = [r for r in after if not r['eligible']]
    for field, subset, n in [('prior_development_ids', before, 209), ('test_development_ids', after, 64),
                             ('saved_training_ids', training, 157), ('saved_test_ids', eligible, 37),
                             ('excluded_test_ids', excluded, 27)]:
        require(scope[field] == [r['battle_id'] for r in subset] and len(subset) == n, 'scope membership: ' + field)
    reservation = set(read_json(root / (saved.BASE + 'scope.json'))['reserved_final_ids'])
    require(len(reservation) == 52 and not reservation & set(indexed) and set(labels) == set(indexed), 'final separation')
    forward = run['populations']['primary']['forward_1813']
    predictions = forward['predictions']
    fold = forward['folds'][0]
    require(fold['train_ids'] == scope['saved_training_ids'] and fold['test_ids'] == scope['saved_test_ids']
            and {r['battle_id'] for r in predictions} == set(scope['saved_test_ids']), 'saved forward membership')
    evidence = read_json(root / EVIDENCE)
    verify_passages(root, evidence, scope, indexed, predictions)
    case_rows = []
    for rank, p in enumerate(sorted(predictions, key=lambda r: (-saved.loss(r['force'], r['y'], 'log_loss'), r['battle_id'])), 1):
        row = indexed[p['battle_id']]
        case_rows.append({**p, 'place': row['place'], 'log_loss_rank': rank, 'force_balance': balance(row),
                          'personnel_totals': {s: row['sides'][s]['primary_value'] for s in ('A', 'B')},
                          'scores': {m: saved.loss(p['force'], p['y'], m) for m in ('log_loss', 'brier')},
                          'qualifiers': {s: {k: row['sides'][s][k] for k in ('approximate', 'footnote_markers', 'context_footnote_markers')}
                                         for s in ('A', 'B')}})
    campaigns = {}
    for group in sorted({r['campaign_group'] for r in after}):
        group_predictions = [r for r in predictions if r['campaign_group'] == group]
        campaigns[group] = {'coverage': coverage([r for r in after if r['campaign_group'] == group], labels),
                            'mean_probability': fmean(r['force'] for r in group_predictions),
                            'auc': auc_pairs([r['force'] for r in group_predictions], [r['y'] for r in group_predictions]),
                            'scores': scores(group_predictions)}
    accounting = brier_accounting(predictions)
    for m, value in scores(predictions).items():
        near(value, forward['metrics']['battle']['force'][m])
    near(accounting['brier'], forward['metrics']['battle']['force']['brier'])
    auc = auc_pairs([r['force'] for r in predictions], [r['y'] for r in predictions])
    test_force = force_summary(eligible, labels)
    require(auc == test_force['force_auc'], 'saved monotone ordering')
    bindings = {**scope['bindings'], **{p: digest(root / p) for p in (SCOPE, EVIDENCE, CODE, saved.CODE)}}
    return {'kind': 'napoleonic_1813_saved_forecast_diagnostic', 'version': 1,
            'status': 'exploratory_primary_verified', 'separate_review': False,
            'absolute_arithmetic_tolerance': 2e-12,
            'historical_refits_performed': 0, 'new_forecasts_generated': 0,
            'reserved_final_entries_used': 0, 'reserved_final_entries': 52,
            'input_sha256': bindings, 'saved_run_checks': verification['checks'],
            'coverage': {'through_1812': coverage(before, labels), '1813': coverage(after, labels)},
            'force_balance': {'through_1812_training': force_summary(training, labels), '1813_test': test_force},
            'discrimination': auc, 'brier_accounting': accounting,
            'saved_calibration_bins': forward['calibration']['battle']['force'],
            'forward_scores': forward['metrics']['battle'], 'campaigns': campaigns,
            'paired_sensitivity': paired_sensitivity(predictions, run['populations']['unqualified_totals']['forward_1813']['predictions']),
            'all_37_saved_predictions_by_loss': case_rows,
            'all_27_exclusions': [{'battle_id': r['battle_id'], 'place': r['place'], 'campaign_group': r['campaign_group'],
                                  'y': labels[r['battle_id']], 'exclusions': r['exclusions'],
                                  'sides': {s: {k: v[k] for k in ('primary_value', 'disposition', 'reasons')}
                                            for s, v in r['sides'].items()}} for r in excluded],
            'passage_checks': evidence['checks']}


def report(d):
    a = d['brier_accounting']; paired = d['paired_sensitivity']
    out = ['# Napoleonic 1813 forward diagnostic v1', '',
           'Primary-verified, exploratory analysis after the completed benchmark. No refit or recalibration.', '',
           '**The saved forecasts overpredict French/allied wins on average, while retaining useful ordering '
           'within these 37 compiler records.** Coverage and recorded outcome shares also change. This supports '
           'designing one training-only temporal calibration comparison; it does not establish that a calibration '
           'repair will generalize or justify a commander model.', '',
           '## Scope and source authority', '',
           'The [accepted bounded scope](../../' + SCOPE + ') binds the completed run and frozen inputs. '
           'A is France and its allies; outcomes are Bodart’s recorded winners. The forward model was trained '
           'through 1812 on 157 eligible entries and scored on 37 eligible 1813 entries. This memo retains all '
           '64 development entries in 1813, including the 27 exclusions. All 52 final entries remain reserved '
           'and unused numerically. The 1813 result has now informed this exploratory diagnosis and is not a '
           'fresh validation set for a future change.', '',
           '## Coverage and recorded outcomes', '',
           '| Period / subset | Entries | Recorded A wins | A-win share |',
           '| --- | ---: | ---: | ---: |']
    for period, c in d['coverage'].items():
        for subset in ('all', 'eligible', 'excluded'):
            r = c[subset]
            out.append(f'| {period} / {subset} | {r["n"]} | {r["recorded_a_wins"]} | {r["recorded_a_win_share"]:.2%} |')
    out += ['', 'Paired coverage falls from 157/209 (75.12%) through 1812 to 37/64 (57.81%) in 1813. '
            'The lower recorded A-win share persists in the complete 1813 development frame (18/64); '
            'eligibility raises it to 13/37. This is descriptive selection, not a missing-data adjustment. '
            'Missing or ambiguous force extracts are not zero forces or zero outcomes.', '',
            '| 1813 campaign | Eligible / all | Excluded | Recorded A wins, eligible | Mean saved probability | AUC pairs | AUC |',
            '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    for group, c in d['campaigns'].items():
        cov = c['coverage']; u = c['auc']
        out.append(f'| {group} | {cov["eligible"]["n"]} / {cov["all"]["n"]} | {cov["excluded"]["n"]} | '
                   f'{cov["eligible"]["recorded_a_wins"]} | {c["mean_probability"]:.6f} | {u["pairs"]} | {u["auc"]:.6f} |')
    out += ['', 'The machine-readable [diagnostic](../../' + OUTPUT + ') retains side dispositions, '
            'all 27 excluded identities with reasons and recorded labels, and all 37 saved forecasts with losses. '
            'It preserves the original populations; no missing force is inferred.', '',
            '## Force balance and discrimination', '',
            '`x = (A-B)/(A+B)` uses the two frozen printed personnel totals. These are entry-level compiler '
            'figures; exact state time and complete combatant/all-ranks coverage remain unestablished.', '',
            '| Eligible period | Mean x | Median x | Minimum | Maximum |',
            '| --- | ---: | ---: | ---: | ---: |']
    for period, f in d['force_balance'].items():
        out.append(f'| {period} | {f["mean"]:.6f} | {f["median"]:.6f} | {f["minimum"]:.6f} | {f["maximum"]:.6f} |')
    out += ['', '| A force relative to B | Through 1812: wins / entries | 1813: wins / entries |',
            '| --- | ---: | ---: |']
    for name in ('smaller', 'equal', 'larger'):
        cells = [f'{d["force_balance"][p]["strata"][name]["recorded_a_wins"]} / {d["force_balance"][p]["strata"][name]["n"]}'
                 for p in ('through_1812_training', '1813_test')]
        out.append('| ' + name + ' | ' + ' | '.join(cells) + ' |')
    u = d['discrimination']; train_auc = d['force_balance']['through_1812_training']['force_auc']
    out += ['', 'The 1813 A side is smaller in 26/37 entries, versus 77/157 earlier. Its win share also '
            'falls within the broad smaller-force stratum (38/77 to 4/26). These coarse strata do not hold '
            'exact force balance or historical context fixed; they cannot separate a historical mechanism '
            'from source, case-mix or coding changes. Each equal-force stratum has only one entry.', '',
            f'On the saved 1813 forecasts, AUC is **{u["auc"]:.6f}**: {u["concordant"]} concordant '
            f'and {u["tied"]} tied pairs among {u["positive"]} recorded wins × {u["negative"]} losses '
            f'= {u["pairs"]} pairs. AUC gives half credit to exact ties. These pairs share entries and '
            'are not independent observations. Pooled AUC includes cross-campaign pairs; Peninsula has '
            'only eight cases and AUC 0.600000. No confidence or uniform-transfer claim follows.', '',
            f'The training force-balance AUC is {train_auc["auc"]:.6f} '
            f'({train_auc["concordant"]} concordant and {train_auc["tied"]} tied of {train_auc["pairs"]} pairs). '
            'This is an in-sample descriptive association, not another validation result. The saved forward '
            'slope is positive, so force balance and its saved probabilities give identical test ordering.', '',
            '## Calibration and exact Brier accounting', '',
            f'Mean saved probability is **{a["mean_probability"]:.6f}** versus recorded A-win share '
            f'**{a["recorded_a_win_share"]:.6f}**: an average overprediction of {100*a["mean_bias"]:.2f} percentage '
            'points. The original fixed bins show where that discrepancy occurs; the highest bin is much '
            'closer to its observed share. No new bins, recalibrated forecasts or fitted intercept are created.', '',
            '| Original probability bin | Entries | Mean probability | Recorded A-win share |',
            '| --- | ---: | ---: | ---: |']
    for b in d['saved_calibration_bins']:
        cells = ['unknown' if b[k] is None else f'{b[k]:.6f}' for k in ('mean_probability', 'recorded_a_win_share')]
        out.append(f'| {b["lower"]:.1f}–{b["upper"]:.1f} | {b["n"]} | ' + ' | '.join(cells) + ' |')
    out += ['', 'Bins are left-closed/right-open, including 1 in the final bin. Empty means remain unknown.', '',
            'Using population variances/covariance (`1/n`), the exact identity is '
            '`Brier = (mean(p)-mean(y))² + Var(p) + Var(y) - 2 Cov(p,y)`. Relative to fixed equal odds:', '',
            '| Arithmetic term | Brier difference |', '| --- | ---: |',
            f'| Difference in squared mean bias | {a["bias_cost_difference"]:+.9f} |',
            f'| Prediction variance minus twice covariance | {a["spread_covariance_difference"]:+.9f} |',
            f'| Total: force minus equal odds | {a["force_minus_equal_brier"]:+.9f} |', '',
            f'The terms reconcile force Brier {a["brier"]:.9f} with equal odds 0.250000000. '
            'This is arithmetic accounting, not a causal attribution or a reliability/resolution estimate '
            'from fitted bins. Useful ordering and poor average calibration can coexist. It does not prove '
            'that an intercept-only repair would work on another period. Original forward log loss remains '
            '0.691121738 versus equal odds 0.693147181; neither score is replaced.', '',
            '## Same-row sensitivity comparison', '',
            'The already-executed unqualified-total model has 133 training entries and 30 test entries. '
            'The seven removed test entries are retained in the diagnostic. Comparing the same 30 entries '
            'separates the arithmetic effect of removing cases from the difference between the two saved models.', '',
            '| Saved forecasts / test subset | Entries | Log loss | Brier |',
            '| --- | ---: | ---: | ---: |']
    for key in ('primary_all', 'primary_common', 'primary_removed', 'unqualified_saved_common'):
        r = paired[key]
        out.append(f'| {key} | {r["n"]} | {r["log_loss"]:.9f} | {r["brier"]:.9f} |')
    out += ['', '| Difference: unqualified common minus primary all | Case removal | Same-row saved models | Total |',
            '| --- | ---: | ---: | ---: |']
    for metric, r in paired['differences'].items():
        out.append(f'| {metric} | {r["case_removal_difference"]:+.9f} | {r["same_row_saved_model_difference"]:+.9f} | {r["total_difference"]:+.9f} |')
    out += ['', 'The primary-all score also equals `(30 × primary_common + 7 × primary_removed) / 37`. '
            'Most of the worsening here comes from case removal in this arithmetic comparison. The small '
            'remaining difference uses two saved models with different training populations; it is not a '
            'causal effect of a source annotation. No variant is selected or refitted.', '',
            '## Five largest errors: inspected source passages', '',
            'The five largest primary forward log losses cover both 1813 campaigns, so the scope’s campaign '
            'augmentation adds no entry. Each complete transcription entry, applicable notes and pinned '
            'page image was re-inspected by the primary. All five are recorded A losses. Their totals, '
            'side assignments and outcomes match the inspected pages; no mechanical correction was found '
            'in this purposive sample. This does not verify the other 32 test entries or adjudicate historical truth.', '',
            'Text source: `bodart-1908-transcription-v1`, raw SHA-256 '
            '`bf12437b6d19226ce127ce5d81e59d20358a5b1999ffe00f5ac6a8f8c20ef986`. '
            'The [primary inspection record](../../' + EVIDENCE + ') retains locators, English renderings, '
            'note applicability, source metadata hashes and the five image hashes.', '']
    cases = {r['battle_id']: r for r in d['all_37_saved_predictions_by_loss']}
    for check in d['passage_checks']:
        b = check['battle_id']; r = cases[b]; c = check['citation']; im = check['page_image']
        out += [f'### {b}: {check["place"]}', '',
                f'A/B printed personnel: {check["personnel_totals"]["A"]:,} / {check["personnel_totals"]["B"]:,}; '
                f'saved probability {r["force"]:.6f}; log loss {r["scores"]["log_loss"]:.6f}.', '',
                f'> {c["quote"]}', '', check['interpretation_en'], '', check['note_check'], '',
                f'Locator: {c["locator"]}; section `{c["section"]}`. Image '
                f'[`{im["source_id"]}`](../../{im["path"]}), SHA-256 `{im["sha256"]}`.', '']
    out += ['## Decision and stopping point', '',
            '**Recommended next action: design one development-only rolling-forward calibration comparison '
            'before any further fit.** Specify the eligible year/campaign folds and minimum training support, '
            'a single training-only calibration alternative and fixed comparators, paired scores and coverage, '
            'and a decision rule before execution. Use earlier development folds to assess whether a correction '
            'travels through time; treat this already-inspected 1813 check as exploratory. Bind a separate '
            'proposal and obtain exact owner run authorization before any new historical fit. Do not consume '
            'the 52 reserved entries to choose the method.', '',
            'The observed bias supplies a concrete reason to design that test. It does not identify a '
            'historical cause, guarantee recalibration success, admit a feature or support commander ratings. '
            'One compiler family, selection, strength-dependent winner coding, uncertain populations, rounded '
            'figures, missing pairs and only two 1813 groups remain limits. Existing inspected conventions '
            'and exact source passages remain in the [original context](../../data/napoleonic/benchmark-v1/context.json). '
            'Wider strict-opening extraction and the stopped appointment branch remain parked.', '',
            '## Reproduction and primary verification', '',
            '- `python3 -m generalship.napoleonic_forward_diagnostic` verifies bound inputs, all saved-run '
            'arithmetic, denominator membership, final separation, pair-count AUC, Brier and paired-score '
            'identities, source quotations/image hashes, and both generated diagnostic files. Derived '
            'floating-point values allow absolute rounding error up to `2e-12`; types, counts, identities '
            'and SHA-256 bindings match exactly. `--write` '
            'regenerates only this memo and its JSON. It never invokes a fitter or recalibration.',
            '- `make check` and `make reproduce` include this saved-forecast path. All 37 forecasts and 27 '
            'exclusions are retained; no previous run, frozen input, source record or prepared packet changes.',
            f'- Original run SHA-256 `{saved.RESULT_SHA}`; the diagnostic JSON binds its own code, scope '
            'and actual passage-check record as well as the original inputs. Verification is primary, '
            'with no separate review, subagent or second-opinion prompt.', '']
    return '\n'.join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    diagnostic = build(args.root)
    text = report(diagnostic)
    if args.write:
        write_json(args.root / OUTPUT, diagnostic)
        (args.root / REPORT).write_text(text, encoding='utf-8')
    compare_records(diagnostic, read_json(args.root / OUTPUT))
    require((args.root / REPORT).read_text(encoding='utf-8') == text, 'stale diagnostic memo')
    print(json.dumps({'status': diagnostic['status'], 'saved_test_entries': 37,
                      'excluded_test_entries': 27, 'primary_passage_checks': len(diagnostic['passage_checks']),
                      'historical_refits_performed': 0, 'reserved_final_entries_used': 0}))


if __name__ == '__main__':
    main()
