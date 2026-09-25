# Separate review: 1864 Western small-operation first passes (15 records)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a fresh-context `evidence-reviewer` subagent, and the author's conversation was not an input. The invoking task ID was not visible to the reviewer.
- **Date:** 2026-09-25
- **Commits:** prepared `498672483393892b357469264e256bbddd017e09`, compared against previous `6945fabb749f35bc0bde68ef37122b5192596735`; the review bundle is at `de84c1da12f274d6b0e177329a539b86e073cce3` (worktree HEAD).
- **Assignment:** `assignment.md` sha256 `8f7fd7632d54b0e0100454b54aedb560797be6cae1c34200c429ea3c2665ff26`.
- **Input manifest:** `inputs.json` sha256 `15c9c75543167529e7329a5e7efafb51cb66e2f404505b63abcd7059b7fc6e81`.
- **Hash verification:** all 101 bound paths match `git show 4986724…:<path>` and the worktree. There were **no mismatches**.
- **`make check` (offline):** `Ran 134 tests … OK`, and `python -m generalship check` exited 0. I ran no build, packet or network commands.
- **Outcome:** **corrections required** (7 required findings, all small extraction or scope fixes). There are 18 advisories.

This is an AI review. It is not human historical adjudication, not independent corroboration, and not feature admission. No dossier is admitted or promoted by it.

## Scope actually inspected

- **Docs:** AGENTS.md, `docs/methodology.md`, `docs/evidence-contract.md`, `docs/cohort-v2.md`, and all ten assigned memos in full.
- **Dossiers:** all 15 (AL002, MS012, MS013, GA006, KY010, TN030, MS014, MS015, TN031, KY011, VA076, TN033, VA081, VA082, AR017). That is 137 claims, 15 null unknowns and 778 citation occurrences, every one read against its cited section.
  - Counts, dimension coverage, null-for-unknown, `draft` status, null replacement dates and phase tags (no `inherited`) all match the memos.
- **Registry:** all 58 added source records were checked against `6945fab`. There are 58 additions, with no changes to or removals of earlier records.
  - I read the author, date and date-map, dependency and inspection fields for all 28 selection records and all 15 NPS text records.
  - All 28 selection files reproduce their recorded parent character ranges exactly (whitespace-collapsed), and all parent hashes match.
  - Independence groups were cross-checked for same-author consistency across the whole registry.
- **Selections read in full:**
  - All 15 NPS text pages.
  - Dodge, Rawlins, Sherman, Polk, W. Sooy Smith, Forrest (Okolona), Thomas, Johnston, Hicks, Forrest (West Tennessee), Leaming, Sturgis, Forrest (Mississippi), A. J. Smith, S. D. Lee, Washburn, Burbridge (Cynthiana and Saltville), A. E. Jackson, Gardner, both Breckinridge selections, Mower and Greene.
- **Selections read partly:**
  - Jordan (Memphis): the context around every cited passage, but not read end to end.
  - Morgan: the June 11 letter in full; the July 20 report by context around every cited passage.
  - Gillem: in full through the Bull's Gap evacuation and the start of the retreat.
  - Stoneman: the telegram in full; the January 6 report by context around every cited passage.
- **HTML snapshots:** checked by hash only.
- **Pinned parent OCR:** consulted only at bounded offsets to test inspection and label statements, with no new source families:
  - Thomas's transmittal sentence after the selected range;
  - the compiler footnote after Johnston's Dalton excerpt;
  - Rawlins's adjacent February 2 dispatch;
  - the dateline of Forrest's address;
  - OR XXXIX pt. 1 text between Gardner's report and Jackson's No. 10.
- **Frozen CSVs:** battle, force and commander rows for all 15 records.
- **Not done:** no new research, no print verification, and no attempt to resolve historical disputes.

## Assessment of the specific choices asked about

