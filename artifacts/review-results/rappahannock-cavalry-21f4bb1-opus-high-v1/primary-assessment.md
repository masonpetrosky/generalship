# Primary assessment: Cavalry Operations along the Rappahannock [March 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`21f4bb1cbca40f987b5b1ad0deb30fad764c4070`. Its SHA-256 is `f9f843040768024113534bf2ce4b82454339c209913f4fa5bee089418f400449`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected the dossier's 9 claims and 60 citation occurrences, including the null unknown, the NPS summary, both OR XXV Part 1 selections in full, parent context at every boundary including Fitz Lee's recapitulation inclosure, the catalog metadata and the frozen row sets. It reported four required findings and three optional notes.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **VA029-R1**: accepted; twelve citations added and four quotes widened across six claims so every value clause is cited.
- **VA029-R2**: accepted; Averell's over-200 estimate is restated with its basis, condition and caveat, with three citations added and the prisoner quote widened.
- **VA029-R3**: accepted; the garbled recapitulation figures are recorded in the casualty rationale without adoption, and the open question and memo now agree with the registry that the inclosure was read but not selected.
- **VA029-R4**: accepted; the conflicting clocks are recorded in the information rationale with three citations; status stays supported.
- **VA029-N1**: adopted as the strength rationale wording.
- **VA029-N2**: the Duffie spelling stays in quotes and Duffié in author prose.
- **VA029-N3**: the 1880 catalog-date wording is a disclosed interpretation; the registry record is immutable and not revised.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. Citations rise from 60 to 78; claims and unknowns are unchanged. The dossier's open question on the recapitulation inclosure is also revised.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: one dossier, 9 claims, 1 unknown and 78 citations. Opening strength, the withdrawal dispute, the morning clocks and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
