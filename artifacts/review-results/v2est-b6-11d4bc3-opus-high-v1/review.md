# Strength ledger v2, batch 6 of 8: separate review

**Outcome: corrections required** (B6-R1 to B6-R5; advisories B6-A1 to B6-A10).

## Reviewer record

| Field | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. I ran as a subagent with fresh context and did not see the author's conversation. |
| Date | 2026-09-25 |
| Prepared commit under review | `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372` (against `96110cf`) |
| Worktree HEAD (bundle commit) | `fde28f09c15ab878b6543ac96e7839a6eeb6da85`. `git diff 11d4bc3 HEAD` adds only review-bundle `assignment.md`/`inputs.json` files. |
| Assignment | `assignment.md` sha256 `6ca0b42158d293e76a98d61c73a22e21a299fa77d294b508095931f176925005` (matches) |
| Input manifest | `inputs.json` sha256 `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0` (matches) |
| Bound inputs | All 25 paths in `inputs.json` match their hashes at `git show 11d4bc3…:<path>` and in the worktree. No mismatches. |
| Other files read (not in the manifest) | `docs/strength-estimates.md` `795212ad…ba3`; `docs/ledgers-v2.md` `a7e05ddf…9eb1`; `docs/feature-admission-reported-strength.md` `0699152d…c48`; `data/estimates/owner-decision-v2-sources-2026-09-25.json` `28da7610…89e9`; `docs/research/strength-estimates-ledger-v1.md` `9d9f7d30…920cf`; `generalship/estimates.py` `af540a92…32f`; `generalship/estimates_v2.py` `368c5052…43a`; `data/pilot/cohort-v2.json` `614f6c9b…6f9`. Every file the ledger binds matches its `bindings` hash. |
| Checks run offline | `make check`: exit 0, 143 tests OK. `python3 -m generalship estimate-check --ledger data/estimates/side-strength-v2.json`: passes. It reports in scope 305, out of scope 79, grades A/B/C/D 184/60/114/252, fit-eligible rows set1/set2/set3 61/83/130, and 20 rows excluded as `post_start_information`. I ran no build or packet commands and did no network or new research. |

Manifest note: the assignment names `docs/ledgers-v2.md`, but `inputs.json` binds `docs/research/ledgers-v2.md` (`e9986d9b…085030`) instead. I read both. The addendum `docs/ledgers-v2.md` is the file the ledger binds.

## Scope actually inspected

**Ledger entries.** All 24 assigned engagements (GA007, GA009, GA010, GA011, GA012, GA014, GA015, GA016, GA017, GA018, GA020, GA021, GA022, MS014, MS015, TN031, KY011, MD007, DC001, VA114, VA115, VA116, WV013 and AL003), both sides of each. For each input I checked:
- its codes, basis, `loss_timing`, `bound` and `reproduction_of`;
- its class, the estimate, the side's null reason and the rationale;
- the engagement's inventory.

**Dossier passages.** I read the `strength` claims (value and rationale) and every citation quote in all 24 bound dossiers. For every figure that sets or bounds an estimate, I also read the surrounding passage through `citation_text`. That covered GA007 [2–4, 7, 10], GA009 [4], GA010 [8], GA016 [3–5], GA020 [3, 6, 7], GA021 [2, 4], MS014 [2, 4, 11–13], MS015 [2, 5, 7], KY011 [2, 8, 12], MD007 [10], DC001 [3] and VA115 [2, 4, 6].

**Frozen CSV cells.** I checked the `cwsac_battles`/`cwsac_forces` rows for all 24 engagements. Seven cells carry figures: MS014 US 8,500; MS015 US 14,000; TN031 CS 400; VA114 5,000 and 8,000; VA116 10,000 and 13,000. All are inventoried and read correctly.

**Livermore.** I read `livermore-transcription-v2` sections p109–p139 in full and checked them against the scoped engagements. I viewed page images `livermore-p115`, `p120`, `p121`, `p122` and `p125`. I did not view p119, p123, p124 or p126; for those pages I relied on the transcription. No registered page carries an entry for GA014, GA020, GA021, MS014, TN031, KY011, MD007, DC001, VA114–VA116, WV013 or AL003. Unregistered pages were out of scope.

**Completeness scan.** I compared every number in each strength claim against the inputs, inventory text and null reasons. The only figures not accounted for were:
- gun counts;
- NPS/CWSAC two-side totals, which are covered as the "same frozen figures";
- two component lines in GA007 (B6-A6);
- one uncited figure in the MS014 claim text (B6-A5).

