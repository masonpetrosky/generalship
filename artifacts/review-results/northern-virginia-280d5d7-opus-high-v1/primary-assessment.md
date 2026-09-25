# Primary assessment: Northern Virginia Campaign

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`280d5d7dade3c49a82c45abc14f53f214b984ad3`. Its SHA-256 is
`9a9ae65a23db0d588d48cf7e868d4f5c5db3d48a8a49e7c2258c79df1956b3c2`. The reviewer ran
as a fresh headless session with the `evidence-reviewer` definition in a detached
worktree of the bundle commit; see [dispatch.json](dispatch.json). It verified all
51 bound input hashes and inspected all six dossiers, 56 claims and 142 citation
occurrences, including 7 null unknowns, six NPS summaries, the Ropes metadata,
title/preface, ten battle passages and Appendix D, and the frozen row sets. It
reported two required findings and six nonblocking notes.

**NV-R1 is accepted and closed by primary verification.** In the retained OCR the
p.18 running header is followed by the close of Chapter I and then the unheaded
Chapter II opening page, before the p.20 header. Both quotes lie on that page, p.19.
Both locators are changed; quotes and claims are unchanged.

**NV-R2 is accepted and closed by primary verification.** Appendix D, p.191, labels
the 7,241 as "The official list of casualties at Manassas Plains, in August, 1862";
only Jackson's 4,387 runs "from the Rappahannock to the Potomac". The exact proposed
value, rationale and added citation are applied, and the memo is corrected. The
conclusion that neither figure is this interval's loss is unchanged.

[correction.json](correction.json) binds the response, both archived dossiers
(`data/evidence/history/VA022.v1.json`, `VA026.v1.json`) and both corrected dossiers;
I checked the `supersedes` links explicitly because the schema-v1 validator does
not. Original packets remain in commit `280d5d7`; the two affected packets are
regenerated. The six nonblocking notes need no claim change.

The reviewer disclosed that it called `generalship.cli.research_packet` in its own
worktree, against the assignment. That rewrote six packets there with byte-identical
content; no repository file changed and all input hashes still matched. The
deviation is recorded, not treated as invalidating the review.

After correction, 82 tests and offline checks pass and `make reproduce` regenerates
the report and receipt. Accept the bounded first pass: six dossiers, 56 claims, 7
unknowns and 143 citations; 10/36 complete groups by presence at that stage. Opening
strengths, exact clocks, casualty reconciliation and original-document verification
remain unresolved. AI review is not historical adjudication, proof of source
independence or feature admission. Zero rows are promoted; the baseline is unchanged
(Brier 0.2768816348133779 versus 0.25).
