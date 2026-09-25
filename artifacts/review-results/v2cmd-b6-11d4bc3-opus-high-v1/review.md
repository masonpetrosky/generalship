# Command-responsibility ledger v2, batch 6: separate review

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a separate
  subagent started with fresh context. I did not see the author's conversation.
- **Date:** 2026-09-25
- **Prepared commit reviewed:** `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372` (against `96110cf`)
- **Bundle commit / worktree HEAD:** `0766caaca08fc55aa7c8d53085b910e8e32246db`. `git diff`
  between the prepared commit and HEAD shows no change under `data/`, `generalship/` or `docs/`.
  The only changes are review-bundle files.
- **Assignment:** `assignment.md` sha256 `923ce48644f2089bb73688ac5e5c236865e147d232e746fe8ba6a0b7e44e11df`
- **Input manifest:** `inputs.json` sha256 `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0`
- **Outcome: corrections required** (one required finding, R1; advisories A1–A8).

This is an AI review, a separate analysis within the scope stated below. It is not human
historical adjudication. It does not establish that any sources are independent, and it does not
admit features or authorize a fit.

## Input verification

- **Bound inputs.** All 25 paths in `inputs.json` match their recorded sha256 in both places:
  - `git show 11d4bc3…:<path>`;
  - the worktree.

  There are no mismatches.
- **Files read but not bound in `inputs.json`.** The assignment also directed me to read these.
  Their hashes are identical at the prepared commit and in the worktree:
  - `docs/commander-ratings.md`: `0ab4b7d541baf4f8e642634f316628f9cb372d68dcdbbc047a305f5a1fb704bb`. This equals the ledger's `design` binding.
  - `docs/ledgers-v2.md`: `a7e05ddfc072c493f8f9152064e444e4b285e070a7dfcdbd279e80fc4aa49eb1`. This equals the ledger's `addendum` binding.
  - `docs/research/command-responsibility-v1.md`: `208b796a3f60ffc869a6686a12241a4356b4e94655128fb84bc88433dc33d0dd`
  - `generalship/command.py`: `58ffe17ebc42cc3d2ec5950e55d56a243caf662460df86059c845ade62ef6954`
  - `data/pilot/cohort-v2.json`: `614f6c9bbb188e0cc003e1132a70b5bc2d72ee1e2f605423ffb957bd4d1b66f9`. This equals the ledger's `cohort` binding.
- **Dossier bindings.** All 24 assigned dossier bindings (`data/evidence/<ID>.json`) match their
  recorded sha256.
- **Checks run offline.**
  - `make check`: 143 tests, `OK`, exit 0.
  - `python3 -m generalship command-check --ledger data/command/responsibility-v2.json`: exit 0.
    It reported 305 engagements, 610 sides, grades A 512 / B 21 / C 68 / D 9, 401 registry
    commanders, and nesting outcomes of 4 nested, 10 not nested and 2 unresolved.

  I ran no build, packet or evaluation command. I made no network access, did no new research,
  started no agents and edited no files other than this one.

## Scope inspected

For all 24 assigned engagements, I checked the following for both sides:

| Group | Engagements |
| --- | --- |
| Atlanta | GA007, GA009, GA010, GA011, GA012, GA014, GA015, GA016, GA017, GA018, GA020, GA021, GA022 |
| Forrest | MS014, MS015, TN031 |
| Morgan | KY011 |
| Early | MD007, DC001, VA114, VA115, VA116, WV013 |
| Mobile Bay | AL003 |

For each side, I read:

- the ledger entry: choice, rule, grade, labels, candidates, successor, superior, echelon and
  rationale;
- the frozen CWSAC description and commander listing, including the name fields;
- the dossier's `responsibility` claim;
- the full resolved passage around every quote cited from a dossier. I read the passage context
  itself, not just checked that the quote occurs.

I also ran targeted searches of the bound passages for missed command statements. These covered:

- Hood and the addressee in Cleburne's report (GA012);
- Hooker's despatch (GA014);
- Hardee's order (GA018);
- Steedman's timing (GA020);
- Kilpatrick's account of the 20th (GA021);
- Buckland in Washburn's report (TN031);
- Washburn in the MS014 and MS015 passages;
- Burbridge at Paris (KY011);
- Lee's orders in Forrest's report (MS015).

For identity, I checked the registry entries of every commander, candidate, successor and
superior that these entries use. That includes these merges and passage-only entries:

