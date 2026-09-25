# Primary assessment: Price's Missouri, Mobile Bay, Mobile and Wilson's Raid first passes review

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `5d5bc1c2eb9152227a63ea8a92f3850a40bd124f`. Its
SHA-256 is `6c427a0a7e717af40ff91fe7d9f5f05fc805c384a7cc5ac48f9ddf7be0ca32c1`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `27ee4e505b5bbffa0f348e8305f418fe00a6d611`; see [dispatch.json](dispatch.json).

Each required finding was checked against the retained source text before it was applied, and every
added quote occurs exactly once in its section; `python3 -m generalship check` passes. Superseded
dossiers are archived under `data/evidence/history/`. [correction.json](correction.json) binds the
corrected dossiers.

## Required findings

- **PRV-R1** (accepted applied): Holds: Britton p.443 says the couriers from Sanborn did not reach Blunt; p.442 says Blunt sent couriers to Sanborn without saying whether they arrived. MO023 scouts-and-intelligence value now reads that Blunt sent couriers to Sanborn but no couriers from Sanborn reached him; p.442 sending passage cited.
- **PRV-R2** (accepted applied): Holds: Price p.629 is passive ('when a charge was ordered and made in the most gallant manner'). MO021 command-roles value now says a charge was ordered about 2 p.m. without naming who ordered it; that p.629 passage (running head 'G29') cited.
- **PRV-R3** (accepted applied): Holds: May 3 OCR p.351 reads 't’loosaod seven hundred prisoners, including 150'; 'officers' is absent. AL007 casualty-records value now quotes the reading and says the thousands figure and the word after 150 are illegible; Wilson memo no longer frames it as disagreeing with the frozen CS 2,700.
- **PRV-R4** (accepted applied): Holds: v1 carried group britton-civil-war-on-border-1899 while parent britton-civil-war-border-2-ocr-v1 and britton-camden-selections-v1 carry britton-civil-war-border-1899. Registered metadata_only successor britton-price-missouri-selections-v2 (supersedes v1, metadata SHA-256 c44ed0f7... recomputed and matching the review) with corrected group and dependency note; all Britton citations in the 11 Price dossiers moved to v2 with quotes, sections and locators unchanged; memo group reference corrected.

## Advisories

- **PRV-A1** (accepted applied): Price names only 'the crossing of the Osage' and 'the prairie beyond the river'. Sentence added to MO028 reported-force-scope and hold-until-night rationales and to the Price memo.
- **PRV-A2** (accepted applied): MO021 fortification-intelligence now cites both the frozen/NPS reason (Price dismissed mounting guns) and Britton's council-of-war account (Price concurred in Mackey's bombardment advice; assault chosen over reported colored garrison and revenge on Ewing); claim set to disputed. 'a company of negroes was also organized' (p.395) cited in reported-force-scope.
- **PRV-A3** (accepted applied): Price memo: 25 records added at merge (not 27), Britton parent and group named; Mobile Bay memo: 4 records (not 6), OR XXXIX parent named as or39-1-illinois-ocr-v1 and the reconcile-at-merge request removed.
- **PRV-A4** (not adopted): Source records not changed: metadata successors for or41-1-price-missouri-selections-v1 and or49-1-wilson-selma-selections-v1 for an advisory note would move every Price citation again. The same-author links (price-camden-1864-report; wilson-south-side-raid-reports) are recorded in the Price and Wilson memos under the docs/sources.md same-author rule.
- **PRV-A5** (accepted applied): Wilson's May 3 OCR 'Taylor had left at3' cited in AL007 recorded-result and added to the Wilson memo's Taylor dispute as a third, garbled account.
- **PRV-A6** (accepted applied): AL003 recorded-result now cites NPS 'Farragut forced the Confederate naval forces, under Adm. Franklin Buchanan, to surrender' and Mahan 'the United States flag hoisted on board the Tennessee at ten o'clock.' (p.244).
- **PRV-A7** (accepted applied): Britton says Fagan's division was brought forward 'to the support of Marmaduke and Shelby'. MO024 reported-force-scope value reworded (Shelby waded to form on Marmaduke's left; Fagan brought forward in support); two p.446 passages cited.
- **PRV-A8** (kept as is): Informational: the Union side of Price's expedition resting on NPS and Britton, and AL006 lacking a Confederate family, are already the memos' stated consequential gaps. Noted in the Mobile memo's review section; no evidence change.
- **PRV-A9** (kept as is): Confirms MO022 frozen-description handling; no change.

This AI review is a separate analysis, not historical adjudication or proof of source independence.
The dossiers remain drafts; no model input changes.
