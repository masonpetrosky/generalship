# Primary assessment: 1864 Eastern small-operation first passes review

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `8642430daf32af81b45aed82da33c819b990556e`. Its
SHA-256 is `816016d0b085dfcc15d04937b27a2979f002e80438ff05dfde066254ce5e6f3d`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `c7f5799595db240736cc9176f345fd69720615a7`; see [dispatch.json](dispatch.json).

Each required finding was checked against the retained source text before it was applied, and every
added quote occurs exactly once in its section; `python3 -m generalship check` passes. Superseded
dossiers are archived under `data/evidence/history/`. [correction.json](correction.json) binds the
corrected dossiers.

## Required findings

- **E1864-R1** (accepted applied): Verified: or33-illinois-ocr-v1 / ia-or33-illinois-metadata-v1 were registered for Plymouth and 8642430 adds 30 records (5/5/8/12). Rapidan memo now names the registered parent and gives five records, not seven; Kilpatrick-Dahlgren memo's two Volume XXXIII sentences name or33-illinois-ocr-v1. Memo-only; no dossier change.
- **E1864-R2** (accepted applied): Verified in the kilpatrick selection: 'Wednesday, March 2.' stands at the foot of p.183 before the p.184 running head, inside the kilpatrick-1864-03-16 range, and is the compiler's footnote to the March 8 dispatch's 'Thursday evening, 11 p. m.*'. VA125 recorded-result citation locator replaced with the reviewer's text.
- **E1864-R3** (accepted applied): Verified (crook-1864-05-23, p.10). VA049 railroad-and-bridge now cites Crook's 'I sent Brig. Gen. W. W. Averell, with a mounted force of 2,000 picked men, to move via Logan Court-House to Saltville, on the railroad,'.
- **E1864-R4** (accepted applied): Verified in McCausland's May 25 report: only the 600 killed and wounded is placed 'at Cloyd's'. VA049 casualty-records value replaced as proposed and the prisoners/1,000 sentence cited (p.48).
- **E1864-R5** (accepted applied): Verified: Pond (p.13) has Crook take and burn the bridge after a two-hour artillery duel; Averell (p.42) reached Dublin the evening of the 11th and crossed New River on the 12th. VA109 recorded-result value and rationale replaced as proposed with the three proposed citations. The primary additionally cited the NPS Description sentence the value paraphrases ('The next day, Averell reached the New River Bridge ... which he burned.'), which was uncited; VA109 citations 47 -> 51. Families unchanged (NPS, Pond, Averell, McCausland).
- **E1864-R6** (accepted applied): Verified: live VA110 '10365 total (US 6275; CS 4090;)' and VA111 '14000 total (US 8500; CS 5500;)' repeat the frozen cwsac_forces values. Both rationales now end with the reviewer's sentence (new common.py constant NOT_ADOPTED_LIVE); VA045, VA125, VA049, VA109 and VA064, whose live pages give zeros, keep the original sentence.
- **E1864-R7** (accepted applied): Crook-Averell memo: the New River bridge dispute bullet added under Cove Mountain; counts updated VA049 74->76, VA109 47->51 (the reviewer's 50 excludes the added NPS citation), batch 121->127. Memo also records R4's scope for McCausland's figures and A8's 538 note.

## Advisories

- **E1864-A1** (accepted applied): Verified Warren's 'I reached the ford about 3 p. m.' and 'General Humphreys ... was present during the enemy's attack at night-fall' in the OR XXXIII parent (Warren No. 2, unselected). VA045 command-roles rationale no longer synchronizes the clocks (reviewer's wording); an uncited open question records Warren's two statements; the memo sentence is softened.
- **E1864-A2** (accepted applied): Verified Kilpatrick ('with upward of 300 officers and men belonging to Colonel Dahlgren’s party,', p.186) and Humphreys ('Captain Mitchell, with 300 of Colonel Dahlgren's party,', p.79). Added to VA125 reported-force-scope value with two citations; memo strength list updated.
- **E1864-A3** (accepted applied): VA125 rivers-roads-and-ambush-point value now quotes Pollard verbatim ('I put them in the position which I had chosen about dark') instead of choosing a reading.
- **E1864-A4** (not adopted): The reviewer calls the post_outcome tag on the Dahlgren-papers claim conservative and defensible; it keeps the claim out of any admission path. Kept.
- **E1864-A5** (not adopted): Optional registry advisory. The R2 locator discloses the compiler footnote where it is cited; registry records are immutable, and a metadata-only successor of or33-kilpatrick-richmond-raid-selections-v1 (repointing all VA125 Kilpatrick citations) is left to a future metadata revision or the primary.
- **E1864-A6** (not adopted): The Humphreys records' note names Volume XXVII rather than XXXIII, but its conclusion (no dependence on the printed compilation) holds for the 1891 Volume XXXIII too. Registry records are immutable; left to a future metadata-only revision.
- **E1864-A7** (not adopted): The two Pond records share a dependency note accurate for the two selections together. Registry records are immutable; the dossier open-question family notes (FAM strings) already state per campaign which reports Pond quotes. Left to a future metadata-only revision.
- **E1864-A8** (accepted applied): Verified the inclosure total line ends '504 538' under 'Total. Aggregate.' and covers 'the battle of Cloyd's Farm, May 9, 1864, and subsequent operations'. VA049 casualty rationale notes the live CS 538 equals that aggregate; a VA049 open question records that the frozen/live descriptions attribute the bridge burning to Averell, not adopted.
- **E1864-A9** (accepted applied): Verified: the 4,500 was 'ascertained' at Tazewell with no stated source; the deserters sentence concerns Confederate knowledge; the 5,000 is 'stated by rebel newspapers'. VA109 strength rationale uses the reviewer's wording.
- **E1864-A10** (accepted applied): Verified: Pond writes 'Imboden, in his report, gives the cavalry at 800' and 'He also puts the infantry actually engaged at 3,440 ...'. VA110 value sentence split so Imboden's figures are attributed to his report, not Lincoln's study.
- **E1864-A11** (accepted applied): VA111 terrain value quotes Hunter's ambiguous sentence verbatim and gives Pond's reading separately; the Pond citation now quotes the fuller 'drove the enemy through the woods to his main works, which were on a curving range of thickly timbered hills ;' (p.27).
- **E1864-A12** (accepted applied): VA064 boundary note and recorded-result value, and the Lynchburg memo, now say Diamond Hill and Quaker church may name the same position, matching the terrain rationale.
- **E1864-A13** (kept as is): No correction required: Sigel's and Breckinridge's groups are those authors' only registered groups; same-author material stays together and is not counted as corroboration. The misleading group names are recorded in the Lynchburg memo.

This AI review is a separate analysis, not historical adjudication or proof of source independence.
The dossiers remain drafts; no model input changes.
