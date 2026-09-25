# Separate design review: best-estimate side strength (`fff4103`)

## Reviewer record

| Field | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, a separate reviewer subagent started with fresh context. The primary's conversation was not an input. |
| Task identity | Assignment `artifacts/review-results/strength-estimates-design-fff4103-opus-high-v1/assignment.md`. The runtime did not give the reviewer a task ID. |
| Date | 2026-09-25 |
| Prepared commit reviewed | `fff4103efea08571af006b4e1c4cc8b171f502e4` |
| Previous commit | `2778c9a04240b926e4aed41d7cca772111796df3` |
| Bundle commit (worktree HEAD) | `cff43ea92a82493987df3a37657ae296e6b5f0c9`. It differs from `fff4103` only by adding `assignment.md` and `inputs.json`. |
| Assignment SHA-256 | `a650c78e5fd1cde7e8fe47fe18a9f9bfa871fcf597bf0a5695e9fcfa71e95d0b` (verified) |
| Input manifest (`inputs.json`) SHA-256 | `80a1d49a3b2abc6cc81bd2405b7d6780dcd54b6f29bd6de038a559ed05594fb2` (verified) |
| Outcome | **Corrections required**: R1–R10. Advisories: A1–A7. |

This is an AI design review, a separate analysis. It is not human historical adjudication and does not approve any estimate, source, classification or feature. It does not establish that any sources are independent. No estimate, dossier, source or model input was proposed or examined.

## Input verification

I hashed every one of the 19 paths in `inputs.json` from `git show fff4103…:<path>`. **All 19 match.** Their worktree bytes are identical to the prepared-commit bytes. `git diff --stat 2778c9a fff4103` shows changes to exactly three files: `README.md` (+2/−1), `docs/roadmap.md` (+5/−2) and the new `docs/strength-estimates.md` (146 lines). So the admission contract, the tier-2 design, the scoping memo, the validator code, the frozen raw inputs and `artifacts/baseline.json` are byte-unchanged by the prepared commit.

**`make check`** ran offline and exited 0:

- 95 unit tests passed.
- `generalship check` reported 127 pilot battles and 23 eligible battles in 13 campaigns.
- Battle-weighted Brier was 0.2768816348133779 (equal odds 0.25). There are 0 promoted admission rows, and candidate statuses were `blocked` 18 and `excluded` 22.
- It wrote no artifacts.

I ran no build, reproduce or packet commands. There was no network access, no new research and no agents. The check did not modify the worktree (`git status` is clean).

## Scope inspected

- **Read in full:**
  - `docs/strength-estimates.md`
  - `docs/feature-admission.md`
  - `docs/feature-admission-reported-strength.md`
  - `docs/research/reported-strength-scoping-v1.md`
  - `docs/methodology.md`
  - `docs/evidence-contract.md`
  - `generalship/baseline.py`
  - `AGENTS.md`
  - the README and roadmap diffs
- **Read in part:**
  - `docs/roadmap.md`, lines 1–80 and 385–420 (the current-priority header and the **Next priority** paragraph);
  - `README.md`, the lines around the changed priority text (grep, lines 76–80).
- **Checked mechanically:**
  - `artifacts/battles.json`: 127 records. 92 are decisive. VA024 is the only aggregate operation, so 91 are decisive and non-aggregate. 35 are inconclusive, and 35 + 1 = 36 have no estimate. This confirms the design's 91/36 counts.
  - `artifacts/baseline.json`: 23 battles, 13 campaigns. Campaign-weighted Brier is 0.2765271817053925 against 0.25.
  - `data/sources.json`: grep only. It has 608 entries, including `ia-livermore-metadata-v1` and `livermore-ocr-v1`.
- **Verified by hash only, not read:**
  - `README.md` beyond the lines above
  - `docs/sources.md`
  - `artifacts/admission-check.json`
  - `data/admission/*.json`
  - `data/pilot/cohort.json`
  - the three raw CSVs
  - `generalship/cli.py`
  - `tests/test_evidence.py`
- **Not inspected:** dossiers, Livermore page images and any historical source passage. This is a design review, so I checked no historical claim, quote or figure against a source. I checked only the scoping memo's figures as the memo states them, not the pages behind them.

