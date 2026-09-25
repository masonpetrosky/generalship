# Best-estimate ledger, batch 3 of 4: separate review

**Outcome: corrections required** (E3-R1 to E3-R10). Advisories E3-A1 to E3-A9 follow.

This is an AI review and a separate analysis. It is not human historical adjudication,
independent corroboration, feature admission or authorization of any fit. It judges the
recorded inputs against the accepted rules and does not re-derive those rules.

## Record

| Item | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), `high` reasoning effort, fresh-context subagent |
| Date | 2026-09-25 |
| Worktree HEAD (bundle commit) | `9dfd6524c9d88b481474e49ff457436d1ea60a5d` |
| Prepared commit reviewed | `4fd1b512f9e4db0402537bfe577031a6cc6939f6` |
| Previous commit | `5151b5700f50fc494b167cc7c4d742c8fc17cc13` |
| `assignment.md` sha256 | `33f9f4c2a5bdaba2a17e357f116e1c2ce88d46fa31462bca04c112f94ec5d9f4` (matches) |
| `inputs.json` sha256 | `3c3d44031bacf0e03bb86c936b63bd653ee3cb7c887a350425dcfc622490c388` (matches) |
| Bound inputs | All 25 paths match both `git show 4fd1b51:<path>` and the worktree; **0 mismatches** |
| Ledger `data/estimates/side-strength-v1.json` | `3408b06a57418ad0ce0df746d815ffc197910f8ff178f81d55de648f2d5b29ba` |
| Design `docs/strength-estimates.md` (not in `inputs.json`) | `795212ad5a3291a6630911fd5671c9f85a52b19c1d05045c091db1de96164ba3`, which equals the ledger's design binding |
| Tier-2 design (not in `inputs.json`) | `0699152d91d2855e3ab052c0da41fd50dfdc78337a01f9c617ecfb7048044c48` |
| Scoping memo (not in `inputs.json`) | `aa8bb163a6a6a7c42b8cdbfa8b877a68a34b29b1f3ea6d0758e061952ce89a1a` |
| 23 bound dossiers | Verified by `estimate-check` against the ledger's `bindings.dossiers` (for example, TN012 `ee2bc871…`, VA032 `e5a8bd5f…`, PA002 `3a93da18…`) |

**Commands run offline.**

- `make check`: 107 tests passed, exit 0.
- `python3 -m generalship estimate-check`: exit 0.
  - Side grades A/B/C/D: 62/25/23/72.
  - Fit-eligible rows: set1_A 21, set2_AB 31, set3_ABC 40.
  - Rows excluded as `post_start_information`: 6.

No build or packet commands were run, and no primary artifact was modified. Before-and-after values below come from an
in-memory replay with `generalship.estimates.estimate_side`, `estimate_row` and `nested_sets`
(scratch copies outside the worktree).

## Scope actually inspected

**Engagements.** All 23 assigned engagements, both sides:

- TN012, TN013, NC010, TN014, TN015, TN016;
- MS004, MS005, AL001, VA032, MS006, VA033, VA034;
- MS007, MS008, MS009, MS010, MS011;
- LA011, VA107, TN017, PA002, AR008.

That covers all 79 ledger inputs, the estimates, labels and nested-set records, the inventories and the rationales.

**Passages.**

- **Dossier claims.** Every `strength` claim in each bound dossier, with every citation quote.
- **Source sections.** For each cited quote, I read the surrounding source section to check side, scope, date and role:
  - Cist: `dover`, `thompsons-station`;
  - Jordan and Pryor: `dover`, `thompsons-station`, `brentwood`, `franklin-reconnaissance` (numbers scan only), `days-gap`;
  - Greene: `grand-gulf`, `port-gibson`, `raymond`, `jackson`, `siege-works-and-garrison`, `helena`;
  - Official Records reports:
    - Bowen: the Grand Gulf report and the May 2 synopsis;
    - Johnston: Jackson;
    - Pemberton: Big Black;
    - Sedgwick;
    - Dennis;
    - McCulloch;
  - Doubleday: `strengths`;
  - the NPS pages for TN015, MS008 and NC010.
- **CWSAC rows.** The frozen `cwsac_forces.csv` rows for both sides of every engagement, and the `cwsac_battles.csv` descriptions for MS009, MS010, MS011 and LA011.
- **Livermore.** The transcription sections p96–p107, and the registered page images p98, p99, p100, p102 and p103.

**Rules applied.** The design §§3–5, tier-2 §3, the extractor policies and `generalship/estimates.py`.

