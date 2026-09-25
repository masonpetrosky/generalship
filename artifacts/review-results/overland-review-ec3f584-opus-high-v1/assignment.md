# Overland Campaign first pass: separate review

Review prepared commit `ec3f5843b73987db72ef9d23815ec3622063108f` against `d41c3ce`. Sibling inputs.json binds
68 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show ec3f5843b73987db72ef9d23815ec3622063108f:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo `docs/research/overland-first-pass-v1.md`, the eleven new dossiers
(VA046, VA048, VA052, VA055, VA056, VA057, VA058, VA059, VA062, VA066, VA099 in `data/evidence/`)
and the new source records in `data/sources.json` (the 34 added at the prepared commit), with
their selections under `data/raw/overland-v1/`.

Check, for every dossier:

1. **Support.** Does each claim's value say only what its cited quotes support, read in their
   surrounding passage? Flag misattribution (wrong side, wrong date, wrong engagement), figures
   whose date, basis or scope is misstated, and quotes that do not support the sentence.
2. **Completeness within the bound.** Within the selected passages, are important figures,
   disputes or command statements for that engagement missed? Is anything in the frozen rows or
   NPS page unaccounted for?
3. **Rules.** No strength adopted as an opening force; unknowns null; disputes marked; phases
   sensible (`inherited` only where the passage shows pre-existing conditions); no automatic
   commander credit; overlapping records (cavalry raids inside army-battle intervals) not double
   counted; the three-family ceiling respected and families correctly grouped.
4. **Sources.** Are the registry records accurate (edition, dates by section, independence groups
   and dependency notes, inspection notes that say what was read)? Is reusing the Humphreys
   Bristoe group for this book, and counting Butler's relayed telegrams as a family at Wilson's
   Wharf, sound?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/overland-review-ec3f584-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
