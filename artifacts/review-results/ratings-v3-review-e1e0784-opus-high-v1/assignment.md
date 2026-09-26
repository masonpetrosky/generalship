# Commander ratings run 3 (all battles, grade E): separate review of code and results

Review prepared commit `e1e07849e7ba1649b8e21250f983150e78d5256f` against `3979161`. Sibling inputs.json binds
21 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show e1e07849e7ba1649b8e21250f983150e78d5256f:<path>` first.

Read AGENTS.md, the accepted design `docs/strength-imputation.md` (and its review
`artifacts/review-results/imputation-design-2779bb6-opus-high-v1/`), `docs/commander-ratings.md`
§§3–8, the authorization `data/command/rating-authorization-v3.json`, `generalship/imputation.py`,
`generalship/ratings_v3.py`, `tests/test_imputation.py`, the outputs
`artifacts/strength-imputation-v1.json` and `artifacts/commander-ratings-v3.{json,md}`, and the memo
`docs/research/commander-ratings-v3.md`.

The full run takes about 75 minutes; **do not rerun it.** Verify instead:

1. **Design fidelity.** Does `imputation.py` implement design §2 exactly (training rows, predictors,
   joint-command and merge rules, ridge fit, σ and p, leave-one-out calibration and k, bound
   eligibility and values, conflicts, truncation, `bound_dominates`, rounding, labels)? Does
   `ratings_v3.py` implement §§3–7 (301 rows and nesting, draw order and seed, shared imputations,
   pooled estimates and intervals, the held-out verdict on averaged probabilities, the Monte Carlo
   check, the views and which set `view_sensitive`, the raw residual p, the gate)? Name any
   divergence with its consequence.
2. **Reproduction, cheaply.** Confirm `artifacts/strength-imputation-v1.json` reproduces
   (`imputation.build(root, verify=False)`, a few seconds). From the stored held-out predictions,
   recompute both log losses, the improvement rule, the campaign counts and the effective
   denominator. Recompute one or two leave-one-campaign-out folds for one imputation in memory
   and check them against the stored per-row probabilities where possible. Do not write artifacts.
3. **Results and wording.** Is every number in the memo and report correct? Does anything
   overclaim or understate (the attenuated force coefficient, modelled-strength dependence,
   overlapping ranks, `not_connected`, selection)?

Run `make check` offline. No rating, evaluation, build or packet commands that write artifacts. No
network, new research or agents.

Write only `artifacts/review-results/ratings-v3-review-e1e0784-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (file, location, replacement), or say there
are none; list advisories separately. A concise review is sufficient. Return the path and outcome.
An AI review is not historical adjudication, feature admission or authorization of any fit.
