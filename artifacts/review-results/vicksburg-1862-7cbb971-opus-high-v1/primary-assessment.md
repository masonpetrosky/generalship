# Primary assessment: Operations Against Vicksburg [December 1862-January 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`7cbb97100ca5db247610b8e198b58f44fd5f5be4`. Its SHA-256 is `b94033b16aabec7cbb0cac9a3dd8030fee637713b322e0106d86189e5fb7c858`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified all 33 bound input hashes and inspected both dossiers, 19 claims and 62 citation occurrences, including 2 null unknowns, both NPS summaries, the Greene title/preface and both Chapter III sections, and the frozen row sets. It reported six required findings and five non-blocking notes.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **VB-R1**: accepted; both unknown-strength rationales now state the blank frozen bounds (missing_numeric_strength) and that the live NPS zeros are not measured absence.
- **VB-R2**: accepted with the optional citation; Churchill named as the frozen Confederate commander and the live heading's omission of McClernand recorded.
- **VB-R3**: accepted; only the Confederate 187 is dated, with the p.79 quote added.
- **VB-R4**: accepted with the optional widened quote; the letter does not name the capturing force, and 'that enemy on our rear and flank' is cited.
- **VB-R5**: accepted; Thompson's Lake is the obstacle and the causeway its only crossing, with two p.77 quotes added.
- **VB-R6**: accepted; the high-water qualifier is restored and the five crossings cited (pp.75–76).

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. Notes VB-N1 to VB-N5 are not applied. The VB-R1 template wording in earlier dossiers with blank frozen bounds is propagated separately. Citations rise from 62 to 69; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: two dossiers, 19 claims, 2 unknowns and 69 citations. Opening strengths, the untraced white-flag order and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
