# Separate review: Franklin-Nashville and Savannah first passes (e03c87e)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. A separate subagent started with fresh context. The author's conversation was not an input.
- **Date:** 2026-09-25.
- **Commits:**
  - prepared `e03c87e330a3596b10727abddcc2e447619648f0`;
  - previous `1191d32433575d224120a6d2aa1df8e381dcecf7`;
  - bundle `0ac7a6951cc3860d325858e214b4b07bbfedc611` (worktree HEAD).
- **Inputs:**
  - `assignment.md` sha256 `dc6d51b0b8020ad2b014ea770f67703a2066256a18b97726e1361446ad6c5646` (verified).
  - `inputs.json` sha256 `6745c2aabdb05eb6685ad4f4d9cd437c6591f908ca4b6985ec7801a9b8a54d2a` (verified).
  - All 113 bound paths hash-match `git show e03c87e:<path>` and the worktree copies. There were no mismatches.
- **Validation:** `make check` was run offline and exited 0.
  - `unittest`: 134 tests, OK.
  - `python3 -m generalship check`: passed; it reports `draft_dossiers: 182` and `artifacts_written: false`.
  - No build, packet or network command was run.
- **Outcome: corrections required.** There are nine required corrections (NASH-R1 to NASH-R9) and a set of advisories (NASH-A1 to NASH-A12).

This is an AI review. It is not human historical adjudication, independent corroboration or feature admission. It adjudicates no historical dispute.

## Scope actually inspected

**Documents.** I read these in full:
- AGENTS.md;
- `docs/evidence-contract.md`;
- `docs/cohort-v2.md`;
- the "Research depth and coverage" section of `docs/methodology.md`;
- both memos;
- the `docs/sources.md` diff;
- the Humphreys precedent passage in `docs/research/overland-first-pass-v1.md` (lines 97–108).

I did not read README.md, `docs/roadmap.md` or the rest of methodology.

**Dossiers.** I read all 13 dossiers (GA023, AL004, TN032, TN034–TN038, GA025, GA026, SC010, GA027, GA028). For each claim I checked:
- the value, rationale, status, phase and open questions;
- every citation.

For every text citation (the non-CSV, non-NPS ones), I read the quote inside its section with about 300 characters of context on each side. Where a claim needed more context, I read longer spans, for example:
- Cox on Lee's crossing, Ruger's fords and the McArthur proposal;
- Wheeler's Buck Head Creek and December 2–4 narrative;
- Kilpatrick's Waynesborough narrative;
- Smith's Honey Hill preamble;
- the Doolittle and Granger strength passages.

I did not read every selection end to end outside those windows.

**NPS pages.** I read all 13 NPS text snapshots in full. I did not inspect the HTML parents.

**Frozen rows.** I read all Arnold battle, force and commander rows for the 13 records.

**Registry.** I read all 51 records the memos describe in full: 13 NPS pairs (group and parent only), four Cox, four OR container and 15 report-selection records. I also compared them with the Atlanta pass's registered Hood, Kilpatrick and Cox records.

**Locators.** I compared each text citation's page locator mechanically with the preceding OCR running heads, and checked every apparent mismatch by hand. No locator error was found.

**Full OCR parents.** I read these only through targeted offline searches:
- `Alatoona` and `Corse` in both Cox volumes;
- the section bounds of the Atlanta-pass Hood selection.

No new source family was opened.

**Not reviewed.** Two other parts of the prepared commit are outside this assignment and were not reviewed:
- the Overland reconciliation (VA046–VA099 and their history archives);
- the three VALLEY-R11/R12 metadata revisions (`or43-1-illinois-ocr-v2`, `or43-1-sheridan-valley-selections-v2`, `or43-1-early-valley-selections-v2`).

## What checked out

- **Counts.** The memo counts match the dossiers:
  - Franklin-Nashville has 76 claims, 8 unknowns, 396 citations, 20 disputed claims (6/7/2/5) and six `inherited` claims.
  - Savannah has 45 claims, 5 unknowns, 212 citations, 13 disputed claims (5/5/3) and two `inherited` claims.
- **Family ceiling.** Every dossier uses exactly three families, counting NPS/CWSAC and Arnold as one.
  - No opening strength is adopted, and all 13 opening-strength claims are null unknowns.
  - Campaign-wide figures are kept as context. Examples are Hood's 7,547 and 10,000, Kilpatrick's campaign losses, Forrest's expedition totals and the army returns.
  - TN035 is not double counted inside TN034.
