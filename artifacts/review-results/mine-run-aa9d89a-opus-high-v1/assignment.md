# Mine Run Campaign: bounded separate source review

Review prepared commit `aa9d89a677415b4474ee3790dd7ed7f2aeb56530` against `535f423`. Sibling inputs.json binds
30 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Intervening commits between the prepared commit and the bundle may include other campaigns' review corrections; they are out of scope. Verify input hashes against `git show aa9d89a677415b4474ee3790dd7ed7f2aeb56530:<path>`, and read any bound path that differs in the worktree from the prepared commit.

Scope: the sole frozen record, VA044 (Mine Run, November 27 to December 2, 1863), in **Mine Run Campaign [November-December 1863]**. Inspect all **9 claims / 72 citation occurrences**, including **1 null unknown** and seven dimensions, source metadata, memo and report. Read the retained live NPS summary, the new Humphreys Chapter III selection reusing the pinned `humphreys-ocr-v2` (which must be unchanged), and the new Lee selection from the already pinned Official Records Volume XXIX Part 1 OCR `or29-1-illinois-ocr-v1` (which must be unchanged). Check cited frozen cells and the battle/force/commander row sets. No network, new research, extra source families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence, and that OCR readings are reported rather than silently corrected. Check: scope (Payne's Farm, New Hope Church and the Mine Run lines; the November 26 crossing and December 2 pursuit as edge context); strength statements (Humphreys's infantry figures, his three-corps comparison, the footnote officer figures summing to 1,436 against his 1,321 as a computation, Meade's belief against the returns, Lee's 'greatly exceeding'), none adopted against the imported frozen bounds; the terrain claim's decision not to tag the Mine Run works `inherited`; the Rosser raid figures (Lee's 18 wagons/150 prisoners against Humphreys's eight wagons/ninety-five prisoners); the Payne's Farm outcome dispute (Lee, Humphreys, NPS); Johnson's loss (498 against 545); prisoners/stragglers; the live 'Major General' rank for Lee, not adopted; interested-source labels, including Humphreys as the Army of the Potomac's chief of staff per his publisher's list. No automatic attribution to every listed commander and no additive credit. Attributed judgments are not causal effects. No Union or other Confederate reports, maps, returns or print were inspected by the author; the No. 99 field return was seen but not selected.

Replay all text derivatives: the NPS summary and the two new sectioned selections against their parents. Check the explicit page-marker maps (Humphreys pp.49–70 with heads read 'SO', '5 1', '$6', '6l', '6?' and 'JO' for pp.50, 51, 56, 61, 67 and 70, no p.60 head, and the 'p.59 or p.60' locators; Lee pp.823–830), including whether any locator relies on a missed or misread header. No extra depth is required to accept explicit unknowns.

At the prepared commit, verify 124/127 dossiers, 3 without, 35/36 complete campaign groups by presence; 568 source records / 548 paths; previous 564 records / 544 raw paths, all 123 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Operations about Dandridge [December 1863-January 1864], TN027, TN028 and TN029.
Check packet JSON blocks and receipt hashes at the prepared commit mechanically. Run `make check` offline.
Do not run build/packet commands, and do not import or call `generalship.cli` functions such as `research_packet` or `build`, which write files; compare packets by reading them. Do not modify primary artifacts. Other campaign reviews may be pending; they are out of scope.

Write only `artifacts/review-results/mine-run-aa9d89a-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
