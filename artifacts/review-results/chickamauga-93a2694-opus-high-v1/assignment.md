# Chickamauga Campaign: bounded separate source review

Review prepared commit `93a269449577504ad3818278d7a08883024ab127` against `5b83af9d3d8f715697f8656a11b5f9224ce0f311`. Sibling inputs.json binds
42 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Scope: all three frozen records, TN018 (Chattanooga, August 21), GA003 (Davis' Cross Roads) and GA004 (Chickamauga), in **Chickamauga Campaign [August-September 1863]**. Inspect all **27 claims / 135 citation occurrences**, including **3 null unknowns** and seven dimensions per record, source metadata, memo and report. Read the three retained live NPS summaries; the new Cist selection reusing the pinned `cist-cumberland-ocr-v1` (which must be unchanged); and the new Hill, Hindman and Bragg selections from the newly pinned Official Records Volume XXX Part 2 OCR and metadata. Check cited frozen cells and the battle/force/commander row sets. Whole-book reading is not required. No network, new research, extra source families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence, and that OCR readings are reported rather than silently corrected. Check:
- scope (TN018's one-day frozen interval against NPS's two weeks of shelling; GA004's interval ending September 20);
- force scopes (Cist's 55,000, 67,548 and 70,000; Bragg's 70,000, 35,000, 5,000 and the September 27 field return; Hindman's and Mackall's estimates and Cist's 30,000), none adopted;
- the casualty comparisons (GA004 frozen and live 34,624 against Cist's 16,336 and 20,950 and Bragg's 18,000, two-fifths and prisoner counts);
- the McLemore's Cove responsibility dispute (Bragg's suspension order as quoted by Hindman, Hindman's account, NPS and Cist) and the Chickamauga command judgments (Bragg on Polk, Cist on Wood and Rosecrans);
- the frozen Breckinridge commander entry for GA003 and the live heading ranks (Hill "Colonel", Hindman Brigadier General, Bragg Major General), none adopted;
- attributed judgments and interested-source labels, including Hindman's post-suspension purpose.
No automatic attribution to every listed commander and no additive credit. Attributed judgments are not causal effects. No Union reports, maps, returns, Hindman's exhibits or print were inspected by the author.

Replay all text derivatives: the three NPS summaries and the four new sectioned selections against their parents. Check the explicit page-marker maps (Cist pp.178–229 with p.206 printed "20'j"; Hill pp.136–137 with p.137 printed "87"; Hindman pp.292–298; Bragg pp.23–37 with p.37 printed "87"), including whether any locator relies on a missed or misread header. No extra depth is required to accept explicit unknowns.

At the prepared commit, verify 108/127 dossiers, 19 without, 27/36 complete campaign groups by presence; 504 source records / 488 paths; previous 492 records / 476 raw paths, all 105 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: East Tennessee Campaign [September-October 1863], TN019 and TN020.
Check packet JSON blocks and receipt hashes at the prepared commit mechanically. Run `make check` offline.
Do not run build/packet commands, and do not import or call `generalship.cli` functions such as `research_packet` or `build`, which write files; compare packets by reading them. Do not modify primary artifacts. Other campaign reviews may be pending; they are out of scope.

Write only `artifacts/review-results/chickamauga-93a2694-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
