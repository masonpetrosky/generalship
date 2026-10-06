"""Local research workflow; all commands except fetch run offline."""

import argparse
import json
import os
from pathlib import Path
import platform
import sys

from .baseline import evaluate
from .admission import DEFAULT_PROPOSAL, check as check_admission
from .strength_admission import DEFAULT_PROPOSAL as STRENGTH_PROPOSAL, check as check_strength
from .estimates import DEFAULT_LEDGER, check as check_estimates
from .estimates_v2 import DEFAULT_LEDGER as ESTIMATE_LEDGER_V2, check as check_estimates_v2
from .estimates_v3 import DEFAULT_LEDGER as ESTIMATE_LEDGER_V3, agreement as compilation_agreement, check as check_estimates_v3
from .estimate_eval import RUNS as EVAL_RUNS, evaluate_estimates, report_text as estimate_report
from .command import DEFAULT_LEDGER as COMMAND_LEDGER, check as check_command
COMMAND_LEDGER_V2 = 'data/command/responsibility-v2.json'
from .ratings import RUNS as RATING_RUNS, rate, report_text as ratings_report
from .ratings_v3 import rate3, report_text as ratings3_report
from .ratings_v4 import OUTPUT as RATINGS4_OUTPUT, rate4, report_text as ratings4_report
from .uncertainty import analyse as rating_uncertainty, report_text as uncertainty_report
from .imputation import COMMAND as IMPUTATION_COMMAND, STRENGTH as IMPUTATION_STRENGTH, build as build_imputation
from .imputation_v2 import OUTPUT as IMPUTATION_V2_OUTPUT, build as build_imputation_v2
from .frame import CIVIL_WAR
from .napoleonic import COHORT as NAPOLEONIC_COHORT, FRAME as NAPOLEONIC_FRAME, build as build_napoleonic, \
    check as check_napoleonic, cohort as napoleonic_cohort
from .dataset import build_dataset
from .evidence import validate_all, validate_napoleonic
from .napoleonic_packet import write_packet as write_napoleonic_packet
from .audit import AUDIT, AuditError, check_audit, report_text as audit_report, review_index
from .replay import bound_view, repository_text
from .site import build_site
from .sources import digest, fetch_sources, read_json, verify_sources, write_json


