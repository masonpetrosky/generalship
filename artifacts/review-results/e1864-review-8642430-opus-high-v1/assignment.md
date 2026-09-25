# 1864 Eastern small-operation first passes: separate review

Review prepared commit `8642430daf32af81b45aed82da33c819b990556e` against `cd780cb22f42d9ce8f1e830e7f97c0db96b0a713`. Sibling inputs.json binds
59 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 8642430daf32af81b45aed82da33c819b990556e:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/rapidan-1864-first-pass-v1.md` and `docs/research/kilpatrick-dahlgren-1864-first-pass-v1.md` and `docs/research/crook-averell-1864-first-pass-v1.md` and `docs/research/lynchburg-1864-first-pass-v1.md`, the 7 new dossiers (VA045, VA125, VA049, VA109, VA110, VA111, VA064 in
`data/evidence/`) and the new source records in `data/sources.json` (the 30 added at the prepared
commit), with their selections under `data/raw/rapidan-1864-v1/` and `data/raw/kilpatrick-dahlgren-1864-v1/` and `data/raw/crook-averell-1864-v1/` and `data/raw/lynchburg-1864-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are these choices sound: Walkerton (VA125) scoped to the March 2 ambush although the frozen description and commanders (Hampton, Kilpatrick, Dahlgren) cover the whole raid, with the Dahlgren papers given their own disputed objectives claim; each record using three families plus one targeted follow-up (a fourth family), and VA109 dropping a Crook citation to stay within that bound; author groups reused from old one-report groups (Sigel's 1864 dispatches in `sigel-carthage-report`, Breckinridge's in `breckinridge-baton-rouge-1862-report`); indorsements and inclosures kept inside the author's selection with the author field naming the writer, and the cited compiler footnote in Kilpatrick's report; Early's dispatch printed '1861' mapped to a null date; garbled compiled tables read but not selected; the Volume XXXIII parent deduplicated at merge?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/e1864-review-8642430-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
