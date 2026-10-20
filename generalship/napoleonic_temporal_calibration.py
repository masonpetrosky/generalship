"""Freeze a development-only temporal calibration plan; never load outcome labels or fit."""

import argparse
from collections import defaultdict
from datetime import date
import hashlib
import json
from pathlib import Path

from . import napoleonic_benchmark as benchmark
from .sources import digest, read_json, write_json

BASE = 'data/napoleonic/temporal-calibration-v1/'
SCOPE, PROTOCOL, PROPOSAL = (BASE + name + '.json' for name in ('scope', 'protocol', 'run-proposal'))
DATA = 'artifacts/napoleonic-benchmark-v1.json'
ARTIFACT = 'artifacts/napoleonic-temporal-calibration-plan-v1'
DESIGN = 'docs/napoleonic-temporal-calibration-v1.md'
CODE = 'generalship/napoleonic_temporal_calibration.py'
RUN_CODE = 'generalship/napoleonic_temporal_calibration_run.py'
RESULT = 'artifacts/napoleonic-temporal-calibration-run-v1.json'
MODELS = ('offset_force', 'same_base_force', 'expanding_force', 'expanding_prior', 'recent_prior', 'equal_odds')
POPULATIONS = ('primary', 'exclude_indecisive', 'exclude_no_combat', 'unqualified_totals')


def require(condition, message):
    if not condition:
        raise ValueError('Napoleonic temporal calibration: ' + message)


def fixed_protocol():
    return {'kind': 'napoleonic_temporal_calibration_protocol', 'version': 1,
            'authorizes_historical_fit': False, 'reserved_final_numerical_use': False,
            'candidate': 'one_ridge1_logit_offset_on_latest_completed_campaign_year_block',
            'models': list(MODELS), 'populations': list(POPULATIONS),
            'feature': '(A-B)/(A+B)', 'force_ridge': 1.0, 'offset_ridge': 1.0,
            'minimum_base_rows': 10, 'minimum_calibration_rows': 10,
            'target_years': list(range(1805, 1814)), 'decision_years': list(range(1808, 1813)),
            'secondary_years': [1813], 'group_completion': 'maximum_known_end_date_of_every_development_group_member',
            'training_cutoff': 'group_completion_strictly_before_January_1_of_target_year',
            'calibration_block': 'all_available_groups_in_latest_nonempty_completion_calendar_year',
            'base_block': 'all_earlier_available_complete_groups',
            'calibration_time_guard': 'every_base_group_must_finish_before_earliest_start_of_every_calibration_member',
            'refit_base_after_offset': False, 'fallback': 'none; retain unscored fold with reasons',
            'weightings': ['battle', 'equal_campaign'], 'calibration_edges': [0., .2, .4, .6, .8, 1.],
            'bootstrap': None, 'model_selection': False, 'decision_tolerance': 1e-12,
            'continuation_rule': {
                'primary': 'lower_log_loss_and_nonhigher_Brier_than_every_comparator_under_both_weightings',
                'year_consistency': 'lower_log_loss_than_expanding_force_in_at_least_3_of_5_decision_years',
                'sensitivity_veto': 'unqualified_totals_must_not_worsen_log_loss_or_Brier_vs_expanding_force_under_either_weighting',
                '1813_affects_decision': False, 'missing_required_scores': 'not_assessable_not_passed',
                'interpretation': 'exploratory_continuation_only_not_feature_admission_or_rating_gate'}}


def group_metadata(rows):
    require(len({r['battle_id'] for r in rows}) == len(rows), 'duplicate development entry')
    groups = defaultdict(list)
    for row in rows:
        require(type(row['start_year']) is int, 'integer cohort year')
        for key in ('start_date', 'end_date'):
            value = row[key]
            require(value is None or (isinstance(value, str) and date.fromisoformat(value).isoformat() == value), 'ISO event date')
        require(row['start_date'] is None or row['end_date'] is None
                or row['start_date'] <= row['end_date'], 'reversed event interval')
        groups[row['campaign_group']].append(row)
    result = {}
    for group, members in sorted(groups.items()):
        years = {r['start_year'] for r in members}
        require(len(years) == 1, 'frozen source group spans cohort years')
        ends = [r['end_date'] for r in members]
        starts = [r['start_date'] for r in members]
        completion = max(ends) if all(ends) else None
        result[group] = {'cohort_year': years.pop(), 'member_ids': sorted(r['battle_id'] for r in members),
                         'completion_date': completion,
                         'earliest_start_date': min(starts) if all(starts) else None,
                         'completion_locators': [f"{r['battle_id']}.end_date" for r in members
                                                  if completion is not None and r['end_date'] == completion],
                         'missing_end_ids': sorted(r['battle_id'] for r in members if r['end_date'] is None)}
    return result


