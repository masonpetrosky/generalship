# East Tennessee Campaign: bounded separate source review

Review prepared commit `49312d9441d898e75b516d4efdcff50d5cab5b58` against `5948133d5ea4010e0f644b5aa32749241c14f075`. Sibling inputs.json binds
36 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Scope: both frozen records, TN019 (Blountsville, September 22) and TN020 (Blue Springs, October 10), in **East Tennessee Campaign [September-October 1863]**. Inspect all **19 claims / 80 citation occurrences**, including **2 null unknowns** and seven dimensions per record, source metadata, memo and report. Read the two retained live NPS pages (whose descriptions are empty, so the frozen CWSAC description column is cited) and the four new Foster, Samuel Jones, Burnside and Williams selections reusing the pinned `or30-2-illinois-ocr-v1` (which must be unchanged). Check cited frozen cells, including the description column, and the battle/force/commander row sets. No network, new research, extra source families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence, and that OCR readings are reported rather than silently corrected. Check:
- scope (the Bristol raid, the September 20 Zollicoffer skirmish, the October 3/5 skirmishes, and the October 11 Henderson's/Rheatown fighting are outside the frozen dates);
- force scopes (Foster's 6,000 at Zollicoffer, Jones's 2,000 mounted on September 20, Williams's 5,000 and 15,000 and his 75–100-man center, Burnside's 6,000 Ninth Corps), none adopted;
- the disputes (who burned Blountsville; the frozen description's noon attack against Foster's clocks; the Blue Springs evening assault; Williams's purpose);
- casualty comparisons (Foster's 6 killed and 14 wounded against the frozen US 27; Burnside's 100 including the pursuit);
- the live heading rank "Colonel John Williams", not adopted;
- the use of Jones's February 1864 report and Williams's supplement, and the interested-source labels.
No automatic attribution to every listed commander and no additive credit. Attributed judgments are not causal effects. No maps, returns or print were inspected by the author.

Replay all text derivatives: the two NPS pages and the four new sectioned selections against their parent. Check the explicit page-marker maps (Foster pp.590–593; Jones pp.601–605 with p.603 printed "003"; Burnside pp.547–552 with p.552 printed "553"; Williams pp.639–643 with the p.639 head printed "G89"), including whether any locator relies on a missed or misread header. No extra depth is required to accept explicit unknowns.

At the prepared commit, verify 110/127 dossiers, 17 without, 28/36 complete campaign groups by presence; 512 source records / 496 paths; previous 504 records / 488 raw paths, all 108 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Bristoe Campaign [October-November 1863], VA039–VA043.
Check packet JSON blocks and receipt hashes at the prepared commit mechanically. Run `make check` offline.
Do not run build/packet commands, and do not import or call `generalship.cli` functions such as `research_packet` or `build`, which write files; compare packets by reading them. Do not modify primary artifacts. Other campaign reviews may be pending; they are out of scope.

Write only `artifacts/review-results/east-tennessee-49312d9-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
