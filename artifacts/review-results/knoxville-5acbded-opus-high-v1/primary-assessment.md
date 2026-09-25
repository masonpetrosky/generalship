# Primary assessment: Longstreet's Knoxville Campaign [November-December 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`5acbdedb03e590741cb037238edaa400ad2c83cd`. Its SHA-256 is `4a3cefeee654d3efb866814b75750da033997808c7ee53fd30fab0cbfd05f003`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected all 27 claims and 123 citation occurrences, including the three null unknowns, the NPS pages and all 20 Official Records sections with replays, the page-marker maps and the frozen row sets. It reported eight required findings and seven non-blocking notes.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **KX-01**: accepted; the date is removed and the Lenoir's Station passage cited.
- **KX-02**: accepted with the 1865 'in all, about 500' citation; Ruff's death at the ditch is also cited.
- **KX-03**: accepted; the 12,000 quote now carries its qualifier.
- **KX-04**: accepted; the Chattanooga rumors are removed and the fuller quote is cited.
- **KX-05**: accepted with the Jenkins citation.
- **KX-06**: accepted; the OCR reading 'Grade’s' is reported.
- **KX-07**: accepted; the reasons and timing are restated with three further citations on Law's march and the enemy's retreat.
- **KX-08**: accepted; rationale and memo treat the clocks as possibly different phases.
- **N1**: Burnside's 11 and 12 o'clock readings stay a deferred lead.
- **N2**: fort-ditch-and-wire rationale gives the campaign-boundary caveat.
- **N3**: Parke's full wording restored.
- **N4**: memo notes the p.454 heading.
- **N5**: Shackelford's unselected December 14 dispatch stays a deferred lead.
- **N6**: picket wording made exact.
- **N7**: the Blain's Cross Roads difference stays a deferred lead.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. No source record changes. Citations rise from 123 to 130 (TN023 43, TN025 49, TN026 38); claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: three dossiers, 27 claims, 3 unknowns and 130 citations. Opening strengths, Burnside's two loss sets, the Bean's Station clocks and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
