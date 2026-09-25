# Primary assessment: Strength ledger v2, batch 1 of 8

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`. Its
SHA-256 is `d190bb2afcff2ff19b8531da8b11346cb0fed397dcf6a81cb4e40d44bcc7d951`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `eddd8313723e0bf2ea9ff5be80a577dc43484588`; see [dispatch.json](dispatch.json).

Each required finding was checked against the cited passage before it was applied, through the
batch builder; the rebuilt ledger replays under its checker. [correction.json](correction.json)
binds the corrected ledger files.

## Required findings

- **R1** (accepted applied): Verified: Pegram's July 15 addendum (pegram-1861-07-15, p.268) reads "their force engaged at Hart's, as before mentioned, three thousand", referring back to the July 14 figure (p.264). WV003 us-pegram-3000-hart basis unknown -> reported_engaged (codes unchanged, note cites the addendum). It now groups with us-pegram-3000-engaged under rule 2. WV003 US: grade C, point 1900 and low 1330 unchanged; high 3000 -> 2470; range_groups drops us-pegram-3000-hart; the label single_input is added. Nested sets unchanged.
- **R2** (accepted applied): Verified in livermore-transcription-v2 section p78-supplement: "General Fremont's dispatch of August 13, placing the force at 8000, assumed the presence of 2000 Home Guards, when in fact they numbered only 200". A compiler's rejection is not a design §3 row 1 non-use ground. The dispatch date alone is not post_engagement_state (tier-2 §3 item 2), and the figure is the Union department commander's own-side figure relayed by a compiler (extractor policy 3). Added MO004 US input us-lv-fremont-8000 (L, p78-supplement, 8000, basis unknown, no codes, class B); it is added to inventory.livermore.inputs and the reason is rewritten. MO004 US: grade B, point 5400 and low 4200 unchanged; high 7480 -> 9200; point_groups [us-lv, us-lv-fremont-8000]. Labels, nested sets and the Confederate side are unchanged. The reviewer's alternative, source_role_unresolved (class C), was not used because the role is the own-side department commander's.

## Advisories

- **A1** (primary decision): No change to KY003. The reviewer asks for one criterion, across batches, for linking CWSAC rows to equal-valued report figures: TN022 links them ("inferred from equal values"), while VA003 and KY003 do not. That is a convention for the primary, not a decision for this batch. If KY003 cs-cw were linked to cs-williams-1010, the CS side would become grade B, 1010 (860-1160), and the row would stay in set3_ABC only.
- **A2** (accepted applied): Verified: the NPS cell quote reads '31680 total (US 28450; CS 3230;)', and the frozen CWSAC row reads 32,230. The VA005 inventory reason now calls the cell a copy discrepancy within one compiled-table lineage (the frozen row is entered as cs-cw; the page total carries the dropped digit) instead of a 'display error'. The cell is still not entered. No estimate change.
- **A3** (not adopted): The wording is a naming convention shared with the v1 ledger, and the change would have no effect: both sides are grade A, and post-start candidates enter the hull only when they set the point. Retagging these inventory reasons belongs in a cross-ledger convention change, not in this batch.
- **A4** (not adopted): The two passages differ. SC001 gives 'a garrison of 128 souls all told' next to citation 2's component list (officers, NCOs and privates, musicians, 43 workmen), which reads as a headcount of those present. VA003 Magruder's 'Our force, all told' does not say what it counts. The reviewer judges SC001's present basis defensible, and aligning the two would change an estimate without passage support.
- **A5** (not adopted): The reviewer calls whole-side scope a plausible reading of Nicolay's 'volunteer force of from four to six thousand supported the rebel batteries', set against Anderson's whole garrison. Adding scope_unresolved would change only a label.
- **A6** (not adopted): The reviewer finds class B acceptable: Thompson's letter ties the 2,000 to 'a victorious army', the force that fought. Kept as coded.
- **A7** (not adopted): The handling follows v1 practice for unlinked restatements by a compiled history. Keeping the batch consistent with that practice; the only effect of linking would be a label.
- **A8** (kept as is): Rule 2 groups equal printed values only. The inputs already note the difference of 2 from Livermore (28,452 and 32,232). compiled_dependence is already set, and points, ranges and labels are unaffected.
- **A9** (accepted applied): Verified: Lane's September 4 letter says 'their force is in the neighborhood of 6,000 ... and are rapidly re-enforcing', state at writing, and the frozen interval is 1861-09-02. Added post_engagement_state to MO005 cs-lane-6000. It stays class C, and the estimate, labels and nested sets are unchanged.
- **A10** (accepted applied): Verified in citation 3's section (KY003): 'On yesterday Captain Holliday, with a small command, met this column from John's Creek. A skirmish took place.' This quote was added to the us-williams-sum note to document that the John's Creek column is covered within the interval. No estimate change.
- **A11** (kept as is): These are engine consequences, reported by the reviewer and not errors (WV004 CS, WV002 CS, VA004, VA006 CS, VA007 CS bound_conflict, MO007 US). Nothing changed.

This AI review is a separate analysis, not historical adjudication, feature admission or
authorization of any fit. The ledger rates nobody and changes no model input.
