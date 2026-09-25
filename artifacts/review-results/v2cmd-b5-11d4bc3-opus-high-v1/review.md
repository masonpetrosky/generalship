# Command-responsibility ledger v2: separate review, batch 5 of 8

**Outcome: corrections required** (4 required findings: R1–R4; 8 advisories: A1–A8).

## Record

| Item | Value |
| --- | --- |
| Reviewer | Separate Claude subagent, fresh context, `claude-opus-5-5`, reasoning effort `high` |
| Date | 2026-09-25 |
| Prepared commit reviewed | `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372` (previous `96110cf`) |
| Bundle commit / worktree HEAD | `2f63306ad033e2bda1710dd88dd47c99cf86f748` |
| `assignment.md` sha256 | `977093f290752586cb454e8576ed38e33055f820f320450ddfc58e316b2b9996` (matches) |
| `inputs.json` sha256 | `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0` (matches) |
| Bound inputs | All 25 paths in `inputs.json` hash-match both `git show 11d4bc3…:<path>` and the worktree. No mismatch. Between the prepared commit and HEAD, only `artifacts/review-results/` changed. |
| Ledger / registry | `data/command/responsibility-v2.json` `1271ea87…753a`; `data/command/commanders-v2.json` `cdf72348…e267c` |

**Unbound reading.** The assignment names several files that `inputs.json` does not bind. I read
them at the worktree, which is identical to the prepared commit for these paths:

- `docs/commander-ratings.md` `0ab4b7d5…4bb`
- `docs/ledgers-v2.md` `a7e05ddf…9eb1`
- `docs/research/command-responsibility-v1.md` `208b796a…dd88`
- `generalship/command.py` `58ffe17e…62ef6954`

The ledger's own `design` and `addendum` bindings match the first two hashes. The assignment calls
the addendum `docs/ledgers-v2.md`, but `inputs.json` binds `docs/research/ledgers-v2.md` (the
extraction record). I read both.

**Checks run (offline).**

- `make check` exited 0, with 143 tests OK.
- `python3 -m generalship command-check --ledger data/command/responsibility-v2.json` exited 0:
  - 305 engagements and 610 sides, graded A 512, B 21, C 68, D 9;
  - 401 registry commanders;
  - nesting outcomes: nested 4, not_nested 10, nesting_unresolved 2.

I ran no build, packet or evaluation command. I modified no primary artifact.

## Scope actually inspected

- **Sides.** All 54 sides of the 27 assigned engagements:
  - VA047, VA053, VA054 (Bermuda Hundred);
  - VA052, VA056, VA059, VA062, VA099 (Overland);
  - VA098, VA063, VA065, VA113, VA067, VA068, VA069, VA070, VA071, VA072, VA073, VA075, VA074,
    VA077, VA078, VA079, VA080, VA083, VA084 (Richmond-Petersburg).
- **Fields checked for each side.** Commander, rule, grade, labels, candidates, successor,
  superior, echelon, citations and rationale.
- **Frozen CWSAC material.** For each engagement, the frozen CWSAC description and every CWSAC
  commander row (name, rank, navy).
- **Dossiers.** The `command-roles` claim of each bound dossier. I also resolved every ledger
  citation to its full dossier-cited section: about 1 MB of text across 27 files.
- **How the sections were read.** I read them in context around each quoted passage and ran
  keyword searches for command, arrival, relief, timing and the names of candidate officers. I
  did not read every page of every section end to end.
- **Registry.** All 40 registry IDs these sides use, including:
  - the merges for Butler, Gillmore, Terry and R. H. Anderson;
  - the passage-only entries for Graham, Johnson, Pickett, Hoke, Robert Ransom, Wise, Farinholt,
    Kershaw and Wilcox;
  - the `passage_merges` entry on `cs-johnson-hagood`.

  I compared these against the frozen CWSAC listing for surname collisions: Henry Wise, Robert
  Hoke, Bushrod R. Johnson, George Pickett and Cadmus Wilcox.
- **Nesting.** The only contained-interval pair that involves an assigned engagement is VA062 ⊃
  VA099. I recomputed this with `contained_pairs` over the in-scope set.
- **Not inspected.**
  - the 91 carried-forward v1 entries, which are out of scope;
  - the other batches' engagements, except the one SC007 passage noted in A2;
  - the strength ledger;
  - any source outside the dossier-cited sections and the frozen CWSAC files.

  I did no new research.

## Required corrections

### R1: VA063 US (Petersburg, June 15–18). Rule 3(a) is not met, so rule 3(b) applies

