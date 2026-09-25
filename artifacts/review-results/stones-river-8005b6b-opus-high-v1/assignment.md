# Stones River Campaign: bounded separate source review

Review prepared commit `8005b6b484045b01f3e4674b593c8f8d7180e36e` against `e79f33d823a7df7d1428481e53f48fdf65c2a1c5`. Sibling inputs.json binds
33 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Scope: both frozen records, TN008 and TN010, in **Stones River Campaign [December 1862-January 1863]**. Inspect all **20 claims / 58 citation occurrences**, including **2 null unknowns** and seven dimensions
per dossier, source metadata, memo and report. Read two retained live NPS summaries, the new Cist selection (title/preface and five passages) and, for boundaries, the existing pinned Cist OCR and metadata, which must be unchanged. Check cited frozen cells and
the battle/force/commander row sets. Parent HTML/OCR provide boundaries and context;
whole-book reading is not required. No network, new research, extra source families
or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence. Check force scopes: Hartsville's about two thousand effectives (Cist) with no Confederate count; Stones River NPS 44,000 versus more than 37,000, live 45,000 Union, and Cist's 43,400 versus a computed 46,604 with 'slightly inferior' (disputed which army was larger). Preserve casualty differences (frozen/live): Hartsville 2,004 / 2,235 (Cist Moore 150 plus captured, Morgan 125), Stones River 23,515 / 23,000 (Cist Bragg 10,125; Rosecrans 1,553 killed, 7,245 wounded, about 2,800 captured). Captured troops are not opening strengths. Check the disputed picket-warning claim (NPS alarm versus Cist no warning; Moore's report summarized by NPS), the disputed Morgan rank-timing claim (Cist's commission after Hartsville), the `inherited` guard-mission tag, the `commander_created` Rosecrans decisions (Cist is Rosecrans's staff historian), Bragg's quoted report and the subordinate retreat notes, the mirror-plans claim, and retreat timing (Cist January 3; NPS January 4–5). Check the explicit map-plate locators (pp.102–103 and p.104). No automatic
attribution to every listed commander and no additive credit across overlapping
intervals. Attributed judgments and counterfactuals are not causal effects. No
original orders, returns, maps or print were inspected by the author.

Replay all three text derivatives: two NPS summaries and the new sectioned Cist selection's six half-open Unicode ranges against the existing `cist-cumberland-ocr-v1` parent. Check that the new selection record reuses the parent's metadata fields and that `source_kind` is `retrospective_history`. Check that book page locators follow OCR page markers. No extra depth is
required to accept explicit unknowns.

Verify 59/127 dossiers, 68 without, 13/36 complete campaign groups by presence; 324 source records / 321 paths; previous 319 records / 316 raw paths, all 57 older dossiers and twelve historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups;
Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Fredericksburg Campaign [November-December 1862], VA028.
Check packet JSON blocks and receipt hashes mechanically. Run `make check` offline.
Do not run build/packet commands or modify primary artifacts. Other campaign reviews
may be pending; they are out of scope.

Write only `artifacts/review-results/stones-river-8005b6b-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-to-three-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
