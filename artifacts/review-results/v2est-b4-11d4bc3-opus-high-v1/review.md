# Separate review: strength ledger v2, batch 4 of 8 (`v2est-b4-11d4bc3-opus-high-v1`)

**Outcome: corrections required** (B4-R1 to B4-R5). Advisories: B4-A1 to B4-A7.

This is an AI review, a separate analysis. It is not human historical adjudication, independent
corroboration, proof of source independence, feature admission or authorization of any fit.

## Record

| Item | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. Separate subagent started with fresh context; the author's conversation was not an input. |
| Date | 2026-09-25 |
| Prepared commit | `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`, against previous commit `96110cf` (`96110cfad1ea80f4b0462947d9f9b5a98a4e71f5`) |
| Worktree commit | `8ca4b5cbc040e166e982c4a5b675382e7c97ecd8` (bundle commit). `git diff 11d4bc3 HEAD` touches only `artifacts/review-results/*/assignment.md` and `inputs.json` files, so every file read here is identical at the prepared commit. |
| Assignment | `assignment.md`, sha256 `5d7b2f1c47db78c27e034cb2159cd09e5454cacd64fc916728f03e3d0b1b0960` (verified) |
| Input manifest | `inputs.json`, sha256 `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0` (verified) |
| Input hashes | All 25 bound paths were checked against `git show 11d4bc3:<path>`: **25/25 match, with no mismatch**. The worktree copies are identical too. Ledger `data/estimates/side-strength-v2.json` = `e594047072a99c84e5239658df444f2946c945916d744de2ca6a82c8082629e8`. |
| Other files read (not in the manifest; unchanged since the prepared commit) | `docs/strength-estimates.md` `795212ad…64ba3` (equals the ledger's design binding); `docs/feature-admission-reported-strength.md` `0699152d…4c48`; `docs/ledgers-v2.md` `a7e05ddf…9eb1` (equals the ledger's addendum binding); `data/estimates/owner-decision-v2-sources-2026-09-25.json` `28da7610…89e9`; `docs/research/strength-estimates-ledger-v1.md` `9d9f7d30…1926`; `generalship/estimates.py` `af540a92…a32f`; `generalship/estimates_v2.py` `368c5052…943a`; `data/raw/strength-v2/livermore-transcription-v2.txt` `688ea736…103f`; page images `livermore-p109.jpg` `0b8a873b…55ba` and `livermore-p110.jpg` `fadd5712…9638`. |
| Note on the manifest | The assignment names the addendum `docs/ledgers-v2.md`, but the manifest binds `docs/research/ledgers-v2.md`, which is the extraction record. I read both. |
| Checks run offline | `make check`: exit 0, 143 tests OK. `python3 -m generalship estimate-check --ledger data/estimates/side-strength-v2.json`: in_scope 305, out_of_scope 79; grades A/B/C/D = 184/60/114/252; fit-eligible set1/set2/set3 = 61/83/130; post-start exclusions 20; `fitted: false`. No build or packet command was run. |

## Scope actually inspected

I reviewed all 27 assigned engagements, both sides of each: AL002, OK005, MS012, MS013, FL005, GA006,
VA125, LA017–LA023, KY010, TN030, AR012–AR016, NC012, VA049, VA110, VA111, VA064 and AR017.

For each one I read the following:

- every ledger input, including its codes, basis, `loss_timing`, `bound`, `reproduction_of` and note;
- the inventory, the null reasons and the rationale;
- every `strength` claim in the bound dossier, with every citation quote (no batch dossier has typed quantities);
- the frozen CWSAC forces rows and the battle description/strength cells.

For the passages that decide a coding question, I opened the registered source text around the
quote:

- Pond, New Market p.21;
- Price, p.780;
- Britton, Elkin's Ferry pp.264–265;
- Hunter, p.99;
- Thomas, inclosure 4 and 5;
- Irwin: p.292, Cane River pp.329–333 and every Polignac mention;
- McCausland, p.48;
- W. S. Smith, p.259;
- Sherman, p.174;
- Forrest, 15 April to Polk;
- Taylor, 16 May.

