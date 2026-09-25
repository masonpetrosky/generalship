# Frontier and Texas coast first passes: separate review

Review prepared commit `d57de7e5a8fd26540f132c1aa845ca711d66fc0f` against `c7f5799595db240736cc9176f345fd69720615a7`. Sibling inputs.json binds
107 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show d57de7e5a8fd26540f132c1aa845ca711d66fc0f:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/sioux-1862-first-pass-v1.md` and `docs/research/texas-coast-1862-first-pass-v1.md` and `docs/research/galveston-1863-first-pass-v1.md` and `docs/research/cache-valley-1863-first-pass-v1.md` and `docs/research/sioux-dakota-1863-first-pass-v1.md` and `docs/research/texas-coast-1863-first-pass-v1.md` and `docs/research/sully-1864-first-pass-v1.md` and `docs/research/sand-creek-1864-first-pass-v1.md` and `docs/research/brazos-santiago-1865-first-pass-v1.md`, the 14 new dossiers (MN001, MN002, TX001, TX002, TX003, TX005, TX006, ID001, ND001, ND002, ND003, ND004, ND005, CO001 in
`data/evidence/`) and the new source records in `data/sources.json` (the 66 added at the prepared
commit), with their selections under `data/raw/sioux-1862-v1/` and `data/raw/texas-coast-1862-v1/` and `data/raw/galveston-1863-v1/` and `data/raw/cache-valley-1863-v1/` and `data/raw/sioux-dakota-1863-v1/` and `data/raw/texas-coast-1863-v1/` and `data/raw/sully-1864-v1/` and `data/raw/sand-creek-1864-v1/` and `data/raw/brazos-santiago-1865-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are these choices sound: 'massacre', 'battle' and 'victory' at Sand Creek and Bear River recorded as disputed characterizations with both accounts quoted and neither adopted; Inkpaduta (ND001-ND005) and Ford (TX005) resting only on the frozen tables and NPS because no inspected report names them; no Dakota, Shoshone, Cheyenne, Arapaho or Palmito Ranch Confederate account obtained, and whether the memos state that gap and its consequence for the evidence clearly; targeted follow-ups counted as a fourth family, and ND002 reusing McPhaill for casualty scope only; Wright's transmittal inside Connor's selection as a dependent source; the committee report and Smith's testimony from one volume treated as separate families; author groups (Magruder reused; Sibley, Sully and Crocker each one group across campaigns; the Sioux-campaign Sibley kept separate from the New Mexico Sibley although the author strings match); the parents deduplicated at merge (Volumes XIII, XV, XXVI Part 1, Navies 19)?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/frontier-review-d57de7e-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
