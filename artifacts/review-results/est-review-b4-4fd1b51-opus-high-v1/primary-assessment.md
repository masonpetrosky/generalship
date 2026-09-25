# Primary assessment: best-estimate ledger review, batch 4 (21 engagements, IN001 to TN029)

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`4fd1b512f9e4db0402537bfe577031a6cc6939f6`. Its SHA-256 is `262f6782ef3ca884fcdcba5f39853a4bbd205c550706f8830fbe156f4e8d2b58`. The reviewer ran as a fresh headless session with the
`evidence-reviewer` definition in a detached worktree of bundle commit `266bcbdca528ab97f7238d70b0a070db3565fbe9`; see
[dispatch.json](dispatch.json).

The primary checked every required finding against the cited passages, the frozen CSV
cells or the registered Livermore page images before applying it. All required findings
are accepted and applied.

## Required findings

- **R1** (accepted applied): OH002: cs-shackelford-375 removed; us-rue (375, Major Rue's Union detachment) added as a partial lower bound.
- **R2** (accepted applied): GA003 cs-hindman-column: partial lower bound; Confederate C 30,000 (21,000-39,000).
- **R3** (accepted applied): TN019 cs-foster-est: adversary + other_engagement (Zollicoffer); Confederate A 1,200 (1,140-1,260).
- **R4** (accepted applied): TN020 us-williams: adversary + one_sided_bound upper; US grade D with the reviewer null_reason.
- **R5** (accepted applied): WV012: us-echols-est basis reported_engaged; us-jackson-est adversary + partial lower bound; US C 5,250 (3,500-7,000).
- **R6** (accepted applied): TN027 cs-martin: scope_unresolved; Confederate C 2,000 (1,400-2,600).
- **R7** (accepted applied): GA004 and TN024 Livermore inventory reasons replaced with the reviewer text.

## Advisories

- **A1** (kept as is): IN001 raid-start figures left as scope_unresolved; same row and outcome.
- **A2** (accepted applied): OH001 us-hobson: partial_scope + engagement_link_unknown, bound null.
- **A3** (accepted applied): OH002 inventory reason 'one-sided and pre-engagement'; cs-shackelford-400 loss_timing not_prior.
- **A4** (accepted applied): TN019 us-jones: adversary + other_engagement, basis reported_engaged.
- **A5** (accepted applied): TN020 us-ninth-corps adds engagement_link_unknown.
- **A6** (accepted applied): TN022 link reversed: us-cw reproduction_of us-hatch, with a note that the dependence is inferred from equal values.
- **A7** (kept as is): GA004 cs-lv and TN024 us-lv keep Livermore's printed 'Total engaged' label, consistently for both.
- **A8** (accepted applied): TN024 us-hooker and TN029 us-wolford bound null; TN027 us-martin-est adds partial_interval, bound null.
- **A9** (kept as is): TN026 us-desc kept as coded; the description ties Shackelford's force to Bean's Station.
- **A10** (accepted applied): TN025 us-burnside adds engagement_link_unknown.

## Result

The corrected ledger `data/estimates/side-strength-v1.json` (SHA-256 `0656b03cbdaa088849dc3795f9c6a9e9d6762be10f53f28e4285be46f7fcde89`) replays with `estimate-check`,
together with the corrections from the other four reviews: sides A/B/C/D 59/21/26/76;
fit-eligible rows 21/29/37 at A, A-B and A-C; 7 rows excluded as post-start. The engine is
`generalship/estimates.py` (SHA-256 `af540a924aed29b20032319b8779742c0f43e991c118ee747672bba73fc3a32f`). [correction.json](correction.json)
lists every disposition.

This AI review is a separate analysis. It is not historical adjudication, proof of source
independence or feature admission. No follow-up review of the corrections was run. Nothing
is fitted; the locked evaluation (design §6) needs an explicit owner authorization naming
the reviewed ledger's hash. The frozen baseline is unchanged.
