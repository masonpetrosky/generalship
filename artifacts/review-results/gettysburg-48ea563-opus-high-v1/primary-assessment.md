# Primary assessment: Gettysburg Campaign [June-July 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`48ea563ad2c79d61eb32e14ac6c457facd86473e`. Its SHA-256 is `cd52fde5aae73dac11ffdad799f7fe89d33ec74725e32a389f0403b1808accd8`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected all 90 claims and 320 citation occurrences, including the ten null unknowns, the Doubleday and Humphreys selections, Lee's and Stuart's selections in full or at every cited passage, all ten NPS summaries with replays and the frozen row sets. It reported eleven required findings and no advisories.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **GB-R1**: accepted; the boundary note in all ten dossiers and the VA036, VA037 and VA038 casualty rationales now scope Stuart's loss total to June 17–22, and the memo bullet is changed.
- **GB-R2**: accepted with value and rationale as proposed; the June 19 attack, the two brigades, Chambliss and Hampton's June 20 arrival are cited.
- **GB-R3**: accepted; MD006's soft-ground, ammunition, reinforcement-report and result values quote the garbled OCR, and the soft-ground quote is extended.
- **GB-R4**: accepted; 'numerous skirmishers' reported as an OCR reading with the full sentence cited, the 200 wagons and Custer's arrival cited, and the footnote locator corrected to p.695.
- **GB-R5**: accepted; Doubleday's detachment remark cited, Stuart's nine and seven regiments stated, and Robertson's 'of which he was cognizant' restored with the extended quote.
- **GB-R6**: accepted; Early's officers and men restored and Doubleday's clearing and withdrawal-order passages cited.
- **GB-R7**: accepted; the untenable-works sentence moved to recorded-result with its retreat clause, the Pughtown-road position cited, and the inherited rationale rewritten; tag kept.
- **GB-R8**: accepted; Lee's statements scoped to Heth's two brigades and his stated risk, with three citations and the rationale addition.
- **GB-R9**: accepted as proposed.
- **GB-R10**: accepted; Lee's 'He succeeded in passing part of his command' cited.
- **GB-R11**: accepted; three metadata_only Humphreys v2 records with the proposed dependency note, citations retargeted, MD004's rationale replaced, and the shared open question in all ten dossiers changed to the publisher's-list wording.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. Three metadata_only source revisions (GB-R11) are recorded in data/sources.json. Citations rise from 320 to 336; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: ten dossiers, 90 claims, 10 unknowns and 336 citations. Opening strengths, Hanover's end state and the frozen casualty figures remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
