# Focused follow-up review: best-estimate side strength (`0e5800b`)

## Reviewer record

| Field | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. A separate reviewer subagent started with fresh context; the primary's conversation was not an input. |
| Task identity | Assignment `artifacts/review-results/strength-estimates-followup-0e5800b-opus-high-v1/assignment.md`. The runtime gave the reviewer no task ID. |
| Date | 2026-09-25 |
| Prepared commit reviewed | `0e5800b3a931305bf3762434b2280b61d3322ef0` |
| Previous commit | `cff43ea92a82493987df3a37657ae296e6b5f0c9` |
| Bundle commit (worktree HEAD) | `16601decd78ac5b1f97f46dd606fe922babbef92`. It differs from `0e5800b` only by adding this directory's `assignment.md` and `inputs.json`. |
| Assignment SHA-256 | `55a863689319ea9ee61b5531fbb884aa4a676c3fa3478d9a0b3d7367b8a9fab2` (verified) |
| Input manifest (`inputs.json`) SHA-256 | `b39828e6390e83a4eaf9b75d3cacfcf269a226859d92efe18c5aedc3d455e3e8` (verified) |
| Outcome | **Corrections required**: S1–S7. Advisories: B1–B5. |

This is an AI design review and a separate analysis. It is not human historical adjudication. It does not approve any estimate, source, classification or feature, and it does not establish that any sources are independent. It proposes no estimate. The numbers in the case analysis are synthetic, except where a frozen CSV value or a scoping-memo figure is quoted as such.

Several of the defects below sit in replacement text that the first review (the same model and effort, in a separate session) supplied and the primary applied as written. That review's corrections created or carried them forward, so they are in scope here.

## Input verification

- **Input hashes.** I hashed all 23 paths in `inputs.json` from `git show 0e5800b…:<path>`. **All 23 match**, and their worktree bytes are identical.
- **Scope of the prepared commit.** `git diff --stat cff43ea 0e5800b` changes seven files:
  - `README.md`, `docs/roadmap.md` and `docs/strength-estimates.md`;
  - four new files in `strength-estimates-design-fff4103-opus-high-v1/`: `correction.json`, `dispatch.json`, `primary-assessment.md` and `review.md`.

  No frozen input, contract, tier-2 design, code or baseline artifact changed.
- **`make check`** ran offline and exited 0:
  - 95 tests ran, `OK`.
  - It reported 127 pilot battles and 23 eligible battles in 13 campaigns.
  - The strength-logistic Brier was 0.2768816348133779, against 0.25 for equal odds.
  - Admission candidates: `blocked` 18 and `excluded` 22. There were 0 promoted rows.
  - `artifacts_written` was `false`, and `git status` stayed clean.
- **Not run.** I ran no build, reproduce or packet commands. I used no network, did no new research and started no agents.

## Scope inspected

- **Read in full:**
  - `docs/strength-estimates.md` (corrected);
  - the first review `review.md` (R1–R10, A1–A7), with `correction.json`, `primary-assessment.md` and `dispatch.json`;
  - `docs/feature-admission-reported-strength.md`;
  - `docs/research/reported-strength-scoping-v1.md`;
  - `AGENTS.md`;
  - the `cff43ea..0e5800b` diffs of `README.md` and `docs/roadmap.md`.
- **Read in part:**
  - `docs/feature-admission.md` §5 and §7;
  - `docs/roadmap.md`, lines 1–30 and 385–420;
  - `README.md`, by grep for "estimate";
  - `docs/evidence-contract.md`, by grep for its section headings and the basis rule on lines 73–74;
  - `generalship/admission.py`, lines 310–335 (how the existing validator computes `same_document_key`);
  - `generalship/baseline.py`, by grep only.
- **Checked mechanically:**
  - `data/sources.json`: the field inventory, the `independence_group` values `nps-cwsac` and `livermore-numbers-losses`, and the Livermore records' `parent_source_id` and `dependency_note`;
  - `data/raw/cwsac_forces.csv` and `artifacts/battles.json` for VA016, VA017, VA022, VA028 and PA002: frozen values, basis and dates.
- **Verified by hash only, not read:**
  - `docs/methodology.md` and `docs/sources.md`;
  - `artifacts/admission-check.json` and `artifacts/baseline.json`;
  - `data/admission/*.json` and `data/pilot/cohort.json`;
  - `cwsac_battles.csv` and `cwsac_commanders.csv`;
  - `generalship/cli.py` and `tests/test_evidence.py`.
