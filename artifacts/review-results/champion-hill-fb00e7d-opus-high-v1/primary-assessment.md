# Primary assessment: Champion Hill (MS009)

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`fb00e7da75b1a21d10033f2dde39379c45949ce0`. Its SHA-256 is
`cbaa5a96977991773a891c5eaacc19a3182cc699eee703625d3b0ebb422edc8a`. The reviewer ran as a fresh
headless session (`36129a89-f488-4f25-9e2b-8fc04eaf4407`) with the `evidence-reviewer` definition
in a detached worktree of bundle commit `379da81`; see [dispatch.json](dispatch.json). The parent
session's effort and session variables were removed, so it ran at `high` effort; the run reports
only `claude-opus-5-5`, no subagents and no permission denials. It verified all 21 bound input
hashes and inspected the whole dossier (7 claims, 4 citation occurrences, 3 null unknowns) and
every column of the MS009 rows in the three CWSAC tables. It reported five required findings and
five advisory notes.

**All five required findings are accepted and verified, but the corrected dossier is staged, not
installed.** CH-R1 cites the repeated Johnston order received on May 16. CH-R2 rewords
`force-candidate` and cites the two formation names in `forces_text`; the blank strength cells are
recorded in the rationale, since blank cells cannot be quoted. CH-R3 to CH-R5 replace the terrain,
information and responsibility unknowns with `terrain-ridge-line`, `information-left-flank` and
`responsibility-orders`. All 16 quotes occur exactly once in their cells, and "he" in the
countermarch and withdrawal sentences is Pemberton. CH-R4 is staged with one wording change: the
review said Pemberton received warning "after" the sighting, but the source gives only narrative
order and the review's own rationale keeps the sequence unresolved, so the staged value says the
summary "then reports" both. Advisory A1 is adopted (the decision is attributed jointly to
Pemberton and his generals); A3 is recorded below; A2, A4 and A5 need no change. The review's total
of 21 citations is an arithmetic slip: its own increments give 20.

**Why the correction is not installed.** Installing it made five tests fail with "Dossier binding:
MS009". The frozen v1 and v2 strength and command ledgers bind `data/evidence/MS009.json` at
`f1d093f1…`, and their MS009 entries cite the `force-candidate` and `pemberton-order` claims that
the correction changes. The strength ledgers also bind the bytes of their checker code
(`generalship/estimates.py`, plus `estimates_v2.py` for v2), so replay cannot be taught to read an
archived version without breaking those bindings. The owner-authorized rating runs replay these
ledgers before fitting. The owner left the choice to the primary, and keeping every frozen ledger
replayable takes precedence, so `data/evidence/MS009.json` stays byte-identical to v1.

[correction.json](correction.json) binds the response, the unchanged installed dossier and the
staged corrected dossier, [staged-MS009.json](staged-MS009.json) (`42d44bef…`), which passed
`generalship check` while briefly installed. Its `supersedes` link already names
`data/evidence/history/MS009.v1.json` at the v1 hash, so installing it is mechanical once a replay
design allows: archive the live v1 file there, copy the staged file in, and run `make check` and
`make reproduce`. The staged dossier has 7 claims, no unknowns and 20 citations; the installed one
keeps 7 claims, 3 unknowns and 4 citations.

With the correction withdrawn, 151 tests and the offline checks pass and all four frozen ledgers
replay. The separate review of MS009 is complete, but the extraction errors it found remain in the
live dossier until installation. MS009 rests on one retrospective source family (`nps-cwsac`),
while the ten other Vicksburg 1863 records each use three; that is a coverage gap, not a review
correction, and no research packet is opened for it. AI review is not historical adjudication,
proof of source independence or feature admission. Zero rows are promoted, and the baseline is
unchanged (Brier 0.2768816348133779 versus 0.25).
