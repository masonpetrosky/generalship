# Cohort v2 ledgers: extraction record

Prepared 2026-09-25 under the [scope addendum](../ledgers-v2.md). **Status: extracted, separate
review pending.** Two versioned successor ledgers extend the v1 strength and command ledgers to
the full-war frame. They rate nobody, fit nothing and change no model input or dossier. The v1
ledgers, the estimate-layer evaluation and the first rating run are unchanged.

## Result

| Ledger | File | Checker |
| --- | --- | --- |
| Strength | `data/estimates/side-strength-v2.json` | `python3 -m generalship estimate-check --ledger data/estimates/side-strength-v2.json` |
| Command | `data/command/responsibility-v2.json`, registry `data/command/commanders-v2.json` | `python3 -m generalship command-check --ledger data/command/responsibility-v2.json` |

Both cover the 305 in-scope engagements of cohort v2 (91 carried forward from v1 unchanged, 214
new); 79 are listed as out of scope (inconclusive, aggregate, or with a Native American
belligerent under the two-sided rule). `make check` replays both.

**Strength (all 305).**

| Measure | All | New 214 |
| --- | ---: | ---: |
| Sides graded A / B / C / D | 184 / 60 / 114 / 252 | 125 / 39 / 88 / 176 |
| Rows with both sides A (fit-eligible) | 61 | 40 |
| Rows with both sides A–B | 83 | 54 |
| Rows with both sides A–C | 130 | 93 |
| Rows excluded as `post_start_information` | 20 | 13 |

v1 had 21, 29 and 37 fit-eligible rows. 59 new sides carry figures from the new Livermore pages
(`livermore-transcription-v2`); 34 Livermore entries match 44 engagements, and campaign
aggregates (Atlanta, May 1864; Appomattox) are inventoried but not used as a single record's force.

**Command (all 305).** Sides graded A 512, B 21, C 68, D 9. For the 428 new sides:

| Measure | Count |
| --- | ---: |
| Grades A / B / C / D | 357 / 13 / 52 / 6 |
| Rules 2 / 3(a) / 3(b) / 3(c) / 5 / 6 | 351 / 58 / 4 / 2 / 12 / 1 |
| `superior_directing` / `command_changed` / `responsibility_unresolved` / `joint_command` | 124 / 42 / 45 / 13 |
| New contained-interval pairs: nested / not nested / unresolved | 2 / 4 / 1 |

The registry has 401 commanders (every v1 ID kept): 11 carry merged CWSAC strings, 63 are named
only in passages, and 6 passage-only names are identified with a listed commander by a cited
passage (`passage_merges`).

On the 130 rows with both strength sides graded A–C, 170 responsible commanders appear and 41
have two or more rows, against 9 on the v1 run's 37 primary rows. This is a coverage count, not
a rating; the rating design's attribution, nesting and view rules have not been applied.

## Extraction record

- **Method.** Eight campaign batches were extracted by separate Claude Opus 5.5 agents under one
  brief, each writing the command entries first and then the strength entries, and each batch
  passed the checkers in subset mode before the full build. The primary decided every merge.
- **Merges.** Listing strings merge only when side and surname match and the given names differ
  only by abbreviation or spelling (for example "Horatio Wright" and "Horatio G. Wright"). A
  passage-only name merges only when a cited passage gives matching initials or the full name
  (for example "General C. C. Augur"). Surname-only matches stay separate (Polk, McDowell, Rust,
  McCausland, Franklin, Hunter), as do "James B. Fagan" and "James F. Fagan" and the passages'
  William Lamb against the listed Charles Lamb.
- **Not blind.** The extractors know outcomes and reputations. The checkers enforce the
  mechanical rules; the judgment calls each batch reported are left to the separate reviews.
- **Engine consequences to watch.** The fixed rules can give implausible points from their
  inputs. Examples flagged by the extractors: Memphis 1864 (TN031) Confederate 400, the lower
  middle of the frozen "approx. 400" and the NPS cell's 2,000; Bentonville (NC020), where both
  points come from three-quarters of opponent estimates because every own-side figure covers
  March 19 only. These are reported, not overridden.

## Next

- Separate Opus reviews in campaign batches: eight for the command entries and eight for the
  strength entries, each checked and reconciled before any use.
- A v2 estimate-layer evaluation or rating run then needs a new owner authorization naming the
  reviewed ledger and registry hashes.
