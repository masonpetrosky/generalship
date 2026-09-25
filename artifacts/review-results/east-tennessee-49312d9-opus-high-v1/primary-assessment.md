# Primary assessment: East Tennessee Campaign [September-October 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`49312d9441d898e75b516d4efdcff50d5cab5b58`. Its SHA-256 is `b4cbb8be80d66dbbd1ed48a0e9f79a169a517f5c563f0ea4ae4cd3a1aff59cd7`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected all 19 claims and 80 citation occurrences, including the two null unknowns, both NPS pages, the frozen description column and all four selections in full with replays, the page-marker maps and the frozen row sets. It reported four required findings and four notes.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **ET-R1**: accepted with the proposed value and two October 17 citations.
- **ET-R2**: accepted with the proposed value and the October 11 citation.
- **ET-R3**: accepted with the proposed clause, two citations and the rationale sentence.
- **ET-R4**: accepted; the frozen description and Carter/Giltner citations are added.
- **ET-N1**: TN019 result now says Carter's Depot, with the optional citation.
- **ET-N2**: Foster's 9 o'clock is cited and TN019 command-roles is marked disputed.
- **ET-N3**: the frozen description's assault sentence is added to TN020's result.
- **ET-N4**: the memo mentions the p.601 'f>01' head; the OCR date readings in section date maps are deferred to a later metadata_only revision.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. No source record changes. Citations rise from 80 to 90; claims and unknowns are unchanged; TN019 command-roles becomes disputed.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: two dossiers, 19 claims, 2 unknowns and 90 citations. Opening strengths, the Blountsville fire and clocks, and the Blue Springs assault remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
