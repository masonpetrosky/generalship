# Operations about Dandridge: bounded separate source review

Review prepared commit `668c58f76fb16476172db6e6200e44209418c619` against `34dc4bea2b45ab3227a76b0f0ac437508aa76e27`. Sibling inputs.json binds
42 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Intervening commits between the prepared commit and the bundle may include other campaigns' review corrections; they are out of scope. Verify input hashes against `git show 668c58f76fb16476172db6e6200e44209418c619:<path>`, and read any bound path that differs in the worktree from the prepared commit.

Scope: all three frozen records, TN027 (Mossy Creek, December 29, 1863), TN028 (Dandridge, January 17, 1864) and TN029 (Fair Garden, January 27, 1864), in **Operations about Dandridge [December 1863-January 1864]**. Inspect all **27 claims / 141 citation occurrences**, including **3 null unknowns** and seven dimensions per record, source metadata, memo and report. Read the three retained live NPS summaries; the new Sturgis and Martin selections reusing the pinned `or31-1-illinois-ocr-v1` (which must be unchanged); and the new Sturgis and Longstreet selections from the newly pinned Official Records Volume XXXII Part 1 OCR and metadata. Check cited frozen cells and the battle/force/commander row sets. No network, new research, extra source families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence, and that OCR readings are reported rather than silently corrected. Check: scope (the December 24/27, January 14/16, January 26 and January 28 actions outside the frozen dates); the TN027 opening rationale (imported CS 2,000, blank US) and the frozen force text's attribution to Sturgis against the inspected Sturgis figures (about 6,000 cavalry; a division of infantry) and Martin's 2,000/4,000; Sturgis's two Mossy Creek totals ('LOO' read as 100 by computation, and 96) and prisoner figures; Longstreet's own-loss 150 against the frozen Union 150; Sturgis's Fair Garden prisoner and gun descriptions; the Mossy Creek withdrawal dispute; the NPS pursuit reasons against Longstreet's; the author/relay attribution of Sturgis's December 29 dispatches (a Strawberry Plains relay heading and Parke's postscript); Parke's role in the Dandridge withdrawal; the live ranks (Sturgis Major General, Martin Colonel, Longstreet Major General), not adopted; the third frozen TN029 commander (McCook); interested-source labels. No automatic attribution to every listed commander and no additive credit. Attributed judgments are not causal effects. No maps, subordinate reports, returns or print were inspected by the author.

Replay all text derivatives: the three NPS summaries and the four new sectioned selections against their parents. Check the explicit page-marker maps (Sturgis OR XXXI pp.646–650 with p.649 read '049'; Martin pp.545–549; Sturgis OR XXXII pp.79–81 and 131–138; Longstreet pp.93–94 and 149–150), including whether any locator relies on a missed or misread header. No extra depth is required to accept explicit unknowns.

At the prepared commit, verify 127/127 dossiers, 0 without, 36/36 complete campaign groups by presence; 580 source records / 560 paths; previous 568 records / 548 raw paths, all 124 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus 0.25). Independently confirm that no frozen campaign group remains without dossiers.
Check packet JSON blocks and receipt hashes at the prepared commit mechanically. Run `make check` offline.
Do not run build/packet commands, and do not import or call `generalship.cli` functions such as `research_packet` or `build`, which write files; compare packets by reading them. Do not modify primary artifacts. Other campaign reviews may be pending; they are out of scope.

Write only `artifacts/review-results/dandridge-668c58f-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
