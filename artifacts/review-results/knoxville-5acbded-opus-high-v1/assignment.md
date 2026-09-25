# Longstreet's Knoxville Campaign: bounded separate source review

Review prepared commit `5acbdedb03e590741cb037238edaa400ad2c83cd` against `dd16b5ed50cc6abff8a3998c51864d8ae973190c`. Sibling inputs.json binds
39 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Intervening commits between the prepared commit and the bundle may include other campaigns' review corrections; they are out of scope. Verify input hashes against `git show 5acbdedb03e590741cb037238edaa400ad2c83cd:<path>`, and read any bound path that differs in the worktree from the prepared commit.

Scope: all three frozen records, TN023 (Campbell's Station), TN025 (Fort Sanders) and TN026 (Bean's Station), in **Longstreet's Knoxville Campaign [November-December 1863]**. Inspect all **27 claims / 123 citation occurrences**, including **3 null unknowns** and seven dimensions per record, source metadata, memo and report. Read the three retained live NPS pages (TN026's has no description, so its frozen description column is cited) and the new Burnside, Longstreet and Parke selections reusing the pinned `or31-1-illinois-ocr-v1` (which must be unchanged). Check cited frozen cells and the battle/force/commander row sets. No network, new research, extra source families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence, and that OCR readings are reported rather than silently corrected. Check: scope (the siege, the November 23–25 actions, the December 15 fighting and the pursuit outside the records); the opposing strength figures (Burnside's 5,000/double, 12,000 and 20,000–23,000, 15,000; Longstreet's 20,000 and Stevenson's 23,000), none adopted; the Fort Sanders `inherited` tag; Burnside's two sets of Fort Sanders losses; the Bean's Station 2 a.m./2 p.m. and 1,600/337 disputes; Longstreet's judgments of Jenkins, Law, McLaws and his cavalry, including the pursuit after the frozen date; the live 'Major General' rank for Longstreet, not adopted; interested-source labels and the use of Parke because Shackelford's dispatches stop before the fight. No automatic attribution to every listed commander and no additive credit. Attributed judgments are not causal effects. No maps, subordinate reports, returns or print were inspected by the author.

Replay all text derivatives: the three NPS pages and the three new sectioned selections against their parent. Check the explicit page-marker maps (Burnside pp.268–278; Longstreet pp.455–465 with p.456's head read '45f)'; Parke pp.325–327 with heads read '320' and '827' and inferred as 326 and 327), including whether any locator relies on a missed or misread header. No extra depth is required to accept explicit unknowns.

At the prepared commit, verify 121/127 dossiers, 6 without, 33/36 complete campaign groups by presence; 555 source records / 535 paths; previous 546 records / 526 raw paths, all 118 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Chattanooga-Ringgold Campaign [November 1863], TN024 and GA005.
Check packet JSON blocks and receipt hashes at the prepared commit mechanically. Run `make check` offline.
Do not run build/packet commands, and do not import or call `generalship.cli` functions such as `research_packet` or `build`, which write files; compare packets by reading them. Do not modify primary artifacts. Other campaign reviews may be pending; they are out of scope.

Write only `artifacts/review-results/knoxville-5acbded-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