## Summary assessment

The design responds to the owner's request with a separate, graded estimate layer. Its framing is sound:

- it states that estimates are not admitted observations;
- it leaves the admission contract, the tier-2 design and the frozen inputs untouched (verified by diff);
- grade D stays null;
- there is no commander attribution (§8);
- it keeps `diagnostic_union_score` naming;
- it bans authored numbers beyond quoted inputs and constants;
- it requires a script to reproduce every value.

As written, however, the design cannot yet be applied deterministically or consistently before extraction:

1. The target merges population bases that the evidence contract requires to be kept apart.
2. The grade table is not exhaustive and has no precedence rule, so many inputs the scoping memo already describes could only be graded by post-extraction judgement.
3. The §4 rules contradict each other, or leave cases undefined, for one-sided bounds, opponent estimates, widening, caps and partial components.
4. Dependent compiled copies count as votes in the median.
5. Inputs that use this engagement's losses (and later ones), survivors or post-start returns enter the primary evaluation set.
6. The fit uses new evidence as model input without the authorization route that AGENTS.md and the admission contract require.
7. The evaluation plan omits evaluability, the paired common-row protocol and a source-availability label.
8. The checker cannot detect selective recording of inputs.

Each of these gaps has an exact replacement below.

## Required corrections

### R1: The target conflates population bases (§1, §4 rule 2)

**Evidence.**

- §1 defines the target as people "present for and taking part in the engagement". That merges presence with engagement.
- §3 grade A accepts any tier-2-applicable basis without adjustment. The tier-2 design (§2) retains `reported_engaged`, `reported_effective`, `reported_present` and `present_for_duty` "exactly".
- §4 rule 2 takes a median across all highest-grade inputs, whatever their basis.
- For Fredericksburg US, the scoping memo gives present for duty 120,281, engaged 113,987 and effectives 106,007. All three would be grade A, and their median would mix bases.
- The evidence contract (*Dossiers and claims*) says: "an estimate of people present must not become an estimate of people engaged." Contract §5 requires preserving basis.
- §3 B's "converting a stated basis" has no defined target basis.
- `basis_mixed` (§5) checks only whether the two sides' bases differ, not mixing within one side.

**Correction.** Replace the text from "For each decisive, non-aggregate frozen engagement" through "The 36 inconclusive or aggregate records get no estimate." (§1, lines 16–23) with:

> For each decisive, non-aggregate frozen engagement (91 records) and each side, estimate:
>
> > the whole force of that side for this engagement, over the frozen record's interval,
> > on one recorded population basis, counted in people.
>
> The admissible bases are the evidence contract's `reported_engaged`, `reported_effective`,
> `present_for_duty` and `reported_present`, plus `unknown` for a figure whose basis is not
> stated. They are not equivalent, and an estimate of people present never becomes an
> estimate of people engaged. Each side records its `point_basis` (§4 rule 3). This is the
> tier-2 whole-engagement measure (tier-2 §2), and it carries that design's leakage caveat:
> within-interval arrivals and commitment can reflect how the battle went. The 36 inconclusive
> or aggregate records get no estimate. They stay in the ledger as out of scope, with that reason.

In the §1 list of recorded fields, insert after the `point` bullet:

> - `point_basis`: the basis of the inputs that set the point (§4 rule 3);

Rule 3 in R3's replacement §4 implements the fixed basis order.

### R2: The grade table is not exhaustive and has no precedence (§3)

**Evidence.** The table lists grade "Examples", so it is not exhaustive. It has no rule for an input that meets conditions from more than one grade. Several input types that the scoping memo already records have no grade:

