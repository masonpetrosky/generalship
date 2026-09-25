# Primary assessment: Averell's Raid on the Virginia & Tennessee Railroad [November 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`b305791dc888d7c9569a6132dfd2a1c36246a775`. Its SHA-256 is `72cbb35357cf538ba460cf4e2b20132a6870d8dc69c58e77b3c8727420bfaee6`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected all 9 claims and 44 citation occurrences, including the null unknown, the NPS summary and both selections with replays, the page-marker maps and the frozen row sets. It reported four required findings and four advisories.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **DM-R1**: accepted with the '2| miles' citation.
- **DM-R2**: accepted with three Echols citations and the memo change.
- **DM-R3**: accepted with two Echols citations and the rationale.
- **DM-R4**: accepted with three Averell citations.
- **DM-A1**: rationale and memo note that Averell gives no total for his own force.
- **DM-A2**: Jackson's 3,500 added to the memo list.
- **DM-A3**: live NPS commanders cited.
- **DM-A4**: the inclosure's exclusion is already disclosed in the registry inspection note.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. No source record changes. Citations rise from 44 to 55; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: one dossier, 9 claims, 1 unknown and 55 citations. Opening strength, the retreat characterization and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