**Correction replay.** I applied B6-R1 to B6-R5 to an in-memory copy of the ledger and replayed it with the unchanged engine and `estimates_v2.check`. It passes, with the results given below. No file was written.

## Required corrections

### B6-R1: GA015 Kennesaw Mountain, both sides: the Livermore figures are a part of the side (`partial_scope`), not `scope_unresolved`

- **Inputs and exact change.** `us-lv-engaged`, `us-lv-eff`, `us-lv-pfd`, `cs-lv-engaged`, `cs-lv-eff` and `cs-lv-pfd`: in each, replace `scope_unresolved` with `partial_scope`, set `bound` to `"lower"` and set `class` to `"bound"`. The resulting codes are:
  - `us-lv-engaged` and `cs-lv-engaged`: `["derived_from_losses", "partial_scope"]`, with `loss_timing` still `not_prior`;
  - the four `-eff` and `-pfd` inputs: `["partial_scope", "post_engagement_state"]`.
- **Evidence.**
  - Livermore p.120 note 7, confirmed on the page image: "The attempt here is to state the numbers of the troops that moved out of the works … The troops on both sides all along the line, and the Army of the Ohio in another field far to the right, engaged the enemy, but did not take part in the assault."
  - Livermore p.121 note 1: "about one half their divisions engaged in the repulse."
  - Both frozen sides are whole armies ("Military Division of the Mississippi [US]; Army of Tennessee [CS]").
- **Why the code changes.** The source itself presents its figure as one part of each side's force that engaged that day. Tier-2 §3 item 1 codes that `partial_scope`. `scope_unresolved` applies only "when the cited passages do not settle" the question. The ledger already codes assault-only Livermore subsets `partial_scope`: LA010 `us-lv-june14` and VA072 `cs-lv`.
- **Contrast with GA016–GA018.** Those entries keep Livermore's engaged-formation entries as whole-side, and that treatment is consistent with tier-2 item 1. GA015 differs because Livermore's note says other troops engaged.
- **Result.** Both sides become grade D (null). `nested` becomes `{"sets": [], "excluded_post_start_information": false}`.
- **Null reasons to add.**
  - US: "No candidate value. Livermore's Kennesaw figures (16,225 engaged; 14,174 effectives; 15,241 present for duty, from June 30 returns) cover the assaulting troops only; his note 7 says troops all along the line and the Army of the Ohio also engaged the enemy (bounds only; post-start figures, not applied)."
  - Confederate: "No candidate value. Livermore's 17,733 engaged, 17,301 effectives and 18,604 present for duty (June 30 returns) cover the divisions facing the assault, with half of French's and Walthall's (note 1); note 7 says troops on both sides all along the line engaged (bounds only; post-start figures, not applied)."
- **Rationale.** Update it to match.
- **Effect on fits.** None. The row was already excluded as `post_start_information`. The count of excluded rows falls from 20 to 19.

### B6-R2: GA022 Jonesborough, Confederate: the August 31 entry is a one-day figure (`partial_interval`)

- **Inputs and exact change.** `cs-lv-aug31-eff` and `cs-lv-aug31-pfd`: set `codes` to `["partial_interval"]`, `bound` to `"lower"` and `class` to `"bound"`.
- **Evidence.**
  - Livermore p.125 heading, confirmed on the page image: "JONESBOROUGH, GA., AUGUST 31, 1864."
  - The frozen interval is 1864-08-31 to 1864-09-01.
- **Why the code changes.** Tier-2 §3 item 2 says: "A figure the source limits to part of a multi-day engagement interval (one day or phase) is excluded: partial_interval." The rules make no exception for a day whose force contains the next day's force. The ledger note builds that exception from a second entry (p.126, Hardee's corps alone on September 1), so it is our inference, not the source's.
- **Precedents.** The ledger codes other day-only or phase-only Livermore entries `partial_interval` even when the result is a weaker estimate: NC020 `us-lv` and `cs-lv`, SC007, VA062 and MS011. If the owner wants a superset exception, it needs a design revision, not a case-by-case coding.
- **Result.** The Confederate side becomes grade D (null). `nested` is unchanged (`[]`; the Union side is already D).
- **Null reason.** "No candidate value. Livermore's August 31 entry (Lee's and Hardee's corps: 25,604 present for duty, 23,811 effectives) and September 1 entry (Hardee's corps: 14,071 present for duty, 13,086 effectives, 12,661 after August 31 losses) each cover one day of the two-day record (bounds only)."
- **Other text.** In the rationale, drop "which include the September 1 force". In the `cs-lv-aug31-eff` note, drop "so the August 31 figure covers the side over both days".

