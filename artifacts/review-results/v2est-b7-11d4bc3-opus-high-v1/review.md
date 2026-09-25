# Strength ledger v2, batch 7 of 8: separate review

**Outcome: corrections required** (F1 changes one range and one label; F2 is a text-only fix).
Findings: F1, F2 (required); A1–A4 (advisory).

## Reviewer record

| Item | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), effort `high`, a fresh-context subagent. I did not see the primary's conversation. |
| Date | 2026-09-25 |
| Assignment | `assignment.md` sha256 `40189f732dad0169018c08e8cd70fcf1b32937037947d2752b8d58e70d7568d1` (verified) |
| Input manifest | `inputs.json` sha256 `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0` (verified) |
| Prepared commit | `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372` (compared against `96110cf`) |
| Worktree HEAD | `fe948a6e949e8d7b0fff25479bc9e64263ef8647`. Relative to `11d4bc3`, it adds only review-assignment bundles. |
| Input hashes | All 25 paths in `inputs.json` match `git show 11d4bc3:<path>`, and the worktree copies are byte-identical. No mismatch. |
| Ledger | `data/estimates/side-strength-v2.json` sha256 `e594047072a99c84e5239658df444f2946c945916d744de2ca6a82c8082629e8`, status `extracted_not_reviewed_not_fitted` |
| Ledger bindings | I confirmed these by sha256: design `795212ad…`, addendum `docs/ledgers-v2.md` `a7e05ddf…`, engine `af540a92…`, script `368c5052…` and owner decision `28da7610…`. The dossier and source bindings of the 25 engagements pass `estimate-check`. |

The assignment names the addendum `docs/ledgers-v2.md`, which is the file the ledger binds and the one I read.
`inputs.json` instead binds `docs/research/ledgers-v2.md`, the extraction record; I skimmed that file only.
This is a naming difference only. The hashes of both files agree with their bindings.

**Checks run (offline).**

- `make check`: exit 0.
- `python3 -m generalship estimate-check --ledger data/estimates/side-strength-v2.json`: exit 0. It reports:
  - 305 engagements in scope and 79 out of scope;
  - side grades A 184, B 60, C 114, D 252;
  - fit-eligible rows: set1 61, set2 83, set3 130;
  - 20 rows excluded as `post_start_information`;
  - `fitted: false`.

I ran no build or packet commands and modified no primary artifact. This file is the only one I wrote.

## Scope actually inspected

I read the following:

- AGENTS.md;
- design `docs/strength-estimates.md` §§1–7;
- tier-2 §3 of `docs/feature-admission-reported-strength.md`;
- `docs/ledgers-v2.md`;
- the owner source decision;
- the ledger's `constants` and `extractor_policies`;
- `generalship/estimates.py` and `generalship/estimates_v2.py` in full.

I skimmed the v1 ledger memo for its policies only.

For each of the 25 engagements I did the following:

- **Ledger entry.** I read both sides' inputs, estimates, null reasons, inventory, rationale and nested sets.
- **Dossier.** I read every citation of each `strength` claim. No batch dossier has typed quantities.
- **CWSAC.** I read the frozen CWSAC forces row.
- **Surrounding text.** I opened the resolved source text around each quote that is an input or that the inventory sets aside. This covered Pond, Early, Price, Britton, Burbridge, A. E. Jackson, Corse, French, Granger, Doolittle, Sinclair, Breckinridge, Gillem, Cox, Hood and NPS.
- **Livermore transcription.** I read the `livermore-transcription-v2` sections p127–p133.
- **Livermore page images.** I compared six page images against the transcription: p127, p129, p130, p131, p132 and p133. Every figure used as an input and every figure listed in the inventory reasons matches the image. That includes the point-setting totals 27,939 and 26,897 (Franklin) and 49,773 and 23,207 (Nashville).

For the batch engagements that the ledger records as having no Livermore entry, I searched the normalized Livermore OCR and the v2 transcription for the engagement names. That was a search only, not a citation. Livermore has entries for Opequon, Cedar Creek, Franklin and Nashville only. The ledger's `livermore: null` entries are therefore accurate.

I replayed the proposed corrections and the advisory alternatives with the unchanged engine, in memory only.

I did not inspect the following:

- the 91 carried-forward v1 entries, which are out of scope;
- other batches;
- page images for pages that carry no batch figure.

