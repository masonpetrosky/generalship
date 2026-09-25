# Best-estimate side strength, design v1 (proposed)

**Status: proposed; awaiting separate review.** The owner decided on 2026-09-25: "I feel
like we should make our best estimate for each." The request followed the finding that
strict admission yields almost no new rows
([scoping memo](research/reported-strength-scoping-v1.md)).

This design adds an **estimate layer**. It sits beside the
[feature-admission contract](feature-admission.md) and the
[tier-2 profile](feature-admission-reported-strength.md) and does not change either. An
estimate is not an admitted observation, and admission gates are not relaxed. Estimates
never overwrite evidence, dossiers or the frozen baseline inputs.

## 1. Target and unit

For each decisive, non-aggregate frozen engagement (91 records) and each side, estimate:

> the number of people in that side's force present for and taking part in the
> engagement over the frozen interval, all arms, including officers.

This is the whole-engagement measure the sources mostly offer. It includes the tier-2
leakage caveat: within-interval arrivals and commitment can reflect how the battle went.
The 36 inconclusive or aggregate records get no estimate.

Each estimate records:

- `point`: the best single value;
- `low` and `high`: a plausible range, not a probability interval;
- `grade`: the evidence quality (§3);
- `method`: the rule applied (§4);
- `labels`: leakage and quality flags (§5);
- `inputs`: every figure used, each with an exact citation;
- a rationale.

## 2. Evidence that may inform an estimate

Only figures quoted in inspected, registered sources may be used. Each input is classified
with the tier-2 §3 codes:

- role;
- basis;
- scope;
- engagement match and state time;
- derivation.

Model recollection, reputation and the recorded outcome are never inputs. Where a side
has no quantitative figure in any inspected source, its estimate is **null (grade D)**
with a reason. The rule "do not invent missing strengths" is unchanged.

## 3. Grades

The grades are fixed now, before any estimate is made.

| Grade | Meaning |
| --- | --- |
| **A** | At least one tier-2-applicable figure: whole side, this engagement, own report or compiled total, not loss-derived, with a stated basis. |
| **B** | A whole-side figure that needs one documented adjustment, where each part of the adjustment is itself quoted. Examples: completing a partial figure with components the sources state; converting a stated basis with a stated ratio; a compiled total that subtracts losses from an **earlier** engagement; one-sided bounds ("did not exceed"); unstated basis. |
| **C** | Indirect evidence only. Examples: a compiled or own figure that adds or subtracts **this** engagement's losses; an opponent's or hearsay estimate; bounds formed from partial components. |
| **D** | No quantitative evidence for the side. The estimate is null. |

A side's grade is the best grade among the inputs that determine its point.

## 4. Estimation rules, fixed before extraction

1. **Candidate values.** For each input, take its printed value, or the midpoint of printed
   bounds. Apply only documented adjustments, and only those allowed for its grade.
2. **Point.** Use the highest-grade inputs only:
   - the median of their candidate values;
   - with an even count, the lower middle value.

   Opponent and hearsay estimates never set the point when an own-side or compiled input
   exists.
3. **Range.** Start from the hull (minimum to maximum) of all candidate values of every
   grade. Widen it by a fixed margin set by the point's grade: A ±5%, B ±15%, C ±30%.
   Then apply bounds:
   - a one-sided figure caps the range where its direction allows;
   - an opponent's estimate may raise `high`, never `point`.
4. **Grade-C point with only opponent or hearsay inputs:** point = 0.75 × the median
   estimate, low = 0.5 ×, high = 1.0 ×. These fixed factors encode the known tendency to
   overestimate an enemy. They are a declared convention, not a finding, and the §6
   sensitivity analysis exposes them.
5. **Partial completion (grade B).** Add only components that the sources state for the
   same engagement and side. Never scale formation counts ("two brigades") into people
   without a quoted per-formation strength for that force.
6. **Rounding.** Points and bounds are rounded to the nearest 10. The rounding records no
   precision the sources lack.

The rules are applied by a script from the recorded inputs, so every point and range can
be reproduced. Authored numbers other than quoted inputs and the fixed constants above are
not allowed.

## 5. Labels

| Label | When it applies |
| --- | --- |
| `whole_engagement_leakage` | Always (§1). |
| `this_engagement_losses` | A this-engagement loss adjustment determines the point. |
| `opponent_estimate_point` | §4 rule 4 applies. |
| `partial_completed` | Rule 5 applies. |
| `basis_mixed` | The two sides' points rest on different bases. |
| `single_input` | One input determines the side. |
| `compiled_dependence` | The point rests on NPS/CWSAC or Livermore values that are likely dependent (scoping memo). |

## 6. Use in evaluation

This is locked before any fit, and the fit itself needs the owner's go-ahead after the
estimate ledger is reviewed.

- **Model.** The same `strength-logistic-v1` specification as the baseline:
  - relative strength from `point`;
  - leave-one-campaign-out;
  - equal-odds and training-prior comparators;
  - output named `diagnostic_union_score`.
- **Nested row sets, all reported:**
  1. both sides grade A;
  2. both sides A or B;
  3. both sides A, B or C.
- **Sensitivity.**
  - Refit with each side at `low` and at `high` (four endpoint combinations).
  - Refit excluding rows labelled `this_engagement_losses` or `opponent_estimate_point`.
- **Reference.** Report the frozen 23-row baseline alongside, on its own rows and on the
  common rows. Never claim improvement across different populations.
- **Reporting.** Each result reports row and campaign counts, the grade mix and label
  counts. Predictions are diagnostics, not win probabilities or command effects.

## 7. Records and review

- **Ledger.** Estimates live in a versioned ledger (`data/estimates/side-strength-v1.json`).
  Every input carries its source ID, section or row key, locator and exact quote.
- **Checker.** An offline checker verifies:
  - quotes against the registry;
  - classifications and grades against §3;
  - that every point and range reproduces from the inputs by §4.
- **Separate review.** A separate Opus review checks the ledger in campaign batches:
  classification, adjustment evidence and grade. Findings are reconciled as for dossiers.
- **What review establishes.** A reviewed ledger is a reviewed *estimate*, not historical
  adjudication or an admitted feature. The dossiers, the tier-2 ledger and the frozen
  inputs stay as they are.

## 8. Non-goals

- No commander ratings from this step.
- No imputation for grade D.
- No borrowing of strengths across engagements or from reputation.
- No outcome-dependent rule choice.
- No change to the admission contract.