- **Disputes.** The frozen and live disagreements are preserved: results, casualties and names or ranks.
- **Commander credit.** I found no automatic sole credit.
- **Date mapping.** Mapping a report date where only the year is garbled is sound and documented. French reads '186i' and maps to 1864-10-08; Hazen reads '18()5' and maps to 1865-01-09. Headings whose day is illegible or blank are correctly null: Smith, Kilpatrick's letter and report, Hatch, and Mason's addendum section.
- **Reused author groups.** French in `french-suffolk-reports` and G. W. Smith in `gw-smith-goldsborough-reports` are sound under the Humphreys precedent.
- **New author groups.** These are sound: the registry has no earlier record for Wheeler, Corse, Hazen or C. R. Woods. Rousseau's new group is also sound, because its note cross-references the 1862 `or-buell` record.
- **Kept in the report's family.** Two cases are sound:
  - Hood's addenda: Mason's letter says it was compiled at Hood's request.
  - Kilpatrick's provost-marshal statement: it is Day's inclosure to the report.
- **Cox read but not cited.** This is sound for AL004, TN032, GA025–GA027 and SC010.
- **Inherited tags.** All eight are supported by passages showing pre-existing conditions. Works made during the operations are left `unresolved`.

## Required corrections

Some fixes change a source's metadata (R1–R3). Each such fix is a `metadata_only` revision under the evidence contract: a new `-v2` ID, `supersedes` carrying v1's metadata hash, and a `revision_note`. The raw path and bytes stay the same, and the dossier citations are repointed to the new ID, as in VALLEY-R11/R12.

### NASH-R1: one Hood report is registered in two independence groups

**Evidence.**
- `or38-3-hood-atlanta-selections-v1` (group `hood-atlanta-reports`, Atlanta pass) contains Hood's report headed "Richmond, Va.. February 15, 1865". It covers "the operations of the Army of Tennessee while commanded by me, from July 18, 1864, to January 23, 1865".
- `or45-1-hood-tennessee-selections-v1`, section `hood-1865-02-15`, is the Tennessee portion of the same report: "No. 232. Reports of General John B. Hood … Richmond, Va., February 15y 1865."
- The new record creates `hood-tennessee-reports`, and its dependency note does not name the registered group. One document now belongs to two families.

**Correction.** Create `or45-1-hood-tennessee-selections-v2`.
- **Group.** Change `independence_group` from `hood-tennessee-reports` to `hood-atlanta-reports`.
- **Dependency note, first change.** Replace "(written after he was relieved; its earlier portions are printed in volumes XXXVIII part 3 and XXXIX part 1)" with: "(written after he was relieved; its earlier portions are printed in volumes XXXVIII part 3 and XXXIX part 1, and its July 18–September 6 portion is registered as or38-3-hood-atlanta-selections-v1 in group hood-atlanta-reports)".
- **Dependency note, second change.** Append: "Following the Humphreys precedent, these reports are placed in that author family, whose name reflects the earlier selection."
- **Citations.** Repoint the Hood citations in TN034, TN035, TN036 and TN038 to v2.
- **Memo.** In the Franklin-Nashville memo, remove `hood-tennessee-reports` from "Other new groups". Under Independence groups, add: "**Hood's** February 15, 1865 report is one document across volumes; its Tennessee portion and the other Volume XLV reports join the Atlanta pass's `hood-atlanta-reports`."

### NASH-R2: the Cox *Atlanta* volume is registered, so "not registered" is wrong and the group is unrelated

**Evidence.**
- `ia-cox-atlanta-metadata-v1`, `cox-atlanta-ocr-v1` and `cox-atlanta-selections-v1` (group `cox-atlanta-1882`) are registered at `1191d32`.
- `cox-atlanta-ocr-v1` narrates Allatoona under the spelling "Alatoona" (52 occurrences), for example: "he signalled to Corse, over the heads of the Confederates, to go at once to the relief of Alatoona."
- Despite this, all four Cox March records say "Cox's earlier volume Atlanta is not registered in this pass". GA023 says "Cox's Allatoona narrative is in his Atlanta volume, not registered". The memo says "(not registered)".
- The Humphreys precedent, which this pass itself invokes, places a second book by the same author in that author's existing group.

