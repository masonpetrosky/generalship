# Primary assessment: Command-responsibility ledger v2, batch 8 of 8

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`. Its
SHA-256 is `9575e703a8b5d66238ac12b33c31519f0f68b856cb072ea507fdedb5564e7dd1`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `ca6f0dc619a28f22be71edf9cc3a392997cbe0d0`; see [dispatch.json](dispatch.json).

Each required finding was checked against the cited passage before it was applied, through the
batch builder; the rebuilt ledger replays under its checker. [correction.json](correction.json)
binds the corrected ledger files.

## Required findings

- **R1** (accepted applied): GA025 CS: verified that the 'no direct orders to the infantry and artillery' quote is from Smith's letter 'Macon, November 19, 1864' (section smith-1864-11-19) and concerns the move from Forsyth to Macon, not Griswoldville (Nov. 22). Replaced the 'Against that choice' passage with the reviewer's wording, keeping Smith 'detained in Macon' (the OCR reads 'detained me a few hours in Macon') and quoting the smith-report OCR exactly ('Notwith- s tan ding my order ...'). Added a citation of the smith-report passage 'my order to avoid an engagement at that place and time, a collision occurred'. Choice (Wheeler), rule 3b, grade C and labels unchanged.
- **R2** (accepted applied): GA028 CS: verified that Cox reads 'Major G. W. Anderson' against the listing 'George A. Anderson', and that the registry keeps conflicting initials separate (cs-james-b-fagan and cs-james-f-fagan). Grade A -> B, rule 2, commander cs-george-a-anderson, citations reduced to the listing, rationale replaced with the reviewer's text.
- **R3** (accepted applied): FL006 CS: verified that Newton's 'The rebel force altogether ... commanded by Generals Jones and Miller' follows the noon reinforcements and does not date the command to the pre-dawn first combat. Grade A -> B, citations reduced to the listing, rationale replaced (Newton's naming of Miller as a brigadier general is kept).
- **R4** (accepted applied): VA088 CS: verified that both Humphreys five-forks quotes ('When the battle began General Pickett and General Fitz Lee were on the north side of Hatcher’s Run.' and 'There was no Confederate commander on the field') occur in reported-force-scope citation 6, and checked the v1 precedents TN006 US and MS010 CS (both grade C, responsibility_unresolved). Grade A -> C, rule 2, labels [responsibility_unresolved, superior_directing] (superior cs-robert-e-lee), both quotes added, rationale replaced. The listing string is 'George Pickett' (cs-george-pickett).
- **R5** (accepted applied): VA093 CS: verified that Ewell's surrender came while G. W. C. Lee was still to be reached ('Before the messenger reached him General Lee had been captured'), and that Humphreys has the contest with Gordon's corps continue until 'just before dark'. Labels are now [command_changed, responsibility_unresolved], with successor null (as LA020 CS; the checker allows it). The last sentence of the rationale is replaced.

## Advisories

- **A1** (accepted applied): Partly applied. VA123 US: removed superior_directing (Grant). Pond shows only Grant's wish and his letters of Feb. 8 and 20, which came from outside the Valley and put suggestions. That makes him a national superior not directing in the field, consistent with VA114 and design §2 ('from within the theater'). The rationale now records this. GA026 US: kept. Sherman met Kilpatrick at Milledgeville, within the theater, and gave the raid's instructions as commander of the army of which the column was part. The primary may still want a single cross-batch reading.
- **A2** (accepted applied): SC010 CS: added Hatch's passage 'They Avere attacked, and re- pnlsed a body of the enemy from the direction of Bee’s Creek battery.' as a citation, with a rationale sentence noting that this earlier Nov. 30 combat has no named Confederate commander. Grade A and choice (Colcock) unchanged.
- **A3** (primary decision): The registry entry cs-g-w-smith (v1 passage-only, NC009) cannot be amended from the batch file. Proposed: record the SC010 identification basis, the report heading in or44-gw-smith-selections-v1 section smith-report (SC010 dossier reported-force-scope citation 3): 'Report of Maj. Gen. Gnstavus Smithy C. 8. Arm^y aomniaadmg First I>ivisio7iy Georgia Militia.' (OCR as printed). Also usable for GA025, where cs-g-w-smith is now a candidate.
- **A4** (accepted applied): GA025 CS: added cs-g-w-smith (existing registry ID) as an unlisted candidate, noted in the rationale. The militia were his command and were withdrawn by his order, though he was in Macon.
- **A5** (accepted applied): VA093 CS: added cs-richard-h-anderson (cid('Richard Anderson'), merged by the primary to Richard H. Anderson) as an unlisted candidate for the co-equal arrangement Ewell describes. The rationale says so.
- **A6** (accepted applied): NC016 CS: the rationale now says Bragg dates his arrival at Wilmington on the 21st, and that his absence at first combat (interval starts Feb. 12) is inferred from that and from the description's 'under Maj. Gen. Robert Hoke', not stated. Grade C and labels unchanged.
- **A7** (kept as is): NC014 US: the reviewer judges grade C under rule 5, second case (Butler's force compelling the result), defensible, and the rationale states its basis. No change.
- **A8** (kept as is): SC011 US: the reviewer accepts grade A under ledger practice (Blair's heading plus his orders). No change.
- **A9** (primary decision): GA002 CS is in resp_b3.py (out of this batch). Its grade is already B. If the primary aligns it with R2, replace 'identity is not in doubt' in its rationale with: 'the conflicting initials are not resolved by any listing field or passage; the listing stands uncontradicted.'

This AI review is a separate analysis, not historical adjudication, feature admission or
authorization of any fit. The ledger rates nobody and changes no model input.
