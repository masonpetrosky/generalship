# Primary assessment: Goldsboro Expedition

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`9de5b1dd90633345ebc7b2d6e54a520c54718ee1`. Its SHA-256 is `338e28310a529b64e71841bb4b09449bf3adf47edfc66e8f068c7e9ec8f3a177`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified all 40 bound input hashes and inspected all three dossiers, 28 claims and 70 citation occurrences, including 4 null unknowns, three NPS summaries, the OR XVIII metadata and both report selections, and the frozen row sets. It reported five required findings and six nonblocking notes, and disclosed calling the packet function in its own worktree with byte-identical results.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **GB-01**: accepted; Foster's OR rank now cited to his own p.59 signature.
- **GB-02**: accepted; 40 guns and cavalry figure cited, with the OCR 'G40' reading recorded.
- **GB-03**: accepted; Smith's drove-back and county-bridge claims and Foster's 'disastrous failure' cited; NC009 result claim now disputed.
- **GB-04**: accepted; repeated uncited expedition-wide figure removed from Kinston and the quote widened.
- **GB-05**: accepted; the full page-marker reading recorded in the memo.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. Nonblocking notes GB-N1 to GB-N6 need no change. Citations rise from 70 to 75; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: three dossiers, 28 claims, 4 unknowns and 75 citations. Opening strengths, the White Hall and Goldsborough result disputes and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
