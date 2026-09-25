# Separate review: Plymouth and Fort Fisher first passes (NC012–NC016)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), `high` reasoning effort, separate subagent with fresh context. I did not see the author's conversation.
- **Date:** 2026-09-25
- **Prepared commit reviewed:** `c5bcb389e38b6f79200e347aaa78ddacd9795953`, against the previous commit `376c8624c495ba687181d4f9a179762639c09a5d`
- **Bundle commit (worktree HEAD):** `4e5ac2968dbfc43e401fef21905ab2c7930a626b`
- **Assignment:** `assignment.md`, sha256 `6a5f93f5bf8598f2cc77367b9e93ba71ebbb5043bb515d00d864573861ff53f1` (verified)
- **Input manifest:** `inputs.json`, sha256 `42d04c7119f053a3028884b7a2cc14bd7886bf7747f33bdf22ea896548dc10a4` (verified)
- **Outcome: corrections required.** Nine required corrections (R1–R9) and one memo correction set (R10). The advisories (A1–A10) are listed separately.

This is an AI review and a separate analysis. It is not human historical adjudication, it does not prove source independence, and it does not admit any feature.

## Input verification

- I checked all 49 bound paths with `git show c5bcb38:<path>`. All 49 match `inputs.json`.
- In the worktree, 47 of 49 match. `data/sources.json` and `docs/sources.md` differ because the later commit `c298447` ("Add six 1861 Eastern first passes") only adds records. I confirmed that none of the 1,111 source records present at `c5bcb38` changes at HEAD. The five dossiers, the three raw directories and the three memos are also identical between `c5bcb38` and HEAD. I read the registry from `c5bcb38`.
- `make check` passes in the worktree at HEAD: 134 tests OK, and `generalship check` exits 0. It also passes on a `git archive` export of `c5bcb38` in `/tmp` (134 tests OK, exit 0). No build, packet or network command was run.
- The nine new selection files reproduce exactly from their pinned parents using the recorded `selection_character_ranges`, with whitespace collapsed. Each parent's `parent_sha256` matches. The section sets match the range keys.
- Every line of the five NPS `.txt` snapshots occurs in its retained `.html` after tags are stripped.

## Scope actually inspected

- **Guidance documents:** AGENTS.md, `docs/evidence-contract.md` in full, `docs/methodology.md` (the research-depth section), `docs/cohort-v2.md`, and the three memos in full.
- **Dossiers:** all five, every claim, value, rationale and citation (NC012 73 citations, NC013 59, NC014 72, NC015 74, NC016 48). The claim, unknown and citation counts match the memos.
- **Selection files, read in full:** Wessells, Cooke, Smith, Butler, Whiting, Terry, Bragg (OR XLVI), Schofield and Bragg (OR XLVII).
- **NPS and frozen rows:** all five NPS text pages, and the frozen `cwsac_battles`, `cwsac_forces` and `cwsac_commanders` rows for NC012–NC016.
- **Registry:** all 23 records added at `c5bcb38`, plus the pre-existing parents they use (`or42-1-illinois-ocr-v1`, `or46-1-illinois-ocr-v1`, `or47-1-illinois-ocr-v1`, `ia-or47-1-illinois-metadata-v1`). I also checked the existing Butler, Bragg and Schofield author groups, with their dates and registration order.
- **Full OCR parents:** I searched `orn9-full.txt` only to check whether Roe is named. I did not read the full OR XXXIII, ORN 9 or OR XLII/XLVI/XLVII parents beyond the selected ranges. I did not inspect the NPS HTML beyond the text-occurrence check, and I did not inspect the metadata JSON contents.

## Required corrections

Each correction below uses only the already-selected passages. Every new quote was checked as an exact substring of the named section.

**R1. NC012 `reported-force-scope`: the phrase "at that time" is applied to the wrong sentence.** In Wessells's report, "at that time" belongs to the naval-force sentence ("The naval force at that time consisted of…"), not to the garrison list. The garrison list itself carries no date.
- `value`: replace "gives the garrison 'at that time' as the Sixteenth Connecticut" with "gives the garrison 'distributed along this line' as the Sixteenth Connecticut".
- Add a citation: `or33-wessells-plymouth-selections-v1`, §`wessells-1864-08-18`, p.297, quote `The garrison was distributed along this line, and composed as follows:`
- `rationale`: replace "Wessells's effective men per regiment on about April 17 (reported four months later from memory)" with "Wessells's effective men per regiment, undated in the passage (the list sits in his narrative of April 17 and was written four months later from memory)".

