# Grade E strength design: separate design review

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. A new subagent with fresh context; the author's conversation was not an input.
- **Date:** 2026-09-25.
- **Commits:** prepared `2779bb6828ee09eb2079db6047b4d8908362fffb`, previous `3f5c7a99d6e75ac6bdb16acb2eede4f8deff31a0`, bundle `27a3dc41d7d2c459d95c9b4ff6b9869376ed7f1e` (worktree HEAD). Between `2779bb6` and `27a3dc4` nothing under `docs/`, `data/` or `generalship/` differs; the bundle commit adds only the assignment and `inputs.json`.
- **Assignment:** `assignment.md`, sha256 `d649c4f9e6003c66f0b0a1967edb6868614851f05b2add3dc3af41336208a684`. **Input manifest:** `inputs.json`, sha256 `d8fa597edbe981e06a5e47f5d2d0bc0f204fffec9e5c2309924d7fd0635a8e7a`.
- **Outcome: corrections required** (R1–R8). Advisories A1–A11 are listed separately.

This is an AI review, a separate analysis. It is not historical adjudication, feature admission, independent corroboration or authorization of any fit.

## Input verification

All 20 paths in `inputs.json` match their recorded SHA-256 under `git show 2779bb6:<path>`, and the working tree matches them too. There were no mismatches.

The assignment also directed me to files that `inputs.json` does not bind. I read them at `2779bb6`, where they are identical to the worktree:

| Path | SHA-256 |
| --- | --- |
| `data/estimates/side-strength-v2.json` | `7855d4d3c8853f7eb94849cb3701c0ca3e3bd759df11b8ffcb5e086cc92deed8` (matches the run-2 authorization prefix) |
| `data/command/responsibility-v2.json` | `495cef30b475920c2bd02991a4a107dfb3f3079fa494d43512a216dc82da06ac` |
| `data/command/commanders-v2.json` | `91fc25260c8370a64b7599940dec22c7640efac8b497dc6ae99ff6eeb45e3768` |
| `docs/strength-estimates.md` | `795212ad5a3291a6630911fd5671c9f85a52b19c1d05045c091db1de96164ba3` |
| `docs/commander-ratings.md` | `0ab4b7d541baf4f8e642634f316628f9cb372d68dcdbbc047a305f5a1fb704bb` |
| `docs/ledgers-v2.md` | `9076d96bd317568f6bf976d1a63f7696a7d7abc22b3f72597af96701ee1ec2ee` |
| `docs/research/commander-ratings-v2.md` | `9607de97d795c9c45ae8071336e0788c307add2d7e1ec4175b7995b549cf2d20` |
| `data/raw/cwsac_campaigns.csv` | `93813220a72767a77a4632905d38718593d401901ae16698973e4ae8b9f555ae` |
| `generalship/estimates.py` | `af540a924aed29b20032319b8779742c0f43e991c118ee747672bba73fc3a32f` |
| `generalship/ratings.py` | `8d41dc88bcbfa99261e841c101107dd0862a6fb3756a6d281b6235f239fcf506` |
| `generalship/baseline.py` | `731d9ad96dc85ca8f69bd7689e7ec64d9a1917b1a4b9d45c9c55b37348d42179` |

## Scope actually inspected

- **Read in full:**
  - `AGENTS.md`;
  - the draft `docs/strength-imputation.md` (152 lines);
  - the owner decision JSON;
  - `docs/strength-estimates.md`, `docs/commander-ratings.md` and `docs/ledgers-v2.md`;
  - the run-2 memo `docs/research/commander-ratings-v2.md`.
- **Read in part:**
  - `generalship/estimates.py`: the §3 classification, `printed_value` and the rule 7 bounds;
  - `generalship/ratings.py`: the view list and the source of p for the residual sum;
  - `generalship/baseline.py`: `advantage`;
  - the headers and theater column of the frozen `cwsac_battles.csv`, `cwsac_forces.csv` and `cwsac_campaigns.csv`.
