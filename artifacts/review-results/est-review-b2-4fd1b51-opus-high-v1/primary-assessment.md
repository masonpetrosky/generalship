# Primary assessment: best-estimate ledger review, batch 2 (22 engagements, TN006 to AR006)

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`4fd1b512f9e4db0402537bfe577031a6cc6939f6`. Its SHA-256 is `33867a7c5143cb18496d0edba42e9216f8d016339c8fa5c9a09e6b9a862f9be5`. The reviewer ran as a fresh headless session with the
`evidence-reviewer` definition in a detached worktree of bundle commit `2c490165397e7991b8a2fbaf2859e9a939cf61e8`; see
[dispatch.json](dispatch.json).

The primary checked every required finding against the cited passages, the frozen CSV
cells or the registered Livermore page images before applying it. All required findings
are accepted and applied.

## Required findings

- **R1** (accepted applied): VA022: us-lv and cs-lv partial_scope lower bounds after the primary confirmed p.87 note 4 on page image livermore-p87-image-v1; US grade D with the reviewer null_reason; the frozen row leaves the fit-eligible set.
- **R2** (accepted applied): MD002 cs-mcclellan re-cited to Palfrey's Confederate sentence ("probably some thirty thousand in all"), basis unknown. The primary reads design §2 source scope (registered sources) as allowing a quote from an already-cited registered section; the narrower reading would drop the input. Recorded in the memo.
- **R3** (accepted applied): MD002 scope: us-mcclellan scope_unresolved; us-lv and cs-lv partial lower bounds; us-palfrey-cap partial with bound null; cs-mcclellan adversary + scope_unresolved. The row is now ABC and no longer post-start.
- **R4** (accepted applied): MS001 cs-greene partial_scope lower bound; bound_conflict now shown.
- **R5** (accepted applied): MS002 us-greene basis reported_effective.
- **R6** (accepted applied): NC007 us-smith-est adds post_engagement_state; the row is excluded as post-start.
- **R7** (accepted applied): VA028 us-palfrey post_engagement_state (December 13 morning reports).
- **R8** (accepted applied): KY009 us-nps-desc: unknown basis, one_sided_bound upper, link removed.
- **R9** (accepted applied): TN006 cs-nps-desc: unknown basis, link removed.
- **R10** (accepted applied): Inventory reasons (a) MD002, (b) KY009, (c) WV010 and (d) VA022 replaced with the reviewer text.

## Advisories

- **A1** (accepted applied): KY007 cs-smith and MS003 us-greene-assault: bound null (a cap on a part does not bound the side).
- **A2** (accepted applied): NC009 us-smith-est bound lower.
- **A3** (accepted applied): TN010: Livermore entry kept as matching; the reason (pre-battle returns of the same army) recorded in the cs-lv-pfd note.
- **A4** (kept as is): KY009 Union basis tension kept visible, as the reviewer advised.
- **A5** (accepted applied): Transcription gaps recorded in the ledger memo; successor deferred.
- **A6** (accepted applied): AR006 dispute stated in the rationale.
- **A7** (accepted applied): TN006 dispute stated in the rationale.
- **A8** (accepted applied): TN011 us-jp-1800: partial_scope lower bound, compiled, newspaper note; inventory reason updated.
- **A9** (accepted applied): VA025 Livermore composite entry recorded as other_engagement.
- **A10** (not adopted): MS002 returns left as linked to the engagement; no point would move.
- **A11** (accepted applied): VA028 November 10 figure reason: earlier return, engagement_link_unknown.
- **A12** (kept as is): MS001 description range kept; disclosed in the note.
- **A13** (kept as is): Cited-source binding kept as a deliberate choice; recorded in the memo.

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