**Correction.** Create v2 of `ia-cox-march-metadata-v1`, `cox-march-ocr-v1`, `cox-franklin-nashville-selections-v1` and `cox-savannah-selections-v1`.
- **Group.** Set `independence_group` to `cox-atlanta-1882`.
- **Dependency note.** Replace "Cox's earlier volume Atlanta is not registered in this pass." with: "Cox's earlier volume Atlanta (Campaigns of the Civil War IX, 1882) is registered as ia-cox-atlanta-metadata-v1, cox-atlanta-ocr-v1 and cox-atlanta-selections-v1; following the Humphreys precedent, this book is placed in that author's existing group, cox-atlanta-1882, whose name reflects the earlier volume. The two books are one author family, not independent witnesses."
- **Citations.** Repoint the Cox citations in TN034, TN035, TN036, TN038 and GA028.
- **GA023 `open_questions[0]`.** Replace "Cox's Allatoona narrative is in his Atlanta volume, not registered." with: "Cox's Allatoona narrative is in his Atlanta volume (registered by the Atlanta pass as cox-atlanta-ocr-v1; not used for this record, which already has three families)."
- **Franklin-Nashville memo, Allatoona sentence.** Replace "(not registered)" with "(registered by the Atlanta pass in `cox-atlanta-1882`; not used here)".
- **Franklin-Nashville memo, Cox group bullet.** Replace the group ID `cox-march-to-the-sea-1882` with `cox-atlanta-1882` and add the one-author-family sentence.
- **Savannah memo.** Make the same group change.

### NASH-R3: the Kilpatrick group ignores the registered Atlanta group

**Evidence.**
- `or38-2-kilpatrick-lovejoy-selections-v1` (group `kilpatrick-atlanta-reports`, Atlanta pass) is registered.
- `or44-kilpatrick-selections-v1` creates `kilpatrick-savannah-report`, and its dependency note does not mention the earlier record.
- This pass merges French and G. W. Smith into their existing groups but leaves Kilpatrick separate, without saying why.

**Correction.** Create `or44-kilpatrick-selections-v2`.
- **Group.** Set `independence_group` to `kilpatrick-atlanta-reports`.
- **Dependency note.** Append: "The same author's August 23 and September 13, 1864 Lovejoy raid dispatch and report (Volume XXXVIII Part 2) are registered as or38-2-kilpatrick-lovejoy-selections-v1 in group kilpatrick-atlanta-reports; following the Humphreys precedent applied in this pass to French and G. W. Smith, this report is placed in that author family, whose name reflects the earlier reports."
- **Citations.** Repoint GA026 and GA027.
- **Savannah memo.** Update "Other new groups".
- **Acceptable alternative.** Keep a separate group, as in the Averell and Sheridan (VALLEY-R11) practice. In that case the note must name `kilpatrick-atlanta-reports` and state that the two groups are one author's accounts and not mutually independent.

### NASH-R4 (TN032): Sinclair's hedge on the gunboat burning is dropped

**Evidence.** The passage reads "It is said the gun-boats continued firing until they were disabled, when Lieuten¬ ant-Commander King ordered them to be abandoned and burned." (Sinclair, p.862.)

**`command-roles.value`.** Replace "that King ordered the disabled gunboats abandoned and burned;" with: "that, as 'It is said', the gunboats kept firing until disabled, when King ordered them abandoned and burned;". Add this citation:
- source `or39-1-sinclair-johnsonville-selections-v1`;
- section `sinclair-1865-01-07`;
- locator "p.862 (OCR page markers; not checked against print)";
- quote `It is said the gun-boats continued firing until they were disabled,`.

**`destruction-attribution.value`.** Replace "Sinclair says the gunboats were burned on King's order and the transports on Thompson's direction," with: "Sinclair reports as hearsay ('It is said') that the gunboats were burned on King's order, and says the transports were burned on Thompson's direction,". Add the same citation.

**Memo.** Change "King's and Thompson's burning orders" to "King's reported and Thompson's stated burning orders".

### NASH-R5 (TN035 `seize-the-pike`): "obstructing" goes beyond Cox

**Evidence.** Cox says only: "Scho- field needed time for Euger to complete his work at the fords below, and to ship by rail some artillery which had no horses" (spring-hill, p.71).

**Correction.** Replace "Cox says Schofield held on at Columbia to finish obstructing the fords and to ship artillery." with: "Cox says Schofield needed time for Ruger to complete his work at the fords below and to ship by rail some artillery which had no horses." Add this citation:
- source `cox-franklin-nashville-selections-v1`;
- section `spring-hill`;
- locator "p.71 (OCR page markers; not checked against print)";
- quote `to ship by rail some artillery which had no horses`.

