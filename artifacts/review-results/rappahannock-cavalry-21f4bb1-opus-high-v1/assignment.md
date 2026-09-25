# Cavalry Operations along the Rappahannock: bounded separate source review

Review prepared commit `21f4bb1cbca40f987b5b1ad0deb30fad764c4070` against `b884e79bd4c9628ad27b766859f12c32ed78ce87`. Sibling inputs.json binds
32 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Scope: the sole frozen record, VA029 (Kelly's Ford), in **Cavalry Operations along the Rappahannock [March 1863]**. Inspect all **9 claims / 60 citation occurrences**, including **1 null unknown** and seven dimensions, source metadata, memo and report. Read the retained live NPS summary and the two new Official Records Volume XXV Part 1 selections (Averell's March 20 report; Fitz Lee's March 23 report, March 26 letter and General Orders No. 10), and for boundaries the newly pinned `or25-1-illinois-ocr-v1` OCR and its catalog metadata. Check cited frozen cells and the battle/force/commander row sets. Parent HTML/OCR provide boundaries and context; whole-volume reading is not required. No network, new research, extra source families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence; check that each value clause is supported by the cited words and that OCR readings are reported rather than silently corrected. Check force scopes: frozen "Divisions (3,000 total)" and strength 3000 with blank side-specific bounds; NPS 2,100 and about 800; Averell's ordered 3,000, detached 900 and marching 2,100; Fitz Lee's "not less than 3,000". Check the disputed withdrawal (NPS mid-afternoon; Averell 5.30 p.m.; Fitz Lee 7.30 p.m. with close pursuit) and the casualty records (frozen 200; live 179 with US 99 / CS 80; Averell 80 with the revised-statement footnote; Fitz Lee 133 including 99 killed and wounded), including the primary's computed observation that the live split matches the reports with sides reversed. Check command attributions (wavering regiments, Duffié's early charge, Averell's withdrawal decision, Stuart's presence as a non-frozen commander, Munford's absence) and the Fitz Lee live heading rank. Check the `unresolved` phase tags and the explicit two-page locator for quotes between the p.50 and p.52 markers, where the OCR prints the p.51 header after that page's text. No automatic attribution to every listed commander and no additive credit. Attributed judgments and counterfactuals are not causal effects. No original manuscripts, returns, maps or print were inspected by the author.

Replay all three text derivatives: the NPS summary and the two new sectioned selections against the new parent. Check the parent and metadata hashes and the registry records' edition and imprint claims against the OCR title and catalog metadata. Check that page locators follow the explicit OCR page-marker maps. No extra depth is required to accept explicit unknowns.

Verify 77/127 dossiers, 50 without, 20/36 complete campaign groups by presence; 379 source records / 376 paths; previous 373 records / 370 raw paths, all 76 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Grant's Operations Against Vicksburg [March-July 1863], ten records without dossiers plus the existing MS009.
Check packet JSON blocks and receipt hashes mechanically. Run `make check` offline.
Do not run build/packet commands, and do not import or call `generalship.cli` functions such as `research_packet` or `build`, which write files; compare packets by reading them. Do not modify primary artifacts. Other campaign reviews may be pending; they are out of scope.

Write only `artifacts/review-results/rappahannock-cavalry-21f4bb1-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
