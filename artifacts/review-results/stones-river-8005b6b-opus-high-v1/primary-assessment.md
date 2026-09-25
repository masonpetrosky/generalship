# Primary assessment: Stones River Campaign

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`8005b6b484045b01f3e4674b593c8f8d7180e36e`. Its SHA-256 is `ce9d9bd0090902cc82005f5b928d3a6325eb0ba25e7043f2f08a2c75baf10c73`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified all 33 bound input hashes and inspected both dossiers, 20 claims and 58 citation occurrences, including 2 null unknowns, two NPS summaries, the new Cist selection and the pinned parent, and the frozen row sets. It reported five required findings and five advisory notes.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **R1**: accepted; Cist's 'shortly after this engagement' sentence now supports Morgan's commission timing.
- **R2**: accepted; Bragg's order and the Cleburne–Withers–Polk notes are cited and the retreat decision attributed to Bragg's noon consultation with his generals.
- **R3**: accepted; NPS's 44,000 scoped to the December 26 departure, rationale corrected, December 10 return cited, memo line changed.
- **R4**: accepted; the unsupported 'after December 31' date replaced by Cist's placement, and the 10,070 cavalry cited.
- **R5**: accepted; eleven missing citations added across both dossiers.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. Advisory A1 is adopted (Bragg's live heading rank recorded with two citations); A2 would need a versioned metadata revision of a committed source record and is not applied; A3–A5 need no change. Citations rise from 58 to 79; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: two dossiers, 20 claims, 2 unknowns and 79 citations. Opening strengths, the picket-warning dispute, casualty reconciliation and original-document verification remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
