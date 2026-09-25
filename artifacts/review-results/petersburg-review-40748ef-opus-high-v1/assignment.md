# Bermuda Hundred and Richmond-Petersburg first passes: separate review

Review prepared commit `40748efdb258cc0382675ebb0bb77f75ad5c2d4a` against `f22b049`. Sibling inputs.json binds
114 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 40748efdb258cc0382675ebb0bb77f75ad5c2d4a:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/bermuda-hundred-first-pass-v1.md` and `docs/research/petersburg-first-pass-v1.md`, the 24 new dossiers (VA047, VA050, VA051, VA053, VA054, VA098, VA063, VA065, VA113, VA067, VA068, VA069, VA070, VA071, VA072, VA073, VA075, VA074, VA077, VA078, VA079, VA080, VA083, VA084 in
`data/evidence/`) and the new source records in `data/sources.json` (the 70 added at the prepared
commit), with their selections under `data/raw/bermuda-hundred-v1/` and `data/raw/petersburg-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are these choices sound: the Volume XL part of Meade's report kept in the Overland Meade group; one Lee group across three volumes; Humphreys kept as a family for VA079 and VA083, where he was a participant and frozen commander; Butler's telegrams selected but not cited at VA053 to respect the ceiling; null section dates where OCR dates are illegible; the inherited and commander_created tags?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/petersburg-review-40748ef-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
