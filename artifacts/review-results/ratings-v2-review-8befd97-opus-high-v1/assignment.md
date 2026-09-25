# Commander residual ratings run 2 (cohort v2): separate review of the code change and results

Review prepared commit `8befd972c30fba5c9e2da1c283dd31182a450cd8` against `6fe077c`. Sibling inputs.json binds
29 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 8befd972c30fba5c9e2da1c283dd31182a450cd8:<path>` first.

Read AGENTS.md, the accepted design `docs/commander-ratings.md` (§§3–8 are the locked plan), the
strength design `docs/strength-estimates.md` §6, the addendum `docs/ledgers-v2.md`, the
authorizations `data/command/rating-authorization-v2.json` and
`data/estimates/evaluation-authorization-v2.json`, `generalship/ratings.py`,
`generalship/estimate_eval.py`, `generalship/dataset.py`, `generalship/cli.py`, `Makefile`, the
outputs `artifacts/estimate-evaluation-v2.{json,md}` and `artifacts/commander-ratings-v2.{json,md}`,
and the memo `docs/research/commander-ratings-v2.md`. For comparison, the run-1 memo
`docs/research/commander-ratings-v1.md` and its review
`artifacts/review-results/ratings-run-review-14c8c3b-opus-high-v1/review.md`. The v2 ledgers were
reviewed separately; do not re-review their coding.

Check:

1. **Parameterization.** The diff turns the runs into versioned `RUNS`. Does run 2 bind exactly the
   authorized ledger, registry and cohort hashes, refuse otherwise, and replay the ledger checkers
   first? Does run 1 still reproduce `artifacts/commander-ratings.json` and
   `artifacts/estimate-evaluation.json` exactly (check in memory)? Is `build_dataset(root,
   'data/pilot/cohort-v2.json')` correct for the v2 frame (records, outcomes, campaigns,
   `baseline_eligible`)? Is anything v1-specific left in the run-2 path (hard-coded row counts,
   years, view names, report text)?
2. **Plan fidelity for run 2.** The primary rows, the held-out verdict (both weightings), the
   effective denominator, every §6 view (including the outcome-only views over all decisive rows,
   with rule 7 nesting), `view_sensitive`, `unranked_in_view`, the raw residuals (from
   `estimate-evaluation-v2.json`), connectivity and the report's ordering now that the verdict is
   positive. The temporal split's years (1861–1863 train, 1864–1865 test) are a v2 choice
   recorded in the code and memo; is it reasonable and clearly non-verdict?
3. **Numerical check.** Recompute the headline verdict independently offline (your own small
   implementation or a check of the stored predictions). Confirm the reported log losses, the
   39/27 campaign split, the effective denominator and a sample of θ intervals and rank intervals.
4. **Results and wording.** Is every number in the memo and both Markdown reports correct? Does
   any sentence overclaim (skill, significance, robustness, a ranking of record) or understate a
   weakness (small margins, overlapping rank intervals, `not_connected`, coverage selection,
   source dependence)? Is the positive verdict presented as the design requires (§5)?

Run `make check` offline. Do not run `make reproduce`, rating, evaluation, build or packet commands
that write artifacts, and do not modify primary artifacts. No network, new research or agents.

Write only `artifacts/review-results/ratings-v2-review-8befd97-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (file, location, replacement), or say there
are none; list advisories separately. A concise review is sufficient. Return the path and outcome.
An AI review is not historical adjudication, feature admission or authorization of any fit.