I did no new research and consulted no source outside the bound inputs.

## Required corrections

### F1. GA023 (Allatoona), US: Corse's two figures cover only the infantry

In the ledger, `us-corse-1500` and `us-corse-1944` are class B, with codes `[]` and basis `unknown`. Both therefore enter the Union range, and `us-corse-1500` sets `low`.

The cited passages show that neither figure covers the whole side:

- **`us-corse-1500`** (citation 3, Oct. 7). The quote is "I brought about 900 mus¬ kets with ]ne. Colonel Tourtellotte had about 600, making in all about 1,500." A total of muskets counts the infantry only. The ledger codes other musket and bayonet figures `partial_scope`: AL005, DC001, GA012, LA002, VA007, VA122 `cs-early-6000`, and others.
- **`us-corse-1944`** (citations 4–5, Oct. 27). The garrison is listed as "Fourth Minnesota Infantry, 450 men; Ninety-third Illinois Infantry, 290 men; seven companies Eighteenth Wisconsin Infantry, 150 men; Twelfth Wisconsin Battery, 6 guns … furnishing a force of 890 men". Then comes the detachment, all infantry, with "total 1,054, making an aggregate of 1,944."
  - 450 + 290 + 150 = 890 exactly, so the listed Twelfth Wisconsin Battery has no men in the aggregate.
  - The 1,944 is therefore a sum of components that the passage shows does not cover the whole force (design §3 row 5; tier-2 §3 item 1, "the infantry alone").

The corrections are exact:

| Input | Field | Now | New |
| --- | --- | --- | --- |
| GA023 US `us-corse-1500` | `codes` / `bound` / `class` | `[]` / `null` / `B` | `["partial_scope"]` / `"lower"` / `bound` |
| GA023 US `us-corse-1500` | `note` | … | "Corse's October 7 'about 900 muskets' brought plus Tourtellotte's 'about 600': infantry muskets only" |
| GA023 US `us-corse-1944` | `codes` / `bound` / `class` | `[]` / `null` / `B` | `["partial_scope"]` / `"lower"` / `bound` |
| GA023 US `us-corse-1944` | `note` | … | "Corse's October 27 aggregate: garrison infantry 890 (450 + 290 + 150; the Twelfth Wisconsin Battery is listed with 6 guns and no count) plus the detachment's infantry 1,054" |

The replayed result changes as follows. Neither bound applies, because each has basis `unknown` and the point basis is `reported_engaged`.

| GA023 US | Now | Corrected |
| --- | --- | --- |
| grade / point | A / 1940 | A / 1940 (unchanged) |
| low / high | 1430 / 2040 | **1850** / 2040 (exact `9234/5`, `10206/5`) |
| labels | `compiled_dependence`, `derivation_unknown`, `whole_engagement_leakage` | adds **`single_input`** |
| range_groups | `us-corse-1500`, `us-corse-1944`, `us-cw` | `us-cw` |
| nested | set1_A, set2_AB, set3_ABC | unchanged |

**Rationale.** Replace it with: "Frozen CWSAC figures on the engaged basis (NPS repeats them). Corse's own 1,500 muskets and 1,944 aggregate count the infantry only; they are lower bounds on an unstated basis and do not apply to the engaged point."

The inventory line for the 890 and 1,054 components can stay as it is.

### F2. VA076 (Saltville), Confederate: the grade D reason and one note misattribute sources

This finding is text only; grade D is unchanged. The null reason says "Burbridge's figures are prisoners' reports". That is true of the October 7 dispatch ("From pris¬ oners I learn the enemy's force was between G,0()0 and 8,000"). The October 10 dispatch gives no source: "we had a heavy engagement with from 0,000 to 10,000 rebels". Its figure is Burbridge's own estimate of the enemy.

The `cs-burbridge-breck` note also quotes "'it is said'". That phrase belongs to the preceding list of commanders ("under Echols, Williams, Vaughn, and, it is said, Breckinridge"). The 4,000 comes from prisoners ("From pris¬ oners I learn … that Breckinridge was present with 4,000 from Lynchburg"). Both inputs remain correctly coded `adversary_or_hearsay_estimate`.

