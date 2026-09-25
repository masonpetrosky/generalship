# 1861 Western and Trans-Mississippi first passes: separate review

Review prepared commit `8a97ac1f37f5d260329c682dab15af8443965c40` against `0b4fbb8`. Sibling inputs.json binds
121 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 8a97ac1f37f5d260329c682dab15af8443965c40:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/missouri-1861-first-pass-v1.md` and `docs/research/eastern-kentucky-1861-first-pass-v1.md` and `docs/research/gulf-blockade-1861-first-pass-v1.md` and `docs/research/belmont-1861-first-pass-v1.md` and `docs/research/indian-territory-1861-first-pass-v1.md` and `docs/research/northeast-missouri-1861-first-pass-v1.md`, the 19 new dossiers (MO001, MO002, MO004, MO005, MO006, MO003, MO007, MO008, KY001, KY002, KY003, KY004, FL001, MO009, OK001, OK002, OK003, MO010, MO011 in
`data/evidence/`) and the new source records in `data/sources.json` (the 78 added at the prepared
commit), with their selections under `data/raw/missouri-1861-v1/` and `data/raw/eastern-kentucky-1861-v1/` and `data/raw/gulf-blockade-1861-v1/` and `data/raw/belmont-1861-v1/` and `data/raw/indian-territory-1861-v1/` and `data/raw/northeast-missouri-1861-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are these choices sound: the University of California OR scans (III, IV) after the Illinois identifiers proved to be other series; Britton volume I in the 1891 second edition; author groups (check against the main registry's existing groups for Britton, Price, Grant, Nelson, Prentiss, Williams, Hindman, Sturgis); Turner's report relaying Hubbard counted as its own family; Cooper's report used for Chustenahlah; Grant's Belmont report date as printed; MO011 kept outside its campaign label; KY001 with two families?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/w1861-review-8a97ac1-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
