# Primary assessment: commander ratings run 2

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `8befd972c30fba5c9e2da1c283dd31182a450cd8`. Its
SHA-256 is `1bb565edd2372582185d6327844a1450b71a957a9eaf86a791d79a627ad58bac`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `3e965cb89633f7a8a3fdb42e10e57d3118c56133`; see [dispatch.json](dispatch.json).
It reproduced all eight run-1 and run-2 outputs byte for byte and recomputed the held-out verdict
independently.

The primary checked each finding against the design and the code. R1 was confirmed against
strength design §6 and the regenerated counts match the reviewer's in-memory check. The run was
regenerated under the same authorizations, which bind the ledgers, not the code; the verdict and
every rating are unchanged. [correction.json](correction.json) binds the corrected files.

## Required findings

- **R1** (accepted applied): estimate_eval.evaluate_estimates: for run 2, common rows are limited to rows of the frozen 23-engagement baseline (strength design §6). Regenerated: common rows 18/20/21 (identical by construction 16/18/18), new rows 43/60/105; primary metrics, sensitivity refits and the ratings unchanged except raw_residual_input.sha256.
- **R2** (accepted applied): Memo verdict wording replaced with the design §5 reading ("held-out log loss was lower on these rows") and the cross-run paragraph replaced with the reviewer text.
- **R3** (accepted applied): Memo: view_sensitive counted over the 68 robustness views; the three outcome-only views do not set it.
- **R4** (accepted applied): Memo: outcome-only scope qualified (301 in-scope decisive rows, the TN035 view, largest moves among ranked commanders; Wilson -0.34 among all modelled).
- **R5** (accepted applied): Memo: the temporal split is described as carrying no verdict and not supporting it; its years are recorded as the author's run-2 choice set at cef8f3f before the run commit.
- **R6** (accepted applied): ratings.report_text states the ordering key (median within-side rank, ties by theta mode) and cautions against reading the order as a ranking; v1 output is unchanged (improved is false there).

## Advisories

- **A1** (accepted applied): Evaluation report: the frozen baseline reference is marked "cohort v1, not these rows" for run 2.
- **A2** (not adopted): The bindings hold through the ledgers and authorizations; explicit cross-checks are deferred to any future run.
- **A3** (not adopted): No unit test added for RUNS[2]; the reviewer verified the refusal and frame checks in memory, and the committed outputs reproduce.
- **A4** (kept as is): The completeness comment holds for cohort v2 (verified by the reviewer).
- **A5** (accepted applied): Memo: "Ranks overlap completely. On each side every pair's 80% rank intervals overlap."
- **A6** (accepted applied): Memo: the 39/27 campaign counts are marked descriptive, not part of the verdict.
- **A7** (kept as is): Noted: the only code change after cef8f3f before the run was a stdout label.
- **A8** (not adopted): The addendum is bound by the ledgers' hashes and cannot change without rebuilding them; the memo states the full-war frame and the §8 limits.

This AI review is a separate analysis, not historical adjudication, feature admission or
authorization of any fit.