**Not inspected.**

- Other batches.
- Non-strength dossier claims, except a citation scan of TN016.
- OCR readings against print.
- The full texts of `README.md`, `docs/methodology.md`, `docs/roadmap.md`, `docs/evidence-contract.md` and `docs/sources.md`; I verified their hashes only.

I did no network access or new research and opened no new source families.

## Required corrections

Each correction names the engagement, side, input ID, fields and new values. "Result" is the
replayed estimate with only that correction applied.

### E3-R1 TN012 Dover: a Confederate figure is entered on the Union side, and Cist's figure is only part of the Confederate force

**Evidence.**

- Jordan and Pryor, p.226 (`dover`): "Forrest was directed to move with his force- about 800 men* and four guns … Meantime, Wharton, with the remainder of the command, some 2000 strong, and two pieces, advanced by a left-hand road." The footnote lists Forrest's regiments.
- Cist, p.140: "Wheeler directed Forrest to move his brigade with four guns on the river road … while Wheeler with Wharton's command of some twenty-five hundred men moved on a road to the left."
- The dossier value itself reads "Jordan and Pryor give Forrest about 800 men".

**Changes.**

- **US `us-jp`: move it to the Confederate side.**
  - Rename it `cs-jp-forrest`, keeping `source_id`, `ref` (`reported-force-scope`, citation 7), `printed` 800/800, `basis: unknown`, `document_key` and `independence_group`.
  - Set `codes: ["partial_scope"]`, `bound: "lower"`, `class: "bound"`.
  - Set `note: "Forrest's brigade only; Wharton had the remainder (cs-jp-remainder)"`.
- **Confederate `cs-cist`.**
  - Set `codes: ["partial_scope"]`, `bound: "lower"`, `class: "bound"`.
  - Set `note: "Wharton's command only; Cist names Forrest's brigade separately"`.
- **Inventory.** In the `reported-force-scope` use list, replace `us-jp` with `cs-jp-forrest`.

**Result.**

- **Numbers.** Unchanged: US A 800 (570–840); Confederate A 2,500 (2,380–2,630).
- **Stored estimates.**
  - US `range_groups` become `["us-cist","us-cw"]`.
  - Confederate `range_groups` become `["cs-cw"]`, and its labels gain `single_input`.

See E3-A1 for the optional completed sum.

### E3-R2 VA032 Chancellorsville: the Confederate 62,000 is not Hooker's estimate and is miscoded as an opponent estimate

**Evidence.** Doubleday, p.2 (`strengths`):

> "Lieut.-Colonel W. T. Forbes, Assistant Adjutant General, who has had access to the records,
> after a careful estimate, places the number as follows … total effective force, 114,500. He
> estimates Lee's army at 62,000, which the Confederate authorities, Hotchkiss and Allan, place
> as follows: …"

- "He" is Forbes, a records-based compiler, not Hooker. The dossier also says "relays Forbes's … 62,000 for Lee".
- The passage ties the figure to the Confederate authorities' own breakdown. It does not show an opponent's field estimate, so under the extractor policy it is a compiled total.
- Because `cs-dd-hooker` and `cs-dd-reports` share a document, a value (62,000) and a basis, rule 2 groups them. The opponent code then turned the whole group into a rule 4 point of 3/4 × 62,000.

**Changes.**

- **Confederate `cs-dd-hooker`.**
  - Set `codes: ["scope_unresolved"]`, which keeps `class: "C"`.
  - Set `note: "Lt.-Col. W. T. Forbes's records-based estimate of Lee's whole army, which Doubleday says the Confederate authorities Hotchkiss and Allan break down; not Hooker's"`.
- **ID.** Renaming it `cs-dd-forbes`, with the inventory updated to match, is recommended so the ID is not misleading.
- **Alternative coding.** If the primary treats a Union compiler's figure as role-unresolved, use `["scope_unresolved","source_role_unresolved"]` instead. The result is the same.

**Result.**

- **Before:** Confederate C 46,500 (31,000–62,000), `rule4_opponent_only`.
- **After:** Confederate C **62,000 (43,400–80,600)**, `unknown`, `rule3_median`.
- **Labels:** `applicability_unresolved`, `basis_mixed`, `single_input`, `whole_engagement_leakage`.
- **Row sets:** the row stays in set3_ABC. The rationale should be updated.

### E3-R3 VA033 Salem Church: Sedgwick's 15,000 is one hearsay column in his rear, not the Confederate force

