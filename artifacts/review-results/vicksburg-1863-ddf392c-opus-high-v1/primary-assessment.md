# Primary assessment: Grant's Operations Against Vicksburg [March-July 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`ddf392c36dc39eb63c2fe3506b35af530e3adbfd`. Its SHA-256 is `a089a34b6ed7d3f67d16dde5477477c163098f13bb16f768f2cc2717e7777361`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected all ten dossiers, 92 claims and 369 citation occurrences, including 10 null unknowns, the ten NPS summaries, the Greene selection and all eleven OR selections, parent context at boundaries, and the frozen row sets. It reported nine required findings and seven non-blocking notes.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **VB63-R1**: accepted; MS004 and MS006 report the OCR readings '12 oT 15' and 'GOO'.
- **VB63-R2**: accepted; MS007 adds Gregg's 50-man squadron and his exact 40, with two citations.
- **VB63-R3**: accepted; MS008 scopes Greene's four brigades and attributes the 'half of Grant's army' inference to Johnston, with two citations.
- **VB63-R4**: accepted; MS011 restores Greene's 'not known', the May 22 scope and Forney's figures, with three citations.
- **VB63-R5**: accepted; LA011 replaces the uncited return-table clause with McCulloch's 184 and notes the difference from 185.
- **VB63-R6**: accepted; LA014 and the memo record Walker's exception for those captured in arms, with one citation.
- **VB63-R7**: accepted; AR008 records Price's delay with Holmes's recorded explanation, with one citation.
- **VB63-R8**: accepted; AR008 restates Holmes's two aims and the surrender condition, with two citations.
- **VB63-R9**: accepted; six metadata_only v2 records correct the OR XXIV Part 2 imprint reading and note the title range; LA011 and LA014 cite the v2 selections.
- **VB63-N1**: component-sum differences recorded in the MS007 and AR008 casualty rationales.
- **VB63-N2**: MS004 now follows Bowen's 'of the artillery'.
- **VB63-N3**: LA014 states that the officers proposed the terms.
- **VB63-N4**: MS011 restores Pemberton's 'so far as I know' and Greene's 'probable'.
- **VB63-N5**: LA011 rationale marks McCulloch's account of Taylor's information as inference.
- **VB63-N6**: the duplicated Greene page lies outside the selection; recorded here only.
- **VB63-N7**: MS005 records Hébert's narrative 'two privates' against his list's corporal and private, with two citations.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. Six metadata_only source revisions (VB63-R9) supersede the OR XXIV Part 2 metadata, OCR and four selection records; raw bytes are unchanged. Citations rise from 369 to 383; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: ten dossiers, 92 claims, 10 unknowns and 383 citations. Opening strengths, the Goodrich's Landing surrender terms and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
