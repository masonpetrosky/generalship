# Next war: French Revolutionary and Napoleonic Wars (scoping decided, frame built)

**Owner decisions:**

- **2026-09-25.** After Civil War run 3, the owner asked which war to do next and accepted the
  Napoleonic Wars as the next priority.
- **2026-10-06.** The owner adopted the author's recommendations on the seven scoping decisions
  below: "Sounds good, go ahead" ([record](../data/napoleonic/owner-decision-scoping-2026-10-06.json)).

Nothing here changes the Civil War cohorts, ledgers or runs.

## Why this war

- **Commanders meet repeatedly.** The same commanders appear across many battles and against each
  other, which should connect the rating comparisons. In Civil War run 3, 19 of 94 ranked
  commanders were `not_connected` to others of their side.
- **Strengths are often reported for both sides**, so fewer sides should need grade E modelled
  strengths. That tests the method on a well-counted war before sparser eras such as the ancient
  battles the owner has in view.
- **A frame list exists.** Gaston Bodart, *Militär-historisches Kriegs-Lexikon (1618–1905)*
  (Vienna and Leipzig, 1908), lists engagements with strengths, losses and a winner. It is in the
  public domain. It is the frame, not an authority, as the CWSAC list was for the Civil War.

## The decisions (2026-10-06)

1. **Frame source: Bodart (1908) alone, frozen as printed.** No merged lists. Bodart's strengths are
   one source among several.
2. **Period and size.**
   - **Frame:** every Bodart entry dated 1792–1815 in the wars France fought.
   - **First cohort:** the 1805–1815 campaigns.
   - **No size cutoff.**
   - **Naval actions** stay in the frame but are not rated.
3. **Sides.**
   - Side A is France and the forces fighting with it; side B is their opponents.
   - Each side's national contingents are recorded.
   - A commander may appear on either side across engagements.
4. **Outcome.**
   - Bodart's recorded winner, frozen.
   - Disputes are recorded in dossiers, not resolved, and do not override the frame.
   - Losses never become predictors.
5. **Sources and language.**
   - **Scope:** each side's own public-domain official histories, returns and reports. These
     include the French General Staff campaign histories and Napoleon's correspondence, the
     Austrian and Prussian general-staff histories, Wellington's dispatches and Oman.
   - **Russian sources:** histories are used only where needed.
   - **Strength:** a side's own figures are preferred for its own strength.
   - **Citing:** quotes are in the original language, with locators and a marked English rendering.
   - **Figures:** read from page images.
6. **Usage budget.**
   - Up to three source families per engagement, plus one targeted follow-up.
   - One research agent per complete campaign; the primary verifies each campaign.
   - Usage is logged per campaign, with a projection after the first.
   - Work continues unless it would exceed a weekly cap set by the owner.
7. **Research dimensions.**
   - Strength and responsibility are researched in full.
   - Outcome is researched only where Bodart's result is disputed.
   - Terrain, logistics, information and objectives are recorded only from passages already read.
   - Posture and fortification, coded from those same passages, are the first candidate predictors.

   Only strength and responsibility feed a model today:

   | Dimension | Share of Civil War claims | Share of citations | Feeds a model |
   | --- | ---: | ---: | --- |
   | Strength | 23% | 19% | yes |
   | Responsibility | 11% | 17% | yes |
   | Outcome | 22% | 28% | no (the frozen frame) |
   | Terrain, logistics, information, objectives | 44% | 36% | no |

   Shares are of 3,577 claims and 16,090 citations.

**Addition.** The Napoleonic rating design (comparator, priors and rule) is fixed before any model
sees those outcomes. Run 4 showed that a comparator cannot be changed after the results are known.

## Frame source check (2026-10-06)

**Copies.** Internet Archive holds two Google scans of the 1908 Vienna and Leipzig edition:
`bub_gb_A0kNAAAAYAAJ` (962 page images) and `bub_gb_Eo4DAAAAYAAJ` (961). Both carry the Public
Domain Mark and ABBYY OCR. The project uses `A0kNAAAAYAAJ`.

- Its OCR yields about a third more entry headers.
- Its page images (1600 px) are clearly legible, including the figures.
- Its OCR is not reliable for figures. Years and digits are often garbled, for example `1N05` and
  `IHK` for 1805. Figures will therefore be taken from the page images, not the OCR.

**Size.** Counting entry headers in the OCR gives about **640 entries dated 1792–1815** and about
**317 dated 1805–1815**. These figures cover every war in those years, including some France did not
fight. The exact counts will come from the transcription.

*Result (2026-10-06):* the transcription has 708 entries on pp. 268–490. The frozen frame holds 663
engagements of 1792–1815 in France's wars, and cohort v1 holds the 325 land engagements of 1805–1815
([frame design](napoleonic-frame.md)).

| Year | 1792 | 1793 | 1794 | 1795 | 1796 | 1797 | 1798 | 1799 | 1800 | 1801 | 1802–04 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Entries | 10 | 56 | 63 | 17 | 42 | 13 | 12 | 71 | 30 | 9 | 0 |