def report_text(root, profile, evaluation, dossiers, admission):
    total, eligible = profile["pilot_battles"], profile["baseline_eligible"]
    lines = ["# Pilot baseline and evidence coverage", "",
             "**Exploratory pipeline result. No validated general rankings or causal effects.**", "",
             f"The frozen frame contains {total} engagements in {profile['pilot_campaigns']} campaign groups.",
             f"Only {eligible}/{total} ({eligible/total:.1%}) meet the numerical-strength, decisive-outcome, and grain rules.",
             "All imported historical rows remain unreviewed. A checksum confirms the input bytes, not historical truth.", "",
             "## Coverage", "", "Exclusion reasons overlap; counts must not be added.", "",
             "| Reason | Engagements | Share of frame |", "|---|---:|---:|"]
    for reason, count in profile["exclusion_counts_nonexclusive"].items():
        lines.append(f"| {reason} | {count} | {count/total:.1%} |")
    lines += ["", "| Theater | Frame | Eligible |", "|---|---:|---:|"]
    for theater, counts in profile["coverage_by_theater"].items():
        lines.append(f"| {theater} | {counts['total']} | {counts['eligible']} |")
    lines += ["", "## Campaign-held-out baseline", "",
              f"Each of the {evaluation['n_campaigns']} eligible campaign groups is held out in full while fitting on the other groups.",
              "Every battle appears once in evaluation. Union win is the positive class; inconclusive cases are excluded, not encoded as half-wins.",
              "Lower Brier score and log loss are better. All baselines use the same eligible rows.", "",
              "| Model | Battle-weighted Brier | Battle-weighted log loss | Campaign-weighted Brier |",
              "|---|---:|---:|---:|"]
    for name, metrics in evaluation["battle_weighted_metrics"].items():
        macro = evaluation["campaign_weighted_metrics"][name]["brier"]
        lines.append(f"| {name} | {metrics['brier']:.6f} | {metrics['log_loss']:.6f} | {macro:.6f} |")
    lines += ["", "These are diagnostics on a small, selected subset. They do not establish better generalship measurement.",
              "The source's campaign boundaries may leave dependence between related operations; commanders also recur across folds.",
              "Strength sensitivity varies the held-out range endpoints with a fixed fitted model. It excludes training-data and model uncertainty.",
              "", "## Draft evidence dossiers", "",
              "Exact passage checks verify provenance only. These drafts do not modify model inputs; the historical disputes they record remain open.", "",
              "| Battle | Claims | Explicit unknowns | Quantities | Events | Status |", "|---|---:|---:|---:|---:|---|"]
    for d in dossiers:
        lines.append(f"| [{d['battle_id']}](../data/evidence/{d['battle_id']}.json) | {d['claims']} | {d['unknown_claims']} | {d['quantities']} | {d['events']} | {d['status']} |")
    coverage = admission['coverage']
    counts = coverage['status_counts']
    lines += ["", "## Admission proposal checks", "",
              f"The offline validator retains all {coverage['frame_engagements']} engagements / {coverage['frame_campaigns']} campaign groups in its [coverage ledger](admission-check.json).",
              f"It checks {coverage['candidate_observations']} Shiloh troop observations: {counts.get('blocked', 0)} blocked, {counts.get('excluded', 0)} excluded, {counts.get('eligible_candidate', 0)} eligible candidates, and {counts.get('invalid', 0)} invalid.",
              f"There are {coverage['complete_candidate_engagements']} complete candidate rows and {admission['promoted_rows']} promoted rows. Missing mappings remain unknown; no canonical opening force is inferred.",
              "The ledger separates dossier availability, candidate status, side coverage and baseline eligibility. These counts are mechanical checks, not historical adjudication or forecast improvement."]
    lines += ["", "## Coverage and current priority", "",
              f"The frozen v1 cohort has dossiers for {sum(d['battle_id'] in set(read_json(root / 'data/pilot/cohort.json')['battle_ids']) for d in dossiers)} of its {total} engagements. "
              f"The full-war research frame ([cohort v2](../docs/cohort-v2.md)) has {len(read_json(root / 'data/pilot/cohort-v2.json')['battle_ids'])} engagements; "
              f"{len(dossiers)} have dossiers. Dossier presence, verification, baseline eligibility and feature admission are different measures.",
              "The current priority, open owner decisions and milestone status are in the [roadmap](../docs/roadmap.md); completed passes, reviews and source investigations are in the [research log](../docs/research-log.md). Commander ratings and estimate evaluations are separate owner-authorized diagnostics with their own reports in `artifacts/`; none of them changes this baseline.",
              "", "## Reproduce and inspect", "", "Run `make check` and `make reproduce` from the repository root.",
              "[Evaluation and fold membership](baseline.json), [coverage](quality.json), [run receipt](receipt.json),",
              "[research queue](research-queue.json), [source manifest](../data/sources.json), [methodology](../docs/methodology.md).", "",
              "Data: Jeffrey B. Arnold, American Civil War Battle Data (CWSAC tables), derived from U.S. National Park Service summaries; CC-BY-4.0 attribution.",
              "[Pinned upstream data](https://github.com/jrnold/acw_battle_data/tree/3a6020dbfcbcfc650a268b10a9f155588472432b/build/acw_battle_data).", ""]
    return "\n".join(lines)


def replay_frozen_ledgers(root, checks):
    """Replay each present ledger with its checker through bound views (docs/ledger-replay.md):
    one view for all of them, or one each if their bound versions conflict. A failure is reported
    as stale_or_invalid, not raised; an absent ledger gives None."""
    def replay(replay_root, path, check):
        try:
            return check(replay_root, path)
        except (ValueError, KeyError, OSError) as exc:
            return {'status': 'stale_or_invalid', 'error': repository_text(str(exc), replay_root, root)}

    present = [path for path, _ in checks if (root / path).is_file()]
    try:
        with bound_view(root, *present) as replay_root:
            return [replay(replay_root, path, check) if path in present else None for path, check in checks]
    except (ValueError, OSError):
        pass  # conflicting bound versions, or no shared view: replay each ledger on its own
    results = []
    for path, check in checks:
        if path not in present:
            results.append(None)
            continue
        try:
            with bound_view(root, path) as replay_root:
                results.append(replay(replay_root, path, check))
        except (ValueError, OSError) as exc:
            results.append({'status': 'stale_or_invalid', 'error': str(exc)})
    return results