**Evidence.** Sedgwick, p.560:

> "I was informed that a column of the enemy, 15,000 strong, coming from the direction of
> Richmond, had occupied the heights of Fredericksburg, cutting off my communications with the
> town."

He then says that "the enemy still maintained his position on Salem Heights". The dossier value agrees ("occupied the Fredericksburg heights behind him").

**Changes.** Confederate `cs-sedgwick`:

- Set `codes: ["adversary_or_hearsay_estimate","partial_scope"]`, `bound: "lower"`, `class: "bound"`.
- Set `note: "hearsay column said to have occupied the Fredericksburg heights in Sedgwick's rear; not the force on Salem Heights"`.

**Result.**

- **Before:** Confederate C 11,250 (7,500–15,000).
- **After:** Confederate **D**, with `null_reason: "No usable candidate value in any inspected source; Sedgwick's hearsay 15,000 is one column in his rear (bound only)."`.
- **Row:** unchanged; it was already incomplete. Update the rationale.

### E3-R4 LA011 Milliken's Bend: Dennis's 2,500 is McCulloch's brigade only

**Evidence.** Dennis, p.448: "The enemy consisted of one brigade, numbering about 2,500, in command of General [H. E.] McCulloch, and 200 cavalry." The ledger already codes the 200 cavalry as `partial_scope`. The brigade figure is the other component.

**Changes.** Confederate `cs-dennis-est`:

- Set `codes: ["adversary_or_hearsay_estimate","partial_scope"]`, `bound: "lower"`, `class: "bound"`.
- Set `note: "McCulloch's brigade only; Dennis lists 200 cavalry separately"`.

**Result.**

- **Confederate:** C 1,880 becomes **D**; give a `null_reason`.
- **US:** unchanged at B 1,060 (900–1,220), but loses `basis_mixed`.
- **Row sets:** the row leaves set3_ABC.

E3-A1 gives a rule 6 completed sum that would keep a grade C Confederate side.

### E3-R5 PA002 Gettysburg: the Confederate effectives line is an intermediate figure from the May 31 returns

**Evidence.** Livermore pp.102–103 (transcription and page images):

- "Army of Northern Virginia, infantry and artillery present for duty May 31 … 64,167 …"
- "Effectives estimated at 93 per cent. … 75,992"
- "Deduct losses prior to Gettysburg 938"
- "Total engaged 75,054"

Livermore states the force brought to Gettysburg only after deducting the prior losses. In the same batch, the ledger codes the identical construction at MS009, `us-lv-apr30-eff` ("Effectives estimated at 93 per cent. 30,955" before "Deduct losses May 1, 12, and 14"), as `engagement_link_unknown`.

Tier-2 §3 item 2 and extractor policy 4 require that for PA002 as well: an earlier state is usable only when the source ties it to the force brought, and here the source says that force is 938 smaller. Keeping `cs-lv-eff` at class A is inconsistent. Applying the same coding to MS009 instead would make its April 30 pre-loss figure (30,955) an A point.

**Changes.** Confederate `cs-lv-eff`:

- Set `codes: ["engagement_link_unknown"]`, `class: "C"`.
- Set `note: "intermediate line from May 31 returns before Livermore's prior-loss deduction; coded as MS009 us-lv-apr30-eff"`.

**Result.**

- **Before:** Confederate A 75,990 (72,190–79,790), `reported_effective`.
- **After:** Confederate **B 75,050 (63,800–86,310), `reported_engaged`**, `point_groups` `["cs-cw"]`.
- **Labels:** `basis_mixed`, `compiled_dependence`, `derivation_unknown`, `single_input`, `whole_engagement_leakage`.
- **Row sets:** the row stays in set2_AB and set3_ABC. The rationale should be updated. The ledger memo's scoping-era statement that Gettysburg keeps a row "only through Livermore's effectives pair" should be revised.

### E3-R6 MS009 Champion Hill: figures in Livermore's note 4 are missing, and the inventory reason is inaccurate

**Evidence.** The p99 transcription reads: "[4] Stevenson's, Bowen's, and Loring's divisions and Wirt Adams's cavalry. General Pemberton places his force at 17,500; but the returns of March 31 give 22,198 as present for duty in these divisions".

The inventory says "entire entry entered", but neither figure is an input. The page image continues note 4: "It therefore is probable that the number given by General Pemberton included only the men bearing muskets. Adding 8 per cent. for officers, 500 for Wirt Adams's cavalry regiment, and 600 for 13 batteries … brings the number to 20,000." Livermore therefore reads Pemberton's figure as probably partial, which is unresolved rather than settled.

