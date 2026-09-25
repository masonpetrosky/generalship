"""Local research workflow; all commands except fetch run offline."""

import argparse
import json
from pathlib import Path
import sys

from .baseline import evaluate
from .admission import DEFAULT_PROPOSAL, check as check_admission
from .strength_admission import DEFAULT_PROPOSAL as STRENGTH_PROPOSAL, check as check_strength
from .estimates import DEFAULT_LEDGER, check as check_estimates
from .estimates_v2 import DEFAULT_LEDGER as ESTIMATE_LEDGER_V2, check as check_estimates_v2
from .estimate_eval import RUNS as EVAL_RUNS, evaluate_estimates, report_text as estimate_report
from .command import DEFAULT_LEDGER as COMMAND_LEDGER, check as check_command
COMMAND_LEDGER_V2 = 'data/command/responsibility-v2.json'
from .ratings import RUNS as RATING_RUNS, rate, report_text as ratings_report
from .ratings_v3 import rate3, report_text as ratings3_report
from .imputation import build as build_imputation
from .dataset import build_dataset
from .evidence import validate_all
from .sources import digest, fetch_sources, read_json, write_json


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
              "Exact passage checks verify provenance only. These drafts do not modify model inputs. Shiloh's four source-review corrections and the focused validator follow-up are accepted; historical disputes remain open.", "",
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
    lines += ["", "## Next research action", "",
              f"The frozen v1 cohort is complete: {sum(d['battle_id'] in set(read_json(root / 'data/pilot/cohort.json')['battle_ids']) for d in dossiers)}/{total} engagements have dossiers. "
              f"The full-war research frame ([cohort v2](../docs/cohort-v2.md)) has {len(read_json(root / 'data/pilot/cohort-v2.json')['battle_ids'])} engagements; "
              f"{len(dossiers)} have dossiers. Dossier presence, separate review, baseline eligibility and feature admission are different measures.",
              "The [Operations about Dandridge first pass](../docs/research/dandridge-first-pass-v1.md) adds all three frozen records: 27 claims, 3 explicit unknowns and 145 citations from NPS/CWSAC, Sturgis's, Martin's and Longstreet's Official Records reports. Strength attributions, the Mossy Creek withdrawal, Sturgis's differing loss and capture figures and the frozen/live casualty differences remain visible; its separate Opus review's seven corrections are applied. All frozen campaign groups now have first-pass dossiers. Earlier passes and reviews remain in the [current roadmap](../docs/roadmap.md).",
              "Use the [bounded first-pass protocol](../docs/methodology.md#research-depth-and-coverage): up to three source families per battle and one targeted follow-up for the most consequential gap. Keep unsupported dimensions unknown, move to the next engagement, and review by campaign. Deeper work requires a concrete decision and stopping point or an explicit owner request.",
              "Shiloh's Agate and overnight-provenance investigations are parked. The [completed research and review history](../docs/roadmap.md#milestone-1--first-independently-reviewed-campaign-dossiers-in-progress) retains all findings and unresolved questions; neither further article collation nor original-newspaper recovery is the next task. No historical feature is admitted by this change in research priority.",
              "", "## Reproduce and inspect", "", "Run `make check` and `make reproduce` from the repository root.",
              "[Evaluation and fold membership](baseline.json), [coverage](quality.json), [run receipt](receipt.json),",
              "[research queue](research-queue.json), [source manifest](../data/sources.json), [methodology](../docs/methodology.md).", "",
              "Data: Jeffrey B. Arnold, American Civil War Battle Data (CWSAC tables), derived from U.S. National Park Service summaries; CC-BY-4.0 attribution.",
              "[Pinned upstream data](https://github.com/jrnold/acw_battle_data/tree/3a6020dbfcbcfc650a268b10a9f155588472432b/build/acw_battle_data).", ""]
    return "\n".join(lines)


