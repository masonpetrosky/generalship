# Tullahoma or Middle Tennessee Campaign: bounded separate source review

Review prepared commit `d6824e51b354adffce6d255775a1e6888cbfdab0` against `d3eddc0dae19ec6cfb5241a2b40114b2c971f073`. Sibling inputs.json binds
32 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Scope: the sole frozen record, TN017 (Hoover's Gap), in **Tullahoma or Middle Tennessee Campaign [June 1863]**. Inspect all **9 claims / 41 citation occurrences**, including **1 null unknown** and seven dimensions, source metadata, memo and report. Read the retained live NPS summary, the new Cist selection reusing the pinned `cist-cumberland-ocr-v1` (which must be unchanged), and the new Bate selection from the newly pinned Official Records Volume XXIII Part 1 OCR and metadata. Check cited frozen cells and the battle/force/commander row sets. Whole-book reading is not required. No network, new research, extra source families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence, and that OCR readings are reported rather than silently corrected. Check: the scope treatment of Liberty Gap (a live NPS "other name" but a separate action in Cist, whose 231 losses are not added); force scopes (Cist's army-wide 43,089; Bate's "less than 700" and "650 engaged"); the casualty comparison (frozen Unknown; live 583 with CS 0; Bate's 146); attributed judgments; the choice of Bate's report because the frozen commander Stewart has no report in the volume's list; and the OR XXIII Part 1 registry records' statement that the imprint year was not read. No automatic attribution to every listed commander and no additive credit. Attributed judgments are not causal effects. No maps, returns or print were inspected by the author.

Replay all text derivatives: the NPS summary and the two new sectioned selections against their parents. Check the explicit page-marker maps (Cist pp.154–163 with p.161 printed "1G1"; Bate pp.611–614), including whether any locator relies on a missed or misread header. No extra depth is required to accept explicit unknowns.

Verify 102/127 dossiers, 25 without, 25/36 complete campaign groups by presence; 474 source records / 464 paths; previous 468 records / 458 raw paths, all 101 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Morgan's Raid in Kentucky, Indiana, and Ohio [July 1863], IN001, OH001 and OH002.
Check packet JSON blocks and receipt hashes mechanically. Run `make check` offline.
Do not run build/packet commands, and do not import or call `generalship.cli` functions such as `research_packet` or `build`, which write files; compare packets by reading them. Do not modify primary artifacts. Other campaign reviews may be pending; they are out of scope.

Write only `artifacts/review-results/tullahoma-d6824e5-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
