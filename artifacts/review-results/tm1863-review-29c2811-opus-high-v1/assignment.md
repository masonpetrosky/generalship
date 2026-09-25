# Trans-Mississippi 1863 first passes: separate review

Review prepared commit `29c28113a3f044892a04f83812e150aa7fd2cdd1` against `0e6063c`. Sibling inputs.json binds
162 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer with
fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 29c28113a3f044892a04f83812e150aa7fd2cdd1:<path>` first.

Read AGENTS.md, `docs/methodology.md` (research depth and coverage), `docs/evidence-contract.md`,
`docs/cohort-v2.md`, the memo(s) `docs/research/prairie-grove-first-pass-v1.md` and `docs/research/marmaduke-1863-first-first-pass-v1.md` and `docs/research/marmaduke-1863-second-first-pass-v1.md` and `docs/research/indian-territory-1863-first-pass-v1.md` and `docs/research/quantrill-1863-first-pass-v1.md` and `docs/research/little-rock-1863-first-pass-v1.md` and `docs/research/indian-territory-north-1863-first-pass-v1.md` and `docs/research/indian-territory-1864-first-pass-v1.md`, the 14 new dossiers (AR004, AR005, MO018, MO019, MO020, AR007, OK006, OK007, AR009, KS001, AR010, AR011, KS002, OK005 in
`data/evidence/`) and the new source records in `data/sources.json` (the 50 added at the prepared
commit), with their selections under `data/raw/indian-territory-1863-v1/` and `data/raw/indian-territory-1864-v1/` and `data/raw/indian-territory-north-1863-v1/` and `data/raw/little-rock-1863-v1/` and `data/raw/marmaduke-1863-first-v1/` and `data/raw/marmaduke-1863-second-v1/` and `data/raw/prairie-grove-v1/` and `data/raw/quantrill-1863-v1/`.

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
   and dependency notes, inspection notes that say what was read)? Are these choices sound: one Official Records report author per record, and for Cape Girardeau, Chalk Bluff, Bayou Fourche and Pine Bluff (no history found) one Union and one Confederate report author instead; indorsements, inclosures, relays and compiled returns by other writers selected as separate sections inside a selection and not counted as extra families; McNeil's May 12 report, Dobbin's report and Pond's report read but not selected (a fourth family); author groups reused (McNeil, Cooper, Hindman, Price) and one new Marmaduke group; the single `commander_created` tag (Clayton's cotton-bale works at Pine Bluff); killings of civilians and surrendered men at Lawrence and Baxter Springs recorded as reported and kept out of ordinary combat casualties; the Britton volume I parent deduplicated at merge (the Prairie Grove memo names the drafting IDs)?

Run `make check` offline. No build, packet or network commands; do not modify primary artifacts.

Write only `artifacts/review-results/tm1863-review-29c2811-opus-high-v1/review.md`; do not edit other files, commit or push. State the scope you actually
inspected. Give required corrections as exact changes (dossier, claim ID, field, replacement text or
added/removed citation with its exact quote), or say there are none; list advisories separately. A
concise review is sufficient. Return the path and outcome. An AI review is not historical
adjudication.
