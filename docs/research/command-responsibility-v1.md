# Command-responsibility ledger v1

Prepared 2026-09-25 under the accepted [commander residual-rating design](../commander-ratings.md)
§2. **Status: a draft ledger awaiting separate review in campaign batches.** It names one
responsible commander per side as a graded best estimate. It rates nobody, fits nothing, and
changes no model input or dossier.

## Result

`data/command/responsibility-v1.json` covers all 91 decisive, non-aggregate engagements, both
sides. `data/command/commanders-v1.json` is the identity registry. `python3 -m generalship
command-check` replays every check, and `make check` runs it.

| Measure | Count |
| --- | ---: |
| Sides graded A / B / C / D (of 182) | 149 / 15 / 15 / 3 |
| Sides labelled `superior_directing` | 15 |
| Sides labelled `command_changed` | 11 |
| Sides labelled `responsibility_unresolved` | 11 |
| Sides labelled `joint_command` | 7 |
| Registry commanders | 128 (119 from CWSAC strings, 9 named only in passages) |
| Contained-interval pairs: nested / not nested / unresolved | 2 / 6 / 1 |

**Grade D sides.** There are three:

- TN002 Confederate: Floyd, Pillow and Buckner are all listed as brigadier general, and no
  inspected passage shows who commanded when the fighting began.
- TN004 US: Davis's gunboats and Ellet's independent rams; no single force is shown compelling
  the result.
- AR006 US: Porter's fleet and McClernand's army; the description credits both together.

**On the 37 primary rows,** 53 commanders appear, and 8 have two or more modelled battles:

| Commander | Battles | Campaigns |
| --- | ---: | ---: |
| Lee | 5 | 5 |
| Jackson | 5 | 1 |
| Rosecrans | 4 | 3 |
| Morgan | 4 | 2 |
| Grant | 3 | 2 |
| Burnside | 3 | 3 |
| Bragg | 2 | 2 |
| Ewell | 2 | 2 |

This matches the design review's provisional count of 8.

## Extraction record

- **Sources.** Every choice rests on one or more of these, each cited with an exact quote that
  the checker verifies:
  - the frozen CWSAC commander listing (its rank field);
  - the frozen CWSAC battle description;
  - dossier citations.

  No source outside the registry was used, and no choice rests on recollection.
- **Listing overturned.** In six sides a passage names a different officer as commanding when
  the fighting began (rule 2, third bullet). Each is grade C, labelled
  `responsibility_unresolved`, with the listed officer kept as a candidate:
  - NC002 CS: Shaw, "the Confederate commander on the field";
  - TN005 CS: Leadbetter, "the commandant of the place", before Kirby Smith arrived;
  - KY007 US: Manson, who "commanded Union forces in the area" before Nelson arrived;
  - KY007 CS: Cleburne, who "led the advance" before Kirby Smith arrived;
  - KY009 CS: Polk, "under the immediate command of General Polk";
  - TN017 CS: Bate, who commanded the detachment in person before Stewart arrived.
- **Listing kept, sources disagree** (grade C):
  - TN006 US: Cist says no one was in command;
  - OH001 US: Hobson says Judah assumed command of the whole force, without dating it;
  - KY008 US: NPS gives Wilder; Cist says Dunham assumed command as senior.
- **Nesting.** VA032 (Chancellorsville) contains VA033 (Salem Church) and VA034
  (Fredericksburg II): its description narrates both, and its whole-army Union strength includes
  Sedgwick's wing. VA033/VA034 is unresolved. The other six pairs are separate actions. None of
  this changes the 37 primary rows (design §2 rule 7).
- **Echelon.** The design lists army, wing or corps, division, brigade, and detachment and post.
  The ledger adds `regiment` (NC006) and `flotilla` (the naval sides). It records `unknown` for
  76 sides whose passages do not state the echelon.
- **Registry merges.** Three pairs of CWSAC strings are merged on the listing's own fields (same
  side and surname; given names differ only by abbreviation or spelling):
  - "Humphery" and "Humphrey Marshall";
  - "Lawrence O'B." and "O'Bryan Branch";
  - "D.H." and "D. H. Hill".

  Nine officers named only in passages carry their citation: Shaw, Leadbetter, Mitchel, Potter,
  Manson, White, Polk, Bate and Judah.
- **Not blind.** The extractor is an AI system that knows outcomes and reputations (design §8).
  The checker enforces the mechanical parts of the rules: rule order by listing count and
  service, rank ties, grade against rule, accounting for every listing, and quotes. The
  judgment calls are left to review.

## Next

- Separate Opus review in the four campaign batches used for the strength ledger.
- Reconciliation.
- The owner's authorization of the gated model run (design §7), naming the hashes of both
  ledgers.
