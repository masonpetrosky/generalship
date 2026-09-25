# Primary assessment: Mine Run Campaign [November-December 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`aa9d89a677415b4474ee3790dd7ed7f2aeb56530`. Its SHA-256 is `852d73f23efb3b31afe11e1d52ac11fdc62228411b5b534804580ba1eeb16cc2`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected all 9 claims and 72 citation occurrences, including the null unknown, the NPS summary and both selections with replays, the page-marker maps and the frozen row sets. It reported four required findings and four advisories.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **MR-R1**: accepted; value, rationale and memo give the prepared-works evidence with four citations, and the p.49 locator is labelled inferred.
- **MR-R2**: accepted; Lee's full sentence is quoted.
- **MR-R3**: accepted; the judgment is attributed to the Third Corps' position with two added citations, the 'three times' quote including the Sixth Corps clause.
- **MR-R4**: accepted; the enlisted sum, return date and scope of Meade's belief are visible, with one added and one replaced citation.
- **MR-A1**: the memo discloses that the p.55 head lies outside the selection.
- **MR-A2**: the dossier does not equate stragglers and prisoners.
- **MR-A3**: Lee's two Rosser accounts are already one family.
- **MR-A4**: the No. 99 abstract remains unselected.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. No source record changes. Citations rise from 72 to 79; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: one dossier, 9 claims, 1 unknown and 79 citations. Opening strength, the Payne's Farm outcome, the Rosser raid figures, Johnson's losses, the works' pre-interval extent and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
