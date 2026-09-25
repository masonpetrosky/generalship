# Separate review: Longstreet's Knoxville Campaign (TN023, TN025, TN026)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. Fresh-context subagent; the author's conversation was not an input.
- **Date:** 2026-09-25
- **Prepared commit reviewed:** `5acbdedb03e590741cb037238edaa400ad2c83cd`. **Previous commit:** `dd16b5ed50cc6abff8a3998c51864d8ae973190c`. **Bundle/worktree HEAD:** `d24eab1e84395c5aa2b295e00c602e17aaaee3f0` (its only change after 5acbded is the assignment bundle).
- **Assignment:** `assignment.md`, sha256 `201ef345190024257628f2124af390950d988c920ee5c5071470f6a5da78c9c7`. **Input manifest:** `inputs.json`, sha256 `00c449ecc3b110969e16b37ffc5826b6bac5d71cc8821242e61c053788189fc6`. Both match.
- **Outcome: corrections required.** Required findings: KX-01 to KX-08. Non-blocking notes: N1 to N7.

This is an AI review, a separate analysis. It is not human historical adjudication, independent corroboration or feature admission. I worked offline and did no new research. I opened no other source families, spawned no agents and wrote only this file.

## What I inspected

- **Input hashes.** All 39 bound paths match `git show 5acbded:<path>`, and every one is byte-identical in the worktree.
- **Dossiers.** I read TN023, TN025 and TN026 in full: 27 claims, 123 citation occurrences (42/46/35) and 3 null unknowns (`opening-personnel-unknown` in each). All seven dimensions appear in each record. For every citation I checked entailment, attribution, scope, phase and status.
- **Memo, registry and docs.** I read the memo in full and the nine new `sources.json` records. I also read the diffs to README, roadmap, methodology, sources.md, cli.py, the tests, pilot-report.md and research-queue.json. I read AGENTS.md, the evidence contract and methodology.
- **Frozen rows.** I read 3 `cwsac_battles` rows, 6 `cwsac_forces` rows and 6 `cwsac_commanders` rows. In the forces rows both strength fields are blank; casualties are 400/570, 100/780 and 700/900. The commander ranks are Longstreet, Lieutenant General, in all three records; Burnside, Major General (TN023, TN025); and Shackelford, Brigadier General (TN026). Every cited cell matches exactly, including the full frozen TN026 description.
- **Text derivatives, replayed independently:**
  - **NPS.** Running HTMLParser, dropping script/style, joining the stripped nodes and taking the span from "Return to Results" up to "Experience More" reproduces all three `.txt` files exactly.
  - **OR selections.** Collapsing whitespace over each recorded range of `or31-1-illinois-ocr-v1` reproduces all 7 Burnside, 9 Longstreet and 4 Parke sections exactly. The parent (`646c2e92…4e7d`) has no diff since dd16b5e, and every `parent_sha256` matches it.
- **Page markers in the parent.**
  - **Burnside.** Heads for pp.268–278 sit at chars 933658, 936577, 939973 ("70 KT."), 943544, 946584, 950188, 954504, 958882, 963148, 967297 and 971445 ("■278").
  - **Longstreet.** p.454 is at 1589507. p.455 is at 1592386 (garbled "(;.\mpai<jx. 455"). p.456 is at 1596257, read "45f)". pp.457–465 follow at 1600469, 1604751, 1609154, 1613306, 1617437, 1621753, 1625894, 1629937 and 1634051.
  - **Parke.** The p.325 head is at 1145482, "320" at 1148176 (an even-page head between 325 and 327, so 326), and "827" at 1150951 (so 327).
  - **Result.** Mapping every OR quote back to parent offsets gives the dossier's own page for all 123 citations. Every quote occurs exactly once in its section. No locator relies on a missed or misread header. The Longstreet No. 58 heading falls on p.454 but is not cited (N4).
- **Mechanical checks at the prepared commit:**
  - **Dossier coverage.** 121/127 dossiers; 6 without (GA005, TN024, TN027, TN028, TN029, VA044). 33/36 complete campaign groups by presence.
  - **Source registry.** 555 records / 535 paths. The first 546 records (526 paths) equal dd16b5e's registry.
  - **Byte identity.** The only `data/evidence` changes are the three new files, so all 118 older dossiers and 91 history files are byte-identical. No diff touches the cohort, either Shiloh admission proposal, `admission-check.json`, `baseline.json`, `battles.json`, the CWSAC CSVs or the OR parent.
  - **Admission and baseline.** `promoted_rows` is 0. The baseline has 23 battles in 13 campaigns, with Brier 0.2768816348133779 against 0.25 for equal odds.
  - **Next group.** Chattanooga-Ringgold [November 1863] is next: TN024 (1863-11-23) and GA005. Mine Run (1863-11-27) and Dandridge (1863-12-29) follow.
  - **Receipt.** All 226 input, 555 source and 7 output hashes match.
  - **Packets.** Each of the three packets has 3 JSON blocks. They equal the `battles.json` row, the dossier and `sources.json`.
