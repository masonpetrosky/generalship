# Morgan's Raid in Kentucky, Indiana, and Ohio: bounded separate source review

Review prepared commit `11c96f5d5ac5de7a6f31c3d76d36422283777360` against `8546a8f6a53f671b2a91863e48b746dd1f03a777`. Sibling inputs.json binds
42 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Intervening commits: after the prepared commit and before this bundle, commits `1a0ba8b`
(Tullahoma review correction: TN017 and three OR XXIII Part 1 `metadata_only` records) and
`567e7b1` (Gettysburg review correction: ten dossiers and three Humphreys `metadata_only`
records) changed README, docs, `data/sources.json` (six appended records only), packets and
receipts. They are out of scope. Verify input hashes against `git show 11c96f5d5ac5de7a6f31c3d76d36422283777360:<path>`,
and read any bound path that differs in the worktree from the prepared commit.

Scope: all three frozen records, IN001 (Corydon), OH001 (Buffington Island) and OH002 (Salineville), in **Morgan's Raid in Kentucky, Indiana, and Ohio [July 1863]**. Inspect all **28 claims / 143 citation occurrences**, including **3 null unknowns** and seven dimensions per record, source metadata, memo and report. Read the three retained live NPS summaries; the new Duke selection from the newly pinned *History of Morgan's Cavalry* OCR and metadata; and the new Burnside, Hobson and Shackelford selections reusing the pinned `or23-1-illinois-ocr-v1` (which must be unchanged). Check cited frozen cells and the battle/force/commander row sets. Whole-book reading is not required. No network, new research, extra source families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence, and that OCR readings are reported rather than silently corrected. Check:
- the treatment of raid-wide figures (start strength, Burnside's 3,000 on entering Indiana, the July 2–26 Union return, NPS's raid totals, Duke's campaign judgments), none of which may be assigned to one record or added;
- force scopes at each battle (Duke's 2,460, 1,900 and 250; Hobson's 2,500 on July 6; Shackelford's 500, 375 and 400) against the imported frozen bounds;
- the casualty comparisons (IN001 frozen 401 against live 411; the return's total row arithmetic and its bearing on Corydon; Buffington's Duke and Hobson figures; Salineville's 350 and 230 against 364);
- the Buffington escape dispute, Hobson's protest at Judah's command, and the Burbeck surrender dispute;
- Duke's status as an interested participant who was captured on July 19 and was absent from Morgan's conference with Bragg;
- attributed judgments, and the Salineville scope question (Way's morning fight versus the afternoon surrender).
No automatic attribution to every listed commander and no additive credit. Attributed judgments are not causal effects. No maps, returns beyond the compiled Union return, or print were inspected by the author.

Known inherited issue: the Tullahoma review (TL-R7) found that the OR XXIII Part 1 records' edition text wrongly says the imprint year was not read (the OCR title reads "1889." at parent offset 1084). The three Morgan's Raid OR selections copied that text; the primary will issue `metadata_only` revisions for them in this campaign's correction. You may confirm this; no separate finding is needed unless the proposed fix is wrong.

Replay all text derivatives: the three NPS summaries and the four new sectioned selections against their parents. Check the explicit page-marker maps (Duke pp.407–461, including p.454 printed "45-1", p.455 printed "456" with an inferred locator, p.458 printed "HISTORY OP" and the p.459 plate caption; OR pp.635–662), including whether any locator relies on a missed or misread header. No extra depth is required to accept explicit unknowns.

At the prepared commit, verify 105/127 dossiers, 22 without, 26/36 complete campaign groups by presence; 486 source records / 476 paths; previous 474 records / 464 raw paths, all 102 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Chickamauga Campaign [August-September 1863], TN018, GA003 and GA004.
Check packet JSON blocks and receipt hashes at the prepared commit mechanically. Run `make check` offline in the worktree.
Do not run build/packet commands, and do not import or call `generalship.cli` functions such as `research_packet` or `build`, which write files; compare packets by reading them. Do not modify primary artifacts. Other campaign reviews may be pending; they are out of scope.

Write only `artifacts/review-results/morgans-raid-11c96f5-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