- **Computed in memory (no fits, no artifacts written):**
  - over all 305 in-scope engagements of both v2 ledgers: grade counts, grade D input profiles, the codes on every bound input of a grade D side, and the eligibility of each bound under the accepted rule 7;
  - L > U conflicts under the draft's rule and under rule 7;
  - training and target counts by echelon, theater, period and side;
  - joint-command and flotilla sides, and nesting outcomes;
  - how many rows have 0, 1 or 2 grade D sides;
  - a descriptive table of grade D status against the recorded CWSAC result (see A2).
- **`make check`:** run offline, exit 0. 143 tests OK; `generalship check` passed. The worktree stayed clean.
- **Not inspected:**
  - no dossier or source passage. This is a design review, and no quotation-level claim was under review;
  - other files named in the manifest (`README.md`, `docs/methodology.md`, `docs/roadmap.md`, `docs/evidence-contract.md`, `docs/sources.md`, the `artifacts/*.json` and admission files, `tests/test_evidence.py`, `generalship/cli.py`) beyond their hash;
  - the review bundles cited by the accepted designs.
- **Not done:** no model was fitted, no rating, build, packet or evaluation command was run, and no network access was used.

## Checked and found sound

- **§1 counts reproduce from the v2 strength ledger.**
  - 262 grade D sides.
  - 88 with only lower bounds, 16 with lower and upper, 9 with only upper.
  - 8 with only unusable or `bound: null` inputs.
  - 141 with no inputs: 85 of them have a frozen `cwsac_forces.csv` description and 56 have none.
  - 126 run-2 rows.
- **§3 rows.** The 301 all-battles rows and the four `nested` contained records are correct. So is TN035 as the only unresolved contained record left once the nested ones are dropped: VA033/VA034 is unresolved, but both records are already dropped as nested in VA032.
- **Leakage from casualties.** Excluding casualties is right. No `casualties*` field enters, and the response excludes `post_start_information` sides (20 A–C sides).
- **Scoring by averaged probabilities.** Averaging each held-out row's probability over imputations and then scoring log loss is sound. It scores the multiple-imputation predictive mixture, and it treats both models identically. Pooling equal numbers of Laplace draws per imputation is a standard mixture approximation to the multiple-imputation posterior, suitable for intervals and ranks.
- **The verdict rule stays fixed.** It uses one configuration, strict inequality under both weightings and a fixed seed and M. No view may reverse it.
- **Fidelity to the owner's decision.** The draft does what the owner decided: modelled strengths fill the blank sides, and the all-battles test is the single verdict for future runs. Run 2 and the ledgers are unchanged.

## Required corrections

### R1 — Bounds: outcome-dependent and non-applicable bounds would truncate grade E (leakage; §2 "Bounds")

**Problem.** The draft applies every `bound`-class input. Of the 113 grade D sides with a directional bound, 15 would be truncated by an input the accepted design classes as post-start information (§3 row 3: `loss_timing: not_prior` or `post_engagement_state`). None of those sides would carry `post_start_information`. Examples:

- GA015 and GA022: Livermore figures that add or deduct this record's own losses;
- VA081 CS: an upper bound of 1,000, the force "at the close of the action";
- VA064 CS: prisoners' 20,000 on the 18th;
- VA054, VA042, VA072, NM002, SC005, LA010 and NC020.

Other bounds would act as hard floors or caps even though the accepted rule 7 refuses to apply them:

- 46 opponent or hearsay lower bounds and 6 upper bounds, for example MO027 US "exceeded 20,000" and NC020 US "above 20,000";
- 37 bounds coded `engagement_link_unknown`. For example, TN034 US uses corps returns of October 31 whose note says "only elements were at Columbia", and MO021/MO023 CS use Price's army on entering Missouri.

Under the draft's rule 5 sides have L > U (AR005 CS, KY005 US, LA018 CS, NM002 US, VA022 US). Under rule 7 eligibility only KY005 US and VA022 US conflict.

The draft also leaves open:

- which value a printed range contributes as a bound;
- what happens to `bound: null` inputs (29 on grade D sides, recorded as parts, phases or post-start counts without a direction);
- what happens to class A, B or C members of an unusable or bound-only group on a grade D side (VA022 US, VA086 US and CS, AR005 CS).

**Replacement for §2 "Bounds":**

