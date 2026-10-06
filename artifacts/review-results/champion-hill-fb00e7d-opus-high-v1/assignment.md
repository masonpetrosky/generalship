# Champion Hill (MS009): bounded separate source review

Review the MS009 draft at prepared commit `fb00e7da75b1a21d10033f2dde39379c45949ce0`.
The dossier has been byte-identical since `4547657` (2026-09-20), when it was drafted
as one of the project's three example dossiers, and it has had no separate review.
Sibling inputs.json binds 21 paths at the prepared commit. You are the separate
Claude Opus 5.5 `high` reviewer with fresh context. Read AGENTS.md, README,
methodology, roadmap, evidence contract and source guidance. The primary's
conversation is not an input.

Scope: `data/evidence/MS009.json` (schema v1): all **7 claims / 4 citation
occurrences**, including **3 null unknowns**, the seven dimensions, the boundary
note and the three open questions. Every citation is a cell of the frozen
`arnold-cwsac-battles` MS009 row (`description`, `results_text`). Read that whole
row, and the MS009 rows of `arnold-cwsac-forces` and `arnold-cwsac-commanders`. All
share the `nps-cwsac` independence group. No network, new research, extra source
families or agents. The ten other Vicksburg 1863 dossiers were reviewed separately
and are out of scope. Keep the review proportional.

Verify entailment and attribution, not just quote presence. Check:

- `pemberton-order`: who gave the order (the quote's "he"), its content, and whether
  the rationale's "later repeated direction" is supported by a cited passage.
- `alternate-plan`: the attribution to "Pemberton and his generals", the `logistics`
  dimension and the `commander_created` tag as a hypothesis.
- `force-candidate`: "about 23,000" as a force under Pemberton's command before the
  engagement, not personnel engaged. Check the statement about the structured force
  table against the MS009 `arnold-cwsac-forces` rows and the `forces_text` and
  `strength` cells, and whether a citation supports it.
- `result`: the frozen result must be retained; check the `result` and
  `results_text` cells.
- Each explicit unknown (terrain, information, responsibility): whether the full
  `description` cell already inspected for this draft supplies evidence for that
  dimension. If it does, propose the exact claim with quotes and locators, or
  explain why the unknown should stand. Do not add sources.
- Phase tags as hypotheses explained by their rationales, since replacement
  boundaries are unset, and no automatic attribution to every listed commander.

Run `make check` offline and confirm the baseline is unchanged (23 eligible / 13
groups; Brier 0.2768816348133779 versus 0.25) with zero promoted rows. Do not run
build or packet commands or modify primary artifacts. A separate Antietam (MD003)
review runs in parallel; it is out of scope.

Write only `artifacts/review-results/champion-hill-fb00e7d-opus-high-v1/review.md`. Do
not edit other files, commit or push. State the actual inspected scope and give
required corrections with exact evidence-backed replacements, or say no corrections
are required; keep advisory notes separate. A concise review is sufficient. Return
the path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
