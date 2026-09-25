# Strength ledger v2, batch 2 of 8: separate review

## Record

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a separate subagent with fresh context; the author's conversation was not an input.
- **Date:** 2026-09-25.
- **Prepared commit reviewed:** `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372` (previous `96110cf`).
- **Worktree / bundle commit:** `7f82df9eedc172090c62f5406f36906b356fa116`. Between `11d4bc3` and `7f82df9`, only review-bundle files (`assignment.md`/`inputs.json` for v2cmd-b1…b8 and v2est-b1…b2) changed. The worktree files read below are therefore identical to the prepared commit.
- **Assignment:** `assignment.md`, sha256 `e369e65d42e045c5d81e8c80f6792e12d60aa91882bd1f851577f172f1df397b` (matches).
- **Input manifest:** `inputs.json`, sha256 `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0` (matches).
- **Input hashes:** all 25 bound paths match their `inputs_sha256` values, both under `git show 11d4bc3:<path>` and in the worktree. There are no mismatches. The ledger is `data/estimates/side-strength-v2.json`, sha256 `e594047072a99c84e5239658df444f2946c945916d744de2ca6a82c8082629e8`.
- **Files outside the manifest:** the assignment asks me to read files that `inputs.json` does not bind: `docs/strength-estimates.md`, `docs/feature-admission-reported-strength.md`, `docs/ledgers-v2.md`, the owner decision JSON, `docs/research/strength-estimates-ledger-v1.md`, `generalship/estimates.py` and `generalship/estimates_v2.py`. I read them at the worktree commit. The ledger's own `bindings` pin the design, addendum, script, engine, cohort and owner decision, and `estimate-check` verified those bindings. `inputs.json` binds `docs/research/ledgers-v2.md`, while the assignment names the addendum `docs/ledgers-v2.md`. I read both.

## Checks run (offline)

- **`make check`:** exit 0; 143 tests, OK.
- **`python3 -m generalship estimate-check --ledger data/estimates/side-strength-v2.json`:**
  - 305 in scope, 79 out of scope.
  - Side grades A/B/C/D: 184/60/114/252.
  - Fit-eligible rows: set1_A 61, set2_AB 83, set3_ABC 130.
  - Rows excluded as `post_start_information`: 20.
- **Replay:** I re-ran the unchanged engine (`classify`, `estimate_side`, `estimate_row`, `nested_sets`) on in-memory copies of the entries, with each proposed correction applied. No primary artifact was modified. Every "result" figure below is the engine's output.

## Scope actually inspected

All 25 assigned engagements, both sides:

NM001, NM002, AR001, GA001, LA001, LA002, SC002, SC003, AR002, FL002, AR003, LA003, LA004, MO013, MO014, MO015, MO016, OK004, MO017, TX001, TX002, FL003, LA005, AR004, AR005.

For each engagement I checked:

- **Inputs:** every input's printed value, bounds, `printed_text`, basis, codes, `loss_timing`, `bound`, `reproduction_of` and `adjustments`, against:
  - the cited dossier quote;
  - the frozen CSV cell;
  - or the `livermore-transcription-v2` section.
- **Dossiers:** every citation of every `strength`-dimension claim in the bound dossier (all schema v1; no typed quantities) and the frozen CWSAC forces rows.
- **Wider passages:** the surrounding raw source text, where the coding depended on context:
  - Canby, Sibley, Scurry, Slough, Chivington and NPS for NM001–NM002;
  - Van Dorn for AR001;
  - Jones for GA001;
  - Hindman for AR002, AR003 and AR005;
  - Irwin and Breckinridge for LA003;
  - McNeil for MO013;
  - Mouton and Irwin for LA005;
  - Cooper and Blunt for OK004.
- **Livermore page images:** `data/raw/reported-strength-v1/livermore-p79.jpg`, `-p95.jpg` and `-p96.jpg`.
- **Livermore coverage:** I searched the Livermore OCR (inventory only) for 1861–62 entry headings. Only Pea Ridge and Prairie Grove match this batch, so no Livermore entry was missed.

I did not re-review the 91 carried-forward v1 entries, and I opened no new sources. A few cross-ledger greps (for "near N" wording and for `post_outcome_claim`) were used only to check consistency; the out-of-batch hits are reported as advisories, not reviewed.