def run_build(root, write=False):
    records, profile = build_dataset(root)
    dossiers = validate_all(root)
    napoleonic_dossiers = validate_napoleonic(root)  # raises on an invalid draft, like the Civil War dossiers
    evaluation = evaluate(records)
    admission = check_admission(root)
    if admission['status'] == 'invalid' or admission['scenario_issues']:
        raise ValueError('Default admission proposal has invalid bindings or scenarios')
    # A ledger bound to evidence that cannot be reached is reported, not fatal: `estimate-check`,
    # `command-check` and their unit tests enforce replay of the committed ledgers.
    reviews = review_index(root)  # historical review records, in the controlled disposition vocabulary
    try:  # like a frozen ledger, an audit whose audited bytes cannot be reached is reported, not fatal
        audit = check_audit(root) if (root / AUDIT).is_file() else None
    except AuditError as exc:
        audit = {'status': 'stale_or_invalid', 'error': str(exc)}
    audit_ok = audit is not None and 'status' not in audit
    try:  # like a frozen ledger, a frame whose bound files cannot be reached is reported, not fatal;
        # tests/test_napoleonic.py enforces the rebuild of the committed frame
        napoleonic = check_napoleonic(root) if (root / NAPOLEONIC_FRAME).is_file() else None
    except (ValueError, OSError) as exc:
        napoleonic = {'status': 'stale_or_invalid', 'error': str(exc)}
    estimates, command, estimates_v2, command_v2, estimates_v3 = replay_frozen_ledgers(root, [
        (DEFAULT_LEDGER, check_estimates), (COMMAND_LEDGER, check_command),
        (ESTIMATE_LEDGER_V2, check_estimates_v2), (COMMAND_LEDGER_V2, check_command),
        (ESTIMATE_LEDGER_V3, check_estimates_v3)])
    if write:
        output = root / "artifacts"
        output.mkdir(exist_ok=True)
        write_json(output / "battles.json", records)
        write_json(output / "quality.json", profile)
        write_json(output / "baseline.json", evaluation)
        write_json(output / "evidence-checks.json", dossiers)
        if napoleonic_dossiers:
            write_json(output / "napoleonic-evidence-checks.json", napoleonic_dossiers)
        write_json(output / "admission-check.json", admission)
        known = {d["battle_id"]: d["status"] for d in dossiers}
        write_json(output / "research-queue.json", [
            {"battle_id": r["battle_id"], "name": r["name"], "campaign": r["campaign"],
             "needs": r["exclusion_reasons"] or ["independent_source_and_responsibility_review"],
             "dossier_status": known.get(r["battle_id"], "not_started")}
            for r in records
        ])
        (output / "pilot-report.md").write_text(report_text(root, profile, evaluation, dossiers, admission), encoding="utf-8")
        write_json(output / "review-index.json", reviews)
        if estimates_v3 is not None and 'side_grades' in estimates_v3:
            write_json(output / "strength-ledger-v3-check.json", estimates_v3)
            write_json(output / "strength-compilation-agreement.json", compilation_agreement(root))
        if audit_ok:
            write_json(output / "extraction-audit-v1.json", audit)
            (output / "extraction-audit-v1.md").write_text(audit_report(read_json(root / AUDIT), audit), encoding="utf-8")
        inputs = sorted((root / "generalship").glob("*.py")) + [root / "data/sources.json", root / "data/pilot/cohort.json",
                                                               root / "data/pilot/cohort-v2.json"]
        inputs += sorted((root / "data/evidence").rglob("*.json"))
        inputs += sorted(p for p in (root / "data/admission").rglob('*') if p.is_file())
        inputs += sorted(p for p in (root / "data/estimates").rglob('*') if p.is_file())
        inputs += sorted(p for p in (root / "data/command").rglob('*') if p.is_file())
        inputs += sorted(p for p in (root / "data/audit").rglob('*') if p.is_file())
        inputs += sorted(p for p in (root / "data/napoleonic").rglob('*') if p.is_file())
        outputs = ["battles.json", "quality.json", "baseline.json", "evidence-checks.json", "research-queue.json", "pilot-report.md", "admission-check.json",
                   "review-index.json"] + (["extraction-audit-v1.json", "extraction-audit-v1.md"] if audit_ok else [])
        outputs += ["strength-ledger-v3-check.json", "strength-compilation-agreement.json"] if (output / "strength-ledger-v3-check.json").is_file() else []
        outputs += ["napoleonic-evidence-checks.json"] if napoleonic_dossiers else []
        write_json(output / "receipt.json", {
            "command": "python3 -m generalship build", "model_id": evaluation["model_id"],
            # Floating-point results can differ in the last bits across Python versions (for example,
            # sum() became compensated in 3.12 and NormalDist.cdf changed in 3.14).
            "environment": {"python": platform.python_version(), "implementation": platform.python_implementation()},
            "input_sha256": {str(p.relative_to(root)): digest(p) for p in inputs},
            "source_sha256": profile["source_hashes"],
            "output_sha256": {name: digest(output / name) for name in outputs},
        })
    return {"pilot_battles": len(records), "eligible_battles": evaluation["n_battles"],
            "eligible_campaigns": evaluation["n_campaigns"], "draft_dossiers": sum(d["status"] == "draft" for d in dossiers),
            "metrics": evaluation["battle_weighted_metrics"],
            "admission_candidate_statuses": admission['coverage']['status_counts'],
            "admission_promoted_rows": admission['promoted_rows'],
            "review_records": {"reviews": len(reviews['reviews']), "findings_by_disposition": reviews['totals']},
            "extraction_audit": ({k: audit[k] for k in ('audited', 'verdicts', 'material_error_rate_95', 'any_issue_rate_95')}
                                 if audit_ok else audit),
            "estimate_ledger": estimates and ({k: estimates[k] for k in ('side_grades', 'rows_by_set_fit_eligible', 'fitted')}
                                              if 'side_grades' in estimates else estimates),
            "command_ledger": command and ({k: command[k] for k in ('side_grades', 'nesting', 'rated')}
                                           if 'side_grades' in command else command),
            "estimate_ledger_v2": estimates_v2 and ({k: estimates_v2[k] for k in ('in_scope', 'side_grades', 'rows_by_set_fit_eligible', 'fitted')}
                                                    if 'side_grades' in estimates_v2 else estimates_v2),
            "command_ledger_v2": command_v2 and ({k: command_v2[k] for k in ('engagements', 'side_grades', 'nesting', 'rated')}
                                                 if 'side_grades' in command_v2 else command_v2),
            "estimate_ledger_v3": estimates_v3 and ({k: estimates_v3[k] for k in ('side_grades', 'filled_from_d', 'rows_by_set_fit_eligible', 'fitted')}
                                                    if 'side_grades' in estimates_v3 else estimates_v3),
            "napoleonic_frame": napoleonic and ({k: napoleonic[k] for k in ('entries_transcribed', 'in_frame', 'campaign_groups')}
                                                  if 'in_frame' in napoleonic else napoleonic),
            "napoleonic_dossiers": {"drafts": len(napoleonic_dossiers), "claims": sum(d['claims'] for d in napoleonic_dossiers),
                                    "unknown_claims": sum(d['unknown_claims'] for d in napoleonic_dossiers)},
            "artifacts_written": write}