| Year | 1805 | 1806 | 1807 | 1808 | 1809 | 1810 | 1811 | 1812 | 1813 | 1814 | 1815 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Entries | 21 | 25 | 17 | 17 | 57 | 16 | 21 | 39 | 47 | 43 | 14 |

The first cohort is therefore about the size of the Civil War frame (384 engagements, 305 in
scope), and decision 2 stands.

**Bodart's own rules** (*Erläuternde Vorbemerkungen*, pp. 45–47):

- **Selection.** An engagement is included if it had significant consequences, such as ending a
  campaign, lifting a siege, taking a capital or a capitulation. Otherwise it is included if
  combined losses on both sides reached 2,000. Naval actions are included at 1,000 or less.
  - The frame is therefore selected on size, losses or consequence. Small actions are absent.
- **Winner.** The winner always stands on the left of the two sides, and the loser on the right.
  "Indecisive" battles are still given a winner:
  - first, the side that held the field or reached its aim, even at greater loss;
  - failing that, the side that reached the same result with fewer troops.

  There are no draws. The fallback ties some outcomes to strength, so entries that dossiers find
  indecisive will need a sensitivity view. That view is fixed in the run design, before modelling.
- **Strengths.** Strengths are the forces *available* for the battle, which could have been brought
  in, not only those engaged. This matches the Civil War finding that Bodart's totals often count
  whole armies. In the strength ledger they are a separate basis, ranking below engaged counts.
- **Rounding.** Figures are rounded up, to 50 or 100.
- **Category.** The number after a place name, from (1.) to (6.), is a category set by combined
  losses (30,000, 20,000, 10,000, 5,000, 3,000 and 2,000 men on land). It is therefore post-start
  information and never a predictor.

**Running heads.** Each page's running head names its war and campaign, for example "Dritter
Koalitionskrieg — Feldzug 1805" and "Krieg gegen Österreich — Feldzug 1809". These give the frozen
campaign table. Because entries are printed by end date, a head can mislabel an entry at a war
boundary; the [frame design](napoleonic-frame.md#4-membership-and-wars) checks heads against
belligerents.

**The Civil War check of Bodart's figures** ([agreement artifact](../artifacts/strength-compilation-agreement.json)).
Arnold's machine-readable Bodart table, pinned for [ledger v3](ledgers-v3.md), covers 66 sides where
a Bodart total can be compared with a v2 point graded A–C:

- 44 are within 25%;
- 7 differ by more than a factor of two;
- the median ratio is 1.09.

**Another tabulation.** Arnold's package at the same commit links 49 battles of the CAA Database of
Battles (CDB90, a licensed dataset) one-to-one to CWSAC records, 43 of them in the Civil War
ledgers' scope. This comes from an unpinned read of `cdb90_to_cwsac.json` (SHA-256 `68aba256…`).
CDB90 itself was not consulted.

## What carries over and what must be versioned

- **Carries over:**
  - the evidence contract, dossier format and bounded first-pass protocol;
  - the source registry and hashing;
  - strength ledger grades A–E;
  - command-responsibility rules;
  - the rating design (partial pooling, leave-one-campaign-out verdict, both weightings);
  - the grade E method.
- **Already war-agnostic.** Rating run 4's code reads a war profile (`generalship/frame.py`) instead
  of Civil War constants: sides, outcome mapping, tables, ledgers, grade E levels and the temporal
  split. A commander's sign comes from the side commanded in each row, so one commander may fight on
  either side, as coalition wars need ([design §10](commander-ratings-v4.md#10-a-profile-for-each-war)).
  A new war adds a profile.
- **Civil War-specific; each needs a versioned design for the new war:**
  - `dataset.py` and `baseline.py`, which import and audit the CWSAC tables;
  - the strength-estimate engine and its checkers (`estimates*.py`), with their two-sided `SIDES`
    and source groups;
  - `command.py`, with its rank orders (`RANK_ORDER_V2`), the two-sided rule and naval handling;
  - the dossier validator, which accepts only cohort-v2 engagements in `data/evidence/`, so
    Napoleonic dossiers need their own directory and cohort;
  - campaign units: the Civil War uses CWSAC campaigns, and the new war uses Bodart's running heads.
- **Within-war pooling.** Ratings are pooled within a war. Comparing commanders across wars is a
  later, separate design.

## Order of work

1. Present decisions 1–7 to the owner with options and a recommendation. *(Done 2026-10-06.)*
2. Pin the frame source and transcribe the frozen list offline, with hashes. *(Done 2026-10-06:
   227 pages transcribed twice, reconciled and audited.)*
3. Write and verify the frame, cohort and campaign-group design. *(Done 2026-10-06:
   [frame design](napoleonic-frame.md).)* The war profile for ratings waits for the run design.
4. Begin first passes, by complete campaign group. The dossier validator first needs a
   Napoleonic cohort path and directory.