## Outcome: corrections required

There are seven required findings, R1–R7. Applying all of them with the unchanged engine gives:

| Measure | Before | After |
| --- | --- | --- |
| Side grades A/B/C/D | 184/60/114/252 | 184/58/113/255 |
| set1_A rows | 61 | 61 |
| set2_AB rows | 83 | 81 |
| set3_ABC rows | 130 | 129 |
| Rows excluded as `post_start_information` | 20 | 19 |

The primary should check each finding against its passage before applying it.

### R1. NM001 US `us-sibley-6000`: "near 6,000" is a one-sided bound (range change)

- **Quote** (or9-sibley-new-mexico-selections-v1, §sibley-1862-02-22): "The force we had to contend against amounted to near 6,000 men."
- **Why it is wrong:** "near" here is the adverb "nearly". Tier-2 §3 item 4 lists "nearly" as a one-sided printed bound. In the same batch, OK004 `cs-blunt-near7000` ("which was near 7,000 men") is already coded `one_sided_bound`, `bound: upper`. The two opponent figures are coded inconsistently, and that changes a range.
- **Change:**
  - `codes`: `["adversary_or_hearsay_estimate", "one_sided_bound"]`
  - `bound`: `"upper"`
- **Result:** class C → bound. US stays C 2,500, but the range changes from (1,750–6,000) to (1,750–3,500), because `us-sibley-3500` now sets `high`. Labels and sets are unchanged.
- **Alternative:** if the primary instead adopts "near N = about N" as a declared extractor policy, the consistent fix is to OK004. There, `cs-blunt-near7000` would take `codes: ["adversary_or_hearsay_estimate"]` and `bound: null`, and the Confederate high would change from 6,000 to 7,000. One reading must be applied to both. See A1 for hits outside this batch.

### R2. NM002: the March 27–28 figures lack the time codes the entry applies to its other day-limited figures (both sides → grade D)

- **Frozen interval:** 1862-03-26 to 03-28.
- **How the entry already codes day-limited figures:**
  - Figures limited to March 26 are coded `partial_interval`: `us-chiv-418`, `us-nps-400`, `cs-nps-pyron`.
  - Two March 27–28 states are coded `post_engagement_state`: `cs-nps-1100` and `us-slough-1300`.
- **Figures left uncoded:** the other figures that describe only the March 27–28 phase carry no time code, or only one.
- **Quotes:**
  - NPS (nps-nm002-v1, Description): "No fighting occurred the next day as reinforcements arrived for both sides. Lt. Col. William R. Scurry's troops swelled the Rebel ranks to about 1,100 while Union Col. John P. Slough arrived with about 900 men. Both Slough and Scurry decided to attack and set out early on the 28th".
  - Scurry (§scurry-1862-03-31), reporting the March 28 action: "The enemy is now known to have numbered 1,400 men".
  - Slough (§slough-1862-03-29), on the 28th: "Learning from our spies that the enemy, about 1,000 strong, were in the Apache Canon"; "The strength of the enemy, as received from spies and prisoners, in the canon was altogether some 1,200 or 1,300".
  - Slough (§slough-1862-03-30), before the 28th advance: "his estimated strength was from 1,200 to 3,400".
- **Rule:** tier-2 §3 item 2 covers both cases. "A figure the source limits to part of a multi-day engagement interval (one day or phase) is excluded: partial_interval". A state dated after the start date is `post_engagement_state`.
- **Changes:**

  | Side | Input | New `codes` | New `bound` |
  | --- | --- | --- | --- |
  | US | `us-scurry-1400` | `["adversary_or_hearsay_estimate", "partial_interval", "post_engagement_state"]` | `"lower"` |
  | US | `us-nps-900` | `["derivation_unknown", "partial_scope", "post_engagement_state"]` | unchanged (`"lower"`) |
  | Confederate | `cs-nps-1100` | `["derivation_unknown", "partial_interval", "post_engagement_state"]` | `"lower"` |
  | Confederate | `cs-slough-1000` | `["adversary_or_hearsay_estimate", "partial_interval", "post_engagement_state"]` | `"lower"` |
  | Confederate | `cs-slough-1200` | `["adversary_or_hearsay_estimate", "partial_interval", "post_engagement_state"]` | `"lower"` |
  | Confederate | `cs-slough-range` | `["adversary_or_hearsay_estimate", "partial_interval", "post_engagement_state"]` | `"lower"` |

  `us-nps-900` is the arrival on the 27th, from the same NPS sentence as `cs-nps-1100`.
