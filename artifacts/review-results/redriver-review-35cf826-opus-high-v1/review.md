# Red River and Camden first passes: separate review

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, separate subagent
  started with fresh context. The author's conversation was not an input.
- **Date:** 2026-09-25
- **Prepared commit reviewed:** `35cf826ea8aa773f67b62447fbcfeddd49cef588` (against `8c0018e`)
- **Bundle commit / worktree HEAD:** `d5f01d6522e31af05ee06bf708faec77da085e13`
- **Assignment:** `assignment.md`, sha256 `81ea861dafea25fb3b6680c23e68b9f65f205bedb177f73ab7c19152f57e157c`
- **Input manifest:** `inputs.json`, sha256 `e5c06968f36d24ffca3e0e4dcd25feaaefdf317feaa2db2844a643bcfbc6d88d`
- **Outcome:** **corrections required** (6 required corrections, 10 advisories)

An AI review is a separate analysis. It is not human historical adjudication, proof of source
independence or feature admission. It changes no model input.

## Verification

- **Input hashes.** All 66 manifest paths were hashed from `git show 35cf826…:<path>` and from the
  worktree. All 66 match; there are **no mismatches**. `git diff 35cf826 d5f01d6` touches only the
  two bundle files.
- **`make check`** was run offline in the worktree. It passed with exit 0 (`Ran 134 tests … OK`).
  The worktree stayed clean. No build, packet or network command was run.
- **Counts.** Recomputed from the dossiers, they match both memos:
  - Red River: 63 claims, 7 unknowns and 312 citations.
  - Camden: 45 claims, 5 unknowns and 226 citations.
  - Every dossier covers all seven dimensions and uses only `unresolved`/`post_outcome` phases.
  - Every dossier cites exactly three independence groups:
    - Red River: `nps-cwsac`, `irwin-nineteenth-corps-1892` and `taylor-red-river-1864-reports`;
    - Camden: `nps-cwsac`, `britton-civil-war-border-1899` and `price-camden-1864-report`.

## Scope actually inspected

- **Guidance.** AGENTS.md, `docs/evidence-contract.md`, `docs/methodology.md` (research depth and
  coverage section), `docs/cohort-v2.md`, and both memos in full.
- **Dossiers.** All 12 were read claim by claim: LA017–LA023 and AR012–AR016, with every value,
  rationale, phase and citation.
- **Frozen rows.** The `cwsac_battles`, `cwsac_forces` and `cwsac_commanders` rows for all 12
  records.
- **NPS pages.** All 12 retained NPS text pages, in full.
- **Source records.** All 34 added records in `data/sources.json` (the 20 NPS HTML/text pairs were
  checked at field level), with sections, date maps and inspection notes.
- **Price.** The whole selection (No. 48).
- **Taylor.** In full: the Sub-inclosure 2 and 8 letters, Inclosures D and F, both April 24
  dispatches, and the May 10, second May 14, May 16, 18 and 19 dispatches. The April 18 report
  was read around every cited passage (pp.561–571), including the Mansfield, Pleasant Hill and
  Blair's Landing narrative and the casualty paragraph.
- **Irwin.** Read in context around every cited passage:
  - Fort De Russy, pp.285–288;
  - Sabine Cross-Roads, pp.299–312;
  - Pleasant Hill, pp.313–322;
  - Grand Ecore, pp.323–326;
  - Cane River, pp.328–333;
  - Last Days, pp.344–348;
  - the head of the appendix table.
- **Britton.** The title page and preface in full. Read in context around the cited passages:
  - camden-opening;
  - Okolona and Elkin's Ferry (pp.257–268);
  - Prairie D'Ane and Moscow (pp.271–275);
  - Poison Spring (pp.280–291);
  - Marks' Mills (pp.292–295);
  - Jenkins' Ferry (pp.295–296, 299–310).
- **Parent OR OCR.** Consulted at three points only, to check what lies just outside the
  selections:
  - Taylor Sub-inclosure No. 1 (March 13, to Douglas);
  - the text before the second May 14 dispatch;
  - the text before Inclosure D.
- **Not inspected.**
  - Irwin chapters outside the selection, and the garbled appendix columns beyond their heading.
  - Britton pages outside the cited contexts; some narrative stretches between cited passages
    were skimmed, not read word by word.
  - The HTML originals, beyond the registry fields.
  - Every OR report that the memos list as uninspected.
- **No new research.** No new source family was opened and no network access was used.

## Required corrections

Every replacement quote below was machine-checked to occur verbatim inside the named section.

### RRC-1. LA017 `fort-and-approach`: a sentence without cited or selected support