**R2. NC012 `warnings-and-reconnaissance`: the dossier says Elliott "brought back" dispatches, but Cooke says Elliott "sent" them.**
- `value`: replace "and that Elliott later reached Hoke by water and brought back dispatches" with "and that Elliott later went by water up a creek in the rear of Plymouth, communicated with Hoke and sent him dispatches".
- Add a citation: `orn9-cooke-albemarle-selections-v1`, §`cooke-1864-04-23`, p.657, quote `proceeded down to the mouth of the river and up a creek in the rear of Plymouth,`

**R3. NC013 `command-roles`: the rationale says Smith's report names Roe, but it does not.** Roe appears in none of the three Plymouth selection files (0 matches). He appears only in the unselected ORN 9 OCR.
- `rationale`: replace "Roe of the Sassacus and the Miami's commander are named as attributed actors only through Smith's report (Roe's own report was not selected)" with "The Sassacus and the Miami act here only through Smith's report, which does not name their commanders in the selected passages; Roe's own Sassacus report was opened but not selected".
- Plymouth memo, Decisions, "Command roles and ranks": remove "Roe" from the list of named attributed actors. The rest of that list is attested in the selections.

**R4. NC014 `reported-force-scope`: the rationale gives the wrong date for the three battalions.** It puts all of Whiting's reinforcement counts on December 24–25. Whiting places the three battalions in the heavy-weather delay after the fleet appeared (the 20th–21st, "Wednesday and Thursday"). Only the 133 regulars and 300 Junior Reserves belong to the night of the 24th–25th.
- `rationale`: replace "Whiting's reinforcement counts for December 24-25" with "Whiting's reinforcement counts: 133 regulars and 300 Junior Reserves thrown in during the night of December 24-25, and three battalions of reserves thrown in during the heavy-weather delay after the fleet appeared on the 20th and 21st".
- Add citations, both from `or42-1-whiting-fort-fisher-selections-v1`, §`whiting-1864-12-30`:
  - p.993: `made its appearance on the 20th and 21st, and remained in the offing about seven miles from New Inlet during Wednesday and Thursday.`
  - p.996: `the delay due to the heavy weather of Wednesday and Thursday after arrival of the fleet was its salvation,`
- NC014 memo, "Opening strengths": replace "three battalions of reserves in all during the weather delay" with "three battalions of reserves during the weather delay after the fleet's arrival". The words "in all" are not in the passage.

**R5. NC014 `seize-the-point-or-pass-the-forts`: Whiting's "no attempt" statement is given without its date or its qualifier.** Whiting says this of the 24th only, "as far as known". On the 25th he reports boats on the bar and an apparent attempt at the entrance.
- `value`: replace "Whiting says no attempt was made to pass the bar and maintains the need for obstructions to hold a fleet under fire." with "Whiting says that on the 24th no attempt, as far as known, was made to land above the forts or to pass the bar; on the 25th he says it appeared the fleet was about to try the entrance before its boats were driven off. He maintains the need for obstructions to hold a fleet under fire."
- Add a citation: `or42-1-whiting-fort-fisher-selections-v1`, §`whiting-1864-12-30`, p.994, quote `At 2 p. m. it appeared as if they were about to try the entrance.`

**R6. NC014 `coal-water-ammunition-and-weather`: the dossier silently adopts the compiler's date query.** The printed text dates the 600 projectiles to "the 21st"; "[25th?]" is the compiler's query.
- `value`: replace "the garrison expended 600 projectiles on the second day with forty-four guns" with "the garrison expended 600 projectiles with forty-four guns on the day printed as the 21st (the compiler queries the 25th)". The existing quote [4] already carries the bracket.

**R7. NC014 `command-roles`: a command statement in the frozen description and on the NPS page is not recorded.** Both say Butler "was relieved of command of the Army of the James and assigned to lead" the expedition. The inspected report headings show him commanding the department and the Army of the James.
- `value`: append "The frozen description and NPS say Butler 'was relieved of command of the Army of the James and assigned to lead' the expedition; his December 20 report is headed as commanding the Department of Virginia and North Carolina, and his January 3 report is dated from the headquarters of the Department of Virginia and North Carolina, Army of the James. The NPS statement is recorded, not adopted."
- `status`: change `supported` to `disputed`. The NC014 memo count of disputed claims becomes four (adding responsibility).
- Add citations:
  - `nps-nc014-v1`, "Description": `Maj. Gen. Benjamin Butler was relieved of command of the Army of the James and assigned to lead an amphibious expedition against Fort Fisher,`
  - `or42-1-butler-fort-fisher-selections-v1`, §`butler-1864-12-20`, p.964: `commanding Department of Virginia and North Carolina.`
  - `or42-1-butler-fort-fisher-selections-v1`, §`butler-1865-01-03`, p.966: `Hdqrs. Dept, of Virginia and North Carolina, Army of the James,`

