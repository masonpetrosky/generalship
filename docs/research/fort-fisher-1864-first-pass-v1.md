# Expedition Against Fort Fisher (December 1864): bounded first pass

Prepared 2026-09-25 under the [cohort v2](../cohort-v2.md) research order, which lists Fort Fisher
among the 1864–65 main-army campaigns. The single record in **Expedition Against Fort Fisher
[December 1864]** now has a draft dossier: **9 claims, 1 explicit null unknown and 72 citation
occurrences**. All seven dimensions are represented. The dossier is a draft; no features are
admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| NC014 — Fort Fisher | 1864-12-07 to 12-27 | 9 | 1 | 72 | 3 |

Dossier presence is not first-pass acceptance, separate review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. NPS/CWSAC and
the Arnold tables are one family. The live page is headed "Fort Fisher I" with the campaign header
"Expedition Against Fort Fisher" and "December 1864"; its Principal Commanders field lists Porter and
Hoke only, while the frozen rows add Butler.

Two further families, both from the already registered ***Official Records* Series I, Volume XLII,
Part 1** (`or42-1-illinois-ocr-v1`, reused as parent; not re-registered):

- **Butler** (Union): his No. 1 report of December 20 (pp.964–965), telegram of December 27
  (pp.965–966) and report of January 3, 1865 (pp.966–970). The p.967 running head reads "9G7" in
  OCR.
- **Whiting** (Confederate): his No. 9 reports of December 30 (pp.993–997) and December 31, 1864
  (pp.997–998), and the January 1, 1865 letters of Anderson (for Bragg) and Whiting printed as
  addenda (pp.999–1000). In those letters Bragg's adjutant corrects a sentence crediting Hoke with
  a message on the afternoon of the 26th, and Whiting agrees to correct it. The printed report
  already reads "the general commanding" there, the corrected wording.

Read but not selected:

- the report list (pp.963–964);
- Grant's indorsements and January 7 forwarding letter, and the opening of Grant's inclosures
  (pp.970–971);
- Lee's No. 8 heading (a cross-reference only);
- Bragg's General Orders No. 17 of December 29 (p.999);
- Hébert's No. 10 report and its casualty list.

Not inspected: Ames's, Curtis's, Weitzel's and the other Union reports; Lamb's No. 12 and the other
Confederate reports; Porter's naval reports. *Official Records of the Navies* Series I, Volume 11
(`officialrecordso0011unse`; North Atlantic Blockading Squadron, October 28, 1864 to February 1,
1865, 1900 imprint) was located and its title page read, but it was not pinned: Porter would have
been a fourth family, and the three-family ceiling was kept with one Union and one Confederate
participant. No 19th-century history was inspected. No targeted follow-up was made. Stop after this
batch.

### New source records

This pass adds **4 source records**:

- one NPS HTML/text pair (`nps-nc014-v1`, with `nps-nc014-v1-html`);
- two selections from the registered Volume XLII Part 1 parent:
  `or42-1-butler-fort-fisher-selections-v1` and `or42-1-whiting-fort-fisher-selections-v1`.

Groups: Butler joins `butler-bermuda-hundred-dispatches`, his most recent registered group (he also
has `butler-wilsons-wharf-dispatches`); the dependency note says the groups are one author family.
Whiting is new (`whiting-fort-fisher-reports`).

## Decisions and limits

- **Scope.** The January 1865 capture is the separate record NC015 in a separate frozen campaign and
  is not added here. The frozen interval (December 7–27) runs from the embarkation to the return.
- **Opening strengths remain unknown.** The frozen bounds are blank and the live Forces Engaged field
  reads zero. Every figure is recorded with its date, basis and scope, and none is adopted:
  - Butler: about 6,500 effective men of Ames's and Paine's divisions moved on December 7; a brigade
    of 1,200 on the Baltic; from deserters and prisoners, fewer than 400 in the garrison and fewer
    than 1,000 within twenty miles when the army arrived; at least two brigades of Hoke's division
    arrived, and Hoke's division outside the works judged larger than his force.
  - Whiting: 133 regulars and 300 Junior Reserves thrown in by the morning of the 25th; three
    battalions of reserves in all during the weather delay; garrisons "reduced one-half"; over fifty
    ships on the 25th.
- **Disputes preserved** (three claims marked `disputed`: force-scope, result, casualty):
  - NPS says "the Federal assault on the fort had already begun when Hoke approached"; Butler says he
    ordered that no assault be made, after his skirmish line reached within seventy-five yards.
    Whiting calls the land effort feeble.
  - Butler's prisoner counts: about 300 men and 10 officers (December 27); 218 men and 10 officers of
    the Reserves taken by Ames's division; 300 including 12 officers in all (January 3).
  - Casualties: frozen 320; live zero; Butler 12 wounded (December 27) against 1 drowned, 2 killed,
    1 officer captured and 10 wounded (January 3); Whiting 14 wounded on the 24th and 38 on the 25th,
    with a printed "61 in all" against components summing to 52 (a computation).
- **Agreement noted, not adopted as proof.** Butler (from a steamer a few hundred yards off) and
  Whiting (inside the fort) both say the bombardment did the works no material damage.
- **Command roles and ranks.** Frozen ranks are kept. Butler says Porter exploded the powder vessel
  and opened the attack without waiting for him, and that Weitzel judged an assault impossible, an
  opinion that "coincided with my own". Whiting says he did not assume Lamb's command and reported
  as a witness. The addenda credit Kirkland, not Hoke, with reopening communication, and put Hoke's
  arrival at Sugar Loaf at about 8 p.m. (the day is not restated), nearly twelve hours after
  Kirkland ordered that movement. Porter's side of the Butler–Porter dispute is
  not in the inspected families. No listed commander receives automatic sole credit.
- **Tags.** The fort's works predate the expedition, but their effect is not scored; no claim is
  tagged `inherited`. All claims stay `unresolved` or `post_outcome`.
- **Unknowns.** The one null unknown is the opening strength.

No morale/readiness score, probability, causal effect or new commander ranking is introduced. The
cohort, both admission proposals and the baseline are unchanged, with zero promoted rows.

## Validation

- `python3 -m generalship check` passes; every quote occurs in its cited section, and `gs.MISSES` is
  empty.
- `python3 -m unittest discover -s tests` passes (134 tests).

## Separate review pending

No separate review has been run for this pass.