The ledger gives Grant under rule 3(a), grade A, as "the listed officer shown in command of the
engaged forces of both armies". The Grant passages it cites date from after the side's first
combat:

- Humphreys (`humphreys-petersburg-selections-v1`, dossier `reported-force-scope`/3) has Smith take
  his orders from Butler, who is not listed: "By sunset of the 14th he had reported in person to
  General Butler at Bermuda Hundred and received orders to move at daylight on Petersburg."
- The first combat came early on the 15th: "This evidently referred to the rifle-pit captured by
  General 11 inks early in the day."
- Grant's direction comes only later: "About four o’clock in the afternoon, General Smith was
  informed by a staff officer sent by General Grant". Grant's despatch to Hancock came "a few
  minutes before" half-past five.
- Meade (`or40-1-meade-petersburg-selections-v1`, `rations-and-bridge`/0) has the same timing:
  "Late in the evening this day, the 15th, orders were received from the lieutenant-general
  commanding, then at City Point".

No inspected passage shows either listed officer in command of the side's engaged forces when the
fighting began. The ranks are not tied (Lieutenant General over Major General), so rule 3(b) gives
Grant.

The same Meade section also records a command change for the engaged troops on the 16th: "the
lieutenant-general commanding, by whom I was instructed to take command of the troops then in
front of Petersburg".

**Change VA063 US to:**

| Field | New value |
| --- | --- |
| `commander_id` | `us-ulysses-s-grant` (unchanged) |
| `rule` | `3b` |
| `grade` | `C` |
| `labels` | `["command_changed", "responsibility_unresolved"]` |
| `successor` | `us-george-g-meade` |
| `candidates` | `["us-george-g-meade"]` (unchanged) |
| `superior` | `null` |
| `echelon` | `army` (unchanged) |

- **Citations.** Add the four quotes above with their dossier locators: `reported-force-scope`/3
  for the first three and `rations-and-bridge`/0 for the Meade quotes. Keep the existing listing
  citations.
- **Rationale.** The replacement should say that:
  - the first combat on the 15th was by Smith's column under Butler's orders;
  - Butler is unlisted;
  - Grant's recorded orders come from the afternoon and evening;
  - Grant is chosen as the senior listed officer (rule 3(b));
  - Meade was instructed to take command of the troops in front of Petersburg on the 16th (rule 4).

### R2: VA065 CS (Jerusalem Plank Road). A passage naming Hill was missed, so grade A does not hold

The rationale says that "no passage names another officer commanding the Confederate engaged
forces". But the same Humphreys section the ledger already cites for the US side
(`humphreys-petersburg-selections-v1`, `reported-force-scope`/2) says: "General A. P. Hill had been
sent down the Weldon Rail¬ road to meet Meade’s attempt upon it, having Wilcox’s and…". Hill is
not listed for VA065.

The first combat on the 21st is not attributed to any commander: "During the day General Barlow
made a reconnoissance toward the Weldon Railroad, and a considerable force of the enemy moved down
the road to meet it."

Lee's dispatch reports the fighting from army headquarters, but it does not state that he
commanded the engaged force. So the inspected sources disagree about who commanded. That is grade
C under rule 2. The listing is not strictly contradicted at first combat, because Hill's command is
not dated to the 21st.

**Change VA065 CS to:**

| Field | New value |
| --- | --- |
| `commander_id` | `cs-robert-e-lee` (unchanged) |
| `rule` | `2` |
| `grade` | `C` |
| `labels` | `["responsibility_unresolved"]` |
| `candidates` | `["cs-a-p-hill"]` |

- **Citations.** Add both quotes above, from `reported-force-scope`/2.
- **Rationale.** Replace the "no passage names another officer" sentence with the Hill passage. It
  should add that the June 21 contact is unattributed. The alternative is noted in A7.

### R3: VA068 CS (Ream's Station, June 29). Rule 3(a) is not met. Tied listed ranks give rule 3(c), grade D

The ledger's own rationale says Hampton's attack at daylight preceded the Reams' Station contact:
"By the clock, Hampton's daylight attack on Wilson's rear near Sappony Church (Lee's dispatch)
preceded the Reams' Station contact". Hampton is not listed here.

The rationale then sets that fight aside as "VA067's record". But VA067's frozen interval is
1864-06-28. The design defines first combat as the side's first combat within the frozen interval,
which here is 1864-06-29. The frozen VA068 description itself includes Wilson "fighting against
elements of William H.F. "Rooney" Lee's cavalry" before joining Kautz. The v1 precedent (VA102
moved to Milroy, who "took the first combat") applies the same rule.

