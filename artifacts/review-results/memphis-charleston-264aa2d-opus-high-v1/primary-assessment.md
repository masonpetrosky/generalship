# Primary assessment: Operations on the Memphis & Charleston Railroad [November 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`264aa2d675e3533e1c2c581eda914ccabf7111cb`. Its SHA-256 is `3239bbef0e45a03be0ee3f43ff0f813c3c37a75c420a8990d657f546314296f6`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes and inspected all 9 claims and 41 citation occurrences, including the null unknown, the NPS summary and both selections with replays, the page-marker maps and the frozen row sets. It reported five required findings and five notes.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **MC-01**: accepted with the proposed value, quote and rationale.
- **MC-02**: accepted with the Second Iowa citation.
- **MC-03**: accepted with the extended quote.
- **MC-04**: resolved from the primary's own inspection: Hurlbut and Trafton read in full; McCulloch seen only in its opening lines and Slemons only in a search snippet. Memo, open question and a metadata_only v2 source record corrected.
- **MC-05**: accepted with the scouts citation.
- **MC-N1**: section id is a label.
- **MC-N2**: the force-composition conflict is named in the rationale.
- **MC-N3**: the 'full retreat' quote is cited.
- **MC-N4**: the rationale already bars adding the picket losses.
- **MC-N5**: locators are accurate against the parent.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. One metadata_only source revision (MC-04) is recorded in data/sources.json. Citations rise from 41 to 44; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: one dossier, 9 claims, 1 unknown and 44 citations. Opening strength and the Union force composition remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