- **Result:**
  - **US** goes from C 1,050 (900–1,400) to **D**. Suggested `null_reason`: "No candidate value: every figure is limited to March 26 or to the March 27–28 phase, or is a partial or opponent bound."
  - **Confederate** goes from C 1,100 (770–2,300) to **D**, with the same reason.
  - **Row effect:** the row is no longer counted as excluded for `post_start_information` (20 → 19 excluded) and becomes incomplete. It was already outside every fit, so no fit row changes.
- **Minimal alternative:** if the primary rejects `partial_interval` for the March 28 figures, still add `post_engagement_state` to `us-scurry-1400` and `us-nps-900`. That gives US C 1,050 (**700**–1,400) with a `post_start_information` label, and the low no longer rests on a post-start arrival figure.

### R3. GA001 Confederate `cs-gillmore-385`: `post_outcome_claim` is misapplied (class change)

- **What the code means:** tier-2 §3 item 6 and design §3 row 1 give `post_outcome_claim` to a figure whose claim is tagged `post_outcome`. The cited claim `reported-force-scope` has `phase: "unresolved"`.
- **Quote** (or6-gillmore-fort-pulaski-selections-v1, §gillmore-1865-10-20-bombardment): "The garrison of the fort was found to consist of 385 men, including a full complement of officers."
- **Correct coding:** this is a count at the surrender, 1862-04-11. That is after the frozen start of 04-10.
- **Change:** `codes`: `["post_engagement_state"]`, so the input is class C instead of unusable.
- **Result:** no change to the estimate. It stays B 390 (330–700), because the post-start candidate is not used for the point or range. Keep the note that Jones's 385 is not shown to reproduce it.

### R4. LA003 Confederate `cs-irwin-2600`: the relay the ledger records is not linked (point, basis and range change)

- **What the ledger says:** its own note calls the input "Irwin (compiled, relaying Breckinridge)".
- **The passages match:**
  - Irwin (irwin-baton-rouge-selections-v1, §baton-rouge): "The Confederates went into action with about 2,600, without counting the partisan rangers and militia, numbering 400 or 500 more."
  - Breckinridge (§breckinridge-1862-09-30): "I did not carry into the action more than 2*,600 men. This estimate does not include some 200 Partisan Bangers … nor about the same number of militia".
  - Irwin's qualifier restates Breckinridge's. The printed value is the same, 2,600.
- **Rule:** design §4 rule 2 puts a recorded reproduction with the same printed value into one group. "If any member is … bound-only (§3 row 5), so is the group." Breckinridge's figure is `one_sided_bound`.
- **Change:** `reproduction_of`: `"cs-bk-2600"`.
- **Result:**
  - **Before:** A 2,600 (2,470–2,600), basis `reported_engaged`.
  - **After:** **A 3,000 (2,850–3,780), basis `reported_effective`**, from Breckinridge's "morning report of the 4th showing but 3,000 effectives". The label set gains `applicability_unresolved` from `cs-irwin-3600` in the range and loses `single_input`.
  - The row stays in set2_AB.

### R5. AR001 Confederate `cs-lv`: Livermore's 14,000 is sourced to Van Dorn's "less than 14,000" (grade change)

