# Primary assessment: Strength ledger v2, batch 5 of 8

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`. Its
SHA-256 is `857d52b2e2c29c987789a7249c721c4b9192a04f1a4d5d0455e73462e3017d7b`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `09c3a6b873b6bbafac2c1363cd3f60185a7c45da`; see [dispatch.json](dispatch.json).

Each required finding was checked against the cited passage before it was applied, through the
batch builder; the rebuilt ledger replays under its checker. [correction.json](correction.json)
binds the corrected ledger files.

## Required findings

- **R1** (accepted applied): Checked: VA047 citation 3 (nps-va047-v1 '39000 total (US 39000; CS 0;)') and VA053 citation 2 (nps-va053-v1 '57000 total (US 39000; CS 18000;)') are the same cell, coded other_engagement at VA047 and class A at VA053. No cited passage says 39,000 is a campaign figure. The doubt comes from the VA047 frozen description ('a Union division'), the VA053 page ('Butler's 30,000') and Humphreys p.149 (Ames about 5,000, Hinks 5,000 and about 3,000 in the intrenchments away from the fight), which is the 'uncertain' case. The ledger's VA004 us-nps precedent codes such a cell [derivation_unknown, scope_unresolved], class C. Applied: VA047 us-nps codes [DU, OE] -> [DU, SU] (class unusable -> C), with the note, rationale and US null_reason removed. VA047 US goes D -> C 39,000 (27,300-50,700), rule3_median, with labels applicability_unresolved, compiled_dependence, derivation_unknown, single_input and whole_engagement_leakage. VA053 us-nps codes [DU] -> [DU, SU] (A -> C), with the note citing Butler's 30,000 and Humphreys p.149. VA053 US stays A 30,000 (28,500-40,950) and gains applicability_unresolved. VA047 us-desc (33,000) stays other_engagement. Nested sets are unchanged (VA047 [], VA053 set1_A/set2_AB/set3_ABC). The results match the reviewer's recomputation exactly.

## Advisories

- **A1** (accepted applied): Checked the VA071 interval (frozen Aug 13-20; Livermore heads the entry Aug 14-19). Kept it uncoded and recorded the reason in the us-lv-eff, us-lv-pfd and cs-lv notes: the same II Corps, X Corps and Gregg's division crossed on the night of Aug 13-14 and withdrew on the 20th. The estimates are unchanged (C/C).
- **A2** (accepted applied): VA054 citation 5 reads 'of very nearly 16,000 infantry'. us-smith was recoded from [PS, PES] bound=lower to [PS, PES, OSB] with no bound, as VA062 cs-hoke. The note and US null_reason were updated. The estimate is unchanged (D/D).
- **A3** (accepted applied): VA063 citation 7 reads 'The Second Corps had 20,000 enlisted men, not 28,000, as has been stated.' Added an inventory reason for the 28,000: an unattributed part-of-force figure that Humphreys rejects, not entered. No estimate effect.
- **A4** (accepted applied): Confirmed that Wilson's 'about 5,500 cavalry and twelve guns' is VA113 citation 2 and is not among the VA067 or VA068 citations. Added to both US null_reasons that it was considered and not borrowed across engagements. The grades stay D.
- **A5** (accepted applied): VA056 inventory reason for Wild citation 7 ('and probably triple') reworded: a multiple of the Union garrison, not a count; the first term is garbled (unreadable_value); not entered. No estimate effect.
- **A6** (kept as is): The reviewer confirms that the VA083 Confederate coding is correct and that the result follows from the declared rules. The rationale already states the mechanism. No change.
- **A7** (kept as is): The reviewer confirms VA072 Confederate grade D and the bound-only coding of Livermore's 14,787. No change.

This AI review is a separate analysis, not historical adjudication, feature admission or
authorization of any fit. The ledger rates nobody and changes no model input.