def research_packet(root, battle_id):
    records, _ = build_dataset(root)
    row = next((r for r in records if r["battle_id"] == battle_id), None)
    if row is None:
        raise ValueError(f"Battle not in cohort: {battle_id}")
    dossier_path = root / f"data/evidence/{battle_id}.json"
    parts = [(root / "prompts/research-dossier.md").read_text(), "\n## Assigned record\n",
             "```json\n" + json.dumps(row, indent=2) + "\n```"]
    if dossier_path.exists():
        parts += ["\n## Existing draft (not adjudicated)\n", "```json\n" + dossier_path.read_text() + "```"]
    parts += ["\n## Source registry\n", "```json\n" + (root / "data/sources.json").read_text() + "```"]
    path = root / "artifacts/research" / f"{battle_id}.md"
    path.parent.mkdir(exist_ok=True, parents=True)
    path.write_text("\n".join(parts), encoding="utf-8")
    return {"packet": str(path), "status": "prepared_only_no_model_called"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root (defaults to cwd)")
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("check", "build", "fetch"):
        sub.add_parser(command)
    sub.add_parser('napoleonic-frame', help='Rebuild and write the Napoleonic frame v1 and cohort v1 from the Bodart transcription')
    nap_packet = sub.add_parser('napoleonic-packet', help='Write the research packet for one cohort v1 campaign group')
    nap_packet.add_argument('group', help="Campaign group, for example 'third-coalition 1805'")
    sub.add_parser('napoleonic-evidence-check', help='Verify source hashes and validate the Napoleonic draft dossiers')
    site_parser = sub.add_parser('site', help='Write the static explorer (plain HTML) from committed files')
    site_parser.add_argument('--out', default='_site', help='Output directory (default _site, git-ignored)')
    site_parser.add_argument('--commit', default=os.environ.get('GITHUB_SHA', 'main'),
                             help='Commit that snapshot and document links point to on GitHub')
    for command in ("inspect", "packet"):
        p = sub.add_parser(command)
        p.add_argument("battle_id")
    admission_parser = sub.add_parser('admission-check', help='Offline proposal/release audit; never promotes inputs')
    admission_parser.add_argument('path', nargs='?', default=DEFAULT_PROPOSAL)
    admission_parser.add_argument('--details', action='store_true', help='Print the complete ledger and provenance')
    est_parser = sub.add_parser('estimate-check', help='Replay the best-estimate side-strength ledger; never fits or promotes')
    est_parser.add_argument('--ledger', default=DEFAULT_LEDGER, help='Ledger path; version-2 and version-3 ledgers are replayed by their own checkers')
    rat_parser = sub.add_parser('commander-ratings', help='Owner-authorized residual ratings (design §7); never changes the baseline')
    rat_parser.add_argument('--version', type=int, default=1, choices=(1, 2, 3, 4),
                            help='Run 1 (cohort v1 ledgers), 2 (cohort v2 ledgers), 3 (all battles with grade E strengths) '
                                 'or 4 (context comparator, estimated tau, leakage handling)')
    imp_parser = sub.add_parser('strength-imputation', help='Fit the grade E strength model and write its output')
    imp_parser.add_argument('--version', type=int, default=1, choices=(1, 2),
                            help='1: v2 ledger (run 3), artifacts/strength-imputation-v1.json; 2: v3 ledger with the '
                                 'pre-start view (run 4), artifacts/strength-imputation-v2.json')
    unc_parser = sub.add_parser('rating-uncertainty', help="Bootstrap a committed rating run's held-out verdict; refits nothing")
    unc_parser.add_argument('--version', type=int, default=3, choices=(2, 3), help='Rating run to analyse')
    cmd_parser = sub.add_parser('command-check', help='Replay the command-responsibility ledger checks; never rates anyone')
    cmd_parser.add_argument('--ledger', default=COMMAND_LEDGER, help='Ledger path (v1 or v2)')
    eval_parser = sub.add_parser('estimate-evaluate', help='Owner-authorized estimate-layer diagnostic (design §6); never changes the baseline')
    eval_parser.add_argument('--version', type=int, default=1, choices=(1, 2), help='Run 1 (v1 ledger) or 2 (v2 ledger)')
    strength_parser = sub.add_parser('strength-check', help='Offline tier-2 reported-strength proposal/release audit; never promotes inputs')
    strength_parser.add_argument('path', nargs='?', default=STRENGTH_PROPOSAL)
    strength_parser.add_argument('--details', action='store_true', help='Print the complete ledger and provenance')
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command in {"check", "build"}:
            result = run_build(root, write=args.command == "build")
        elif args.command in {'admission-check', 'strength-check'}:
            checked = (check_admission if args.command == 'admission-check' else check_strength)(root, args.path)
            result = checked if args.details else {
                'kind': checked['kind'], 'status': checked.get('release_status', checked['status']),
                'coverage': {k: v for k, v in checked['coverage'].items() if k != 'ledger'},
                'scenario_issues': checked['scenario_issues'], 'promoted_rows': checked['promoted_rows']}
            print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
            return int(checked['status'] == 'invalid' or bool(checked['scenario_issues'])
                       or checked.get('release_status') == 'blocked')
        elif args.command == 'estimate-check':
            version = read_json(root / args.ledger).get('version', 1)
            with bound_view(root, args.ledger) as replay_root:
                result = {1: check_estimates, 2: check_estimates_v2, 3: check_estimates_v3}[version](replay_root, args.ledger)
        elif args.command == 'commander-ratings':
            if args.version == 4:
                ratings, out = rate4(root), RATINGS4_OUTPUT
                text = ratings4_report(ratings)
            elif args.version == 3:
                ratings, out, text = rate3(root), 'artifacts/commander-ratings-v3', None
                text = ratings3_report(ratings)
            else:
                ratings = rate(root, args.version)
                out = RATING_RUNS[args.version]['output']
                text = ratings_report(ratings)
            write_json(root / f'{out}.json', ratings)
            (root / f'{out}.md').write_text(text, encoding='utf-8')
            improved = ratings['verdict']['improved'] if args.version == 4 else ratings['heldout_test']['improved']
            result = {'heldout_improved': improved, 'outputs': [f'{out}.json', f'{out}.md']}
        elif args.command == 'rating-uncertainty':
            analysis = rating_uncertainty(root, args.version)
            out = f'artifacts/commander-ratings-v{args.version}-uncertainty'
            write_json(root / f'{out}.json', analysis)
            (root / f'{out}.md').write_text(uncertainty_report(analysis), encoding='utf-8')
            result = {'point': analysis['point'], 'bootstrap_95': {w: [analysis['bootstrap'][w]['q0.025'], analysis['bootstrap'][w]['q0.975']]
                                                                for w in ('battle_weighted', 'campaign_weighted')},
                      'outputs': [f'{out}.json', f'{out}.md']}
        elif args.command == 'strength-imputation' and args.version == 2:
            with bound_view(root, CIVIL_WAR['strength_ledger'], CIVIL_WAR['command_ledger']) as replay_root:
                check_estimates_v3(replay_root, CIVIL_WAR['strength_ledger'])
                check_command(replay_root, CIVIL_WAR['command_ledger'])
            imputation = build_imputation_v2(root, CIVIL_WAR)
            write_json(root / IMPUTATION_V2_OUTPUT, imputation)
            result = {'grade_E_sides': len(imputation['sides']), 'by_reason': {
                          'grade_D': sum('post_start_modelled' not in s['labels'] for s in imputation['sides']),
                          'post_start': sum('post_start_modelled' in s['labels'] for s in imputation['sides'])},
                      'k': imputation['model']['k'], 'loo_coverage_80': imputation['model']['loo_coverage_80'],
                      'output': IMPUTATION_V2_OUTPUT}
        elif args.command == 'strength-imputation':
            with bound_view(root, IMPUTATION_STRENGTH, IMPUTATION_COMMAND) as replay_root:
                imputation = build_imputation(replay_root)  # frozen impute replays both ledgers
            write_json(root / 'artifacts/strength-imputation-v1.json', imputation)
            result = {'grade_E_sides': len(imputation['sides']), 'k': imputation['model']['k'],
                      'loo_coverage_80': imputation['model']['loo_coverage_80'],
                      'output': 'artifacts/strength-imputation-v1.json'}
        elif args.command == 'command-check':
            with bound_view(root, args.ledger) as replay_root:
                result = check_command(replay_root, args.ledger)
        elif args.command == 'estimate-evaluate':
            evaluation = evaluate_estimates(root, args.version)
            out = EVAL_RUNS[args.version]['output']
            write_json(root / f'{out}.json', evaluation)
            (root / f'{out}.md').write_text(estimate_report(evaluation), encoding='utf-8')
            result = {'ledger_sha256': evaluation['ledger']['sha256'],
                      'row_sets': {k: {'evaluable': v['evaluable'], 'rows': v['rows'],
                                       'brier': v['metrics']['battle_weighted'] if v['evaluable'] else None}
                                   for k, v in evaluation['row_sets'].items()},
                      'outputs': [f'{out}.json', f'{out}.md']}
        elif args.command == 'napoleonic-frame':
            frame = build_napoleonic(root)
            write_json(root / NAPOLEONIC_FRAME, frame)
            cohort = napoleonic_cohort(frame, digest(root / NAPOLEONIC_FRAME))
            write_json(root / NAPOLEONIC_COHORT, cohort)
            result = {'frame': frame['counts'], 'cohort': cohort['counts'], 'outputs': [NAPOLEONIC_FRAME, NAPOLEONIC_COHORT]}
        elif args.command == 'napoleonic-packet':
            result = write_napoleonic_packet(root, args.group)
        elif args.command == 'napoleonic-evidence-check':
            sources = verify_sources(root)  # every registered hash and section map, even before any draft exists
            checked = validate_napoleonic(root, sources)
            result = {'sources_verified': len(sources), 'drafts': len(checked), 'claims': sum(d['claims'] for d in checked),
                      'unknown_claims': sum(d['unknown_claims'] for d in checked), 'dossiers': checked}
        elif args.command == 'site':
            result = build_site(root, args.out, args.commit)
        elif args.command == "fetch":
            result = {"restored_sources": fetch_sources(root)}
        elif args.command == "packet":
            result = research_packet(root, args.battle_id)
        else:
            records, _ = build_dataset(root)
            result = next((r for r in records if r["battle_id"] == args.battle_id), None)
            if result is None:
                raise ValueError(f"Battle not in cohort: {args.battle_id}")
        print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
        return 0
    except (ValueError, KeyError, OSError, TypeError) as exc:
        print(f"generalship: {exc}", file=sys.stderr)
        return 1