- **VA076 Confederate `null_reason`** becomes: "No candidate value: Burbridge's enemy figures are opponent estimates whose lower ends are unreadable in the OCR (October 7, from prisoners, 'between G,0()0 and 8,000'; October 10, his own, 'from 0,000 to 10,000'). Only the upper ends 8,000 and 10,000 are recorded, as bounds. The 4,000 with Breckinridge is a prisoners' report for one part, and Jackson's 300 is one reinforcement."
- **VA076 Confederate `cs-burbridge-breck` `note`** becomes: "prisoners' report relayed by Burbridge that Breckinridge was present with 4,000 from Lynchburg; one part".

## Advisories (no required change)

- **A1. TN034 and TN038, Confederate: coding of the Hood addenda table.** Both engagements use the same table of the Army of Tennessee's strength on November 6 and December 10 (TN034 `cs-hood-30600`, TN038 `cs-hood-23053`).
  - **What the table's arithmetic shows.** The first column sums exactly: 25,889 + 2,306 + 2,405 = 30,600, and 18,342 + 2,306 + 2,405 = 23,053. The totals increase across the row (30,600 < 40,730 < 44,719 < 88,793 < 96,367), and the OCR header lists "Effective". Together these support the reading in the reviewed dossiers ("an effective total of 30,600 on November 6", "an effective total of 23,053 on December 10").
  - **What the ledger says instead.** Its inventory says the column alignment "is unreadable", and both inputs have basis `unknown`.
  - **The scope question.** The November 6 cavalry line is 2,306 (it reads the same on December 10). Cox, cited in the same claim, says Forrest joined about November 15. The ledger codes the parallel Cox figure for November 6, `cs-cox-44729`, `partial_scope` for exactly that reason. But the indorsement ties the 30,600 to "Crossed Tennessee, November 21", and the dossier leaves its scope open. So I do not require a change.
  - **Replayed effects:**
    - TN034, `cs-hood-30600` changed to `partial_scope`: CS low 21,420 → 24,500 and adds `single_input`; the point stays 35,000.
    - TN034, the same input with basis `reported_effective` and scope still unresolved: CS point 35,000 → **30,600**.
    - TN038, `cs-hood-23053` with basis `reported_effective`: CS low 21,900 → 22,050.

  The primary should decide the column and scope reading once, for both inputs. At a minimum, the inventory wording should say that the arithmetic supports the effective reading.
- **A2. MO029 US `us-price-3000`: scope code.** Price gives the 3,000 as the force of the onslaught at about 3 p.m. ("about 3 o'clock General Blunt, with 3,000 Federal cavalry … made a furious onslaught"). Britton (p.510) has Sanborn's brigade arrive "shortly before sundown" and go into action.
  - At MO027, the ledger codes a comparable early-force figure, `us-britton-7000`, `partial_scope`.
  - If Price's figure were coded `partial_scope`, the MO029 Union side would drop from C (2,250) to D.
  - I leave it as `scope_unresolved` because Price's short account does not show whether his 3,000 describes only the pre-Sanborn force.
- **A3. VA122 CS `cs-lv-total`: missing tier-2 code.** Livermore prints "Add loss October 19 (as below) 2,911" to reach "Total engaged 18,410". Tier-2 §3 item 5 would add `derived_from_losses`. The class does not change, because `loss_timing: not_prior` and `post_engagement_state` already put the input in class C `post_start_information`. The ledger applies this code unevenly overall; this entry has no numeric effect.
- **A4. MO026 US: wording of the null reason.** The null reason calls Price's 6,000–8,000 "a lower bound". Price's "Blunt's army" is the whole Big Blue line after Curtis joined, not the force at Byram's Ford, although it excludes Pleasonton. It is an opponent estimate, so it could never apply as a bound and grade D stands. The reason could say "an opponent estimate of a different scope (the whole Big Blue line, without Pleasonton)".

## Engagements confirmed without change

For each engagement below, I checked the following:

- every input's printed value, bounds and `printed_text` against the passage;
- the side each input is attributed to;
- its codes, basis, `loss_timing`, `bound` and `reproduction_of`;
- inventory completeness, including every figure of a matching Livermore entry;
- the grade D reasons;
- that the result is consistent with its inputs.

No required issue was found beyond those listed above.

