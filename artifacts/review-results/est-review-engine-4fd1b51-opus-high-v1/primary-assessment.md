# Primary assessment: best-estimate ledger review, the engine, checker, tests and memo

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`4fd1b512f9e4db0402537bfe577031a6cc6939f6`. Its SHA-256 is `16fe667725334e8cdd42d7564cb3e20039845a819e1ab75c7d9419f2dbc03870`. The reviewer ran as a fresh headless session with the
`evidence-reviewer` definition in a detached worktree of bundle commit `98212664305094d1ea7a4f02d00c89006edb919b`; see
[dispatch.json](dispatch.json).

The primary checked every required finding against the cited passages, the frozen CSV
cells or the registered Livermore page images before applying it. All required findings
are accepted and applied.

## Required findings

- **R1** (accepted applied): estimate_side: an opponent candidate that sets high joins the range, so its §5 labels apply; test added for the synthetic post-start case.
- **R2** (accepted applied): Count wording replaced in the memo and README, with the reconciled counts (43 with both sides estimated, 37 fit-eligible).
- **R3** (accepted applied): Memo restatement wording replaced, updated for batch 2 R8/R9 (KY009 and TN006 are no longer linked).

## Advisories

- **A1** (accepted applied): Memo records livermore-transcription-v1 as a declared §2 exception.
- **A2** (kept as is): Owner-level choice left open: the unlinked restatement sides are reported as lacking single_input.
- **A3** (accepted applied): Checker assertions added. The row-5 direction check is bound in {upper, lower, null}, because caps on part of a side now carry null.
- **A4** (accepted applied): Non-discriminating test fixed; tests added for floor_applied, lower bounds and conflicts, the residual-C bound, post-start hull inclusion, basis_mixed, nested_sets and eight checker tamper cases.
- **A5** (not adopted): Receipt already hashes the ledger and the build output reports the estimate summary; no separate status field added.
- **A6** (not adopted): quoted_ratio and group-value paths remain unused; document them before first use.
- **A7** (accepted applied): Memo states that basis_mixed needs both points.
- **A8** (accepted applied): Memo says 7 post-start = 6 + WV010; stray line deleted; 'for lack of a usable candidate value' in the roadmap.
- **A9** (accepted applied): Design acceptance recorded in the memo.
- **A10** (not adopted): No role field added; deferred to a later schema version.

## Result

The corrected ledger `data/estimates/side-strength-v1.json` (SHA-256 `0656b03cbdaa088849dc3795f9c6a9e9d6762be10f53f28e4285be46f7fcde89`) replays with `estimate-check`,
together with the corrections from the other four reviews: sides A/B/C/D 59/21/26/76;
fit-eligible rows 21/29/37 at A, A-B and A-C; 7 rows excluded as post-start. The engine is
`generalship/estimates.py` (SHA-256 `af540a924aed29b20032319b8779742c0f43e991c118ee747672bba73fc3a32f`). [correction.json](correction.json)
lists every disposition.

This AI review is a separate analysis. It is not historical adjudication, proof of source
independence or feature admission. No follow-up review of the corrections was run. Nothing
is fitted; the locked evaluation (design §6) needs an explicit owner authorization naming
the reviewed ledger's hash. The frozen baseline is unchanged.
