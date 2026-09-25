# Commander residual ratings: separate design review

Review prepared commit `0de28bd7cdf595b49a8aa80e170650ad82d72a20` against `f5fed2e6e971cc37a0610a38b10ed0bad4e300d6`. Sibling inputs.json binds
22 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 0de28bd7cdf595b49a8aa80e170650ad82d72a20:<path>` first.

Read AGENTS.md, `docs/methodology.md`, `docs/roadmap.md` (Milestones 2–3), the proposed design
`docs/commander-ratings.md`, the accepted strength design `docs/strength-estimates.md`, the
evaluation memo `docs/research/estimate-evaluation-v1.md` and its outputs
`artifacts/estimate-evaluation.json`, and `generalship/baseline.py`. Look at
`data/raw/cwsac_commanders.csv` and a sample of dossier `responsibility` claims in
`data/evidence/*.json` to judge feasibility.

This is a design review; nothing is implemented. The owner delegated the design choices to the
author ("I'm fine with whatever you recommend"), so judge the choices on their merits.

Check:

1. **Consistency with the project's rules.** AGENTS.md and the methodology: no automatic
   attribution to every listed commander, no battle/campaign double counting, the distinction
   between predictive residuals, execution effects and campaign contribution, mediators, no
   invented causal effects, no validation by reputation, visible missingness and coverage.
   Does anything in the design break or blur these?
2. **Attribution rules (§2).** Are the target, rules 1–6 and the grades well defined,
   mechanically checkable and feasible from the registered evidence? Find concrete
   engagements in the cohort where a rule is ambiguous or gives a clearly wrong-looking
   choice, such as several listed commanders, a command change, a superior absent or present,
   naval/joint actions, or wing commanders at an army-level battle. Is "start of interval" the
   right primary anchor?
3. **Model (§4).** Is the hierarchical logistic well specified and identifiable at 37 rows?
   Consider the fixed τ = 0.5 and its justification, sign handling, the Laplace approximation
   and rank intervals, the ≥ 2-battle ranking rule, grade-D sides, and the Union intercept. Is
   anything statistically wrong or misleading? Say what should be fixed in advance that is
   not.
4. **Held-out test (§5).** Is the test fair and pre-specified enough (folds, unseen
   commanders, weighting, the reading if there is no improvement)? Could it be gamed or
   misread?
5. **Sensitivities and outputs (§§6–7).** Is anything required missing? Is anything
   misleading, for example the outcome-only view's labelling or `view_sensitive`?
6. **Limits (§8) and scope.** Are the limits complete and stated honestly, including the
   truncated 1862–63 frame?

Run `make check` offline if useful. Do not run build, packet or evaluation commands. No
network, new research or agents.

Write only `artifacts/review-results/ratings-design-0de28bd-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you
actually inspected. Give required corrections as exact replacement text or precise design
changes, each tied to evidence; list advisories separately. A concise review is sufficient.
Return the path and outcome. An AI review is not historical adjudication, feature admission
or authorization of any fit.
