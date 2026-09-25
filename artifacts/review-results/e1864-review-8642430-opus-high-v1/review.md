# Separate review: 1864 Eastern small-operation first passes (VA045, VA125, VA049, VA109, VA110, VA111, VA064)

## Reviewer record

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a separate
  subagent started with fresh context. The author's conversation was not an input.
- **Date:** 2026-09-25.
- **Assignment:** `artifacts/review-results/e1864-review-8642430-opus-high-v1/assignment.md`,
  sha256 `7f5b512d50c0f3f47f0c7b74459c152ea27429046b689824b9c6e27fdd56c637` (verified).
- **Input manifest:** `inputs.json`, sha256
  `7dede83fd2ea65f9eea5f36852010affee2a0bfa4b73e31cc103c373dcf96531` (verified).
- **Commits:**
  - prepared commit `8642430daf32af81b45aed82da33c819b990556e`;
  - previous commit `cd780cb22f42d9ce8f1e830e7f97c0db96b0a713`;
  - bundle commit `c7f5799595db240736cc9176f345fd69720615a7`. This worktree's HEAD is the bundle
    commit, whose diff from `8642430` adds only `assignment.md` and `inputs.json`.
- **Input hashes:** all 59 paths in `inputs.json` were hashed from
  `git show 8642430…:<path>` and from the worktree. **All 59 match; there are no mismatches.**
- **`make check`:** run offline in this worktree. It ran 134 tests with result `OK` and exit 0.
  No build, packet or network command was run, and no primary artifact was modified.
- **Status:** this is an AI review. It is not human historical adjudication, proof of source
  independence or feature admission.

## Coverage actually inspected

- **Project documents:** `AGENTS.md`, `docs/evidence-contract.md` (full),
  `docs/methodology.md` §"Research depth and coverage", `docs/cohort-v2.md`, the `docs/sources.md`
  diff for this batch, and all four memos in full.
- **Dossiers:** all 7 in full. That covers all 64 claims and all 484 citation occurrences, each
  read against its cited section.
  - Counts per record, which match the memos: VA045 9/61, VA125 10/91, VA049 9/74, VA109 9/47,
    VA110 9/72, VA111 9/67 and VA064 9/72.
- **Frozen rows:** the frozen Arnold battle, force and commander rows for all 7 records, from
  `data/raw/cwsac_*.csv`.
- **NPS pages:** all 7 normalized NPS text snapshots, read in full.
- **New source records:** all 30 records added to `data/sources.json` at the prepared commit, with
  every field read. No existing record changed.
- **Selections:** all 16 selection snapshots under the four `data/raw/*-1864-v1/` directories,
  read in full, including the Pond Appendix B range.
  - For every selection, a script re-derived each section from the pinned parent. It used the
    recorded `selection_character_ranges`, parent hash, section set and date map, and every section
    reproduced exactly.
  - The Volume XXXIII parent (`or33-illinois-ocr-v1`,
    `data/raw/plymouth-1864-v1/or33-full.txt`) matched its recorded `parent_sha256`.
- **Targeted parent reads:**
  - the Warren report (No. 2) range of the OR XXXIII parent, to check the Caldwell registry note
    that Warren quotes the March 22 report;
  - the raw OCR around the "Wednesday, March 2." footnote in Kilpatrick's range.
- **Registry checks:** prior-registry independence groups for Sigel, Breckinridge, Hunter, Vaughn,
  McCausland, Pollard, Caldwell, Kilpatrick, Averell, Crook, Early, Lee, Humphreys and Pond.
- **Not inspected:** print pages, maps, unselected parent passages beyond those just named, and
  any source outside the repository. No new research was done.

## Outcome: corrections required

The extraction is generally careful. Quotes occur in the cited sections and population and date
scopes are mostly well kept. Unknowns are null, and no figure is adopted as an opening force. Seven
findings require corrections: two provenance and memo errors, one citation-locator
misattribution, one scope misstatement, one uncited proposition, one missed in-family dispute, and
one false boilerplate phrase in two dossiers.

## Required corrections

### E1864-R1: Rapidan and Kilpatrick memos misstate the Volume XXXIII parent and the record count

