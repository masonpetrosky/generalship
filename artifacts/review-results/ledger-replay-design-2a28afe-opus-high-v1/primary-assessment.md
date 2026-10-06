# Primary assessment: frozen-ledger replay design

Read the complete [Claude Opus 5.5 `high` response](review.md) for prepared commit
`2a28afe5f90d6dc2a377bcf4d549b6657a4d387f`. Its SHA-256 is recorded in
[correction.json](correction.json). The reviewer ran as a fresh headless session
(`10440d1c-0035-465d-ba41-9ac922248e31`) with the `evidence-reviewer` definition in a detached
worktree of bundle commit `19e0d76`; see [dispatch.json](dispatch.json). The parent session's
effort and session variables were removed, so it ran at `high` effort; the run reports only
`claude-opus-5-5`, no subagents and no permission denials. It verified all 35 bound input hashes,
read the checkers, the run modules, the CLI and the relevant tests, and ran `make check` (151 tests
OK). It also reproduced the problem and the fix in a temporary mirror outside the repository: with
MS009's correction simulated, all four frozen checkers raised `Dossier binding: MS009`, and through
a view presenting the v1 bytes all four passed, with the repository unchanged. It ran no rating,
evaluation, imputation or build command, so the four run callers were not exercised under a view.

**The design is sound.** The reviewer found no way for a view to present bytes other than the
bound bytes, because the resolver's final condition is a SHA-256 match against the ledger's own
binding. It confirmed that section 3.3 lists every code path that replays a frozen ledger and that
the runs read no dossier after replay.

**All eight required corrections are accepted and applied exactly.** The primary checked each one:
the command checker is bound by nothing (R1); the resolver's errors must fail closed (R2); a live
match counts in conflict detection (R3); the source figures are 1,601 entries, 1,555 distinct files
and 345.2 MB, recomputed by the primary (R4); run 1 reads the estimate-evaluation output, so that
run goes first (R5); the installation updates the evidence contract and records itself in a new
file (R6); the test plan gains the error cases, the live-versus-archive conflict and a simulated
installation (R7); and the design now discloses that views widen what replay accepts (R8).
Anchoring every replay to authorization hashes was considered for R8 and not adopted: replay never
authenticated ledger bytes, and the rating and evaluation runs already anchor them.

Advisories A1, A3, A5 and A6 are adopted; A2 and A4 are not, and A7 needs no action. The design
moves from `45814d76…` to its revised text, bound in [correction.json](correction.json). No ledger,
authorization, bound document, bound code, dossier or model input changes. The design awaits the
owner's acceptance; acceptance would authorize implementation only, not a feature, a frozen-input
change or a run. AI review is not owner acceptance or human adjudication.
