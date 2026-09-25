# Primary assessment: Command-responsibility ledger v2, batch 7 of 8

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`. Its
SHA-256 is `429c4a47273e030682eec0d489d5e6e44c3ec4fbacf54fefa5f54a0ee1eccad2`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `4ad2dc29f803ebc1ca151bd5b8239dcf6c6a8649`; see [dispatch.json](dispatch.json).

Each required finding was checked against the cited passage before it was applied, through the
batch builder; the rebuilt ledger replays under its checker. [correction.json](correction.json)
binds the corrected ledger files.

## Required findings

- **F1** (accepted applied): Checked Price 1864-12-28 (p.632: Shelby sent 'to divert the attention of the enemy'; 'Clark was unable to commence the attack for one hour after Brigadier-General Shelby had engaged them') and Britton glasgow p.454 ('In the plan of attack it had been arranged ...'; 'the Confederate force advancing under General Clark'). No passage puts either tied brigadier over the side's engaged forces; Shelby commanded a diversionary detachment, not the side. MO022 Confederate: commander cs-joseph-shelby -> null, grade A -> D, rule 3a -> 3c, echelon detachment_or_post -> unknown, labels + responsibility_unresolved, candidates [Clark] -> [Clark, Shelby]; Britton plan passage added (dossier citation via FQ); rationale replaced with the reviewer's text. Superior Price unchanged.
- **F2** (accepted applied): (a) VA076 passages give only 'Breckinridge' / 'Major-General Breckinridge'; docs/research/ledgers-v2.md requires matching initials or full name for a passage-only merge. Candidate cs-john-c-breckinridge replaced by passage-only PO('Breckinridge') = cs-breckinridge, citing Gardner 'paroled by Major-General Breckinridge' (shooting-of-wounded-prisoners[1]), exactly the reviewer's registry entry; the registry and its hash are rebuilt by the primary. (b) Verified: only the Oct 1 dispatch is addressed to 'Brig. Gen. John Echols'; the Oct 2 5 p.m. dispatch is to 'Capt. H. T. Stanton'. Both rationale sentences replaced with the reviewer's text. Choice Jackson, grade C, rule 2, labels unchanged.
- **F3** (accepted applied): RANK_ORDER_V2 navy includes 'Lieutenant Commander'. TN032 US rationale sentence replaced with the reviewer's text. Choice null, grade D, rule 5, joint_command unchanged.

## Advisories

- **A1** (kept as is): VA121 US echelon corps_or_wing kept: Pond shows Torbert directing two cavalry divisions (Merritt, Custer), an above-division command, and the rationale already states that no passage names his formation.
- **A2** (accepted applied): Partly adopted. Williams and Vaughn not added as passage-only candidates (surname only, no rank or role; a 'Vaughn' PO would collide with the VA111 cs-vaughn entry and so identify them on surname alone); the VA076 CS rationale now states why they are excluded. The frozen description's 'On the morning of October 1, the Federals attacked' is now cited and the conflict with the frozen Oct 2 interval recorded in the rationale. If the primary wants Williams/Vaughn as candidates, it needs a distinct non-colliding passage-only ID scheme (primary's call).
- **A3** (kept as is): TN032 US rationale already records the rule-5 second-case alternative (Thompson, grade C) from Sinclair's responsibility finding; left visible.
- **A4** (accepted applied): MO024 US: added Britton 'General Curtis, who was present on the field directing the general movements of his forces' (dossier reported-force-scope[4]) to citations and a clause to the rationale. Grade A unchanged.
- **A5** (not adopted): Informational: KS003/KS004/MO028 share the 1864-10-25 interval, so contained_pairs yields no pair (same as v1). Nothing the batch file can record; noted for the primary's report on views that include all three.
- **A6** (not adopted): Moot: F1 was accepted; the plan passage and 'to divert the attention of the enemy' are both in the MO022 CS citations and rationale.

This AI review is a separate analysis, not historical adjudication, feature admission or
authorization of any fit. The ledger rates nobody and changes no model input.