- composite entries covering several records (VA021, VA026: `other_engagement`). §8 forbids "borrowing ... across engagements", but §3 does not say these inputs are unusable.
- post-engagement returns (Chattanooga CS, December 10; Chickasaw Bayou CS, Jan 2–3 returns);
- later-engagement losses added to a later return (Gaines' Mill CS, "adding losses June 28–July 1");
- the unresolved codes `scope_unresolved`, `engagement_link_unknown`, `interval_unresolved` and `source_role_unresolved`;
- `partial_interval`;
- figures that need two B-type adjustments. B says "one documented adjustment".

Other problems:

- One-sided bounds are listed as grade B, although tier-2 blocks them as having "no finite pair of bounds" (tier-2 §6). §4 rule 1 gives them no candidate value, which contradicts that B grading (see R3).
- "Bounds formed from partial components" (C) give only a lower bound. No quoted upper end exists, so a point from them would be an invented value.
- The assignment requires grades that are "fixed before extraction" and leave no post-extraction choice. That is not met.

**Correction.** Replace everything from "The grades are fixed now" through "A side's grade is the best grade among the inputs that determine its point." (§3, lines 52–61) with:

> The grades are fixed now, before any estimate is made. Each input takes its class from the
> first matching row below, using its tier-2 §3 coding and derivation; the labels of every
> matching row apply (§5). The class never depends on the figure's value, on the other side
> or on the outcome.
>
> | Row | Input condition (tier-2 §3 codes) | Class |
> | --- | --- | --- |
> | 1 | `other_engagement` (including composite entries spanning several frozen records or a campaign), `unreadable_value`, `post_outcome_claim` | Not usable; recorded with its reason |
> | 2 | `adversary_or_hearsay_estimate`, including a compiled figure whose cited basis is visibly an opponent's estimate | C, `opponent_or_hearsay` |
> | 3 | A value that uses losses, captures, surrenders or survivors of this engagement or of a later one, or a return state-dated after the frozen start date (`post_engagement_state`, with tier-2 §3 item 2's earlier-date exception) | C, `post_start_information` |
> | 4 | `scope_unresolved`, `engagement_link_unknown`, `interval_unresolved` or `source_role_unresolved` | C, `applicability_unresolved` |
> | 5 | `one_sided_bound`; `partial_scope` or `partial_interval` (a part of the side's force or of the interval), including a sum of components not shown to cover the whole force | Bound only (§4 rule 7); never a candidate value |
> | 6 | Two or more of the row 7 conditions | C |
> | 7 | Exactly one of: `basis_unknown`; adding or subtracting losses only from engagements that ended before the frozen start date, each loss figure quoted; a completed sum under §4 rule 6; conversion between bases using a ratio quoted for this side in this engagement | B |
> | 8 | Tier-2-applicable (that design's §3) with no condition above. `derivation_unknown` and `estimation_status_unknown` are labels here, not exclusions | A |
>
> A figure that a source itself prints after a stated conversion (for example, a stated
> percentage of a return) is that source's figure and is classed on its other attributes.
> **Grade D** is a side-level status: the side has no input of class A, B or C. Its point, low
> and high are null (§4 rule 8). A side's grade is the class of the inputs that set its point
> (§4 rules 3–4); by construction, they share one class.

### R3: The §4 rules contradict each other or leave cases undefined (§4)

**Evidence.**

- **One-sided bounds.** Rule 1 ("the midpoint of printed bounds") cannot give a candidate value for a one-sided bound. §3 grades such bounds B, and rule 3 uses them only as caps. The case the assignment names, a one-sided bound as a side's only input, has no defined point.
- **Opponent estimates.** Rule 3's hull covers "all candidate values of every grade". Opponent estimates can therefore lower `low`, and "may raise `high`" is redundant. Rule 4 separately fixes low and high at 0.5× and 1.0× the median. With two or more opponent estimates, rule 4's high falls below the hull maximum. Nothing states which rule prevails.
- **Widening.** "Widen ... ±5%" does not say what the percentage applies to (the hull ends or the point).
- **Caps.** A cap that falls on the wrong side of the point is undefined, and so is a cap that crosses `low`.
- **Partial-component bounds.** "Bounds formed from partial components" (C) have no finite upper bound, so there is no midpoint.
- **Rounding.** The tie rule and the arithmetic type are unstated. Different floating-point or rounding conventions can give different reproductions.
- **Rounding wording.** "The rounding records no precision the sources lack" is inaccurate. For example, 0.75 × 21,000 = 15,750 is more precise than an "about 21,000" source supports.

**Correction.** Replace §4 (lines 63–90, from "## 4. Estimation rules, fixed before extraction" through "not allowed.") with:

> ## 4. Estimation rules, fixed before extraction
>
> All arithmetic uses exact rationals (Python `fractions.Fraction`) on the recorded inputs.
> Only rule 9 rounds.
>
> 1. **Candidate values.** Each class A, B or C input has one candidate value: its printed
>    value, or the midpoint of printed two-sided bounds, after the single adjustment its class
>    allows (§3 row 7). Bound-only and unusable inputs have no candidate value.
> 2. **Dependent inputs count once.** Inputs from one underlying document (the same
>    `same_document_key`, registry aliases, transcript/facsimile pairs), or inputs recorded as a
>    reproduction of another input with the same printed value, form one candidate: the member
>    with the lowest source ID. Other agreement, including NPS/CWSAC with Livermore, is not
>    corroboration and never raises a grade (contract §5).
> 3. **Point.** Take the candidates of the best class present (A, then B, then C). Within class
>    C, drop the `opponent_or_hearsay` candidates if any other candidate exists. From the
>    remainder, keep the candidates of the first basis present in the order
>    `reported_engaged`, `reported_effective`, `present_for_duty`, `reported_present`,
>    `unknown`. That basis is `point_basis`; the order is a declared convention. The point is
>    the median of their values. With an even count, it is the lower middle value. If only
>    `opponent_or_hearsay` candidates remain, rule 4 applies instead.
> 4. **Opponent or hearsay only.** Let M be the median of those candidates (the lower middle
>    value for an even count), and let min and max be the smallest and largest candidates. Then
>    point = 3/4 × M, low = 1/2 × min and high = max. No margin is added. These factors are a
>    declared convention, not an evidence-based correction: no inspected source establishes a
>    general bias factor. The §6 sensitivity refits expose them.
> 5. **Range (all other cases).** Take the hull (minimum and maximum) of the candidates that
>    are not `opponent_or_hearsay` and whose basis is `point_basis` or `unknown`.
>    `post_start_information` candidates enter the hull only when one of them is used in rule
>    3's median. Let the margin m be 1/20 for grade A, 3/20 for B and 3/10 for C (declared
>    conventions). Then low = hull minimum × (1 − m) and high = hull maximum × (1 + m). An
>    `opponent_or_hearsay` candidate larger than high becomes high. Such a candidate never
>    lowers `low` or sets the point. Candidates on other stated bases are recorded but do not
>    enter the point or the range.
> 6. **Partial completion.** Our own sum is allowed only under contract §5. The components must
>    be evidenced as disjoint, must cover the side's whole force for this engagement, and must
>    share one basis and one state time. A sum never adds an initial force to later arrivals
>    (tier-2 §3 item 5). Never scale formation counts ("two brigades") into people. A sum not
>    shown to cover the whole force is a lower bound only (rule 7).
> 7. **Bounds.** A bound-only input applies only if, apart from being one-sided or partial,
>    it would be class A or B, and only if its basis is `point_basis`.
>    - A printed upper bound U sets high = U when point ≤ U < high.
>    - A lower bound L sets low = L when low < L ≤ point. L may be a printed lower bound, or a
>      partial-scope, partial-component or partial-interval figure, because the target counts
>      the whole side over the whole interval.
>    - An upper bound below the point, or a lower bound above it, is not applied, and the
>      side is labelled `bound_conflict`.
>    - A bound outside the range on its own side has no effect.
>    - Bounds never move the point.
> 8. **Grade D.** If a side has bounds but no candidate value, or no usable input at all, its
>    point, low and high are null. Its reason and any bounds are recorded. There is no
>    imputation.
> 9. **Rounding.** Point, low and high are rounded to the nearest 10, with halves rounded
>    upward, after rules 1–8. Rounding is a presentation convention. It does not imply that
>    the sources support precision to ten people. §6 uses the stored, rounded values.
>
> The rules are applied by a script from the recorded inputs, so every point and range can
> be reproduced. Authored numbers other than quoted inputs and the fixed constants above are
> not allowed.

Rounding halves upward is monotone, so low ≤ point ≤ high survives rounding. Rule 4 always gives 1/2·min ≤ 3/4·M ≤ max.

### R4: Partial completion lacks the overlap, basis and time conditions (§4 rule 5)

**Evidence.**

- The current rule 5 requires only components "that the sources state for the same engagement and side".
- Contract §5 requires evidence that the components are disjoint, cover the target and share the time and population. It says "unknown overlap blocks the transform". Tier-2 §3 item 5 forbids "our own sum of an initial force and a force that arrived later".
- AGENTS.md forbids double counting.

**Correction.** Rule 6 of the R3 replacement text resolves this.

### R5: Dependent copies count as votes in the median (§4 rule 2)

**Evidence.**

- The scoping memo (finding 2) shows five frozen CWSAC figures identical to Livermore's. It concludes that the families "are therefore not independent".
- A median over "the highest-grade inputs" counts such a figure twice. Contract §5 says: "Do not count citations as votes." Tier-2 §4 treats aliases and transcript/facsimile pairs as one document.

**Correction.** Rule 2 of the R3 replacement text resolves this.

### R6: The 0.75 factor rests on uncited historical generalization (§4 rule 4)

**Evidence.**

- The sentence "These fixed factors encode the known tendency to overestimate an enemy" is a general historical claim.
- No inspected repository source supports it. The tier-2 design records only that own-side reports "carry a known bias", recorded and never corrected.
- AGENTS.md says: "Never substitute model recollection for a source."

**Correction.** Rule 4 of the R3 replacement text resolves this by stating that no inspected source establishes a bias factor. §6 exposes the factor (see R8).

### R7: Leakage labels are incomplete, and post-start information enters the primary evaluation set (§5, §6)

**Evidence.**

- **Label scope.** `this_engagement_losses` applies only when such an input "determines the point". Under rule 3's hull, the same input still moves `low` and `high`, and so the endpoint refits.
- **Later losses and survivors.** The label does not cover later-engagement losses or post-start returns (survivors). Examples in the memo are Gaines' Mill CS, Chickasaw Bayou CS, Chattanooga CS and Arkansas Post ("93% of those surrendered plus the loss").
- **Nested set 3.** Set 3 includes these rows as a primary reported set. The methodology says: "Post-battle casualties, survivors, narrative outcome language ... are not predictors." Contract §4 requires transitive dependency checks.
- **Missing labels.** The tier-2 labels `derivation_unknown` and `estimation_status_unknown` are absent. Tier-2 §2 notes that for `derivation_unknown` "an undisclosed loss-based reconstruction cannot be ruled out". The scoping memo found three of the five compared frozen figures were loss-derived.
- **Source availability.** There is no `conditional_on_source_availability` statement. Grade membership itself depends on which sides have figures, which tier-2 §2 says "may itself depend on the outcome, on size and on fame".

**Correction.** Replace the §5 table (lines 94–102) with:

> | Label | When it applies |
> | --- | --- |
> | `whole_engagement_leakage` | Always (§1). |
> | `post_start_information` | Any candidate used for the point or range is class C under §3 row 3: losses, captures, surrenders or survivors of this or a later engagement, or a post-start return. |
> | `opponent_estimate_point` | §4 rule 4 applies. |
> | `applicability_unresolved` | A candidate used for the point is class C under §3 row 4. |
> | `partial_completed` | A candidate used for the point is a §4 rule 6 sum. |
> | `derivation_unknown` | A candidate used for the point or range carries tier-2's `derivation_unknown` label. An undisclosed loss-based reconstruction cannot be ruled out. |
> | `estimation_status_unknown` | A candidate used for the point carries that tier-2 label. |
> | `bound_conflict` | §4 rule 7. |
> | `basis_mixed` | The two sides' `point_basis` values differ, or either is `unknown`. |
> | `single_input` | One candidate (after §4 rule 2) determines the side. |
> | `compiled_dependence` | A candidate used for the point comes from the NPS/CWSAC or Livermore families (scoping memo, finding 2). |
>
> The script derives every label mechanically from the recorded codes.

Excluding these rows from fits, and adding the result label, is part of R8's replacement §6.

### R8: The fit lacks its authorization route, and the evaluation plan is incomplete (§6)

**Evidence.**

- **Authorization.** §6 plans a `strength-logistic-v1` fit on estimate points, gated only by "the owner's go-ahead after the estimate ledger is reviewed". But:
  - AGENTS.md says: "Implement a reviewed feature-admission contract before adding enriched predictors."
  - Evidence contract step 6 requires "a separately reviewed feature-admission mapping ... before using any new evidence in a model".
  - Contract §7 says: "No enriched evaluation is authorized by this design."

  The design says it "does not change" the contract. It therefore needs an explicit, recorded owner decision that places this evaluation outside the contract as an exploratory diagnostic, or a reviewed profile. A generic "go-ahead" is not enough.
- **Evaluability.** The plan has no minimum. Contrast tier-2 §6 ("at least 6 rows from 3 campaigns, with both outcome classes") and `baseline.evaluate`, which raises below that minimum.
- **Common rows.** The plan has no paired common-row protocol. It says only "on the common rows". Contract §7 and tier-2 §6 require both models to be fit on common training rows and scored on the same held-out rows.
- **Metrics.** None are listed.
- **Frozen values.** Nothing covers estimates identical to frozen values.
- **Constants.** Nothing refits to expose the 0.75 factor or the basis-order convention.
- **Result labels.** The source-availability label is missing (R7).
- **Significance.** Nothing warns that tiny-sample differences are not evidence. The methodology says "no calibrated uncertainty estimate for comparative model performance yet".

**Correction.** Replace §6 (lines 104–124, from "## 6. Use in evaluation" through "not win probabilities or command effects.") with:

> ## 6. Use in evaluation
>
> This plan is locked before any fit. **It authorizes no fit.** Estimates used as model inputs
> are an enriched evaluation. The feature-admission contract does not authorize one (contract
> §7), and AGENTS.md places enriched predictors behind a reviewed admission contract. A fit
> may run only after two things:
>
> - the ledger's campaign-batch review is reconciled; and
> - the owner records an explicit authorization naming the reviewed ledger hash.
>
> That authorization must do one of two things. It may (a) accept this evaluation as an
> exploratory estimate-layer diagnostic outside the admission contract. Or it may (b) place
> the evaluation under a separately reviewed admission profile. Outputs never enter
> `artifacts/baseline.json` and never replace the baseline.
>
> - **Model.** `strength-logistic-v1` is unchanged:
>   - ridge 1.0 logistic regression on (US − Confederate)/(US + Confederate), using each
>     side's rounded `point`;
>   - leave-one-campaign-out over the campaigns present in the row set;
>   - equal odds and the Laplace-smoothed, training-only prior as comparators.
>
>   Predictions are named `diagnostic_union_score`, never `p_union_win`.
> - **Leakage exclusion.** A row with either side labelled `post_start_information` enters no
>   fit. It stays in the ledger and is counted in every report.
> - **Nested row sets, all reported:**
>   1. both sides grade A;
>   2. both sides A or B;
>   3. both sides A, B or C.
> - **Evaluability.** A row set needs at least 6 rows from 3 campaigns, with both outcome
>   classes. A smaller set is reported as not evaluable, with its counts.
> - **Sensitivity refits,** each on every evaluable set:
>   - four endpoint combinations: every US side at `low` or at `high`, crossed with every
>     Confederate side at `low` or at `high`;
>   - excluding rows labelled `opponent_estimate_point`, `applicability_unresolved`,
>     `derivation_unknown` or `bound_conflict`, one label at a time;
>   - a §4 rule 4 point factor of 1 instead of 3/4;
>   - the §4 rule 3 basis order `reported_effective`, `present_for_duty`, `reported_present`,
>     `reported_engaged`, `unknown`.
> - **Reference and comparison.**
>   - Retain the frozen 23-engagement, 13-group baseline. Its battle-weighted Brier is
>     0.2768816348133779 and its campaign-weighted Brier is 0.2765271817053925, each
>     against 0.25 for equal odds.
>   - **Common rows** have both a frozen baseline row and an estimate row. In each fold, both
>     models are fit only on common training rows and scored on the same held-out rows.
>     Common rows whose estimate points equal the frozen values are reported as identical by
>     construction.
>   - **Newly covered rows** are compared only with equal odds and the prior.
>   - Results from different row sets, grade subsets or sensitivity variants are never
>     compared as improvements. At these row counts, no difference is presented as
>     significant or as evidence that the estimates are accurate.
> - **Reporting.** Each result gives:
>   - battle- and campaign-weighted Brier and log loss;
>   - row and campaign counts;
>   - the grade mix;
>   - every §5 label count;
>   - the number of rows excluded as `post_start_information`.
>
>   Every result carries `whole_engagement_leakage` and `conditional_on_source_availability`.
>   Which sides have figures, and so which rows and grades exist, may depend on the outcome,
>   on size and on fame (tier-2 §2). Predictions are diagnostics, not win probabilities or
>   command effects.

### R9: The ledger and checker cannot detect selective input recording (§7)

**Evidence.**

- §4 is deterministic only for the inputs that are recorded. As written, the checker verifies quotes, "classifications and grades against §3" and reproduction. It does not check that every available figure was recorded.
- An extractor who already knows the outcomes could therefore omit an inconvenient figure without detection. Contract §4 forbids outcome-driven selection and says blinding cannot be assumed.
- The checker also has no coverage check against the frozen cohort, no hash bindings (contract §3) and no check that each printed value appears in its quote.
- The design does not state that code-to-passage entailment cannot be checked automatically. The evidence contract (*Research and review*) says automatic checks "cannot establish ... claim entailment".

**Correction.** Replace the **Ledger**, **Checker** and **Separate review** bullets in §7 (lines 128–135) with:

> - **Ledger.** Estimates live in a versioned, immutable ledger
>   (`data/estimates/side-strength-v1.json`). It binds the hashes of this design, the source
>   registry snapshot, every cited dossier revision and the estimation script. Each input
>   carries:
>   - its source ID;
>   - its section, or its row key and column;
>   - its locator and exact quote;
>   - its tier-2 §3 codes;
>   - its same-document key;
>   - its class, basis and value.
> - **Inventory.** For each of the 91 engagements and each side, the ledger lists every
>   strength figure from three places, whether used or not, with its class or its reason for
>   non-use:
>   - the bound dossier's `strength` claims and typed quantities;
>   - the frozen CWSAC forces row;
>   - the matching Livermore entry, if any.
>
>   The other 36 records are listed as out of scope, with their reason.
> - **Checker.** An offline, standard-library checker verifies:
>   - coverage: exactly the 91 in-scope records × 2 sides, plus the 36 out-of-scope records,
>     against the frozen cohort;
>   - bindings: registry, raw-file and dossier hashes, and that no input cites a source
>     outside the bound snapshot;
>   - passages: each quote occurs in its section or CSV cell, and each input's printed value
>     occurs in its quote;
>   - inventory: every `strength` claim and typed quantity in the bound dossiers, and every
>     frozen CWSAC force figure, is referenced by an input or recorded with a reason;
>   - consistency: codes come from the tier-2 list, and each class, grade and label follows
>     mechanically from its codes under §§3 and 5;
>   - reproduction: every candidate, point, range, `point_basis`, label and nested-set
>     membership reproduces under §§4–6 with the recorded constants. Grade D sides have null
>     values and a reason. For every non-null side, 0 < low ≤ point ≤ high.
>
>   The checker cannot verify that a code, basis or quote supports its classification. That
>   is the review's task.
> - **Separate review.** A separate Opus review checks the ledger in campaign batches. It
>   covers classification, adjustment evidence, grade and the completeness of the inventory.
>   Findings are reconciled as for dossiers.

### R10: Source scope and research authorization are unstated (§2), and the roadmap is stale

**Evidence.**

- **Source scope.** §2 allows "inspected, registered sources" but does not say whether this layer authorizes new source research. Grade D ("no quantitative figure in any inspected source") depends on that answer. AGENTS.md requires deeper work to be bounded, or to follow an explicit owner request.
- **Codes list.** §2's list of "tier-2 §3 codes" omits tier-2 §3 item 4 (printed value and bounds, `estimation_status`).
- **Stale roadmap.** The roadmap header (line 13) points to "**Next priority** below". That paragraph (lines 392–405) still names only the tier-2 pipeline ("Next come a validator extension, typed quantities and one targeted strength follow-up") and does not mention the estimate decision.

**Correction 1.** In `docs/strength-estimates.md`, replace everything from "Only figures quoted in inspected, registered sources may be used." through "The rule "do not invent missing strengths" is unchanged." (§2, lines 37–48) with:

> Only figures quoted in sources registered in `data/sources.json` at the commit that accepts
> this design may be used: the first-pass dossier citations and the pinned Livermore records
> (scoping memo). New source research for this layer needs a separate, bounded owner
> authorization under AGENTS.md; until then, an unfilled side stays grade D. Each input is
> classified with the tier-2 §3 codes and fields:
>
> - whole-side scope;
> - engagement match and state time;
> - source role;
> - printed value and bounds, including `estimation_status`;
> - derivation.
>
> Model recollection, reputation and the recorded outcome are never inputs. A side with no
> usable candidate value (§3) in any inspected source gets a **null estimate (grade D)** with
> a reason. Any one-sided bound found is recorded beside the null. The rule "do not invent
> missing strengths" is unchanged.

**Correction 2.** In `docs/roadmap.md`, append the following at the end of the **Next priority** paragraph, after "Keep every engagement regardless of outcome, reputation or available strengths.":

> Owner decision, same day, after the [extraction scoping](research/reported-strength-scoping-v1.md):
> "I feel like we should make our best estimate for each." The immediate next step is separate
> review of the [best-estimate design](strength-estimates.md), which sits beside this profile
> and changes none of it. The order of the remaining tier-2 steps relative to it is not recorded.

## Advisories (no correction required)

- **A1: Interpretation of "each".**
  - The owner's words were "for each". The design reads this as the 91 decisive, non-aggregate records, because only they can be rows for the binary target.
  - That is a reasonable interpretation but not the owner's stated scope. Strength estimates for the 35 inconclusive records and VA024 would be feasible, although no model could use them.
  - Consider recording the interpretation as such, or confirming it with the owner.
  - README line 79 says "each decisive engagement". Of the 92 decisive records, 91 are non-aggregate, so "each decisive, non-aggregate engagement" would be exact.
- **A2: Officers.** The original §1 target said "including officers", and no basis code records officer inclusion. If officer inclusion is to matter, record it as included, excluded or unstated. An unstated value should not change the grade, and an explicitly enlisted-only figure should be `partial_scope`. Otherwise drop the phrase. R1's replacement drops it.
- **A3: Lower-middle median.** With an even count, the lower-middle rule shifts points systematically downward. It is declared, which is acceptable. An "upper middle" refit would expose it cheaply.
- **A4: Leakage and the C preference order.** Rule 3 (unchanged in intent from the original rule 2) prefers an own-side or compiled class-C input over an opponent estimate. When that own input is `post_start_information`, the row is excluded from fits (R8), even if a non-leaking opponent estimate exists. This follows the author's stated preference. Record that it is deliberate.
- **A5: Extraction is not blind.** The extractor and reviewers are AI systems that may already know the outcomes. Contract §4 says blinding cannot be claimed as proof. Add a sentence saying so. The R9 inventory is the structural mitigation.
- **A6: Naming the endpoint refits.** The baseline's endpoint sensitivity holds the fitted model fixed (methodology). The design's endpoint refits are true refits. Name them `endpoint_refit_*` so that the two are not confused.
- **A7: Existing tier-2 source ID.** Tier-2 §4 fixes the Livermore selection's source ID as `livermore-numbers-losses-selections-v1`. The registry grep shows `livermore-ocr-v1`, `ia-livermore-metadata-v1` and page-image IDs. This is outside this review's scope, but the §7 inventory and the `compiled_dependence` label should use whatever IDs actually exist.

## What this review does not establish

- It does not approve the design. Acceptance and reconciliation belong to the primary and the owner.
- It does not approve any estimate, classification, grade or quote.
- It does not adjudicate any historical dispute.
- It does not find any source family independent.
- It does not admit any feature or authorize a fit.
- The admission contract, the tier-2 design and the frozen baseline inputs remain as verified above.