**Livermore.** I checked the `livermore-transcription-v2` sections p109 and p110 against the page
images `livermore-p109.jpg` and `livermore-p110.jpg`. Every entered figure and printed bound in FL005
and LA019 matches the image.

Only Olustee and Pleasant Hill in this batch have Livermore entries in the transcription. For the
inventory only (it is never citable), I searched the pinned Livermore OCR (`livermore-full.txt`) for
every batch battle name. It has no other battle entry for these engagements. Its "Fort Pillow 3,847"
belongs to an April 1862 Confederate strength table, and the transcription runs Drewry's Bluff (p113)
→ Cold Harbor (p114) → Petersburg (p115).

**Verification.** I replayed the proposed corrections in memory with the unchanged engine
(`estimate_side`, `estimate_row`, `nested_sets`). No file was modified.

**Not inspected:** the 91 carried-forward v1 entries, other batches, and any source outside the bound
dossiers, frozen CSVs and registered Livermore records. No new source was consulted.

## Required corrections

### B4-R1 — VA110 New Market, Confederate, `cs-imboden-engaged`: a whole-side total is coded as a part

**Passage** (`pond-lynchburg-selections-v1`, p.21; dossier citations 13–15):

> "Imboden, in his report, gives the cavalry at 800, which would make the total of the three arms
> over 5,000. He also puts the infantry actually engaged at 3,440 and the artillery at 350, with 18
> guns, making a total of 4,590 men. … we may, therefore, safely set down the Confederate strength in
> the engagement at from 4,600 to 5,000 men."

**Why the coding is wrong:**

- 3,440 + 350 = 3,790. The printed 4,590 equals 3,440 + 350 + **800**, so the source's own total
  includes the cavalry. It is Imboden's three-arm total as relayed by Pond (own role under extractor
  policy 3), not "infantry and artillery; the 800 cavalry are separate".
- The `partial_scope` code and the lower bound are therefore a mis-reading.
- It is also the only source of the side's `bound_conflict` label, because 4,590 is taken as a lower
  bound above the 4,090 point.

**Exact change:**

- **Input `cs-imboden-engaged`:**
  - `codes`: `[]` (remove `partial_scope`)
  - `bound`: `null`
  - `basis`: `unknown`. "Actually engaged" qualifies only the infantry component, and no basis is
    stated for the cavalry.
  - `class`: `B`
  - `note`: "Imboden (own side, via Pond): infantry actually engaged 3,440, artillery 350 and cavalry
    800, printed total 4,590 (3,440 + 350 + 800); whole side, basis unstated for the total"
- **Input `cs-imboden-cav`**, `note`: "Imboden: the cavalry; a component of the printed 4,590 (cs-imboden-engaged)".
- **Inventory:** replace "Imboden's 3,440 infantry and 350 artillery are the components of the entered
  4,590" with "Imboden's 3,440 infantry, 350 artillery and 800 cavalry are the components of the
  entered 4,590".
- **Rationale**, Confederate clause: "Confederate: the frozen 4,090; Imboden's three-arm 4,590 and
  Pond's 4,600–5,000 enter the range; Sigel's estimate raises the high."

**Replayed result:**

- Confederate: grade A, point 4,090, range 3,890–8,500, basis `reported_engaged`. Labels
  `compiled_dependence`, `derivation_unknown`, `whole_engagement_leakage`; **`bound_conflict` is
  removed**. Sets are unchanged (set1/2/3).
- If the primary keeps `basis: reported_engaged` instead, the input is class A. The point, range and
  labels come out identical: the lower middle of 4,090 and 4,590 is still 4,090.

### B4-R2 — AR012 Elkin's Ferry, Confederate, `cs-price-1200`: a day-only figure is coded as whole-interval

**Passages:**

- `or34-1-price-camden-selections-v1`, p.780 (dossier citation 3, with context): "On April 3, they
  crossed the Little Missouri River at Elkin's Ferry. The next day (April 4) were attacked by Marmaduke
  and driven back some 3 miles. In this affair we had only some 1,200 men actually engaged".
