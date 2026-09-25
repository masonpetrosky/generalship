# Bristoe Campaign: bounded separate source review

Review prepared commit `dc77737bbeb20024b5817e9292d6ace5a6a7ddfc` against `2203b712059f37ada174fc171b56f46cca331a2e`. Sibling inputs.json binds
50 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Intervening commits between the prepared commit's parent and the bundle may include other campaigns' review corrections; they are out of scope. Verify input hashes against `git show dc77737bbeb20024b5817e9292d6ace5a6a7ddfc:<path>`, and read any bound path that differs in the worktree from the prepared commit.

Scope: all five frozen records, VA039 (Auburn, October 13), VA040 (Bristoe Station), VA041 (Auburn/Coffee Hill, October 14), VA042 (Buckland Mills) and VA043 (Rappahannock Station), in **Bristoe Campaign [October-November 1863]**. Inspect all **45 claims / 190 citation occurrences**, including **5 null unknowns** and seven dimensions per record, source metadata, memo and report. Read the five retained live NPS summaries; the new Humphreys selection reusing the pinned `humphreys-ocr-v2` (which must be unchanged); and the new Stuart, A. P. Hill and Lee selections from the newly pinned Official Records Volume XXIX Part 1 OCR and metadata. Check cited frozen cells (including VA043's `result` column) and the battle/force/commander row sets. No network, new research, extra source families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence, and that OCR readings are reported rather than silently corrected. Check:
- overlap handling (two Auburn records and Bristoe Station; Humphreys' combined Auburn-and-Bristoe losses not assigned; Kelly's Ford losses not added to VA043);
- the Buckland date conflict (frozen October 19 and Stuart's "yesterday" against Humphreys' 20th);
- force scopes (Humphreys' 8,243/3,000/17,223/15,000, 6,867/3,500, 2,117/1,950; Stuart's ten regiments; Lee's "three army corps"), none adopted;
- the disputes (brigade composition at Auburn and NPS's "Harry Hays's division"; Third versus Fifth Corps at Bristoe; Kilpatrick's rank; the adequacy of the Rappahannock works; the frozen VA043 result fields);
- `inherited` tags on the Bristoe embankment and summer works and the Rappahannock earthworks;
- attributed judgments (Hill and the Lee/Seddon/Davis indorsements, NPS's rebuke remark, Stuart's credit to Fitzhugh Lee and his counterfactual, Lee's explanation) and interested-source labels.
No automatic attribution to every listed commander and no additive credit. Attributed judgments are not causal effects. No Union reports, maps, returns or print were inspected by the author.

Replay all text derivatives: the five NPS summaries and the four new sectioned selections against their parents. Check the explicit page-marker maps (Humphreys pp.20–48 with p.30 printed "3<3"; Stuart pp.438–452; Hill pp.426–428; Lee pp.609–616 with pp.614–615 as bare running heads), including whether any locator relies on a missed or misread header. No extra depth is required to accept explicit unknowns.

At the prepared commit, verify 115/127 dossiers, 12 without, 29/36 complete campaign groups by presence; 531 source records / 512 paths; previous 515 records / 496 raw paths, all 110 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Reopening the Tennessee River [October 1863], TN021.
Check packet JSON blocks and receipt hashes at the prepared commit mechanically. Run `make check` offline.
Do not run build/packet commands, and do not import or call `generalship.cli` functions such as `research_packet` or `build`, which write files; compare packets by reading them. Do not modify primary artifacts. Other campaign reviews may be pending; they are out of scope.

Write only `artifacts/review-results/bristoe-dc77737-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