def folds(rows, selected, protocol):
    """Only source metadata and eligibility enter planning. No labels are accepted."""
    groups = group_metadata(rows)
    selected_ids = {r['battle_id'] for r in selected}
    require(len(selected_ids) == len(selected) and selected_ids <= {r['battle_id'] for r in rows}, 'selected membership')
    output = []
    for year in protocol['target_years']:
        cutoff = f'{year}-01-01'
        available = [g for g, m in groups.items() if m['cohort_year'] < year
                     and m['completion_date'] is not None and m['completion_date'] < cutoff]
        calibration_year = max((int(groups[g]['completion_date'][:4]) for g in available), default=None)
        calibration_groups = [g for g in available if int(groups[g]['completion_date'][:4]) == calibration_year]
        base_groups = [g for g in available if g not in calibration_groups]
        starts = [groups[g]['earliest_start_date'] for g in calibration_groups]
        calibration_start = min(starts) if starts and all(starts) else None
        test_groups = [g for g, m in groups.items() if m['cohort_year'] == year]
        deferred = [g for g, m in groups.items() if m['cohort_year'] < year and g not in available]
        ids_for = lambda gs, eligible: sorted(r['battle_id'] for r in rows if r['campaign_group'] in gs
                                             and (not eligible or r['battle_id'] in selected_ids))
        base, calibration, test = (ids_for(gs, True) for gs in (base_groups, calibration_groups, test_groups))
        reasons = []
        if not test:
            reasons.append('empty_eligible_test')
        if len(base) < protocol['minimum_base_rows']:
            reasons.append('insufficient_base_rows')
        if len(calibration) < protocol['minimum_calibration_rows']:
            reasons.append('insufficient_calibration_rows')
        if calibration_groups and calibration_start is None:
            reasons.append('unknown_calibration_start')
        elif calibration_start and any(groups[g]['completion_date'] >= calibration_start for g in base_groups):
            reasons.append('base_not_complete_before_calibration_start')
        region = 'decision' if year in protocol['decision_years'] else 'reused_1813_secondary' if year in protocol['secondary_years'] else 'warmup'
        output.append({'target_year': year, 'cutoff': cutoff, 'region': region,
                       'calibration_start': calibration_start,
                       'status': 'not_estimable' if reasons else 'planned', 'reasons': reasons,
                       'latest_available_completion_year': calibration_year,
                       'base_groups': base_groups, 'calibration_groups': calibration_groups,
                       'test_groups': test_groups, 'deferred_earlier_groups': deferred,
                       'base_ids': base, 'calibration_ids': calibration, 'expanding_ids': sorted(base + calibration),
                       'test_ids': test, 'all_test_ids': ids_for(test_groups, False),
                       'excluded_test_ids': sorted(set(ids_for(test_groups, False)) - set(test)),
                       'deferred_earlier_ids': ids_for(deferred, True)})
    return output


