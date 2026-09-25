# Primary assessment: Command-responsibility ledger v2, batch 1 of 8

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`. Its
SHA-256 is `5b9ece7d5ac72afdd0f14733db3c170751c4d6d9a8e035830b4fe17b321d107b`. The reviewer ran as a fresh headless session with the `evidence-reviewer`
definition in a detached worktree of bundle commit `1b6b83012d485fe9170b9aa5807da9a0b1509884`; see [dispatch.json](dispatch.json).

Each required finding was checked against the cited passage before it was applied, through the
batch builder; the rebuilt ledger replays under its checker. [correction.json](correction.json)
binds the corrected ledger files.

## Required findings

- **R1** (accepted applied): Verified: orn6-stringham-hatteras-selections-v1 section stringham-1861-08-30 (p.120) contains the quoted articles of capitulation styling Stringham 'commanding the Atlantic Blockading Squadron'. Added as a P() citation to NC001 US and added the sentence to the rationale. Commander (Stringham, passage-only), grade C, rule 2, labels and candidates unchanged.
- **R2** (accepted applied): Verified: every Polk mention in the MO009 dossier's resolved passages (Pillow, or3-pillow-belmont-selections-v1, sections 1861-11-09/10/12) is 'Major-General Polk' or 'General Polk'; no full name or initials, and the MO009 description does not name Polk. Registered a separate passage-only entry cs-polk-mo009 (name 'Polk', citation MO009 reported-force-scope 5, quote 'Under instructions delivered in person by Major-General Polk') directly in PASSAGE_ONLY (PO() would slug to v1 'cs-polk'); MO009 Confederate successor and superior set to cs-polk-mo009; rationale's last sentence replaced with the reviewer's wording. Grade A, command_changed and superior_directing unchanged. Any later merge of cs-polk-mo009 / cs-polk / cs-leonidas-polk needs a primary decision with a stating passage.

## Advisories

- **A1** (accepted applied): NC001 US rationale now records that joint_command is used descriptively outside rule 5 (design interpretation for the primary) and notes Martin's 'between 8 and 9 o'clock' clock (cited, orn6-martin-hatteras-selections-v1 martin-1861-08-31) against Stringham's 10 o'clock; both precede the 11.30 landing. Label kept.
- **A2** (kept as is): MO003 Confederate stays grade A: the frozen description's 'his force crossed the Missouri River' is read as the stating passage, and the rationale already keeps the compilers' 'No record of his official status' and the column commanders visible. The primary may downgrade if it does not accept 'his force' as a statement of command (B is not available without dropping the citations; C under a contradiction reading).
- **A3** (accepted applied): Verified the compilers' footnote (MO005 casualty-records 3, section compiler-footnote-confederate-loss). Added FQ citation 'Brig. Gen. J. S. Rains cornmandiDg' to MO005 Confederate and a rationale sentence; rule 3(b), grade C and responsibility_unresolved unchanged.
- **A4** (accepted applied): Verified Britton's 'Colonel Dorsey threw for- ward a superior force' describes Howland's December 27 skirmish near Hallsville, outside the 1861-12-28 interval. MO010 Confederate rationale reworded to rest the first-combat command on the frozen description and place Britton's quote on the 27th. Citations and grade A unchanged.
- **A5** (accepted applied): Verified both quotes in Pierce's report (pierce-1861-06-12). Added 'I directed Colonel Townsend, with his regiment, to advance' and command-roles 7 ('Shortly after I directed all the forces to retire.') to VA003 US; rationale now notes the 'I rode back' quote concerns the night friendly-fire. Grade A unchanged.
- **A6** (accepted applied): Added VA004 command-roles 5 and 6 (Nicolay, blackburns-ford: Tyler 'heeded his instructions'; McDowell ordered all divisions forward on hearing the cannonade) to VA004 US citations. Grade A unchanged.
- **A7** (accepted applied): WV004 Confederate: 'proposed as one person (report)' changed to 'merged on the listing fields'. WV001 US: removed the stale MD008 'Benjamin F. Kelley' merge sentence. No citation or grade change.
- **A8** (accepted applied): Verified the MO001 frozen description contains 'Claiborne Jackson, the pro-Southern Governor of Missouri'; added as a superior citation for MO001 Confederate and the rationale names it as the identity basis for the MO002 listing 'Clairborne Jackson'.
- **A9** (accepted applied): KY002 US: added stated-aims 2 ('I can hold my position with my present force...') and changed echelon brigade -> unknown, since 'what amounted to a brigade' describes only Schoepf's reinforcement and the description gives a combined force of about 7,000. Grade A unchanged.
- **A10** (accepted applied): MO006/MO003 nesting reason now quotes Atchison's 'I delivered your orders to the above commands to hasten to this point (Lexington)...' with MO003 stated-aims 0 added to the citations. Outcome not_nested unchanged. The cross-batch rule for force-scope-only nesting (LA010/LA009 nested vs partial overlap not_nested) is outside this batch and left to the primary.
- **A11** (kept as is): VA007 US keeps command_changed (successor McCall) with superior_directing (McCall); the reviewer finds the pair defensible and the grade unaffected. No change.

This AI review is a separate analysis, not historical adjudication, feature admission or
authorization of any fit. The ledger rates nobody and changes no model input.
