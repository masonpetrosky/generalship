# Primary assessment: Middle Tennessee Operations [February-April 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`ba8d06850c1ccc671332a76af667a48e4457a0e8`. Its SHA-256 is `741ef4ecf2a940de2dd260c0d67ebb3a7904a42106889a3e805a0bf97d99e3fc`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified all 46 bound input hashes and inspected all five dossiers, 46 claims and 135 citation occurrences, including 7 null unknowns, all five NPS summaries, both new selections in full, and the frozen row sets. It reported four required findings and two recommendations.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **MT-R1**: accepted; TN016 records the May 10 date in the frozen description and identical live page against the frozen April 10 interval, with three citations added.
- **MT-R2**: accepted; TN012 gunboat timing restated from intact words, the cropped lines flagged, and two p.229 quotes added.
- **MT-R3**: accepted; TN015 adds NPS's half-hour sequence and the bridge-stockade refusal, with three citations; status stays disputed.
- **MT-R4**: accepted; the 529 is attributed to Federal accounts with the OCR '7591' noted, and Wharton's delay is Wheeler's explanation; two citations added.
- **MT-N1**: adopted; four clause citations added and the TN012 casualty rationale notes that 'wounded' rests on the cropped 'td'.
- **MT-N2**: the footnote tension is kept as an open question in the memo.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. TN013 and TN016 also receive the blank-bounds unknown-strength rationale propagated from VB-R1. Citations rise from 135 to 149; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: five dossiers, 46 claims, 7 unknowns and 149 citations. Opening strengths, the Dover gunboat and Brentwood surrender disputes, Franklin's date and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
