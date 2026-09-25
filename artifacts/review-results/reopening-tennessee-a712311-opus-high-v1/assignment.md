# Reopening the Tennessee River: bounded separate source review

Review prepared commit `a71231105d0b86140739ffb20163311fa2439ac1` against `35ecf46496fdcb9515e0fd68a54d3a94d24e1552`. Sibling inputs.json binds
32 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Intervening commits between the prepared commit and the bundle may include other campaigns' review corrections; they are out of scope. Verify input hashes against `git show a71231105d0b86140739ffb20163311fa2439ac1:<path>`, and read any bound path that differs in the worktree from the prepared commit.

Scope: the sole frozen record, TN021 (Wauhatchie, October 28–29), in **Reopening the Tennessee River [October 1863]**. Inspect all **9 claims / 40 citation occurrences**, including **1 null unknown** and seven dimensions, source metadata, memo and report. Read the retained live NPS summary, the new Cist selection reusing the pinned `cist-cumberland-ocr-v1` (which must be unchanged), and the new Bratton selection from the newly pinned Official Records Volume XXXI Part 1 OCR and metadata. Check cited frozen cells and the battle/force/commander row sets. No network, new research, extra source families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence, and that OCR readings are reported rather than silently corrected. Check: the scope treatment of Brown's Ferry (a live other name; the October 27 landing before the frozen interval, not added); the casualty comparison (frozen 828 against live 572; Cist's 437 and "unknown"; Bratton's 356 brigade total with a row missing a figure in OCR); the use of Bratton because Jenkins, the frozen commander, has no report in the list; the order-to-withdraw attribution; interested-source labels. No automatic attribution to every listed commander and no additive credit. Attributed judgments are not causal effects. No maps, Longstreet or Law reports, Union reports, returns or print were inspected by the author.

Replay all text derivatives: the NPS summary and the two new sectioned selections against their parents. Check the explicit page-marker maps (Cist pp.232–233 and 237–242 with p.240 printed "24:0"; Bratton pp.231–233), including whether any locator relies on a missed or misread header. No extra depth is required to accept explicit unknowns.

At the prepared commit, verify 116/127 dossiers, 11 without, 30/36 complete campaign groups by presence; 537 source records / 518 paths; previous 531 records / 512 raw paths, all 115 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Operations on the Memphis & Charleston Railroad [November 1863], TN022.
Check packet JSON blocks and receipt hashes at the prepared commit mechanically. Run `make check` offline.
Do not run build/packet commands, and do not import or call `generalship.cli` functions such as `research_packet` or `build`, which write files; compare packets by reading them. Do not modify primary artifacts. Other campaign reviews may be pending; they are out of scope.

Write only `artifacts/review-results/reopening-tennessee-a712311-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