- **TN030 `killing-after-assault`: sound.**
  - Every statement is attributed to its writer and date: NPS (undated modern summary); Leaming (January 17, 1865); Forrest (April 15 letter to Jack, April 26 report, May 16 letter, June address).
  - The claim's own voice goes no further than "The accounts conflict". No characterization or count is adopted, the status is `disputed`, and the uninspected Joint Committee report and other survivors' reports stay visible.
  - Advisories A7 and A8 suggest two balancing passages.
- **VA076 `shooting-of-wounded-prisoners`: sound.**
  - NPS's hedged "were said to have" is kept. Gardner's report is attributed to him, identity rests explicitly on "as I believe", and the October 7 shooters are correctly left unidentified.
  - No count is adopted and no deaths are added to casualties. The "no Confederate account inspected" wording is accurate but could be sharper (A13).
- **AL002: acceptable and transparent.**
  - The Confederate side rests on Union accounts and NPS, and this is recorded as the consequential gap.
  - Counting Rawlins as a family is acceptable as an effort count. However, his January 29 dispatch has no stated source; dependence on Dodge is inferred from matching figures. That is correctly disclosed in the registry, but the memo table's "3" families could mislead (A1).
- **Fourth-family follow-ups: within the methodology's one targeted follow-up.**
  - MS015 (S. D. Lee): the listed senior Confederate commander.
  - TN031 (Jordan and Pryor): adds Confederate detail but is explicitly not independent of Forrest.
  - VA076 (Gardner): the witness report for the most consequential gap.
- **OCR dates: handled correctly.**
  - Garbled dates are mapped null: Forrest address "June ^8", Gardner "2G", Jackson letter "<S", Maury relay.
  - Others are mapped with a note: Dodge "18G4", Forrest "Ajwil".
  - Printed dates that do not fit are kept and flagged: Hicks "April 6 / 25th instant", Jackson "October 2, 5 p.m.".
  - One further unfit date was missed: Forrest's "evening of the 26th" (KY010-R1).
- **Johnston's October 20, 1864 report in `johnston-atlanta-report`: supported.**
  - Same date and place (Vineville), and the compiler's footnote after the excerpt reads "Portion of report here omitted will appear in connection with the Atlanta campaign" (see A4 for its volume reference).
- **Breckinridge's 1864 reports in `breckinridge-baton-rouge-1862-report`: consistent.**
  - That group already holds his New Market selection, and no other Breckinridge group exists.
  - Other groupings also check out: Forrest's 1864 selections are all in `forrest-1864-reports`, both Burbridge selections share one group, Sturgis joins his existing group, and Thomas joins his existing group.
  - The new author groups have no earlier registry appearance: Dodge, Rawlins, Hicks, Leaming, W. Sooy Smith, S. D. Lee, A. J. Smith, Washburn, J. H. Morgan, A. E. Jackson, Gardner, Gillem, Stoneman, Mower and Colton Greene.

## Required corrections

Each correction adds text and/or one citation. No existing citation needs removal. The matching memo sentence should be updated in parallel. All quotes below were verified to occur exactly in the named section.

### KY010-R1: unflagged conflict in Forrest's printed attack date

**Problem.** Forrest's March 27 dispatch (already cited four times in KY010) says he "attacked it on the evening of the 26th". This conflicts with:
- the frozen date, March 25;
- Hicks's "25th instant";
- Forrest's own surrender demand as printed by Hicks, dated March 25.

The dossier and memo flag only Hicks's printed date.

**Correction.** `KY010` / `recorded-result`:
- **value:** append: "Forrest's March 27 dispatch dates the attack 'on the evening of the 26th', against the frozen March 25, Hicks's '25th instant' and Forrest's own surrender demand dated March 25 as printed by Hicks; the dispatch's date is kept and not reconciled."
- **add citation:**
  - `{"source_id": "or32-1-forrest-west-tennessee-1864-selections-v1", "section": "forrest-1864-03-27", "locator": "p.607 (OCR page markers; not checked against print)", "quote": "attacked it on the evening of the 26th"}`
  - `{"source_id": "or32-1-hicks-paducah-selections-v1", "section": "hicks-1864-04-06", "locator": "p.547 (OCR page markers; not checked against print)", "quote": "Headquarters Forrest’s Cavalry Corps, Paducah, Ky ., March 25, i864."}`