The Volume XXXIII parent in the registry is `or33-illinois-ocr-v1` with its metadata record
`ia-or33-illinois-metadata-v1` (`data/raw/plymouth-1864-v1/`). It was first registered in commit
`c5bcb38` (Plymouth and Fort Fisher). The prepared commit adds no Volume XXXIII parent or catalog
record. Its 30 new records are 5 for Rapidan, 5 for Kilpatrick-Dahlgren, 8 for Crook-Averell and 12
for Lynchburg, and `docs/sources.md` correctly records the merge deduplication. The two memos still
describe the pre-merge state.

- `docs/research/rapidan-1864-first-pass-v1.md`, Caldwell bullet:
  - replace "from newly pinned *Official Records* Series I, Volume XXXIII (1891 imprint), with
    catalog metadata:"
  - with "from *Official Records* Series I, Volume XXXIII (1891 imprint), using the registered
    parent `or33-illinois-ocr-v1` (first registered for Plymouth):".
- Same memo, source count:
  - replace "This pass adds **seven source records**: the NPS HTML/text pair; the Volume XXXIII
    catalog metadata and full OCR (the parent shared with the Kilpatrick-Dahlgren pass); and the
    Caldwell, Lee and Humphreys selections."
  - with "This pass adds **five source records**: the NPS HTML/text pair and the Caldwell, Lee and
    Humphreys selections. This pass's own copy of Volume XXXIII was byte-identical to the registered
    parent `or33-illinois-ocr-v1` and was deduplicated at merge (see `docs/sources.md`)."
- `docs/research/kilpatrick-dahlgren-1864-first-pass-v1.md`, first replacement:
  - replace "The parent OCR is the one pinned by the Rapidan pass."
  - with "The parent OCR is the registered `or33-illinois-ocr-v1`."
- Same memo, second replacement:
  - replace "The Volume XXXIII parent is counted in the Rapidan pass."
  - with "The Volume XXXIII parent `or33-illinois-ocr-v1` was already registered and is not counted
    in this batch."

### E1864-R2: VA125 cites a compiler footnote under Kilpatrick's March 16 section without saying so

In the raw OCR, "Wednesday, March 2." stands alone at the foot of p.183. It falls between "led to
the city of" and the p.184 running head, and it is the compiler's footnote to the asterisk in
Kilpatrick's March 8 dispatch ("Thursday evening, 11 p. m.*"). Because it falls inside the
`kilpatrick-1864-03-16` character range, the section's author (Kilpatrick) and its mapped date
(1864-03-16) would attach to 1891 compiler text. The claim's value and rationale correctly call it
the compiler's footnote. Only the locator hides this.

- `data/evidence/VA125.json`, claim `recorded-result`: the citation with `source_id`
  `or33-kilpatrick-richmond-raid-selections-v1`, section `kilpatrick-1864-03-16`, quote
  "Wednesday, March 2.".
