# Primary assessment: Maryland Campaign

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`3796300981ae53e5d94d8b2411af3eef3b53d7fd`. Its SHA-256 is `8cce5f7f02b987754d97a3bda30ee60bb9f45deaf081137a996c3cde702451d0`. The reviewer
ran as a fresh headless session with the `evidence-reviewer` definition in a
detached worktree of the bundle commit; see [dispatch.json](dispatch.json). It
verified all bound input hashes and inspected the three new dossiers, 29 claims and
79 citation occurrences, including 4 null unknowns, three NPS summaries, the Palfrey
metadata, title/preface and four passages, and the frozen row sets. MD003 was
confirmed unchanged and not re-reviewed. It reported four required findings and
three advisory notes.

**All four required findings are accepted and closed by primary verification.**
R1 corrects the new-record count from 12 to 9 (301 to 310 records). R2 restores
Palfrey's attribution of the unknown lost-order hour to others and his hedges. R3
restores "with the possible exception of Couch" and limits "substantially
unopposed" to Franklin's pass. R4 adds exact citations for five stated facts. Every
replacement quote was checked to occur once in its section, and every computed
locator matches the review. Citations rise from 79 to 86; claims, unknowns, phase
tags and outcome values are unchanged.

Advisory A3 is adopted in the dossiers' shared note and the memo: the inspected
text shows Palfrey was formerly colonel of the 20th Massachusetts, not that he served
in this campaign. The registered source record keeps its original dependency note,
now flagged in `docs/sources.md`; changing it would need a versioned metadata
revision. A1 and A2 are not applied.

[correction.json](correction.json) binds the response and all three archived and
corrected dossiers; the `supersedes` links were checked explicitly. Original packets
remain in commit `3796300`; the three packets are regenerated. The same count error
also appears in the Iuka and Corinth memo under separate review; it is not corrected
in this commit, to keep that review's inputs intact.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates
the report and receipt. Accept the bounded first pass for the three new records.
Opening strengths, the surrendering officer, the receipt hour, casualty allocation
and original-document verification remain unresolved. AI review is not historical
adjudication, proof of source independence or feature admission. Zero rows are
promoted; the baseline is unchanged (Brier 0.2768816348133779 versus 0.25).
