# Primary assessment: Reopening the Tennessee River [October 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`a71231105d0b86140739ffb20163311fa2439ac1`. Its SHA-256 is `3530f858c8cc3bb20d3e239cd8fa35785e96fa80c141c8c822eca40660427456`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected all 9 claims and 40 citation occurrences, including the null unknown, the NPS summary and both selections with replays, the page-marker maps and the frozen row sets. It reported five required findings and three advisories.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **RT-R1**: accepted with the extended quote.
- **RT-R2**: accepted with the Cist and two NPS citations.
- **RT-R3**: accepted; the uncited clause is removed.
- **RT-R4**: accepted with the 6th South Carolina citation and the memo change.
- **RT-R5**: accepted; value and rationale changed.
- **RT-A1**: the casualty rationale says the match does not establish derivation or coverage.
- **RT-A2**: the inherited Cist dependency count needs a metadata_only revision.
- **RT-A3**: Jenkins's missing report and Law's report remain uninspected.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. No source record changes. Citations rise from 40 to 44; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: one dossier, 9 claims, 1 unknown and 44 citations. Opening strength, the withdrawal order's source and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