- **Not inspected:**
  - dossiers;
  - Livermore page images or OCR text;
  - any historical source passage.

  Figures attributed to Livermore below are the scoping memo's statements of them. I did not check them against the pages.

## Status of R1–R10

| Finding | Status | Notes |
| --- | --- | --- |
| R1 target and bases | **Fully applied** | §1 text matches the replacement. It is split into *Bases*, *Relation to tier 2* and *Out of scope* paragraphs, and the `point_basis` field was added. |
| R2 grade table | **Fully applied (text)** | The table and the paragraphs on source-printed conversions, grade D and side grade match. New defects in this text: S1 (row order), S2 (loss rows). |
| R3 §4 rules | **Fully applied (text)** | Rules 1–9 match. They are reformatted as bullets, and the A4 sentence was added to rule 3. New defects in this text: S3 (rule 1 with several adjustments), S5 (rules 4 and 5). |
| R4 partial completion | **Fully applied** | Through rule 6. How the sum is recorded is left open (S3). |
| R5 dependent copies | **Applied, but the intent is not met** | Rule 2 is as specified. It still lets identical CWSAC/Livermore values vote twice or hide their derivation, and it merges different-basis figures from one document (S4). |
| R6 bias factor | **Fully applied** | Rule 4 disclaims any evidence-based bias factor, and §6 refits it. |
| R7 labels | **Fully applied (text)** | The table matches, with the A7 sentence added. New defects in the label definitions: S6. |
| R8 evaluation plan | **Fully applied** | §6 matches, with the A3 and A6 additions. New defect in the identity statement: S7. |
| R9 ledger and checker | **Fully applied (text)** | §7 matches. It needs fields for the S2/S3 codes and operands. |
| R10 source scope and roadmap | **Fully applied** | §2 matches. The roadmap paragraph was appended with updated wording that reports the review outcome instead of "the next step is separate review". This is accurate. |

## Adopted advisories

| Advisory | Check |
| --- | --- |
| A1 "each" | Adopted in §§0–1 and in README line 79. The roadmap header (lines 10–12) still says "estimates … for each decisive engagement" (B4). |
| A2 officers | Adopted; the phrase is gone. |
| A3 upper-middle refit | Adopted (§6). It applies to the medians of both rule 3 and rule 4, which is correct as written. |
| A4 C preference | Adopted (§4 rule 3, second bullet). |
| A5 blinding | Adopted (§2). |
| A6 `endpoint_refit_*` | Adopted (§6). |
| A7 Livermore IDs | Partly adopted. The Livermore IDs are named, but the NPS/CWSAC side of `compiled_dependence` is not. The registry already has exact `independence_group` strings for both families. The S6 correction uses them. |

## Worked cases (assignment items i–v)

**(i) The side's only inputs are an opponent estimate and a one-sided own bound.**

- **Current text:**
  - The own one-sided bound is row 5, bound-only. The opponent estimate is row 2, class C `opponent_or_hearsay`.
  - Rule 3 finds only opponent candidates and hands over to rule 4. So the grade is C, with labels `whole_engagement_leakage`, `opponent_estimate_point` and `single_input`.
  - Rule 4 never sets `point_basis`. Rule 3's basis step is skipped, and M, min and max run over all opponent candidates whatever their basis. So §1's "one recorded population basis" is not guaranteed, and `basis_mixed` is undefined.
  - Rule 7 applies a bound "only if its basis is `point_basis`", so it cannot be evaluated. That makes the outcome **undefined (S5)**.
  - If the opponent figure is itself one-sided (for example, "over 20,000"), rows 2–4 are tested before row 5. It becomes a class-C *candidate* with value 20,000, not a bound. Rule 4 then gives high = 20,000, which is below a figure the source says was exceeded **(S1)**.
- **After S1 and S5 (synthetic):**
  - Inputs: an opponent estimate of 20,000 on basis *b*, and an own "over 12,000" on *b*, which is otherwise class A.
  - Result: `point_basis` *b*, point 15,000, low 10,000 raised to 12,000 by rule 7, high 20,000; grade C.
  - An own "over 16,000" instead lies above the point. It is not applied, and the side is labelled `bound_conflict`.
  - If the opponent figure's basis is `unknown`, `point_basis` is `unknown`, and an own bound on a stated basis never applies (B3).
  - An opponent-only one-sided figure becomes grade D, with its bound recorded.