- The dossier's own summary: "only some 1,200 Confederates were actually engaged on April 4".
- The frozen interval is 1864-04-03 to 04-04. The dossier records Confederate fighting at the ford on
  April 3:
  - `britton-camden-selections-v1` p.264: "some of Marmaduke's mounted detachments discovered the
    Federal pickets near the ford";
  - p.265: "capturing sixteen Confederate soldiers", with Drake's line checking Preston's regiment
    that day.

**Why the coding is wrong.** The source limits the figure to one day of a two-day record. Tier-2 §3
item 2 codes that `partial_interval`, which is bound-only under design §3 row 5. This is the same
day-only treatment the extraction record applies to Bentonville. `interval_unresolved` does not fit,
because the passage states the date explicitly.

**Exact change:**

- **Input `cs-price-1200`:**
  - `codes`: `["partial_interval"]`
  - `bound`: `lower`
  - `class`: `bound`
  - `note`: "Price: 'only some 1,200 men actually engaged' in the April 4 attack; the frozen record
    also covers April 3, when Britton describes Confederate skirmishing at the ford"
- **Confederate `null_reason`:** "No whole-interval candidate: Price's 1,200 engaged is limited to the
  April 4 attack, while the frozen record (April 3–4) includes the April 3 skirmishing at the ford
  that Britton describes; recorded as a lower bound (not applied)."
- **Rationale**, second sentence: "Confederate grade D: Price's engaged count covers April 4 only."

**Replayed result:**

- Confederate: grade D.
- US: unchanged (C, 7,500, 5,000–10,000), but `basis_mixed` drops.
- Nested sets `[]`; the row leaves `set3_ABC`.

### B4-R3 — VA064 Lynchburg, Confederate, `cs-hunter-17th`: a June 17 state is coded as the whole interval

**Passage** (`or37-1-hunter-lynchburg-selections-v1`, p.99; dossier citation 10, with the following
sentence of the same report):

> "This force was variously estimated at from 10,000 to 15,000 men, well supplied with artillery …
> During the night the trains on the different railroads were heard running without intermission,
> while repeated cheers and the beating of drums indicated the arrival of large bodies of troops in the
> town".

The dossier also cites:

- Pond (citation 13): "the 17th, brought to the city half of Early's corps";
- Early (citation 14): the attack of the 18th "was repulsed by the part of my command which was up".

**Why the coding is wrong.** The figure is the force of June 17 before arrivals that the same report
describes, and the frozen interval runs to June 18. The source limits it to part of the interval, so
the code is `partial_interval` and the input is bound-only. As an opponent figure it also could not
apply as a bound (§4 rule 7).

**Exact change:**

- **Input `cs-hunter-17th`:**
  - `codes`: `["adversary_or_hearsay_estimate", "partial_interval"]`
  - `bound`: `lower`
  - `class`: `bound`
  - `note`: "Hunter: the force at Lynchburg on the 17th 'variously estimated at from 10,000 to 15,000',
    before the overnight arrivals he reports; limited to June 17 of the June 17–18 record"
- **Confederate `null_reason`:** "No whole-interval candidate: Hunter's 10,000–15,000 describes the
  force of June 17 before the overnight arrivals he reports; the Ewell and Early 20,000 figures are a
  rumor and prisoners' statements of parts, the latter after the start; all recorded as bounds (not
  applied)."
- **Rationale**, second sentence: "Confederate grade D: every figure is an opponent's or hearsay figure
  for part of the force or of the interval."

**Replayed result:**

- Confederate: grade D.
- US: unchanged (C, 18,000, 12,600–23,400), but `basis_mixed` drops.
- Nested sets `[]`; the row leaves `set3_ABC`.

### B4-R4 — GA006 Dalton I, Confederate, `cs-gladden`: the statement's state is after the start, but it is coded as before

**Passage** (`or32-1-thomas-dalton-selections-v1`, inclosure 4; dossier citations 3–4, with context):

> "Says he left Dalton on Saturday last. He states that the rebel losses in the battles we had at
> Buzzard Roost and on the east of Rocky Face Ridge were from 50 to 60 killed and 150 wounded. …
> their force in all was about 30,000 men, and that their forces, which had previously started for
> Mobile, had all returned".