The evidence:

- Lee (`or40-1-lee-petersburg-selections-v1`, `command-roles`/1): "General Hampton reports that he
  attacked the enemy’s cavalry yesterday afternoon…" and "The fight continued during the night, and
  at daylight this morning he turned their left and routed them."
- Wilson (`or40-1-wilson-south-side-raid-selections-v1`, `reported-force-scope`/3): "By 7 a. m. of
  the 29th General Kautz’s advance reached Beams’ Station".

No passage shows Mahone or Fitzhugh Lee in command of the side's engaged forces when the fighting
began. No passage names one officer over Hampton, Mahone and Fitzhugh Lee. Both listed officers
are Major General, a tie.

**Change VA068 CS to:**

| Field | New value |
| --- | --- |
| `commander_id` | `null` |
| `rule` | `3c` |
| `grade` | `D` |
| `labels` | `["responsibility_unresolved"]` |
| `candidates` | `["cs-william-mahone", "cs-fitzhugh-lee"]` |
| `successor` | `null` |
| `superior` | `null` |
| `echelon` | `unknown` |

- **Citations.** Keep the existing ones, and add the Wilson 7 a.m. quote.
- **Rationale.** State that the first combat within the interval was Hampton's daylight attack.
  Hampton is unlisted, and his command is recorded as context only. The two listed officers tie,
  so rule 3(c) applies.

The US side is unaffected: Wilson commanded at both the dawn fight and Reams' Station.

### R4: VA072 CS (Globe Tavern). The rationale misreads the first-combat passage. The choice and grade stand

The rationale says: "The dawn fighting of the 18th … is not assigned to any commander in the
inspected passages." The cited Humphreys section (`humphreys-petersburg-selections-v1`,
`reported-force-scope`/2) identifies the opposition: Warren took the railroad "finding only
Dealing’s cavalry brigade to oppose him". It also says: "General Dearing had reported to General
Beauregard the appearance of some force on the railroad". Neither Dearing nor Beauregard is listed
for VA072.

The Lee dispatch (`or42-1-lee-petersburg-selections-v1`, `reports-of-movement`/2) disagrees on who
met Warren first: "About noon the enemy in front of Petersburg moved his Fifth Corps toward the
Weldon railroad, when he was met by General Heth". Because the sources disagree, rule 3(a) with
grade C remains supportable.

**Change VA072 CS as follows:**

- Keep `commander_id` `cs-henry-heth`, rule `3a`, grade `C`, and all labels, candidates, successor
  and superior as they are.
- Add the two Humphreys quotes above as citations, from `reported-force-scope`/2.
- Replace the quoted rationale sentence with: "Humphreys has Warren meet only Dearing's cavalry
  brigade at first (Dearing, unlisted, reported to Beauregard, unlisted), while Lee's dispatch has
  Warren 'met by General Heth'. The sources disagree on who commanded at first contact (grade C)."
- If the primary does not accept Lee's dispatch as a disagreeing account, rule 3(b) would give Lee
  (the sole General listed), grade C, `responsibility_unresolved`, with Hill, Heth and Mahone as
  candidates.

## Advisories (no change required)

- **A1: nesting VA062 ⊃ VA099.**
  - `not_nested` is defensible: the Trevilian fighting is in Louisa County, and the Cold Harbor
    description does not narrate it.
  - However, the recorded reason itself says the force scopes "partly overlap" and that no passage
    says whether the Cold Harbor strength includes Sheridan's divisions.
  - If force-scope uncertainty is meant to trigger it, `nesting_unresolved` would be the more
    cautious outcome. This is the primary's decision.
