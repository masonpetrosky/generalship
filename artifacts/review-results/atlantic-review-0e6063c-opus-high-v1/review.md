# Separate review: Atlantic coast 1862–65 first passes (15 dossiers, 65 source records)

## Reviewer record

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This is a separate subagent started with fresh context. The author's conversation was not an input.
- **Date:** 2026-09-25.
- **Commits:**
  - prepared commit reviewed: `0e6063c61be793b103e9ca9b9081f8639ae136df`, compared with `ae1ee84`;
  - assignment bundle: `4efb30e022dc68de1198e1bad46c8ba7da3f1456`, which is also the worktree HEAD. Its diff from `0e6063c` adds only `assignment.md` and `inputs.json`.
- **Assignment and manifest hashes:**
  - `assignment.md` sha256 `b7b058277bcea3991697850eaa1aa907c3d09ab0b1c1fc15a12a731b0ec6a3e4`;
  - `inputs.json` sha256 `726ef48f2b70dd6b0e91527fd5678f1d69cb59e5190014ceeebbbe3b916fdd08`.
  - Both match the values in my brief.
- **Input verification:** all 107 bound paths match their `inputs.json` hashes, both in `git show 0e6063c:<path>` and in the worktree. There are **no mismatches**.
- **`make check`:** run offline. It exited 0: `Ran 134 tests … OK`. The check reported `artifacts_written: false`. I ran no build, packet or network commands.
- **Outputs:** I wrote only this file. I did not commit, push or modify any primary artifact.
- **Nature of this review:** it is an AI review. It is not human historical adjudication, not proof of source independence and not feature admission.

## Scope actually inspected

**Documents read in full:**
- AGENTS.md (the copy provided in my context);
- `docs/methodology.md`, `docs/evidence-contract.md` and `docs/cohort-v2.md`;
- all nine first-pass memos;
- the Atlantic section of `docs/sources.md` (lines 172–196).

I did not read `README.md` or `docs/roadmap.md` beyond confirming their hashes.

**Dossiers.** I read all 15 dossiers in full: 135 claims, 16 null unknowns and 648 citation occurrences. The counts per dossier match every memo table.

**Citation checks.**
- **CSV citations:** checked against the frozen `cwsac_battles`, `cwsac_forces` and `cwsac_commanders` rows, which I printed for all 15 records.
- **Every non-CSV citation:** read in its surrounding passage. The method varied by source.

**Selections read end to end:**
- all 15 NPS text pages;
- GA001: the Gillmore and Jones selections;
- SC002: Benham, and Jones's Secessionville section;
- SC003: Rhind and Parker;
- FL002: Pearson and Finegan;
- FL003: Brannan and Hopkins;
- GA002: Drayton and McCrady;
- SC004: Du Pont and Beauregard;
- FL004: Semmes and Westcott.

**Selections checked by context windows and keyword searches, not read end to end.** For these I used ±220–300-character context windows around every cited quote, plus targeted keyword searches:
- the Gillmore 1863 selection (64 KB);
- the Jones 1863 selection (146 KB);
- Seymour and Finegan at Olustee;
- Newton.

**Registry.** I listed all 65 new records with their paths and groups. I read the full metadata of the parents and of about 15 selection records. For all 26 new selections I verified two things:
- the `selection_character_ranges` reproduce the snapshot text exactly from the parent;
- `parent_sha256` equals the registered parent hash.

This includes the deduplicated `or6-illinois-ocr-v1` (gulf-blockade-1861-v1) and `or49-1-illinois-ocr-v1` (mobile-v1). I also checked that each `document_dates_by_section` map covers every non-editorial section. All passed.

**Limited checks of pinned inputs:**
- I checked the report list of Volume VI (parent OCR) to test a GA001 rationale.
- I searched the ORN 17 OCR (the FL002 follow-up volume) for Tampa and Drake, to test the recorded negative follow-up.
- I looked at the parent context of Newton's casualty table.

No other source families were opened.

**Not done:**
- I did not re-derive the NPS text from the HTML.
- I did not inspect any unselected report beyond the checks listed above.
- I did not adjudicate any historical dispute.