def build(root):
    scope, protocol = read_json(root / SCOPE), read_json(root / PROTOCOL)
    require(protocol == fixed_protocol(), 'changed fixed protocol')
    require(scope['authorizes_historical_fit'] is False and scope['preparation_only'] is True, 'design-only owner scope')
    for path, sha in scope['bindings'].items():
        require(digest(root / path) == sha, 'changed frozen input: ' + path)
    benchmark.validate_proposal(root)
    data = read_json(root / DATA)
    rows = data['entries']
    partition = read_json(root / 'data/napoleonic/methods-v1/evaluation.json')
    require([r['battle_id'] for r in rows] == scope['development_ids'] == partition['development']
            and len(rows) == 273, 'development denominator')
    final = set(scope['reserved_final_ids'])
    require(len(final) == 52 and scope['reserved_final_ids'] == partition['reserved_final']
            and not final & {r['battle_id'] for r in rows}, 'final reservation')
    metadata = group_metadata(rows)
    require({g: sorted(v['member_ids']) for g, v in metadata.items()}
            == {g: sorted(v) for g, v in scope['development_groups'].items()}, 'whole frozen groups')
    populations = {}
    for population in POPULATIONS:
        selected = benchmark.population_rows(data, population)
        planned = folds(rows, selected, protocol)
        regions = {}
        for name in ('warmup', 'decision', 'reused_1813_secondary'):
            fs = [f for f in planned if f['region'] == name]
            regions[name] = {'all_entries': sum(len(f['all_test_ids']) for f in fs),
                             'eligible_entries': sum(len(f['test_ids']) for f in fs),
                             'planned_scored_entries': sum(len(f['test_ids']) for f in fs if f['status'] == 'planned'),
                             'excluded_entries': sum(len(f['excluded_test_ids']) for f in fs),
                             'planned_years': [f['target_year'] for f in fs if f['status'] == 'planned'],
                             'groups': sorted({g for f in fs for g in f['test_groups']})}
        require(sum(r['all_entries'] for r in regions.values()) == 273, 'region denominator')
        populations[population] = {'eligible_entries': len(selected), 'excluded_ids': sorted(
            {r['battle_id'] for r in rows} - {r['battle_id'] for r in selected}), 'regions': regions, 'folds': planned}
    fits = sum(3 for p in populations.values() for f in p['folds'] if f['status'] == 'planned')
    return {'kind': 'napoleonic_temporal_calibration_prepared_plan', 'version': 1,
            'status': 'primary_verified_preparation_only', 'historical_fits_performed': 0,
            'historical_forecasts_generated': 0, 'historical_outcome_labels_loaded': False,
            'owner_run_authorization_created': False, 'reserved_final_entries_used': 0,
            'development_entries': 273, 'development_groups': len(metadata), 'reserved_final_entries': 52,
            'planned_parameter_fits': fits, 'models': list(MODELS), 'group_metadata': metadata,
            'date_provenance': {'source_id': benchmark.SOURCE,
                                'raw_sha256': scope['bindings']['data/raw/bodart-1908-v1/transcription.txt'],
                                'frame_path': 'data/napoleonic/frame-v1.json',
                                'frame_sha256': scope['bindings']['data/napoleonic/frame-v1.json'],
                                'basis': 'unchanged encoded entry start/end dates; metadata audit only, no new page inspection'},
            'input_sha256': {p: digest(root / p) for p in (SCOPE, PROTOCOL, DESIGN, CODE, RUN_CODE)},
            'populations': populations,
            'exclusion_ledger': [{'battle_id': r['battle_id'], 'campaign_group': r['campaign_group'],
                                  'eligible': r['eligible'], 'reasons': r['exclusions']}
                                 for r in rows]}