- **Memo:** in the "Dates" bullet, add the same sentence.

### KY011-R1: NPS prisoner figure omitted

**Problem.** The NPS Description gives about 1,300 Union prisoners held overnight after the 11th. This bears directly on the dossier's unsupported inference that the frozen US 1,092 "presumably includes the men captured on the 11th", but it is not recorded.

**Correction.** `KY011` / `casualty-records`:
- **value:** after "…says 2,500 prisoners were paroled.", insert: "NPS says Morgan had about 1,300 Union prisoners camping with him overnight after the 11th."
- **rationale:** replace "the frozen Union 1,092 presumably includes the men captured on the 11th, but no inspected source states it." with "NPS's about 1,300 prisoners of the 11th and Morgan's 400 and 1,500 (or 2,000) surrendered bear on the frozen Union 1,092, but no inspected source states its basis."
- **add citation:** `{"source_id": "nps-ky011-v1", "locator": "Description", "quote": "Altogether, Morgan had about 1,300 Union prisoners of war camping with him overnight in line of battle."}`

### TN031-R1: Washburn's own "500 prisoners" figure omitted and misattributed in the dispute

**Problem.** Washburn's report prints his August 21 dispatch No. 2 to A. J. Smith: "He has 500 prisoners, I think". The dossier gives Washburn only "about 250", and the memo attributes 500 to NPS alone. The defender's own count changes across his documents (about 250, 500, then 116 officers and men captured or missing), and that change is part of the dispute.

**Correction.** `TN031` / `casualty-records`:
- **value:** replace "his first dispatch says about 250 hundred-days' men were captured." with "his first dispatch says about 250 hundred-days' men were captured, and his second dispatch to Smith, printed in the report, 'He has 500 prisoners, I think'."
- **rationale:** replace "the prisoner counts differ (about 250, 400, 500, some 600) and none is adopted." with "the prisoner counts differ (Washburn about 250 and 500; Forrest 400; NPS 500; Jordan some 600) and none is adopted."
- **add citation:** `{"source_id": "or39-1-washburn-memphis-selections-v1", "section": "washburn-1864-09-02", "locator": "p.470 (OCR page markers; not checked against print)", "quote": "He has 500 prisoners, I think, but failed to take the battery"}`
- **Memo:** change "prisoners: about 250 (Washburn), 400 (Forrest), 500 (NPS) and some 600 (Jordan)" to "prisoners: about 250 and 500 (Washburn's two dispatches), 400 (Forrest), 500 (NPS) and some 600 (Jordan)".

### VA081-R1 and VA082-R1: scope of Breckinridge's "not more than twenty prisoners" misstated

**Problem.** In the postscript, the twenty is what remains after two exclusions:
- Breckinridge has "no report yet from Vaughn and Duke of the prisoners from their command". Duke's command fought at Marion.
- He says most prisoners were citizens, afterward turned loose.

The dossiers say "taken from his troops" (VA081) and "not more than twenty of his men … in the whole expedition" (VA082). Both overstate the scope.

**Correction.** `VA081` / `casualty-records`:
- **value:** replace "he says not more than twenty prisoners were taken from his troops, most at Saltville." with "in his postscript, saying he had no report yet from Vaughn and Duke of prisoners from their commands and that most prisoners taken were citizens afterward released, he says that for the rest not more than twenty were taken, most at Saltville."
- **add citation:** `{"source_id": "or45-1-breckinridge-swva-selections-v1", "section": "breckinridge-1865-01-03", "locator": "p.827 (OCR page markers; not checked against print)", "quote": "I have no report yet from Vaughn and Duke of the prisoners from their command, but I know that most of the prisoners taken by the enemy were citizens, afterward turned loose"}`

