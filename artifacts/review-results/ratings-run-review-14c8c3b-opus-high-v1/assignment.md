# Commander residual ratings: separate review of the model code and first run

Review prepared commit `14c8c3bfe3ce4e9c9de36a24b7f937ccb36c998f` against `28072824d7f1801db2a252e5617976d3c67e7eb9`. Sibling inputs.json binds
26 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 14c8c3bfe3ce4e9c9de36a24b7f937ccb36c998f:<path>` first.

Read AGENTS.md, the accepted design `docs/commander-ratings.md` (§§3–8 are the locked plan), the
authorization `data/command/rating-authorization-v1.json`, `generalship/ratings.py`,
`generalship/baseline.py`, `tests/test_ratings.py`, the outputs `artifacts/commander-ratings.json`
and `artifacts/commander-ratings.md`, and the memo `docs/research/commander-ratings-v1.md`. The
two ledgers (`data/estimates/side-strength-v1.json`, `data/command/responsibility-v1.json`) were
reviewed separately; do not re-review their coding.

Check:

1. **Plan fidelity.** Does `ratings.py` implement §§3–7 exactly? Cover the primary rows, the model
   and priors, the fit and Laplace approximation, the rank set and rank intervals, connectivity
   and `not_connected`, the held-out verdict (configuration, the improvement rule under both
   weightings, the effective denominator), the temporal split, every §6 view (including the
   alternative-candidate, superior, successor, command-change, endpoint and both outcome-only
   views, with rule 7 nesting on view (ii)), `view_sensitive` and `unranked_in_view`, the
   raw-residual definition, the gate and the no-signal presentation. Name any divergence with
   the code path and a concrete consequence.
2. **Numerical correctness.** Is the Newton/Cholesky fit correct, including the β handling when
   `use_force=False`? Is the Laplace covariance correct, and are the rank-interval draws correct
   (Cholesky of the sub-covariance, within-side ranking, quantiles)? Recompute the headline
   verdict independently offline, for example by re-running the held-out comparison in memory
   with your own small implementation or by checking the stored predictions. Also confirm that
   `artifacts/commander-ratings.json` reproduces. You may import the package and call functions
   in memory, but do not overwrite artifacts.
3. **Results and wording.** Is every number in the memo and the Markdown report correct? Does
   any sentence overclaim (ranking, skill, significance, robustness) or understate a weakness?
   Is the negative verdict stated as the design requires?

Run `make check` offline. Do not run `make reproduce`, `make commander-ratings`, build or packet
commands, and do not modify primary artifacts. No network, new research or agents.

Write only `artifacts/review-results/ratings-run-review-14c8c3b-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (file, location, replacement), or say there
are none; list advisories separately. A concise review is sufficient. Return the path and outcome.
An AI review is not historical adjudication, feature admission or authorization of any fit.