**R8. NC015 `reported-force-scope`: two of Bragg's figures have the wrong scope.**
- **(a) The 2,300 figure.** Bragg counts 2,300 "arms-bearing men … after manning all the artillery", so the artillery crews are excluded. The dossier drops that qualifier.
  - Replace citation [11]'s quote with `the garrison now fully 2,300 arms-bearing men, or four to the yard, after manning all the artil¬ lery.` (the same section, p.433).
  - In `value`, replace "'fully 2,300 arms-bearing men' after 500 of 1,100 reinforcing infantry arrived on the night of the 14th" with "'fully 2,300 arms-bearing men' after manning all the artillery, once 500 of 1,100 reinforcing infantry had arrived on the night of the 14th".
- **(b) The 110 officers and 2,400 or 2,500 men.** Bragg gives this as the garrison's composition ("The garrison consisted of…"), not as the number in the struggle.
  - In `value`, replace "and, in the struggle, about 110 officers and 2,400 or 2,500 men" with "and, as the garrison's composition (no date given; stated after his account of the final struggle), about 110 officers and 2,400 or 2,500 men".
  - Fort Fisher–Wilmington memo, "Opening strengths", Bragg bullet: replace "about 110 officers and 2,400 or 2,500 men in the struggle" with "a garrison of about 110 officers and 2,400 or 2,500 men (no date given)".

**R9. NC016 `reported-force-scope`: the rationale's boilerplate is wrong for this record.** It says "the live zeros are not measured absence", but NC016's live Forces Engaged field reads `18600 total (US 12000; CS 6600;)`.
- `rationale`: replace "the live zeros are not measured absence." with "the live Forces Engaged field repeats the frozen 12,000 and 6,600 and belongs to the same NPS/CWSAC family, so it is not a separate confirmation."

**R10. Fort Fisher–Wilmington memo: the source-record count is stale at the prepared commit.** No OR XLVII record is added at `c5bcb38`:
- `ia-or47-1-illinois-metadata-v1` and `or47-1-illinois-ocr-v1` already exist at `376c862`, at `data/raw/carolinas-v1/` with sha256 `4dcd50b3…`.
- Both XLVII selections name that record as their parent.
- Across the three passes, 11 + 4 + 8 = 23 records are added.

Two edits are needed:
- **"New source records":** replace "This pass adds **10 source records**" with "This pass adds **8 source records**". Replace the bullet "OR XLVII Part 1 catalog metadata and full OCR (…), expected to deduplicate to the main repository's records of the same IDs on merge" with "the OR XLVII Part 1 selections use the existing Carolinas registrations `ia-or47-1-illinois-metadata-v1` and `or47-1-illinois-ocr-v1` (`data/raw/carolinas-v1/`) as parent; no OR XLVII record is added".
- **"Inspection and stopping record":** replace "Pinned in this worktree with catalog metadata under the same IDs and with the same OCR bytes (SHA-256 `4dcd50b3…`) as the Carolinas pass registered in the main repository; the records describe one artifact and should deduplicate on merge." with "Already registered by the Carolinas pass (SHA-256 `4dcd50b3…`) and reused as parent; not re-registered."

## Checks on the assigned source questions

- **Navies volume 9, not 11.** Sound. The ORN 9 title covers May 5, 1863 to May 5, 1864, which includes April 17–20 and May 5, 1864. The May 24 Bombshell report is printed there. The registry records the 1899 imprint and correctly treats the 1894 catalog date as the authorizing act.
- **Porter deferred under the three-family ceiling.** This is an acceptable reading, and it is recorded:
  - NC014's `command-roles` rationale and its open questions say the Butler–Porter dispute is represented by Butler only.
  - NC014, NC015 and NC016 each list Porter as deferred.
  - The methodology would also have allowed one targeted follow-up for the most consequential gap. Not using it is a permitted choice, not an error (see A10).
- **Author groups reused from the main registry.** These are correct and follow the established convention:
  - **Butler:** `butler-bermuda-hundred-dispatches` is the more recently registered of his two groups (index 836 against 641).
  - **Bragg:** `bragg-chattanooga-report` already holds `or47-1-bragg-kinston-selections-v1`.
  - **Schofield:** `schofield-atlanta-report` is his only group.
  - The dependency notes state that each author's groups form one author family.
- **Volume XLVII parent deduplication.** Done correctly in the registry (the selections point to the Carolinas parent and its hash). Only the memo text is stale (R10).
- **Frozen Plymouth total equals the compiled return.** Verified:
  - The return's rows sum to 127 officers and 2,707 men, 2,834 in all, which equals the frozen `casualties` value.
  - The dossier correctly treats this as an observation and not a reconciliation. The total includes the captured garrison as missing and no Confederate losses.
