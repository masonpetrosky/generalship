# Command-responsibility ledger v1

Prepared 2026-09-25 under the accepted [commander residual-rating design](../commander-ratings.md)
§2. **Status: reviewed and reconciled.** Four separate Claude Opus 5.5 `high` reviews, one per
campaign batch, found 29 required corrections; all were checked against the passages and
applied, with most advisories (see [Reviews](#reviews)). It names one
responsible commander per side as a graded best estimate. It rates nobody, fits nothing, and
changes no model input or dossier.

## Result

`data/command/responsibility-v1.json` covers all 91 decisive, non-aggregate engagements, both
sides. `data/command/commanders-v1.json` is the identity registry. `python3 -m generalship
command-check` replays every check, and `make check` runs it.

| Measure | Count |
| --- | ---: |
| Sides graded A / B / C / D (of 182) | 155 / 8 / 16 / 3 |
| Sides labelled `superior_directing` | 28 |
| Sides labelled `command_changed` | 17 |
| Sides labelled `responsibility_unresolved` | 12 |
| Sides labelled `joint_command` | 7 |
| Registry commanders | 132 (119 from CWSAC strings, 13 named only in passages) |
| Contained-interval pairs: nested / not nested / unresolved | 2 / 6 / 1 |

**Grade D sides.** There are three:

- TN002 Confederate: Floyd, Pillow and Buckner are all listed as brigadier general, and no
  inspected passage shows who commanded when the fighting began. The command passed to Buckner
  within the interval (`command_changed`).
- TN004 US: Davis's gunboats and Ellet's independent rams; no single force is shown compelling
  the result.
- AR006 US: Porter's fleet and McClernand's army; the description credits both together.

**On the 37 primary rows,** 52 commanders appear, and 9 have two or more modelled battles:

| Commander | Battles | Campaigns |
| --- | ---: | ---: |
| Lee | 5 | 5 |
| Jackson | 5 | 1 |
| Rosecrans | 4 | 3 |
| Morgan | 4 | 2 |
| Grant | 3 | 2 |
| Burnside | 3 | 3 |
| Bragg | 2 | 2 |
| Milroy | 2 | 2 |
| Ewell | 2 | 2 |

The design review's provisional count was 8. The batch 1 review moved McDowell (VA102) from
Schenck to Milroy, who took the first combat before Schenck arrived.

## Extraction record

- **Sources.** Every choice rests on one or more of these, each cited with an exact quote that
  the checker verifies:
  - the frozen CWSAC commander listing (its rank field);
  - the frozen CWSAC battle description;
  - dossier citations.

  No source outside the registry was used, and no choice rests on recollection.
- **Listing overturned.** In seven sides a passage names a different officer as commanding when
  the fighting began (rule 2, third bullet). Each is grade C, labelled
  `responsibility_unresolved`, with the listed officer kept as a candidate:
  - NC002 CS: Shaw, "the Confederate commander on the field";
  - TN005 CS: Leadbetter, "the commandant of the place", before Kirby Smith arrived;
  - KY007 US: Manson, who "commanded Union forces in the area" before Nelson arrived;
  - KY007 CS: Cleburne, who "led the advance" before Kirby Smith arrived;
  - KY009 CS: Polk, "under the immediate command of General Polk";
  - TN017 CS: Bate, who commanded the detachment in person before Stewart arrived;
  - TN011 US: Dunham, "the Federal commander" whose brigade made first contact, with Sullivan
    directing (review batch 2).
- **Listing kept, sources disagree** (grade C):
  - TN006 US: Cist says no one was in command;
  - OH001 US: NPS has Judah's brigade attacking; Hobson says Judah, arriving after Hobson's
    advance had engaged, assumed command of the whole force (also `command_changed`);
  - MS010 CS: Greene says there "seemed to be no one in command".

  KY008 US is no longer disputed: read in sequence, Cist agrees with NPS that Wilder commanded
  at the first assault, and Dunham took over later that day (`command_changed`).
- **Superior directing.** The label is used when a passage shows a named superior ordering or
  directing this operation, not merely holding departmental command. Borderline cases are kept
  in the rationales: Meade at Bristoe, Hardee at Ringgold Gap, Dennis at Milliken's Bend and
  Pope at Cedar Mountain.
- **Nesting.** VA032 (Chancellorsville) contains VA033 (Salem Church) and VA034
  (Fredericksburg II): its description narrates both, and its whole-army Union strength includes
  Sedgwick's wing. VA033/VA034 is unresolved. The other six pairs are separate actions. None of
  this changes the 37 primary rows (design §2 rule 7).
- **Echelon.** The design lists army, wing or corps, division, brigade, and detachment and post.
  The ledger adds `regiment` (NC006 CS) and `flotilla` (the naval sides). It records `unknown`
  for 70 sides whose passages do not state the echelon.
- **Registry merges.** Three pairs of CWSAC strings are merged on the listing's own fields (same
  side and surname; given names differ only by abbreviation or spelling):
  - "Humphery" and "Humphrey Marshall";
  - "Lawrence O'B." and "O'Bryan Branch";
  - "D.H." and "D. H. Hill".

  Thirteen officers named only in passages carry their citation: Shaw, Leadbetter, Mitchel,
  Potter, Manson, White, Polk, Bate, Judah, G. W. Smith, McDowell, Gilbert and Couch.
- **Not blind.** The extractor is an AI system that knows outcomes and reputations (design §8).
  The checker enforces the mechanical parts of the rules: rule order by listing count and
  service, rank ties, grade against rule, accounting for every listing, and quotes. The
  judgment calls are left to review.

## Reviews

| Review | Engagements | Required findings | Bundle |
| --- | --- | --- | --- |
| cmd-review-b1 | KY005 to VA021 (25) | R1–R7 | `artifacts/review-results/cmd-review-b1-a9520c2-opus-high-v1` |
| cmd-review-b2 | TN006 to AR006 (22) | R1–R10 | `artifacts/review-results/cmd-review-b2-a9520c2-opus-high-v1` |
| cmd-review-b3 | TN012 to AR008 (23) | R1–R7 | `artifacts/review-results/cmd-review-b3-a9520c2-opus-high-v1` |
| cmd-review-b4 | IN001 to TN029 (21) | R1–R5 | `artifacts/review-results/cmd-review-b4-a9520c2-opus-high-v1` |

The corrections were:

- two changes of the chosen commander (VA102 US, TN011 US);
- grade changes where passages were missed or misread;
- missing command-change and superior-directing labels, with four new passage-only registry
  entries;
- a corrected registry citation for Mitchel.

Unresolved items stay visible in the rationales. These include OH001 (whether Judah's column
engaged before joining Hobson), TN021 (the literal reading of Cist on Longstreet) and TN017 (the
earlier picket fight). These are AI reviews, not human historical adjudication.

## Next

- The owner's authorization of the gated model run (design §7), naming the hashes of both
  ledgers.
