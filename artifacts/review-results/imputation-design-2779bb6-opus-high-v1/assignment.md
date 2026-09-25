# Grade E strength design: separate design review

Review prepared commit `2779bb6828ee09eb2079db6047b4d8908362fffb` against `3f5c7a99d6e75ac6bdb16acb2eede4f8deff31a0`. Sibling inputs.json binds
20 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 2779bb6828ee09eb2079db6047b4d8908362fffb:<path>` first.

Read AGENTS.md, the draft `docs/strength-imputation.md`, the owner's decision
`data/estimates/owner-decision-grade-e-2026-09-25.json`, the accepted designs
`docs/strength-estimates.md` and `docs/commander-ratings.md`, the addendum `docs/ledgers-v2.md`,
the run-2 memo `docs/research/commander-ratings-v2.md`, and look at the reviewed ledgers
`data/estimates/side-strength-v2.json` and `data/command/responsibility-v2.json` (their grade D
sides, bound inputs and echelons) and the frozen tables in `data/raw/`. You may compute summaries
from these files in memory; do not fit the proposed model or any rating, and do not write
artifacts.

Check whether the design is sound and complete enough to implement without further choices:

1. **Leakage and circularity.** Does any input to grade E depend on the outcome, directly or
   through the ledgers' coding (for example bounds from post-outcome counts, echelons chosen with
   knowledge of the result)? Is excluding casualties right, and is anything else that should be
   excluded still in?
2. **The imputation model.** Are the predictors, reference levels, merges, ridge, σ, the
   leave-one-out calibration rule and the truncation to bounds well defined and appropriate for
   the data (training rows by echelon, theater, period)? Are there cases the rules do not cover
   (a side with only an upper bound below the modelled range, a naval side, a grade D side whose
   ledger has non-bound inputs, `unknown` echelon)? Is it biased in a way the design should state
   or correct (for example the training set over-representing large, famous battles)?
3. **Multiple imputation and the verdict.** Is averaging held-out probabilities over imputations,
   then scoring log loss, a sound replacement for the design §5 test? Is M = 20 enough? Is pooling
   Laplace draws across imputations a correct way to form intervals and ranks? Is the verdict rule
   still fixed and unambiguous? Are the declared views sufficient, and does anything allow tuning
   after results are seen?
4. **Fidelity to the owner's decision and the accepted designs.** Does the draft do what the owner
   asked, keep run 2 and the ledgers unchanged, and say plainly what grade E is and is not? Does it
   generalize to sparser eras as the owner intends?

Run `make check` offline. No build, packet, rating or evaluation commands; do not modify primary
artifacts. No network, new research or agents.

Write only `artifacts/review-results/imputation-design-2779bb6-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes to the design text (section, replacement),
or say there are none; list advisories separately. A concise review is sufficient. Return the path
and outcome. An AI review is not historical adjudication, feature admission or authorization of
any fit.
