# Fredericksburg Campaign: bounded separate source review

Review prepared commit `dbcd3da1efa834a36528e5cdfe74ad780349712e` against `7c852429dd28e8e08363e814e4aa264ecbc0263a`. Sibling inputs.json binds
29 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Scope: the sole frozen record, VA028, in **Fredericksburg Campaign [November-December 1862]**. Inspect all **10 claims / 31 citation occurrences**, including **1 null unknown** and seven dimensions
per dossier, source metadata, memo and report. Read the retained live NPS summary, the new Palfrey selection (title/preface and seven Chapter IV passages) and, for boundaries, the existing pinned Palfrey OCR and metadata, which must be unchanged. Check cited frozen cells and
the battle/force/commander row sets. Parent HTML/OCR provide boundaries and context;
whole-book reading is not required. No network, new research, extra source families
or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence. Check force scopes: frozen 172,504 (US 100,007; CS 72,497); the live field's '100007 total (US 0; CS 100007;)' side misassignment, not adopted; Palfrey's 113,000 (December 13), 78,000 (December 10) and 127,574 (November 10) present for duty. Preserve casualty differences (frozen/live): 17,929 (US 13,353; CS 4,576) / 17,900 (US 12,600; CS 5,300); Palfrey's grand-division columns summing to 12,353 (computed, not printed), Longstreet's 1,894 over five days and Jackson's 3,415. Check the `inherited` pontoon/crossing tag, the stone-wall terrain claim, Palfrey's inference about Burnside's expectation for Franklin's attack, the obscurity-of-orders responsibility claim, the post-outcome renewed-assault claim attributed through Swinton, and the new selection record's corrected dependency note (Palfrey's campaign service is not shown in the inspected text). No automatic
attribution to every listed commander and no additive credit across overlapping
intervals. Attributed judgments and counterfactuals are not causal effects. No
original orders, returns, maps or print were inspected by the author.

Replay both text derivatives: the NPS summary and the new sectioned Palfrey selection's eight half-open Unicode ranges against the existing `palfrey-antietam-ocr-v1` parent. Check that book page locators follow OCR page markers. No extra depth is
required to accept explicit unknowns.

Verify 60/127 dossiers, 67 without, 14/36 complete campaign groups by presence; 327 source records / 324 paths; previous 324 records / 321 raw paths, all 59 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups;
Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Goldsboro Expedition [December 1862], NC007, NC008 and NC009.
Check packet JSON blocks and receipt hashes mechanically. Run `make check` offline.
Do not run build/packet commands or modify primary artifacts. Other campaign reviews
may be pending; they are out of scope.

Write only `artifacts/review-results/fredericksburg-dbcd3da-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-to-three-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
