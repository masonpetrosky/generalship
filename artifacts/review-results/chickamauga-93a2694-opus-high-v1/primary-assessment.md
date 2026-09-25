# Primary assessment: Chickamauga Campaign [August-September 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`93a269449577504ad3818278d7a08883024ab127`. Its SHA-256 is `742ac463ab7afab1f225f08c0edf4c08693f069ed20fd446303b5c530c662a9c`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected all 27 claims and 135 citation occurrences, including the three null unknowns, the three NPS summaries and all four selections in full with replays, the page-marker maps and the frozen row sets. It reported eight required findings and five observations.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **CH-R1**: accepted with the proposed value and Clayton citation.
- **CH-R2**: accepted with the NPS 'two weeks' citation.
- **CH-R3**: accepted; rationale replaced and the Cist 'felling timber' citation added.
- **CH-R4**: accepted; both rationales changed and the October 22 and September 29 citations added.
- **CH-R5**: accepted; both citations added.
- **CH-R6**: accepted; value, three citations and the memo bullet replaced.
- **CH-R7**: accepted; value replaced, the fuller p.223 quote substituted and the p.222 citation added.
- **CH-R8**: accepted; rationale appended with the Wheeler citation.
- **CH-O1**: the boundary note now says the withdrawal after September 20, without uncited dates.
- **CH-O2**: the inherited Cist dependency count would need a metadata_only revision; no claim is affected.
- **CH-O3**: the terrain value now says the selected passage gives no date for the night.
- **CH-O4**: the memo uses the sources' 'or' wording.
- **CH-O5**: no date is assigned to Cist's shelling.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. No source record changes. Citations rise from 135 to 147; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: three dossiers, 27 claims, 3 unknowns and 147 citations. Opening strengths, the McLemore's Cove and Chickamauga command disputes and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
