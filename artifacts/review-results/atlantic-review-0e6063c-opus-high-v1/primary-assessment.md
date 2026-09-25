# Primary assessment: Atlantic coast 1862-65 first passes review

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `0e6063c61be793b103e9ca9b9081f8639ae136df`. Its
SHA-256 is `9e08ef1125ebe2a4d3bc83dbf80b34e938b3300a251e73779111328385c884d2`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `4efb30e022dc68de1198e1bad46c8ba7da3f1456`; see [dispatch.json](dispatch.json).

Each required finding was checked against the retained source text before it was applied, and every
added quote occurs exactly once in its section; `python3 -m generalship check` passes. Superseded
dossiers are archived under `data/evidence/history/`. [correction.json](correction.json) binds the
corrected dossiers.

## Required findings

- **R1** (accepted applied): Verified in the Volume VI parent OCR (or6-illinois-ocr-v1): the Fort Pulaski report list names No. 7 Pemberton and No. 8 Lawton; no Olmstead report is listed. GA001 concealment-and-messengers rationale replaced as proposed.
- **R2** (accepted applied): Verified: Jones p.82 'There were eleven batteries mounting thirty- six guns,'; the 1865 report's battery table in gillmore-1865-10-20-investment-and-batteries sums 3+3+3+3+1+3+2+4+6+4+4 = 36 (computation). GA001 reported-force-scope: Jones citation added; rationale sentence appended (marked as a computation from the listed rows); Pulaski memo armament line updated.
- **R3** (accepted applied): Verified in nps-ga002-v1 Description ('then a small three-gun earthwork battery'). GA002 reported-force-scope: status supported -> disputed, NPS citation added, sentence inserted after Drayton's seven guns and a mortar; rationale notes the gun counts differ; memo updated.
- **R4** (accepted applied): Verified: McCrady's table heading (p.734) 'which attacked Fort McAllister on March 3, 1863.' and Drayton's March 8 ordnance report (p.725) 'on the Ogeechee, on the 3d of March,'. GA002 recorded-result: both cited, final sentence replaced as proposed; Fort McAllister memo inspection and disputes items updated.
- **R5** (accepted applied): Verified: the cited 'This was probably the Montauk' refers to the vessel carrying a turret flag; 'No. 1 is supposed to be the Montauk' (p.732) identifies monitor No. 1. GA002 observation-and-identification: citation added.
- **R6** (accepted applied): Verified (p.732): Elarbee's party fired at an officer stepping out of No. 1's turret, 'but was shot in the act, stumbling forward,'. GA002 casualty-records: citation added, sentence replaced as proposed, rationale notes the claim against the live US 0; memo updated.
- **R7** (accepted applied): Verified (Jones, morris-island-july-10-11, p.220). SC005 casualty-records: citation added for the value's 1 officer and 5 men killed, 1 officer and 5 men wounded.
- **R8** (accepted applied): Verified: in gillmore-1864-02-28-first-bombardment, paragraph 134 quotes the August 24 report ('The practical demolition of Fort Sumter as the result of our seven days' bombard- ment of that work.', p.23), and 'mere infantry outpost' is the February 1864 report's own narrative. SC008 recorded-result value replaced as proposed (with 'southeast face as a ruin'); the August 24 passage cited in recorded-result and state-of-the-fort; the southeast-face sentence (p.30) also cited in recorded-result, where it was previously uncited.
- **R9** (accepted applied): Verified in Hopkins's December 24 letter: Finegan is quoted only on reconnaissance; the spiking remarks answer the commanding general's communication. FL003 command-roles value reworded as proposed (no citation change).
- **R10** (accepted applied): Verified (Semmes, p.573): '2 prisoners of war and 5 blockade runners (one of them severely wounded)' and a 10-name wounded list beginning 'Wounded. — J. P. Randall, acting ensign, Tahoma;'. FL004 casualty-records: both citations added and sentence appended as proposed; memo updated.
- **R11** (accepted applied): Verified against the registry at 0e6063c: the 65 added records split 4 (fort-pulaski-v1) and 3 (st-marks-1865-v1), and the Gillmore and Newton selections' parents are or6-illinois-ocr-v1 and or49-1-illinois-ocr-v1. Fort Pulaski and St. Marks memos: parent paragraphs and record counts replaced as proposed (4 and 3 records).

## Advisories

- **A1** (accepted applied): GA001 casualty-records rationale: '(possibly captured garrison against battle casualties; neither basis is stated)'.
- **A2** (accepted applied): Verified (Jones p.81 'effectually isolated Pulaski'). GA001 siege-labor-and-isolation: Jones's statement added and cited; rationale records the difference from Gillmore's 'impossible to perfectly isolate' and Jones's non-independence; status unchanged (supported). Pulaski memo disputes item added.
- **A3** (accepted applied): SC003 casualty-records: status -> disputed; rationale notes Parker's men's report of cries implies Union losses that Rhind's 'without loss' denies. Charleston 1862 memo disputes item added.
- **A4** (accepted applied): Verified (Beauregard May 19, pp.241-242). SC004 obstructions-and-ranges: New Ironsides at 1,700 yards and 'could not stand the fire at the range of a mile' added and cited; recorded-result: 'maintained their fire until 5.25 p. m.,' added beside Du Pont's 4:30 signal and cited. Memo disputes item updated.
- **A5** (accepted applied): Verified (Gillmore paragraph 46, p.8; Jones wagner-july-18, p.244). SC005 reported-force-scope: 10,000 effective volunteer infantry, 350 artillerists, 600 engineer troops and Jones's report of Gillmore's 'somewhat more than 13,000' added with four citations; SC007 reported-force-scope: the 13,000 added and cited. None adopted; memo strength lists updated.
- **A6** (accepted applied): Verified (Jones wagner-siege-and-evacuation, p.276). SC007 casualty-records: the 641 now stated to include SC005's July 10-11 losses; the 296 for the bombardment (after deducting the July 10 descent and the July 11 and 18 assaults) added with two citations. Nothing added to SC005; memo updated.
- **A7** (not adopted): Would need a metadata-only successor of orn13-mccrady-fort-mcallister-selections-v1. The dependency note is accurate as far as it goes; after R4 the dossier and memo carry the tables' March 3 dating and the section date stays null.
- **A8** (accepted applied): Verified in the ORN 17 index (other Tampa entries exist, e.g. p.309, Howell's September 3, 1862 report). Tampa memo reworded to 'no June–July 1862 Tampa entry'. The same wording in the immutable orn17-trent-ocr-v1 inspection note is left unchanged (no metadata-only successor of a parent OCR record for an advisory); flagged for the primary.
- **A9** (accepted applied): St. Marks memo: 'Two families were inspected (below the three-family ceiling); the naval reports in the already pinned Official Records of the Navies volume 17 were deferred.'
- **A10** (not adopted): Optional; would add a new Finegan selection and source record. The dispute is visible through Hopkins's reply quoting the charge, and the indorsement stays recorded as read, not selected.
- **A11** (accepted applied): Verified (Newton April 6, p.64). FL006 reported-force-scope: expected 600 to 700 local troops increased with pressed men to about 1,000 before the Georgia arrival added with two citations; rationale notes the frozen text ties its 1,000 to the Georgia reinforcements alone. Memo updated.
- **A12** (not adopted): Verified: the 'Key West, Fla., March 19, 1865' dateline lies just after the newton-casualties-1865-03-06 end offset (272432) in the parent. The 1865-03-19 mapping is correct against the parent; no metadata-only successor registered; the fact is recorded in the St. Marks memo.
- **A13** (accepted applied): FL004 destroy-the-runners: Semmes's cotton-loaded vessels passage and his staked-feint sentence cited (both already cited elsewhere in the dossier).

This AI review is a separate analysis, not historical adjudication or proof of source independence.
The dossiers remain drafts; no model input changes.
