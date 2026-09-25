# Primary assessment: grade E strength design

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `2779bb6828ee09eb2079db6047b4d8908362fffb`. Its
SHA-256 is `b5aa284bcab581c7b40c81f145bf3f43996c9bc6ce72a7b333675a29b03351d3`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `27a3dc41d7d2c459d95c9b4ff6b9869376ed7f1e`; see [dispatch.json](dispatch.json).

The primary checked each finding against the accepted designs and the ledgers and applied all
eight required corrections to `docs/strength-imputation.md`, with ten of eleven advisories.

## Required findings

- **R1** (accepted applied): Bounds limited to rule 7-eligible directional bounds (class A or B apart from bound codes); printed values; set-aside inputs listed with reasons; bound_not_applied label; no post-start information in grade E. all_bounds view added.
- **R2** (accepted applied): joint_command sides use echelon unknown in training and imputation (label joint_command_echelon_unknown); ledger_echelon_joint view added.
- **R3** (accepted applied): General merge rule; regiment and flotilla merge into unknown; naval_side label; no_naval_grade_e view added.
- **R4** (accepted applied): Force feature stated as x = (US - CS)/(US + CS).
- **R5** (accepted applied): Ridge objective, p, single fit, LOO scoring against the refit, calibration grid, draw stream and inverse-CDF sampling, shared imputations specified.
- **R6** (accepted applied): Endpoint refits added; median_imputation defined as the view_sensitive reference; non-robustness views listed and excluded from view_sensitive; strength_graded_only must reproduce run 2.
- **R7** (accepted applied): Per-commander outcome minus p uses the held-out strength-only probability averaged over imputations.
- **R8** (accepted applied): Superseded clauses named in the header; §8 states grade E borrows strength and that transfer to sparser eras is not shown.

## Advisories

- **A1** (accepted applied): Composition table and LOO error by echelon added to the output.
- **A2** (accepted applied): Grade D status against recorded result declared as a fixed descriptive output.
- **A3** (accepted applied): Leave-one-campaign-out coverage reported; calibration on observed sides stated.
- **A4** (accepted applied): Mixed response bases stated; train_graded_ab view added.
- **A5** (accepted applied): On conflicting applicable bounds, neither bound is applied (label bound_conflict).
- **A6** (accepted applied): Monte Carlo check on imputations 1-10 and 11-20 reported outside the verdict.
- **A7** (accepted applied): Pooled point estimate named as such (mean of modes, not a mode).
- **A8** (accepted applied): Header states the owner chose replacement after run 2, over the recommended option.
- **A9** (accepted applied): Theater source named (cwsac_campaigns.csv) and included in the authorization.
- **A10** (accepted applied): Negligible-mass fallback: point at the nearer bound, label bound_dominates.
- **A11** (kept as is): Manifest coverage noted for future bundles.

This AI review is a separate analysis, not historical adjudication, feature admission or
authorization of any fit.
