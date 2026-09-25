# Chancellorsville Campaign: bounded separate source review

Review prepared commit `c3a49116df083863dee0a0ddf7d1947cb2d000ba` against `0f341660bdb72868683b27842fd6597eec8b8182`. Sibling inputs.json binds
42 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Scope: all three frozen records, VA032, VA034 and VA033, in **Chancellorsville Campaign [April-May 1863]**. Inspect all **27 claims / 119 citation occurrences**, including **3 null unknowns** and seven dimensions per dossier, source metadata, memo and report. Read the three retained live NPS summaries, the new Doubleday selection (with its newly pinned OCR and catalog metadata), and the three new selections from the already pinned Official Records Volume XXV Part 1 OCR (Lee's September 21 report, Sedgwick's May 15 report, Early's May 7 report). Check cited frozen cells and the battle/force/commander row sets. Whole-book reading is not required. No network, new research, extra source families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence, and that OCR readings are reported rather than silently corrected. Check: the nesting of VA033 and VA034 inside VA032's frozen interval and that Doubleday's campaign losses table, Sedgwick's 4,925 and Early's division total are not assigned or added; force scopes (VA032 frozen structured bounds 97,382 / 57,352 kept as imported; Doubleday's rolls, effective and relayed figures; unit-level "Corps" for VA033 and VA034); casualty texts against live zeros; attributed judgments by Doubleday on Hooker and Howard and by Lee on his subordinates; Early's flag-of-truce statement; the rank conflicts (live Lee Major General; frozen Jackson Major General against Lee's "Lieutenant-General"); Doubleday's status as an interested participant; and the two explicit inferred Doubleday locators (Hooker's injury on p.54; the losses table between the p.69 and p.73 markers). No automatic attribution to every listed commander and no additive credit across overlapping intervals. Attributed judgments and counterfactuals are not causal effects. No original manuscripts, returns, maps, Hooker's testimony or print were inspected by the author.

Replay all text derivatives: three NPS summaries, the Doubleday selection against its new parent, and the three OR selections against the existing parent. Check the explicit page-marker maps. Check the Doubleday registry records' edition, preface-date and dependency claims against the OCR title/preface and catalog metadata. No extra depth is required to accept explicit unknowns.

Verify 90/127 dossiers, 37 without, 22/36 complete campaign groups by presence; 429 source records / 426 paths; previous 417 records / 414 raw paths, all 87 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Streight's Raid in Alabama and Georgia [April 1863], AL001.
Check packet JSON blocks and receipt hashes mechanically. Run `make check` offline.
Do not run build/packet commands, and do not import or call `generalship.cli` functions such as `research_packet` or `build`, which write files; compare packets by reading them. Do not modify primary artifacts. Other campaign reviews may be pending; they are out of scope.

Write only `artifacts/review-results/chancellorsville-c3a4911-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-to-three-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
