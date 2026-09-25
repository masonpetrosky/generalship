# Primary assessment: Operations about Dandridge [December 1863-January 1864]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`668c58f76fb16476172db6e6200e44209418c619`. Its SHA-256 is `3b35df4ccd09d4b79c9326393ae9d93d57e84f5f1d3eb144de3c5c3f9d82c956`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected all 27 claims and 141 citation occurrences, including the three null unknowns, the NPS summaries and all four selections with replays, the page-marker maps and the frozen row sets. It reported seven required findings and five advisories.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **DAN-R1**: accepted; the estimates are attributed to Elliott, others and Sturgis's January 1 letter.
- **DAN-R2**: accepted with two Longstreet citations and the memo change.
- **DAN-R3**: accepted; value, rationale and memo no longer read the 2,000 as Sturgis's.
- **DAN-R4**: accepted with metadata_only source revision or32-1-longstreet-dandridge-selections-v2; TN028 and TN029 citations retargeted; memo corrected.
- **DAN-R5**: accepted with the two-month citation.
- **DAN-R6**: accepted in the memo.
- **DAN-R7**: accepted in value, rationale and memo.
- **DAN-A1**: the causal 'because' is removed.
- **DAN-A2**: TN029 open-question typo fixed.
- **DAN-A3**: memo loss bullet corrected.
- **DAN-A4**: the 'LOO' footnote is noted in the rationale and Sturgis's 6 p.m. postscript is cited as an intra-source difference.
- **DAN-A5**: captures not counted twice; the Morgan/Armstrong identification dated to the 26th.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. One metadata_only source revision (or32-1-longstreet-dandridge-selections-v2); registry 581 entries / 560 paths. A TN029 open question also changes. Citations rise from 141 to 145 (TN027 53, TN028 43, TN029 49); claims and unknowns are unchanged. TN028 and TN029 list more changed claims because their Longstreet citations were retargeted to v2.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: three dossiers, 27 claims, 3 unknowns and 145 citations. Opening strengths, the Mossy Creek withdrawal, Sturgis's differing loss and capture figures and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
