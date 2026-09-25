# Carolinas Campaign first pass: separate review

Review prepared commit `e83348c4911c949390d89b96262a175eb9053f70` against `a2be26f`. Sibling inputs.json binds
47 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show e83348c4911c949390d89b96262a175eb9053f70:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/carolinas-first-pass-v1.md`, the 5 new dossiers (SC011, NC017, NC018, NC019, NC020 in
`data/evidence/`) and the new source records in `data/sources.json` (the 23 added at the prepared
commit), with their selections under `data/raw/carolinas-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are these choices sound: the compiled Union casualty return used as the single targeted follow-up beyond three families; authors with several registered groups placed in their most recent group (Kilpatrick, Johnston, Bragg, Hardee, Wheeler) and Cox's report in the Cox book group; Harrison registered as a separate author family; the frozen NC020 'Right Wing' label and the NC019 CS 5,400 recorded as frozen-record issues; the Cox report/book disagreement on Upham's regiments?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/carolinas-review-e83348c-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
