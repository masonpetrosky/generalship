# Admission implementation review: corrections needed

This is separate AI implementation analysis, not human historical adjudication, source independence certification, or feature admission. Reviewed commit: `7b41de14011dbb7150a4b4ea2a30e570a0421e33`; base: `aac2ed229b3fb8a4d0db4cb8a0a332548ede39b1`; accepted contract hash: `b858b7a27f3617408779c928ea545da814b31229ff2c40caf64927773f320c99`. Verdict: **corrections_needed**, with three P2 findings. No implementation or historical evidence was edited by this reviewer.

Reviewer task: `/root/admission_implementation_review`; model: `gpt-6-astra`; reasoning effort: `xhigh`; fresh context: `fork_turns: none`; date: 2026-09-20. The execution identity and assignment are recorded in `dispatch.json`. The initial duplicate-reference example was forwarded by the primary and independently reproduced; the other required findings arose from this review. The primary began corrections after all reported tests/reproductions completed. Final input bindings were checked against immutable Git blobs at the reviewed commit; working-tree corrections are outside this verdict.

## Required corrections

### ADM-IMPL-R1 — [P2] Bind each observation reference to one leaf mapping within a candidate

Location: `generalship/admission.py:303-305`.

Quantity leaves are indexed by node ID, while overlap checks trust each node's authored members. Two leaves can reference the exact same immutable quantity under different membership atoms and be summed as disjoint evidence.

Reproduction: Starting with tests/admission_fixtures.fixture, set p["candidates"][0]["nodes"][1]["reference"] = "us-a"; keep its members ["us-b"]. Save, validate, then build the synthetic release and audit it with allow_test_only=True.

Observed: `{"US_preview_bounds": [80, 80], "US_status": "eligible_candidate", "release_admitted_candidates": 2, "release_status": "verified", "scenario_issues": []}`.

Expected: Reject conflicting reuse of the same observation; it must not produce a complete preview row or verified audit.

Correction: Enforce one observation leaf per (kind, reference) within each candidate, or otherwise guarantee a single consistent semantic mapping for that immutable observation. Permit multiple references to the same existing DAG node so valid (A+B)-B remains supported. Add a duplicate-reference regression while preserving ordinary disjoint sum/subtraction cases.

Contract sections 5 and 8 require disjoint populations and forbid double counting. Detecting conflicting reuse of one bound quantity is structural and does not require historical adjudication.

### ADM-IMPL-R2 — [P2] Require coherent joint representation when compatible sides are available

Location: `generalship/admission.py:433-435`.

Scenario completeness checks only whether each candidate ID appears anywhere. Splitting two applicable, compatible same-boundary sides into separate partial scenarios removes a fully available engagement from every dataset while the release audit verifies and marks both candidates admitted.

Reproduction: Copy the fixture base scenario as cs-only. Set the base SYN001 Confederate assignment to null, and the cs-only SYN001 US assignment to null. Both candidates and their shared boundary remain unchanged. Validate and audit the synthetic release.

Observed: `{"candidate_statuses": {"cs": "eligible_candidate", "us": "eligible_candidate"}, "preview_rows_by_scenario": {"base": [], "cs-only": []}, "release_admitted_candidates": 2, "release_status": "verified", "scenario_issues": []}`.

Expected: Report unresolved joint scenario coverage and prevent verified audit because a compatible complete assignment exists but is omitted everywhere.

Correction: For outcome/grain-eligible engagements, require each applicable candidate with a compatible opposite-side candidate on the same boundary to occur in at least one coherent complete assignment, or block unresolved scenario coverage. Preserve legitimate partial-side coverage when the other side is absent or inapplicable, and retain unsupported outcomes/aggregate operations in the denominator. This does not require full Cartesian expansion.

The locked all_applicable_joint_alternatives_no_weights policy and contract sections 5 and 7 require coherent datasets and visible required exclusions; candidate-ID union coverage cannot establish that.

### ADM-IMPL-R3 — [P2] Compare parsed quantity dates at the temporal gate

Location: `generalship/admission.py:332-337`.

