# Chattanooga-Ringgold Campaign: bounded separate source review

Review prepared commit `450a5ba46975e7f117cbe542d2d87a7d51cd1dc9` against `803bfc6477ef15d668307991dfa3862c18bd2540`. Sibling inputs.json binds
37 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Intervening commits between the prepared commit and the bundle may include other campaigns' review corrections; they are out of scope. Verify input hashes against `git show 450a5ba46975e7f117cbe542d2d87a7d51cd1dc9:<path>`, and read any bound path that differs in the worktree from the prepared commit.

Scope: both frozen records, TN024 (Chattanooga, November 23–25) and GA005 (Ringgold Gap, November 27), in **Chattanooga-Ringgold Campaign [November 1863]**. Inspect all **18 claims / 82 citation occurrences**, including **2 null unknowns** and seven dimensions per record, source metadata, memo and report. Read the two retained live NPS summaries, the new Cist selection reusing the pinned `cist-cumberland-ocr-v1` (which must be unchanged), and the new Bragg and Cleburne selections from the newly pinned Official Records Volume XXXI Part 2 OCR and metadata (whose title page has no imprint line). Check cited frozen cells and the battle/force/commander row sets. No network, new research, extra source families or agents. Keep review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence, and that OCR readings are reported rather than silently corrected. Check: scope (Orchard Knob, Lookout Mountain and Missionary Ridge in TN024; the November 26 pursuit outside both); strength statements (Bragg's 'at least double', Cist's part-force 8,000 and under 10,000, Cleburne's 4,157), none adopted; the `inherited` tag on the Missionary Ridge works; the responsibility dispute (Bragg on Stevenson and his troops; Cist on the unordered charge and Grant's plan); Cist's printed 3,951 against components summing to 2,951; the Ringgold Gap outcome dispute (NPS five hours/failed against Cist over an hour/driven); Cleburne's 221 against the frozen 480; the live ranks for Grant and Bragg, not adopted; interested-source labels. No automatic attribution to every listed commander and no additive credit. Attributed judgments are not causal effects. No Union reports, maps, returns, Cist's Lookout Mountain pages or print were inspected by the author.

Replay all text derivatives: the two NPS summaries and the three new sectioned selections against their parents. Check the explicit page-marker maps (Cist pp.243–262 with p.261 printed '201'; Bragg pp.664–667; Cleburne pp.753–758 with heads '1T&7' and '15 8'), including whether any locator relies on a missed or misread header. No extra depth is required to accept explicit unknowns.

At the prepared commit, verify 123/127 dossiers, 4 without, 34/36 complete campaign groups by presence; 564 source records / 544 paths; previous 555 records / 535 raw paths, all 121 older dossiers and all historical revisions byte-identical, plus cohort, both admission proposals, admission-check, baseline and battles artifacts. Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier 0.2768816348133779 versus 0.25). Independently confirm the next group: Mine Run Campaign [November-December 1863], VA044.
Check packet JSON blocks and receipt hashes at the prepared commit mechanically. Run `make check` offline.
Do not run build/packet commands, and do not import or call `generalship.cli` functions such as `research_packet` or `build`, which write files; compare packets by reading them. Do not modify primary artifacts. Other campaign reviews may be pending; they are out of scope.

Write only `artifacts/review-results/chattanooga-ringgold-450a5ba-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
