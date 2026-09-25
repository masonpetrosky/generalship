# Gulf and Louisiana 1862-63 first passes: separate review

Review prepared commit `be711a9045e1bc71c6a869423d1c0994b9931818` against `badefa6b3c7d8d914a616217be81551cc931864a`. Sibling inputs.json binds
88 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show be711a9045e1bc71c6a869423d1c0994b9931818:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/new-orleans-1862-first-pass-v1.md` and `docs/research/baton-rouge-1862-first-pass-v1.md` and `docs/research/lafourche-1862-first-pass-v1.md` and `docs/research/west-louisiana-1863-first-pass-v1.md` and `docs/research/port-hudson-first-pass-v1.md` and `docs/research/taylor-louisiana-1863-first-pass-v1.md`, the 14 new dossiers (LA001, LA002, LA003, LA004, LA005, LA006, LA007, LA008, LA009, LA010, LA012, LA013, LA015, LA016 in
`data/evidence/`) and the new source records in `data/sources.json` (the 50 added at the prepared
commit), with their selections under `data/raw/new-orleans-1862-v1/` and `data/raw/baton-rouge-1862-v1/` and `data/raw/lafourche-1862-v1/` and `data/raw/west-louisiana-1863-v1/` and `data/raw/port-hudson-v1/` and `data/raw/taylor-louisiana-1863-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are these choices sound: Taylor's 1863 report placed in the existing Taylor group; dependency notes rewritten on the new Irwin and Mahan selection records; LA004 without a history family (two naval-records documents plus NPS); the April 28 surrender recorded only in LA001; Port Hudson siege strengths left as the main gap; the Volume VI parent deduplicated to the 1861 West registration?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/gulf-review-be711a9-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