- the merges Wright, Burbridge, Augur, Hardee and Schofield;
- the passage-only entries Laiboldt, Garis and Hunter.

I recomputed contained-interval pairs with `contained_pairs`. The only pair involving an assigned
engagement is GA011 ⊃ GA012.

I did not re-inspect the 91 carried-forward v1 entries or other batches' entries. I also did not
inspect dossier passages outside the 24 engagements, except where a registry entry used here cites
another record (SC010, OK004, LA009 listing), and those only at the level of the recorded quote and
basis.

## Required corrections

### R1. MS014 US: the superior's identity with the listed C. C. Washburn has no rule-compliant basis

**Finding.** The MS014 US side records `superior: "us-c-c-washburn"`. That registry ID is the
TN031 listing string "C.C. Washburn" (listing field `first_name` = "C.C."). The MS014 passages do
not identify the superior that way:

- The superior citations give only these phrases:
  - "the major-general commanding the District of West Tennessee";
  - the addressee "Maj. Gen. G. G. Washburn".
- Elsewhere the same report says only "General Washburn" (surname only).

The rationale makes the identification "by the district command". That rests on a passage in a
different record: TN031, Washburn's August report, "commanding District of West Tennessee", which
is dated more than two months after the MS014 fight. The registry records no `passage_merges`
entry or basis for this identification.

**Rule.** The v2 merge rule (`docs/ledgers-v2.md`, Registry; `docs/research/ledgers-v2.md`,
Merges) says a passage-only name merges "only when a cited passage gives matching initials or the
full name". It also says surname-only matches stay separate, as for Polk, McDowell and Hunter.
Here the initials do not match ("G. G." against "C.C."), and the other evidence is surname-only.

**Why it matters.** The §6 "Superior directing" view uses the named superior. With this identity,
MS014 US would be credited to the same commander term as TN031 US. That gives Washburn two
modelled battles, which is enough to rank.

**Exact correction:**

1. **Registry.** Add a passage-only entry to `data/command/commanders-v2.json`:
   ```json
   {"id": "us-washburn", "name": "Washburn", "side": "US", "cwsac_names": [],
    "passage_citation": {"dossier": {"claim_id": "recorded-result", "citation_index": 2},
      "source_id": "or39-1-sturgis-brices-cross-roads-selections-v1",
      "quote": "Maj. Gen. G. G. Washburn", "battle_id": "MS014"}}
   ```
   The quote occurs in the resolved passage. It closes Sturgis's June 11 dispatch:
   "S. D. STUEGIS, Briga dier- Gen era 1. Maj. Gen. G. G. Washburn."
2. **Ledger, MS014 US.** Set `superior` to `"us-washburn"`. Keep the label and both superior
   citations.
3. **Rationale.** Replace "identified with the TN031 listing by the district command" with this
   text: "kept separate from the TN031 listing 'C.C. Washburn': the passage's initials read
   'G. G.' and the district-command match rests on another record's later passage, so under the
   v2 surname/initials rule it is not merged (as for Hunter)."

If the primary instead judges that the district-command match justifies a merge, that is an
exception to the documented v2 rule. The addendum would have to state it, and it would have to be
recorded as a `passage_merges` entry with its basis. Under the rule as written, I cannot endorse
it.

No other required corrections.

## Advisories (not required)

- **A1. MS015 Confederate: `command_changed`, successor Forrest.**
  - The quote is accurate: "On reaching Harrisburg Lieutenant-General Lee ordered me to take
    command of the troops and to pursue the enemy."
  - The same passage continues that Forrest moved "with Lieutenant-General Lee to Tupelo for the
    purpose of consulting and receiving orders". So Lee kept directing after the handover.
  - The label is defensible because Forrest took command of the engaged troops for the Old Town
    Creek fight. However, it is a delegation, not a relief or a death.
  - Suggestion: add that sentence to the rationale as a borderline note, because view (ii)
    credits the successor.
- **A2. Grade A where the chosen officer is shown commanding only part of the engaged force.**
  - Cases:
    - GA021 CS (Jackson): the infantry at the station, which Kilpatrick met first on the 20th, is
      not shown under Jackson.
    - VA115 CS (Ramseur): Averell's report names the cavalry brigades of "Vaughn and Imboden and
      Colonel Jackson" alongside Ramseur's division.
    - GA012 CS (Cleburne): the frozen forces field reads "Cleburne's Division and Brig. Gen. John
      H. Kelly's Brigade".
  - In each case, rule 2 correctly keeps the single listing, and no passage names a different
    officer over the whole force. The rationales disclose the partial scope.
  - Grade A there rests on passages that show the officer commanding the principal force. That
    reading of "the side's engaged forces" could be stated once in the extraction record.
