# Primary assessment: Fredericksburg Campaign

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`dbcd3da1efa834a36528e5cdfe74ad780349712e`. Its SHA-256 is `a6ae92611e45b9dec814f1937add57a4c7795ef696f12effa8c7da9524faa509`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified all 29 bound input hashes and inspected the dossier's 10 claims and 31 citation occurrences, including 1 null unknown, the NPS summary, the new Palfrey selection and the pinned parent, and the frozen rows. It reported seven required findings and six nonblocking notes.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **FR-01**: accepted; present-for-duty figures attached to the named morning reports, 'is said to have been' restored, three citations changed or added.
- **FR-02**: accepted; unsupported agency claim for the works removed and the wall description cited.
- **FR-03**: accepted; lower bridge 'without much opposition' restored, phase changed from inherited to unresolved.
- **FR-04**: accepted; Palfrey's conditional, his 'not confident' reading and the fog's limited effect restored and cited.
- **FR-05**: accepted; the planned move on Richmond cited.
- **FR-06**: accepted; the Swinton attribution's position just before the retained range recorded, proposal details cited, post_outcome scope explained.
- **FR-07**: accepted; memo page spans corrected to pp.137–138 and p.146.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. Notes FR-N1 (source wording), FR-N2 (Lee's rank conflict, two citations) and FR-N3 (corrupt OCR cell, unexplained 1,000 difference) are adopted; FR-N4 to FR-N6 need no change. An optional v2 selection starting at the Swinton subject is not created. Citations rise from 31 to 44; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: one dossier, 10 claims, 1 unknown and 44 citations. Opening strength, casualty reconciliation and original-document verification remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