**Correction.** `VA082` / `casualty-records`:
- **value:** replace "Breckinridge says not more than twenty of his men were taken prisoner in the whole expedition, most at the capture of Saltville," with "Breckinridge, excluding Vaughn's and Duke's commands (no report yet) and the citizens he says made up most prisoners, says not more than twenty others were taken, most at the capture of Saltville,"
- **add citation:** the same citation as VA081-R1.

### TN030-R1: NPS statement in the terrain value lacks a citation

**Problem.** The `bluff-fort-and-commanding-ground` value attributes to NPS "artillery that could not be depressed to cover the approaches". None of the three NPS quotes cited supports it. The page does support it.

**Correction.** `TN030` / `bluff-fort-and-commanding-ground`:
- **add citation:** `{"source_id": "nps-tn030-v1", "locator": "Description", "quote": "The garrison was unable to depress its artillery enough to cover the approaches to the fort"}`

### GA006-R1: the "refugee" label is not supported by the cited passage

**Problem.** Inclosure No. 4 is headed "JOHN W. GLADDEN'S STATEMENT", and Gladden says he "was himself upon the field and also heard it from officers". The word "refugee" appears only in Thomas's transmittal sentence, which falls after the selected range (parent OCR, about char 53,381: "a statement of a refugee from Dalton"). The label is Thomas's characterization and matters for the statement's basis.

**Correction.** `GA006`:
- In `reported-force-scope`, replace "a refugee's statement forwarded with his report" with "John W. Gladden's statement, submitted by James Lamon and forwarded with Thomas's report,".
- In `transport-and-forage`, replace "The refugee's statement" with "Gladden's statement".
- In `casualty-records`, replace "The refugee's statement" with "Gladden's statement".
- In `open_questions[1]`, replace "the refugee's statement" with "Gladden's statement (which Thomas's transmittal, outside the selection, calls a refugee's)".
- **Add citation** to `reported-force-scope`: `{"source_id": "or32-1-thomas-dalton-selections-v1", "section": "thomas-inclosure-4-gladden-statement", "locator": "p.13 (OCR page markers; not checked against print)", "quote": "JOHN W. GLADDEN’S STATEMENT. Says he left Dalton on Saturday last."}`
- **Memo and registry:** make the same wording change in the memo. For `or32-1-thomas-dalton-selections-v1.dependency_note`, use a metadata-only revision if that is wanted, not an in-place edit.

## Advisories (optional; no correction required)

**Family counts and source basis**

- **A1 (AL002, memo):** In the family table, annotate "3" as "3 (Rawlins's dispatch not independent of Dodge)". The effective independent witnesses are NPS/CWSAC and Dodge.
- **A2 (AL002):** The frozen force field names the 1st Alabama Cavalry. Dodge's report names "Patterson's and Hannon's regiments". The rationale could note that the unit names differ, without resolving them.

**Omitted figures and statements within the selected passages**

- **A3 (MS013):** Two items could be recorded:
  - Sherman's March 7 report, already inspected in the campaign's Sherman selection, calls Smith's delay "unpardonable". Adding it would be the record's one follow-up; otherwise note it in `open_questions`.
  - Forrest's February 26 letter gives enemy losses as "6 pieces of artillery, 100 killed, over 100 prisoners, and wounded estimated at 300 or over". This could join `casualty-records` beside his 800.
