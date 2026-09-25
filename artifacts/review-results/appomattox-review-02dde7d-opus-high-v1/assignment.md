# Appomattox and Waynesboro first passes: separate review

Review prepared commit `02dde7d6d5dc6b5796059efabddf4b1b47f2d474` against `e72731fca9799260e77d670d691c2d0c20e8f6d9`. Sibling inputs.json binds
75 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 02dde7d6d5dc6b5796059efabddf4b1b47f2d474:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/appomattox-first-pass-v1.md` and `docs/research/sheridan-petersburg-1865-first-pass-v1.md`, the 15 new dossiers (VA085, VA086, VA087, VA088, VA089, VA090, VA124, VA091, VA092, VA093, VA095, VA094, VA096, VA097, VA123 in
`data/evidence/`) and the new source records in `data/sources.json` (the 40 added at the prepared
commit), with their selections under `data/raw/appomattox-v1/` and `data/raw/sheridan-petersburg-1865-v1/`.

Check, for every dossier:

1. **Support.** Does each claim's value say only what its cited quotes support, read in their
   surrounding passage? Flag misattribution (wrong side, wrong date, wrong engagement), figures
   whose date, basis or scope is misstated, and quotes that do not support the sentence.
2. **Completeness within the bound.** Within the selected passages, are important figures,
   disputes or command statements for that engagement missed? Is anything in the frozen rows or
   NPS page unaccounted for?
3. **Rules.** No strength adopted as an opening force; unknowns null; disputes marked; phases
   sensible (`inherited` only where the passage shows pre-existing conditions); no automatic
   commander credit; overlapping or aggregate records not double counted; the three-family ceiling
   respected and families correctly grouped.
4. **Sources.** Are the registry records accurate (edition, dates by section, independence groups
   and dependency notes, inspection notes that say what was read)? Are these choices sound: Humphreys kept as a family where he was a corps commander (labelled participant); author groups reused from the main registry (Lee, Sheridan, Fitzhugh Lee) and new for Johnson, Miles, Gibbon, Ewell; the Humphreys strengths paragraph cited from the Petersburg selection; totals spanning records (High Bridge two days, Five Forks prisoners) kept as context; inferred page locators?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/appomattox-review-02dde7d-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