**Changes.**

- **Add Confederate `cs-lv-pemberton`.**
  - Source and citation: `source_id` `livermore-transcription-v1`, citation section `p99`, locator `p.99 (page image livermore-p99-image-v1)`, quote `General Pemberton places his force at 17,500`.
  - Value and coding: `printed` 17,500/17,500; `basis: unknown`; `codes: ["scope_unresolved"]`; `loss_timing: none`; `adjustments: []`; `bound: null`.
  - Keys: `document_key` and `independence_group` as in `cs-lv`.
  - `class: "C"`.
  - Note: "Pemberton's own figure relayed in note 4; the page image adds that it probably counted only men bearing muskets".
- **Add Confederate `cs-lv-mar31`.**
  - Citation: the same section, with quote `the returns of March 31 give 22,198 as present for duty in these divisions`.
  - Value and coding: `printed` 22,198/22,198; `basis: present_for_duty`; `codes: ["engagement_link_unknown"]`.
  - `class: "C"`.
  - Note: "March 31 return".
- **Inventory.** Replace the Livermore reason with: "entry lines entered; note 4 figures entered as cs-lv-pemberton and cs-lv-mar31; the 1,582 loss deduction is Livermore's adjustment, not a strength; notes 2–3 and the rest of note 4 are not in the transcription (see E3-A3)".

Both new quotes occur in the section and contain their printed values; I checked this with the checker's own `_passage` and `_printed_in_quote`.

**Result.**

- **Before:** Confederate A 20,000 (19,000–24,150).
- **After:** Confederate A 20,000 (**16,630**–24,150).
- **Labels:** gain `applicability_unresolved`.
- **Range groups:** `["cs-desc","cs-lv","cs-lv-pemberton"]`.
- **US:** unchanged.

Coding `cs-lv-pemberton` with `codes: []` would give the same low but no new label.

### E3-R7 MS004 and MS009: pre-engagement state figures lack `engagement_link_unknown` (extractor policy 4)

**Evidence.**

- **MS004.** Greene p.123: "Stevenson was directed to hold 5,000 men in readiness to move at a moment's notice to Bowen's assistance, whose force, including Green's brigade, numbered about 4,700 men. … This was the condition of affairs on the Confederate side on April 28th." The passage dates the figure before the April 29 action, in a paragraph about reinforcement decisions, and does not say it describes the force at Grand Gulf on April 29.
- **MS009.** The CWSAC description: "he ordered Lt. Gen. John C. Pemberton, commanding about 23,000 men, to leave Edwards Station and attack the Federals at Clinton". This figure is attached to an order before the engagement, and the passage does not tie it to the force brought to Champion Hill.
- **Contrast.** MS006 (Greene's "force engaged in this action … according to the latest returns") and MS008 (Johnston's later "the resistance made by the brigades of Gregg and Walker") do tie their figures to the engagement, so those are not flagged.

**Changes.**

- **MS004 Confederate `cs-greene`:** set `codes: ["engagement_link_unknown"]`, `class: "C"`.
  - Before: Confederate B 4,700 (4,000–5,410).
  - After: **C 4,700 (3,290–6,110)**, with `applicability_unresolved`, `single_input` and `whole_engagement_leakage`.
- **MS009 Confederate `cs-desc`:** set `codes: ["derivation_unknown","engagement_link_unknown"]`, `class: "C"`.
  - The class changes from B to C. With E3-R6 applied, the numbers and labels do not change further.
  - Without E3-R6, this change alone adds `applicability_unresolved`.

### E3-R8 NC010 Fort Anderson: Pettigrew's column is part of the Confederate force

**Evidence.** Foster, p.184: "General Pettigrew, with a force of 7,000 men and seventeen pieces artillery". The ledger's own note says "Pettigrew's column".

**Change.** Confederate `cs-foster-pettigrew`: set `codes: ["adversary_or_hearsay_estimate","partial_scope"]`, `bound: "lower"`, `class: "bound"`.

**Result:** the input's class changes from C to bound. The estimate is unchanged.

### E3-R9 TN015 Brentwood: the 529 surrendered were the Brentwood post only

**Evidence.** Jordan and Pryor, pp.242–243 give two separate groups:

- at Brentwood, "some five hundred and twenty-nine officers, men, and teamsters";
- at the stockade, "The men at this point, some 230 … made the sum total of prisoners 7591" (the OCR reading).

