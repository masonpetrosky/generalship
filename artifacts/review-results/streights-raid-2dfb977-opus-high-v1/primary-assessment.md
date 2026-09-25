# Primary assessment: Streight's Raid in Alabama and Georgia [April 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`2dfb977b75537c2598429b9399e15287949d78d1`. Its SHA-256 is `2c1e025b920db343e533ec767ca7c4c11f0fba584933d9d092cd8557a0332ac6`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected the dossier's 9 claims and 41 citation occurrences, including the null unknown, the NPS summary, both new selections in full with parent context at boundaries, and the frozen row sets. It reported three required findings and five advisory notes.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **SR-R1**: accepted with value and rationale as proposed; three citations added and the memo bullet replaced.
- **SR-R2**: accepted; 'Roddy's men' and an unstated hospital side; the optional Cist 'same afternoon' citation and the forty-of-350 quote added.
- **SR-R3**: accepted in both parts with both optional citations.
- **SR-A1**: the copied Cist dependency count would need a metadata_only revision; no claim is affected.
- **SR-A2**: the dossier already scopes the rank conflict to the live heading.
- **SR-A3**: the conflicting afternoon clocks are recorded as an open question, not reconciled.
- **SR-A4**: 'lying down concealed' citation added to the terrain claim.
- **SR-A5**: the OCR synopsis figure outside the selections is noted only as an unverified lead.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. The dossier's open questions gain the unreconciled afternoon clocks. Citations rise from 41 to 49; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: one dossier, 9 claims, 1 unknown and 49 citations. Opening strength, the record's scope within April 30 and casualty attribution remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
