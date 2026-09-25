# Primary assessment: Strength ledger v2, batch 8 of 8

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`. Its
SHA-256 is `b3199132027fb071470ad08b834e5ba6c3ea13677ba4dd42bf9d5f23da5cc601`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `c08ab6f1c424772520144afa9ab146dc9bafb77a`; see [dispatch.json](dispatch.json).

Each required finding was checked against the cited passage before it was applied, through the
batch builder; the rebuilt ledger replays under its checker. [correction.json](correction.json)
binds the corrected ledger files.

## Required findings

- **R1** (accepted applied): NC020 US us-johnston-44000: checked Johnston's March 27 report (or47-1-johnston-carolinas-selections-v1, johnston-1865-03-27): 'amounting to near 44,000, including losses' adds losses the passage does not date before the 1865-03-19 start. Added flags=['this_or_later_losses'] (loss_timing none -> not_prior), appended the note text and extended the rationale. Replay: class C (opponent_or_hearsay) and point 33,000 (22,000-44,000) unchanged; US side gains post_start_information; row excluded_post_start_information true. The extraction memo counts (set3_ABC 130->129, post-start exclusions 20->21) are for the primary to update in docs/research/ledgers-v2.md.
- **R2** (accepted applied): GA028 CS cs-hazen-garrison: Hazen report passage 'The captures were as follows: The garrison, including killed, 250 men and officers' confirmed; the cited reported-force-scope claim has phase 'unresolved', so post_outcome_claim (reserved for post_outcome-tagged claims) does not apply. Codes [POC] -> [], loss_timing none -> not_prior, class unusable -> C (design §3 row 3), note replaced; rationale sentence replaced as proposed. Matches v1 precedent TN006 us-cist-surrendered and WV010 us-surrendered (codes [], not_prior, C). Estimate unchanged: A 120 (110-210).
- **R3** (accepted applied): SC010 CS cs-sc-reserves: Smith report confirms 'At midnight Brigadier-General Chesnut arrived at Grahamville Station with about 3o0 effective muskets of South Carolina reserves', after 'During the night the enemy retired'. The printed 350 was an unsupported OCR correction and the body arrived after the action. Input deleted (preferred option) and replaced in the reported-force-scope inventory by the reviewer's reason string. Estimate unchanged: A 1,400 (1,330-1,470).

## Advisories

- **A1** (accepted applied): AL005 US us-canby-assembly: Canby's June 7 section confirmed (Veatch ordered in to report to Steele; 'On the 3d Garrard was ordered in to complete the investment'). Coding kept (scope_unresolved + engagement_link_unknown, C); note extended to record the transfers to the Blakely investment (AL006) and why other_engagement was not used. Estimate unchanged: C 32,200 (22,540-41,860).
- **A2** (kept as is): FL006 CS cs-cw read as the Georgia reinforcements (partial_scope) following the dossier and Newton's postscript. The reviewer calls it a genuine reading dispute and requires no change; the reading and its alternative (scope_unresolved gives C 1,000 (700-1,750) instead of rule-4 C 1,310 (880-1,750)) stay visible for the primary.
- **A3** (not adopted): 'near N' convention: NC020 follows the ledger majority (approximate, NM001/MO010/FL005); OK004 (one_sided_bound) is outside this batch. A ledger-wide convention is a primary decision; no change here.
- **A4** (accepted applied): VA086 US us-lv: Livermore p137 transcription confirmed ('Add loss of 5th corps, March 29 and 30 394 ... Total engaged [2] 45,247'), losses dated before the 1865-03-31 start. Added flags=['prior_losses_only'] (loss_timing none -> prior_engagements_only) and a note. No class effect (other_engagement, unusable); side stays D.
- **A5** (accepted applied): AL007 US us-jordan: the Jordan and Pryor passage ('press directly for Selma with his other divisions, still at least 9000 strong') is the compilers' narrative; per v1 policy it is a compiled figure, not visibly an opponent estimate. Removed adversary_or_hearsay_estimate (codes [ADV, OSB] -> [OSB]); still bound-only on basis unknown, which is not point_basis, so no effect: C 13,500 (9,450-17,550).
- **A6** (not adopted): Cross-batch consistency of capture/surrender counts coded post_outcome_claim (GA001 cs-gillmore-385, LA010 cs-prisoners, KY011 us-morgan-hobson) is outside this batch file; for the primary to check claim phases and apply R2's reasoning where the claim is not tagged post_outcome.

This AI review is a separate analysis, not historical adjudication, feature admission or
authorization of any fit. The ledger rates nobody and changes no model input.
