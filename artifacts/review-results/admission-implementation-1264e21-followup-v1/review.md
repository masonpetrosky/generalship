# Admission implementation follow-up: accepted

Verdict: **accept**, limited to closure of ADM-IMPL-R1, ADM-IMPL-R2 and ADM-IMPL-R3 at `1264e217fc1e952b2115a316313f9dfeea4869ec`, compared with `7b41de14011dbb7150a4b4ea2a30e570a0421e33`. There are no unresolved findings in this focused follow-up. This is AI implementation analysis; it does not admit historical features or establish human historical adjudication.

Reviewer task: `/root/admission_implementation_review`; model: `gpt-6-astra`; reasoning effort: `xhigh`; date: 2026-09-20. This continues the original fresh-context reviewer task under the primary's explicit bounded follow-up assignment. The original review and result remain byte-identical, with hashes `75bee8d61c35fba33d780519f7a9499c7c700242ac7fd5f576d962ab8ad04493` and `b55cf1e38770de8a189ca7589bd3e9ec35568b260f583207b264cfe51079f7e8` respectively.

## Findings closed

### ADM-IMPL-R1: closed

Location: `generalship/admission.py:294-298`. One leaf per (kind, reference) closes the conflicting observation-remapping bypass without disallowing shared-node arithmetic.

The original duplicate-reference mutation is invalid with no preview bounds; audit rejects with Invalid proposal cannot be released. Shared existing DAG node reuse for (A+B)-B remains eligible and the synthetic audit verifies US bounds [40,40].

### ADM-IMPL-R2: closed

Location: `generalship/admission.py:448-465`. Candidate coverage now requires an available coherent complete assignment on eligible frame rows, while retaining legitimate missingness and target/grain exclusions. This does not require Cartesian expansion.

The original US-only/CS-only split produces compatible_candidate_missing_joint_assignment for both candidates and the release audit rejects. Separate probes for absent, blocked and explicitly incompatible opposite sides, inconclusive outcome and aggregate operation produce no joint-coverage issues and no complete rows.

### ADM-IMPL-R3: closed

Location: `generalship/admission.py:337-343`. Parsed date comparisons close the lexicographic temporal bypass while retaining original evidence text.

The original 1999-W52-7 period against boundary 2000-01-01 is excluded with observed_state_after_boundary; audit rejects. Basic pre-boundary date 20000101 against 2000-01-02 remains eligible with a verified synthetic audit. The added regression also checks basic-format later dates and preserves original period strings.

## Tests and inspected scope

Inspected the complete five-file diff: admission.py, test_admission.py, admission-validator.md, regenerated admission-check.json, and receipt.json. The implementation changes are limited to duplicate observation identity, parsed quantity dates, and coherent joint coverage. The documentation reflects those checks. All supplied hashes matched the exact reviewed commit and executing files.

Independently ran `PYTHONPATH=tests python3 -m unittest test_admission -v`: **30/30 tests passed** on Python **3.14.7**. The full 82-test suite and make reproduce were reported by the primary; this focused follow-up did not rerun that broader work.

Independently exercised **11 temporary synthetic proposal/release probes**:

| Probe | Result |
|---|---|
| Unmodified fixture | Eligible US [100,100], Confederate [80,80]; one row; audit verified |
| Original duplicate observation | US invalid; no complete row; audit rejected |
| Original split compatible sides | Both joint assignments missing; audit rejected |
| Original cross-year week date | US excluded as post-boundary; audit rejected |
| Basic-format earlier date | Eligible; one row; audit verified |
| Shared DAG subtraction `(A+B)-B` | Eligible US [40,40]; one row; audit verified |
| Absent opposite candidate | Partial coverage retained; zero rows; audit verified |
| Blocked opposite candidate | Partial coverage retained; zero rows; audit verified |
| Explicitly incompatible opposite source choice | Partial scenarios retained; zero rows; audit verified |
| Inconclusive outcome | Frame exclusion retained; zero rows; audit verified |
| Aggregate operation | Frame exclusion retained; zero rows; audit verified |

Verified audits above are test-only audits and always retain `emitted_rows=[]` and `promoted_rows=0`. They are not historical approvals or model installation.

Recomputed the default production proposal audit and compared its full result to committed admission-check.json: exact equality. It still covers **127 engagements / 36 campaigns**, with **18 blocked / 22 excluded** quantities, zero complete rows and zero promoted rows. The real proposal, evidence snapshot, Shiloh dossier, source registry and accepted contract hashes are unchanged.

This follow-up does not reopen the full implementation review, claim exhaustive adversarial coverage, independently review historical passage entailment or scans, certify reviewer sincerity or source independence, or validate an enriched model. No implementation, evidence, original review, commit or push was changed by this reviewer.

## Exact input bindings

| Input | SHA-256 |
|---|---|
| `generalship/admission.py` | `55927091b8f7fa4e6a1eaef8a3b57d54de341aff01dfc666eda678a360941993` |
| `tests/test_admission.py` | `9e3096dc06b8213fbc46a67a2e54e5814b32eb3b41cb1713713c4ddd163ecdcb` |
| `docs/admission-validator.md` | `ffaaeecd72b08b1162ccb38ea4f7af30d0ef0fffd7ed4e87c5a1778c7dd33bfd` |
| `artifacts/admission-check.json` | `d0e8d3286bd34cb34cdd2a0a1d74f0b2d3c2f6ddf955c8e66336c4cb213ee756` |
| `artifacts/receipt.json` | `02ababbf44788545ec883c88e364617a56b1c7c0f84ff6940c03f60ac2649d0a` |
| `generalship/evidence.py` | `cf52c44b86956201cb6fa8c1a9c3cec85047ada71366f656330c551b536dee69` |
| `generalship/sources.py` | `98df0d690b2a2c9e0ac4c55c4ad8e496c28ad26e6054f1053097cd7ebefe6ab4` |
| `tests/admission_fixtures.py` | `8a0c50aaf91bde0430be2d35d71d501bc979c3b874a9ad8efc560dc52e38eb8a` |
| `data/admission/shiloh-opening-v1.json` | `a4eca5a91e8c93baa2243a314e8d8e76c754d44ef42d7926435847efe849f5b6` |
| `data/admission/snapshots/pilot-evidence-aac2ed2-v1.json` | `d3f3a2b9f2e8e48726812e08bf925d7c0e60b8ff012a4b0d4cdc95581a5a884c` |
| `data/evidence/TN003.json` | `fb622c81b48110d1d7b25212b5c3f10881c4a7724a9ccbb93ef793816cf100ee` |
| `data/sources.json` | `3430c1ef145256fc8edd8638fdf565f7f0c0ae4e5feed237b3cd5db6cf4322e7` |
| `docs/feature-admission.md` | `b858b7a27f3617408779c928ea545da814b31229ff2c40caf64927773f320c99` |
