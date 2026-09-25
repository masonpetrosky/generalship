# Primary assessment: Strength ledger v2, batch 4 of 8

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`. Its
SHA-256 is `a5a551f110cf27bdd0b771b168c12c6c4c781e5ca7012d36494854ebd12768f4`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `8ca4b5cbc040e166e982c4a5b675382e7c97ecd8`; see [dispatch.json](dispatch.json).

Each required finding was checked against the cited passage before it was applied, through the
batch builder; the rebuilt ledger replays under its checker. [correction.json](correction.json)
binds the corrected ledger files.

## Required findings

- **B4-R1** (accepted applied): Verified at Pond p.21 (new-market section): 3,440 + 350 = 3,790, so the printed 4,590 includes Imboden's 800 cavalry; it is a three-arm whole-side total. VA110 cs-imboden-engaged is now codes [], bound null, basis unknown, class B, with the reviewer's note. The cs-imboden-cav note, the inventory component text and the Confederate rationale are updated. VA110 CS: A 4,090 (3,890-8,500) stays the same; bound_conflict drops.
- **B4-R2** (accepted applied): Verified: Price p.780 limits 'only some 1,200 men actually engaged' to the April 4 attack ('The next day (April 4) were attacked...'). Britton pp.264-265 dates Preston's skirmish at the ford and the capture of sixteen Confederates to April 3, inside the frozen April 3-4 record. AR012 cs-price-1200 is now [partial_interval], bound lower, class bound. The Confederate null_reason and rationale are added. AR012 CS: A 1,200 becomes D. US stays C 7,500 (5,000-10,000) but loses basis_mixed. The row leaves set3.
- **B4-R3** (accepted applied): Verified: Hunter p.99 gives the 10,000-15,000 estimate on the 17th and, in the next sentence, reports overnight trains and troop arrivals; the frozen record runs June 17-18. VA064 cs-hunter-17th is now [adversary_or_hearsay_estimate, partial_interval], bound lower, class bound. The Confederate null_reason and rationale are added. VA064 CS: C 9,380 becomes D. US stays C 18,000 (12,600-23,400) but loses basis_mixed. The row leaves set3.
- **B4-R4** (accepted applied): Verified: in Thomas inclosure 4, Gladden reports the Buzzard Roost and Rocky Face losses and says he was on the field; inclosure 5 dates Buzzard Roost to February 24-25, 1864, after the frozen start of 1864-02-22. No passage supports the old 'about February 20'. GA006 cs-gladden is now [adversary_or_hearsay_estimate, post_engagement_state] with the reviewer's note, and the rationale is updated. CS stays C 22,500 (15,000-30,000) and gains post_start_information; the row is now in the post-start exclusion.
- **B4-R5** (accepted applied): Verified: none of the Polignac mentions in irwin-red-river-selections-v1 says he reached the crossing as the last Union troops passed. At p.329 Irwin has Wharton 'supported by Polignac' engaging Lucas on the 22d, and at p.330 Bee and Major hold the bluff. The LA021 inventory text is replaced with the reviewer's wording. No estimate change (CS stays D).

## Advisories

- **B4-A1** (kept as is): 'probably 16,000 men on the field, and perhaps more' is kept as a hedged point estimate, not a one-sided lower bound. It is not one of tier-2's over/nearly/at least forms, and the reviewer judges the current coding defensible. LA022 US stays C.
- **B4-A2** (kept as is): VA111 Vaughn's 5,600 stays whole-interval: no inspected passage shows fighting on June 6. The reviewer's replay shows no change under either alternative coding.
- **B4-A3** (accepted applied): Applied in part: TN030 us-nps-white and us-nps-usct now carry bound 'lower', the convention every other component_of input in the v2 batches uses (24 of 24). No effect on the estimate (US A 600, 530-700). Not adopted: treating us-nps-sum as a lower bound because the New Era crew is uncounted. The same caveat applies to the frozen 600 and to Leaming's 'entire garrison', so whole-side treatment is kept for consistency.
- **B4-A4** (kept as is): MS013 cs-forrest-2500 stays class B with basis unknown. There is no separate frozen February 21 record, so it is not a composite; the reviewer calls the coding reasonable.
- **B4-A5** (kept as is): AL002 cs-desc stays B under extractor policy 1, with derivation_unknown already recorded. The reversed NPS cell stays scope_unresolved: no tier-2 code names side misattribution, and any row-4 code gives the same class.
- **B4-A6** (kept as is): AR016 cs-britton-10000 keeps bound upper. The reviewer calls the direction arguable with no effect: CS is grade D with no candidate either way.
- **B4-A7** (not adopted): These are engine consequences, noted for the record, not coding errors: VA049 CS bound_conflict, VA111's post-start exclusion under the v1 engine-review R1 convention, the VA110 US high from NPS's ordered 10,000, the KY010 CS high from Hicks, and the MS012 US point from NPS's February 3 main force. No change: the fixed rules are reported, not overridden.

This AI review is a separate analysis, not historical adjudication, feature admission or
authorization of any fit. The ledger rates nobody and changes no model input.