Quantity period validation accepts ISO forms recognized by date.fromisoformat, but admission compares those original strings lexicographically to a canonical calendar-date boundary. A valid ISO week date can sort before the boundary while representing a later day.

Reproduction: Set the fixture boundary to 2000-01-01 and quantity us-a period start/end to 1999-W52-7. date.fromisoformat parses the latter as 2000-01-02. Save, validate and audit the synthetic release.

Observed: `{"US_reasons": [], "US_status": "eligible_candidate", "boundary": "2000-01-01", "parsed_period": "2000-01-02", "period_literal": "1999-W52-7", "release_status": "verified"}`.

Expected: Exclude the post-boundary observation (or reject noncanonical input at schema validation); clean mapping labels must not override its known later state date.

Correction: Compare parsed date objects for quantity start/end and boundary while preserving original source period text, or require canonical YYYY-MM-DD dates before comparison. Add a cross-year ISO-week post-boundary regression and a basic-format pre-boundary case to cover false acceptance and false exclusion.

Contract sections 4 and 8 require known post-boundary state to be excluded transitively. Calendar ordering is structural and independent of source entailment.

## Verified behavior and coverage

- Read AGENTS.md, README, methodology, roadmap, evidence contract, sources documentation, accepted feature-admission design and admission-validator documentation. Inspected all 616 lines of admission.py, all admission tests and fixture code, the CLI/evidence changes, and supporting source/dossier validation routines.
- Independently ran `make check`: all **79 tests passed**, including **27 admission tests**, followed by successful `generalship check`. Runtime: **Python 3.14.7**. No network or model jobs were needed. A separate Python 3.11 interpreter was not exercised.
- The tests meaningfully exercise positive synthetic audit, first-review waiting, adverse/insufficient review scope, exact binding changes, transitive post-state/outcome leakage, missing values, basic overlap/nesting, cycles, test-only rejection, source aliases, incompatible joint choices, snapshot replay isolation and coverage separation. The three reproductions above cover structural gaps in that passing suite.
- The recomputed real proposal audit exactly equaled the committed admission-check.json. Candidate quantity references form an exact unique census of **40/40 Shiloh quantities**. Coverage: **127/127 engagements**, **36/36 campaign groups**, three dossiers, one engagement with candidates, **18 blocked / 22 excluded**, zero eligible candidates, zero complete rows, and zero promoted rows. The snapshot binds 53 registry entries and 50 distinct raw paths. These are structural/source-binding checks, not fresh historical entailment or scan review.
- A temporary rebuild matched all eight committed outputs byte-for-byte: admission-check.json, baseline.json, battles.json, evidence-checks.json, pilot-report.md, quality.json, receipt.json, and research-queue.json. The complete generated pilot report was inspected. The unchanged baseline retains **23 engagements / 13 eligible campaign groups**, with Brier **0.2768816348133779** versus **0.25** for equal odds.
- The original dossier, current source registry, battle/baseline/quality/research-queue artifacts and prepared Shiloh packet are byte-identical to the base commit. Every dispatched input hash matched the reviewed commit.
- Proposal and release audit report `emitted_rows=[]` and `promoted_rows=0`; the CLI/build has no test override or enriched-model installer. The verified synthetic audits in these findings are audit results only. No real historical admission manifest, approval or model installation was created.

Two exploratory probes also tested identical scenario assignments and diagonal-only choices across separate source-choice dimensions. They are not additional required findings. This review does not require full Cartesian expansion, scenario averaging, or a model behavior absent from the non-promoting implementation. R2 concerns the narrow omission of an available coherent complete assignment.

## Reproduce the three findings

Run from an unchanged checkout of the reviewed commit. Only explicitly synthetic temporary artifacts are written, through the Python-only test harness. This does not create production approval or promote model inputs.

