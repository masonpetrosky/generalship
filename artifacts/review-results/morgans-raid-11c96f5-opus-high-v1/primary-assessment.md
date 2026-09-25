# Primary assessment: Morgan's Raid in Kentucky, Indiana, and Ohio [July 1863]

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`11c96f5d5ac5de7a6f31c3d76d36422283777360`. Its SHA-256 is `79560f26434141354a509f0f721e161a2bc956ceaae30a935f6f9284ee942c94`. The reviewer ran as a fresh headless session
with the `evidence-reviewer` definition in a detached worktree of the bundle commit;
see [dispatch.json](dispatch.json). It verified the bound input hashes against the prepared commit and inspected all 28 claims and 143 citation occurrences, including the three null unknowns, all three NPS summaries and all four selections with replays and boundary context, the page-marker maps and the frozen row sets. It reported five required findings and several optional notes, and confirmed the inherited OR edition issue.

The primary checked every required finding against the retained source text, and
every replacement or added quote was confirmed to occur exactly once in its section
or snapshot before being applied. Dispositions:

- **MR-R1**: accepted; both IN001 values now say a Colonel Morgan with no initials in Duke's passage.
- **MR-R2**: accepted; OH002's boundary note and the memo's scope and strength bullets use Shackelford's sequence without clock labels and note that Duke does not name Way.
- **MR-R3**: accepted; the rationale records Duke's capture during the withdrawal, citing his p.452 capture passage.
- **MR-R4**: accepted; the memo bullet is replaced as proposed.
- **MR-R5**: accepted; OH002's dust clause is scoped to the earlier Blennerhassett march with the proposed citation and rationale, and OH001's rationale scopes Hobson's march totals.
- **MR-O1**: optional: 'militia surgeon' replaced by Dr. D. K. Scriver of the Ohio militia.
- **MR-O2**: optional: the earthwork's garrison and guns are stated as Morgan's information, with three added citations including the 'commanded the ford' clause.
- **MR-O3**: optional note on Duke's 2,460 location: the value now says the passage does not itself state its date.
- **MR-P1**: OH001's boundary note named 'the Hocking', which no inspected source gives; replaced with Shackelford's July 20 action and surrender.
- **MR-META**: the inherited TL-R7 edition text is corrected by three metadata_only v2 selection records reparented to or23-1-illinois-ocr-v2; all three dossiers cite them.

[correction.json](correction.json) binds the response and each archived and
corrected dossier; the `supersedes` links were checked explicitly because the
schema-v1 validator does not. Original packets remain in the prepared commit; the
affected packets are regenerated. Three metadata_only source revisions are recorded in data/sources.json. Citations rise from 143 to 149; claims and unknowns are unchanged.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates the report and receipt. Accept the bounded first pass: three dossiers, 28 claims, 3 unknowns and 149 citations. Opening strengths, the Salineville record's scope and the escape counts remain unresolved. AI review is not historical adjudication, proof of source independence or
feature admission. Zero rows are promoted; the baseline is unchanged (Brier
0.2768816348133779 versus 0.25).