- **VA119 Opequon.** The CWSAC and NPS figures are grouped as reproductions. Livermore p127's effective and present-for-duty lines are on other bases. Pond's 45,509 and 17,195 are correctly class C (scope and link unresolved). The inventory lists every p127 line.
- **VA120 Fisher's Hill.** The live NPS 38,950 is correctly a separate A candidate; the lower median gives 29,444. Livermore has no entry.
- **VA121 Tom's Brook.** Confirmed.
- **VA122 Cedar Creek.**
  - `us-lv` is correctly coded `post_engagement_state` (the October 30 return). Its only deduction is the October 13 loss, so `loss_timing` is `prior_engagements_only`.
  - The CS Livermore totals are class C (post-start). Early's 6,000 muskets and Pond's "nearly 5,000" are parts of the side.
  - The CS point is the lower median of 21,000 and 15,265, which gives 15,270.
- **MO021 Fort Davidson.**
  - US: rule 4 applies, and Britton's 1,051 lower bound (basis `unknown` = point basis; residual class A) correctly raises low from 750 to 1,050. The citizen and Black companies are in addition to the 1,051.
  - CS: grade D is correct. The 12,000 is a one-sided figure for the whole army, including the detached Shelby, and the 5,600 counts the assault columns only.
- **MO022 Glasgow.** Price's report shows Shelby firing from the west bank, which supports coding the 5,000–7,000 for "Clark … on the field" `partial_scope`. The 800–900 prisoners are post-outcome.
- **MO023 Lexington.** The NPS "did set out" figure follows the policy on departures. Price's 3,000–4,000 raises high to 3,500 under rule 5.
- **MO024 Little Blue River.** The NPS 2,000 is the force that set out for Lexington (MO023). Whether it is coded `other_engagement` or link/partial, it is not a candidate. Grade D holds for both sides.
- **MO025, KS004, MO028 and TN035.** These have no counts, and grade D holds for both sides.
- **MO026 Byram's Ford.** Grade D for both sides. See A4.
- **MO027 Westport.** Britton's own text supports the `partial_scope` code for the 7,000–8,000: Blair's brigade and Deitzler's militia "came up" later. Grade D for both sides.
- **KS003 Mine Creek.** Marmaduke's "3,000 strong … lines still extending" is an opponent lower bound. Grade D for both sides.
- **MO029 Newtonia.** See A2.
- **VA076 Saltville.**
  - US: Burbridge's own "2,500 engaged" appears in two dispatches, which are grouped. Jackson's "variously estimated from 4,000 to 8,000" (midpoint 6,000) sets high under rule 5.
  - Treating the unreadable lower ends as one-sided upper bounds follows the LA013 precedent. See F2 for the text fix.
- **AL004 Decatur.** The CWSAC 5,000 is A. Doolittle's total of "about 5,000" is B. The day figures are partial-interval bounds. The CS figure comes from Doolittle's opponent 40,000 under rule 4, giving 30,000 / 20,000 / 40,000. Granger's opponent bound "not less than 35,000" correctly does not apply.
- **TN032 Johnsonville.** US 4,000 is A, and Sinclair's parts are bounds. CS follows rule 4 on Thompson's 13,000, which his scouts and captured men reported.
- **TN033 Bull's Gap.**
  - Breckinridge's report dates Palmer's arrival ("The next day (13th) Colonel Palmer arrived"), which confirms the `partial_interval` code on the 1,800.
  - Ammen, a Union officer, gave the 1,200, so it is correctly an opponent figure for the Confederate side.
  - Gillem's 2,500–3,000 at Morristown on the 14th is correctly set aside.
- **TN034 Columbia.** US grade D is correct: the Cox corps figures are dated October 31, and only elements of the Fourth Corps were present. For the CS side, see A1.
- **TN036 Franklin.** Livermore's totals, 27,939 (Union; November 30 returns, not after the start date) and 26,897 (Confederate), match the page images and are correctly A. The inventory lists every component.
- **TN037 Murfreesboro.** Using the description text's 6,500–7,000 rather than the stored 6,500/6,500 is documented. Grouping the NPS 6,750 (the midpoint) as a reproduction is correct.
- **TN038 Nashville.**
  - The Livermore totals 49,773 and 23,207 match the images.
  - Cox's 44,000 is correctly class C: it is derived from Hood's prior losses (`prior_engagements_only`) and its scope is unresolved. Under the rule 5 hull it sets CS high to 46,200.
  - See A1.

## Limits

This is a separate AI analysis within the scope stated above. It is not historical adjudication, independent corroboration, feature admission or authorization of any fit. The primary should check each finding against its passage before changing the ledger.
