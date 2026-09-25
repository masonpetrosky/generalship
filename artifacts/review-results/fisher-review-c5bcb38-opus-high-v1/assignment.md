# Plymouth and Fort Fisher first passes: separate review

Review prepared commit `c5bcb389e38b6f79200e347aaa78ddacd9795953` against `376c8624c495ba687181d4f9a179762639c09a5d`. Sibling inputs.json binds
49 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show c5bcb389e38b6f79200e347aaa78ddacd9795953:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/plymouth-1864-first-pass-v1.md` and `docs/research/fort-fisher-1864-first-pass-v1.md` and `docs/research/fort-fisher-wilmington-1865-first-pass-v1.md`, the 5 new dossiers (NC012, NC013, NC014, NC015, NC016 in
`data/evidence/`) and the new source records in `data/sources.json` (the 23 added at the prepared
commit), with their selections under `data/raw/plymouth-1864-v1/` and `data/raw/fort-fisher-1864-v1/` and `data/raw/fort-fisher-wilmington-1865-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are these choices sound: Navies volume 9 (not 11) for Plymouth and Albemarle Sound; Porter's naval reports deferred to respect the three-family ceiling (the Butler-Porter dispute recorded as a gap); author groups reused from the main registry (Bragg, Butler, Schofield); the Volume XLVII parent deduplicated to the Carolinas registration; the frozen Plymouth total equal to the compiled return; Whiting's casualty total not matching its components?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/fisher-review-c5bcb38-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
