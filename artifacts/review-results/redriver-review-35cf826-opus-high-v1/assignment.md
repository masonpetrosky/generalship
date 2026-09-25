# Red River and Camden first passes: separate review

Review prepared commit `35cf826ea8aa773f67b62447fbcfeddd49cef588` against `8c0018e`. Sibling inputs.json binds
66 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 35cf826ea8aa773f67b62447fbcfeddd49cef588:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/red-river-first-pass-v1.md` and `docs/research/camden-first-pass-v1.md`, the 12 new dossiers (LA017, LA018, LA019, LA020, LA021, LA022, LA023, AR012, AR013, AR014, AR015, AR016 in
`data/evidence/`) and the new source records in `data/sources.json` (the 34 added at the prepared
commit), with their selections under `data/raw/red-river-v1/` and `data/raw/camden-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are these choices sound: Irwin (1892) and Britton (1899) as the history families where no Scribner volume exists; Taylor's inclosures (his artillery chief's ordnance list, his printed letters) kept in his family; the Okolona fights (April 2 and 4) kept separate from Elkin's Ferry; atrocity reports at Poison Spring and Marks' Mills recorded as reported and kept apart from combat categories?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/redriver-review-35cf826-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