- **Livermore p.79** (page image `livermore-p79.jpg`): "Van Dorn's command, about ² 14,000 ᶜ", with source note "ᶜ 8 W. R., 285".
- **Van Dorn, p.285** (dossier citation 10, `cs-vd-14000`, loc p.285): "The force with which I went into action was less than 14,000 men."
- **What the ledger misses:** the transcription omits the source line, so the dependence is not recorded.
- **Precedent:** v1 links a Livermore figure to the OR figure it reproduces (TN003 `cs-lv-eff` → `cs-return-before`; TN002 `us-lv` → `us-final`).
- **Rule:** under design §4 rule 2, the group formed with the bound becomes bound-only. Through the NPS/Livermore equality link, that group also contains `cs-nps`.
- **Change:** `reproduction_of`: `"cs-vd-14000"`.
- **Result:**
  - **Before:** B 14,000 (11,900–25,000).
  - **After:** **C 16,000 (11,200–25,000)**, basis unknown, from Van Dorn's "The whole force under my command was about 16,000" (`engagement_link_unknown`). Labels: `applicability_unresolved`, `basis_mixed`, `whole_engagement_leakage`.
  - The row leaves set2_AB and stays in set3_ABC.
- **Inventory:** extend the Livermore `reason` to record the source note and the link.

### R6. AR005 Confederate `cs-lv`: Livermore's 10,000 is sourced to Hindman's "less than 10,000" (grade change)

- **Livermore p.95** (page image `livermore-p95.jpg`): "1st corps trans-Mississippi army . . . ⁴ 10,000 ᶜ", with source note "ᶜ 32 W. R., 140". Note 4 reads: "Possibly 700 to 1000 should be added for officers."
- **Hindman** (or22-1-hindman-prairie-grove-selections-v1, dossier citation 6, loc p.140; OR vol. 22 pt. 1 is serial 32): "These aiM rangements left me for the fight less than 10,000 men of all arms." This is `cs-hind-lt10000`, `one_sided_bound`.
- **What the ledger says:** the inventory calls this "may relay … its source line is not transcribed (judgment call)". The registered page image resolves it: the page carries the source line.
- **Change:** `reproduction_of`: `"cs-hind-lt10000"`.
- **Result:**
  - **Confederate** goes from B 10,000 (8,500–10,000) to **D**. Suggested `null_reason`: "No candidate value: Livermore's 10,000 reproduces Hindman's 'less than 10,000' (bound only); the other figures are marching components or an opponent's one-sided estimate."
  - **US** is unchanged at B 10,000 (8,500–11,500) and loses `basis_mixed`.
  - The row leaves set2_AB and set3_ABC and becomes incomplete.
- **Inventory:** update the Livermore `reason`.

### R7. LA005 `cs-mouton-1000` and `us-mouton-close`: a same-day state is coded as post-start (class change)

- **Quote** (or15-mouton-la-fourche-selections-v1, §mouton-1862-11-04): "and at the close of the day the force of the enemy numbered about 2,000 infantry, 100 cavalry, and a battery, while my own barely reached 1,000".
- **Why it is wrong:**
  - The day is 27 October, which is the frozen start and end date (1862-10-27).
  - `post_engagement_state` needs a state date after the start date (tier-2 §3 item 2).
  - The figure is limited to part of the one-day interval, the close of the day.
- **Changes:**
  - `cs-mouton-1000`: `codes` `["partial_interval"]`, `bound` `"lower"`. Its class changes from C to bound.
  - `us-mouton-close`: `codes` `["adversary_or_hearsay_estimate", "partial_scope", "partial_interval"]`. It is already a bound.
- **Result:** no change to either estimate: US A 4,000 (3,800–4,200), Confederate A 1,390 (1,320–1,460).

## Advisories (no required change)

- **A1. "near N" outside this batch.** The same reading question as R1 applies to:
  - FL005 US `us-seymour` ("The entire force near 5,500"), coded as a point;
  - MO010 Confederate `cs-prentiss-900` ("numbering near 900 men");
  - NC020 US `us-johnston-44000` ("amounting to near 44,000").

  I did not review these. The primary should apply one reading across all batches.
- **A2. `post_outcome_claim` outside this batch.** The code is also used, apparently for surrender or after-action counts on claims with `phase: "unresolved"`, in:
  - AR009 `cs-after`;
  - GA028 `cs-hazen-garrison`;
  - KY011 `us-morgan-hobson`;
  - LA010 `cs-prisoners`.

  These are not reviewed here; see R3.
