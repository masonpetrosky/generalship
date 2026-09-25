# Estimate-layer evaluation: separate review of the implementation and results

Review prepared commit `ce6da9a7a562778dd3ae81c82e3233809676ba65` against `4ba48a12b51a1a654710777c4ac475fde1ada938`. Sibling inputs.json binds
27 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show ce6da9a7a562778dd3ae81c82e3233809676ba65:<path>` first.

Read AGENTS.md, the accepted design `docs/strength-estimates.md` (its §6 is the locked
evaluation plan), the ledger memo `docs/research/strength-estimates-ledger-v1.md`, the new
memo `docs/research/estimate-evaluation-v1.md`, the authorization record
`data/estimates/evaluation-authorization-v1.json`, `generalship/estimate_eval.py`,
`generalship/baseline.py`, `generalship/estimates.py`, `tests/test_estimate_eval.py` and the
outputs `artifacts/estimate-evaluation.json` and `artifacts/estimate-evaluation.md`.

Scope: the evaluation code and its gate, the optimizer change in `baseline.py`, the results
and the memo. The ledger's per-engagement coding was reviewed separately; do not repeat it.

Check:

1. **Plan fidelity.** Does `estimate_eval.py` implement design §6 exactly: the unchanged
   model and features, leave-one-campaign-out over the campaigns present, the comparators,
   the post-start leakage exclusion, the three nested sets, the evaluability rule, every named
   sensitivity refit (endpoint refits as true refits, label exclusions one at a time, rule 4
   factor 1, the alternative basis order, the upper-middle median), the common-row comparison
   (both models fit on the same common training rows; identical-by-construction rows), the
   newly-covered comparison, and the reporting items (Brier and log loss, battle- and
   campaign-weighted, counts, grade mix, §5 label counts, excluded rows, flags)? Name any
   divergence with the concrete code path.
2. **Gate.** Does the authorization gate refuse a fit when the record's hash differs from the
   ledger, and is the record itself an adequate §6 authorization (explicit, naming the
   reviewed ledger hash, choosing option (a) or (b))? Say what it does and does not establish.
3. **Optimizer change.** `fit_logistic` now returns the full Newton step when the Newton
   decrement `g·d` is below 1e-12. Is this sound for this ridge-penalized objective, does it
   change the minimizer, and is it safe for the frozen baseline? Confirm offline that
   `artifacts/baseline.json` is reproduced byte-for-byte (for example, by running the baseline
   evaluation in memory and comparing with the committed file; do not overwrite artifacts).
   Is the regression test meaningful?
4. **Results and wording.** Recompute the headline numbers from the JSON (or by re-running
   `evaluate_estimates` in memory). Is every number in the memo, README and roadmap correct?
   Does any sentence overclaim (improvement, significance, accuracy of estimates, anything
   about commanders), or understate a weakness?

Run `make check` offline. You may run `python3 -c` scripts that import the package and
compute in memory. Do not run `make reproduce`, `make estimate-evaluation`, build or packet
commands, and do not modify primary artifacts. No network, new research or agents.

Write only `artifacts/review-results/est-eval-review-ce6da9a-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you
actually inspected. Give required corrections as exact, evidence-backed changes (file,
location, replacement), or say there are none; list advisories separately. A concise review
is sufficient. Return the path and outcome. An AI review is not historical adjudication,
feature admission or authorization of any fit.
