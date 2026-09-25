# Primary assessment: Command-responsibility ledger v2, batch 2 of 8

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`. Its
SHA-256 is `22471b61b2fd437dce9cf1448de878398154abf9f5591c647bcd1b486a313d84`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `1c6e0eba9c23ee03475d2055d99012a832dd1bb8`; see [dispatch.json](dispatch.json).

Each required finding was checked against the cited passage before it was applied, through the
batch builder; the rebuilt ledger replays under its checker. [correction.json](correction.json)
binds the corrected ledger files.

## Required findings

- **R1** (accepted applied): Verified in Jones (secessionville section): Hunter's assent/deferred departure concerns the movement planned for the 11th, which was deferred; Hunter 'left the field of operations on the evening of the 11th, leaving General Benham in command' with written instructions to make no attempt on Charleston/Fort Johnson; description says 'contrary to Hunter's orders'. SC002 US: superior_directing label, superior (us-david-hunter) and superior_citations removed; added the Jones quote (command-roles[2]) and description quote; rationale replaced per review. Benham A, rule 2, corps_or_wing unchanged.
- **R2** (accepted applied): Verified: description '1,600 Rebels under Col. J.T. Coffee' attacked night of 15th; Britton says Coffey 'up to this time, was acting independently of the Confederate officers', Cockrell's main force three miles away, and Cockrell 'was reinforced by twelve hundred men under Colonel Coffey' after 11 a.m. MO015 CS changed from cs-jeremiah-vard-cockrell (C, 3a, [responsibility_unresolved]) to cs-j-t-coffee (passage-only, C, 3a, unknown), labels [command_changed, responsibility_unresolved], candidates [Cockrell, Thompson, Hays], successor Cockrell; added Britton citation; rationale per review including the 3(c)/grade D alternative reading. Follows the AR003 reading of rule 3(a) with rule 2's third bullet and v1 KY007/TN017 first-combat precedents; the primary should confirm that reading (the rule-consistent alternative is 3(c), grade D).
- **R3** (accepted applied): Verified RANK_ORDER_V2 in generalship/command.py includes Captain (army) and Lieutenant Commander (navy). GA001 US rationale's stale final sentence replaced with the reviewer's text. Out of batch for the primary: TN032 US carries a similar stale 'Lieutenant Commander is not in the declared navy rank order' note.
- **R4** (accepted applied): Verified both report headings. MO016 CS echelon unknown -> division, added Cooper heading citation (command-roles[5]); MO016 US echelon unknown -> division, added Salomon heading citation (command-roles[3]); both rationales now state the echelon basis, and the US rationale records the 'Headquarters First Brigade, Army of Kansas' letterhead conflict. Division adopted for US because Salomon ordered the First and Second Kansas Brigades plus Hall's Fourth Brigade MSM.

## Advisories

- **A1** (accepted applied): Partly: MO016 CS rationale now records Rains ('orders from Brigadier-General Bains', OCR) as a borderline superior not labelled (order concerned the march to join Shelby; no passage shows him directing at Newtonia; Rains not listed), with the citation added. Lovell (LA001) and Blunt (AR005) already discussed in rationales; no labels added (not adopted: labelling is borderline, the v1 convention keeps such cases in rationales).
- **A2** (accepted applied): LA001 US: added Mahan citation 'The steam vessels of the flotilla were at once ordered by the flag-officer to Southwest Pass' (reported-force-scope[3]) and a rationale clause. Grade unchanged (A).
- **A3** (accepted applied): MO014 CS: added Britton citations for Hughes leading a column (quote spans the running head exactly as OCR) and 'After Colonel Hughes was killed Colonel G. W. Thompson took command'; rationale updated. Grade unchanged (A, 3a).
- **A4** (accepted applied): OK004 CS: added cs-stand-watie (listed registry ID from OK006) as a candidate, with citations to Cooper 25 Oct 'Colonel Watie, who has command during my illness' and Cooper 15 Dec 'under command of Col, Stand Watie' (the planned 22nd march, Cooper too ill); rationale records the reading. Buster, grade C unchanged.
- **A5** (accepted applied): MO017 CS rationale now states that no inspected passage identifies Wickersham's 'General Green' with the listed Colton Greene. Grade and candidates unchanged.
- **A6** (accepted applied): Partly: LA003 CS echelon corps_or_wing -> unknown, since the description ('his corps') and Breckinridge's report heading ('Breckinridge's Division') disagree; rationale says so. The US Dudley/Cahill successor dispute stays as recorded (Dudley has no registry entry; kept_as_is).
- **A7** (accepted applied): Registry us-m-h-brawner passage citation changed from Foster's 'Captain Brawner was then in command.' (no initials) to the description "Foster's successor, Capt. M.H. Brawner to order a retreat". No other batch uses this ID; no merge involved.
- **A8** (not adopted): Not expressible in the batch file: LA001 (16-28 Apr) and LA002 (25 Apr-1 May) overlap but are not a contained-interval pair, so rule 7 does not apply. Passed to the primary for a note in the rating views about Farragut being credited in both.
- **A9** (kept as is): FL002 US echelon 'flotilla' for a single gunboat kept; the reviewer finds either value defensible.

This AI review is a separate analysis, not historical adjudication, feature admission or
authorization of any fit. The ledger rates nobody and changes no model input.