- **A2: registry `cs-johnson-hagood` `passage_merges` (bound to SC007, outside this batch).**
  - The `basis` says "the passage names 'General Johnson Hagood'", but the cited quote ("General
    Hagood relieved General Taliaferro in command of Wagner…") has no given name.
  - The given name does appear in SC007 `command-roles`/6 (`jones-charleston-1863-selections-v1`,
    section `wagner-siege-and-evacuation`): "commanded succes- sively by Brigadier Generals
    Taliaferro, Johnson Hagood". I verified that it resolves.
  - Suggest using that quote for the merge citation. VA047's outcome does not depend on it.
- **A3: VA052 US `superior_directing` Meade.**
  - The label rests on "on your instructions", which in Sheridan's report refers to the initial
    march. The same report says Sheridan himself "determined at once to march around the enemy's
    right flank".
  - The label is defensible because Meade ordered the expedition, but it is borderline. The
    rationale could say so.
- **A4: VA077 US (Kautz, rule 3(a), A).**
  - Humphreys places Kautz on "the right of the force on the north side of the James", which
    implies a larger force whose commander no inspected passage names for October 7.
  - The same source's August section says "the Tenth Corps, or part of it, under General Birney",
    which is not dated to October.
  - The choice stands. Grade C would also be defensible, and the rationale could note it.
- **A5: VA083 US (grade D, rule 3(c)).**
  - A defensible reading. Rule 3(a) giving Humphreys is an alternative: his two divisions made a
    named first contact ("soon dis¬ persed").
  - Gregg's Dinwiddie contact is unordered in time and falls under neither listed officer, so D is
    reasonable.
  - Note that Humphreys is both a candidate and the author of the history.
- **A6: VA059 US.** The fourth citation is a substring of the second (the same Sheridan dispatch).
  This is harmless and could be deduplicated.
- **A7: VA065 CS alternative.** If the primary reads Hill's force as the force that met Barlow on
  the 21st, rule 2's third bullet would give Hill, grade C, with Lee as a candidate. That would be
  consistent with VA073, where Hill was chosen on a similar Humphreys passage.
- **A8: VA063 US context.** After R1, the rationale could name Butler, who is unlisted, as the
  officer whose orders sent Smith's first-combat column. It could also name Smith. This is context
  only: rule 3 chooses among listed officers.

## Sides checked with no finding

All other sides in the batch were checked with no finding. For each, the choice, rule, grade,
labels, echelon and citations are supported by the quoted passages read in context. Notes on some
sides follow.

**Bermuda Hundred**

- **VA047 CS.** The choice of Graham is supported. Hagood's report says of the May 6 force "the
  whole under Colonel Graham" and that Hagood "at dark on that night … arrived at Petersburg".
  Johnson came as successor, "arriving after the repulse", and "withdrawn hv General Johnson".
  Pickett is flagged as a borderline superior, and Humphreys's "relieved of that command by
  General Beauregard about the 1st of May" confirms the rationale's caveat. The alternative
  reading is recorded.
- **VA047 US, VA053, VA054.** No finding. For VA053 CS, the rule-2 grade C rests on Humphreys:
  Beauregard is at Petersburg on the 12th and Hoke is "to obey the orders of the Secretary of
  War". Hoke and Ransom as candidates are sound.

**Overland**

- **VA052 CS.** Stuart is shown "commanding the enemy's cavalry". `command_changed` with no
  successor is correct: no passage names who succeeded him on the field.
- **VA056, VA059 CS, VA062.** No finding. VA062 US chooses Meade under rule 3(a) with Grant
  directing, which contrasts appropriately with R1.
- **VA099.** No finding.

**Richmond-Petersburg**

- **VA098 CS.** Wise is supported under rule 2's third bullet: "had charge of the defences of
  Petersburg". Not merging him with the listed "Henry Wise" is correct, because the passage gives
  no given name.
- **VA098 US, VA113, VA067, VA068 US, VA069, VA070, VA071.** No finding.
- **VA073 CS.** Hill is supported under rule 2's third bullet. Two passages name him: Humphreys's
  "was assigned to this task, having with him…" and Lee's dispatch.
- **VA074, VA075 CS.** No finding. For VA075 CS, Ewell holds "in command … where he was joined by
  General Lee during the day", and `command_changed` gives Lee.
- **VA078, VA079, VA080, VA084.** No finding.

**Registry**

- **Listing merges.** The merges for Butler, Gillmore (including "Qunicy"), Terry and Richard
  (H.) Anderson follow the listing-field rule.
- **Passage-only names.** These correctly stay separate from same-surname listings, because the
  passages give no given names or initials:
  - Johnson from Bushrod R. Johnson;
  - Pickett from George Pickett;
  - Hoke from Robert Hoke;
  - Wilcox from Cadmus Wilcox;
  - Wise from Henry Wise.
- **Robert Ransom.** The passage gives the full name, but there is no CWSAC listing to merge with.

## Limits

- This is a separate AI analysis within the scope stated above. It is not human historical
  adjudication, not proof of source independence, not feature admission, and not authorization of
  any fit or rating run.
- Most passages are OCR text. Page locators are marked "not checked against print".
- Several key accounts are retrospective (Humphreys 1883) or adversarial (Butler and Gillmore;
  Burnside and Meade). I treated them as the sources state them, not as verified contemporary
  record.
