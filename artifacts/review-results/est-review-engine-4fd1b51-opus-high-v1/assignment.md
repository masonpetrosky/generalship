# Best-estimate ledger: separate review of the engine and ledger bindings

Review prepared commit `4fd1b512f9e4db0402537bfe577031a6cc6939f6` against `5151b5700f50fc494b167cc7c4d742c8fc17cc13`. Sibling inputs.json binds
25 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 4fd1b512f9e4db0402537bfe577031a6cc6939f6:<path>` first. Other review bundles may be committed after the prepared
commit; they are out of scope.

Read AGENTS.md, the accepted design `docs/strength-estimates.md` (its §§3–5 are the rules), the
tier-2 design `docs/feature-admission-reported-strength.md` (its §3 codes), the scoping memo
`docs/research/reported-strength-scoping-v1.md`, the ledger memo
`docs/research/strength-estimates-ledger-v1.md`, the ledger `data/estimates/side-strength-v1.json`
(including its `extractor_policies`) and `generalship/estimates.py`.

Scope: `generalship/estimates.py`, `tests/test_estimates.py`, the `estimate-check` and build
wiring in `generalship/cli.py`, and the ledger's top-level structure (bindings, constants,
policies, out-of-scope list, inventory shape). The four batch reviews cover per-engagement
coding; do not repeat them beyond spot checks.

Check:

1. **Rules.** Does the code implement design §3 (row order, `loss_timing`, adjustments), §4
   rules 1–9 (candidate values, dependence groups, point, opponent-only rule, range, sums,
   bounds, grade D, rounding and floor) and §5 labels exactly? Name any divergence with a
   concrete input that exposes it. Work through at least: a group whose members disagree in
   basis; a bound on the point basis whose residual class is C; an opponent candidate on a
   different stated basis; two opponent candidates of different bases; and a completed sum.
2. **Checker.** Does `check` enforce design §7 (coverage, bindings, passages, printed values,
   inventory, consistency, reproduction, range order, nested sets)? What does it not enforce?
3. **Two implementation choices** recorded in the ledger memo: binding cited-source hashes
   instead of the whole registry, and not linking NPS narrative restatements as
   reproductions. Are they consistent with the design, and do they create any loophole?
4. **Build wiring.** The build reports a stale ledger instead of failing, while the unit test
   and `estimate-check` enforce replay. Is that sound?
5. **Ledger-level facts.** Verify the memo's counts (grades, row sets, common and new rows,
   exclusions) from the ledger.

Run `make check` and `python3 -m generalship estimate-check` offline. Do not run build or
packet commands and do not modify primary artifacts. No network, new research or agents.

Write only `artifacts/review-results/est-review-engine-4fd1b51-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you
actually inspected (which engagements, inputs and passages). Give required corrections as exact,
evidence-backed changes to specific ledger inputs (engagement, side, input ID, field, new value),
or say there are none; list advisories separately. A concise review is sufficient. Return the
path and outcome. An AI review is not historical adjudication, feature admission or
authorization of any fit.
