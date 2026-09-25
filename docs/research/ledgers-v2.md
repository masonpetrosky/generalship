# Cohort v2 ledgers: extraction and review record

Prepared 2026-09-25 under the [scope addendum](../ledgers-v2.md). **Status: reviewed and
reconciled.** Sixteen separate Claude Opus 5.5 `high` reviews, one per ledger and campaign batch,
found 54 required corrections; each was checked against its passage and applied or dispositioned
(see [Reviews](#reviews)). Two versioned successor ledgers extend the v1 strength and command
ledgers to the full-war frame. They rate nobody, fit nothing and change no model input or dossier.
The v1 ledgers, the estimate-layer evaluation and the first rating run are unchanged.

## Result

| Ledger | File | Checker |
| --- | --- | --- |
| Strength | `data/estimates/side-strength-v2.json` | `python3 -m generalship estimate-check --ledger data/estimates/side-strength-v2.json` |
| Command | `data/command/responsibility-v2.json`, registry `data/command/commanders-v2.json` | `python3 -m generalship command-check --ledger data/command/responsibility-v2.json` |

Both cover the 305 in-scope engagements of cohort v2 (91 carried forward from v1 unchanged, 214
new); 79 are listed as out of scope (inconclusive, aggregate, or with a Native American
belligerent under the two-sided rule). `make check` replays both.

**Strength.**

| Measure | All 305 | New 214 |
| --- | ---: | ---: |
| Sides graded A / B / C / D | 182 / 57 / 109 / 262 | 123 / 36 / 83 / 186 |
| Rows with both sides A (fit-eligible) | 61 | 40 |
| Rows with both sides A–B | 80 | 51 |
| Rows with both sides A–C | 126 | 89 |
| Rows excluded as `post_start_information` | 17 | 10 |

v1 had 21, 29 and 37 fit-eligible rows. 59 new sides carry figures from the new Livermore pages
(`livermore-transcription-v2`); 34 Livermore entries match 44 engagements, and campaign
aggregates (Atlanta, May 1864; Appomattox) are inventoried but not used as one record's force.

**Command.** All 610 sides: A 504, B 24, C 71, D 11. For the 428 new sides:

| Measure | Count |
| --- | ---: |
| Grades A / B / C / D | 349 / 16 / 55 / 8 |
| Rules 2 / 3(a) / 3(b) / 3(c) / 5 / 6 | 351 / 55 / 5 / 4 / 12 / 1 |
| `superior_directing` / `command_changed` / `responsibility_unresolved` / `joint_command` | 121 / 45 / 50 / 13 |
| New contained-interval pairs: nested / not nested / unresolved | 2 / 4 / 1 |

The registry has 403 commanders (every v1 ID kept): 11 carry merged CWSAC strings, 65 are named
only in passages, and 8 passage-only names are identified with a listed commander by a cited
passage giving initials or the full name (`passage_merges`).

On the 126 rows with both strength sides graded A–C, 166 responsible commanders appear and 40
have two or more rows, against 9 on the v1 run's 37 primary rows. This is a coverage count, not a
rating; the rating design's attribution, nesting and view rules have not been applied.

## Extraction record

- **Method.** Eight campaign batches were extracted by separate Claude Opus 5.5 agents under one
  brief, command entries first and strength entries second; each batch passed the checkers in
  subset mode before the full build. The primary decided every merge.
- **Merges and identification.** Listing strings merge only when side and surname match and the
  given names differ only by abbreviation or spelling ("Horatio Wright" and "Horatio G. Wright").
  A passage-only name merges only on a passage giving initials or the full name ("General C. C.
  Augur"; "JOHN McCAUSLAND, Colonel, Commanding"). Surname-only matches stay separate where the
  surname is shared or a review required it (Polk at MO009, Breckinridge at VA076, Rust, Hunter),
  as do "James B." and "James F." Fagan, the passages' William Lamb against the listed Charles
  Lamb, and MS014's "G. G. Washburn" against the listed C. C. Washburn. The identification rule
  is stated in the addendum.
- **Conventions settled across batches** (applied by the primary after review):
  - "near N" is read as "nearly N", a one-sided bound, as v1 read "nearly" (FL005, MO010, NC020,
    and NM001 and OK004 in review);
  - a surrender or after-action count whose dossier claim is not tagged post-outcome is a
    post-engagement state, not a post-outcome claim (AR009, GA001, GA028, KY011, LA010);
  - a frozen CWSAC figure equal to a report figure is not linked as a reproduction without a
    passage or printed source note showing the dependence (Livermore's printed source letters did
    show it at AR001 and AR005);
  - Hood's addenda-table totals (TN034, TN038) keep an unknown basis: the cited quotes do not
    include the table's "Effective" header.
- **Not blind.** The extractors know outcomes and reputations. The checkers enforce the mechanical
  rules; the reviews checked the judgment calls within their batches.
- **Engine consequences.** The fixed rules can give implausible points from their inputs, for
  example Memphis 1864 (TN031) Confederate 400, the lower middle of the frozen "approx. 400" and
  the NPS cell's 2,000, and VA047 US 39,000 from a campaign-level NPS cell coded
  `scope_unresolved` for a division-level action. These are reported, not overridden.

## Reviews

| Review | Batch | Required | Bundle |
| --- | --- | ---: | --- |
| v2cmd-b1 … b8 | command, 1861 through 1865 | 2, 4, 6, 2, 4, 1, 3, 5 | `artifacts/review-results/v2cmd-b{1..8}-11d4bc3-opus-high-v1` |
| v2est-b1 … b8 | strength, same batches | 2, 7, 2, 5, 1, 5, 2, 3 | `artifacts/review-results/v2est-b{1..8}-11d4bc3-opus-high-v1` |

Every required finding was accepted and applied after its passage was checked, except where the
correction needed a shared registry decision; those were decided by the primary (the Hagood merge
evidence, the Franklin and McCausland merges). Each bundle's `primary-assessment.md` lists every
finding's disposition, and `correction.json` binds the corrected ledger files. Notable changes:
Petersburg June 15 US (Grant, A → C, `command_changed` to Meade), Glasgow MO022 CS and Ream's
Station VA068 CS (to grade D), Five Forks VA088 CS (A → C: "There was no Confederate commander
on the field"), Kennesaw GA015 and Jonesborough GA022 CS (Livermore entries partial, to D), and
Pea Ridge and Prairie Grove CS (Livermore relays the commanders' own figures).

These are AI reviews, not human historical adjudication. Open questions stay in the rationales:
several `superior_directing` borderlines, nesting on force scope alone (LA010/LA009,
GA011/GA012), Farragut credited at both LA001 and LA002, and the three one-day Price records
(KS003, KS004, MO028).

## Next

A v2 estimate-layer evaluation or rating run needs a new owner authorization naming the reviewed
ledger and registry hashes.