> **Bounds.** A grade D side's input constrains its distribution only if its `bound` is `lower` or `upper` and, apart from its `one_sided_bound`, `partial_scope` or `partial_interval` codes, it would be class A or B under strength-estimates §3 (the eligibility test of §4 rule 7). The `point_basis` condition of rule 7 is not applied, because a grade D side has no point basis and the response mixes bases. A bound's value is its printed value (the midpoint of a printed range, as `printed_value` in `generalship/estimates.py`). L is the largest applicable lower bound and U the smallest applicable upper bound, in people. A lower bound coded `partial_scope` or `partial_interval` is still a lower bound on the whole side. Inputs with `bound: null`, bound inputs that fail the eligibility test (opponent or hearsay, post-start, applicability unresolved), and class A–C or unusable inputs of a grade D side are not used. Each is listed in the output with its reason, and the side is labelled `bound_not_applied` when any directional bound was set aside. No grade E value uses post-start information.

**Add to §6:**

> - `all_bounds`: multiple imputation (M = 20, same seed) in which every recorded `lower` or `upper` bound of a grade D side is applied, whatever its class; sides whose applied bounds include a §3 row 3 input carry `post_start_information`.

### R2 — Echelon of joint-command sides is chosen by the result (leakage; §2 "Predictors")

**Problem.** For the second case of commander-ratings §2 rule 5, the ledger takes the commander of "the force that … shows compelling the result". The echelon of such a side (flotilla, army, detachment and so on) therefore depends on the outcome. 20 sides are labelled `joint_command`, and 15 of them are grade D strength sides whose echelon would drive their grade E value: AL003 US and CS, AR002 US, LA001 CS, LA002 US, LA020 US, MO012 US, NC001 US, NC014 US, NC015 US, TN004 US and CS, TX003 US, TX006 US and VA012 CS. The training set includes TN001 US (`flotilla`, 17,000).

**Replacement for the §2 "Echelon" bullet:**

> - **Echelon** of the side's responsible command, from the v2 command ledger (`army`, `corps_or_wing`, `division`, `brigade`, `regiment`, `detachment_or_post`, `flotilla`, `unknown`). A side with no chosen commander uses its ledger echelon as recorded. A side labelled `joint_command` uses `unknown`, in training and in imputation, because commander-ratings §2 rule 5 chooses its commander by the force that compelled the result; such a grade E side is labelled `joint_command_echelon_unknown`.

**Add to §6:**

> - `ledger_echelon_joint`: multiple imputation (M = 20, same seed) using the ledger echelon for `joint_command` sides.

### R3 — Merged levels and naval sides are not stated (§2 "Levels with fewer than five…")

**Problem.** Among the 328 training sides, `regiment` has 1 row and `flotilla` has 3 (SC004 US 1,200; SC009 US 410; TN001 US 17,000). Both therefore merge into `unknown`, whose training median is 3,000. The draft names only `regiment`. The 15 grade D flotilla sides (8 remain `flotilla` after R2: FL002, FL004, GA002, LA004, MS004, TX001, TX002 and VA012, all US) would be modelled as land sides of unknown echelon. The draft has no naval rule, and the grade D null reasons for such sides include "Only vessel counts" and "one gunboat". No in-scope engagement is in the Pacific Coast campaign, so the draft's theater merge is moot.

**Replacement for the paragraph "Levels with fewer than five training rows…":**

> Any level of any predictor with fewer than five training rows is merged: echelon levels into `unknown`, and a theater or period level into the adjacent level named in the output. On the v2 ledgers this merges `regiment` (1 training row) and `flotilla` (3) into `unknown`; no theater or period level merges (Pacific Coast has no in-scope engagement). Every merge and its training count is recorded in the output. A grade E side whose ledger echelon is `flotilla` is modelled as a land side of unknown echelon, which is not evidence about crew size; it is labelled `naval_side`.

**Add to §6:**

> - `no_naval_grade_e`: drops rows with a grade E side labelled `naval_side`.

### R4 — The force feature is misdescribed (§5 "Multiple imputation")

The accepted design (commander-ratings §4) and the code (`generalship/baseline.py` `advantage`) use x = (US − CS)/(US + CS), not a log-ratio.

**Replace** "The force feature x is the same log-ratio as before." **with:**

> The force feature is unchanged: x = (US − CS)/(US + CS) on each imputation's strengths (`advantage` in `generalship/baseline.py`).

