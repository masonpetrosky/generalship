# Early's Raid and Sheridan's Valley first passes: separate review

Review prepared commit `586811f3d24d6d21fa217e498d22471e94e0beb2` against `1e791f7b8e9da05b030e355815ac0b68c43adf92`. Sibling inputs.json binds
81 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 586811f3d24d6d21fa217e498d22471e94e0beb2:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memos `docs/research/early-raid-first-pass-v1.md` and `docs/research/sheridan-valley-first-pass-v1.md`, the fifteen new dossiers
(MD007, DC001, VA114, VA115, VA116, MD008, WV013, VA117, WV014, WV015, VA118, VA119, VA120, VA121, VA122 in `data/evidence/`)
and the new source records in `data/sources.json` (the 46 added at the prepared commit), with
their selections under `data/raw/early-raid-v1/` and `data/raw/sheridan-valley-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are the choices sound: new
   1864 independence groups for authors registered earlier (Early, Averell, Wallace), the Sheridan
   group relative to the Overland pass's Sheridan selection, the `warofrebellion431unit_0` scan
   with its missing pp.561–562, and the `inherited` tag on Fort Stevens' works?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/valley-review-586811f-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
