# Primary assessment: Tullahoma or Middle Tennessee Campaign [June 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`d6824e51b354adffce6d255775a1e6888cbfdab0`. Its SHA-256 is `9a8a7127e7abbfb5cdbe7e6d830be4695a789c2327509836482dda5c5d3a5b02`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected the dossier's 9 claims and 41 citation occurrences, including the null unknown, the NPS summary, both selections in full with replays, the OR XXIII report list and the frozen row sets. It reported seven required findings and three advisories.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **TL-R1**: accepted; the 43,089 quote extended to Bragg's June 20 Shelbyville report and Cist's two-brigade attack added with its citation.
- **TL-R2**: accepted; Bate's right-hand section commanding the exit and the left-hand artillery moved to the rear hills are separated, with two citations.
- **TL-R3**: accepted; Reynolds's lead and support of Wilder cited, and the live NPS commanders cited.
- **TL-R4**: accepted; Manchester cited and Bate's holding action scoped to the fewer than 700 engaged, citing his figure.
- **TL-R5**: accepted; Cist's 231 scoped to Johnson's command at Liberty Gap on the following day, Bate's 146 tied to June 24, and the memo bullet changed.
- **TL-R6**: accepted; the p.161 locator now reports the OCR header '1G1'.
- **TL-R7**: accepted; three metadata_only v2 records give the 1889 imprint at parent offset 1084, and TN017 cites the v2 Bate selection. The later Morgan's Raid OR selections carry the same text and are left for that review.
- **TL-A1**: the copied Cist dependency count would need a metadata_only revision; no claim is affected.
- **TL-A2**: the Brannan and Elk River clauses are cited.
- **TL-A3**: whether the live 583 includes Liberty Gap stays an open question.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. Three metadata_only source revisions (TL-R7) are recorded in data/sources.json. Citations rise from 41 to 54; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: one dossier, 9 claims, 1 unknown and 54 citations. Opening strength and whether the live casualty figure includes Liberty Gap remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
