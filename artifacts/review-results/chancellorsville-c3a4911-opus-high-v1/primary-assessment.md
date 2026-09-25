# Primary assessment: Chancellorsville Campaign [April-May 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`c3a49116df083863dee0a0ddf7d1947cb2d000ba`. Its SHA-256 is `7d3ab5792bdd9db69b77de31355bb4decfa5313a5e0ff32220d9f6e7fb35b711`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected all three dossiers, 27 claims and 119 citation occurrences, including 3 null unknowns, the three NPS summaries, the Doubleday selection and the three OR XXV Part 1 selections with parent context and page markers, and the frozen row sets. It reported ten required findings and six optional notes.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **CV-R1**: accepted; Hooker-injury locators now p.53, memo corrected, and a metadata_only v2 selection record corrects the inspection note.
- **CV-R2**: accepted; losses-table locators now p.70 and inferred p.71, memo and v2 inspection note corrected.
- **CV-R3**: accepted; the p.25 locator is labelled as inferred and the memo counts three inferred locators.
- **CV-R4**: accepted; value rewritten with four citations and the attributed-judgment rationale.
- **CV-R5**: accepted; Doubleday's own words replace 'apathy', with one citation.
- **CV-R6**: accepted; 'lost' replaces 'leaving', with one citation.
- **CV-R7**: accepted; hearsay attribution and the table's OCR arithmetic recorded.
- **CV-R8**: accepted; Sedgwick's captures qualified and scoped, with one citation.
- **CV-R9**: accepted; the CWSAC/NPS 'left flank' and 'Lt. Gen.' recorded with two citations and not adopted.
- **CV-R10**: accepted; memo strength wording corrected.
- **CV-O1**: the edition's series numeral comes from OCR signature marks, not catalog; not revised in this pass.
- **CV-O2**: VA034 names Griffin's 18th and 21st Mississippi and cites the rest of Barksdale's infantry.
- **CV-O3**: VA034 adds Early's 'in all probability, stragglers'.
- **CV-O4**: VA032 says Fitzhugh Lee's cavalry under Stuart in person.
- **CV-O5**: VA033 cites the left resting on the river.
- **CV-O6**: VA032 calls the frozen bounds imported source-reported forces-engaged figures.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. One metadata_only revision supersedes the Doubleday Chancellorsville selection record; raw bytes are unchanged. Citations rise from 119 to 131; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: three dossiers, 27 claims, 3 unknowns and 131 citations. Opening strengths, engagement-specific casualties for VA033 and VA034 and the losses table's Confederate column remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
