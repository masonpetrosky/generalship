"""Outcome-unused schedule audit, fixed evaluation partitions and synthetic-job receipts."""

from collections import Counter, defaultdict
import math
from pathlib import Path
import platform
import re
import unicodedata

from .evidence import citation_text
from .napoleonic import COHORT, FRAME
from .research_checks import BASE, POPULATION, CONVENTIONS, bound_dossier, write_artifacts, write_json
from .sources import digest, read_json

PROTOCOL = BASE + '/protocol.json'
EVALUATION = BASE + '/evaluation.json'
PILOT = BASE + '/campaign-pilot.json'
RESULT = 'artifacts/napoleonic-methods-v1.json'
REPORT = 'artifacts/napoleonic-methods-v1.md'
CODE = ('generalship/napoleonic_methods.py', 'generalship/recovery.py', 'generalship/research_checks.py',
        'generalship/baseline.py', 'generalship/sources.py', 'generalship/evidence.py',
        'generalship/napoleonic.py', 'generalship/__init__.py')


def label(text):
    if not text:
        return None, 'missing_printed_label'
    if re.search(r'\bund\b|\bseit\b|[()\d]', text, re.I):
        return None, 'joint_or_complex_printed_label'
    key = ''.join(ch if ch.isalnum() else ' ' for ch in unicodedata.normalize('NFC', text).casefold())
    key = ' '.join(key.split())
    return (key, None) if key else (None, 'empty_printed_label')


def schedule(entries, cohort_ids):
    """Whitelist fields explicitly; no outcome, strength or loss enters the returned schedule."""
    by_id = {r['id']: r for r in entries}
    rows = []
    for battle in cohort_ids:
        e = by_id[battle]
        french = e['french_side']
        if french not in ('winner', 'loser'):
            raise ValueError(f'{battle}: unresolved side orientation')
        other = 'loser' if french == 'winner' else 'winner'
        a, ai = label(e[french + '_commander_text'])
        b, bi = label(e[other + '_commander_text'])
        rows.append({'battle_id': battle, 'campaign': e['campaign_group'], 'war': e['war'],
                     'year': e['start_year'], 'a': a, 'b': b,
                     'a_issue': ai, 'b_issue': bi,
                     'a_printed': e[french + '_commander_text'], 'b_printed': e[other + '_commander_text']})
    return rows


def connected(rows):
    adjacent = defaultdict(set)
    for row in rows:
        for c in (row['a'], row['b']):
            if c:
                adjacent[c]
        if row['a'] and row['b']:
            adjacent[row['a']].add(row['b'])
            adjacent[row['b']].add(row['a'])
    seen, groups = set(), []
    for c in sorted(adjacent):
        if c in seen:
            continue
        queue, members = [c], []
        while queue:
            current = queue.pop()
            if current in seen:
                continue
            seen.add(current)
            members.append(current)
            queue.extend(sorted(adjacent[current] - seen))
        groups.append(sorted(members))
    return sorted(groups, key=lambda g: (-len(g), g))


def audit_schedule(rows):
    groups = Counter(r['campaign'] for r in rows)
    occurrences, campaigns = Counter(), defaultdict(set)
    for r in rows:
        for s in ('a', 'b'):
            if r[s]:
                occurrences[r[s]] += 1
                campaigns[r[s]].add(r['campaign'])
    usable = [r for r in rows if r['a'] and r['b'] and r['a'] != r['b']]
    components = connected(rows)
    exclusions = [{'battle_id': r['battle_id'], 'a_issue': r['a_issue'], 'b_issue': r['b_issue'],
                   'same_label_on_both_sides': bool(r['a'] and r['a'] == r['b'])}
                  for r in rows if r not in usable]
    return {'cohort_entries': len(rows), 'cohort_sides': 2 * len(rows), 'campaign_groups': dict(sorted(groups.items())),
            'literal_labels': len(occurrences), 'labels_at_least_two_appearances': sum(n >= 2 for n in occurrences.values()),
            'labels_in_multiple_groups': sum(len(c) > 1 for c in campaigns.values()),
            'component_sizes': [len(c) for c in components], 'components': components,
            'heldout_rows_with_any_recurrent_label': sum(any(r[s] and len(campaigns[r[s]]) > 1 for s in ('a', 'b')) for r in rows),
            'heldout_rows_with_both_recurrent_labels': sum(all(r[s] and len(campaigns[r[s]]) > 1 for s in ('a', 'b')) for r in rows),
            'synthetic_schedule_rows': len(usable),
            'synthetic_schedule_labels': len({r[s] for r in usable for s in ('a', 'b')}),
            'excluded_from_synthetic_schedule': exclusions,
            'resolved_historical_army_sides': 0,
            'commander_army_identification': 'not_assessed_no_verified_cross_engagement_army_registry',
            'interpretation': 'Conservative printed-label recurrence; no title or alias merging, no attribution '
                              'to joint commands, no resolved identity or causal claim. Missing labels remain in cohort counts.'}


