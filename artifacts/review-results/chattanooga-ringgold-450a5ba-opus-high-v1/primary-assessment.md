# Primary assessment: Chattanooga-Ringgold Campaign [November 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`450a5ba46975e7f117cbe542d2d87a7d51cd1dc9`. Its SHA-256 is `2ffc4d94462e80bb689a1e8c191390e7b627afc271b2c0bb8760ce3910d79a82`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected all 18 claims and 82 citation occurrences, including both null unknowns, the NPS summaries and all three selections with replays, the page-marker maps and the frozen row sets. It reported five required findings and five advisories.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **R1**: accepted; value, rationale and memo treat 3,951 as an OCR reading and report the Sheridan discrepancy.
- **R2**: accepted; boundary note and memo give the frozen interval and descriptions as the scope basis.
- **R3**: accepted with the Stevenson and Cleburne citations.
- **R4**: accepted; the ridge-works rationale and memo bound the tag at November 23.
- **R5**: accepted; the p.243 locator is labelled inferred.
- **A1**: both GA005 order rationales note Brent's signature and the basis for calling it Bragg's order.
- **A2**: GA005 open question records Bragg's Cleburne and Gist passage, keeping the OCR reading 'Binggold'.
- **A3**: the TN024 casualty rationale notes Howard's command in both Cist figures.
- **A4**: a versioned Cist metadata revision is not needed for this batch.
- **A5**: the live title and date are not adopted and need no claim.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. No source record changes. The TN024 boundary note and a GA005 open question also change. Citations rise from 82 to 84 (TN024 50, GA005 34); claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: two dossiers, 18 claims, 2 unknowns and 84 citations. Opening strengths, the responsibility and Ringgold Gap disputes and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