### NASH-R6 (GA025 `reported-force-scope`): Smith's engaged-population statements are missing

**Evidence.** Smith states which units were engaged in the same passage as his "one-fourth" ratio (smith-report, p.414): "The First Brigade of militia were not engaged, … Major Cook, commanding the Athens and Augusta battalions, … was uiAon the ground and engaged in this action."

**Value.** After "…puts the two State Line regiments at about 400 muskets." insert: "His report says the First Brigade of militia was not engaged and that Major Cook's Athens and Augusta battalions, moving under separate orders, were on the ground and engaged." Add two citations, both with source `or44-gw-smith-selections-v1`, section `smith-report` and locator "p.414 (OCR page markers; not checked against print)":
- quote `The First Brigade of militia were not engaged,`;
- quote `was uiAon the ground and engaged in this action.`

**Rationale.** Append: "The 1,900 muskets are for Smith's four militia brigades, including the First Brigade, which he says was not engaged; Cook's battalions, which he says were engaged, are not identified in that figure. The engaged total is unknown."

### NASH-R7 (GA026 `recorded-result`): two phases of Wheeler's account are merged

**Evidence.** In Wheeler's account (p.408–409), "The roirt was complete" refers to the morning attack on Kilpatrick's fortified position before the creek. The "uncontrollable confusion" charge came after the creek crossing. That charge is followed at once by "Unfortu¬ nately the open ground did not continue, and we finally encountered a line so positioned that it could not be approached by cavalry", and then by Ashby's wrong road: "Tliis error enabled the enemy to move off*, …".

**Value.** Replace "Wheeler says his charge sent the enemy fleeing in uncontrollable confusion and that the rout was complete." with: "Wheeler says his morning attack drove the enemy from his fortified position ('The rout was complete'); beyond Buck Head Creek his charge on the breastworks made the enemy flee in uncontrollable confusion, but the open ground then ended at a line that could not be approached by cavalry, and Ashby's wrong road let the enemy move off." Add two citations, both with source `or44-wheeler-selections-v1`, section `wheeler-1864-12-24` and locator "p.409 (OCR page markers; not checked against print)":
- quote `Unfortu¬ nately the open ground did not continue,`;
- quote `Tliis error enabled the enemy to move off*,`.

**Savannah memo.** Replace "Wheeler reports a complete rout" with: "Wheeler reports routing Kilpatrick in the morning and a charge beyond the creek that ended at a line cavalry could not approach".

### NASH-R8 (GA026 `reported-force-scope`): a Waynesborough statement is used for Buck Head Creek

**Evidence.** "During all the engagements the enemy's cavalry Avere at least double my own numbers, and were, besides, re-enforced by one or more divisions of infantry" (p.410). The sentence closes Wheeler's December 2–4 narrative, and its mention of infantry does not fit Buck Head Creek. GA027 already cites it correctly.

**Correction.** Delete ", and that the enemy's cavalry was at least double his own numbers" from the value, and remove citation index 8 (quote `the enemy’s cavalry Avere at least double my own numbers,`).

### NASH-R9 (GA027 `rout-the-cavalry`): a post-engagement decision is presented as an objective

**Evidence.** Wheeler's "remained to protect Augusta and to strike his flanks and rear" (p.410) follows his account of the action, after "The enemy re¬ mained in town about three hours". The fuller sentence begins "…liaAing sent Lewis’ brigade … to fall back before the enemy, I, with the remainder of my command, remained to protect Augusta".

**Correction.** Replace "Wheeler says he stayed to protect Augusta and strike the enemy's flanks and rear." with: "Wheeler says that after the engagement he sent Lewis's brigade to fall back before the enemy and remained with the rest of his command to protect Augusta and strike the enemy's flanks and rear; this is his later course, not a stated aim for December 4." Keep the existing citation.

## Advisories (not required)

### NASH-A1: boilerplate rationale about "live zeros"

The `reported-force-scope` rationales for GA023, TN037 and SC010 say "live zeros are not measured absence". Their live force fields are non-zero (3,944, 14,750 and 6,400). Replace the phrase with "the live figures are not adopted".

### NASH-A2: value text that is supported but not cited

The quotes below exist verbatim in the cited sections.

