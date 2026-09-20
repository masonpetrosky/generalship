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
