# Primary assessment: Appomattox and Waynesboro first passes review

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `02dde7d6d5dc6b5796059efabddf4b1b47f2d474`. Its
SHA-256 is `22032365a6e1ed08888395704a8c623c1c281a437c694f15d1e8b1ec82f524df`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `ac30b17ec86fbd7dbfc28c9020ea057d50207f80`; see [dispatch.json](dispatch.json).

Each required finding was checked against the retained source text before it was applied, and every
added quote occurs exactly once in its section; `python3 -m generalship check` passes. Superseded
dossiers are archived under `data/evidence/history/`. [correction.json](correction.json) binds the
corrected dossiers.

## Required findings

- **APX-R1** (accepted applied): Verified: Humphreys, high-bridge-and-farmville p.390 (page head 'LEE NEAR FARMVILLE, APRIL 7th'), 'The loss of the Second Corps to-day was five hundred and seventy-one officers and men killed, wounded, and missing.' VA095 casualty-records: reviewer's value sentence appended, the p.390 citation added (same quote and locator as VA094), and 'No figure is given for April 7.' replaced with the reviewer's rationale text. Figure stays unassigned.
- **APX-R2** (accepted applied): Verified: Humphreys' 'lost the supplies awaiting him at Appomattox Station' (p.391) sits in his counterfactual about the April 7 detention. VA096 supply-trains phase commander_created -> unresolved; rationale replaced with the reviewer's text verbatim. Appomattox memo Tags bullet corrected: no commander_created claims remain in the batch; the train capture is listed as unresolved.
- **APX-R3** (accepted applied): Verified: VA096 casualty-records cites the live NPS field '1048 total (US 48; CS 1000;)' yet said 'Humphreys and NPS give no loss figures.' Replaced with 'Humphreys gives no loss figures, and the NPS description adds none beyond the live casualty field.'

## Advisories

- **APX-A1** (accepted applied): Verified the note's first entry reads 'Quaker road: Muse lost' and the 187 entry has no unit. VA087 casualty-records rationale adds: the note's unit is garbled in OCR ('Muse' in its first entry) and its population is unclear; its 187 is not compared with or added to Johnson's 800 ('division-wide' omitted: Johnson says 'Our losses').
- **APX-A2** (accepted applied): Verified: Sheridan dates Crook's reporting to March 27, then gives the three divisions' effective force undated; the force moved out on the 29th. VA088 reported-force-scope value reworded as suggested; citation 'on the same day the Second Cavalry Division, which had been serving with the Army of the Potomac, reported to me,' (p.1101) added. Memo strength bullet softened the same way.
- **APX-A3** (accepted applied): Adopted with one change: the passage ('General Meade informed that Lee's whole remaining force, probably about 18,000 infantry, had been come up with') gives no hour, so 'that afternoon' is not used. VA094 rationale: the estimate his 1883 history says was sent to Meade during the action (the dispatch itself was not inspected); not a count at Cumberland Church.
- **APX-A4** (accepted applied): Verified live fields VA092 '66 total (US 66; CS 0;)' and VA094 '571 total (US 571; CS 0;)'. Both casualty-records rationales add 'The live Confederate zero is not measured absence.' The memo sentence now matches all four records it names.
- **APX-A5** (accepted applied): Verified VA086 cites humphreys-petersburg-selections-v1#spring-1865-strengths (13,000 cavalry present for duty). VA085 boundary note and the memo's spanning-totals bullet now say VA086 also cites the paragraph and nothing is summed across records.
- **APX-A6** (accepted applied): Applied in neutral form. VA086 and VA087 command-roles record the NPS phrase ('Maj. Gen. W.H. Fitzhugh Lee's cavalry' / '... cavalry divisions at Five Forks', NPS citations added) beside Humphreys' 'the cavalry di¬ visions of the two Lees' (p.328, cited); rationale: the NPS name form does not distinguish the two Lees and is not used for attribution. Whether NPS conflates the two men is not adjudicated, since the inspected sources do not settle how NPS meant the name.
- **APX-A7** (accepted applied): Pond part adopted: metadata_only successor pond-waynesboro-selections-v2 (same path, bytes, parent, ranges and group pond-shenandoah-valley-1883) attributes the quoted-report sentence to the earlier Pond records and names the parent and the two earlier selections in the existing group, replacing 'No earlier registry group for this author'. VA123's 12 Pond citations moved to v2; Waynesboro memo updated. Humphreys part not adopted: the stale Volume XXXVI sentences in humphreys-appomattox-selections-v1 are harmless per the reviewer and change no family, group or citation; no successor (it would move ~400 citations).
- **APX-A8** (not adopted): Verified Humphreys relays Johnson ('General Bushrod Johnson, whose division numbered about 3,800, says that his loss was small', p.384). No dossier pairs Johnson's report with Humphreys for Sailor's Creek (VA093 defers Johnson's April 6 account), so no source successor was added for the Johnson dependency note; the dependency is recorded in the Appomattox memo's Independence groups bullet for a future registry revision.
- **APX-A9** (accepted applied): Verified p.381: 'their total loss could not have been less than 2,000' (Gordon's corps in the running contest with the Second Corps). VA093 casualty-records value records it, citation added, and the rationale says the 6,000 and 2,000 fall within his not less than 8,000 and are not added to it.
- **APX-A10** (accepted applied): VA095 boundary note adds 'He is also a frozen Union commander of this record.' (frozen commander A. A. Humphreys, US, already cited in command-roles).

This AI review is a separate analysis, not historical adjudication or proof of source independence.
The dossiers remain drafts; no model input changes.
