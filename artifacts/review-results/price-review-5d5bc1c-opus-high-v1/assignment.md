# Price's Missouri Expedition, Mobile Bay, Mobile and Wilson's Raid first passes: separate review

Review prepared commit `5d5bc1c2eb9152227a63ea8a92f3850a40bd124f` against `b8d19758f70f04d12cf6c22a5bc4d569af78af03`. Sibling inputs.json binds
81 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 5d5bc1c2eb9152227a63ea8a92f3850a40bd124f:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/price-missouri-first-pass-v1.md` and `docs/research/mobile-bay-first-pass-v1.md` and `docs/research/mobile-first-pass-v1.md` and `docs/research/wilson-raid-first-pass-v1.md`, the 15 new dossiers (MO021, MO022, MO023, MO024, MO025, MO026, MO027, KS003, KS004, MO028, MO029, AL003, AL005, AL006, AL007 in
`data/evidence/`) and the new source records in `data/sources.json` (the 44 added at the prepared
commit), with their selections under `data/raw/price-missouri-v1/` and `data/raw/mobile-bay-v1/` and `data/raw/mobile-v1/` and `data/raw/wilson-raid-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Selections from Britton volume II and OR XXXIX Part 1 were deduplicated at merge to the registered parents (see docs/sources.md); check that each such selection's parent_sha256 matches its parent. Are these choices sound: no Union commander's report for Price's expedition (Britton relies on them); Page's Confederate report at Mobile Bay instead of Granger's; Gibson at Spanish Fort and Andrews at Fort Blakely; Jordan and Pryor at Selma; Price's report date read as 1864 where OCR shows 1861; the Marmiton reading?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/price-review-5d5bc1c-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