- **Whiting's total does not match its components.** Verified. The 24th gives 0 + 1 + 3 + 10 = 14 and the 25th gives 3 + 2 + 7 + 26 = 38, so the components sum to 52 against the printed "61 in all". Both numbers are kept.
- **Rules.**
  - No figure is adopted as an opening force. The unknowns are null with no citations.
  - No claim is tagged `inherited`. The `unresolved` and `post_outcome` tags are reasonable.
  - No listed commander receives automatic credit, and nothing is double counted between records.
  - Families per record: NC012 has NPS, Wessells and Cooke; NC013 has NPS, Smith and Cooke; NC014 has NPS, Butler and Whiting; NC015 has NPS, Terry and Bragg; NC016 has NPS, Schofield and Bragg. All five respect the ceiling.
  - The registry inspection notes match what the selection files contain.

## Advisories (not required)

- **A1. NC012 `recorded-result`: Cooke's hearsay on the Miami.** Consider adding that Cooke says he "since learned" that the Miami's captain was killed and that she sank after reaching Edenton. This conflicts with NPS ("damaging the Miami"). Quote: `orn9-cooke-albemarle-selections-v1`, §`cooke-1864-04-23`, p.657, `I have since learned that her captain was killed, and that she sunk after reaching Edentou,`
- **A2. NC013 `reported-force-scope`: Smith's prize list.** Smith's May 24 report names seven vessels entitled to prize shares; the order of attack's eight add the Seymour. Seven matches the NPS count. Quote: §`smith-1864-05-24-bombshell`, p.761, `The vessels entitled to share iu the capture are the Mattabesett, Wy aiming , Sassacus , Miami, Commodore Hull, Ceres , and Whitehead.`
- **A3. NC014 `recorded-result`: Butler's two distances.** Butler's December 27 telegram puts the picket line "within fifty yards" and credits Weitzel; his January 3 report says seventy-five yards and credits Curtis's skirmish line. Quote: §`butler-1864-12-27`, `He brought his picket line within fifty yards of the work,`
- **A4. NC014 logistics and responsibility: two Whiting passages not used.**
  - Logistics: `Probably 10,000 projectiles were thrown on the point during this day's work.` (the 24th; the OCR has a typographic apostrophe).
  - Responsibility: `while the advance of Hoke's division completed their discomfiture;`
- **A5. NC014 `warning-deception-and-prisoners`: precise wording of the addenda.** The addenda say Hoke arrived nearly twelve hours "after Brigadier-General Kirkland had ordered the movement". Prefer that wording over "after Kirkland's movement".
- **A6. NC014 family grouping of the addenda.** Anderson's January 1 letter conveys Bragg's headquarters' version of events, yet it is grouped under `whiting-fort-fisher-reports` because it is printed as addenda. Consider noting in the dependency note that it is a Bragg-headquarters statement. That keeps the NC014 family count honest if Bragg's family is used later.
- **A7. NC015 `command-roles`: Lamb's first name.** The frozen commander is "Charles Lamb". The NC015 selections name only "Colonel Lamb", while Whiting's December 30 report (NC014 source) names "Col. William Lamb, of the Thirty-sixth North Carolina". Consider recording the discrepancy and leaving the frozen row unchanged; it matters for later commander-identity ledgers. Also note, as NC014 does, that the live page lists only Porter and Bragg.
- **A8. NC016 `command-roles`: Schofield's February 11 advance.** "Pushed forward General Terry's line" is Schofield's February 11 action, outside the frozen interval. Date it in the value. Quote: `On the 11th of February I pushed forward General Terry's line,`
- **A9. NC016 `casualty-records`: "one brigade's loss".** The rationale calls Bragg's 350 "one brigade's loss", but Bragg calls it the loss of Hagood's "command" from "his garrison of 2,000". Prefer "the loss of Hagood's command (his Fort Anderson garrison of 2,000, per Bragg)". Separately, NC016's logistics value merges Schofield's storm-defeated sea plan with the tide-defeated beach attempt of February 14; consider separating them.
- **A10. Unused targeted follow-up (no change required).** Porter's report is the most consequential gap for NC014's responsibility dimension. If the owner wants the Butler–Porter dispute two-sided, a single ORN 11 targeted follow-up is the bounded option.

## Unresolved, left visible

This review does not settle:
- the Plymouth surrender hour;
- vessel counts;
- Cooke's sinking claims;
- prisoner-count differences;
- the Fort Anderson evacuation night;
- the scale of the Wilmington stores;
- the basis of the frozen casualty totals (320, 88, 2,000, 1,150);
- the Butler–Porter responsibility dispute.

The dossiers correctly keep these as disputes or unknowns.

## Finding IDs

R1, R2, R3, R4, R5, R6, R7, R8, R9, R10 (required); A1–A10 (advisory).