## Outcome: **corrections required**

There are eleven required corrections (R1–R11). They are extraction or coverage fixes within the selected passages or the memos. None requires new research, and none changes a model input.

Overall, the batch is careful:
- Opening strengths are null throughout, and no figure is adopted as an opening force.
- Disputes are kept visible.
- The only phase tags are `unresolved` and `post_outcome`.
- No commander is credited automatically.
- Each dossier stays within three families.
- The author-group reuse is correct.

## Required corrections

Locators follow the existing form "p.N (OCR page markers; not checked against print)". I verified every quote below as an exact substring of the named section.

### R1: GA001 `concealment-and-messengers`, `rationale` (false statement about the report list)

The rationale says no Confederate report is listed. The Fort Pulaski memo says the list names Pemberton and Lawton, and the dossier's own open questions defer "Pemberton's and Lawton's Confederate reports". The Volume VI parent OCR confirms: "No. 7. — Maj. Gen. John C. Pemberton, C. S. Army. No. 8. — Brig. Gen. Alexander E. Lawton, C. S. Army."

Replace `(none is listed in the volume's report list)` with:

> (the volume's report list includes Pemberton's and Lawton's reports, which were not inspected; no report by Olmstead is listed)

### R2: GA001 `reported-force-scope`, `value`/`citations`/`rationale` (unsupported attribution; the "30 pieces" framing)

**Add a citation.** The value credits Jones with thirty-six pieces, but no Jones passage is cited for that figure. Add:

- source `jones-fort-pulaski-selections-v1`, section `fort-pulaski`;
- quote `There were eleven batteries mounting thirty- six guns,`;
- locator p.82.

**Append to the rationale:**

> The '30 pieces' reading of the 1865 report conflicts with its own itemized battery table in the same section (Batteries Stanton through Totten list 3+3+3+3+1+3+2+4+6+4+4 = 36 pieces); the OCR figure is preserved but is probably a misreading, not an independent count.

The sum is my own arithmetic on the cited table rows, not a new source.

### R3: GA002 `reported-force-scope`, `status`/`value`/`citations` (NPS figure not accounted for)

The live NPS page calls the fort "then a small three-gun earthwork battery". This conflicts with Drayton's seven guns and a mortar, and with McCrady's list of at least six named pieces.

- **Status:** change `supported` → `disputed`.
- **Citation:** add source `nps-ga002-v1`, quote `then a small three-gun earthwork battery`, locator `Description`.
- **Value:** insert after "…he judged the fort to contain seven guns and a mortar.":

> NPS calls the fort 'then a small three-gun earthwork battery'.

### R4: GA002 `recorded-result`, `value`/`citations` (date evidence inside the selected section omitted)

The value presents McCrady's OCR date "Tuesday, March 8" only against the frozen March 3. It omits two passages:
- McCrady's own signed tables, in the same section, date the bombardment March 3, 1863;
- Drayton's March 8 ordnance report places the action "on the 3d of March".

**Add citations:**

| Source | Section | Quote | Locator |
| --- | --- | --- | --- |
| `orn13-mccrady-fort-mcallister-selections-v1` | `mccrady-1863-03-report-and-tables` | `which attacked Fort McAllister on March 3, 1863.` | p.734 |
| `orn13-drayton-fort-mcallister-selections-v1` | `drayton-1863-03-08-ordnance` | `on the Ogeechee, on the 3d of March,` | p.725 |

**Replace the final sentence** "McCrady's report dates the attack 'Tuesday, March 8' in OCR; the frozen date is March 3." with:

> McCrady's report text reads 'Tuesday, March 8' in OCR, but his tables in the same section and Drayton's ordnance report date the action March 3, matching the frozen date.

The same fact belongs in the GA002 memo's "Disputes preserved" bullet. For the reviewer's own information only, calendar computation (not a source) shows that 3 March 1863 fell on a Tuesday.

### R5: GA002 `observation-and-identification`, `citations` (cited passage does not identify the vessel under fire)

The cited quote "This was probably the Montauk…" identifies the vessel that carried a turret flag. It does not identify monitor No. 1, the vessel under fire. Add:

- source `orn13-mccrady-fort-mcallister-selections-v1`, section `mccrady-1863-03-report-and-tables`;
- quote `No. 1 is supposed to be the Montauk`;
- locator p.732.

### R6: GA002 `casualty-records`, `value`/`citations` (Confederate claim of a Union casualty omitted)

McCrady reports that Elarbee's party shot an officer who stepped out of monitor No. 1's turret. The live field is US 0, and Drayton's selected reports list no casualties.

**Add a citation:**
- source `orn13-mccrady-fort-mcallister-selections-v1`, section `mccrady-1863-03-report-and-tables`;
- quote `but was shot in the act, stumbling forward,`;
- locator p.732.

**Replace** "Drayton's reports list damage to the Passaic but no casualties." with:

> McCrady also reports that riflemen in the marsh shot an officer stepping out of monitor No. 1's turret; Drayton's selected reports list damage to the Passaic but no casualties.

### R7: SC005 `casualty-records`, `citations` (value figure with no cited passage)

The value gives Jones's Confederate assault loss as 1 officer and 5 men killed and 1 officer and 5 men wounded, but no citation supports it. Add:

- source `jones-charleston-1863-selections-v1`, section `morris-island-july-10-11`;
- quote `The Confederate loss in the assault was i officer and 5 enlisted men killed and i officer and 5 enlisted men wounded.`;
- locator p.220.

### R8: SC008 `recorded-result`, `value`/`citations` (date attached to the wrong statement)

The value says Gillmore "reported Sumter reduced to a mere infantry outpost on August 24". The cited "mere infantry outpost" sentence comes from the February 28, 1864 report. The August 24 report is quoted there as reporting "practical demolition".

**Add a citation:**
- source `or28-1-gillmore-charleston-selections-v1`, section `gillmore-1864-02-28-first-bombardment`;
- quote `The practical demolition of Fort Sumter as the result of our seven days’ bombard- ment of that work.`;
- locator p.23.

This quote is also the passage that supports the uncited "practical demolition … after seven days" wording in the `state-of-the-fort` claim.

**Replace** "Gillmore reported Sumter reduced to a mere infantry outpost on August 24" with:

> Gillmore reported to the General-in-Chief on August 24 the practical demolition of Sumter after seven days' bombardment, and his February 1864 report describes it as reduced to a mere infantry outpost

### R9: FL003 `command-roles`, `value` (attribution beyond the cited passage)

The cited December 24 letter quotes Finegan's charge only on reconnaissance. Hopkins's remarks on the unspiked guns answer the commanding general's communication "through General Finegan"; the letter does not attribute that point to Finegan.

Replace "in December he answered Finegan's charge that he had failed to reconnoitre and to spike the guns." with:

> in December he answered Finegan's charge that he had failed to reconnoitre, and explained why he had not spiked the guns.

### R10: FL004 `casualty-records`, `value`/`citations` (Confederate loss omitted; wounded count uncited)

**Add citations:**

| Source | Section | Quote | Locator |
| --- | --- | --- | --- |
| `orn17-semmes-fort-brooke-selections-v1` | `semmes-1863-10-20` | `We have in our possession 2 prisoners of war and 5 blockade runners (one of them severely wounded),` | p.573 |
| `orn17-semmes-fort-brooke-selections-v1` | `semmes-1863-10-20` | `Wounded. — J. P. Randall, acting ensign, Tahoma;` | p.573 |

The second citation supports the value's "10 wounded", which is currently uncited.

**Append to the value:**

> Semmes also reports holding 2 prisoners of war and 5 blockade runners, one severely wounded, against the live CS 0.

### R11: memos `fort-pulaski-first-pass-v1.md` and `st-marks-1865-first-pass-v1.md` (stale after merge deduplication)

At the prepared commit the Volume VI and Volume XLIX Part 1 parents are the pre-existing `or6-illinois-ocr-v1` and `or49-1-illinois-ocr-v1`, and no new catalog records were added. `docs/sources.md` records this deduplication, and the registry adds 65 records. The two memos still describe the parents as newly pinned and count them.

**Fort Pulaski memo:**
- Replace "newly pinned *Official Records* Series I, Volume VI (1882 imprint; `or6-illinois-ocr-v1`, catalog volume v.6 and OCR title checked)" with:

  > *Official Records* Series I, Volume VI (1882 imprint; the already registered `or6-illinois-ocr-v1`, deduplicated at merge; catalog volume v.6 and OCR title checked)

- Replace "This campaign adds **6 records**: the GA001 NPS HTML/text pair, the Volume VI catalog metadata and full OCR, the Gillmore selection and the Jones Fort Pulaski selection." with:

  > This campaign adds **4 records**: the GA001 NPS HTML/text pair, the Gillmore selection and the Jones Fort Pulaski selection. The Gillmore selection's parent is the already registered Volume VI OCR (`or6-illinois-ocr-v1`); this pass's byte-identical copy and catalog record were deduplicated at merge.

**St. Marks memo:**
- Replace "newly pinned *Official Records* Series I, Volume XLIX, Part 1 (1897 imprint; `or49-1-illinois-ocr-v1`)" with:

  > *Official Records* Series I, Volume XLIX, Part 1 (1897 imprint; the already registered `or49-1-illinois-ocr-v1`, deduplicated at merge)

- Replace "This campaign adds **5 records**: … Another parallel pass may register Volume XLIX Part 1 separately; the primary will deduplicate." with:

  > This campaign adds **3 records**: the FL006 NPS HTML/text pair and the Newton selection, whose parent is the already registered Volume XLIX Part 1 OCR (`or49-1-illinois-ocr-v1`); this pass's byte-identical copy and catalog record were deduplicated at merge.

With these changes the memo counts sum to 65 (4+12+4+4+6+20+6+6+3), matching the registry.

## Answers on the specific choices (assignment item 4)

**Reused author groups: sound.**
- Gillmore's two selections share `gillmore-petersburg-june-9-report`, and Fort Pulaski and Charleston 1863 are correctly treated as one family.
- Beauregard reuses `beauregard-drewrys-bluff-report`. The registry already splits Beauregard across older groups; `docs/sources.md` states that they are one family. Nothing new is introduced here.
- Samuel Jones's book belongs in `samuel-jones-east-tennessee-reports` because he is the same person.
- The dependency notes correctly say three things: he is a frozen FL006 commander; the book does not reach FL006; and it follows Gillmore and the other Official Records reports, so it is not independent of them.
- The posthumous, unfinished status of the book is recorded in the registry.

**Other authors' transmittals and indorsements read but not selected: sound under the ceiling.** In each case the item would be a fourth family for that battle:
- Evans at SC003 (Evans is also the frozen SC002 commander);
- Finegan at FL003 (a new family for that battle, although the family is used at FL002 and FL005);
- Gillmore's 1865 indorsement at FL005.

Each dispute stays visible through the selected reply or an open question. As an option, since Finegan's FL003 indorsement was already read, selecting it as that battle's single targeted follow-up would put the accuser's own words on record (advisory A10).

**Unsigned Confederate Olustee casualty table as its own section: sound.** It is headed "[Compiled from nominal lists.]", has a null date and sits inside the Finegan selection. This keeps it inside a non-independent family, and the dossier calls it "the compiled Confederate table" without attributing it to Finegan. Its printed grand total (946) and Finegan's 93 + 841 are kept separate.

**Null section dates: sound.**
- Drayton: the day is lost in OCR. His report says a short report was written the evening before.
- McCrady: the heading reads "March <§". Null is appropriate, but see R4 and advisory A7 on the tables' March 3 dating.
- Semmes: dated October 20 with an October 22 continuation.

**Tampa with no Union report after one follow-up: sound.** My search of the pinned ORN 17 OCR found no June–July 1862 report of the bombardment. The p.309 Tampa item is Howell's report of September 3, 1862, on an attack on refugees. See advisory A8 on the memo's wording.

**Natural Bridge with two families: permissible, but mislabelled.** The methodology does not require three families, and Volume XLIX Part 1 prints no Confederate report. However, the memo's "Two families are recorded as the effort ceiling" misstates the rule, since the ceiling is three families. The already pinned ORN 17 covers the East Gulf squadron to July 17, 1865, so it contains the naval side of Newton's blame dispute. The dossier's open question correctly records it as deferred. See advisory A9.

**Volume VI and XLIX Part 1 parents deduplicated at merge: sound for the registry.** Both parent hashes match, and both selections reproduce exactly from the recorded character ranges. Neither parent record was altered, which is correct given immutability. The two memos are stale (R11).

## Advisories (not required)

- **A1. GA001 `casualty-records` rationale.** "(captured garrison against battle casualties)" asserts populations that the memo says are unstated. Suggested wording: "possibly captured garrison against battle casualties; neither basis is stated".
- **A2. GA001 `siege-labor-and-isolation`.** Jones's same passage says the batteries "effectually isolated Pulaski". Gillmore says it was "impossible to perfectly isolate the work" and that messengers passed. Consider noting the tension.
- **A3. SC003 `casualty-records`.** Parker's "cries were heard after several shots" implies claimed Union losses, against Rhind's "without loss". Consider `disputed`.
- **A4. SC004 `obstructions-and-ranges`.** Beauregard also puts the New Ironsides at 1,700 yards ("could not stand the fire at the range of a mile"), against Du Pont's 1,000. He also has the monitors firing until 5.25 p.m., against Du Pont's 4:30 withdrawal signal. Both could join the existing dispute.
- **A5. SC005/SC007 strength.**
  - Gillmore's paragraph 46 gives the offensive means as 10,000 effective volunteer infantry, 350 artillerists and 600 engineers. This is not recorded in SC005.
  - Jones reports Gillmore's July 20 letter saying he began with "somewhat more than 13,000 on Morris and Folly Islands" (`wagner-july-18`). This is not recorded in SC005 or SC007.
- **A6. SC007 `casualty-records`.** State that Jones's 641 covers July 10–September 7 and so includes SC005's July 10–11 losses. Consider adding his 296 for the bombardment period, which excludes the July 10 descent and the July 11 and 18 assaults (`wagner-siege-and-evacuation`). The rationale already forbids adding these figures to SC005.
- **A7. McCrady registry `dependency_note`.** It cites only "Tuesday, March 8". A `metadata_only` revision could add that the tables in the same section date the action March 3, 1863.
- **A8. ORN 17 inspection note and the FL002 memo.** "the index lists only an April 13, 1862 naval demonstration" is literally too broad, because the index has other Tampa entries (for example p.309, September 1862). Suggested wording: "no June–July 1862 Tampa entry".
- **A9. St. Marks memo.** Reword "Two families are recorded as the effort ceiling" to "Two families were inspected (below the three-family ceiling); the naval reports in the already pinned ORN 17 were deferred."
- **A10. FL003 (optional).** Use the targeted follow-up to select Finegan's already-read indorsement.
- **A11. FL006 `reported-force-scope`.** Newton's April 6 letter also says the local Confederate force was "increased to about 1,000 men" before the Georgia troops arrived. This bears on the frozen CS 1,000, which the frozen text ties to the Georgia reinforcements alone.
- **A12. FL006 casualty table section date (1865-03-19).** The dateline ("Key West, Fla., March 19, 1865") lies just after the selection's end offset in the parent, so the mapped date is not visible in the snapshot. Note this in the inspection or dependency note, through a `metadata_only` revision if changed.
- **A13. FL004 `destroy-the-runners`.** Cite the Semmes passage on the cotton-loaded vessels ready to run the blockade (already cited under logistics). It is the direct support for "object was to destroy the blockade runners".

## Finding IDs

R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11; advisories A1–A13.

No historical dispute is resolved by this review. All unknowns, source disputes and deferred reports remain open, as recorded in the dossiers and memos.