def report(plan):
    out = ['# Prepared temporal calibration test v1', '',
           'Primary-verified preparation only. No historical label was loaded into a fit, '
           'no historical forecast was generated and no run authorization was created.', '',
           '## Fixed question and method', '',
           'Test one ridge-1 additive logit offset, estimated from the latest fully completed '
           'campaign completion-year block. Its base force model uses earlier completed groups '
           'and stays fixed after correction. Compare it with the same uncorrected base, a force '
           'model fitted on all available groups, expanding/recent Laplace priors and equal odds. '
           'All six models score identical test entries within each population.', '',
           'Group completion is the maximum known end date of every development member, including '
           'ineligible members. A missing end blocks the entire group. Groups finishing on or '
           'after January 1 are unavailable for that year. This is a retrospective temporal '
           'safeguard, not proof of source publication or a historical information set.', '',
           'The base groups must also finish strictly before the earliest known start of every '
           'calibration member. An unknown calibration start or overlap makes the entire paired '
           'fold not estimable, with no alternate block. Every scorable prepared fold satisfies this guard.', '',
           '## Frozen group availability', '',
           'Locators refer to the unchanged prepared dataset’s `battle_id.end_date` fields. '
           'These are metadata checks, not fresh source adjudication or a change to the frozen groups.', '',
           '| Frozen group | Entries | Last recorded end | Controlling entry locator(s) |',
           '| --- | ---: | --- | --- |']
    for group, m in plan['group_metadata'].items():
        out.append(f'| {group} | {len(m["member_ids"])} | {m["completion_date"] or "unknown"} | '
                   + ', '.join(m['completion_locators']) + ' |')
    provenance = plan['date_provenance']
    out += ['', f'Date provenance: `{provenance["source_id"]}`, raw SHA-256 `{provenance["raw_sha256"]}`; '
            f'frame SHA-256 `{provenance["frame_sha256"]}`. This task checks the frozen metadata and '
            'its temporal use; it performs no new page inspection or date correction.', '',
            '## Every population and annual fold', '',
            'Counts below are eligibility and planned-fit counts, never predictive results. '
            'Each scorable fold uses one base force fit, one offset fit and one expanding force fit. '
            'Fixed minimum support is ten base and ten calibration rows; this is a pragmatic floor, '
            'not evidence of adequate statistical precision. There is no fallback to another window.', '']
    for population, p in plan['populations'].items():
        out += [f'### {population}', '',
                f'{p["eligible_entries"]}/273 eligible; {len(p["excluded_ids"])} excluded. '
                'All identities, role assignments and exclusions remain in the JSON.', '',
                '| Test cohort year | Region | Calibration completion year | Base | Calibration | Available expanding | Deferred earlier eligible | Test eligible / all | Status |',
                '| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |']
        for f in p['folds']:
            out.append(f'| {f["target_year"]} | {f["region"]} | {f["latest_available_completion_year"] or "unknown"} | '
                       f'{len(f["base_ids"])} | {len(f["calibration_ids"])} | '
                       f'{len(f["expanding_ids"])} | {len(f["deferred_earlier_ids"])} | '
                       f'{len(f["test_ids"])} / {len(f["all_test_ids"])} | {f["status"]} |')
        out.append('')
    p = plan['populations']['primary']['regions']
    out += ['## Decision population and limits', '',
            f'The primary decision region is 1808–1812: **{p["decision"]["planned_scored_entries"]}/'
            f'{p["decision"]["all_entries"]} entries, five annual folds and seven complete source groups**. '
            f'All {p["decision"]["excluded_entries"]} excluded entries remain visible. '
            f'The 1805–1807 warmup retains {p["warmup"]["all_entries"]} entries '
            f'({p["warmup"]["eligible_entries"]} eligible), with no outer score. '
            'The reused 1813 region retains 37/64 test entries and 27 exclusions as secondary diagnostics '
            'only; its score cannot change the continuation decision.', '',
            'All development outcomes were exposed by prior work. This is an exploratory follow-up fixed '
            'before its own execution, not a fresh confirmation. The same calibration block repeats in '
            '1808–1809 and 1810–1812 when later complete groups are unavailable; it is not necessarily '
            'the immediately preceding start-year cohort. Earlier test outcomes can become later training '
            'data after their whole group completes. Overlapping training and operations remain dependencies.', '',
            'Two eligible development entries starting in 1813 finish in 1814; their IDs remain development '
            'under the existing reservation. No final ID is reclassified. Whole-entry personnel figures '
            'still have uncertain population/time and are not contemporary opening-force forecasts.', '',
            '## Fixed continuation rule', '',
            'On the primary 1808–1812 region, the candidate must lower log loss and not worsen Brier '
            'against every comparator under both battle and equal-campaign weighting. It must also '
            'lower log loss against expanding force in at least three of five years. The unqualified-total '
            'sensitivity vetoes continuation if either score worsens against expanding force under either '
            'weighting. A missing required score yields not assessable. Numerical tolerance is `1e-12`.', '',
            'This is a pragmatic exploratory continuation rule, not a significance test, feature-admission '
            'contract or the methods-v1 commander-rating gate. No bootstrap confidence claim is proposed '
            'for five annual folds/seven source groups. Publish every score, paired difference, yearly/group '
            'result, fixed calibration bin and case contribution, including failures. No alternative '
            'window, offset penalty or best sensitivity is selected after results.', '',
            '## Bound execution proposal and stop', '',
            f'The exact proposal binds the code, design, inputs and this plan: '
            f'[proposal](../{PROPOSAL}); [full design](../{DESIGN}); '
            f'[plan JSON]({Path(ARTIFACT).name}.json). A future authorized run proposes '
            f'**{plan["planned_parameter_fits"]} parameter fits across 24 scorable population/year folds** '
            '(two force fits and one one-parameter offset per fold). This preparation performs zero.', '',
            '`python3 -m generalship.napoleonic_temporal_calibration` verifies the prepared plan and proposal. '
            '`--write` restores only the two plan files; frozen input/code changes cannot silently rebind '
            'the proposal. `make check` and `make reproduce` never invoke the historical runner.', '',
            'Preparation stops here. A separate exact owner run authorization is required before any '
            'historical fit. All 52 final entries remain unused numerically. Original sources, dossiers, '
            'measurements, model inputs, runs and diagnostics retain their bytes. Wider opening extraction, '
            'the appointment branch and the unscored extraction-review sample remain parked. No separate '
            'reviewer, subagent or second-opinion prompt ran.', '']
    return '\n'.join(out)


