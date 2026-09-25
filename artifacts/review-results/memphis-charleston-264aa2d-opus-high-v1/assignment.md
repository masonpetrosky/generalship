# Operations on the Memphis & Charleston Railroad: bounded separate source review

Review prepared commit `264aa2d675e3533e1c2c581eda914ccabf7111cb` against `e0fa3588df0ac462d12a0f25e022b77bd00dd65f`. Sibling inputs.json binds
30 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Intervening commits between the prepared commit and the bundle may include other campaigns' review corrections; they are out of scope. Verify input hashes against `git show 264aa2d675e3533e1c2c581eda914ccabf7111cb:<path>`, and read any bound path that differs in the worktree from the prepared commit.

Scope: the sole frozen record, TN022 (Collierville, November 3, 1863), in **Operations on the Memphis & Charleston Railroad [November 1863]**. Inspect all **9 claims / 41 citation occurrences**, including **1 null unknown** and seven dimensions, source metadata, memo and report. Read the retained live NPS summary and the new Hatch and Chalmers selections reusing the pinned `or31-1-illinois-ocr-v1` (which must be unchanged). Check cited frozen cells and the battle/force/commander row sets. No network, new research, extra source families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence, and that OCR readings are reported rather than silently corrected. Check: scope (the Quinn's Mill picket, the Coldwater stand and the November 4 pursuit); the force comparison (Hatch's 850 against the imported bounds; no Confederate count); the casualty comparison (Hatch's "will not exceed 60"; Chalmers's 6/63/26 and the garbled return's 95); Chalmers's change of plan and withdrawal; interested-source labels. No automatic attribution to every listed commander and no additive credit. Attributed judgments are not causal effects. No maps, subordinate reports or print were inspected by the author.

Replay all text derivatives: the NPS summary and the two new sectioned selections against their parent. Check the explicit page-marker maps (Hatch pp.243–246 with p.246 printed "24G"; Chalmers pp.247–249 with the p.247 head printed "^47"), including whether any locator relies on a missed or misread header. No extra depth is required to accept explicit unknowns.

At the prepared commit, verify 117/127 dossiers, 10 without, 31/36 complete campaign groups by presence; 541 source records / 522 paths; previous 537 records / 518 raw paths, all 116 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Averell's Raid on the Virginia & Tennessee Railroad [November 1863], WV012.
Check packet JSON blocks and receipt hashes at the prepared commit mechanically. Run `make check` offline.
Do not run build/packet commands, and do not import or call `generalship.cli` functions such as `research_packet` or `build`, which write files; compare packets by reading them. Do not modify primary artifacts. Other campaign reviews may be pending; they are out of scope.

Write only `artifacts/review-results/memphis-charleston-264aa2d-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
