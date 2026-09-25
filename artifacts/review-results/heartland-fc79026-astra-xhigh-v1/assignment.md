# Confederate Heartland Offensive: bounded separate source review

Review prepared commit `fc79026845cde8b8e3544ab460e2b4e3d6d595d1` against `686b787c7bbd797e3bece51681f387b54bf49f17` in
`/Users/masonpetrosky/Projects/generalship`. Sibling inputs.json binds 48 paths.
You are the separate GPT-6 Astra xhigh reviewer with fresh context. Read AGENTS.md,
README, methodology, roadmap, evidence contract and source guidance. The primary's
conversation is not an input.

Scope: all five frozen records in **Confederate Heartland Offensive [June-October
1862]**: TN005, TN006, KY007, KY008 and KY009. Inspect all **54 claims / 155 citation
occurrences**, including **6 null unknowns** and seven dimensions per dossier, source
metadata, memo and report. Read five retained live NPS summaries, the Cist catalog
metadata, title/preface and all five selected battle passages. Check cited frozen
cells, including the four commander-rank cells, and all five battle/force/commander
row sets. Parent HTML/OCR provide boundaries and relevant context; whole-book reading
is not required. No network, new research, extra source families or agents. Keep
review proportional to bounded draft extraction.

Verify entailment and attribution, not just quote presence. Check Murfreesboro's
live NPS result field ("Union Victory") against the frozen Confederate victory and
its own surrender narrative; the frozen value must be retained, not corrected.
Check force scopes: Murfreesboro frozen approx. 1,400 CS / 900 US versus Cist's
about 2,000 and 1,700 surrendered; Richmond's whole-command 7,000 / 12,000;
Perryville's live 55,000, narrative nearly 55,000, Cist's 58,000 effective, less
than half engaged and Hardee's 16,000. Live zeros are not measured absence.
Surrendered or captured populations must not become opening counts or extra
aggregate losses. Preserve casualty differences (frozen/live): Chattanooga 88 / 3,
Murfreesboro 1,040 / 1,350, Richmond 5,650 / 6,223 (NPS ~4,000 captured versus
Cist over 2,000), Munfordville 4,862 / 4,433, Perryville 7,407 / 7,607. Check
the draft's statement that Cist's OCR prints 4,348 with components 916 / 2,943 /
189 summing to 4,048.

Check command roles and clocks: Kirby Smith's June 8 arrival and Leadbetter at
Chattanooga; Crittenden July 11 (Cist) versus July 12 (NPS) and "no one in command";
Manson/Cleburne before Nelson/Smith at Richmond; Wilder → Dunham → Wilder at
Munfordville; Polk's immediate command and Bragg's two reports as quoted by Cist.
Check the Munfordville September 13/14 demand chronology, the Murfreesboro 4:15–4:30
versus about 5:00 clocks, and live heading rank conflicts (Negley, Forrest,
Kirby Smith, Bragg). No automatic attribution to every listed commander. Check
the one `commander_created` tag (Forrest's continued attack) and two `inherited`
tags for fit. Attributed counterfactuals (Duke on the river; NPS on Buell's reserves),
Cist's Louisville-intent inference and Wilder's reported 25,000 are not verified
message chains, true strengths or causal effects. Excluded neighbors: Jasper,
Perryville's October 7 fighting and later pursuit. No original orders, returns,
maps or print were inspected by the author.

Replay all six text derivatives: five NPS summaries and the sectioned Cist
selection's six half-open Unicode ranges. Cist is an interested 1882 retrospective
Union history (staff of Rosecrans and Thomas); quoted Duke/Bragg/Buell passages are
not separately inspected originals. Check that `source_kind` is `retrospective_history`,
not a participant witness, for these 1862 actions. The preface is undated. Each
battle uses two families. Check that Cist page locators match OCR page markers.
No extra depth is required to accept explicit unknowns.

Verify 45/127 dossiers, 82 without, 9/36 complete campaign groups by presence;
286 source records / 283 paths; previous 273 records / 270 raw paths and 52
protected files byte-identical (40 older dossiers, six historical revisions,
cohort, both admission proposals, admission-check, baseline and battles artifacts).
Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier
0.2768816348133779 versus 0.25). Independently confirm the next complete group:
Northern Virginia Campaign [August 1862], VA022–VA027. Check packet JSON blocks and
receipt hashes mechanically without printing five registries. Run `make check`
offline. Do not run build/packet commands or modify primary artifacts.

Write only `artifacts/review-results/heartland-fc79026-astra-xhigh-v1/review.md`.
Do not edit other files, commit or push. State actual inspected scope and required
corrections with exact evidence-backed replacements, or say no required corrections.
A concise two-to-three-page review is sufficient. Return the path and outcome.
AI review is not historical adjudication, independent corroboration or feature admission.