def run_build(root, write=False):
    records, profile = build_dataset(root)
    dossiers = validate_all(root)
    evaluation = evaluate(records)
    admission = check_admission(root)
    if admission['status'] == 'invalid' or admission['scenario_issues']:
        raise ValueError('Default admission proposal has invalid bindings or scenarios')
    estimates = None
    if (root / DEFAULT_LEDGER).is_file():
        # A ledger bound to earlier evidence is reported, not fatal: `estimate-check`
        # and its unit test enforce replay of the committed ledger.
        try:
            estimates = check_estimates(root)
        except (ValueError, KeyError, OSError) as exc:
            estimates = {'status': 'stale_or_invalid', 'error': str(exc)}
    command = None
    if (root / COMMAND_LEDGER).is_file():
        try:
            command = check_command(root)
        except (ValueError, KeyError, OSError) as exc:
            command = {'status': 'stale_or_invalid', 'error': str(exc)}
    estimates_v2 = command_v2 = None
    if (root / ESTIMATE_LEDGER_V2).is_file():
        try:
            estimates_v2 = check_estimates_v2(root)
        except (ValueError, KeyError, OSError) as exc:
            estimates_v2 = {'status': 'stale_or_invalid', 'error': str(exc)}
    if (root / COMMAND_LEDGER_V2).is_file():
        try:
            command_v2 = check_command(root, COMMAND_LEDGER_V2)
        except (ValueError, KeyError, OSError) as exc:
            command_v2 = {'status': 'stale_or_invalid', 'error': str(exc)}
    if write:
        output = root / "artifacts"
        output.mkdir(exist_ok=True)
        write_json(output / "battles.json", records)
        write_json(output / "quality.json", profile)
        write_json(output / "baseline.json", evaluation)
        write_json(output / "evidence-checks.json", dossiers)
        write_json(output / "admission-check.json", admission)
        known = {d["battle_id"]: d["status"] for d in dossiers}
        write_json(output / "research-queue.json", [
            {"battle_id": r["battle_id"], "name": r["name"], "campaign": r["campaign"],
             "needs": r["exclusion_reasons"] or ["independent_source_and_responsibility_review"],
             "dossier_status": known.get(r["battle_id"], "not_started")}
            for r in records
        ])
        (output / "pilot-report.md").write_text(report_text(root, profile, evaluation, dossiers, admission), encoding="utf-8")
        inputs = sorted((root / "generalship").glob("*.py")) + [root / "data/sources.json", root / "data/pilot/cohort.json",
                                                               root / "data/pilot/cohort-v2.json"]
        inputs += sorted((root / "data/evidence").rglob("*.json"))
        inputs += sorted(p for p in (root / "data/admission").rglob('*') if p.is_file())
        inputs += sorted(p for p in (root / "data/estimates").rglob('*') if p.is_file())
        inputs += sorted(p for p in (root / "data/command").rglob('*') if p.is_file())
        outputs = ["battles.json", "quality.json", "baseline.json", "evidence-checks.json", "research-queue.json", "pilot-report.md", "admission-check.json"]
        write_json(output / "receipt.json", {
            "command": "python3 -m generalship build", "model_id": evaluation["model_id"],
            "input_sha256": {str(p.relative_to(root)): digest(p) for p in inputs},
            "source_sha256": profile["source_hashes"],
            "output_sha256": {name: digest(output / name) for name in outputs},
        })
    return {"pilot_battles": len(records), "eligible_battles": evaluation["n_battles"],
            "eligible_campaigns": evaluation["n_campaigns"], "draft_dossiers": sum(d["status"] == "draft" for d in dossiers),
            "metrics": evaluation["battle_weighted_metrics"],
            "admission_candidate_statuses": admission['coverage']['status_counts'],
            "admission_promoted_rows": admission['promoted_rows'],
            "estimate_ledger": estimates and ({k: estimates[k] for k in ('side_grades', 'rows_by_set_fit_eligible', 'fitted')}
                                              if 'side_grades' in estimates else estimates),
            "command_ledger": command and ({k: command[k] for k in ('side_grades', 'nesting', 'rated')}
                                           if 'side_grades' in command else command),
            "estimate_ledger_v2": estimates_v2 and ({k: estimates_v2[k] for k in ('in_scope', 'side_grades', 'rows_by_set_fit_eligible', 'fitted')}
                                                    if 'side_grades' in estimates_v2 else estimates_v2),
            "command_ledger_v2": command_v2 and ({k: command_v2[k] for k in ('engagements', 'side_grades', 'nesting', 'rated')}
                                                 if 'side_grades' in command_v2 else command_v2),
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
    for command in ("inspect", "packet"):
        p = sub.add_parser(command)
        p.add_argument("battle_id")
    admission_parser = sub.add_parser('admission-check', help='Offline proposal/release audit; never promotes inputs')
    admission_parser.add_argument('path', nargs='?', default=DEFAULT_PROPOSAL)
    admission_parser.add_argument('--details', action='store_true', help='Print the complete ledger and provenance')
    est_parser = sub.add_parser('estimate-check', help='Replay the best-estimate side-strength ledger; never fits or promotes')
    est_parser.add_argument('--ledger', default=DEFAULT_LEDGER, help='Ledger path; a version-2 ledger is replayed by estimates_v2')
    rat_parser = sub.add_parser('commander-ratings', help='Owner-authorized residual ratings (design §7); never changes the baseline')
    rat_parser.add_argument('--version', type=int, default=1, choices=(1, 2, 3),
                            help='Run 1 (cohort v1 ledgers), 2 (cohort v2 ledgers) or 3 (all battles with grade E strengths)')
    sub.add_parser('strength-imputation', help='Fit the grade E strength model and write artifacts/strength-imputation-v1.json')
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
            result = (check_estimates_v2 if version == 2 else check_estimates)(root, args.ledger)
        elif args.command == 'commander-ratings':
            if args.version == 3:
                ratings, out, text = rate3(root), 'artifacts/commander-ratings-v3', None
                text = ratings3_report(ratings)
            else:
                ratings = rate(root, args.version)
                out = RATING_RUNS[args.version]['output']
                text = ratings_report(ratings)
            write_json(root / f'{out}.json', ratings)
            (root / f'{out}.md').write_text(text, encoding='utf-8')
            result = {'heldout_improved': ratings['heldout_test']['improved'], 'outputs': [f'{out}.json', f'{out}.md']}
        elif args.command == 'strength-imputation':
            imputation = build_imputation(root)
            write_json(root / 'artifacts/strength-imputation-v1.json', imputation)
            result = {'grade_E_sides': len(imputation['sides']), 'k': imputation['model']['k'],
                      'loo_coverage_80': imputation['model']['loo_coverage_80'],
                      'output': 'artifacts/strength-imputation-v1.json'}
        elif args.command == 'command-check':
            result = check_command(root, args.ledger)
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
