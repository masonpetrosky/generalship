# Northern Virginia Campaign: bounded separate source review

Review prepared commit `280d5d7dade3c49a82c45abc14f53f214b984ad3` against `c0013520981791b4b5d049bd15722a11a17fa58f`. Sibling inputs.json binds
51 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Scope: all six frozen records in **Northern Virginia Campaign [August 1862]**:
VA022, VA023, VA024, VA025, VA026 and VA027. Inspect all **56 claims / 142 citation
occurrences**, including **7 null unknowns** and seven dimensions per dossier,
source metadata, memo and report. Read six retained live NPS summaries, the Ropes
catalog metadata, title/preface and all ten selected passages plus Appendix D.
Check cited frozen cells, including commander-rank cells, and all six battle/force/
commander row sets. Parent HTML/OCR provide boundaries and relevant context;
whole-book reading is not required. No network, new research, extra source
families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence. Check force scopes:
Cedar Mountain's frozen 24,898 (US 8,030; CS 16,868) against Ropes's under-8,000
Union corps and 20,000–25,000 Confederates and NPS's 14,000 at Gordonsville; live
zeros elsewhere are not measured absence. Preserve casualty differences
(frozen/live): Cedar Mountain 2,707 / 3,900 (and Ropes's 2,393 total whose
components sum to 2,384), Rappahannock Station 225 / 0, Manassas Station 1,100 / 0,
Thoroughfare Gap 100 / 0, Second Manassas 22,180 / 22,179, Chantilly 2,100 agree.
Check Ropes's Appendix D Confederate figures are not treated as this interval's
losses. Check result labels: Inconclusive/Indecisive for VA023 and VA027 (with its
strategic qualifier); Second Manassas's "precipitous" (NPS) versus "not a rout"
(Ropes) retreat; the August 28 drawn fight kept inside VA026 and not added.
Check the disputed claim about what Pope knew of Longstreet on August 30.

Check command roles: the disputed order Banks received; Banks's attack decision and
McDowell's unordered Ricketts detachment, both tagged `commander_created`; Winder →
Taliaferro; Stuart's command of the Manassas Junction capture; Kearny's and
Stevens's deaths; Lee and Longstreet live heading ranks against frozen ranks. No
automatic attribution to every listed commander. VA024 is a frozen aggregate
operation; component casualties must not be added. Adjoining intervals (August
22–25, 25–27, 28, 28–30) share troops; no additive credit. Attributed judgments
(Ropes on Cedar Mountain's cause; NPS on Thoroughfare Gap ensuring defeat; Jackson's
quoted captures) are not causal effects or verified inventories. No original
orders, returns, maps or print were inspected by the author.

Replay all seven text derivatives: six NPS summaries and the sectioned Ropes
selection's eleven half-open Unicode ranges. Ropes is an interested 1881
retrospective history by a civilian writing from the Federal standpoint; check that
`source_kind` is `retrospective_history`. Check that Ropes page locators match OCR
body page markers (the OCR contents page numbers differ; one header misreads 134
as 131 and chapter-opening pages lack headers). Each battle uses two families.
No extra depth is required to accept explicit unknowns.

Verify 51/127 dossiers, 76 without, 10/36 complete campaign groups by presence;
301 source records / 298 paths; previous 286 records / 283 raw paths, all 45 older
dossiers and seven historical revisions byte-identical, plus cohort, both admission
proposals, admission-check, baseline and battles artifacts. Check zero promoted rows
and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus
0.25). Independently confirm the next group: Maryland Campaign [September 1862],
WV010, MD002, MD003 (already drafted) and WV016. Check packet JSON blocks and receipt
hashes mechanically without printing six registries. Run `make check` offline.
Do not run build/packet commands or modify primary artifacts.

Write only `artifacts/review-results/northern-virginia-280d5d7-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-to-three-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
