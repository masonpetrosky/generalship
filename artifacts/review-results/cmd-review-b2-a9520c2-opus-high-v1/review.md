# Command-responsibility ledger, separate review, batch 2 of 4

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This is a separate
  subagent that started with fresh context. It did not see the author's conversation.
- **Date:** 2026-09-25.
- **Commits:**
  - prepared commit `a9520c2d5628c25b49437f4f54bfc78268a85393`;
  - previous commit `16a32116067912a1b5cb380097d75092a2a430b4`;
  - review bundle committed at `3d2cde9af400215d2842a292dc866ecb7ccb0d48`, the worktree HEAD.
- **Assignment:** `assignment.md`, sha256
  `b2c4606b440f8a0badddaafd9f8738efd7bd6dcf183865607aae07b5920d31d2`. Verified.
- **Input manifest:** `inputs.json`, sha256
  `11f34d78cb94fd48165b789ec37c0e0ff8ad82f6acee3d1d7e90581f9b5e3a62`. Verified.
- **Input hashes:**
  - All 24 bound paths match their manifest hashes, both through `git show a9520c2:<path>` and in
    the worktree. There is no mismatch.
  - Between `a9520c2` and HEAD, only the two review-bundle directories changed.
- **Status of this review:** an AI review is a separate analysis. It is not human historical
  adjudication, independent corroboration, feature admission or authorization of any fit. It made
  no changes to primary artifacts.

## Outcome: corrections required

Required findings: **R1–R10**. Advisories: **A1–A12**.

## Checks run (offline)

- `make check`: 126 tests, OK. It exited 0 and wrote no artifacts.
- `python3 -m generalship command-check`: exited 0. It reported:
  - 91 engagements and 182 sides;
  - grades A/B/C/D of 149/15/15/3;
  - 128 registry commanders;
  - nesting of 2 nested, 6 not nested and 1 unresolved;
  - `rated: false`.
- No build, packet, evaluation or network command was run.

## Scope actually inspected

**Documents read:**

- `AGENTS.md`;
- design `docs/commander-ratings.md`, §1–§3 in full;
- `docs/research/command-responsibility-v1.md`;
- `generalship/command.py`;
- the registry entries used by the batch, the passage-only entries (`us-white`,
  `us-mahlon-d-manson`, `cs-polk`), and a surname-collision scan;
- all 9 nesting records.

**For each of the 22 assigned engagements** (TN006, VA022, VA025, VA026, KY007, WV010, KY008,
MD002, MS001, WV016, MS002, TN007, KY009, TN008, VA028, NC007, NC009, TN009, MS003, TN010, TN011,
AR006), I read:

- both ledger sides in full: choice, rule, grade, echelon, labels, candidates, successor,
  superior, every citation and the rationale;
- the frozen CWSAC description and commander listing;
- every claim and citation in the bound dossier.

**Source sections read in full:**

- Cist `murfreesboro-raid`, `richmond-engagement` and `munfordville-siege`;
- Ropes `thoroughfare-gap` and `gainesville-august-28`;
- Palfrey `harpers-ferry-garrison-and-orders`, `harpers-ferry-investment-and-surrender` and
  `shepherdstown`;
- Greene `arkansas-post`;
- G. W. Smith OR reports `smith-1862-12-18` and `smith-1862-12-29`, plus the openings of the
  December 15 and 16 sections.

**Source sections searched for command passages only, not read in full:**

- Cist `perryville-approach-and-battle`, for Polk and Bragg;
- Ropes `cedar-mountain`, for Pope, and the Manassas sections, for Lee;
- Palfrey `south-mountain`, for Lee, Hill, Longstreet, McLaws and Cobb;
- Greene `corinth-and-hatchie`, for Grant, Hurlbut, Ord and Rosecrans;
- Greene `chickasaw-bayou`, for Pemberton and command;
- Jordan & Pryor `parkers-cross-roads`, for Sullivan, Dunham, Fuller and command.

**Not inspected beyond the dossier's own quotes:**

- Greene `iuka`;
- the Cist Stones River sections (TN008 and TN010);
- the Palfrey Fredericksburg sections (VA028);
- the OR Foster report (NC007 and NC009);
- Jordan & Pryor `jackson-operations` (TN009);
- the NPS raw files. I read only the NPS passages quoted in the dossiers, plus a search of
  `nps-ky008` for "brigade".

I did not test the other batches' engagements.

## Per-engagement result

