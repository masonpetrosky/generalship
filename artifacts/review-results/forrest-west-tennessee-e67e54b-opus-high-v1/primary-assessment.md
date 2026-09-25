# Primary assessment: Forrest's Expedition into West Tennessee

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`e67e54b7d95c880d4fcacbfc4447389eba09c471`. Its SHA-256 is `a88c2a32f9d94e2100fc8297b118794875438af28eabc13fb72b2affbc350c64`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified all 35 bound input hashes and inspected both dossiers, 18 claims and 61 citation occurrences, including 2 null unknowns, both NPS summaries, the Jordan and Pryor metadata, title/preface with Forrest's note and the three Chapter VII passages, and the frozen row sets. It reported three required findings and six advisories.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **FWT-R1**: accepted; Parker's Cross Roads figures restated as the book's arithmetic (1,554; unreproducible printed 1,824), Dunham's 8,000 recorded as pre-battle information, the two-brigade/Fuller difference and Carroll's warning cited; seven citations added, one replaced.
- **FWT-R2**: accepted; the NPS concurrency is attributed to Forrest's view and Jordan and Pryor's night-before raid timing cited; the NPS 'two mounted columns' quote is kept beside the new one, so four citations are added rather than the review's three.
- **FWT-R3**: accepted; the armament claim changed from inherited to unresolved with the proposed rationale.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. Advisories A1 to A6 are not applied. Citations rise from 61 to 72; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: two dossiers, 18 claims, 2 unknowns and 72 citations. Opening strengths, the contested results and casualty reconciliation remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