def evaluation(entries, cohort_ids, frame_sha, cohort_sha):
    by_id = {r['id']: r for r in entries}
    development = [i for i in cohort_ids if by_id[i]['start_year'] <= 1813]
    final = [i for i in cohort_ids if by_id[i]['start_year'] >= 1814]
    group_ids = {g: [i for i in cohort_ids if by_id[i]['campaign_group'] == g]
                 for g in sorted({by_id[i]['campaign_group'] for i in cohort_ids})}
    wars = {w: [i for i in development if by_id[i]['war'] == w]
            for w in sorted({by_id[i]['war'] for i in development})}
    return {'kind': 'napoleonic_evaluation_partition', 'version': 1,
            'frame_sha256': frame_sha, 'cohort_sha256': cohort_sha,
            'development': development, 'reserved_final': final, 'frozen_groups': group_ids,
            'development_wars': wars,
            'forward_development': {'train': [i for i in development if by_id[i]['start_year'] <= 1812],
                                    'test': [i for i in development if by_id[i]['start_year'] == 1813]},
            'comparators': ['force_only', 'context_without_commanders', 'training_smoothed_prior', 'equal_odds'],
            'development_rule': 'All comparator log-loss differences must have campaign-bootstrap one-sided 95% '
                                'upper bounds below zero under both weightings. Every comparison is published.',
            'final_rule': 'Evaluate the single locked candidate once, report all comparator differences and each '
                          'group, do not treat a three-group bootstrap as a decisive significance test.',
            'final_status': 'reserved_from_numerical_model_selection_not_historically_blind',
            'authorizes_historical_outcome_fit': False}


def inputs(root):
    root = Path(root)
    protocol = read_json(root / PROTOCOL)
    if (protocol.get('kind') != 'napoleonic_methods_protocol' or protocol.get('version') != 1
            or protocol.get('seed') != 20261018 or protocol.get('repetitions') != 100
            or protocol.get('validation_repetitions') != 20
            or protocol.get('scenarios') != ['null', 'commander', 'stable_army_alias', 'switching_armies', 'source_bias']
            or protocol.get('historical_outcomes_fitted') is not False
            or protocol.get('admits_feature') is not False or protocol.get('changes_baseline') is not False):
        raise ValueError('Methods protocol differs from the version-1 design')
    if protocol['design']['sha256'] != digest(root / protocol['design']['path']):
        raise ValueError('Methods design differs from its frozen protocol')
    for path, expected in protocol['inputs'].items():
        if digest(root / path) != expected:
            raise ValueError(f'Methods input differs from its frozen binding: {path}')
    frame, cohort = read_json(root / FRAME), read_json(root / COHORT)
    expected = evaluation(frame['entries'], cohort['battle_ids'], digest(root / FRAME), digest(root / COHORT))
    if read_json(root / EVALUATION) != expected:
        raise ValueError('Evaluation partitions differ from the fixed frame-only rule')
    population = read_json(root / POPULATION)
    for binding in population['dossiers']:
        bound_dossier(root, binding['path'], binding['sha256'])
    # A pilot observation binds the original dossier, source bytes and exact cited passage.
    sources = {s['id']: s for s in read_json(root / 'data/sources.json')['sources']}
    pilot = read_json(root / PILOT)
    for obs in pilot['observations']:
        b = obs['dossier']
        dossier = bound_dossier(root, b['path'], b['sha256'])
        claim = next(c for c in dossier['claims'] if c['id'] == b['claim_id'])
        for citation in obs['citations']:
            source = sources[citation['source_id']]
            if source['sha256'] != citation['source_sha256'] or digest(root / source['path']) != citation['source_sha256']:
                raise ValueError('Pilot source binding changed')
            original = {k: citation[k] for k in ('source_id', 'section', 'locator', 'quote')}
            if original not in claim['citations'] or citation['quote'] not in citation_text(root, sources, citation):
                raise ValueError('Pilot passage does not replay')
    if pilot['estimable'] or pilot['contribution_estimate'] is not None:
        raise ValueError('This feasibility pilot does not estimate campaign contribution')
    return protocol, frame, cohort, pilot