### R5 — Fit, calibration and draw definitions are not complete (§2 "Fit", "Calibration"; §5)

**Problem.** Implementation still needs several choices the draft leaves open:

- the ridge objective and the p in √(n/(n − p));
- which σ scores a leave-one-out row;
- "makes coverage 0.80" on discrete data;
- the truncated-normal sampling method and draw order;
- whether the imputation model is refitted per fold, and whether draws are shared across folds.

**Replacement for "Fit":**

> **Fit.** Minimize Σ residual² + 1.0 × Σ (non-intercept coefficient)², with indicator columns for every non-reference level after merges (reference levels `unknown`, US, 1863, Eastern). σ is the root mean squared residual scaled by √(n / (n − p)), where p is the number of columns including the intercept. The model is fitted once, on all training rows; it is not refitted within the §5 folds (it uses no outcome).

**Replacement for the "Calibration" sentence beginning "If c < 0.80":**

> Each held-out row is scored against N(μ₋ᵢ, σ₋ᵢ²) from the refit without it. If c < 0.80, σ is multiplied by the smallest k on the grid 1.00, 1.01, … for which the leave-one-out share inside the central 80% of N(μ₋ᵢ, (kσ₋ᵢ)²) is at least 0.80.

**Add to §5 "Multiple imputation":**

> Draws use one `random.Random(20260926)` stream, taken in the order imputation m = 1…20, then grade E sides sorted by battle ID and side (US before Confederate). A draw is Φ⁻¹(Φ(a) + u(Φ(b) − Φ(a))) on the standardized truncation limits a, b (−∞/+∞ where absent), with `statistics.NormalDist`. The same M imputed data sets are used in every fold, view and model.

### R6 — Views: run-2 endpoint refits missing, view_sensitive reference undefined (§6)

**Problem.**

- **Endpoint refits.** Run 2's robustness views include the four endpoint refits (`endpoint_us_{low,high}_cs_{low,high}` in `ratings.py`). The draft's list omits them without saying so.
- **Mismatched reference.** The views run on one median imputation, but `view_sensitive` compares a view's intervals with the primary's. Under the draft that primary is the pooled multiple-imputation result, whose intervals are wider for a different reason.
- **Unclassified views.** The draft does not say which of its declared views set `view_sensitive`.

**Replacement for the §6 opening and last line:**

> Run on the grade E points (one imputation at the medians), except where stated. That single-imputation fit on the 301 rows is reported as the view `median_imputation`, and it is the reference for `view_sensitive` and `unranked_in_view` in the robustness views.
>
> - every run-2 robustness view (τ 0.25 and 1.0, α sd 3, grades A–B for command, superior, command-changed excluded and successor, alternative candidates), and the four endpoint refits, with each A–C side at its ledger `low` or `high` and each grade E side at its 10th or 90th percentile;
>
> …
>
> `view_sensitive` and `unranked_in_view` follow design §6 over the robustness views listed in the first bullet, compared with `median_imputation`. The other views here (`strength_graded_only`, `no_post_start`, `no_bound_conflict`, `wide_imputation`, `all_bounds`, `ledger_echelon_joint`, `no_naval_grade_e`, `drop_nesting_unresolved`, `outcome_only_all`) are reported beside the primary with their differences, and do not set `view_sensitive`. `strength_graded_only` must reproduce run 2's primary fit; the report states whether it does.

### R7 — Per-commander "outcome minus p" has no source for the new rows (§7)

**Problem.** commander-ratings §7 takes p from the A–C strength-only fit in the estimate evaluation (`set3_ABC` in `ratings.py`), which has no grade E rows.

**Add to §7:**

> - The per-commander sum of outcome minus p uses, for p, the §5 held-out strength-only probability averaged over the M imputations.

### R8 — State what is superseded, and what grade E is not (header, §8)

**Problem.**

- **Superseded clauses.** The draft says it "extends" the accepted designs. It actually overrides clauses that say the opposite: strength-estimates §4 rule 8 ("There is no imputation") and §8 ("No imputation for grade D"; "No borrowing of strengths across engagements"), and commander-ratings §3/§5 (the verdict on the primary A–C rows only) and §4 (intervals "leave out … strength … uncertainty").
- **Era claim.** The draft cites ancient battles as the motive, but every predictor (US/CS, CWSAC theater, 1861–65 periods, CWSAC-listing echelons) is specific to this war. An era with almost no reported counts would have almost no training rows.

