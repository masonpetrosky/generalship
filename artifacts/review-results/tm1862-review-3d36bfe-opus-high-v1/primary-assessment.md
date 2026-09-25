# Primary assessment: Trans-Mississippi 1862 first passes review

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `3d36bfe394ead1264b329d1d8b5b35ed794086f0`. Its
SHA-256 is `33243e50c705879b7ea16ed7324ecad1a515e072e958f56098cc846c4e2e3e53`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `aeeeecf9e3de705bf72fe52430e6b41c3fc05e18`; see [dispatch.json](dispatch.json).

Each required finding was checked against the retained source text before it was applied, and every
added quote occurs exactly once in its section; `python3 -m generalship check` passes. Superseded
dossiers are archived under `data/evidence/history/`. [correction.json](correction.json) binds the
corrected dossiers.

## Required findings

- **TM-R1** (accepted applied): Verified: the Britton volume I selection carries britton-civil-war-on-border-1899 while its parent britton-border-1-ocr-v1 is in britton-civil-war-border, and its dependency note misdescribes the author's groups. Applied in the Boston Mountains memo only (parent and group named, reference to the docs/sources.md W61-R14 author-group note). Per the primary's author-group decision, no metadata-only successor britton-border-1-boston-mountains-selections-v2 was registered and the MO014/MO015 Britton citations are unchanged; the proposed -v2 is left to the primary.
- **TM-R2** (accepted applied): Verified against the registry (or8-cooper-indian-territory-selections-v1 in cooper-indian-territory-report). Registered metadata-only successor or13-cooper-newtonia-old-fort-wayne-selections-v2 (group cooper-indian-territory-report, corrected dependency note, predecessor digest 368b670e... matches the review). MO016 (16) and OK004 (18) Cooper citations repointed; Boston Mountains memo table and group sentence corrected.
- **TM-R3** (accepted applied): Verified in hindman-1863-06-19-saint-charles and Dunnington's report: Hindman names no author for the 'detailed report' and his 79/35 figures are not in Dunnington. Registered metadata-only successor or13-hindman-cache-river-selections-v2 (corrected dependency note; predecessor digest 41387fd1... matches). AR002 (11) and AR003 (12) Hindman citations repointed; AR002 last open question and White River memo reworded as proposed.
- **TM-R4** (accepted applied): Pea Ridge memo: OR VIII parent named as the registered or8-illinois-ocr-v1/ia-or8-illinois-metadata-v1, dedup sentence removed, 4 records (not 6). Boston Mountains memo: Britton parent named as britton-border-1-ocr-v1, 23 records (not 25), Britton bullet reduced to one selection.
- **TM-R5** (accepted applied): Verified in Salomon's October 1 report ('On the 29th ultimo I sent scouting parties'; firing 'on the 30th'). MO016 reported-force-scope value and rationale corrected as proposed, two dating citations added; memo Newtonia line dated.
- **TM-R6** (accepted applied): Verified (Wickersham 8 enemy killed; Barstow 9 in the morning skirmish, 34 for the day). MO017 casualty-records rationale replaced as proposed.

## Advisories

- **TM-A1** (accepted applied): NM002: Slough's March 29 enemy-loss estimate (40 to 60 killed, probably over 100 wounded, some 25 prisoners) added and cited; the OR IX OCR line '27 killed j 63 wounded. Total, 90.' after Chivington's No. 3 report recorded in open_questions as of unclear attribution, not used as evidence.
- **TM-A2** (accepted applied): OK004: the No. 5 return's aggregate column read as 37, 4 and 22, summing to 63 (a computation), recorded as a compiled-return reading distinct from Cooper's figures and the frozen CS 150; three row citations added; memo updated.
- **TM-A3** (accepted applied): MO015 march-horses-and-ammunition rationale notes that the two ammunition statements may refer to different times; claim stays disputed.
- **TM-A4** (accepted applied): NM001: Canby's 'But see revised statement on p. 493' footnote noted in the casualty rationale and cited; Sibley's poorly armed, thinly clad brigade dated to mid-January 1862 'at this point' in a report dated at Fort Bliss, with the sentence cited.
- **TM-A5** (accepted applied): AR001 stand-and-envelopment: 'Halleck's orders' replaced by the orders of 'the general' of February 22 (not named in the passage); the sentence is cited.
- **TM-A6** (accepted applied): MO014: Buel's stone wall added to the terrain claim (noting Britton's dependence on the reports); Buel's 65-man Herington detachment against Britton's forty added to reported-force-scope, both cited.
- **TM-A7** (accepted applied): MO015 (US 800/800) and MO016 (US 1,500/1,500) frozen numeric bounds cited as cwsac_forces cells and named in the values/rationales.
- **TM-A8** (accepted applied): Boston Mountains memo sentence now says Confederate wounded found in houses gave their loss as 150 killed and wounded, per Blunt, matching the OK004 value.

This AI review is a separate analysis, not historical adjudication or proof of source independence.
The dossiers remain drafts; no model input changes.
