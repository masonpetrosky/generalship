# Primary assessment: Bristoe Campaign [October-November 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`dc77737bbeb20024b5817e9292d6ace5a6a7ddfc`. Its SHA-256 is `b94dabcd80d67a3e1faa6edfcf1d91c5abbd0a2c5e1b43715e5c6512e917eaa5`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected all 45 claims and 190 citation occurrences, including the five null unknowns, the five NPS summaries and all four selections with replays, the page-marker maps and the frozen row sets. It reported four required findings and five advisories.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **BR-R1**: accepted; both p.40 locators and the memo bullet changed.
- **BR-R2**: accepted in all four parts, with the 'loth' and '2£' citations.
- **BR-R3**: accepted; Lomax and Russell attributions with both citations.
- **BR-R4**: accepted; printed components cited and sums marked as computations.
- **BR-A1**: the rationale already separates on-the-day use; the inherited tags stay.
- **BR-A2**: indorsement dates would need a metadata_only revision; no claim relies on them.
- **BR-A3**: Davis's indorsement is quoted in VA040's corps-identification dispute.
- **BR-A4**: Stuart's 'On the next day, October 20' is cited in VA042's result as same-family support.
- **BR-A5**: Russell's brigade totals are recorded as summing to 326 against the printed 336.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. No source record changes. Citations rise from 190 to 197; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: five dossiers, 45 claims, 5 unknowns and 197 citations. Opening strengths, the Buckland date, the Bristoe corps identification and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