def bindings(root, protocol):
    paths = sorted(set(CODE) | {PROTOCOL, EVALUATION, POPULATION, CONVENTIONS,
                               protocol['design']['path']} | set(protocol['inputs']))
    return {p: digest(Path(root) / p) for p in paths}


def run(root, progress=None):
    from .recovery import experiment
    root = Path(root)
    if (root / RESULT).is_file():
        check(root)  # refuse to overwrite an earlier version with changed code or inputs
    protocol, frame, cohort, pilot = inputs(root)
    rows = schedule(frame['entries'], cohort['battle_ids'])
    audit = audit_schedule(rows)
    usable = [{k: r[k] for k in ('battle_id', 'campaign', 'war', 'year', 'a', 'b')}
              for r in rows if r['a'] and r['b'] and r['a'] != r['b']]
    result = {'kind': 'napoleonic_methods_result', 'version': 1, 'verification': 'primary-verified',
              'bindings': bindings(root, protocol), 'protocol': protocol,
              'environment': {'python': platform.python_version(), 'implementation': platform.python_implementation()},
              'schedule_audit': audit, 'historical_outcomes_fitted': False,
              'pilot_estimable': pilot['estimable'], 'scenarios': experiment(usable, protocol, progress),
              'admits_feature': False, 'changes_baseline': False}
    write_json(root / RESULT, result)
    regenerate(root)
    return result


def check(root, preparations=False):
    """Verify stored inputs and schemas; this never fits or reruns the simulation."""
    root = Path(root)
    protocol, frame, cohort, pilot = inputs(root)
    result = read_json(root / RESULT)
    if result['bindings'] != bindings(root, protocol) or result['protocol'] != protocol:
        raise ValueError('Stored synthetic experiment is bound to different code or inputs; version it explicitly')
    if result['schedule_audit'] != audit_schedule(schedule(frame['entries'], cohort['battle_ids'])):
        raise ValueError('Stored schedule audit does not rebuild')
    if result['historical_outcomes_fitted'] or result['admits_feature'] or result['changes_baseline']:
        raise ValueError('Methods checkpoint cannot fit historical outcomes or admit features')
    if list(result['scenarios']) != protocol['scenarios']:
        raise ValueError('Scenario output is incomplete')
    for scenario, output in result['scenarios'].items():
        if output['repetitions'] != protocol['repetitions']:
            raise ValueError('Wrong synthetic repetition count')
        if set(output['validation']) != set(protocol['validation_strategies']):
            raise ValueError('Missing validation strategy')
        for v in output['validation'].values():
            if v['repetitions'] != protocol['validation_repetitions']:
                raise ValueError('Wrong validation repetition count')
    def finite(value):
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError('Nonfinite synthetic result')
        if isinstance(value, dict):
            for x in value.values():
                finite(x)
        if isinstance(value, list):
            for x in value:
                finite(x)
    finite(result)
    if preparations:
        from .research_checks import check_artifacts
        check_artifacts(root, protocol)
        if (root / REPORT).read_text(encoding='utf-8') != report_text(result, read_json(root / EVALUATION)):
            raise ValueError('Stored methods report does not regenerate')
    return result


