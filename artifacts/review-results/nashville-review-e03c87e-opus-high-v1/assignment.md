# Franklin-Nashville and Savannah first passes: separate review

Review prepared commit `e03c87e330a3596b10727abddcc2e447619648f0` against `1191d32433575d224120a6d2aa1df8e381dcecf7`. Sibling inputs.json binds
113 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show e03c87e330a3596b10727abddcc2e447619648f0:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/franklin-nashville-first-pass-v1.md` and `docs/research/savannah-first-pass-v1.md`, the 13 new dossiers (GA023, AL004, TN032, TN034, TN035, TN036, TN037, TN038, GA025, GA026, SC010, GA027, GA028 in
`data/evidence/`) and the new source records in `data/sources.json` (the 51 added at the prepared
commit), with their selections under `data/raw/franklin-nashville-v1/` and `data/raw/savannah-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are these choices sound: reusing existing author groups for French and G. W. Smith; new groups for Rousseau, Hood, Wheeler, Kilpatrick, Hazen, Corse and C. R. Woods (check against groups registered for the same authors by the Atlanta pass); report dates mapped where only the year is garbled in OCR; Hood's strength addenda (by A. P. Mason) and Kilpatrick's provost-marshal statement kept in the report's family; Cox read but not cited where three families already existed?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/nashville-review-e03c87e-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
