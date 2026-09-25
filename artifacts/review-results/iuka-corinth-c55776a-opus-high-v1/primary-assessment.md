# Primary assessment: Iuka and Corinth Operations

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`c55776a89d1d10d43bba36fefe04512d19b0e1e9`. Its SHA-256 is `2f6418b5195415b74498b3ce67283c6468066833efe69210a401b9363133a7d4`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified all bound input hashes and inspected all three dossiers, 28 claims and 76 citation occurrences, including 3 null unknowns, three NPS summaries, the Greene metadata, title/preface and both passages, and the frozen row sets. It reported eight required findings and six nonblocking notes.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **IC-01**: accepted; MS001 now records the frozen structured US bounds (4,000/4,000) beside the 4,000–4,500 text, with two forces-table citations. Recorded, not corrected.
- **IC-02**: accepted; the unsupported 12:40 p.m. reading is replaced by the OCR '12. -10 p.m.' with an explicit caveat, and Ord's statement is cited.
- **IC-03**: accepted; the guide's fault is attributed to Rosecrans's quoted message and the added causal link removed.
- **IC-04**: accepted; three NPS citations added (Bragg's order, Grant's approval, the Fulton-road escape).
- **IC-05**: accepted; Greene cited for Van Dorn's senior command, and the burial count attributed to Rosecrans's Medical Director with the prisoner and ratio passages cited.
- **IC-06**: accepted; TN007 force claim status changed to disputed.
- **IC-07**: accepted; 'lack of preparation' limited to the later pursuit to Ripley, with citation.
- **IC-08**: accepted; Ord's command and wound cited and the retreat quote completed.
- **PRIMARY-01**: primary-found; the memo and docs/sources.md said 12 new source records, but the registry grew 310 to 319 (9). Not raised by the reviewer.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. Notes IC-N1 (remove 'instead'; one citation added) and IC-N2 (Price's 494 versus printed 496) are adopted; IC-N3 to IC-N6 are not. Citations rise from 76 to 91 (90 from the required findings plus one from IC-N1); claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: three dossiers, 28 claims, 3 unknowns and 91 citations. Opening strengths, casualty reconciliation and message chronology remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