- **A3. TN031 US echelon.** The echelon `detachment_or_post` has no basis in the rationale.
  Washburn reports as "commanding District of West Tennessee", and Buckland commanded the District
  of Memphis. Consider `unknown`, or state the basis.
- **A4. Superior citations that could be sharper.**
  - GA016 US: the quote "whilst Thomas with more than half the whole army marched by several
    roads" does not name Sherman. The same passage contains "Sherman therefore determined that the
    longest way round would prove the surest".
  - GA014 US: "Schofield, in accordance with instructions from General Sherman, made no serious
    effort to cross the stream" concerns the June 19 approach. Cox's account of Kolb's Farm has
    Sherman "concerned lest Schofield had not fully met the spirit of his instructions", which is
    at the `command-roles` citation 1 locator. If it occurs in a bound citation, it is closer.
  - Neither issue changes the label.
- **A5. GA022 US.** The rationale relies on Cox (Howard's army received the August 31 attack;
  Sherman and Thomas urged Stanley on September 1), but no Cox citation is recorded. Grade A still
  rests on the description. Add a Cox citation or trim the rationale.
- **A6. AL003, both sides.** The rule 5 second case is applied and the grade D reading is
  disclosed. Over the 22-day interval, the army siege took Gaines and helped take Morgan. For the
  losing side, "the force compelling the result" is also an unusual reading.
  - The choices (Farragut C, Buchanan C, `joint_command`, candidates Granger and Page) follow the
    rule as written.
  - A joint reading would make both sides D. That is a legitimate alternative to keep visible.
- **A7. GA011 ⊃ GA012 `nested`.** The outcome is consistent with the VA032 precedent: whole-army
  force fields ("Military Division of Mississippi [US]; Army of Tennessee [CS]") and a description
  that runs through May 26 to June 1. It is consequential, though: it drops GA012, a Confederate
  victory, from any view that contains both records. The rationale's narrower reading ("the Battle
  of Dallas occurred on May 28") would make the pair `nesting_unresolved`. GA010 has the same
  whole-army force fields but only overlaps GA011, so rule 7 does not reach it.
- **A8. Assignment inputs.**
  - The assignment names the addendum as `docs/ledgers-v2.md`, but `inputs.json` binds
    `docs/research/ledgers-v2.md`, the extraction record. The ledger binds `docs/ledgers-v2.md`.
    I read both.
  - The design, the v1 memo, `generalship/command.py` and `cohort-v2.json` are not in
    `inputs.json`. Their hashes are recorded above.
  - Later bundles could bind these explicitly.

## Checked and found sound

For every side not named above, the choice, rule, grade, labels, candidates, successor and
echelon follow design §2 on the passages I inspected, and each cited quote supports what its
rationale says. The table notes the points that needed a closer look.

| Engagement | Side | What was checked |
| --- | --- | --- |
| GA010 | US | Rule 3(a), Sherman over Hooker with continuous command authority. The first-contact reading is disclosed. |
| GA014 | US | Rule 3(c), grade D; no passage puts either tied officer over the other. |
| GA014 | CS | Johnston is not labelled; Hood attacked "on his own". |
| GA016 | CS | The change to Hood came before the interval. |
| GA018 | CS | Hardee's ordered takeover did not take effect: "the battle was over by the time that general could reach the field". |
| GA020 | US | Laiboldt "commanding Dalton", C, successor Steedman. Steedman reached the bridge "after midnight" and advanced "At daylight". |
| KY011 | US | Garis, C, successor Burbridge, who was at Paris with "the telegraph lines being cut". |
| DC001 | US | Rule 3(a), McCook: "held his corps in reserve, subject to McCook's orders". Superior Augur by the matching-initials merge. |
| WV013 | CS | McCausland; his absence from the point of first contact does not contradict his command. |
| WV013 | US | Superior is the passage-only `us-hunter`, consistent with the surname rule. |

- **Registry merges used here, all sound on listing fields or matching initials:**
  - Horatio G. Wright / Horatio Wright;
  - Stephen Gano Burbridge / Stephen Burbridge;
  - C. C. Augur;
  - W. J. Hardee;
  - John M. Schofield.
- **Passage-only entries, each citing its passage:** Laiboldt, Garis, Hunter.
