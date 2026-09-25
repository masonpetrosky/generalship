# Operations Against Vicksburg 1862–63: bounded separate source review

Review prepared commit `7cbb97100ca5db247610b8e198b58f44fd5f5be4` against `e865cffa9390b65fd2015ff19c2f8ce15e950ba2`. Sibling inputs.json binds
33 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Scope: both frozen records, MS003 and AR006, in **Operations Against Vicksburg [December 1862-January 1863]**. Inspect all **19 claims / 62 citation occurrences**, including **2 null unknowns** and seven dimensions
per dossier, source metadata, memo and report. Read both retained live NPS summaries, the new Greene selection (title/preface and two Chapter III passages) and, for boundaries, the existing pinned Greene OCR and metadata, which must be unchanged. Check cited frozen cells and
the battle/force/commander row sets. Parent HTML/OCR provide boundaries and context;
whole-book reading is not required. No network, new research, extra source families
or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence. Check force scopes: Greene's 32,000 expedition, at least 12,000 defenders versus the 6,000 garrison, and not more than 6,000 assaulting; Arkansas Post garrison about 5,000 versus the quoted Sherman letter's seven thousand. Preserve casualty differences (frozen/live): Chickasaw Bayou 1,983 (US 1,776; CS 207) / 1,963 (US 1,776; CS 187), Greene 1,929 and 187; Arkansas Post 6,547 / 6,096, Greene 977 plus 31 on gunboats, about 200 and 4,791 prisoners. Check the disputed white-flag claim (origin untraced; Churchill denied authority), the information claims (spies' reports; Sherman unaware of reinforcements; McClernand's news), the two `inherited` terrain tags, subordinate-execution and joint-command claims, and the Sherman ('General') and Porter ('Rear Admiral') live heading rank conflicts. No automatic
attribution to every listed commander and no additive credit across overlapping
intervals. Attributed judgments and counterfactuals are not causal effects. No
original orders, returns, maps or print were inspected by the author.

Replay all three text derivatives: two NPS summaries and the new sectioned Greene selection's three half-open Unicode ranges against the existing `greene-mississippi-ocr-v1` parent. Check that book page locators follow OCR page markers. No extra depth is
required to accept explicit unknowns.

Verify 67/127 dossiers, 60 without, 17/36 complete campaign groups by presence; 349 source records / 346 paths; previous 344 records / 341 raw paths, all 65 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups;
Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Middle Tennessee Operations [February-April 1863], TN012–TN016.
Check packet JSON blocks and receipt hashes mechanically. Run `make check` offline.
Do not run build/packet commands or modify primary artifacts. Other campaign reviews
may be pending; they are out of scope.

Write only `artifacts/review-results/vicksburg-1862-7cbb971-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-to-three-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
