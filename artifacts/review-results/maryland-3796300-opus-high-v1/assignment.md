# Maryland Campaign: bounded separate source review

Review prepared commit `3796300981ae53e5d94d8b2411af3eef3b53d7fd` against `7c4902bd8cb01fe0d026c11207daab07e9a3d80f`. Sibling inputs.json binds
39 paths at the prepared commit. You are the separate Claude Opus 5.5 `high`
reviewer with fresh context. Read AGENTS.md, README, methodology, roadmap, evidence
contract and source guidance. The primary's conversation is not an input.

Scope: the three new dossiers in **Maryland Campaign [September 1862]**: WV010,
MD002 and WV016. MD003 Antietam's existing draft must be byte-identical and is not
re-reviewed. Inspect all **29 claims / 79 citation occurrences**, including **4 null
unknowns** and seven dimensions per dossier, source metadata, memo and report. Read
three retained live NPS summaries, the Palfrey catalog metadata, title/preface and
all four selected passages. Check cited frozen cells, including the commander-rank
cell, and the three battle/force/commander row sets. Parent HTML/OCR provide
boundaries and context; whole-book reading is not required. No network, new
research, extra source families or agents. Keep review proportional.

Verify entailment and attribution, not just quote presence. Check South Mountain's
live NPS result field ("Indecisive") against the frozen Union victory, with
Palfrey's "tactical defeats … strategical victories"; the frozen value must be
retained. Check Harpers Ferry force scopes (Palfrey 9,000 + 2,500 arriving, 11,000
surrendered; NPS more than 12,000) and the disputed surrendering officer (Miles in
NPS, White in Palfrey). Surrender counts are not opening strengths. Check South
Mountain's McClellan 30,000 each, Palfrey's 35,155 cap and brigade counts, kept
separate. Preserve casualty differences (frozen/live): Harpers Ferry 12,922 /
13,005, South Mountain 4,500 / 4,625 (Palfrey's per-gap figures not summed),
Shepherdstown 625 / 654; 118th Pennsylvania 269 (NPS) versus 282 of 800 (Palfrey);
A. P. Hill's quoted 3,000 is an attributed claim; four versus five guns.

Check phase tags: Halleck's hold order tagged `inherited`; McClellan's no-night-march
decision tagged `commander_created`; Palfrey's counterfactual stays attributed.
Check command roles (Cox then Reno; Franklin at Crampton's; Pendleton on the 19th,
A. P. Hill on the 20th; Lee's live heading rank). No automatic attribution to every
listed commander, and no additive credit across overlapping Maryland intervals.
The lost order's receipt hour is explicitly unknown. No original orders, returns,
maps or print were inspected by the author.

Replay all four text derivatives: three NPS summaries and the sectioned Palfrey
selection's five half-open Unicode ranges. Palfrey is an 1882 retrospective history
by a Union participant who used advance sheets of the Official Records; check that
`source_kind` is `retrospective_history` and the dependence note says so. Check that
Palfrey page locators follow OCR markers, including the misread p.24 ("21") and p.34
("31") headers. Each new battle uses two families. No extra depth is required to
accept explicit unknowns.

Verify 54/127 dossiers, 73 without, 11/36 complete campaign groups by presence; 310
source records / 307 paths; previous 301 records / 298 raw paths, all 51 older
dossiers (including MD003) and seven historical revisions byte-identical, plus
cohort, both admission proposals, admission-check, baseline and battles artifacts.
Check zero promoted rows and unchanged baseline (23 eligible / 13 groups; Brier
0.2768816348133779 versus 0.25). Independently confirm the next group: Iuka and
Corinth Operations [September-October 1862], MS001, MS002, TN007. Check packet JSON
blocks and receipt hashes mechanically. Run `make check` offline. Do not run
build/packet commands or modify primary artifacts. A separate Northern Virginia
review may be pending; it is out of scope.

Write only `artifacts/review-results/maryland-3796300-opus-high-v1/review.md`. Do not edit other files, commit or push. State actual
inspected scope and required corrections with exact evidence-backed replacements,
or say no required corrections. A concise two-to-three-page review is sufficient.
Return the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
