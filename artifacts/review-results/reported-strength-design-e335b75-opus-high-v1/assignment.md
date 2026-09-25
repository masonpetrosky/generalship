# Reported side-strength profile: separate design review

Review prepared commit `e335b751e354bd2581eec5770b0fba7e200f6c0e` against `ff494b976d0d2dd124ad2c6b50304e016f3002f1`. Sibling inputs.json binds
19 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, the evidence
contract, the reviewed feature-admission contract (`docs/feature-admission.md`), the
validator description (`docs/admission-validator.md`) and the implementation
(`generalship/admission.py`, `generalship/baseline.py`). The primary's conversation is not
an input.

Verify input hashes against `git show e335b751e354bd2581eec5770b0fba7e200f6c0e:<path>` before reviewing.

Scope: the proposed design `docs/feature-admission-reported-strength.md`
(`reported_side_strength_v1`) and the roadmap/README text that records the owner's
2026-09-25 decision to add it. This is a design review. No evidence, candidate, dossier,
source record or model input is changed or proposed for admission. No network, new
research, extra sources or agents.

Assess, with evidence from the repository:

1. **Relationship to the reviewed contract.** Does the design leave
   `opening_available_combatants_v1` and contract design v1 intact, or does any clause relax,
   contradict or silently reinterpret them? Where it reuses §§3–6, is that reuse coherent?
2. **Measure definition and leakage.** Is the population, interval and basis definition
   precise enough for consistent evidence-use review? Is the outcome-leakage weakness of
   whole-engagement/engaged totals stated accurately and carried into every place results
   could appear? Are there leakage routes it misses (e.g. casualty-derived "effectives",
   post-battle returns, reinforcements, selection of which engagements get figures)?
3. **Applicability gates.** Whole-side scope, engagement match, source role (including the
   exclusion of adversary/hearsay estimates and the bias of own-side reports), printed
   value/bounds and derivation. Are statuses (`excluded` vs `blocked`) assigned consistently
   with contract §6? Anything ambiguous enough to invite outcome- or reputation-driven choice?
4. **Rows, basis pairing and scenarios.** Are the `compiled_first`/`reports_first` orderings
   and the `mixed_basis` scenario consistent with contract §5 (one observation per
   engagement, every applicable alternative in some scenario, no weights or score-based
   selection)? Is the rule truly fixed before extraction? Any combinatorial or
   denominator problem?
5. **Evaluation plan.** Is it locked tightly enough (model, folds, comparators, common rows
   vs expanded coverage, per-scenario reporting, the retained 23-row reference)? Would any
   reported number invite a misleading improvement claim?
6. **Counts and facts.** Independently verify from `artifacts/battles.json` and the frozen
   CSVs: 127 engagements; 91 decisive non-aggregate; 23 with both numeric strengths; 5 with
   one side; 63 with none; 36 inconclusive or aggregate. Verify 113 dossiers carry an
   `opening-personnel-unknown` claim with status `unknown`, and that the roadmap/README
   statements match the design.
7. **Implementability.** Are the §8 notes (validator extension, `source_role`, basis handling,
   schema v3 quantities, new snapshot) sufficient and consistent with `admission.py`'s
   current object model? Name anything that would force a later contract change.
8. **Research authorization (§7).** Is the bounded follow-up consistent with AGENTS.md's
   stopping rule and three-family ceiling? Is the expected-yield statement honest?

Run `make check` offline. Do not run build/packet commands and do not import or call
`generalship.cli` functions that write files. Do not modify primary artifacts.

Write only `artifacts/review-results/reported-strength-design-e335b75-opus-high-v1/review.md`. Do not edit other files, commit or push. State the scope you
actually inspected. Give required corrections as exact, evidence-backed replacement text
for the design (or say there are none), then advisories separately. A concise review is
sufficient. Return the path and outcome. An AI design review is not historical
adjudication, feature admission or approval of any candidate.