The value says "Taylor wrote that the river works would resist a boat attack but the land
approach was the dangerous one". That wording comes from Taylor's Sub-inclosure No. 1 (March 13,
to Douglas, OR pp.575–576). That letter was read but not selected, and no citation supports the
sentence. The only Taylor citation (p.561) supports just the later statement about the land
attack.

- **Field `value`: replace with**
  > NPS describes an earthen fortification with a partly iron-plated battery designed to resist
  > the fire of Union ironclads. Irwin says the fort lay twenty-eight miles from the landing by
  > land and nearly seventy by the river, and that the navy broke through a raft nine miles below
  > it. Taylor's April 18 report says the place was taken by a land attack before the gunboats
  > appeared.
- **Field `rationale`: append**
  > Taylor's March 13 letter to Douglas on the land approach (Sub-inclosure No. 1, pp.575–576)
  > was read but not selected, so it is not cited.
- **Citations:** unchanged. Adding the letter would need a new versioned selection, which is
  optional.

### RRC-2. LA018 and LA019 `casualty-records`: the compiler's "Not found" is attributed to Taylor, and the side of the 2,500 is unstated

Taylor's report says a consolidated report of the casualties of the two battles "accompanies this
report". "Not found" is the OR compiler's footnote. The LA018 value instead says "his report says
the consolidated casualty report for the two battles was not found". In context, "the whole loss
to 2,500" is Taylor's own side's loss for the two battles. The LA019 wording "the loss of both
battles" leaves the side unstated, next to Union figures.

