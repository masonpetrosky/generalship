# Primary assessment: best-estimate ledger review, batch 1 (25 engagements, KY005 to VA021)

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`4fd1b512f9e4db0402537bfe577031a6cc6939f6`. Its SHA-256 is `44eec013a92798ac559a2c133134ec764a47859d3d540edff70011dc1c64d50e`. The reviewer ran as a fresh headless session with the
`evidence-reviewer` definition in a detached worktree of bundle commit `a8b422c35f4493a706854802cfbf5fb295f0fbc9`; see
[dispatch.json](dispatch.json).

The primary checked every required finding against the cited passages, the frozen CSV
cells or the registered Livermore page images before applying it. All required findings
are accepted and applied.

## Required findings

- **R1** (accepted applied): KY005 US: sum us-sum deleted; us-left and us-reinf are partial lower bounds; US grade D with a null_reason (rule 6 forbids summing a start force and an arrival).
- **R2** (accepted applied): TN002 US us-start: partial_scope, bound lower. The US side is now C 27,000 from the post-start figure, and the row is excluded as post-start.
- **R3** (accepted applied): NC002 us-nps-landed: basis unknown, reproduction link removed.
- **R4** (accepted applied): TN003 Confederate: engagement_link_unknown added to cs-return-before, cs-lv-eff, cs-r136-eff and cs-r136-present.
- **R5** (accepted applied): MS016: interval_unresolved added to all three inputs (May figures only).
- **R6** (accepted applied): TN002 Livermore inventory reason replaced with the reviewer text.
- **R7** (accepted applied): VA017 Livermore pages [82, 83, 84], with the p.84 note 7 reason.

## Advisories

- **A1** (kept as is): MS016 "probably not much over 50,000" kept as an approximate value; the reviewer called that reading defensible.
- **A2** (accepted applied): Partial-scope inputs carry bound: lower (KY005, TN003 us-atenn-pfd).
- **A3** (accepted applied): TN003 us-force-sunday note records the 32,000-33,000 passage and the conservative choice.
- **A4** (kept as is): VA101 cs-desc division figure left as coded; the change would only add a label.
- **A5** (not adopted): VA016 present-for-duty 16,808 not entered; no estimate effect. Recorded here.
- **A6** (accepted applied): Transcription gaps recorded in the ledger memo; a versioned successor transcription is deferred.
- **A7** (kept as is): Livermore's own exclusions (VA017 note 6, TN003 note 4) accepted as the source's population; kept in view.
- **A8** (accepted applied): Handled by batch 2 R8 and R9 (KY009, TN006 restatements unlinked).
- **A9** (kept as is): Bundle binding gap noted; the reviewer recorded the unbound hashes.

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