Inclosure 5 dates Buzzard Roost to "February 24 and 25, 1864". Gladden left Dalton after the
fighting of this record, which begins 1864-02-22, and he describes the army after the detached
forces returned.

**Why the coding is wrong.** The ledger note "dated about February 20" is not supported by the
passage. Tier-2 §3 item 2 makes the input `post_engagement_state` (design §3 row 3). The class stays C
with the opponent tag, because row 2 is tested first, but the `post_start_information` label now
applies.

**Exact change:**

- **Input `cs-gladden`:**
  - `codes`: `["adversary_or_hearsay_estimate", "post_engagement_state"]`
  - `note`: "refugee Gladden's statement forwarded by Thomas (hearsay); he reports the Buzzard Roost and
    Rocky Face fighting of February 24–25 and the return of the forces sent toward Mobile, so the state
    is after the frozen start"
- **Rationale:** "No Union count. Confederate only from a refugee's post-start hearsay figure (rule 4);
  Johnston's December returns are earlier and partial."

**Replayed result:**

- Confederate: C, 22,500, 15,000–30,000, with labels `opponent_estimate_point`,
  `post_start_information`, `single_input`, `whole_engagement_leakage`.
- Nested `excluded_post_start_information: true`. The row was already incomplete (US grade D).

### B4-R5 — LA021 Monett's Ferry inventory: an inaccurate reason for not entering a figure

**Passage** (`irwin-red-river-selections-v1`, p.329; dossier citation 8, with context):

> "This left Taylor only the infantry of Polignac, reduced to 2,000 muskets, and the reorganized cavalry
> corps under Wharton … At three o'clock in the afternoon of the 22d, Wharton with Steele's division,
> supported by Polignac, engaged Lucas sharply".

p.330 places "Bee with the brigades of Debray and Terrell, Major with his two brigades … and the
twenty-four guns" on the bluff.

**Why the reason is wrong.** No inspected passage says Polignac "reached the crossing only as the last
Union troops passed". I searched every Polignac mention in the registered Irwin selection.

**Exact change.** Replace the inventory text:

- Old: "Irwin's 'reduced to 2,000 muskets' is Polignac's infantry, which reached the crossing only as
  the last Union troops passed (not the force at the crossing)"
- New: "Irwin's 'reduced to 2,000 muskets' is Polignac's infantry, which Irwin places with Wharton
  against the Union rear on April 22 while Bee and Major held the bluff (not a count of the force at
  the crossing; not entered)"

No estimate changes; the Confederate side stays grade D.

### Combined effect of B4-R1 to B4-R4 (replayed)

| Measure | Before | After |
| --- | --- | --- |
| Side grades A / B / C / D | 184 / 60 / 114 / 252 | 183 / 60 / 113 / 254 |
| Fit-eligible rows, set1 / set2 / set3 | 61 / 83 / 130 | 61 / 83 / 128 |
| Rows excluded as `post_start_information` | 20 | 21 |

The primary should check each finding against its passage before applying it.

## Confirmed without change

The other inputs were checked against their passages. Their printed values, bounds, `printed_text`,
side attribution, role, basis, scope, timing and loss coding agree with the passages and the
extractor policies. In particular:

- **FL005 and LA019 Livermore lines.** They match the page images exactly:
  - 5,115, 5,200;
  - 12,897, 11,994, 347 → 11,647, 1,000, 12,647;
  - 11,000, 4,300, 15,300, 1,000 → 14,300.

  The April 8 deductions are correctly `prior_engagements_only`: LA018 is dated April 8, entirely
  before April 9. The inventory reason (the note 1 "(800)", note 3, "4000 bayonets" + 300) is accurate.
  The unlisted casualty lines and p110 note 2 (459 and 114) are loss figures, not strength figures.
- **KY010, TN030, AR014, VA111, LA017.** The frozen CWSAC/NPS A candidates and their `reproduction_of`
  links are correct.