| Record | Value text | Quote to add |
| --- | --- | --- |
| AL004 | 'never exceeded 5,000' | `Our garrisou never exceeded 5,000 inen,` (Doolittle) |
| AL004 | Granger's sorties | `ordered Colonel Doolittle to send ont the Fourteenth` |
| GA023 | 400 prisoners | `400 prisoners, including the wounded;` (Corse, October 7) |
| GA023 | credits Tourtellotte and Rowett | a credit passage for each |
| TN032 | hills within 100 yards | `a range of hills coming down to within 100 yards of the river-bank` |
| TN035 | Cleburne unaware | `He does not seem to have been fully aware of Bradley's position` |
| GA025 | Baldwin and Murray | `I also applied to Colonel Murray for some caA^alry to coA^er the flanks;` |

### NASH-A3 (GA023): the fort names do not agree

NPS says the garrison regrouped in the "Star" fort. French describes "a star fort on the east" of the cut. Corse and French place the final stand in the west fort or "center redoubt on the west of the railroad". Note the naming discrepancy in the `pass-and-redoubts` rationale rather than leave it implicit.

### NASH-A4 (TN032): "three batteries" simplifies Sinclair's list

Sinclair lists:
- the First Kansas Battery;
- Company A, Second U.S. Colored Artillery (two guns);
- a section of the quartermaster's battery;
- two captured 20-pounder Parrotts.

The memo and value say "three batteries". Consider "a battery, a colored artillery company, a section and two captured Parrotts".

### NASH-A5 (SC010): three small gaps in Smith's account

- **"By rail".** In `landing-and-ammunition`, "by rail" is not in the cited sentence. It is implied only by "before leaving the cars" earlier in the report. Drop it or cite that passage.
- **Rail shortfall.** Smith's shortfall ("instead of finding five trains … there were but two", which left three brigades at Thomasville) and Robertson's 4.30 p.m. reserve ("came u]) too late to be used in the action") are relevant, uncited logistics and force-scope context.
- **Rifle pits.** The `inherited` tag covers the redoubt, but the value also includes rifle pits "the enemy had thrown up", whose timing is not stated.

### NASH-A6 (GA027): Kilpatrick does not deny that infantry fought

Kilpatrick's account of December 4 names only cavalry units. He does not deny that infantry took part. Reword "the two commanders disagree on whether infantry attacked" to "Kilpatrick's account names only his cavalry; Wheeler reports infantry advancing". The Savannah memo's "says his cavalry did the fighting" overstates the text in the same way.

### NASH-A7 (TN034 `command-roles`): Hood left two divisions, not the corps

"Hood says he left Lee's corps in front of Columbia" should read "Lee, with the other two divisions of his corps". Cite `leaving the other divisions of Lee’s corps in the enemy’s front at Columbia.` (section `hood-1865-02-15`, p.652). Johnson's division went with Hood.

### NASH-A8: the population behind Hood's addenda totals is unclear

In the garbled OCR rows, the cavalry and artillery components (2,306 and 2,405) appear the same on both dates. The effective totals (30,600 and 23,053) may therefore not include Forrest's corps. Record in the TN034 and TN038 rationales that this population is unestablished. Do not infer it.

### NASH-A9 (TN037): a frozen bounds discrepancy is not cited

The frozen force text reads CS "(6,500-7,000)", but `cwsac_forces.csv` stores 6500/6500. Consider citing both and noting the discrepancy.

### NASH-A10: the registry count covers more than this pass

The prepared commit adds 54 source records. The memos' 51 are correct for this pass. The other three are the VALLEY-R11/R12 metadata revisions, which this review did not inspect.

### NASH-A11: interaction with the pending Atlanta review

R1–R3 touch groups created by the Atlanta pass, whose review (`atlanta-review-1191d32-opus-high-v1`) has no results yet. Coordinate so that neither reconciliation undoes the other.

### NASH-A12: Cox inspection note

The `cox-march-ocr-v1` inspection note says keyword searches found no Allatoona narrative. That conclusion holds: the March volume has only two passing "Alatoona" mentions, the p.23 bridge and the index. It is worth noting that the OCR spells the name "Alatoona".

## Finding IDs

- **Required:** NASH-R1, NASH-R2, NASH-R3, NASH-R4, NASH-R5, NASH-R6, NASH-R7, NASH-R8, NASH-R9.
- **Advisory:** NASH-A1 to NASH-A12.
