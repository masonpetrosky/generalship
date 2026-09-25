# Trans-Mississippi 1862 first passes: separate review

Review prepared commit `3d36bfe394ead1264b329d1d8b5b35ed794086f0` against `0019009548110f6535c69deeb6ef9c3f7306d0db`. Sibling inputs.json binds
80 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 3d36bfe394ead1264b329d1d8b5b35ed794086f0:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/new-mexico-1862-first-pass-v1.md` and `docs/research/pea-ridge-first-pass-v1.md` and `docs/research/white-river-1862-first-pass-v1.md` and `docs/research/cache-river-1862-first-pass-v1.md` and `docs/research/boston-mountains-1862-first-pass-v1.md`, the 11 new dossiers (NM001, NM002, AR001, AR002, AR003, MO013, MO014, MO015, MO016, OK004, MO017 in
`data/evidence/`) and the new source records in `data/sources.json` (the 46 added at the prepared
commit), with their selections under `data/raw/new-mexico-1862-v1/` and `data/raw/pea-ridge-v1/` and `data/raw/white-river-1862-v1/` and `data/raw/cache-river-1862-v1/` and `data/raw/boston-mountains-1862-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are these choices sound: the single targeted follow-up used as a fourth family at Glorieta (Chivington) and Saint Charles (Hindman's 1863 report); author groups reused from the main registry (Canby, Hindman, Britton); compiled casualty returns kept inside commanders' selections and labelled as the compiler's work; Kirksville with two families; frozen Union strength bounds equal to casualty figures at Independence and Clark's Mill recorded as possible import errors; the Volume VIII and Britton I parents deduplicated at merge?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/tm1862-review-3d36bfe-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