- **`make check`.** Run offline: 82 tests OK, then `generalship check` reports `draft_dossiers: 121`, `admission_promoted_rows: 0` and `artifacts_written: false`, and exits 0. I ran no build or packet command.
- **Targeted parent context.** I read the OR parent only at range boundaries, report datelines and page heads. I also checked the dates in Shackelford's No. 39 to test the memo's reason for using Parke; that is still the pinned parent, not a new family.
- **Not inspected:** print, facsimiles, maps, subordinate reports, returns, or other parent text.

## Required corrections

After making them, update the citation count everywhere it is stated: the memo table and prose, README, roadmap, the `cli.py` report string and the regenerated pilot report. The count goes from **123 to 126**: TN023 goes to 43 (KX-01), TN025 to 48 (KX-02, KX-05), and TN026 stays at 35. Claims and unknowns do not change. Then regenerate and update the three packets.

**KX-01: TN023 adds a date and place that the cited passages do not state.**
- **Problem.**
  - `guides-and-reconnaissance` says the guides failed "on the night of the 15th". The cited passage (p.458) says only "When daylight came it was found that the guides had failed…". No selected text gives a date.
  - `trains-and-wagons` places the abandoned train "at Lenoir's". The cited quote has no place. The place is in a different, uncited section.
- **`guides-and-reconnaissance`, replacement first sentence:** "Longstreet says that when daylight came it was found that his guides had failed to put the troops on the right road."
- **`trains-and-wagons`, add this citation:** `{"source_id": "or31-1-longstreet-east-tennessee-selections-v1", "section": "longstreet-before-knoxville", "locator": "p.459 (OCR page markers; not checked against print)", "quote": "in the abandoned wagons of the enemy at Lenoir’s Station"}`

**KX-02: TN025 `casualty-records` omits one of Burnside's two sets of figures.**
- **Problem.** The 1865 passage (p.277) says: "Such as could not retreat surrendered ; in all, about 500." That differs from the "about 300" taken in the 1863 dispatch, and the value leaves it out. "in all" may cover the surrendered only or everyone who reached the ditch, so keep it as printed.
- **Second problem.** "three colonels found dead in the ditch" overreads the text. Ruff "was killed at the ditch". Only McElroy's and Thomas's bodies were "found in the ditch".
- **Replacement (Burnside and Longstreet sentences of the value):** "…his 1865 report says that such as could not retreat surrendered, 'in all, about 500', that the enemy's loss was certainly over 1,000 and his own 13. Longstreet says Colonel Ruff was killed at the ditch and that the bodies of Colonels McElroy and Thomas were afterward found in it."
- **Citation to add:** `{"source_id": "or31-1-burnside-knoxville-selections-v1", "section": "burnside-1865-11-13-fort-sanders", "locator": "p.277 (OCR page markers; not checked against print)", "quote": "Such as could not retreat surrendered ; in all, about 500."}`
- **Memo, Fort Sanders dispute bullet:** "…about 300 prisoners in 1863; about 500 surrendered 'in all' and over 1,000 lost in 1865…"

**KX-03: TN025 `reported-force-scope` drops a population qualifier from the 12,000.**
- **Problem.** Burnside's figure is "about 12,000 effective men, exclusive of the new recruits of loyal Tennesseeans".
- **Replacement clause:** "Burnside gives about 12,000 effective men in Knoxville, exclusive of new Tennessee recruits, against…"
- **Citation change.** Replace the quote with `"Our force at this time in Knoxville was about 12,000 effective men, exclusive of the new recruits of loyal Tennesseeans."`. Keep the same section and p.275 locator.

**KX-04: TN025 `rumors-and-warning` attributes content from outside the selection.**
- **Problem.** "rumors of a battle at Chattanooga" comes from the parent sentence just before the `longstreet-fort-sanders` range. The selected passage says only that "so many reports leading to the same conclusion" made him attack.
- **Replacement first clause:** "Longstreet says so many reports led to the same conclusion that he determined he must attack (the reports' subject lies just outside the selected passage), and that approaching the fort he saw men straggling back."
- **Citation change.** Replace `"I determined that I must attack,"` with `"There seemed to be so many reports leading to the same conclusion that I determined that I must attack,"`. Keep the same section and p.460 locator.

**KX-05: TN025 `take-knoxville` has an uncited and ambiguous clause about Jenkins.**
- **Problem.** "with Jenkins's brigade to pass east of the fort" has no citation, and it could be read as Jenkins's own brigade. The source says "General Jenkins was ordered to advance a brigade".
- **Replacement clause:** "…by three brigades, with Jenkins ordered to advance a brigade a little later and pass the enemy's lines east of the fort."
- **Citation to add:** `{"source_id": "or31-1-longstreet-east-tennessee-selections-v1", "section": "longstreet-fort-sanders", "locator": "p.460 (OCR page markers; not checked against print)", "quote": "General Jenkins was ordered to advance a brigade a little later than the assaulting columns"}`

**KX-06: TN026 `reported-force-scope` silently corrects an OCR reading.**
- **Problem.** The value names "Gracie's infantry brigade". The OCR reads "Grade’s", and the cited quote does not include the name at all.
- **Replacement sentence:** "Parke relays a prisoner's statement that he belonged to an infantry brigade read \"Grade’s\" in OCR (not checked against print) and that this brigade had the advance."
- **Citation change.** Replace `"this brigade had the advance,"` with `"he belongs to Grade’s brigade of infantry ; that this brigade had the advance,"`. Keep the same section and p.327 inferred locator.