**(ii) Two class-A candidates on different bases.**

- **Separate documents:**
  - Rule 3 keeps the first basis in the declared order and sets `point_basis`.
  - Rule 5's hull takes only candidates on `point_basis` or `unknown`. A class-A candidate cannot have an `unknown` basis, because `basis_unknown` is a row 7 condition.
  - The other-basis candidate is recorded and unused. The margin is 1/20. The labels include `single_input`.
  - Synthetic example: engaged 10,000 and effective 9,000 give a point of 10,000 with range 9,500–10,500.
- **Same document:** Rule 2's first bullet applies. For example, the scoping memo says Livermore p.96 gives Fredericksburg US present-for-duty, engaged and effective figures together.
  - All three inputs share one `same_document_key`, so rule 2 merges them into **one** candidate "taken from the member with the lowest source ID".
  - The members share a source ID, so the member chosen, its value and its basis are all **undefined**. Two of the three bases are lost **(S4)**.

**(iii) A class-B unknown-basis figure with a class-A figure on another basis.**

- Rule 3 uses the class-A figure; `point_basis` is its basis, and the grade is A.
- Rule 5's hull also admits the class-B figure, because its basis is `unknown`. So low = min × 19/20 and high = max × 21/20, at grade A's margin.
- Synthetic example: A engaged 10,000 and B unknown 12,000 give point 10,000, low 9,500 and high 12,600.
- The B figure's `derivation_unknown` label propagates, because that label covers the range. An `applicability_unresolved` label would not propagate.
- Whether `single_input` applies is ambiguous: one candidate sets the point, but two set the range **(S6)**.
- `basis_mixed` is not triggered. That hull rule was an accepted R3 choice and is not reopened here (B1).

**(iv) Identical CWSAC and Livermore values (rule 2).**

- **Two routes.** Rule 2 merges them only if they are "recorded as a reproduction", which is an extraction-time judgement with no criterion.
  - If they are not recorded as one, they are two candidates. With equal class and basis, the value votes twice in the median.
  - If they are recorded as one, the merged candidate is "the member with the lowest source ID". `arnold-cwsac-forces` sorts before `livermore-…`, so the CWSAC copy's class, basis and labels win.
- **Gaines' Mill Confederate side (frozen VA017, start 1862-06-27).**
  - The frozen CWSAC value is 57,018 (`source_reported_forces_engaged`, `arnold-cwsac-forces`). The CWSAC row states no derivation, so it is row 8: class A with `derivation_unknown`.
  - The scoping memo states that Livermore's identical 57,018 is effectives "adding losses June 28–July 1". Those are later engagements, so it is row 3: class C `post_start_information`.
  - **Either route:** the side is grade A, the point is 57,018 (57,020 after rounding) and there is no `post_start_information` label. The row can enter every nested set, including the grade-A primary set.
