# Working on Generalship

Read `README.md`, `docs/methodology.md`, and `docs/roadmap.md` before substantial work.
For evidence changes, also read `docs/evidence-contract.md` and `docs/sources.md`.
`docs/research-log.md` and `docs/source-additions.md` are history: read the entries
your task touches, not the whole log.

- Keep missing values, source disputes, and coverage denominators visible.
- Cite inspected passages and retain source IDs, locators, and SHA-256 hashes.
  Never substitute model recollection for a source.
- Preserve pinned raw inputs; add a versioned source and documented migration
  when changing evidence. Keep cohort changes explicit and reproducible.
- Do not invent morale/readiness scores, causal effects, win probabilities, or
  independent review records. A source-backed claim can still be historically wrong.
- Preserve the distinction between predictive residuals, tactical effects, and
  campaign contribution. Commander-created advantages may be mediators.
- No automatic attribution to every listed commander. No battle/campaign double counting.
- Draft dossiers do not modify model inputs. Implement a reviewed feature-admission
  contract before adding enriched predictors.
- Tests/builds run offline with Python 3.11+ and the standard library. Keep runtime
  dependencies minimal. Network fetching is explicit; model jobs are not part of tests.
- Run `make check` for logic/data-contract changes. Regenerate with `make reproduce`
  after code or input changes; update the prepared packet if its evidence changed.
- Inspect the generated report, preserve failing or unimproved results honestly,
  and report exact coverage and remaining limits. Never validate by reputation.
- Keep `README.md` a short public overview and `docs/roadmap.md` to the current
  priority, open owner decisions and milestone status. Record per-batch pass
  summaries in `docs/research-log.md` and new sources in `docs/source-additions.md`;
  update the README only when its status, results or instructions change.

## Research scope and stopping rule

- Prioritize comparable first-pass coverage across the current frozen cohort, grouped
  by complete source campaigns. Read the current priority in `docs/roadmap.md`;
  an unresolved question in an old packet is not automatically the next task.
- Default first pass: inspect up to three source families per battle and make at
  most one targeted follow-up for its most consequential gap. Reuse relevant
  campaign sources; copies and reprints are not independent families. This is an
  effort ceiling, not a quota or a substitute for checking every cited passage.
- Address the existing evidence dimensions with supported claims or explicit
  unknowns, record what was checked and deferred, then move to the next battle.
  A draft need not resolve every clock, picket post or source lineage.
- Verify first-pass work by complete campaign before moving on. Fix extraction
  errors, but do not turn each unresolved historical question into another packet.
- Deeper work must identify the concrete admission or methodological decision it
  could change and have a bounded scope, or follow an explicit owner request.
  Shiloh's Agate/overnight provenance follow-ups are parked; retain all evidence
  and unknowns. Coverage, verification and feature admission stay distinct.

## Review policy

- Owner policy, 2026-10-06: there is no separate design or evidence review step.
  The primary agent designs, implements and verifies its own work, and does it
  correctly the first time. Before committing:
  - inspect every cited passage;
  - test new logic and run `make check`;
  - recheck counts, denominators and generated reports;
  - fix what you find.
- This replaces the separate Claude Opus 5.5 `high` reviewer policy of 2026-09-24
  and the earlier GPT-6 Astra `xhigh` policy. Completed reviews remain valid
  records of their own scope.
- Label work as primary-verified. Never describe it as separately or independently
  reviewed, and never create a review record for a review that did not happen.
- Run a separate review only when the owner explicitly asks for one. The
  `evidence-reviewer` agent in `.claude/agents/` remains available for that.
- Verification does not admit features or change frozen model inputs. Keep versioned
  records, review bundles and source records immutable.

## Commit and push cadence

- Push coherent, validated work promptly after a completed change or a small
  related batch of commits. The owner authorizes routine pushes to `origin/main`
  for this repository without another confirmation. Follow an explicit later
  override and retain the evidence and validation requirements above.
- Use normal fast-forward pushes. Verify the remote commit after pushing and
  report any work that remains local.