The dossier value says the same.

**Change.** US `us-jp-surrendered`:

- Set `codes: ["partial_scope","post_engagement_state"]`, `bound: "lower"`, `class: "bound"`.
- Set `note: "surrendered at Brentwood only; about 230 more at the stockade"`.

**Result:** the input's class changes from C to bound. The estimate is unchanged.

### E3-R10 AL001 and TN013: partial counts on grade D sides are not recorded (design §2 and rule 7)

**AL001 Confederate: add `cs-jp-roddy`.**

- **Evidence.** Jordan and Pryor, p.258: "leaving forty out of three hun- dred and fifty either killed or wounded on the ground". This is Roddy's command, which the dossier value records.
- **Citation and value.** `source_id` `jordan-streights-raid-selections-v1`; `ref` `reported-force-scope`, citation 4; `printed` 350/350; `printed_text` `three hun- dred and fifty`.
- **Coding.** `basis: unknown`; `codes: ["partial_scope"]`; `bound: "lower"`; `class: "bound"`.
- **Keys.** `document_key` `a8d90966…` (the source sha256) and `independence_group` `jordan-pryor-forrest-1868`.
- **Inventory.** Replace "no Confederate count" with "Roddy's command count entered as cs-jp-roddy (partial)".

**TN013 US: add `us-jp-cav`.**

- **Evidence.** Jordan and Pryor, p.234: "with five regiments of infantry, some 600 cavalry, and a field-battery".
- **Citation and value.** `source_id` `jordan-middle-tennessee-selections-v1`; `ref` `reported-force-scope`, citation 5; `printed` 600/600.
- **Coding.** `basis: unknown`; `codes: ["partial_scope"]` (add `adversary_or_hearsay_estimate` if the primary reads it as a visible opponent estimate); `bound: "lower"`; `class: "bound"`.
- **Keys.** `document_key` `60d2ae8d…` (the source sha256).
- **Inventory.** Name the entry.

Both quotes pass the checker's passage and printed-value tests. **Result:** both sides stay grade D with no numeric change.

**Combined effect of E3-R1 to E3-R10 (this batch only; replayed on the full ledger).**

| Measure | Before | After |
| --- | --- | --- |
| Side grades A/B/C/D | 62/25/23/72 | **61/25/22/74** |
| Fit-eligible rows (set1_A, set2_AB, set3_ABC) | 21/31/40 | **21/31/39** |
| Rows excluded as post-start | 6 | 6 |

With the optional LA011 sum (E3-A1), the side grades are C 23 and D 73, and set3_ABC stays at 40. The ledger memo's table, counts and prose need to be regenerated after reconciliation.

## Checked without a required finding

- **TN014, VA107.** The frozen CWSAC pairs are read and attributed correctly.
- **TN016, MS005, VA034.** Grade D both sides. The dossiers give only formation, vessel or regiment names, and the recorded reasons are accurate.
- **MS007.** Gregg's "Our aggregate engaged was 2,500" is an own report on the engaged basis (A). Greene's "something over 3,000" is a one-sided bound on another basis, correctly not applied. There is no Union count.
- **MS010.** Pemberton's "in all about 4,000 men" is the three brigades named in the CWSAC row (B). Greene's cap of 5,000 lies above the high, so it has no effect.
- **MS011.** The Union point rests on Greene's June 30 figure (post-start C, excluded from fits). The Confederate figure is "about 20,000 effective men" "when the siege began" (A). The Livermore p100 entry is correctly `partial_interval`.
- **TN017.** Bate's figures are partial brigade bounds. The Cist 43,089 is Bragg's army at Shelbyville on June 20 and is correctly recorded as not usable.
- **AR008.** Holmes's own "My whole force engaged in this expedition amounted to 7,646" (A). Greene's 8,000–9,000 adds officers as a source-printed adjustment (B). The Union officers' 15,000 correctly sets the high under rule 5. Greene's Union 4,129 describes "the garrison at this time".
- **MS006, MS008.** The coding is defensible; see E3-A2 and E3-A6.
- **NC010 `cs-nps`, AL001 `us-jp-est`, MS009 US.**
  - `cs-nps` is a directive figure and `us-jp-est` a scouts' estimate from April 27. Each already falls in the same §3 row.
  - The MS009 Union April 30 lines are correctly `engagement_link_unknown`, and `us-lv-may16` is correctly `prior_engagements_only`, because all deducted losses are dated May 1, 12 and 14.
- **Grade D reasons.** The recorded reasons are accurate for every D side in the batch, apart from the omissions fixed in E3-R10.