def proposal(root, output_hashes=None):
    paths = [SCOPE, PROTOCOL, DESIGN, CODE, RUN_CODE, DATA, benchmark.SCOPE, benchmark.PROTOCOL,
             benchmark.PROPOSAL, 'generalship/baseline.py', 'generalship/napoleonic_benchmark.py',
             'generalship/napoleonic_benchmark_run.py', 'generalship/sources.py', 'generalship/__init__.py',
             ARTIFACT + '.json', ARTIFACT + '.md']
    return {'kind': 'napoleonic_temporal_calibration_run_proposal', 'version': 1,
            'status': 'prepared_awaiting_exact_owner_run_authorization', 'authorizes_historical_fit': False,
            'bindings': {p: output_hashes[p] if output_hashes and p in output_hashes else digest(root / p) for p in paths},
            'scope': 'one_fixed_development_only_temporal_offset_test_all_four_populations_no_final_use',
            'command': 'python3 -m generalship.napoleonic_temporal_calibration_run --authorization '
                       + BASE + 'owner-run-authorization.json --out ' + RESULT,
            'required_authorization': {'kind': 'napoleonic_temporal_calibration_owner_run_authorization',
                                       'approved': True, 'proposal_sha256': 'SHA-256 of this exact proposal',
                                       'command': 'exact command above', 'scope': 'exact scope above',
                                       'owner_request': 'verbatim later owner approval; no record created here'}}


def validate_proposal(root):
    actual = read_json(root / PROPOSAL)
    require(actual == proposal(root), 'changed proposal inputs/code; a new exact proposal and authorization are required')
    return actual


def write_artifacts(root):
    pinned = read_json(root / PROPOSAL) if (root / PROPOSAL).exists() else None
    outputs = [ARTIFACT + '.json', ARTIFACT + '.md']
    if pinned:
        require(pinned == proposal(root, {p: pinned['bindings'][p] for p in outputs}), 'changed frozen preparation inputs/code')
    plan = build(root)
    payloads = {outputs[0]: json.dumps(plan, indent=2, ensure_ascii=False, allow_nan=False) + '\n', outputs[1]: report(plan)}
    if pinned:
        require(all(hashlib.sha256(text.encode('utf-8')).hexdigest() == pinned['bindings'][path]
                    for path, text in payloads.items()), 'regenerated plan differs from frozen proposal')
    for path, text in payloads.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_text(text, encoding='utf-8')
    return plan


def check(root):
    plan = build(root)
    require(read_json(root / (ARTIFACT + '.json')) == plan, 'stale plan JSON')
    require((root / (ARTIFACT + '.md')).read_text(encoding='utf-8') == report(plan), 'stale plan report')
    validate_proposal(root)
    return {'status': plan['status'], 'development_entries': 273, 'planned_parameter_fits': plan['planned_parameter_fits'],
            'historical_fits_performed': 0, 'historical_outcome_labels_loaded': False, 'reserved_final_entries_used': 0}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--write', action='store_true')
    p.add_argument('--freeze-proposal', action='store_true')
    args = p.parse_args()
    if args.write:
        write_artifacts(args.root)
    if args.freeze_proposal:
        require(not (args.root / PROPOSAL).exists(), 'v1 proposal cannot be overwritten')
        write_json(args.root / PROPOSAL, proposal(args.root))
    print(json.dumps(check(args.root), indent=2))


if __name__ == '__main__':
    main()
