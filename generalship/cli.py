"""Local research workflow; all commands except fetch run offline."""

import argparse
import json
from pathlib import Path
import sys

from .baseline import evaluate
from .admission import DEFAULT_PROPOSAL, check as check_admission
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
              "The [Shiloh research memo](../docs/research/shiloh.md) preserves competing returns, dated orders, reinforcement phases, and disputed responsibility. No canonical opening strength or effective command-transfer time has been adjudicated.",
              "The [Confederate return audit](../docs/research/shiloh-confederate-returns.md) and [Union availability audit](../docs/research/shiloh-union-availability.md) retain source and population disputes. The [Ohio reinforcement audit](../docs/research/shiloh-ohio-reinforcements.md) separates crossing, landing, formation and participation while preserving conflicting clocks, the untraced 600-person basis, mixed-date estimates and Reed's 7,553/7,552 discrepancy.",
              "The fresh-context Astra xhigh [source review](review-results/TN003-a42f063-astra-xhigh-v1/review.md) checked all 62 claims, 40 quantities, 26 events and 26 supplied scan selections. Of 65 cited source/section pairs, 35 remain text/CSV-only. The [versioned correction pass](../docs/research/shiloh-review-corrections.md) implements estimation provenance, section-specific document dates, same-return dependence and Crittenden arrival wording. Focused review accepted all changed evidence; the [validator follow-up](review-results/TN003-corrections-5e23790-followup-v1/review.md) closed the sole implementation finding. The [feature-admission design](../docs/feature-admission.md) and [13 source-bound cases](../docs/research/shiloh-admission-examples.md) have a separate Astra xhigh [design review](review-results/feature-admission-838189f-astra-xhigh-v1/review.md) with no required corrections. The cases reference 26/62 claims, 27/40 quantities and 8/26 events, emitting zero model rows. The [offline validator](../docs/admission-validator.md) now checks all 40 Shiloh troop observations and retains the complete frame without promotion. The Astra xhigh [implementation review and focused follow-up](review-results/admission-implementation-1264e21-followup-v1/primary-assessment.md) accepted fixes for observation reuse, joint scenario coverage and calendar-date ordering. All 82 tests pass. Historical boundary and population mappings still require evidence-use review; no feature is admitted and historical disputes remain open.",
              "The separate [opening-boundary/population proposal](../docs/research/shiloh-opening-boundary-v1.md) has an explicit [v2 ledger](admission/shiloh-opening-v2-check.json): 7 blocked / 33 excluded across the same 40 observations and complete frame, with zero complete or promoted rows. The default v1 ledger above is unchanged. Its [Astra xhigh review and primary assessment](review-results/shiloh-opening-330599b-astra-xhigh-v1/primary-assessment.md) accept the bounded proposal with one nonblocking precision clarification. First-contact identification, the mapped area and both full populations remain unresolved. The [contact-and-location packet](../docs/research/shiloh-contact-location-v1.md) now compares nine participant reports, 16 visually inspected book pages and two maps, with 14 attributed assertions and no input promotion. Astra xhigh reviewed the packet; two literal transcription errors are [corrected in versioned sources](../docs/research/shiloh-contact-location-corrections-v1.md) with primary verification and no historical assertion change. Next audit the April 3–5 contact chain and engagement segmentation; map control, ford guards and the afloat rule remain open.",
              "Then expand by complete campaign, retaining every unscorable engagement in the coverage denominator.",
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
        inputs = sorted((root / "generalship").glob("*.py")) + [root / "data/sources.json", root / "data/pilot/cohort.json"]
        inputs += sorted((root / "data/evidence").rglob("*.json"))
        inputs += sorted(p for p in (root / "data/admission").rglob('*') if p.is_file())
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
            "admission_promoted_rows": admission['promoted_rows'], "artifacts_written": write}


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
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command in {"check", "build"}:
            result = run_build(root, write=args.command == "build")
        elif args.command == 'admission-check':
            checked = check_admission(root, args.path)
            result = checked if args.details else {
                'kind': checked['kind'], 'status': checked.get('release_status', checked['status']),
                'coverage': {k: v for k, v in checked['coverage'].items() if k != 'ledger'},
                'scenario_issues': checked['scenario_issues'], 'promoted_rows': checked['promoted_rows']}
            print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
            return int(checked['status'] == 'invalid' or bool(checked['scenario_issues'])
                       or checked.get('release_status') == 'blocked')
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