| Engagement | US | Confederate |
| --- | --- | --- |
| TN006 | sound (A6) | sound (A5) |
| VA022 | sound (A9) | sound |
| VA025 | **R8** | sound |
| VA026 | sound (A5) | sound: rule 3(b), C |
| KY007 | sound (A5) | **R5** (A4) |
| WV010 | sound (A5, A8) | **R6** |
| KY008 | **R2** | **R3** (A5) |
| MD002 | sound | sound (A5) |
| MS001 | sound: the design's own example | sound |
| WV016 | sound | sound |
| MS002 | **R10** (A10) | sound |
| TN007 | **R9** (A12) | sound |
| KY009 | sound (A5) | **R4** |
| TN008 | sound | sound |
| VA028 | sound | sound |
| NC007 | sound | sound |
| NC009 | sound | **R7** (A5) |
| TN009 | sound | sound |
| MS003 | sound | sound (A7) |
| TN010 | sound | sound (A5) |
| TN011 | **R1** | sound (A5) |
| AR006 | sound: D under rule 5 (A1) | sound |

**Nesting.** Two pairs involve assigned engagements: VA026/VA025 and WV010/MD002. Both are
recorded `not_nested`, and both outcomes are defensible on fighting scope; see A2 and A3.

## Required corrections

The corrections are listed by consequence. For every correction, the primary must:

- recompute the memo counts, the grade and label table, and the "listing overturned" and "sources
  disagree" lists;
- rerun `command-check`.

R7 and R8 add passage-only registry entries. R1 and R7 cite sources that are not yet in
`bindings.cited_sources`:

- `jordan-west-tennessee-selections-v1`;
- `nps-tn011-v1`, if it is cited directly rather than through the dossier;
- `or18-smith-selections-v1`.

Their binding entries must be added from `data/sources.json`.

### R1. TN011 US: the listing is contradicted, and Dunham commanded when the fighting began

**What the ledger has.** Sullivan, rule 2, grade A. It cites only the listing and the description
line that has Sullivan, with Dunham's and Fuller's brigades, trying to cut Forrest off.

**What the passages show.** The engaged Union force at first contact was Dunham's brigade.

- The description says: "Dunham's and Forrest's march routes, on December 31, 1862, brought them
  into contact at Parker's Cross Roads."
- The description also says: "Forrest sent Dunham a demand for an unconditional surrender. Dunham
  refused". Fuller arrived later.
- Jordan & Pryor, `parkers-cross-roads`, p.211, a footnote citing Dunham's official report, names
  him "Dunham, the Federal commander".

Under rule 2, third bullet, this passage names a different officer as commanding the side's
engaged forces when the fighting began. The description shows Sullivan directing the operation.

**Exact change**, for `engagements[TN011].sides.US`:

- `commander_id`: `"us-cyrus-l-dunham"`. Identity rests on the description's "Col. Cyrus L.
  Dunham", which is the same string as the KY008 US listing on the same side. Jordan's OCR reads
  "C« T. Dunham"; record this in the rationale.
- `rule`: `"2"`.
- `grade`: `"C"`.
- `echelon`: `"brigade"`. The support is the description's "Dunham pulled his brigade back".
- `labels`: `["responsibility_unresolved", "superior_directing"]`.
- `candidates`: `["us-jeremiah-c-sullivan"]`.
- `successor`: `null`.
- `superior`: `"us-jeremiah-c-sullivan"`.
- `citations`:
  - keep the Sullivan listing rank;
  - add `{source_id: "jordan-west-tennessee-selections-v1", section: "parkers-cross-roads",
    locator: "p.211 (OCR page markers; not checked against print)", quote: "Dunham, the Federal
    commander", battle_id: "TN011"}`;
  - add `arnold-cwsac-battles` TN011 `description` "Dunham's and Forrest's march routes, on
    December 31, 1862, brought them into contact at Parker's Cross Roads.";
  - add `arnold-cwsac-battles` TN011 `description` "Forrest sent Dunham a demand for an
    unconditional surrender. Dunham refused".
- `superior_citations`: move the existing description quote there: "Union Brig. Gen. Jeremiah C.
  Sullivan, with the brigades of Col. Cyrus L. Dunham and Col. John W. Fuller, attempted to cut
  Forrest off".
