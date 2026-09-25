# 1861 Eastern first passes: separate review

Review prepared commit `c2984479b0f96581acfcc85fee50cb3b8a221488` against `c5bcb389e38b6f79200e347aaa78ddacd9795953`. Sibling inputs.json binds
119 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show c2984479b0f96581acfcc85fee50cb3b8a221488:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/charleston-1861-first-pass-v1.md` and `docs/research/chesapeake-1861-first-pass-v1.md` and `docs/research/western-virginia-1861-first-pass-v1.md` and `docs/research/manassas-1861-first-pass-v1.md` and `docs/research/carolina-coast-1861-first-pass-v1.md` and `docs/research/northern-virginia-1861-first-pass-v1.md`, the 17 new dossiers (SC001, VA001, VA002, VA003, WV001, WV003, WV004, WV006, WV005, WV007, WV008, WV002, VA004, VA005, NC001, VA006, VA007 in
`data/evidence/`) and the new source records in `data/sources.json` (the 78 added at the prepared
commit), with their selections under `data/raw/charleston-1861-v1/` and `data/raw/chesapeake-1861-v1/` and `data/raw/western-virginia-1861-v1/` and `data/raw/manassas-1861-v1/` and `data/raw/carolina-coast-1861-v1/` and `data/raw/northern-virginia-1861-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are these choices sound: the University of California scans for OR volumes I and II; Navies volumes 4-6 as report sources (Hatteras without army OR volume IV); two report families (one per side) where Nicolay does not cover Big Bethel and Hoke's Run; WV004 relying on Rosecrans relaying Cox and on Wise, who was not present; new per-campaign groups for Beauregard and Stuart (check the main registry's existing groups for these authors and whether they should be reused); undated sections mapped to null; Martin's newspaper-clipping report at Hatteras?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/e1861-review-c298447-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