def report_text(result, partitions):
    audit, protocol = result['schedule_audit'], result['protocol']
    lines = ['# Napoleonic methods checkpoint v1', '',
             '**Primary-verified. No historical outcomes fitted; no historical ranking or causal estimate.**', '',
             f"Schedule: {audit['cohort_entries']} cohort entries, {len(audit['campaign_groups'])} frozen war/year groups, "
             f"{audit['cohort_sides']} side slots. {audit['synthetic_schedule_rows']} entries enter the synthetic schedule; "
             f"{len(audit['excluded_from_synthetic_schedule'])} have missing, joint/complex or identical labels and remain in the cohort. "
             f"The usable schedule contains {audit['synthetic_schedule_labels']} literal labels.", '',
             f"Conservative printed keys: {audit['literal_labels']} labels; "
             f"{audit['labels_at_least_two_appearances']} recur; {audit['labels_in_multiple_groups']} occur in multiple groups. "
             f"There are {len(audit['component_sizes'])} opponent components; the largest contains "
             f"{audit['component_sizes'][0]} labels. The JSON retains every component.", '',
             f"Held-out availability: {audit['heldout_rows_with_any_recurrent_label']}/{audit['cohort_entries']} rows have "
             f"at least one label in another group; {audit['heldout_rows_with_both_recurrent_labels']} have both. "
             'These are printed labels, not resolved people or credited command appointments.', '',
             '**Commander versus army identification: not assessed.** There are 0 verified historical army labels '
             f"for {audit['cohort_sides']} side slots in this checkpoint. The source-backed pilot shows overlapping "
             'authority, but does not establish army continuity. Connectivity cannot fill this gap.', '',
             '**Campaign pilot: not estimable.** Local orders and authority distinctions replay from their sources. '
             'Campaign-onset boundaries, eligible replacements, inherited resources, information and the campaign '
             'outcome vector remain unknown. No battle results are added into campaign contribution.', '',
             '## Synthetic recovery', '',
             f"{protocol['repetitions']} recoveries and {protocol['validation_repetitions']} validation repetitions per "
             f"scenario; seed {protocol['seed']}. All army labels, force covariates and outcomes here are simulated. "
             'Fixed tau, reduced additive logistic model; this is not the complete run-4 selection procedure. '
             'Recovery gives each usable printed label equal weight after global centering; disconnected and '
             'side/intercept offsets remain prior-dependent. Ranges in the JSON describe repetitions, '
             'not historical confidence intervals.', '',
             '| Scenario | Centered theta RMSE | Estimated theta SD | Recovery correlation | Recovery slope |',
             '|---|---:|---:|---:|---:|']
    fmt = lambda x: 'undefined (true spread zero)' if x is None else f'{x:.4f}'
    for name, item in result['scenarios'].items():
        r = item['recovery']
        lines.append(f"| {name} | {fmt(r['rmse']['mean'])} | {fmt(r['estimated_sd']['mean'])} | "
                     f"{fmt(r['correlation']['mean'])} | {fmt(r['slope']['mean'])} |")
    lines += ['', 'The stable-army scenario has zero true commander effect and identical army/commander columns. '
              'Its estimated commander spread measures misattribution under this assumption, not discovered skill. '
              'The source-bias scenario tests whether commander labels absorb biased strength measurement.', '',
              '| Scenario | Test | Rows / groups | Commander minus force, battle | Equal-group | Commander minus prior, battle | Equal-group |',
              '|---|---|---:|---:|---:|---:|---:|']
    for name, item in result['scenarios'].items():
        for strategy, v in item['validation'].items():
            lines.append(f"| {name} | {strategy} | {v['rows']} / {v['groups']} | {v['force_battle']['mean']:+.4f} | "
                         f"{v['force_group']['mean']:+.4f} | {v['prior_battle']['mean']:+.4f} | {v['prior_group']['mean']:+.4f} |")
    lines += ['', 'Negative log-loss differences favor the commander model. A gain in the army or source-bias '
              'scenario would show why predictive gain alone does not identify a commander contribution. '
              'Forward-time scores cover a different test subset; do not rank strategies as though their rows were identical.', '',
              '## Observing the invented army assignments', '',
              '| Scenario | Commander RMSE without army terms | With observed synthetic army terms | Estimated theta SD with army terms |',
              '|---|---:|---:|---:|']
    for name, item in result['scenarios'].items():
        if 'with_observed_synthetic_armies' in item:
            r = item['with_observed_synthetic_armies']
            lines.append(f"| {name} | {item['recovery']['rmse']['mean']:.4f} | {r['rmse']['mean']:.4f} | {r['estimated_sd']['mean']:.4f} |")
    lines += ['', 'Permanent pairing is still structurally confounded when both columns are supplied; priors allocate '
              'the shared effect. Rotating assignments are only an invented sensitivity case, not evidence of historical crossovers.', '',
              '## Fixed evaluation and research handoff', '',
              f"Development: {len(partitions['development'])} entries through 1813. Reserved final: "
              f"{len(partitions['reserved_final'])} entries of 1814–1815 in three intact groups. "
              'The reservation concerns future numerical model selection; historical events have already been seen. '
              'No historical outcome fit is authorized by this checkpoint.', '',
              'The versioned design fixes group and temporal sensitivities and requires comparison with force only, '
              'context only, the training prior and equal odds. Three final groups provide limited replication.', '',
              'The calibration sample is prepared and unscored; no independent review was performed. '
              'The research screen flags digit/locator/family issues for primary inspection, and cannot verify entailment.', '',
              'Reproduce the experiment explicitly with `make napoleonic-methods`. `make reproduce` rebuilds this '
              'report and preparation artifacts from the stored result without a model job. The JSON carries exact '
              'bindings, scenario distributions, exclusions and environment. See `docs/napoleonic-methods-v1.md`.']
    return '\n'.join(lines) + '\n'


def regenerate(root):
    root = Path(root)
    result = check(root)
    outputs = write_artifacts(root, result['protocol'])
    (root / REPORT).write_text(report_text(result, read_json(root / EVALUATION)), encoding='utf-8')
    return [RESULT, REPORT, *outputs]
