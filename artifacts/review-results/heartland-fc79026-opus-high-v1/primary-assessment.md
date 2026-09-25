# Primary assessment: Confederate Heartland Offensive

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`fc79026845cde8b8e3544ab460e2b4e3d6d595d1`. Its SHA-256 is
`2a7ae990b649393fcf224536f9e0db2c6947d0a1cc80d901b35b51833ae3a572`. The reviewer ran
as a fresh headless session with the `evidence-reviewer` definition; see
[dispatch.json](dispatch.json). It verified all 48 bound input hashes and inspected
all five dossiers, 54 claims and 155 citation occurrences, including 6 null unknowns,
the five NPS summaries, the Cist metadata, title/preface and five selections, and
the frozen row sets. It reported one required finding, HO-R1, and five nonblocking notes.

**HO-R1 is accepted and closed by primary verification.** I reread Cist's retained
p.68 passage. It reports Wagner's brigade of Wood's division engaged and "the rest
of Crittenden's corps" not engaged, so "the idle corps" overstated the unengaged
population. The correction applies the exact proposed value, rationale and two
appended citations; the claim ID, dimension, phase, status and four existing
citations are unchanged. [correction.json](correction.json) binds both dossier
hashes and the response. The original dossier is preserved byte-for-byte in
`data/evidence/history/KY009.v1.json`, linked by `supersedes`; I checked that link
explicitly because the schema-v1 validator does not. The original packet remains
in commit `fc79026`; the KY009 packet is regenerated. No follow-up reviewer pass is claimed.

HO-N1 to HO-N3 are addressed by memo wording only; the registered Cist source
records are unchanged, since a metadata change would need a versioned revision.
HO-N4 and HO-N5 need no change. The reviewer's out-of-scope note about stale policy
text is addressed in `docs/evidence-contract.md`. The reviewer also noted that the
assignment understated the `inherited` tags (three, not two) and checked all three.

After correction: 82 tests and offline checks pass; `make reproduce` regenerates the
report and receipt. Only KY009 and its packet changed among evidence files;
the other four dossiers, all sources and the 52 protected files are unchanged.
Accept the bounded first pass: 45/127 draft dossiers, 82 without, 9/36 complete
frozen groups by presence, 54 claims, 6 unknowns and 157 citations. Opening
strengths, exact clocks, casualty reconciliation and original-document verification
remain unresolved. AI review is not historical adjudication, proof of source
independence or admission of features. Zero rows are promoted; the baseline is
unchanged (Brier 0.2768816348133779 versus 0.25). Next is the six-record Northern
Virginia Campaign; this batch does not begin it.