- Replace its `locator` "p.183 (OCR page markers; not checked against print)" with "p.183
  (compiler's footnote to the March 8 dispatch's 'Thursday evening, 11 p. m.*', printed at the
  foot of p.183 inside the selected range of the March 16 report; compiler text of the 1891
  volume, not Kilpatrick's and not dated March 16; OCR page markers; not checked against print)".
- Registry follow-up (advisory, see A5).

### E1864-R3: VA049 `railroad-and-bridge` has an uncited proposition

The value's sentence "Crook sent Averell toward Saltville." has no citation in the claim, though the
selected Crook report supports it.

- `data/evidence/VA049.json`, claim `railroad-and-bridge`: **add** this citation:
  - `source_id` `or37-1-crook-cloyds-mountain-selections-v1`;
  - `section` `crook-1864-05-23`;
  - quote "I sent Brig. Gen. W. W. Averell, with a mounted force of 2,000 picked men, to move via
    Logan Court-House to Saltville, on the railroad,";
  - locator "p.10 (OCR page markers; not checked against print)".

### E1864-R4: VA049 `casualty-records` scopes McCausland's "nearly 200 prisoners" to Cloyd's

McCausland's May 25 sentence reads: "The enemy lost 600 in killed and wounded at Cloyd's, and we have
taken nearly 200 prisoners from them, and their loss in all will not fall short of 1,000 men." Only
the 600 is placed at Cloyd's. The prisoners and the 1,000 are campaign-wide, and the report
covers the operations through Gap Mountain and the Greenbrier. The current value reads as if the
prisoners were taken at Cloyd's.

- `data/evidence/VA049.json`, claim `casualty-records`, `value`:
  - replace "McCausland says the enemy lost 600 killed and wounded at Cloyd's and nearly 200
    prisoners, and the list inclosed"
  - with "McCausland says the enemy lost 600 killed and wounded at Cloyd's; he adds, without
    placing them at Cloyd's, that the Confederates had taken nearly 200 prisoners from them and that
    the enemy's loss in all would not fall short of 1,000 men; the list inclosed".
- **Add** this citation:
  - `source_id` `or37-1-mccausland-cloyds-mountain-selections-v1`;
  - section `mccausland-1864-05-25`;
  - quote "and we have taken nearly 200 prisoners from them, and their loss in all will not fall
    short of 1,000 men.";
  - locator "p.48 (OCR page markers; not checked against print)".

### E1864-R5: VA109 repeats NPS's claim that Averell burned the New River bridge and omits the contrary sources

The VA109 `recorded-result` value says NPS has Averell burning the New River bridge "the next day".
Two families already cited in VA109 contradict this:

- Pond has Crook burning the bridge after an artillery duel.
- Averell's own report says he reached Dublin on the evening of the 11th, crossed New River on the
  12th, and describes the enemy seeing "the ruins of the railroad and bridges".

The frozen VA049 description repeats the NPS attribution. Adding these citations keeps VA109 within
its three families plus follow-up, and it does not undo the decision to drop Crook.

- `data/evidence/VA109.json`, claim `recorded-result`, `value`:
  - replace "NPS says the Confederates delayed Averell and then withdrew, and that he burned the New
    River bridge the next day."
  - with "NPS says the Confederates delayed Averell and then withdrew, and that he burned the New
    River bridge the next day; Pond instead has Crook take and burn the bridge after an artillery
    duel, and Averell says he reached Dublin on the evening of the 11th and crossed New River on the
    morning of the 12th."
- `rationale`:
  - replace "The bridge burning is expedition context."
  - with "The bridge burning is expedition context; the NPS attribution of it to Averell is
    contradicted by Pond and by Averell's own timing and is not adopted."
- **Add** these citations:
  1. `pond-crook-averell-selections-v1`, section `cloyds-mountain-and-wytheville`, quote "After an
     artillery duel of two hours, with a Union loss of but 11 men, Crook took posses- sion of this
     important structure, and burned it.", locator "p.13 (OCR page markers; not checked against
     print)";
  2. `or37-1-averell-cove-mountain-selections-v1`, section `averell-1864-05-23`, quote "I marched
     to Dublin, where I arrived on the evening of the 11th.", locator "p.42 (OCR page markers; not
     checked against print)";
  3. `or37-1-averell-cove-mountain-selections-v1`, section `averell-1864-05-23`, quote "We crossed
     New River, swollen by recent rains on the morning of the 12th.", locator "p.42 (OCR page
     markers; not checked against print)".

### E1864-R6: VA110 and VA111 strength rationales say "live zeros" where the live pages give non-zero totals

Both live pages give non-zero totals: VA110 "10365 total (US 6275; CS 4090;)" and VA111 "14000
total (US 8500; CS 5500;)". The phrase "live zeros are not measured absence" is boilerplate that
does not apply to these records.

- `data/evidence/VA110.json`, claim `reported-force-scope`, `rationale`:
  - replace "None is adopted as a matched opening strength; live zeros are not measured absence."
  - with "None is adopted as a matched opening strength; the live totals repeat the frozen values
    within one NPS/CWSAC family and are not independent corroboration."
- `data/evidence/VA111.json`, claim `reported-force-scope`, `rationale`: make the same
  replacement.

### E1864-R7: memo and dossier alignment after R5

After R5 is applied, update `docs/research/crook-averell-1864-first-pass-v1.md` so the change is
visible.

- Under "Disputes preserved" → "Cove Mountain", **add** this bullet: "the New River bridge: burned
  by Averell the next day (NPS) against taken and burned by Crook after an artillery duel (Pond),
  with Averell reaching Dublin on the evening of the 11th (Averell);".
- Update the VA109 citation count in the table from 47 to 50. Update the batch total from 121 to
  126 (VA049 +1 from R3 and +1 from R4 raises it from 74 to 76) if the counts are kept in the
  memo.

## Advisories (no correction required)

- **A1 (VA045, clocks and an unselected conflict).** The `command-roles` rationale synchronizes two
  sources' clocks, contrary to the contract's warning against that: "the heaviest fighting, at
  sunset, came after Warren had taken command". Caldwell gives Warren's arrival as between 4 and
  5 p.m., and Humphreys puts the sharp contest "toward sunset". Warren's own report (No. 2), which
  was read and not selected, says "I reached the ford about 3 p. m." It also says Humphreys was
  "present during the enemy's attack at night-fall", which bears on Humphreys' participant status
  in the Rapidan registry note.
  - Suggested rationale: "Caldwell places Warren's arrival between 4 and 5 p.m. and Humphreys
    places the sharp contest toward sunset; read together they suggest the heaviest fighting
    followed Warren's arrival, but the accounts' times are not synchronized."
  - Suggested open question: "Warren's report (read, not selected) gives his arrival at the ford as
    about 3 p.m. and places Humphreys on the field at night-fall."
  - The memo sentence "The sharp fight toward sunset came after that." should be softened the same
    way.
- **A2 (VA125, strength completeness).** Kilpatrick's report and Humphreys both say Mitchell came in
  with about 300 of Dahlgren's party. The cited sources are Kilpatrick ("with upward of 300 officers
  and men belonging to Colonel Dahlgren's party,") and Humphreys ("Captain Mitchell, with 300 of
  Colonel Dahlgren's party,"). Together with 460 or 500, these bound the separated party and could be
  added to `reported-force-scope`.
- **A3 (VA125, wording).** In `rivers-roads-and-ambush-point`, "a position he had chosen about dark"
  resolves an ambiguity in Pollard: "I put them in the position which I had chosen about dark"
  could mean he posted them about dark. Quoting it verbatim would avoid picking a reading.
- **A4 (VA125, phase).** `dahlgren-papers` is tagged `post_outcome`. The correspondence is
  post-outcome, but the papers' content, if authentic, is a pre-engagement objective. `unresolved`
  may describe the claim better. The current tag is conservative, since it keeps the claim out of
  any admission path, and is defensible.
- **A5 (registry, Kilpatrick record).** The `inspection` note of
  `or33-kilpatrick-richmond-raid-selections-v1` does not say that the `kilpatrick-1864-03-16` range
  contains the compiler footnote "Wednesday, March 2." Its section date maps to 1864-03-16. If the
  registry is revised, a `metadata_only` successor could note the footnote in `inspection` and
  `dependency_note`. Registry records are immutable, so this is optional; R2's locator fix is the
  minimum.
- **A6 (registry, Humphreys records).** `humphreys-rapidan-1864-selections-v1` and
  `humphreys-kilpatrick-dahlgren-selections-v1` both carry the Gettysburg-era note "Volume XXVII was
  printed in 1889, after this book". The volume relevant here is XXXIII, with its 1891 imprint. The
  conclusion (no dependence on the printed compilation) still holds. A future `metadata_only`
  revision could name Volume XXXIII.
- **A7 (registry, Pond notes).** Both Pond records carry an identical `dependency_note` ("In these
  passages he quotes Crook's, Sigel's, Hunter's, Vaughn's and Imboden's reports …, and cites
  Lincoln's regimental history"). That is accurate for the two selections together. The Crook-Averell
  selection alone quotes Sigel's and Grant's despatches and Crook's spoken remark, but not Hunter,
  Vaughn, Imboden, Strother or Lincoln.
- **A8 (VA049, completeness).** The live CS figure 538 equals the "538" aggregate of McCausland's
  inclosure, which covers "the battle of Cloyd's Farm … and subsequent operations". Noting this in
  the `casualty-records` rationale would show that the live CS figure may carry the wider scope.
  The frozen VA049 description repeats the NPS attribution of the New River bridge burning to
  Averell (see R5). An open-question line in VA049 would account for it.
- **A9 (VA109, basis).** The strength rationale calls Averell's enemy figures "hearsay (deserters and
  newspapers)". The 5,000 is attributed to rebel newspapers. The 4,500 at Saltville was "ascertained"
  at Tazewell without a stated source; the deserters sentence concerns Confederate knowledge. The
  suggested wording is "the 5,000 is attributed to rebel newspapers and the 4,500 has no stated
  basis".
- **A10 (VA110, attribution).** "From Lincoln's roster study Pond cites … and Imboden's 800
  cavalry…" attaches Imboden's figures to Lincoln's study. Pond cites them as "Imboden, in his
  report". The suggested fix is to split the sentence.
- **A11 (VA111, wording).** "An advanced position in a wood behind defenses of fallen timber and fence
  rails" paraphrases an ambiguous Hunter sentence. Pond ("drove the enemy through the woods to his
  main works") suggests Moor drove the enemy back behind that line. Quoting Hunter verbatim would
  avoid choosing between the two readings.
- **A12 (VA064, consistency).** The `terrain` rationale says Diamond Hill and Quaker church "may name
  the same position". The `recorded-result` value, however, writes "Diamond Hill (Quaker church)"
  as an identity, and the memo does the same. One wording should be used throughout.
- **A13 (families).** The reuse of groups is sound for independence purposes. Sigel's 1864
  dispatches are placed in `sigel-carthage-report` and Breckinridge's in
  `breckinridge-baton-rouge-1862-report`, which are those authors' only prior groups, per the prior
  registry. Same-author material is kept together and not counted as corroboration. The group IDs
  are misleading names only.

## Answers to the assignment's specific questions

- **VA125 scope.** Scoping the record to the March 2 ambush is sound. The record's name, date and
  NPS locality identify the ambush. Raid-wide figures stay labelled and unassigned. The frozen
  commanders are recorded with the explicit note that no inspected passage places Hampton or
  Kilpatrick at Walkerton, and none receives automatic credit. Giving the Dahlgren papers their own
  `disputed` objectives claim is sound: both sides' positions are preserved and the claim is not
  resolved. Its phase tag is covered in A4.
- **Family ceiling.** Every record uses NPS/CWSAC plus two families plus one targeted follow-up.
  This was verified by counting distinct independence groups per dossier: exactly 4 in each. That
  is consistent with the methodology. Dropping the Crook citation from VA109 to stay within the
  bound is sound. R5 uses Pond and Averell, both already in the record, to add the missing bridge
  dispute without breaching it.
- **Author groups.** The reuse is sound; see A13.
- **Indorsements and inclosures.** Keeping them inside the author's selection, with the author
  field naming each writer, is sound and conservative. This covers:
  - Stuart's, Lee's and Seddon's indorsements (Pollard);
  - Seddon's and "J. D."'s indorsements and the Francis inclosure (McCausland), with the inclosure's
    date null;
  - Vaughn's Staunton dispatch printed as an inclosure;
  - Averell's General Orders No. 5 over Rumsey.

  The dossiers attribute cited indorsements to their writers ("Stuart's indorsement credits
  Pollard's dispositions"). The compiler footnote in Kilpatrick's range is the exception, and needs
  R2.
- **Early's "1861" dispatch.** Mapping the date to null is sound and follows the contract. The
  section ID names the inferred date, and the dossier's use of "the 19th" rests on the legible
  day and month. No correction is needed.
- **Garbled compiled tables.** Reading them without selecting them is sound. They are recorded as
  read, not selected, in each record's open questions.
- **Volume XXXIII deduplication.** The deduplication itself is correct. The selections' recorded
  `parent_sha256` equals the registered parent, and every range re-derives exactly. The memos,
  however, were not updated; see R1.

## Finding IDs

Required: E1864-R1, E1864-R2, E1864-R3, E1864-R4, E1864-R5, E1864-R6, E1864-R7.
Advisory: E1864-A1 through E1864-A13.
