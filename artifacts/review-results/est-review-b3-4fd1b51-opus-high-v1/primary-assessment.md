# Primary assessment: best-estimate ledger review, batch 3 (23 engagements, TN012 to AR008)

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`4fd1b512f9e4db0402537bfe577031a6cc6939f6`. Its SHA-256 is `43c70a6f780bf21e91faed71814d9cb5027055113a9e1ff0767021cc007be11d`. The reviewer ran as a fresh headless session with the
`evidence-reviewer` definition in a detached worktree of bundle commit `9dfd6524c9d88b481474e49ff457436d1ea60a5d`; see
[dispatch.json](dispatch.json).

The primary checked every required finding against the cited passages, the frozen CSV
cells or the registered Livermore page images before applying it. All required findings
are accepted and applied.

## Required findings

- **E3-R1** (accepted applied): TN012: us-jp moved to the Confederate side as cs-jp-forrest (partial lower bound); cs-cist partial lower bound (Wharton's command).
- **E3-R2** (accepted applied): VA032: cs-dd-hooker renamed cs-dd-forbes, codes [scope_unresolved]; Confederate C 62,000 (43,400-80,600).
- **E3-R3** (accepted applied): VA033 cs-sedgwick: adversary + partial lower bound; Confederate grade D with the reviewer null_reason.
- **E3-R4** (accepted applied): LA011 cs-dennis-est: adversary + partial lower bound (McCulloch's brigade).
- **E3-R5** (accepted applied): PA002 cs-lv-eff: engagement_link_unknown; Confederate B 75,050 on the engaged basis.
- **E3-R6** (accepted applied): MS009: cs-lv-pemberton (17,500, scope_unresolved) and cs-lv-mar31 (22,198 present for duty, engagement_link_unknown) added; inventory reason replaced.
- **E3-R7** (accepted applied): MS004 cs-greene and MS009 cs-desc: engagement_link_unknown.
- **E3-R8** (accepted applied): NC010 cs-foster-pettigrew: adversary + partial lower bound.
- **E3-R9** (accepted applied): TN015 us-jp-surrendered: partial lower bound, with loss_timing not_prior per E3-A8 in place of post_engagement_state.
- **E3-R10** (accepted applied): AL001 cs-jp-roddy (350) and TN013 us-jp-cav (600) added as partial lower bounds.

## Advisories

- **E3-A1** (accepted applied): Both completed sums added: TN012 cs-jp-sum 2,800 (high 2,940) and LA011 cs-dennis-sum 2,700 (adversary; C 2,030, 1,350-2,700; the row stays ABC).
- **E3-A2** (kept as is): MS008 row-4 codes kept; the reviewer called them defensible.
- **E3-A3** (accepted applied): Gaps recorded in the memo; MS011 cs-lv-assault loss_timing not_prior; PA002 inventory names the p.103 note 1 figure 77,707.
- **E3-A4** (accepted applied): VA032 us-dd-cap adds scope_unresolved.
- **E3-A5** (not adopted): No wider scan for same-document same-value pairs with different roles was run; the other batch reviews checked their own engagements.
- **E3-A6** (kept as is): MS006 Greene 8,500 basis kept unknown (conservative); the uncited 7,000 not entered.
- **E3-A7** (not adopted): NPS live-figure recording style not aligned; estimates unaffected.
- **E3-A8** (accepted applied): Applied with E3-R9.
- **E3-A9** (accepted applied): Memo table and counts regenerated.

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
