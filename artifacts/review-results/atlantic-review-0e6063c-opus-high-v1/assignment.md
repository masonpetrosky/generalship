# Atlantic coast 1862-65 first passes: separate review

Review prepared commit `0e6063c61be793b103e9ca9b9081f8639ae136df` against `ae1ee84`. Sibling inputs.json binds
107 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 0e6063c61be793b103e9ca9b9081f8639ae136df:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/fort-pulaski-first-pass-v1.md` and `docs/research/charleston-1862-first-pass-v1.md` and `docs/research/tampa-1862-first-pass-v1.md` and `docs/research/st-johns-bluff-first-pass-v1.md` and `docs/research/fort-mcallister-1863-first-pass-v1.md` and `docs/research/charleston-1863-first-pass-v1.md` and `docs/research/hillsboro-1863-first-pass-v1.md` and `docs/research/florida-1864-first-pass-v1.md` and `docs/research/st-marks-1865-first-pass-v1.md`, the 15 new dossiers (GA001, SC002, SC003, FL002, FL003, GA002, SC004, SC005, SC006, SC007, SC008, SC009, FL004, FL005, FL006 in
`data/evidence/`) and the new source records in `data/sources.json` (the 65 added at the prepared
commit), with their selections under `data/raw/charleston-1862-v1/` and `data/raw/charleston-1863-v1/` and `data/raw/florida-1864-v1/` and `data/raw/fort-mcallister-1863-v1/` and `data/raw/fort-pulaski-v1/` and `data/raw/hillsboro-1863-v1/` and `data/raw/st-johns-bluff-v1/` and `data/raw/st-marks-1865-v1/` and `data/raw/tampa-1862-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are these choices sound: author groups reused from the main registry (Gillmore, Beauregard, and Samuel Jones's book placed in `samuel-jones-east-tennessee-reports` because he is the same person, who is also the frozen Confederate commander at Natural Bridge); other authors' transmittals and indorsements (Evans at Simmon's Bluff, Finegan's indorsement on Hopkins, Gillmore's 1865 indorsement disputing Seymour at Olustee) read but not selected to respect the three-family ceiling; the unsigned Confederate Olustee casualty table kept as its own section inside the Finegan selection; section dates set to null where the day is lost in OCR (Drayton, McCrady) or the report has a later continuation (Semmes); Tampa with no Union report after the one targeted follow-up in Navies 17; Natural Bridge with two families because Volume XLIX Part 1 prints no Confederate report; the Volume VI and XLIX Part 1 parents deduplicated at merge?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/atlantic-review-0e6063c-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
