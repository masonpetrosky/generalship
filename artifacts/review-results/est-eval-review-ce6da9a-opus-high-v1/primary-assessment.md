# Primary assessment: estimate-layer evaluation review

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`ce6da9a7a562778dd3ae81c82e3233809676ba65`. Its SHA-256 is `efa2b7ca134cbf58d2d3dad46b83cc2fffe586dd3a83baf26ff5247d2d3a4e96`. The reviewer ran as a fresh headless session with the
`evidence-reviewer` definition in a detached worktree of bundle commit `26584abfe5c723b9e79b8b7e71c0ab1c8c829d1c`; see
[dispatch.json](dispatch.json).

The primary checked each finding against the code, the committed outputs and the ledger. All
required findings are accepted and applied. Regenerating the outputs under the unchanged
authorization changed no metric (checked field by field against the prepared commit).

## Required findings

- **R1** (accepted applied): Excluded-row count: the memo and report now say 7 rows carry a post-start side and 6 are excluded from the A-C fits (WV010 enters no row set).
- **R2** (accepted applied): Memo: all of the A-C battle-weighted gain comes from the 16 new rows; common rows score 0.2932.
- **R3** (accepted applied): Memo: "nearly the same predictions" (largest difference 0.007; 0.2947 against 0.2941).
- **R4** (accepted applied): Memo and roadmap: option (a) is the recording agent's reading, not the owner's words; the owner is asked to confirm it.
- **R5** (accepted applied): Sensitivity results now carry label counts, flags and post-start exclusion counts; metrics unchanged (verified).

## Advisories

- **A1** (accepted applied): Significance wording: no test was run; no difference is presented as significant.
- **A2** (accepted applied): Optimizer note corrected (g·d 2.7e-17; 34 of 570 fits failed before).
- **A3** (accepted applied): README summary reworded as suggested.
- **A4** (accepted applied): Memo states the campaign-weighted log-loss tie at A-C.
- **A5** (accepted applied): Output binds the authorization record SHA-256; the gate requires admits_feature and changes_baseline to be false.
- **A6** (accepted applied): Test compares FROZEN_REFERENCE with artifacts/baseline.json.
- **A7** (kept as is): Owner confirmation of option (a) is requested in the report; a v2 record would follow only if the owner answers.
- **A8** (accepted applied): Common-row and newly-covered results carry grade mix, label counts and flags.
- **A9** (accepted applied): Regression test also asserts the ridge-penalized gradient is below 1e-9.

The regenerated `artifacts/estimate-evaluation.json` has SHA-256 `d02fa45ce7b876940393deb104725fc856ffbc11fb8929f564beb43a94a59886`. This AI review is
a separate analysis, not historical adjudication, feature admission or a new authorization.
The frozen baseline is unchanged.