## Advisories

- **E3-A1: optional completed sums (rule 6; precedent in KY005 and WV010).**
  - **TN012 Confederate.** A Jordan and Pryor sum `cs-jp-sum` = `cs-jp-forrest` 800 + `cs-jp-remainder` 2,000 = 2,800. The components are disjoint ("the remainder of the command"), cover the whole force and share an unknown basis. The sum would be class C and raise the high to 2,940; the point stays 2,500 (A).
  - **LA011 Confederate.** `cs-dennis-sum` = 2,500 + 200 = 2,700, coded `adversary_or_hearsay_estimate`. Rule 4 then gives C **2,030 (1,350–2,700)**, labelled `bound_conflict` (McCulloch's cap of 1,500) and `partial_completed`. The row stays in set3_ABC.
- **E3-A2: MS008 Confederate high (13,800).** The high is set by projected concentrations, not by the force that fought:
  - Johnston: arrivals "would … swell my force to about 11,000";
  - Greene: his 12,000 includes Gist's and Maxey's brigades, which were "expected to arrive the next day";
  - Johnston credits "the resistance made by the brigades of Gregg and Walker".

  The current row-4 codes are defensible. If the primary decides the passages settle these as forces not brought, recoding both to `other_engagement` gives B 6,000 (5,100–6,900).
- **E3-A3: Livermore transcription omissions seen on the page images.** None changes an estimate in this batch by my replay or reasoning, but the transcription note claims that formation-bearing notes are transcribed.
  - **p99.** Notes 2–3 are omitted, including Grant's three divisions, "whose effective strength was 15,390". This is a partial lower bound below the MS009 Union low. The rest of note 4 is also omitted: "present for duty May 16 at least 22,500" and the non-loss derivation of the 20,000. That derivation supports `cs-lv`'s current class.
  - **p100.** The Union 42,315 line and the Confederate component lines (dated May 22–June 25) are omitted, including "Losses prior to June 23 … 2,340". MS011 `cs-lv-assault` should record `loss_timing: not_prior`; this changes no class.
  - **p103.** Note 1 is omitted: an alternative "Total engaged 77,707" from the July 31 returns plus 28,070 Gettysburg losses. It would be a post-start class C figure. The PA002 Livermore inventory reason should mention it.
  - **Remedy.** Transcribing these needs a new versioned transcription, not an edit to the registered one.
- **E3-A4: VA032 `us-dd-cap`.** Add `scope_unresolved`, for consistency with `us-dd-all` and `us-dd-eff` (Hooker's whole army). There is no effect: the bound's basis differs from `point_basis`.
- **E3-A5: rule 2 same-document grouping.** VA032 shows that two figures in one book with the same value, but relayed from different originators, merge and take the class of the union. E3-R2 fixes this instance. The primary may wish to scan other batches for same-document, same-value pairs whose members carry different roles. This is not a request to change the design.
- **E3-A6: MS006.**
  - **Range clipped.** Bowen's own "did not number over 5,500" (a basis-unknown upper bound) clips the Confederate high to 5,500, below Greene's 8,500 candidate. This follows mechanically from rule 7.
  - **Basis of the 8,500.** Greene calls it "Bowen's force engaged in this action … according to the latest returns prior to the battle". Coding the basis as `unknown` is conservative. Reading it as `reported_engaged` would make that input class A, and 8,500 would become the point. That is the primary's judgment.
  - **Uncited figure.** Greene's "7,000 men, after deducting the losses in the battle" is in the section but not cited in the dossier. It would be post-start class C and would not change the estimate.
- **E3-A7: NPS live figures.** These figures are recorded as text in TN014's inventory but as `reproduction_of` inputs in TN012, VA107 and PA002. The estimates are unaffected; aligning the style would help the audit.
- **E3-A8: TN015 `us-jp-surrendered`.** A surrender count of this engagement fits `loss_timing: not_prior` more exactly than `post_engagement_state`. The row and class are the same.
- **E3-A9: ledger memo.** The ledger memo and the estimate table should be regenerated after reconciliation. Other batches' findings are not included in the counts above.

## Finding IDs

- **Required:** E3-R1, E3-R2, E3-R3, E3-R4, E3-R5, E3-R6, E3-R7, E3-R8, E3-R9, E3-R10.
- **Advisory:** E3-A1, E3-A2, E3-A3, E3-A4, E3-A5, E3-A6, E3-A7, E3-A8, E3-A9.
