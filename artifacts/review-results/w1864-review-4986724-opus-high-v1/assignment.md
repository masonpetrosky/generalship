# 1864 Western small-operation first passes: separate review

Review prepared commit `498672483393892b357469264e256bbddd017e09` against `6945fabb749f35bc0bde68ef37122b5192596735`. Sibling inputs.json binds
101 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 498672483393892b357469264e256bbddd017e09:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/north-alabama-1864-first-pass-v1.md` and `docs/research/meridian-1864-first-pass-v1.md` and `docs/research/dalton-1864-first-pass-v1.md` and `docs/research/forrest-west-tennessee-1864-first-pass-v1.md` and `docs/research/forrest-mississippi-1864-first-pass-v1.md` and `docs/research/morgan-kentucky-1864-first-pass-v1.md` and `docs/research/burbridge-1864-first-pass-v1.md` and `docs/research/breckinridge-tennessee-1864-first-pass-v1.md` and `docs/research/stoneman-1864-first-pass-v1.md` and `docs/research/lake-village-1864-first-pass-v1.md`, the 15 new dossiers (AL002, MS012, MS013, GA006, KY010, TN030, MS014, MS015, TN031, KY011, VA076, TN033, VA081, VA082, AR017 in
`data/evidence/`) and the new source records in `data/sources.json` (the 58 added at the prepared
commit), with their selections under `data/raw/north-alabama-1864-v1/` and `data/raw/meridian-1864-v1/` and `data/raw/dalton-1864-v1/` and `data/raw/forrest-west-tennessee-1864-v1/` and `data/raw/forrest-mississippi-1864-v1/` and `data/raw/morgan-kentucky-1864-v1/` and `data/raw/burbridge-1864-v1/` and `data/raw/breckinridge-tennessee-1864-v1/` and `data/raw/stoneman-1864-v1/` and `data/raw/lake-village-1864-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are these choices sound: TN030's separate disputed `killing-after-assault` claim, recording NPS, Leaming and Forrest each as that source's statement with no characterization or count adopted, and VA076 recording NPS's statement and Gardner's witness report with no Confederate account inspected (check that every quoted statement is attributed to its writer and date, and that nothing is stated in the claim's own voice beyond the sources); AL002 resting on Union accounts and NPS for the Confederate side, with Rawlins counted as a family although he relays Dodge; the three records using a targeted follow-up as a fourth family (MS015 S. D. Lee, TN031 Jordan and Pryor, VA076 Gardner); garbled OCR dates mapped null or mapped with a note, and printed dates that do not fit (Hicks, Jackson) kept and flagged; Johnston's October 20, 1864 report placed in `johnston-atlanta-report` as the same document; Breckinridge's 1864 reports in `breckinridge-baton-rouge-1862-report`?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/w1864-review-4986724-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