**Add after the paragraph "The reviewed v2 ledgers, run 2 …" in the header:**

> For grade E outputs and rating run 3 only, this design supersedes strength-estimates §4 rule 8 ("There is no imputation") and the §8 non-goals "No imputation for grade D" and "No borrowing of strengths across engagements", and commander-ratings §3's primary row set, §5's verdict configuration and §4's statement that intervals leave out strength uncertainty. The ledgers still record these sides as grade D; grade E lives only in `artifacts/strength-imputation-v1.json`. Run 2's verdict remains the record of run 2 and is not re-scored.

**Add to §8:**

> - Grade E borrows strength across engagements: each value is a typical size for sides that had a reported count, not an observation of this side. It is not an estimate layer entry, not an admitted feature and not historical adjudication.
> - The predictors are specific to this war and its CWSAC listings. A sparser era needs its own predictors, reference levels and training rows. With few reported counts, such a model has little to learn from and its ranges will be wide; this design does not show that it transfers.

## Advisories (not required)

- **A1 — Composition shift.** Training and target composition differ.

  | Group | Training rows | Grade D rows |
  | --- | ---: | ---: |
  | `corps_or_wing` | 15 | 40 |
  | `army` | 96 | 59 |
  | 1864–65 | 120 | 137 |
  | Eastern | 98 | 99 |

  Report this table in the output. One σ for all echelons assumes equal log-scale spread; report the leave-one-out error by echelon as well.
- **A2 — Selection, descriptive only.**
  - After the nested records are dropped, grade D sides are on the recorded winning side 130 times and the losing side 124 times; A–C sides 171 and 177.
  - In the 70 rows with exactly one grade D side, that side won 38 times and lost 32.
  - I computed these from the frozen `result` column without fitting anything. They show no large imbalance but do not rule out selection by size or fame.
  - I suggest the design declare this table as a fixed output. It is not a basis for changing any rule.
- **A3 — Leave-one-out calibration.** Leave-one-out by side can be optimistic when residuals cluster within campaigns. A leave-one-campaign-out coverage figure, reported beside k, would show this. Calibration uses sides with reported counts only; the design should say that k is calibrated on observed sides.
- **A4 — Mixed response.** The response mixes bases (engaged, effective, present for duty, present). It also includes 43 rule 4 opponent-only points, which carry the declared 3/4 and 1/2 conventions. Consider stating this in §2 and a view that trains on A–B sides.
- **A5 — Bound conflicts.** When bounds conflict, the swap rule narrows the range to [U, L]. That treats conflicting evidence as precise. Dropping both bounds is an alternative. Under R1 only KY005 US and VA022 US are affected.
- **A6 — Monte Carlo error.** With M = 20, report the verdict's two log-loss differences recomputed on imputations 1–10 and 11–20 as a descriptive Monte Carlo check. It is not part of the verdict.
- **A7 — Naming the point estimate.** "The reported θ mode is the mean of the M modes" is not a mode. Call it the pooled point estimate and say so in the outputs.
- **A8 — Transparency about timing.** The owner record shows the replacement was chosen after run 2's verdict was known, over the author's recommended option (add a second test). The design could say so. The record's "~290 battles" and the design's 301 rows refer to the same set.
- **A9 — Theater source.** Theater comes from `data/raw/cwsac_campaigns.csv`, not from the battles table. Name it in §2, and bind its hash in the checker and authorization.
- **A10 — Numerical fallback.** Specify a fallback for the case where the truncation interval has negligible mass under N(μ, (kσ)²), for example Φ(b) − Φ(a) < 1e-12 when an upper bound lies far below the modelled range. One option is a point at the nearer bound, labelled.
- **A11 — Manifest coverage.** The input manifest did not bind the two v2 ledgers, the registry or the accepted designs that this review was told to read. Their hashes are recorded above. Future design-review manifests should bind them.

## Finding IDs

Required: R1, R2, R3, R4, R5, R6, R7, R8. Advisories: A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11.