- **LA018 `casualty-records`, field `value`.** Replace the sentence "Taylor's April 11 order
  claims twenty-one guns, 2,500 prisoners and 250 wagons; his report says the consolidated
  casualty report for the two battles was not found and that the cavalry would swell the whole
  loss to 2,500." with:
  > Taylor's April 11 order claims twenty-one guns, 2,500 prisoners and 250 wagons. His report
  > says a consolidated report of the Confederate casualties of the two battles accompanies it
  > (the OR compiler's footnote reads "Not found") and that the casualties of the cavalry will
  > swell the whole Confederate loss to 2,500.
- **LA018, added citation:** `or34-1-taylor-red-river-selections-v1`, section `taylor-1864-04-18`,
  locator `p.569 (OCR page markers; not checked against print)`, quote `* Not found.`
- **LA019 `casualty-records`, field `value`.** Replace "and that the cavalry would swell the loss
  of both battles to 2,500" with:
  > and that the casualties of his cavalry would swell the whole Confederate loss for both battles
  > to 2,500
- **Citations:** otherwise unchanged. The existing quote "The casualties of the cavalry will swell
  the whole loss to 2,500." stays.

### RRC-3. LA021 `finding-a-crossing`: the Emory report belongs to a different engagement

Taylor's first April 24 dispatch reports Emory "believed to have fallen in the fight". That fight
is Wharton's pursuit to Cloutierville, a rear-guard action the memo lists as context only. It is
not Monett's Ferry. The value presents the report without saying so.

- **Field `value`.** Replace "and on April 24 reported Emory believed killed, although Irwin says
  Emory directed the forcing of the crossing." with:
  > and on April 24 reported Emory believed to have fallen in Wharton's fight near Cloutierville
  > (a rear-guard action recorded as context, not this record), although Irwin says Emory directed
  > the forcing of the crossing.
- **Added citation:** `or34-1-taylor-red-river-selections-v1`, section
  `taylor-1864-04-24-near-natchitoches`, locator
  `p.579 (OCR page markers; not checked against print)`, quote
  `Yesterday General Wharton pursued the enemy to Clou- tierville, where he attempted to make a stand.`

### RRC-4. LA023 `bayou-swamp-and-flooded-river`: a quote read the wrong way round

The value says "the Union rear had no exit except by the De Glaize road through swamps". The May
18 passage says something else. Confederate raiders cut into the Union wagon train on May 17, and
"The wagons could not be brought off, as there was no exit except by the De Glaize road, on which
was the Sixteenth Corps". The constraint fell on the Confederates trying to remove captured
wagons, on the day before this record.

- **Field `value`.** Replace "and that the Union rear had no exit except by the De Glaize road
  through swamps;" with:
  > and his May 18 dispatch says the wagons cut out near Yellow Bayou on the 17th could not be
  > brought off because the only exit was the De Glaize road, held by the Sixteenth Corps, and
  > that Union stragglers were left scattered through the De Glaize swamps;
- **Existing citation [1]:** keep it. Optionally lengthen its quote to
  `The wagons could not be brought off, as there was no exit except by the De Glaize road, on which was the Sixteenth Corps,`.
- **Added citation:** `or34-1-taylor-red-river-selections-v1`, section `taylor-1864-05-18`,
  locator `p.594 (OCR page markers; not checked against print)`, quote
  `Many were left on this side scat- tered through the De Glaize swamps.`
- **Field `rationale`: append**
  > The May 17 train raid is context; the passage describes ground, not a Union entrapment on
  > May 18.

### RRC-5. AR013 `reported-force-scope`: the reinforcements can be read as going to the wrong side

The value says "Price says Thayer's command joined Steele with 5,500 men and ten guns, that
Gano's brigade of 500 and Tandy Walker's brigade of about 1,000 reinforced him". Grammatically,
"him" is Steele. In Price, Gano's brigade reinforced Marmaduke on the prairie (by April 7), and
Tandy Walker's brigade was Maxey's reinforcement for the April 13 Moscow attack.

- **Field `value`.** Replace that clause with:
  > Price says Thayer's command joined Steele with 5,500 men and ten guns on April 6; on the
  > Confederate side Gano's brigade (500) had reinforced Marmaduke on the prairie, and Tandy
  > Walker's brigade of about 1,000 came up with Maxey before the April 13 Moscow attack;
- **Existing citations [3] and [4]:** optionally lengthen them to
  `I found Brigadier-General Marmaduke, re-enforced by Brigadier-General Gano’s brigade (500 men)`
  and
  `additional re-enforcements from his command, consisting of Tandy Walker’s Choctaw Brigade, about 1,000 strong,`
  (section `price-1864-05`, p.780).

### RRC-6. AR015 `casualty-records`: Drake's statements are credited to Britton, and part of his estimate is dropped

Britton relays the 250 and 800–900 figures explicitly as Colonel Drake's report ("In his report
of the battle, Colonel Drake stated … He also stated that …"). Drake also said "that about one
half of these were Confederates". The value credits the estimate to Britton and says "many of
them Arkansas refugees and Black civilians", which drops the Confederate half.

- **Field `value`.** Replace "Drake's surgeon's count of about 250 Union killed and wounded, and
  an estimate of 800 to 900 dead and wounded on the field, many of them Arkansas refugees and Black
  civilians killed with the train." with:
  > and relays Colonel Drake's report that his chief surgeon counted about 250 of his men killed
  > and wounded, and that an estimated 800 to 900 dead and wounded lay on the field, about one
  > half of them Confederates and a large proportion of the rest Arkansas refugees and Black
  > civilians travelling with the train, whom Drake reported murdered.
- **Added citations:** section `marks-mills`, source `britton-camden-selections-v1`:
  - locator `p.294 (OCR page markers; not checked against print)`, quote
    `In his report of the battle, Colonel Drake stated that his chief surgeon informed him`;
  - locator `p.295 (OCR page markers; not checked against print)`, quote
    `that about one half of these were Confederates,`.
- **Rationale:** keep the existing statement that civilian dead are not military casualties.

## Advisories (not required)

- **RRA-1. LA018/LA019: an omitted figure.** Taylor claims "The third army of the enemy … was
  routed and driven from the field with a loss of at least 10,000 men" (April 18 report, p.569).
  The selected passage contains it, but no dossier records it. It is an interested, unsupported
  claim spanning both days, or the expedition. It could be added to both `casualty-records`
  claims as a two-day claim, neither split nor added. The exact quote is
  `with a loss of at least 10,000 men.` in `taylor-1864-04-18`.
- **RRA-2. LA020 `command-roles`: an unsurfaced timing difference.**
  - Taylor has Green marching "at G p. m. of the 11th". The value's "evening" depends on reading
    the OCR "G" as 6.
  - Irwin says Green "marched from Pleasant Hill early on the morning of the nth".
  - Record both readings, or drop "evening".
- **RRA-3. LA020 `reported-force-scope`: dates of the vessel counts.** Irwin's six gunboats and
  twenty transports describe the ascent from Grand Ecore on April 7. Taylor's "about thirty
  vessels" passed Grand Bayou Landing on the 9th. Neither counts the fleet at Blair's Landing on
  April 12. Stating those dates would prevent a scope misreading.
- **RRA-4. AR012 `casualty-records`: the date's source.** Price gives no date for Shelby's Terre
  Noir attack; he places it after the April 1 advance to Spoonville. "April 2" is Britton's date.
  Suggested wording: "Price says Shelby, attacking the rear at the Terre Noir crossing (April 2
  per Britton), killed near 100 and captured 60 (read 'GO')."
- **RRA-5. AR014 `casualty-records` rationale: one word.** "The killing of wounded and captured
  Black soldiers" goes slightly beyond the cited text. Britton reports wounded soldiers shot and
  bayoneted, and soldiers "separated from their command or cut off from it … shot down without
  mercy". Suggested replacement: "wounded and cut-off Black soldiers".
