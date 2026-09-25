# Goldsboro Expedition: bounded separate source review

Review prepared commit `9de5b1dd90633345ebc7b2d6e54a520c54718ee1` against `9d5b254beaf2767b6ba16340983c118fee8e91d0`. Sibling inputs.json binds
40 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Scope: all three frozen records, NC007, NC008 and NC009, in **Goldsboro Expedition [December 1862]**. Inspect all **28 claims / 70 citation occurrences**, including **4 null unknowns** and seven dimensions
per dossier, source metadata, memo and report. Read three retained live NPS summaries, the Official Records XVIII catalog metadata, title, and both report selections (Foster December 14, 20 and 27; G. W. Smith December 15, 16 letter and telegram, 18 and 29). The prepared state spans two commits: 4a91368 added the evidence and 9de5b1d completed the documentation after a failed test; check both. Check cited frozen cells and
the battle/force/commander row sets. Parent HTML/OCR provide boundaries and context;
whole-book reading is not required. No network, new research, extra source families
or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence. Check force scopes: Foster's about 10,000 infantry, 40 guns and 640 cavalry (expedition, at departure) and his 6,000 for Evans; Smith's 2,000 for Evans, relayed 30,000 and 'certainly over 15,000' for Foster; none adopted. Preserve casualty differences: Kinston 685 agrees; White Hall 150 / 0 and Goldsborough Bridge 220 / 0 (frozen/live) disputed; Foster's expedition-wide 90/478/9 and Smith's 71/268/about 400 recorded once in NC009 and not allocated. Check the disputed White Hall result (Foster silenced guns versus Smith 'driven back'), Goldsborough framing, Foster's rank conflict (frozen/live Brigadier General versus OR 'Maj. Gen.'), the `inherited` approach-delay tag, and that report dates are section-specific and not event times. Verify the explicit page-marker map (OR running headers misprint p.57 as '61', p.55 as 'S5', p.107 as 'm'). Report families: NPS, Foster and Smith are three; the OR volume is a shared container. No automatic
attribution to every listed commander and no additive credit across overlapping
intervals. Attributed judgments and counterfactuals are not causal effects. No
original orders, returns, maps or print were inspected by the author.

Replay all five text derivatives: three NPS summaries and the two sectioned OR selections (Foster four ranges, Smith six ranges) against `or18-illinois-ocr-v1`. Check section document dates and source_kind values. Check that book page locators follow OCR page markers. No extra depth is
required to accept explicit unknowns.

Verify 63/127 dossiers, 64 without, 15/36 complete campaign groups by presence; 337 source records / 334 paths; previous 327 records / 324 raw paths, all 60 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups;
Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Forrest's Expedition into West Tennessee [December 1862-January 1863], TN009 and TN011.
Check packet JSON blocks and receipt hashes mechanically. Run `make check` offline.
Do not run build/packet commands or modify primary artifacts. Other campaign reviews
may be pending; they are out of scope.

Write only `artifacts/review-results/goldsboro-9de5b1d-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-to-three-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
