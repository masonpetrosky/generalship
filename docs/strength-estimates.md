# Best-estimate side strength, design v1 (proposed)

**Status: proposed; revised after a separate design review.** The owner decided on
2026-09-25: "I feel like we should make our best estimate for each." The request followed
the finding that strict admission yields almost no new rows
([scoping memo](research/reported-strength-scoping-v1.md)).

This text applies the required corrections R1–R10 of the separate
[design review](../artifacts/review-results/strength-estimates-design-fff4103-opus-high-v1/review.md)
of `fff4103`, with advisories A1–A7 adopted.

This design adds an **estimate layer**. It sits beside the
[feature-admission contract](feature-admission.md) and the
[tier-2 profile](feature-admission-reported-strength.md) and does not change either. An
estimate is not an admitted observation, and admission gates are not relaxed. Estimates
never overwrite evidence, dossiers or the frozen baseline inputs.

**Interpretation of "each" (A1).** The design reads "each" as each decisive,
non-aggregate engagement, because only those records can be rows for the binary target.
The inconclusive and aggregate records are listed but not estimated. This is the author's
interpretation, recorded as such. Estimates for those records remain possible if the owner
wants them.

## 1. Target and unit

For each decisive, non-aggregate frozen engagement (91 records) and each side, estimate:

> the whole force of that side for this engagement, over the frozen record's interval,
> on one recorded population basis, counted in people.

**Bases.** The admissible bases are the evidence contract's `reported_engaged`,
`reported_effective`, `present_for_duty` and `reported_present`, plus `unknown` for a figure
whose basis is not stated. They are not equivalent, and an estimate of people present never
becomes an estimate of people engaged. Each side records its `point_basis` (§4 rule 3).

**Relation to tier 2.** This is the tier-2 whole-engagement measure (tier-2 §2), and it
carries that design's leakage caveat: within-interval arrivals and commitment can reflect how
the battle went.

**Out of scope.** The 36 inconclusive or aggregate records get no estimate. They stay in
the ledger as out of scope, with that reason.

**Recorded fields.** Each estimate records:

- `point`: the best single value;
- `point_basis`: the basis of the inputs that set the point (§4 rule 3);
- `low` and `high`: a plausible range, not a probability interval;
- `grade`: the evidence quality (§3);
- `method`: the rule applied (§4);
- `labels`: leakage and quality flags (§5);
- `inputs`: every figure used, each with an exact citation;
- a rationale.

## 2. Evidence that may inform an estimate

**Source scope.** Only figures quoted in sources registered in `data/sources.json`, at the
commit that accepts this design, may be used:

- the first-pass dossier citations;
- the pinned Livermore records (scoping memo).

New source research for this layer needs a separate, bounded owner authorization under
AGENTS.md. Until then, an unfilled side stays grade D.

**Classification.** Each input is classified with the tier-2 §3 codes and fields:

- whole-side scope;
- engagement match and state time;
- source role;
- printed value and bounds, including `estimation_status`;
- derivation.

**Exclusions.** Model recollection, reputation and the recorded outcome are never inputs. A
side with no usable candidate value (§3) in any inspected source gets a **null estimate
(grade D)** with a reason. Any one-sided bound found is recorded beside the null. The rule
"do not invent missing strengths" is unchanged.

**Blinding (A5).** Extraction is not blind: the extractor and reviewers are AI systems that
may already know the outcomes, and contract §4 says blinding cannot be claimed as proof. The
§7 inventory is the structural mitigation.

## 3. Grades

The grades are fixed now, before any estimate is made.

**Classification rule.** Each input takes its class from the first matching row below,
using its tier-2 §3 coding and derivation. The labels of every matching row apply (§5). The
class never depends on the figure's value, on the other side or on the outcome.

