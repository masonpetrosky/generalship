# Frozen-ledger replay design: bounded separate review

Review the design `docs/ledger-replay.md` at prepared commit
`2a28afe5f90d6dc2a377bcf4d549b6657a4d387f`. Sibling inputs.json binds 35 paths at that commit.
You are the separate Claude Opus 5.5 `high` reviewer with fresh context. Read AGENTS.md, the
evidence contract, the roadmap's follow-up of 2026-10-06 and its deferred implementation choices,
and the Champion Hill review record. The primary's conversation is not an input. This is a design
review: check the document against the code and records it names. Do not implement anything.

The design lets a corrected dossier that frozen ledgers bind be installed while those ledgers keep
replaying. Each replay would run the unchanged frozen checker against a temporary hard-linked view
of the repository, in which every bound dossier path holds the archived bytes the ledger bound,
reached through the live dossier's hash-verified `supersedes` chain.

Check, with file and line evidence:

- **Facts.** Which files each of the four ledgers binds (dossiers, code, documents, cohorts); that
  `generalship/imputation.py` is bound through the grade E output and run 3's authorization; how
  `safe_path`, `digest` and `verify_sources` behave; and whether the checkers and
  `imputation.impute` write anything.
- **Call graph.** Whether section 3.3 lists every code path that replays a frozen ledger,
  including `run_build`, the CLI commands, `ratings.rate`, `ratings_v3.rate3`,
  `estimate_eval.evaluate_estimates`, the frozen `imputation.impute`, and the tests. Name any it
  misses. Check the claim that the runs read no dossier after replay.
- **Soundness.** Whether the view presents exactly the bound bytes and nothing else changed;
  whether any tampered ledger, dossier or archive could pass replay through a view that would fail
  today; whether fail-closed behaviour, conflict handling, the chain rules (history directory,
  battle ID, repeats) and cleanup on error are right; and the hard-link write risk and copy
  fallback.
- **Plan.** Whether the MS009 installation steps and the reproduction of the authorized runs are
  complete and in the right order, and whether the test plan covers the requirements.
- **Policy.** Consistency with AGENTS.md and the evidence contract: no frozen input or bound file
  changes, no feature admission and no model input change.

Work offline. You may read anything in the repository, run `make check`, and run read-only probes
in a temporary directory outside the repository. Do not run build, packet, rating, evaluation or
imputation commands, and do not modify the repository.

Write only `artifacts/review-results/ledger-replay-design-2a28afe-opus-high-v1/review.md`. Do not
edit other files, commit or push. State the coverage you actually inspected. Give each required
correction as exact replacement text for the design, or say no corrections are required; keep
advisory notes separate. A concise review is sufficient. Return the path and outcome. An AI review
is not owner acceptance and authorizes nothing.