**KX-07: TN026 `command-roles` misstates the reasons and timing of the abandoned pursuit.**
- **Problem.** Longstreet's reasons (p.464) are Law's "complaint of hardships", McLaws's unfed troops and "so strong a desire for rest". Law's late march is a separate December 15 complaint. The pursuit was ordered the morning after the enemy left its position on the 15th, so "the next day" relative to the frozen December 14 is wrong.
- **Replacement clause:** "…Jones retired from the gap, that Law joined Jenkins late on the 15th, and that when pursuit was ordered after the enemy withdrew that night, Law's complaint of hardships, McLaws's still-unfed troops and a strong desire for rest made him abandon it, the second time in the campaign the enemy escaped."
- **Citation change.** Replace `"that I was obliged to abandon the pursuit,"` with `"General Law preferred a complaint of hardships, &:c. Gen- eral McLaAYS Avas not yet fed, and there seemed so strong a desire for rest rather than to destroy the enemy, that I was obliged to abandon the pursuit,"`. Keep the same section and p.464 locator. The quote appears exactly once.

**KX-08: TN026 `surprise-and-clocks` states a clock conflict the passages do not establish.**
- **Problem.** The frozen description has picket skirmishing "By 2:00 am" and then says the battle "soon" started and lasted most of the day. Parke says the enemy attacked "at 2 p. m." These may be different phases. The clearer disagreement is Longstreet's complete surprise against the description's picket warning.
- **Replacement rationale:** "The frozen description's 2 a.m. picket skirmishing, followed 'soon' by a battle lasting most of the day, differs from Parke's report of an attack at 2 p.m.; the passages may describe different phases, and neither clock is adopted. Longstreet's complete surprise differs from the description's picket warning. Attributed knowledge from interested accounts."
- **Memo bullet, replacement:** "Bean's Station: the frozen description's 2 a.m. picket skirmishing and day-long battle against Parke's 2 p.m. attack, Longstreet's surprise against the pickets' warning, and frozen 1,600 against live 337 casualties."

## Checks that passed (no change needed)

- **Opening strengths.** They stay null. Every opposing figure is attributed and left unadopted: Burnside's little over 5,000 against at least double, 15,000, 12,000 and 20,000–23,000; Longstreet's 20,000 and Stevenson's 23,000; the NPS figure of two divisions plus about 5,000 cavalry; and the frozen description's 4,000. Live zeros and blanks are not treated as measured absence.
- **Casualties.** The differences are kept: 970 against Burnside's ~300; 880 against 815; Burnside's ~500/~300/~20 against >1,000/13; and 1,600 against 337, which is 4.75×, so "almost five" holds. The 1863 "about 20" excludes the separately stated south-side ~40, which the boundary note puts outside the record.
- **Longstreet's judgments.** His blame of Jenkins and Law, the "must have destroyed" counterfactual, the formation of McLaws's lines and his cavalry criticisms are all attributed. The TN026 rationale says the pursuit falls after the frozen date. No listed commander gets automatic or additive credit.
- **Ranks and labels.** The live "Major General" rank for Longstreet is recorded but not adopted. Interested-source labels, report dates (1863-11-17/30, 1865-11-13, 1864-01-01 per the parent datelines) and the note that the OR volume is a shared container are correct.
- **Why Parke.** Shackelford's No. 39 dispatches run from November 15 to a December 14 message that reports no demonstrations since the previous night, so they stop before the fight. Using Parke is justified.
- **Phase tags.** `post_outcome` is used only on outcome claims. `inherited` on TN025 `fort-ditch-and-wire` fits the repository's convention of tagging relative to the engagement start (see N2).

## Non-blocking notes

- **N1.** Burnside's November 17 dispatch says the attack came "about 11 o'clock"; his 1865 report says "about 12 o'clock". Both passages are selected but not recorded. They are one family, so this is not corroboration.
- **N2.** In `fort-ditch-and-wire`, consider this rationale: "Inherited relative to the November 29 start; the works and siege-built entanglements may be commander-created under a campaign boundary." Longstreet's lack of ladders is Confederate preparation, not inherited ground.
- **N3.** TN026 `surprise-and-capture` shortens "unless further orders or developments require it" to "without orders". Suggested wording: "make no advance unless further orders or developments required it".
- **N4.** The Longstreet No. 58 heading is on p.454, so the memo's "pp.455–465" describes the cited passages only. No locator is affected.
- **N5.** Shackelford's December 14 dispatch (No. 39, unselected) bears on the 2 a.m. question. It is a deferred lead only, not a reason to open another packet.
- **N6.** In TN025, "night advance of Confederate pickets" would be more exact as "a Confederate night advance that drove in the Union pickets".
- **N7.** The frozen TN026 description has the Federals retiring to Blain's Cross Roads. Longstreet puts them in a position 3 miles below the station. The dossier could note this difference in place.