- **A4 (GA006):** Cite the compiler footnote ("Portion of report here omitted will appear in connection with the Atlanta campaign, Vol. XXXVIII, Part II") as the basis for the same-document grouping, and note a mismatch: the registered Atlanta selection is from Part 3 (No. 597). Also, the Inclosure No. 5 total row has an asterisk whose footnote was not selected.
- **A5 (MS014):** Sturgis reports a captured sergeant's estimate of 12,000 engaged plus two infantry divisions in reserve. This could join the strength figures.
- **A6 (MS015):** A. J. Smith gives the Old Town Creek force (inside the frozen interval) as "numbering perhaps 1,000 men". It could be recorded as a scoped estimate.
- **A7 (TN030):** For balance within the killing dispute, Leaming himself says that before the surrender "one company of the Sixth U. S. Heavy Artillery, colored troops, rushed down the bluff" and many jumped into the river throwing away arms. This bears on Forrest's "retreated toward the river" account.
- **A8 (TN030):** Leaming states that Bradford, a listed commander, "was brutally murdered the first night of his capture". It could be recorded, as Leaming's statement, in `command-roles` or the killing claim.
- **A9 (KY010):** Hicks says Forrest's 35–40 captured "were convalescents in the general hospital". This context belongs with the 35–40 figure.
- **A10 (KY011):** Two scope notes for Burbridge's casualty list:
  - It is "the loss of my immediate command", not all brigades over the raid.
  - Its footnote says many of the missing later returned.
- **A11 (TN031):** Jordan puts the infantry Neely attacked at "at least a thousand strong". This is a defender-strength figure from the follow-up.
- **A12 (VA081/VA082):** Breckinridge's "The prisoners, including the wounded left in our hands, will reach 200" and "at least 800 horses" are expedition-scope Union losses. They could be recorded as context, not assigned.

**Inspection records, dates and wording**

- **A13 (VA076):** Tighten the inspection record in two places:
  - The registry inspection list omits the No. 4 McLean First Division itinerary (pp.555–556), which follows Gardner's indorsements. It gives "4,200 effective men" and attributes Lieutenant Smith's killing to "the guerrilla Champ Ferguson". Record whether it was read.
  - Echols's No. 9, read and not selected, reports Black regiments "badly cut up" but gives no account of the shootings. Consider replacing "no Confederate account of these events was inspected" with "the Confederate reports read (Jackson No. 10, Echols No. 9 and others) give no account of these events".
- **A14 (VA076):** The frozen Arnold description also reads "On the morning of October 1". The date conflict therefore sits inside the frozen record itself, not only between it and NPS.
- **A15 (VA076, registry):** The compiler footnote to Gardner's report (outside the selection) records a duplicate dated October 18, 1864, co-signed by Assistant Surgeon J. T. Harper. This is relevant to the null-mapped date and to authorship.
- **A16 (TN033):** In `recorded-result`, the rationale could say explicitly that Breckinridge's date for driving the rearguard into the gap ("the evening of the 11th") conflicts with Gillem's arrival on the 10th and the attack on the morning of the 11th. Also, Breckinridge's "An attack … was arranged" is passive; `command-roles` states it as "Breckinridge says he arranged".
- **A17 (KY010, TN030):** The boundaries extend one day past single-day frozen intervals (the 26th; the 13th). This is disclosed and tagged `post_outcome` with nothing added to casualties. Keep it explicit if these records are later bounded for features.
- **A18 (all):** Most NPS pages carry wrong Campaign fields: Atlanta, "Operations in Mobile Bat", "Forrest's Defense Of Mississippi", Franklin-Nashville, "Hood's Operations…", "Forrest's Raid Into West Tennessee". All are correctly noted in the NPS inspection fields and not adopted. No action is needed.

## Unresolved (retained, not for this review to settle)

The review leaves these open:
- all opening strengths;
- the Fort Pillow and Saltville killings;
- who commanded the Confederate defense at Saltville I;
- the Bull's Gap and Marion date and encounter disputes;
- all frozen or live casualty bases without an inspected source.

Findings: KY010-R1, KY011-R1, TN031-R1, VA081-R1, VA082-R1, TN030-R1, GA006-R1; advisories A1–A18.