- **RRA-6. Registry: a section label.** `taylor-1864-05-14-evening` carries no evening marker in
  the printed dispatch. It is the second of two May 14 dispatches; the first reports the
  evacuation "after midday to-day". Its date map (1864-05-14) is correct. At the next metadata-only
  revision, describe it as the second May 14 dispatch. Do not rename the section in place.
- **RRA-7. Registry: author field.** The author field of `or34-1-taylor-red-river-selections-v1`
  reads "Richard Taylor", but Inclosure F is signed "J. L. BRENT, Chief of Art. and Ord., Dist. of
  West Louisiana. Mansfield, April 14, 1864." The dependency note discloses this. A metadata-only
  revision could read "Richard Taylor; Inclosure F by J. L. Brent".
- **RRA-8. Registry: Britton's dependency note.** The note records the diaries, the depositions
  and the Frontier Division's part. The preface also says "Having participated in the operations
  described". The note could label Britton, like Irwin, as partly a participant and an interested
  Union account. It could also record that some chapters appeared in the *National Tribune*.
- **RRA-9. LA018: a tension within Irwin.** Irwin's chapter table (p.311) gives Banks's loss "in
  the battle of Sabine Cross-Roads" alone as 2,186. His appendix return says the War Department
  found it "impossible to separate the losses, for each day". The dossier keeps both. The
  rationale could say that the chapter's one-day split is Irwin's own and is not the War
  Department return.
- **RRA-10. LA017: context not used.** In the parent OCR, Sub-inclosure No. 1 (March 13) is the
  natural target if a later bounded follow-up wants Taylor's pre-assault view of the land
  approach. No follow-up is recommended under the stopping rule.

## Checks against the assignment criteria

- **Support.** Apart from RRC-1 to RRC-6, the cited quotes support their values when read in the
  surrounding passage. The checks included:
  - Taylor's March 13–14 letters and Inclosure F;
  - Irwin's Mansfield and Pleasant Hill strength and loss figures;
  - Kirby Smith's words quoted in Irwin, which are attributed as quoted;
  - Price's figures for all five Camden records;
  - Britton's Poison Spring, Marks' Mills and Jenkins' Ferry figures and their attributions to
    Maxey, Cabell, Fagan and Cunningham.
- **Completeness.** The frozen battle, force and commander rows and the NPS pages are fully
  accounted for in every dossier, including:
  - blank bounds;
  - the Fort DeRussy 350 and Poison Spring 1,100 with no inspected basis;
  - live zeros treated as non-measurements;
  - live-only ranks, not adopted.

  The one material omission within the selections is RRA-1.
- **Rules.**
  - No strength is adopted as an opening force, and the 12 opening strengths are null unknowns.
  - The disputes are marked.
  - No claim is tagged `inherited`. The Mansfield and Monett's Ferry ground was chosen by the
    defenders, and the dates of the works at Fort DeRussy and Prairie D'Ane are unestablished.
  - No automatic commander credit is given.
  - The two-day Mansfield/Pleasant Hill totals are cited in both records but neither split nor
    added.
  - The Okolona and April 2 figures are kept out of the ferry fight's figures.
  - Britton's escort components are not summed.
  - The three-family ceiling holds. Embedded reports (Kirby Smith and Cunningham via Irwin;
    Maxey, Cabell, Fagan and Drake via Britton) are not counted as extra families.
- **Sources.**
  - The registry records match the snapshots: editions, the OCR title check, section date maps
    (Inclosure F 1864-04-14; Price null), selection ranges, independence groups, and inspection
    notes that say what was read and what was not.
  - The four choices in the assignment are sound:
    - **Irwin (1892) and Britton (1899) as the history families** where no Scribner volume
      exists. Both are registered as not independent of the OR families.
    - **Taylor's inclosures kept in his family.** They are printed as inclosures to his report;
      the ordnance list is his staff chief's; the letters are his own. See RRA-7.
    - **The Okolona fights of April 2 and 4 kept apart from Elkin's Ferry.** This matches the
      separate actions in Britton and prevents double counting.
    - **The Poison Spring and Marks' Mills atrocity reports.** They are recorded as reported,
      attributed to the reporting officers via Britton, and kept out of combat categories. Civilian
      dead are excluded from military casualties. See RRA-5 and RRC-6.

## Finding IDs

- **Required:** RRC-1, RRC-2, RRC-3, RRC-4, RRC-5, RRC-6
- **Advisory:** RRA-1, RRA-2, RRA-3, RRA-4, RRA-5, RRA-6, RRA-7, RRA-8, RRA-9, RRA-10

These are proposals. The primary agent should check each against the sources before changing
evidence. Source records and review bundles are immutable; any registry change requires a
versioned metadata-only revision.