- **A3. MO015 `cs-britton-3000`.** Britton's sentence "of not less than three thousand men, with his little command of seven hundred and forty men" repeats both of Foster's own report figures ("about 3,000 strong"; "about 740 men"). Under tier-2 §3 item 3, it is arguably visibly Foster's (opponent) estimate. If it is recoded `adversary_or_hearsay_estimate`, the bound no longer applies and `bound_conflict` drops. The point stays at 2,250. The judgment call is recorded in the ledger.
- **A4. FL003 US and LA005 Confederate: frozen figures that equal an OR total.**
  - **FL003:** the frozen 1,573 equals Brannan's "Total 1 573". The rationale calls it "Brannan's printed total".
  - **LA005:** the frozen 1,392 equals Mouton's return total. The rationale says "is Mouton's return total".
  - **Linking:** neither is linked. That is consistent with v1's practice of not linking on equal value alone. Linking would group an engaged-basis cell with an effective-basis or unknown-basis figure, and both sides would fall from A to B.
  - **Suggestion:** reword the rationales to "equals" unless a passage shows derivation.
- **A5. MO014 and MO017: frozen numeric bounds equal the frozen casualty figures.** MO014 has 344 = 344 against the text's "approx. 300"; MO017 has 113 = 113 against "approx. 100". Both are entered as A candidates beside the text value, and the lower median limits their effect (points 310 and 100). The notes record the anomaly; keep it visible.
- **A6. NM002 `cs-slough-range` "1,200 to 3,400".** This is an unverified OCR reading, and it currently sets the Confederate high of 2,300. The point is moot if R2 is applied.
- **A7. NM001 NPS cells.**
  - The dispute over the cells' side assignment is coded `scope_unresolved`. No tier-2 code describes side attribution, and any row-4 code gives the same class.
  - The Confederate B 2,500 lies above Sibley's own "did not exceed 1,750 on the field" (`bound_conflict`). This is a declared consequence (design B3), not an error.
- **A8. Estimates that sit oddly against their inputs** (engine consequences, not coding errors):
  - MO016 Confederate C 5,250 (¾ of the prisoners' hearsay 7,000) against Cooper's own "did not exceed 4,000" (`bound_conflict`);
  - MO015 Confederate C 2,250 against Britton's "not less than three thousand" (see A3);
  - TX001 Confederate A 60 from the frozen 55, whose own cell text puts 25 of them "3 1/2 miles away". Tier-2 §3 item 1 accepts a side-level table entry as whole-side scope.
- **A9. Minor inventory gaps.** Some sub-figures inside cited quotes are not named individually. All are parts or components, so none could change an estimate:
  - NM001 citation 8: "l,20p [1,200] of whom were old regulars";
  - SC002 citation 4: divisional components 3232, 4313 and 1927 of `us-jones-9472`;
  - LA003 citation 16: "3,200" (earlier strength) and citation 14's "400 or 500 more".

  Adding one-line reasons would match the style of the other entries.
- **A10. AR002 Confederate completed sum.** C 110 is the sum of 79 + 35. It rests on Hindman, who was not present and wrote in 1863, presenting these as the whole defence. The frozen row's "fifty men and C.S. boats" suggests a different composition. This is recorded as a judgment call and is acceptable at grade C.

## Engagements with no required correction

The inputs, codes, inventory and replayed estimates were confirmed as recorded for:

- SC002, SC003, AR002, FL002, AR003;
- LA001, LA002, LA004;
- MO013, MO014, MO015, MO016, OK004, MO017;
- TX001, TX002, FL003, AR004.

OK004 depends on R1's consistency choice.

The recorded reasons for the grade D sides are accurate, and no usable figure was missed in the inspected sources:

- GA001 US;
- LA001 both sides;
- LA002 US;
- SC003 both sides;
- AR002 US;
- FL002 both sides;
- AR003 US;
- LA004 both sides;
- OK004 US;
- TX001 US;
- TX002 both sides;
- FL003 Confederate.

## Limits

This is a separate AI review: an analysis of the recorded inputs against the accepted rules within the scope stated above. It is not:

- human historical adjudication;
- proof of source independence;
- feature admission;
- authorization of any fit.

The OR and NPS passages were read as OCR text, not checked against print. The Livermore figures were checked against the registered page images named above. Findings R1–R7 are proposals for the primary to verify against the passages before any change to the ledger.