- **Other own-side counts.** Hicks's 665 (a sum printed by the source), Leaming's "entire garrison …
  some 550 effective men" and Forrest's own 1,500 ("I attacked Fort Pillow … with a part of Bell's and
  McCulloch's brigades, numbering 1,500") are correctly whole-side.
- **Grade D sides.** OK005 CS, MS012 CS, GA006 US, VA125 CS, LA018 both, LA020 both, LA021 CS, LA022 CS,
  LA023 both, AR013 both, AR015 both, AR016 both, NC012 both and AR017 both have accurate reasons. The
  inspected sources hold no missed usable figure.
- **MS013 US.** The frozen 7,000 as `engagement_link_unknown` is supported by the dossier's reading
  and by Smith's "less than 5,000 men instead of full 7,000".

## Advisories (no required change)

- **B4-A1 — LA022, US `us-taylor-est`.** The phrase is "probably 16,000 men on the field, and perhaps
  more". The ledger reads "and perhaps more" as a hedge on a point estimate, which is defensible: it
  is not one of tier-2's "over / nearly / at least" forms. If the primary reads it as a one-sided
  lower bound, the US side becomes grade D.
- **B4-A2 — VA111, Confederate `cs-vaughn` / `cs-pond-vaughn`.** "Went in the fight yesterday" dates
  the figure to June 5 within the June 5–6 record. Unlike AR012, no inspected passage shows fighting
  on June 6 (NPS: Hunter "occupied Staunton on June 6"), so the whole-interval coding is kept. Replayed
  as `partial_interval`, nothing changes. Reading "aggregate … went in the fight" as engaged basis
  would also change no value.
- **B4-A3 — TN030, US `us-nps-sum`.** The note says the New Era's crew is uncounted. That caveat
  applies equally to the frozen 600 and to Leaming's "entire garrison", so treating the NPS garrison
  sum as whole-side is consistent. If the primary holds that design §4 rule 6 requires the crew, the
  sum becomes a lower bound and the replayed US low moves from 530 to 570 (point 600 unchanged).
  `us-nps-white` and `us-nps-usct` carry `bound: null` where the v1 convention for parts is `lower`,
  which has no effect here.
- **B4-A4 — MS013, Confederate `cs-forrest-2500`.** "With 2,500 men" covers the drive over two days
  (February 21–22) against a one-day record. No separate frozen record exists for February 21 (checked
  in `cwsac_battles.csv`), so it is not a composite. Coding it B with basis unknown is reasonable.
- **B4-A5 — AL002, Confederate `cs-desc`.** The frozen description's "about 600 … about 100" equals
  Dodge's same-day dispatch figures. It is not *visibly* an opponent estimate, so B is correct under
  policy 1, but its derivation may rest on the Union estimate; `derivation_unknown` is recorded. On
  the US side, the live NPS cell's reversed sides are coded `scope_unresolved`. No tier-2 code names
  side misattribution exactly, and any row-4 code gives the same class.
- **B4-A6 — AR016, Confederate `cs-britton-10000`.** Britton calls his 1,000 per brigade "a very low
  estimate", so the "nearly 10,000" works as a floor in his reasoning, not a cap. The `bound: upper`
  direction is arguable, with no effect (grade D, no candidate).
- **B4-A7 — Results to note.** These are engine consequences, not coding errors:
  - VA049 CS: the rule 4 point of 4,130 lies above McCausland's own "we never had 3,000 men in all"
    (`bound_conflict`).
  - VA111: the row is excluded from the fits only because Vaughn's June 6 opponent estimate (10,000,
    `post_engagement_state`) raises the US high. This is the v1 engine-review R1 convention.
  - VA110 US: the high of 10,500 comes from NPS's ordered 10,000 (`engagement_link_unknown`).
  - KY010 CS: the high of 6,500 is Hicks's estimate.
  - MS012 US: the point of 20,000 is NPS's February 3 main force for a record with no general
    engagement.

## Finding IDs

Required: B4-R1, B4-R2, B4-R3, B4-R4, B4-R5. Advisory: B4-A1, B4-A2, B4-A3, B4-A4, B4-A5, B4-A6, B4-A7.
