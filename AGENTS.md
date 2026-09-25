# Working on Generalship

Read `README.md`, `docs/methodology.md`, and `docs/roadmap.md` before substantial work.
For evidence changes, also read `docs/evidence-contract.md` and `docs/sources.md`.

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

## Research scope and stopping rule

- Prioritize comparable first-pass coverage across all 127 engagements, grouped
  by complete frozen source campaigns. Read the current priority in `docs/roadmap.md`;
  an unresolved question in an old packet is not automatically the next task.
- Default first pass: inspect up to three source families per battle and make at
  most one targeted follow-up for its most consequential gap. Reuse relevant
  campaign sources; copies and reprints are not independent families. This is an
  effort ceiling, not a quota or a substitute for checking every cited passage.
- Address the existing evidence dimensions with supported claims or explicit
  unknowns, record what was checked and deferred, then move to the next battle.
  A draft need not resolve every clock, picket post or source lineage.
- Review first-pass work in campaign batches. Fix extraction errors, but do not
  turn each unresolved historical question into another research/review packet.
- Deeper work must identify the concrete admission or methodological decision it
  could change and have a bounded scope, or follow an explicit owner request.
  Shiloh's Agate/overnight provenance follow-ups are parked; retain all evidence
  and unknowns. Coverage, separate review and feature admission stay distinct.

## Separate reviewer policy

- When a separate review is useful, use a Claude Opus 5.5 subagent with `high`
  reasoning effort: the `evidence-reviewer` agent in `.claude/agents/`
  (`model: claude-opus-5-5`, effort `high`). The owner set this on 2026-09-24,
  replacing the earlier GPT-6 Astra `xhigh` policy; completed Astra reviews remain
  valid records of their own scope. The owner authorizes this workflow for this
  repository; a separate user-managed chat or manual response relay is not
  required. Follow an explicit later override.
- Start the reviewer with fresh context (a new subagent, never a fork of the
  author's conversation) and a bounded, self-contained assignment tied to the
  exact commit, dossier and source hashes. Give it the evidence and review
  criteria, not the author's conversational history.
- The reviewer proposes evidence-backed findings and exact corrections. It must
  state the coverage it actually inspected and write only its assigned review
  outputs. The primary agent checks returned findings before changing evidence.
- Preserve the actual response, reviewer task identity, model, effort, date,
  input hashes and unresolved findings. An AI review is a separate analysis;
  it is not human historical adjudication or proof of source independence.
  It can fulfill the separate-review step within its demonstrated scope; require
  a human or external review only when the owner or a specific evidence requirement
  actually calls for one.
- Reviews do not automatically admit features or change frozen model inputs.
  Keep versioned review bundles and source records immutable. If the requested
  reviewer cannot run, report the concrete blocker rather than claiming review
  completion or silently selecting another model.

## Commit and push cadence

- Push coherent, validated work promptly after a completed change or a small
  related batch of commits. The owner authorizes routine pushes to `origin/main`
  for this repository without another confirmation. Follow an explicit later
  override and retain the evidence, review and validation requirements above.
- Use normal fast-forward pushes. Verify the remote commit after pushing and
  report any work that remains local.
