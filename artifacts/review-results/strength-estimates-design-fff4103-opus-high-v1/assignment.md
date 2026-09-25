# Best-estimate side strength: separate design review

Review prepared commit `fff4103efea08571af006b4e1c4cc8b171f502e4` against `2778c9a04240b926e4aed41d7cca772111796df3`. Sibling inputs.json binds
19 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. The primary's conversation is not an input. Verify input
hashes against `git show fff4103efea08571af006b4e1c4cc8b171f502e4:<path>` first.

Scope: the proposed design `docs/strength-estimates.md` and the roadmap/README text
recording the owner's 2026-09-25 decision ("I feel like we should make our best estimate
for each"). Read AGENTS.md, README, methodology, evidence contract,
`docs/feature-admission.md`, `docs/feature-admission-reported-strength.md`,
`docs/research/reported-strength-scoping-v1.md` and `generalship/baseline.py` for context.
This is a design review: no estimate, dossier, source or model input is proposed. No
network, new research or agents.

Assess with evidence from the repository:

1. **Faithfulness and scope.** Does the design implement the owner's request while staying
   within AGENTS.md (no invented values, no recollection, missing values visible, no
   automatic commander attribution, distinct from feature admission)? Does it leave the
   admission contract, tier-2 design and frozen inputs untouched?
2. **Target and grades.** Is the target well defined and consistent with the evidence the
   scoping memo describes? Are grades A–D mutually exclusive, fixed before extraction and
   unambiguous enough for consistent review? Is anything left to post-extraction choice?
3. **Estimation rules.** Check §4 for determinism and reproducibility (median, ties,
   hull, widening, caps, opponent-estimate factors, partial completion, rounding). Find
   contradictions or undefined cases (e.g. one-sided bounds as sole input, only partial
   components, conflicting bases, two sides with different grades). Are the fixed constants
   disclosed as conventions and exposed by sensitivity analysis?
4. **Leakage and bias.** Are this-engagement loss adjustments, opponent estimates, source
   availability and compiled-source dependence labelled and carried into evaluation? Any
   route by which the recorded outcome could influence an estimate?
5. **Evaluation plan.** Is it locked (model, folds, nested grade subsets, endpoint and label
   sensitivity, reference comparisons, minimum evaluability)? Would any reported number
   invite a misleading improvement or accuracy claim?
6. **Records and review.** Are the ledger, checker and campaign-batch review sufficient to
   make every estimate reproducible and auditable? What must the checker verify that §7
   omits?

Run `make check` offline; do not run build or packet commands. Write only
`artifacts/review-results/strength-estimates-design-fff4103-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope inspected; give
required corrections as exact replacement text, or say there are none; list advisories
separately. Return the path and outcome. An AI design review is not historical
adjudication or approval of any estimate.