```sh
python3 - <<'PY'
from copy import deepcopy
from datetime import date
from pathlib import Path
import json, sys, tempfile
sys.path.insert(0, 'tests')
from admission_fixtures import fixture, save, release
from generalship.admission import validate_proposal, audit_release

def duplicate_reference(p, s):
    p['candidates'][0]['nodes'][1]['reference'] = 'us-a'

def split_sides(p, s):
    other = deepcopy(p['scenarios'][0])
    other['id'] = 'cs-only'
    other['assignments']['SYN001']['US'] = None
    p['scenarios'][0]['assignments']['SYN001']['Confederate'] = None
    p['scenarios'].append(other)

def week_date(p, s):
    p['boundaries'][0]['date'] = '2000-01-01'
    s['dossiers'][0]['quantities'][0]['period'].update(
        start='1999-W52-7', end='1999-W52-7')
    assert date.fromisoformat('1999-W52-7').isoformat() == '2000-01-02'

for mutate in (duplicate_reference, split_sides, week_date):
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        p, s = fixture(root)
        mutate(p, s)
        save(root, p, s)
        report = validate_proposal(root, 'data/proposal.json', allow_test_only=True)
        release(root)
        audited = audit_release(root, 'data/release.json', allow_test_only=True)
        print(json.dumps({
            'case': mutate.__name__,
            'decisions': [{k: d[k] for k in ('candidate_id', 'status', 'preview_bounds')}
                          for d in report['decisions']],
            'scenario_issues': report['scenario_issues'],
            'rows': report['preview_rows_by_scenario'],
            'release_status': audited['release_status'],
            'admitted_candidates': audited['release_admitted_candidates'],
            'promoted_rows': audited['promoted_rows']}, sort_keys=True))
PY
```

## Input hashes and limits

The frozen snapshot binds every source entry's metadata and raw bytes. No historical passage or scan was independently adjudicated in this implementation review. Hashes, declared identities and citation matches cannot establish historical truth, source independence, reviewer sincerity or entailment. The primary must reconcile these findings and obtain a focused follow-up on the changed implementation.

| Input | SHA-256 |
|---|---|
| `generalship/admission.py` | `59beaa31827b394e5191fe5b852abe351d450389fab35ae99d90e746aff58b3e` |
| `generalship/cli.py` | `0743e6a6159b756f174f3f97634c9a6f99bda6b868d04488a54f8223f789aec6` |
| `generalship/evidence.py` | `cf52c44b86956201cb6fa8c1a9c3cec85047ada71366f656330c551b536dee69` |
| `tests/test_admission.py` | `951863576273e4f2b10e76932e9ff223de974f23ed57943a6eb7506f9b179b74` |
| `tests/admission_fixtures.py` | `8a0c50aaf91bde0430be2d35d71d501bc979c3b874a9ad8efc560dc52e38eb8a` |
| `data/admission/shiloh-opening-v1.json` | `a4eca5a91e8c93baa2243a314e8d8e76c754d44ef42d7926435847efe849f5b6` |
| `data/admission/snapshots/pilot-evidence-aac2ed2-v1.json` | `d3f3a2b9f2e8e48726812e08bf925d7c0e60b8ff012a4b0d4cdc95581a5a884c` |
| `data/admission/snapshots/feature-admission-v1.md` | `b858b7a27f3617408779c928ea545da814b31229ff2c40caf64927773f320c99` |
| `artifacts/admission-check.json` | `d607150efae2cf06652792c87cd03585f937a9a4393942c9da87165f5e931100` |
| `docs/admission-validator.md` | `8f86aafbb976e7284c11bc53f3dc3457fbf507dd77f81be84acd629355e62eb4` |
| `docs/feature-admission.md` | `b858b7a27f3617408779c928ea545da814b31229ff2c40caf64927773f320c99` |
| `data/evidence/TN003.json` | `fb622c81b48110d1d7b25212b5c3f10881c4a7724a9ccbb93ef793816cf100ee` |
| `data/sources.json` | `3430c1ef145256fc8edd8638fdf565f7f0c0ae4e5feed237b3cd5db6cf4322e7` |
| `data/pilot/cohort.json` | `17d08348ed1399a0f0033ded3b1ba40c541d342b6aeed920cf2c26818ee6adc8` |
| `artifacts/baseline.json` | `592b62bef69b4f76a626fa7c06f17f8813b02bcf4c6753601d4ad2b413e09595` |
| `generalship/sources.py` | `98df0d690b2a2c9e0ac4c55c4ad8e496c28ad26e6054f1053097cd7ebefe6ab4` |