| Row | Input condition (tier-2 §3 codes) | Class |
| --- | --- | --- |
| 1 | `other_engagement` (including composite entries spanning several frozen records or a campaign), `unreadable_value`, `post_outcome_claim` | Not usable; recorded with its reason |
| 2 | `adversary_or_hearsay_estimate`, including a compiled figure whose cited basis is visibly an opponent's estimate | C, `opponent_or_hearsay` |
| 3 | A value that uses losses, captures, surrenders or survivors of this engagement or of a later one, or a return state-dated after the frozen start date (`post_engagement_state`, with tier-2 §3 item 2's earlier-date exception) | C, `post_start_information` |
| 4 | `scope_unresolved`, `engagement_link_unknown`, `interval_unresolved` or `source_role_unresolved` | C, `applicability_unresolved` |
| 5 | `one_sided_bound`; `partial_scope` or `partial_interval` (a part of the side's force or of the interval), including a sum of components not shown to cover the whole force | Bound only (§4 rule 7); never a candidate value |
| 6 | Two or more of the row 7 conditions | C |
| 7 | Exactly one of: `basis_unknown`; adding or subtracting losses only from engagements that ended before the frozen start date, each loss figure quoted; a completed sum under §4 rule 6; conversion between bases using a ratio quoted for this side in this engagement | B |
| 8 | Tier-2-applicable (that design's §3) with no condition above. `derivation_unknown` and `estimation_status_unknown` are labels here, not exclusions | A |

**Source-printed conversions.** A figure that a source itself prints after a stated
conversion (for example, a stated percentage of a return) is that source's figure. It is
classed on its other attributes.

**Grade D.** Grade D is a side-level status: the side has no input of class A, B or C. Its
point, low and high are null (§4 rule 8).

**Side grade.** A side's grade is the class of the inputs that set its point (§4 rules
3–4). By construction, those inputs share one class.

## 4. Estimation rules, fixed before extraction

All arithmetic uses exact rationals (Python `fractions.Fraction`) on the recorded inputs.
Only rule 9 rounds.

1. **Candidate values.** Each class A, B or C input has one candidate value: its printed
   value, or the midpoint of printed two-sided bounds, after the single adjustment its class
   allows (§3 row 7). Bound-only and unusable inputs have no candidate value.
2. **Dependent inputs count once.** These form one candidate, taken from the member with the
   lowest source ID:
   - inputs from one underlying document (the same `same_document_key`, registry aliases,
     or transcript/facsimile pairs);
   - inputs recorded as a reproduction of another input with the same printed value.

   Other agreement, including NPS/CWSAC with Livermore, is not corroboration and never raises
   a grade (contract §5).
3. **Point.**
   - Take the candidates of the best class present: A, then B, then C.
   - Within class C, drop the `opponent_or_hearsay` candidates if any other candidate exists.
     This is deliberate even when the remaining candidate is `post_start_information`, whose
     row then leaves the fits (§6); see A4.
   - From the remainder, keep the candidates of the first basis present in the order
     `reported_engaged`, `reported_effective`, `present_for_duty`, `reported_present`,
     `unknown`. That basis is `point_basis`. The order is a declared convention.
   - The point is the median of their values. With an even count, it is the lower middle
     value.
   - If only `opponent_or_hearsay` candidates remain, rule 4 applies instead.
4. **Opponent or hearsay only.** Let M be the median of those candidates (the lower middle
   value for an even count), and let min and max be the smallest and largest candidates.
   Then:
   - point = 3/4 × M;
   - low = 1/2 × min;
   - high = max.

   No margin is added. These factors are a declared convention, not an evidence-based
   correction: no inspected source establishes a general bias factor. The §6 sensitivity
   refits expose them.
5. **Range (all other cases).**
   - Take the hull (minimum and maximum) of the candidates that are not
     `opponent_or_hearsay` and whose basis is `point_basis` or `unknown`.
   - `post_start_information` candidates enter the hull only when one of them is used in
     rule 3's median.
   - Let the margin m be 1/20 for grade A, 3/20 for B and 3/10 for C. These are declared
     conventions.
   - Then low = hull minimum × (1 − m) and high = hull maximum × (1 + m).
   - An `opponent_or_hearsay` candidate larger than high becomes high. Such a candidate never
     lowers `low` or sets the point.
   - Candidates on other stated bases are recorded but do not enter the point or the range.
6. **Partial completion.** Our own sum is allowed only under contract §5:
   - the components must be evidenced as disjoint;
   - they must cover the side's whole force for this engagement;
   - they must share one basis and one state time.

   A sum never adds an initial force to later arrivals (tier-2 §3 item 5). Never scale
   formation counts ("two brigades") into people. A sum not shown to cover the whole force
   is a lower bound only (rule 7).
7. **Bounds.** A bound-only input applies only if, apart from being one-sided or partial,
   it would be class A or B, and only if its basis is `point_basis`.
   - A printed upper bound U sets high = U when point ≤ U < high.
   - A lower bound L sets low = L when low < L ≤ point. L may be a printed lower bound, or a
     partial-scope, partial-component or partial-interval figure, because the target counts
     the whole side over the whole interval.
   - An upper bound below the point, or a lower bound above it, is not applied, and the side
     is labelled `bound_conflict`.
   - A bound outside the range on its own side has no effect.
   - Bounds never move the point.
8. **Grade D.** If a side has bounds but no candidate value, or no usable input at all, its
   point, low and high are null. Its reason and any bounds are recorded. There is no
   imputation.
9. **Rounding.** Point, low and high are rounded to the nearest 10, with halves rounded
   upward, after rules 1–8. Rounding is a presentation convention. It does not imply that the
   sources support precision to ten people. §6 uses the stored, rounded values.

The rules are applied by a script from the recorded inputs, so every point and range can be
reproduced. Authored numbers other than quoted inputs and the fixed constants above are not
allowed.

## 5. Labels

| Label | When it applies |
| --- | --- |
| `whole_engagement_leakage` | Always (§1). |
| `post_start_information` | Any candidate used for the point or range is class C under §3 row 3: losses, captures, surrenders or survivors of this or a later engagement, or a post-start return. |
| `opponent_estimate_point` | §4 rule 4 applies. |
| `applicability_unresolved` | A candidate used for the point is class C under §3 row 4. |
| `partial_completed` | A candidate used for the point is a §4 rule 6 sum. |
| `derivation_unknown` | A candidate used for the point or range carries tier-2's `derivation_unknown` label. An undisclosed loss-based reconstruction cannot be ruled out. |
| `estimation_status_unknown` | A candidate used for the point carries that tier-2 label. |
| `bound_conflict` | §4 rule 7. |
| `basis_mixed` | The two sides' `point_basis` values differ, or either is `unknown`. |
| `single_input` | One candidate (after §4 rule 2) determines the side. |
| `compiled_dependence` | A candidate used for the point comes from the NPS/CWSAC or Livermore families (scoping memo, finding 2). The registered Livermore IDs are `livermore-ocr-v1` and `livermore-p{N}-image-v1`; A7. |

The script derives every label mechanically from the recorded codes.

## 6. Use in evaluation

This plan is locked before any fit. **It authorizes no fit.**

**Authorization.** Estimates used as model inputs are an enriched evaluation. The
feature-admission contract does not authorize one (contract §7), and AGENTS.md places
enriched predictors behind a reviewed admission contract. A fit may run only after two
things:

- the ledger's campaign-batch review is reconciled; and
- the owner records an explicit authorization naming the reviewed ledger hash.

That authorization must do one of two things. It may (a) accept this evaluation as an
exploratory estimate-layer diagnostic outside the admission contract. Or it may (b) place
the evaluation under a separately reviewed admission profile. Outputs never enter
`artifacts/baseline.json` and never replace the baseline.

- **Model.** `strength-logistic-v1` is unchanged:
  - ridge 1.0 logistic regression on (US − Confederate)/(US + Confederate), using each
    side's rounded `point`;
  - leave-one-campaign-out over the campaigns present in the row set;
  - equal odds and the Laplace-smoothed, training-only prior as comparators.

  Predictions are named `diagnostic_union_score`, never `p_union_win`.
- **Leakage exclusion.** A row with either side labelled `post_start_information` enters no
  fit. It stays in the ledger and is counted in every report.
- **Nested row sets, all reported:**
  1. both sides grade A;
  2. both sides A or B;
  3. both sides A, B or C.
- **Evaluability.** A row set needs at least 6 rows from 3 campaigns, with both outcome
  classes. A smaller set is reported as not evaluable, with its counts.
- **Sensitivity refits,** each on every evaluable set:
  - `endpoint_refit_*` (A6): four endpoint combinations, with every US side at `low` or at
    `high`, crossed with every Confederate side at `low` or at `high`. These are true refits,
    unlike the baseline's fixed-model endpoint sensitivity.
  - Excluding rows labelled `opponent_estimate_point`, `applicability_unresolved`,
    `derivation_unknown` or `bound_conflict`, one label at a time.
  - A §4 rule 4 point factor of 1 instead of 3/4.
  - The §4 rule 3 basis order `reported_effective`, `present_for_duty`, `reported_present`,
    `reported_engaged`, `unknown`.
  - An upper-middle median for even counts (A3).
- **Reference and comparison.**
  - Retain the frozen 23-engagement, 13-group baseline. Its battle-weighted Brier is
    0.2768816348133779 and its campaign-weighted Brier is 0.2765271817053925, each against
    0.25 for equal odds.
  - **Common rows** have both a frozen baseline row and an estimate row. In each fold, both
    models are fit only on common training rows and scored on the same held-out rows. Common
    rows whose estimate points equal the frozen values are reported as identical by
    construction.
  - **Newly covered rows** are compared only with equal odds and the prior.
  - Results from different row sets, grade subsets or sensitivity variants are never
    compared as improvements. At these row counts, no difference is presented as significant
    or as evidence that the estimates are accurate.
- **Reporting.** Each result gives:
  - battle- and campaign-weighted Brier and log loss;
  - row and campaign counts;
  - the grade mix;
  - every §5 label count;
  - the number of rows excluded as `post_start_information`.

  Every result carries `whole_engagement_leakage` and `conditional_on_source_availability`.
  Which sides have figures, and so which rows and grades exist, may depend on the outcome,
  on size and on fame (tier-2 §2). Predictions are diagnostics, not win probabilities or
  command effects.

## 7. Records and review

- **Ledger.** Estimates live in a versioned, immutable ledger
  (`data/estimates/side-strength-v1.json`). It binds the hashes of this design, the source
  registry snapshot, every cited dossier revision and the estimation script. Each input
  carries:
  - its source ID;
  - its section, or its row key and column;
  - its locator and exact quote;
  - its tier-2 §3 codes;
  - its same-document key;
  - its class, basis and value.
- **Inventory.** For each of the 91 engagements and each side, the ledger lists every
  strength figure from three places, whether used or not, with its class or its reason for
  non-use:
  - the bound dossier's `strength` claims and typed quantities;
  - the frozen CWSAC forces row;
  - the matching Livermore entry, if any.

  The other 36 records are listed as out of scope, with their reason.
- **Checker.** An offline, standard-library checker verifies:
  - coverage: exactly the 91 in-scope records × 2 sides, plus the 36 out-of-scope records,
    against the frozen cohort;
  - bindings: registry, raw-file and dossier hashes, and that no input cites a source
    outside the bound snapshot;
  - passages: each quote occurs in its section or CSV cell, and each input's printed value
    occurs in its quote;
  - inventory: every `strength` claim and typed quantity in the bound dossiers, and every
    frozen CWSAC force figure, is referenced by an input or recorded with a reason;
  - consistency: codes come from the tier-2 list, and each class, grade and label follows
    mechanically from its codes under §§3 and 5;
  - reproduction: every candidate, point, range, `point_basis`, label and nested-set
    membership reproduces under §§4–6 with the recorded constants. Grade D sides have null
    values and a reason. For every non-null side, 0 < low ≤ point ≤ high.

  The checker cannot verify that a code, basis or quote supports its classification. That is
  the review's task.
- **Separate review.** A separate Opus review checks the ledger in campaign batches. It
  covers classification, adjustment evidence, grade and the completeness of the inventory.
  Findings are reconciled as for dossiers.
- **What review establishes.** A reviewed ledger is a reviewed *estimate*, not historical
  adjudication or an admitted feature. The dossiers, the tier-2 ledger and the frozen inputs
  stay as they are.

## 8. Non-goals

- No commander ratings from this step.
- No imputation for grade D.
- No borrowing of strengths across engagements or from reputation.
- No outcome-dependent rule choice.
- No change to the admission contract.
