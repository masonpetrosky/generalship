# Primary assessment: Red River and Camden first passes review

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `35cf826ea8aa773f67b62447fbcfeddd49cef588`. Its
SHA-256 is `0bf48f371c3aa68cb230df826a99a30ef8209906cf4adaa0db658258ef746b1b`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `d5f01d6522e31af05ee06bf708faec77da085e13`; see [dispatch.json](dispatch.json).

Each required finding was checked against the retained source text before it was applied, and every
added quote occurs exactly once in its section; `python3 -m generalship check` passes. Superseded
dossiers are archived under `data/evidence/history/`. [correction.json](correction.json) binds the
corrected dossiers.

## Required findings

- **RRC-1** (accepted applied): LA017 fort-and-approach: verified that the 'land approach is the dangerous one' wording comes only from Taylor's Sub-inclosure No. 1 (March 13, to Douglas, parent OCR pp.575-576), which is not in the selection (the selected 'to-douglas-10pm' section is Sub-inclosure No. 2). Value replaced with the reviewer's text; rationale records the letter as read, not selected and not cited. Citations unchanged. Red River memo's 'read but not selected' list now names the letter.
- **RRC-2** (accepted applied): LA018/LA019 casualty-records: verified '* Not found.' is the OR compiler's footnote (bottom of p.569) and that Taylor's 2,500 is his own army's two-day loss ('heavy to the country'; cavalry casualties swell 'the whole loss'). Both values corrected; the side is stated as 'in context the Confederate loss' since Taylor does not use the word. LA018 cites '* Not found.' (p.569). Memo's consequential-gap sentence corrected.
- **RRC-3** (accepted applied): LA021 finding-a-crossing: verified the April 24 near-Natchitoches dispatch places Emory's reported fall in Wharton's pursuit to Cloutierville. Value corrected per the reviewer; Wharton sentence cited (p.579).
- **RRC-4** (accepted applied): LA023 bayou-swamp-and-flooded-river: verified the May 18 dispatch's 'no exit' constraint concerns the Confederate raiders' inability to bring off the wagons cut out on May 17. Value corrected; citation [1] lengthened to include 'on which was the Sixteenth Corps,'; De Glaize swamps sentence added (p.594); rationale appended.
- **RRC-5** (accepted applied): AR013 reported-force-scope: verified in Price (p.780) that Gano's 500 reinforced Marmaduke on the prairie and Tandy Walker's ~1,000 came up with Maxey before the April 13 Moscow attack. Value corrected per the reviewer; the two Price citations lengthened to the reviewer's quotes. Camden memo's strength list clarified.
- **RRC-6** (accepted applied): AR015 casualty-records: verified Britton relays the 250 and 800-900 figures as Colonel Drake's report, including 'about one half of these were Confederates'. Value corrected per the reviewer; two citations added (pp.294, 295). Civilian-dead rationale kept. Camden memo's dispute list and atrocity paragraph corrected.
- **RRA-1** (accepted applied): LA018 and LA019 casualty-records: Taylor's 'with a loss of at least 10,000 men.' (p.569) added to both values and cited as an interested two-day claim, not split or added. Memo two-day-totals bullet updated.
- **RRA-2** (accepted applied): LA020 command-roles: 'evening' replaced by Taylor's 'G p. m.' (OCR; probably 6 p.m.) of the 11th against Irwin's 'early on the morning of the nth'; Irwin quote cited (p.325); rationale says the timing is unresolved. Status unchanged.
- **RRA-3** (accepted applied): LA020 reported-force-scope: Irwin's six gunboats/twenty transports dated to the April 7 ascent from Grand Ecore and Taylor's ~30 vessels to the April 9 passage of Grand Bayou Landing; rationale says neither counts the fleet at Blair's Landing on April 12. Two citations added (Irwin p.295, Taylor p.570). Memo dispute line updated.
- **RRA-4** (accepted applied): AR012 casualty-records: verified Price gives no date for Shelby's Terre Noir attack; April 2 is Britton's ('April 2cl'). Value reworded; Price's Terre Noir location and Britton's date cited (pp.780, 257).
- **RRA-5** (accepted applied): AR014 casualty-records: rationale now says 'wounded and cut-off Black soldiers'; Britton's 'When separated from their com mand or cut off from it, the colored soldiers were shot down without mercy.' added to the value and cited (p.291).
- **RRA-6** (not adopted): Section label taylor-1864-05-14-evening: the reviewer itself defers it to the next metadata-only revision and says not to rename in place; the date map is correct and the memo already calls it the second May 14 dispatch. No source successor registered.
- **RRA-7** (not adopted): Taylor selection author field: the dependency note already discloses that Inclosure F is signed by J. L. Brent, and LA017's value says so. A metadata-only successor would move every Taylor citation in seven dossiers for an advisory; left for a later metadata-only revision.
- **RRA-8** (accepted applied): Partly adopted: verified in the selected preface ('Having participated in the operations described'; National Tribune serialization). Recorded in the Camden dossiers' common open question (touches all five, so AR016 is revised for this alone) and the memo, without claiming Britton's presence on the Camden Expedition. Registry dependency note not revised: the parent britton-civil-war-border-2-ocr-v1 is shared with the Price pass and must not change, and a selection-only successor would diverge from it.
- **RRA-9** (accepted applied): LA018 casualty-records rationale: Irwin's one-day 2,186 is not the War Department return, which his appendix says could not separate the days; worded as 'basis not stated in the inspected passage' rather than the reviewer's 'Irwin's own'. Memo updated.
- **RRA-10** (kept as is): No follow-up recommended under the stopping rule; the RRC-1 rationale and memo record Sub-inclosure No. 1 as read and not selected.

## Advisories



This AI review is a separate analysis, not historical adjudication or proof of source independence.
The dossiers remain drafts; no model input changes.