### B6-R3: MS015 Tupelo, Union: Livermore's 14,000 reproduces Smith's figure

- **Input and exact change.** `us-lv`: add `"reproduction_of": "us-smith"`.
- **Evidence.**
  - Livermore p.121, confirmed on the page image: "A. J. Smith's command, about [2] 14,000".
  - Note 2: "The Records do not afford the means of determining whether this number, as given by General Smith, includes only effectives."
  - Smith (dossier citation 5): "the aggregate of which was about 14,000 men."
- **Why the link is needed.** The values are the same and the source names Smith as the origin, so design §4 rule 2's reproduction link applies. The ledger links other relays the same way: AL002 `us-rawlins`→`us-dodge-100`, LA012, LA019, VA111, and v1 TN003 `cs-lv-eff`→`cs-return-before`.
- **Result.** The dependence group becomes {`us-cw`, `us-lv`, `us-nps`, `us-smith`}. The union of its conditions includes `engagement_link_unknown`, because `us-smith` is the aggregate on leaving La Grange on July 5.
  - **Old estimate:** US B 14,000 (11,900–19,000).
  - **New estimate:** US C 14,000 (9,800–19,000), basis `unknown`. Labels are unchanged: `applicability_unresolved`, `basis_mixed`, `compiled_dependence`, `derivation_unknown` and `whole_engagement_leakage`.
  - **Row sets:** `nested.sets` becomes `["set3_ABC"]`, losing `set2_AB`. The set2 fit-eligible count falls from 83 to 82.

### B6-R4: KY011 Cynthiana, Confederate: Morgan's cap covers the 12th and the engaged part only

- **Input and exact change.** `cs-morgan-cap`: set `codes` to `["one_sided_bound", "partial_interval", "partial_scope"]` and `bound` to `null`.
- **Evidence.** The passage around citation 12 reads: "The next morning (12th instant) we were attacked by 5,200 … My command engaged did not exceed 1,200 men, as a large detail had to be made to guard prisoners and protect wagon train, and also detachments destroying the two lines of railroad."
- **Why the coding changes.** The record runs June 11–12, and Morgan's command also fought on the 11th. A cap on one day's engaged part does not cap the whole side. The ledger's own policy is that such caps take `bound: null`. The exact precedent is AL004 `us-doolittle-500` ("less than 500 actually fighting on the first day"), coded `["one_sided_bound", "partial_interval", "partial_scope"]` with `bound: null`.
- **Result.**
  - **Old estimate:** Confederate B 1,200 (1,020–1,200).
  - **New estimate:** Confederate B 1,200 (1,020–5,000). The high now comes from `cs-burbridge-5000` under rule 5, because the cap no longer lowers it. Labels are unchanged. `nested` is unchanged (`[]`; the Union side is D).
- **Note to update.** Change the `cs-morgan-cap` note to say the cap covers the 12th only, with details detached.

### B6-R5: MD007 Monocacy, Confederate: Wallace's 18,000 is for the left bank only

- **Input and exact change.** `cs-wallace-18000`: set `codes` to `["adversary_or_hearsay_estimate", "partial_scope"]`, `bound` to `"lower"` and `class` to `"bound"`.
- **Evidence.** Citation 7: "By calculation this would give him about 18,000 men engaged on the left bank, while he had at least 2,000 more skirmishing and fighting in my front across the river." The same sentence presents the 18,000 as one part of the force engaged.
- **Result.** The input changes class (C to bound). The estimate is unchanged: Confederate C 17,000 (11,900–22,100) from `cs-pond`. The opponent candidate was being dropped from the point anyway, and its basis kept it out of the range.

**Aggregate effect of R1–R5**, replayed in memory with the unchanged engine and checker:

| Measure | Before | After |
| --- | --- | --- |
| Side grades A/B/C/D | 184/60/114/252 | 183/59/113/255 |
| Fit-eligible rows set1/set2/set3 | 61/83/130 | 61/82/130 |
| Rows excluded as `post_start_information` | 20 | 19 |

## Advisories (no required change)

