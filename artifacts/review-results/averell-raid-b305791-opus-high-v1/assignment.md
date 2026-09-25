# Averell's Raid on the Virginia & Tennessee Railroad: bounded separate source review

Review prepared commit `b305791dc888d7c9569a6132dfd2a1c36246a775` against `216d15ec2c0bc3782f3564c65aca318bfef7a6b9`. Sibling inputs.json binds
30 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Intervening commits between the prepared commit and the bundle may include other campaigns' review corrections; they are out of scope. Verify input hashes against `git show b305791dc888d7c9569a6132dfd2a1c36246a775:<path>`, and read any bound path that differs in the worktree from the prepared commit.

Scope: the sole frozen record, WV012 (Droop Mountain, November 6, 1863), in **Averell's Raid on the Virginia & Tennessee Railroad [November 1863]**. Inspect all **9 claims / 44 citation occurrences**, including **1 null unknown** and seven dimensions, source metadata, memo and report. Read the retained live NPS summary and the new Averell and Echols selections reusing the pinned `or29-1-illinois-ocr-v1` (which must be unchanged). Check cited frozen cells and the battle/force/commander row sets. No network, new research, extra source families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence, and that OCR readings are reported rather than silently corrected. Check: scope (the November 5 Mill Point skirmish, Duffie's column and the later march); the opposing strength figures (Averell's 1,175 and 4,000; Echols's 1,700, 7,000, 3,500 and 10,000), none adopted; the retreat characterization dispute; the casualty comparison (frozen 526 against live 415; Averell's 100 and 250; Echols's 275); the attribution of success to Moor and of the withdrawal order to Echols; interested-source labels. No automatic attribution to every listed commander and no additive credit. Attributed judgments are not causal effects. No maps, diagrams, subordinate reports or print were inspected by the author.

Replay all text derivatives: the NPS summary and the two new sectioned selections against their parent. Check the explicit page-marker maps (Averell pp.503–508; Echols pp.528–532), including whether any locator relies on a missed or misread header. No extra depth is required to accept explicit unknowns.

At the prepared commit, verify 118/127 dossiers, 9 without, 32/36 complete campaign groups by presence; 545 source records / 526 paths; previous 541 records / 522 raw paths, all 117 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Longstreet's Knoxville Campaign [November-December 1863], TN023, TN025 and TN026.
Check packet JSON blocks and receipt hashes at the prepared commit mechanically. Run `make check` offline.
Do not run build/packet commands, and do not import or call `generalship.cli` functions such as `research_packet` or `build`, which write files; compare packets by reading them. Do not modify primary artifacts. Other campaign reviews may be pending; they are out of scope.

Write only `artifacts/review-results/averell-raid-b305791-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