- `rationale`: "Jordan and Pryor, citing Dunham's report, call Dunham 'the Federal commander'. The
  description has Dunham's brigade make first contact and refuse Forrest's demand before Fuller
  arrived. Sullivan directed the operation (rule 2, third bullet; superior_directing: Sullivan).
  Jordan and Pryor is a Forrest-endorsed history. An OCR-interleaved footnote ('just as General
  Sullivan came up') suggests that Sullivan arrived later; no inspected passage says that he took
  command."

`command_changed` is not added, because no passage has Sullivan taking command.

### R2. KY008 US: the ledger misreads Cist's sequence

**What the ledger says.** Its rationale says that the sources disagree about who commanded when
the fighting began.

**What Cist says** (`munfordville-siege`):

- He puts the garrison "under Colonel John T. Wilder" when Chalmers arrived (p.57).
- He then says: "an assault was made by the enemy, which was repulsed with heavy loss. Two
  detachments reported during the day, reinforcing Wilder's command." (p.58). Only after this
  does Dunham, "being Wilder's senior in rank", assume command.

So Cist agrees with NPS that Wilder commanded at the first assault on the 14th. The change to
Dunham happened within the interval, which is rule 4.

**Exact change**, for `engagements[KY008].sides.US`:

- `grade`: `"A"`.
- `labels`: `["command_changed"]`.
- `successor`: `"us-cyrus-l-dunham"`.
- `candidates`: unchanged, `["us-cyrus-l-dunham"]`.
- Add two direct `cist-heartland-selections-v1` citations in section `munfordville-siege`:
  - locator p.57, quote "the garrison there under Colonel John T. Wilder";
  - locator p.58, quote "an assault was made by the enemy, which was repulsed with heavy loss. Two
    detachments reported during the day, reinforcing Wilder's command."
- `rationale`: "NPS and Cist both put Wilder in command at the first assault on the 14th. Cist has
  Dunham arrive later that day and assume command as senior, and Wilder resume it under Gilbert's
  orders on the 16th (rule 3(a); rule 4)."

### R3. KY008 Confederate: unsupported echelon

`echelon` is `"brigade"`, but no inspected passage gives Chalmers's formation. Cist calls it
"Bragg's advance under General Chalmers". A search of `nps-ky008` finds no "brigade".

**Change:** `echelon` → `"unknown"`.

### R4. KY009 Confederate: `superior_directing` is missing

The same Cist section that the ledger cites has Bragg directing the operation within the theater
and on the field:

- p.63: "Bragg ordered Polk to move Cheatham's division back to Perryville";
- p.69: "again ordered Polk to bring on the engagement".

**Change:**

- `labels`: `["responsibility_unresolved", "superior_directing"]`.
- `superior`: `"cs-braxton-bragg"`.
- `superior_citations`: those two quotes, from `cist-heartland-selections-v1`, section
  `perryville-approach-and-battle`, at the locators given.

The choice of Polk and grade C stand.

### R5. KY007 Confederate: `superior_directing` is missing

The description, which the dossier also cites at `orders-for-contact[0]` through
`nps-ky007-v1`, reads: "Kirby Smith ordered Cleburne to attack in the morning and promised to
hurry reinforcements (Churchill's division)." This is the pattern of the design's MS001 example,
and the ledger itself uses it at KY008 CS, where a listed superior is also the successor.

**Change:**

- `labels`: `["command_changed", "responsibility_unresolved", "superior_directing"]`.
- `superior`: `"cs-e-kirby-smith"`.
- `superior_citations`: `[{dossier: {claim_id: "orders-for-contact", citation_index: 0},
  source_id: "nps-ky007-v1", quote: "Kirby Smith ordered Cleburne to attack in the morning and
  promised to hurry reinforcements (Churchill's division).", battle_id: "KY007"}]`.

See A4 on the choice itself.

### R6. WV010 Confederate: `superior_directing` is missing

The description shows Lee ordering and organizing this operation:

- "Lee decided to surround the force and capture it."
- "He divided his army into four columns, three of which converged upon and invested Harpers
  Ferry."

The ledger labels the comparable VA107 CS side on "Lee ordered it to clear the lower Valley".

**Change:**

- `labels`: `["superior_directing"]`.
- `superior`: `"cs-robert-e-lee"`.
- `superior_citations`: the two quotes above. Use `arnold-cwsac-battles` WV010 `description`,
  or the dossier reference `dislodge-objective[1]` (`nps-wv010-v1`) for the first.

Grade B and the choice of Jackson stand. The checker's grade B test looks only at `citations`.

### R7. NC009 Confederate: `superior_directing` is missing, and G. W. Smith needs a registry entry

G. W. Smith's December 29 report, which the dossier already cites (`smith-1862-12-29`), has him at
Goldsborough directing the fight:

- p.109: "I directed Lieutenant-Colonel Ste- vens";
- p.110, on the counterattack after the bridge was fired: "were ordered to cross, supported by
  Pettigrew’s brigade". The quote has a curly apostrophe.

**Change:**

- Add a registry entry: `{id: "cs-g-w-smith", name: "G. W. Smith", side: "Confederate",
  cwsac_names: [], passage_citation: {source_id: "or18-smith-selections-v1", section:
  "smith-1862-12-15-goldsborough", locator: "p.107 (OCR page markers; not checked against
  print)", quote: "G. W. SMITH", battle_id: "NC009"}}`.
- NC009 CS:
  - `labels`: `["superior_directing"]`;
  - `superior`: `"cs-g-w-smith"`;
  - `superior_citations`: the two quotes above, from `or18-smith-selections-v1`, section
    `smith-1862-12-29`.
- Bind `or18-smith-selections-v1` in `bindings.cited_sources`.

**Caveat on identity.** The December 29 section is unsigned in the selection. That its author is
G. W. Smith rests on the source record's `author` field and on the signed December 15 report.
State this in the rationale.

### R8. VA025 US: `superior_directing` is missing, and McDowell needs a registry entry

Ropes (`thoroughfare-gap`, p.68, which the dossier cites at `detachment-without-orders`)
attributes the operation to McDowell: "This action of McDowell's, taken, as it was, on his own
responsibility". Ricketts' division "was detached and sent to the Gap by way of Haymarket". The
dossier's own rationale says: "Authority for the detachment lay with McDowell".

**Change:**

- Add a registry entry: `{id: "us-mcdowell", name: "McDowell", side: "US", cwsac_names: [],
  passage_citation: {source_id: "ropes-northern-virginia-selections-v1", section:
  "thoroughfare-gap", locator: "p.68 (OCR page markers; not checked against print)", quote:
  "This action of McDowell's, taken, as it was, on his own responsibility", battle_id: "VA025"}}`.
- VA025 US:
  - `labels`: `["superior_directing"]`;
  - `superior`: `"us-mcdowell"`;
  - `superior_citations`: that quote.

Grade A and the choice of Ricketts stand.

### R9. TN007 US: `superior_directing` is missing

Greene (`corinth-and-hatchie`, p.52) says the interception was set by Grant:

- "Hurlbut, in obedience to orders from Grant, moved with his division from Bolivar", which is
  the dossier's `reported-force-scope[3]`;
- "with orders to intercept the Confederate re- treat.", which is the dossier's
  `interception-orders[0]`.

This is the MS001 pattern: Grant ordering Ord.

**Change:**

- `labels`: `["command_changed", "superior_directing"]`.
- `superior`: `"us-ulysses-s-grant"`.
- `superior_citations`: those two dossier citations.

### R10. MS002 US: the grade A citations come after the fighting

Both non-listing citations concern the pursuit decision after the battle ended. The dossier tags
this as `post_outcome`. Neither citation shows command when the fighting began on October 3.

**Change:**

- Add the dossier citation `{dossier: {claim_id: "reported-force-scope", citation_index: 3},
  source_id: "greene-iuka-corinth-selections-v1", quote: "23,000 under Eosecrans at Corinth",
  battle_id: "MS002"}`. This is Grant's October 1 return, which Greene gives.
- `rationale`: "Greene's October 1 return puts 23,000 under Rosecrans at Corinth before the October
  3 fighting; the pursuit decision shows he still commanded at the end."

The grade stays A.

## Advisories (no required change)

- **A1. AR006 US (grade D).**
  - The ledger did not consider two Greene passages: "Churchill himself surrendered the fort to
    McClernand about 4.30 p.m." and "McClernand's expedition proceeded up the Arkansas on January
    9th, the gunboats in the lead".
  - The design's rule 5 example treats the surrender recipient as the force compelling the result
    (TN001, surrender "to the fleet"). Read that way, rule 5's second case would give McClernand,
    grade C, `joint_command`, with Porter as candidate.
  - D remains defensible, because the frozen description credits "this envelopment, and the attack
    by McClernand's troops" together. McClernand "asked" Porter to open the bombardment, which does
    not show that McClernand commanded both forces.
  - Record the alternative in the rationale.
- **A2. WV010/MD002 nesting.**
  - Palfrey says McLaws, who commanded one of the Harpers Ferry investing columns, "sent word to
    General Cobb, who com- manded one of them, to take command of Crampton's Gap". He also says
    Cobb's, Semmes's and Mahone's brigades then rejoined McLaws's line.
  - So WV010's force scope partly overlaps MD002's Crampton's Gap defenders. The fighting scopes
    differ, so `not_nested` is defensible.
  - Add this to the reason, or use `nesting_unresolved`. Only outcome-only view (ii) is affected.
- **A3. VA026/VA025 nesting.** VA026's force field ("Armies") and its "Longstreet's wing of 28,000"
  include the units that fought at the Gap. Its description does not narrate the Gap fight, so
  `not_nested` stands. Note the force-scope point, since the VA032 outcome used force scope.
- **A4. KY007 CS choice.**
  - "Cleburne led the advance" could be read as rule 2's second bullet: a subordinate leading part
    of the force. That reading keeps Kirby Smith (rule 2, grade C, `responsibility_unresolved`,
    candidate Cleburne).
  - The ledger's choice is defensible because NPS has Smith arrive and take command later.
  - Record the alternative.
- **A5. Stronger or earlier-dated command passages.** These are all in sources the dossiers already
  cite. Adding them would not change any grade.
  - TN006 CS: the description's "Forrest's cavalry surprised the Union pickets".
  - VA026 US: Ropes, "Near midnight General Pope's order of 9 p.m. arrived". The ledger cites a
    passage dated August 29, but the fighting began on August 28.
  - KY007 US: Cist, "Nelson then ordered Manson's and Craft's brigades, under the command of the
    former".
  - WV010 US: Palfrey, "Colonel Miles, its commander".
  - KY008 CS: Cist, "On Bragg's advance under General Chalmers".
  - MD002 CS: Palfrey, "D. H. Hill was ordered to guard the pass, and Longstreet to march from
    Hagerstown to his support".
  - KY009 US: Cist has Buell with Gilbert's corps drawing up in line of battle.
  - NC009 CS: Smith, "under Gen- eral Clingman’s command to protect the two bridges".
  - TN010 CS: Cist, "Bragg issued orders to attack at daylight".
  - TN011 CS: Jordan & Pryor has Forrest throwing "his command in order of battle".
- **A6. TN006 US.** Cist also says "The post was under the command of General T. T. Critten- den",
  so Cist is internally inconsistent as well as disagreeing with NPS. Say so in the rationale.
  Grade C stands.
- **A7. MS003 CS rationale.**
  - The rationale says "no inspected passage states or contradicts the command". It overlooks two
    passages in Greene:
    - "Pemberton immediately went in person to Vicksburg" (December 26), which dates his personal
      presence;
    - "the original garrison of Vicksburg under Martin L. Smith", which is subordinate context.
  - B is still defensible, because neither passage states that Pemberton commanded the engaged
    forces. Update the rationale.
- **A8. WV010 US.** NPS has Miles surrender and then be mortally wounded. Palfrey has White succeed
  on Miles's wound and then surrender. The `command_changed` label rests on Palfrey alone. Record
  the conflict. Neither account disputes Miles at the start.
- **A9. Borderline `superior_directing` cases, left unlabelled.** Each is defensible as it stands.
  Record them.
  - VA022 US: Pope's order through Marshall. Ropes disputes its meaning: "It was not any part of
    General Pope's plan that it should be fought".
  - MS002 US: Grant "notified Rosecrans to be prepared, and directed Hurlbut".
  - MS003 CS: "Johnston and Pemberton, who immediately took steps to frustrate it".
- **A10. Echelon consistency.** MS002 US is `unknown`, but MS001 US is `army` for the same Army of
  the Mississippi. MS002's frozen force field reads "Army of the Mississippi [US]".
- **A11. Outside this batch (TN005).** The passage citation of registry entry `us-ormsby-mitchel`
  ("for an expedition against Chattanooga under the command of Negley.") does not name Mitchel. I
  did not inspect its context. Pass it to that batch's review.
- **A12. TN007 US.** NPS's "Hurlbut's 4th Brigade ... in the Confederates's front" leaves open
  whether Hurlbut's force skirmished before Ord took command. Greene has Ord arrive and take
  command before the Hatchie fight. A stands; note the ambiguity.

## Registry and identity

The batch's surname pairs are correctly kept apart:

- A. P. and D. H. Hill;
- R. E. and S. S. Lee;
- D. D. Porter and Fitz John Porter;
- John G. and John W. Foster.

The passage-only entries `us-white`, `us-mahlon-d-manson` and `cs-polk` cite passages that name
their officers. None of the batch's listings depends on a merge. R1, R7 and R8 add identity
decisions, which are stated in those findings.

## Limits

- This review checks extraction against the inspected passages. It does not adjudicate the history.
- Several of the decisive passages come from interested or single-family retrospective sources:
  - Cist, a Union staff history;
  - Jordan & Pryor, which Forrest endorsed;
  - Ropes, Palfrey and Greene;
  - commanders' own OR reports.
- Agreement between NPS and the CWSAC description is one family.
- OCR has not been checked against print.
- The superior-directing findings R4–R9 apply the ledger's own precedents (MS001, VA107, NC010 and
  KY008 CS) consistently. Whether that threshold is right is a design question for the owner.
