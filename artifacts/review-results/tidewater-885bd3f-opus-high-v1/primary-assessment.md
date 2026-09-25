# Primary assessment: Longstreet's Tidewater Operations [March-April 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`885bd3f97721982d5e431e2e720a2a93dc492b65`. Its SHA-256 is `b76521a40024b5cd8b3e471a309414cceecf0f9eb1800cf3da830a84619d8ea7`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified all 44 bound input hashes and inspected all four dossiers, 38 claims and 187 citation occurrences, including 4 null unknowns, the four NPS summaries, all four OR XVIII selections in full, parent context at every boundary, and the frozen row sets. It reported five required findings and four optional notes.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **TW-R1**: accepted; NC011 result restates all three grounds of Foster's 'in all probability' judgment with three p.216 citations and notes the undated movements; memo corrected.
- **TW-R2**: accepted; VA031 records French's judgment as conditional (one p.325 citation added) and only Longstreet's indorsement as judging surprise; memo corrected.
- **TW-R3**: accepted in the preferred form; union-works keeps inherited for pre-April 11 Union works with a p.275 citation, and the Confederate siege works move to a new unresolved claim.
- **TW-R4**: accepted; two French citations link the old river work to Hill's Point by sequence, the rationale says so, and the memo states the NPS difference as unestablished.
- **TW-R5**: accepted; NC010 reports Foster's OCR 'I 4' and the scope of his and the footnote's figures; memo corrected.
- **TW-N1**: adopted for Peck's officer count (OCR '0'); French's uncited '10th' is left as is.
- **TW-N4**: adopted; VA030 quotes Peck's 'under the immediate command of General French' and states its ambiguity.
- **TW-N2**: source differences on garrison lists, siege length and the Hill's Point work in progress are not recorded in this pass.
- **TW-N3**: casualty status stays disputed where sources give conflicting counts (NC010, VA031) and supported where only a frozen count and a live zero exist (NC011, VA030).

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. Claims rise from 38 to 39 and citations from 187 to 194; unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: four dossiers, 39 claims, 4 unknowns and 194 citations. Opening strengths, the April 24 dispute, the Hill's Point work's origin and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