- **Why this matters.** This contradicts scoping memo finding 2 (Gaines' Mill is loss-derived on both sides) and the exclusions that tier-2 §2 lists "with transitive dependency checks". The outcome also depends on a judgement made after extraction **(S4)**.
- **OCR and page images.** For Livermore, the lowest-source-ID rule also prefers `livermore-ocr-v1` over `livermore-p{N}-image-v1`, although the memo says the OCR corrupts figures and every figure was read from the images.

**(v) A grade-C post-start figure as the sole input.**

- **Current text:**
  - The input is row 3, class C. Rule 3 gives point V and `point_basis` its basis.
  - Rule 5's hull includes V, because it is used in the median. With m = 3/10, low = 7/10 V and high = 13/10 V. For V = 10,000 that is 10,000, 7,000 and 13,000.
  - Labels: `whole_engagement_leakage`, `post_start_information`, `single_input`, and `compiled_dependence` if the source is from a compiled family.
  - §6 keeps the row out of every fit and counts it in each report.

  This case is internally consistent.
- **Variants that are not:**
  - If V is also an opponent estimate, the first-match class is row 2. Rule 4 then applies, and §5 defines `post_start_information` as "class C under §3 row 3", so the leakage label may not fire **(S6)**.
  - If V is also partial-scope, it becomes a whole-side candidate instead of a bound **(S1)**.

## Required corrections

### S1: First-match order turns one-sided and partial figures into whole-side candidates (§3)

**Evidence.**

- §3 says each input takes "its class from the first matching row". Rows 2 (opponent/hearsay), 3 (post-start) and 4 (unresolved) are tested before row 5 (`one_sided_bound`, `partial_scope`, `partial_interval`).
- So an opponent's "over 10,000", a prisoner's figure for one enemy column, or a post-start return for one division becomes a class-C **candidate value** for the whole side (rule 1: "its printed value").
- This conflicts with:
  - row 5 ("never a candidate value");
  - contract §5 ("A partial army total is not a whole-army estimate");
  - tier-2 §6 (a one-sided bound has "no finite pair of bounds").
- Rule 7 already says what the other rows should decide for a bound: it applies only if, "apart from being one-sided or partial, it would be class A or B".

**Correction.** Replace §3 lines 86–88, from "**Classification rule.** Each input takes its class from the first matching row below," through "on the other side or on the outcome.", with:

> **Classification rule.** Each input takes its class from the first matching row below,
> testing row 1, then row 5, then rows 2–4 and 6–8 in order, using its tier-2 §3 coding,
> its derivation and the §3 loss and adjustment fields. A one-sided or partial input is
> therefore bound-only whatever else it matches; its other matching rows decide only whether
> §4 rule 7 may apply it. The labels of every matching row apply (§5). The class never
> depends on the figure's value, on the other side or on the outcome.

### S2: The loss rows leave gaps and cannot be derived mechanically from the codes (§3 rows 3 and 7, §7)

**Evidence.**

- **Row 3** covers losses "of this engagement or of a later one". **Row 7** covers losses "only from engagements that ended before the frozen start date, each loss figure quoted". Three kinds of input match neither row, fall through to row 8 and become **class A**:
  - losses of an engagement that ends on the frozen start date but is not this record;
  - losses the passage does not date;
  - a prior-loss adjustment made by the source without quoting the loss figures.

  The scoping memo lists source-made prior-loss adjustments, such as the Gettysburg CS total that "deducts prior losses" and Gaines' Mill US "from a return less June 26 losses". Under the current text, such a figure is class A if the losses are unquoted but only class B if they are quoted. The better-documented figure gets the worse class.
- **Mapping.** The tier-2 code `derived_from_losses` (tier-2 §3 item 5, §8) is the only tier-2 code that no row names. The tier-2 codes do not record *whose* losses were used or *when*.
- **Checker.** §7's checker requires each class to follow "mechanically from its codes", using codes "from the tier-2 list". That cannot separate rows 3, 7 and 8.

**Correction 1.** Replace §3 row 3 with:

> | 3 | A value that uses losses, captures, surrenders or survivors of any engagement that the passage does not date entirely before the frozen start date (this engagement, a later one, or an undated one), whether the source or we made the adjustment (`loss_timing: not_prior`); or a return state-dated after the frozen start date (`post_engagement_state`, with tier-2 §3 item 2's earlier-date exception) | C, `post_start_information` |

**Correction 2.** Replace §3 row 7 with:

> | 7 | Exactly one of: `basis_unknown`; losses added or subtracted only from engagements that the passage dates entirely before the frozen start date (`loss_timing: prior_engagements_only`), by the source or by us, with each loss figure quoted as its own input when we make the adjustment; a completed sum under §4 rule 6; conversion between bases using a ratio quoted for this side in this engagement | B |

**Correction 3.** Insert after the **Source-printed conversions** paragraph (after line 103):

> **Loss and adjustment fields.** The tier-2 codes do not separate rows 3, 7 and 8, so each
> input also records:
>
> - `loss_timing`: `none`, `prior_engagements_only` or `not_prior`. An input coded
>   `derived_from_losses`, or whose passage shows losses, captures, surrenders or survivors
>   added or subtracted, is `prior_engagements_only` only if the passage dates every such
>   loss before the frozen start date; otherwise it is `not_prior`.
> - `adjustments`: each adjustment we apply, with its kind (`completed_sum`, `prior_loss`
>   or `quoted_ratio`) and the input IDs of its quoted operands. An adjustment that the
>   source itself made is not listed here. It is classed through `loss_timing` or the
>   source-printed conversion rule above.

**Correction 4.** In §7, replace the checker's **consistency** bullet (lines 301–302) with:

> - consistency: codes come from the tier-2 list and the §3 `loss_timing` and `adjustments`
>   fields, and each class, grade and label follows mechanically from them under §§3 and 5;

### S3: Rule 1 allows one adjustment where row 6 allows several, and sums and operands have no record (§4 rule 1, §7)

**Evidence.**

- §3 row 6 classes an input with "two or more of the row 7 conditions" as C. Two of those conditions can be adjustments, for example a prior-loss subtraction and a quoted-ratio conversion.
- Rule 1 applies only "the single adjustment its class allows (§3 row 7)". For a row 6 input with two adjustments, the candidate value is therefore undefined. The order matters too: ratio × (return − loss) differs from ratio × return − loss.
- A rule 6 sum has no printed value or quote of its own. Yet §7 requires every input to carry "its locator and exact quote", and the checker requires "each input's printed value occurs in its quote".
- The §7 ledger has no field for adjustment operands. The script therefore cannot reproduce adjusted candidates from the recorded inputs, although §4 forbids authored numbers.

**Correction 1.** Replace §4 rule 1 (lines 116–118) with:

> 1. **Candidate values.** Each class A, B or C input has one candidate value. Its starting
>    value is its printed value, the midpoint of its printed two-sided bounds, or, for a
>    `completed_sum`, the sum of its operands' values. The script then applies the other
>    adjustments in its `adjustments` field (§3) in the fixed order `prior_loss`, then
>    `quoted_ratio`. Class B allows one listed adjustment or condition (§3 row 7); more make
>    the input class C (§3 row 6). Bound-only and unusable inputs have no candidate value.

**Correction 2.** In §7 **Ledger**, replace the bullet "its class, basis and value." (line 283) with:

> - its class, basis and value;
> - its `loss_timing` and `adjustments` (§3), with the input IDs of every operand. A
>   `completed_sum` input has no quote of its own; it lists its component inputs instead.

**Correction 3.** In §7 **Checker**, replace the **passages** bullet (lines 297–298) with:

> - passages: each quote occurs in its section or CSV cell, and each input's printed value
>   occurs in its quote. A `completed_sum` input is checked through its operands, and its
>   value is recomputed from them;

### S4: Rule 2 merges the wrong inputs and keeps the wrong member (§4 rule 2)

**Evidence.**

- **Different bases from one document.** "Inputs from one underlying document … form one candidate". This merges figures on *different bases* from one document into one, with no defined basis. Examples from the scoping memo are the three Fredericksburg US figures on p.96, the Stones River present-for-duty and effectives figures, and Corinth US. Those members share one source ID, so "the member with the lowest source ID" is undefined.
- **OCR over page image.** The same tie-break prefers `livermore-ocr-v1` over `livermore-p{N}-image-v1`. According to the scoping memo, the OCR "runs superscript note markers into the figures", and every figure it reports was read from the page images. The registry links the images to the OCR by `parent_source_id`. The existing validator (`generalship/admission.py`, lines 321–324) gives them different `same_document_key` values unless `facsimile_source_id` is set. So whether rule 2's "transcript/facsimile pairs" even covers them is unresolved.
- **CWSAC and Livermore.**
  - Scoping memo finding 2 says five frozen CWSAC values equal Livermore's exactly, and "the NPS/CWSAC and Livermore families are therefore not independent". The registry `dependency_note` on the Livermore records says the same.
  - Rule 2 counts such a pair once only when an extractor "records" a reproduction, which is a post-extraction judgement.
  - Whether merged or not, the CWSAC copy decides the class. Worked case (iv) shows the Gaines' Mill Confederate side entering the grade-A set with no `post_start_information` label.
  - The frozen VA017 value 57,018 and its date 1862-06-27 are confirmed in `cwsac_forces.csv` and `artifacts/battles.json`.
- **Basis relabelling.** The copies also relabel bases. The frozen CWSAC basis is `source_reported_forces_engaged` for all ten figures in the five matching engagements. Livermore calls several of those same numbers effectives, including VA016 US and CS, VA017 US and CS, and PA002 US. Rule 3's basis order then prefers the CWSAC "engaged" label. The evidence contract (lines 73–74) says a basis is retained, never inferred.

**Correction.** Replace §4 rule 2 (lines 119–126, from "2. **Dependent inputs count once.**" through "never raises a grade (contract §5).") with:

> 2. **Dependent inputs count once.** Class A, B and C inputs for one side form one
>    dependence group when any of these links them; links are transitive:
>    - they come from one underlying document (the same `same_document_key`, registry
>      aliases, or transcript/facsimile pairs) and give the same printed value on the same
>      basis;
>    - one is recorded as a reproduction of the other with the same printed value;
>    - one comes from a source whose registry `independence_group` is `nps-cwsac` and the
>      other from `livermore-numbers-losses`, and their printed values are equal, whatever
>      bases they record (scoping memo, finding 2).
>
>    A group is one candidate with that value. §3 is applied to the union of its members'
>    conditions: the group takes the class of the first row that union matches and carries
>    every member's labels. If any member is unusable (§3 row 1) or bound-only (§3 row 5),
>    so is the group. When members record different bases, the group's basis is `unknown`
>    and the union includes `basis_unknown`; otherwise it keeps the members' basis. The
>    group cites the member with the lowest source ID and lists the others. Figures from one
>    document on different bases, or with different values, stay separate candidates.
>
>    A Livermore figure is cited from its registered page image (`livermore-p{N}-image-v1`).
>    The OCR text of the same figure (`livermore-ocr-v1`) is listed in the inventory only,
>    because the OCR runs note markers into figures (scoping memo).
>
>    Other agreement is not corroboration and never raises a grade (contract §5).

**Consequence to record.**

- Under this text, an identical CWSAC/Livermore value takes the most restrictive class of its copies.
- Where the two families label one number with different bases, it becomes `unknown`-basis. By the scoping memo's figures, that makes it class B or lower for VA016 (both sides), VA017 US, VA022 US and PA002 US.
- VA017 CS and VA022 CS become class C `post_start_information` and leave every fit. For VA022 CS, the memo says note 5 adds the 195 lost on Aug 9, the frozen start date.

Another convention fixed before extraction would also cure the defect, provided that the more informative copy's derivation is never hidden. One example is always taking the basis a Livermore passage states.

### S5: Rule 4 has no `point_basis`, and rule 5's opponent cap ignores basis (§4 rules 4 and 5)

**Evidence.**

- §1 says "Each side records its `point_basis` (§4 rule 3)". §5's `basis_mixed` and rule 7's bound test both depend on it.
- When rule 3 hands over to rule 4, no basis is chosen. M, min and max then run across every opponent candidate, mixing bases within one side. That contradicts §1's "on one recorded population basis".
- In rule 5, "An `opponent_or_hearsay` candidate larger than high becomes high" has no basis condition. Rule 5's last bullet, however, says "Candidates on other stated bases … do not enter the point or the range". So the rule contradicts itself.

**Correction 1.** Replace the opening of §4 rule 4 (lines 138–140, from "4. **Opponent or hearsay only.** Let M be" through "the smallest and largest candidates.") with:

> 4. **Opponent or hearsay only.** Keep the `opponent_or_hearsay` candidates of the first
>    basis present in the rule 3 order; that basis is `point_basis`. Let M be the median of
>    the kept candidates (the lower middle value for an even count). Let min and max be the
>    smallest and largest `opponent_or_hearsay` candidates whose basis is `point_basis` or
>    `unknown`.

Keep the "Then:" bullets and the rest of rule 4 unchanged. The invariant still holds: min ≤ M ≤ max, so 1/2 min ≤ 3/4 M ≤ max.

**Correction 2.** In §4 rule 5, replace the bullet "An `opponent_or_hearsay` candidate larger than high becomes high. Such a candidate never lowers `low` or sets the point." with:

> - An `opponent_or_hearsay` candidate whose basis is `point_basis` or `unknown` and that is
>   larger than high becomes high. Such a candidate never lowers `low` or sets the point.

### S6: Some label definitions are not mechanical (§5)

**Evidence.**

- **`post_start_information` and `applicability_unresolved`.** They are defined by "class C under §3 row 3" and "row 4". Under first match, an input that is both an opponent estimate and post-start is classed by row 2. §3 says "the labels of every matching row apply", but §5 keys on the class. The leakage label may therefore not fire. The input can still set the point (rule 4) or `high` (rule 5), and endpoint refits use `high`.
- **`single_input`.** It says "One candidate … determines the side". That is ambiguous when one candidate sets the point but others widen the range (case iii).
- **`compiled_dependence`.** It names the "NPS/CWSAC or Livermore families" without the registry keys, although the registry has them: `independence_group` values `nps-cwsac` and `livermore-numbers-losses`.

**Correction.** Replace these four §5 rows (lines 193, 195, 201 and 202) with:

> | `post_start_information` | Any candidate used for the point or range matches §3 row 3, whatever row set its class: losses, captures, surrenders or survivors of an engagement not dated entirely before the frozen start date, or a post-start return. |
> | `applicability_unresolved` | A candidate used for the point matches §3 row 4, whatever row set its class. |
> | `single_input` | Exactly one candidate (after §4 rule 2) enters the side's point and range under §4 rule 4 or 5. |
> | `compiled_dependence` | A candidate used for the point, or any member of its §4 rule 2 group, cites a source whose registry `independence_group` is `nps-cwsac` or `livermore-numbers-losses` (scoping memo, finding 2; A7). The registered Livermore IDs are `livermore-ocr-v1` and `livermore-p{N}-image-v1`. |

### S7: Rounding stops the "identical by construction" statement from ever firing (§6)

**Evidence.**

- §6 says "Common rows whose estimate points equal the frozen values are reported as identical by construction", and it uses "the stored, rounded values" (rule 9).
- The frozen values are unrounded integers. In the five engagements where CWSAC equals Livermore, 9 of the 10 frozen values are not multiples of 10: 16,356, 15,631, 57,018, 34,214, 16,868, 72,497, 100,007, 75,054 and 83,289. Only VA022 US 8,030 is.
- So an estimate resting on the frozen figure itself is never reported as identical. The paired comparison would then show differences caused only by rounding, without saying so.

**Correction.** In §6 **Reference and comparison**, replace "Common rows whose estimate points equal the frozen values are reported as identical by construction." with:

> Common rows whose estimate points equal the frozen values on both sides before §4 rule 9
> rounding are reported as identical by construction; their fitted inputs differ from the
> frozen values only by that rounding, and the report says so.

## Advisories (no correction required)

- **B1: Lower-class candidates in higher-grade ranges (case iii).**
  - Rule 5's hull takes every non-opponent candidate on `point_basis` or `unknown`, whatever its class, and applies the side grade's margin. So a class-B or class-C figure can widen a grade-A range at the 1/20 margin.
  - `derivation_unknown` and `post_start_information` cover the range, but `applicability_unresolved` covers only the point.
  - This follows from the accepted R3 text. Consider reporting, per side, the lowest class of any range input, or extending `applicability_unresolved` to "point or range".
- **B2: Livermore completeness is not checked mechanically.**
  - §7's inventory lists "the matching Livermore entry, if any", but the checker's **inventory** bullet covers only dossier claims and quantities and the CWSAC rows. No structured Livermore extraction exists for it to check against.
  - Consider adding to the sentence "The checker cannot verify…": "or that every figure in a matching Livermore entry is listed".
- **B3: Rule 7 and unknown `point_basis`.**
  - Opponent estimates often have no stated basis. Then `point_basis` is `unknown`, and an own-side bound on a stated basis never applies.
  - Separately, an own lower bound above a rule 4 point is set aside as `bound_conflict`.
  - Both follow from the accepted "bounds never move the point" and basis rules. Record them as declared consequences so the row counts are not a surprise.
- **B4: Stale status text.**
  - The roadmap header (lines 10–12) still says "The next step is separate review of the best-estimate side-strength design … for each decisive engagement". README line 80 says the design "awaits separate review".
  - Both should be updated when this follow-up is reconciled. The header should also say "decisive, non-aggregate" (A1).
- **B5: Rounding and the positivity check.**
  - Rule 9 rounds a low below 5 to 0, and the checker then fails "0 < low".
  - This needs a side smaller than about 8 people and is unlikely in this cohort. If it occurs, the fix is a documented floor of 10, not a silent fix.

## Outcome

**Corrections required: S1, S2, S3, S4, S5, S6, S7.** Advisories: B1–B5.

S4 and S1 are the most consequential:

- **S4:** without it, a CWSAC copy of a Livermore loss-derived figure enters the grade-A set with no leakage label.
- **S1:** without it, partial or one-sided figures can set whole-side points.

S2, S3, S5 and S6 close cases the rules leave undefined, or that could only be settled after extraction. S7 fixes a reporting statement that could never be true.

## What this review does not establish

- It does not approve the design. Acceptance and reconciliation belong to the primary and the owner.
- It does not approve any estimate, classification, grade or quote, and it computes no estimate for any engagement.
- It does not adjudicate any historical dispute. It did not check any Livermore figure against the page; the figures come from the scoping memo.
- It does not find any sources independent.
- It does not admit a feature or authorize a fit.