- **B6-A1: GA016 `us-lv-eff-p121` (20,139).** The p.121 image confirms that this line is printed at the foot of the Tupelo Confederate entry. It equals 93 per cent of the Peach-Tree Creek Union 21,655, so it almost certainly belongs to that entry. Even so, the link is inferred, not printed, so `engagement_link_unknown` (class C) is defensible. If the primary instead treats the arithmetic as establishing the link, the input becomes class A `reported_effective`. It would then set the Union point at 20,140 (effective) and remove `basis_mixed` from the row. This is a judgement for reconciliation, not a coding error.
- **B6-A2: TN031 Memphis, Confederate point 400.** This is mechanically correct: it is the lower middle of the frozen "approx. 400" and the NPS cell's 2,000, and the extraction record already reports it. The same NPS page describes 2,000 as the force Forrest set out with, which then "lost about a quarter of his strength". Coding `cs-nps-table` as `engagement_link_unknown` would therefore be arguable, but it would not change the point, range or labels. The row sits in set1_A with a point far below every other figure (Jordan 1,500; Washburn 2,500–3,000). That is a result to report, not an input error.
- **B6-A3: GA018 wording.** The rationale says Loring's division is one "which Cox has engaged". Cox's cited sentence says Loring's and Walthall's divisions were withdrawn "to support General S. D. Lee". Suggested wording: "which Cox has sent to support Lee". The `scope_unresolved` code stands.
- **B6-A4: GA020 `cs-steedman-6000`.** "Wheeler's command was not less than 6,000 strong, moving in detachments" is the whole raiding command, so it is larger than the Dalton force, not a part of it; Steedman gives the Dalton attackers as 3,000. `scope_unresolved` (or `other_engagement`) with `bound: null` would describe it better than `partial_scope` with `lower`. The estimate is unaffected.
- **B6-A5: MS014 inventory.** The claim value says Forrest's orders were to move "with 2,000 of his own men and 1,000 of Roddey's", but no dossier citation carries that quote, so it can be neither an input nor seen by the checker. Suggestion: add an inventory reason, such as "planned force named in the claim text; no cited quote; not entered".
- **B6-A6: GA007 inventory.** Some figures in the claim and its citations are not named in the inventory:
  - the components "4,527 48,465" of the entered 52,992 line (citation 6);
  - the gun counts (254, 130, 96, 28);
  - Johnston's statement that Wheeler's 2,200 met "more than double that number" (a partial opponent figure).

  Suggestion: add them to the reason string. No estimate changes.
- **B6-A7: GA016 and GA017 Confederate ranges.** The highs (53,480 and 51,190) come from rule 5's hull, which admits lower-class, scope-unresolved whole-army effective figures (Hood's 48,750; Cox's 50,932). This is mechanical and not an error. It is worth reporting because each range then spans both the engaged-subset and the whole-army populations.
- **B6-A8: GA017 Confederate `cs-lv-eff`.** Livermore's note 3 says the July 10 total "should be reduced by the casualties between July 10 and 22", but no reduction is printed. `loss_timing: none` and class A are therefore correct under the rules. The source is signalling that the figure somewhat overstates the force brought.
- **B6-A9: Grade D sides confirmed.** I found no usable figure missed in the inspected sources, and the recorded reasons are accurate, for these sides:
  - GA009, GA010, GA011 and GA012: US and CS;
  - GA014, WV013 and AL003: both sides;
  - GA022, KY011 and MD007: US;
  - DC001: CS.

  Barnard's footnote in the DC001 passage also gives effectives north and south of the Potomac (1,819, 1,834, 63; 4,064, 1,772, 51). These are parts of the 20,400 and fall outside the claim and quote. `scope_unresolved` on `us-pond-available` is right, because the figure both includes troops south of the Potomac and excludes the Sixth Corps.
- **B6-A10: Entries verified without finding.** I verified the passages, values, `printed_text` and coding of GA007, GA016 (apart from A1), GA017, GA020, GA021, MS014, VA114, VA115 and VA116. That includes:
  - the GA007 completed sums (Cox's three armies, "Of these"; Johnston's infantry-artillery plus cavalry);
  - the VA115 Averell sum and the application of the 2,350 lower bound;
  - the MS014 and TN031 opponent raises of `high`;
  - the GA020 and VA115 rule 4 points.

## Limits

This is an AI review. It is a separate analysis of whether the recorded inputs follow the accepted rules. It is not historical adjudication, independent corroboration, feature admission or authorization of any fit. Where I relied on the transcription instead of the page image (p119, p123, p124, p126), a transcription error would not have been caught. The primary should check each required finding against its passage before applying it.
