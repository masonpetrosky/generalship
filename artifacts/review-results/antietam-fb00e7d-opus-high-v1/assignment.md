# Antietam (MD003): bounded separate source review

Review the MD003 draft at prepared commit `fb00e7da75b1a21d10033f2dde39379c45949ce0`.
The dossier has been byte-identical since `4547657` (2026-09-20), when it was drafted
as one of the project's three example dossiers, and it has had no separate review.
Sibling inputs.json binds 22 paths at the prepared commit. You are the separate
Claude Opus 5.5 `high` reviewer with fresh context. Read AGENTS.md, README,
methodology, roadmap, evidence contract and source guidance, including "Live NPS
evidence snapshots" in `docs/sources.md`. The primary's conversation is not an input.

Scope: `data/evidence/MD003.json` (schema v1): all **9 claims / 5 citation
occurrences**, including **5 null unknowns**, the seven dimensions, the boundary
note and the three open questions. Its sources are the retained NPS snapshot
`nps-md003` (`data/raw/nps-md003.txt`, normalized text; check its hash and transform
note in `data/sources.json`) and the frozen MD003 cells of `arnold-cwsac-battles`.
Also read the MD003 rows of `arnold-cwsac-forces` and `arnold-cwsac-commanders` for
context. All of these share the `nps-cwsac` independence group. No network, new
research, extra source families or agents. Palfrey and the other Maryland sources
belong to other records' reviews and are out of scope. Keep the review proportional.

Verify entailment and attribution, not just quote presence. Check:

- `zero-sentinel`: the displayed zeros, the `disputed` status, and that zeros are
  not treated as measured counts; compare the blank CWSAC force cells.
- `force-narrative`: whether "outnumbered two-to-one" and "less than three-quarters"
  remain attributed narrative statements about available and committed forces, not
  counts.
- `recorded-result`: the frozen CWSAC `result` value must be retained. Check the
  `result` and `results_text` cells and the live NPS result against the value and
  rationale.
- `withdrawal`: the timing and attribution of the withdrawal statement.
- Phase tags (`unresolved`, `post_outcome`) as hypotheses explained by their
  rationales, since replacement boundaries are unset.
- Each explicit unknown: whether the passages already inspected for this draft (the
  snapshot and the cited row) supply evidence for that dimension. If they do,
  propose the exact claim with quotes and locators, or explain why the unknown
  should stand. Do not add sources.
- That agreement between the NPS page and the CWSAC cells is not presented as
  independent corroboration, and that the open questions remain accurate.

Run `make check` offline and confirm the baseline is unchanged (23 eligible / 13
groups; Brier 0.2768816348133779 versus 0.25) with zero promoted rows. Do not run
build or packet commands or modify primary artifacts. A separate Champion Hill
(MS009) review runs in parallel; it is out of scope.

Write only `artifacts/review-results/antietam-fb00e7d-opus-high-v1/review.md`. Do not
edit other files, commit or push. State the actual inspected scope and give required
corrections with exact evidence-backed replacements, or say no corrections are
required; keep advisory notes separate. A concise review is sufficient. Return the
path and outcome. AI review is not historical adjudication, independent
corroboration or feature admission.
