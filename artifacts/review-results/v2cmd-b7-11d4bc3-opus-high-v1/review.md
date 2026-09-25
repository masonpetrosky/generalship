# Command-responsibility ledger v2, batch 7 of 8: separate review

## Reviewer and inputs

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. A fresh-context subagent
  with no access to the author's conversation.
- **Date:** 2026-09-25.
- **Assignment:** `artifacts/review-results/v2cmd-b7-11d4bc3-opus-high-v1/assignment.md`
  (sha256 `4e729703a1000cebc15753318c44efde3d429dc56288433c85548811c5020eae`, verified).
- **Input manifest:** `inputs.json` (sha256
  `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0`, verified).
- **Commits:** prepared commit `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372`, compared against
  `96110cf`. The worktree is at the bundle commit `4ad2dc29f803ebc1ca151bd5b8239dcf6c6a8649`, which
  adds only review assignments after `11d4bc3` (`git diff --stat 11d4bc3 4ad2dc2` touches only
  `artifacts/review-results/*/assignment.md|inputs.json`).
- **Hash check:** all 25 manifest paths hash to their recorded values at
  `git show 11d4bc3:<path>`, and the same values in the worktree. There are no mismatches.
- **Files read that the manifest does not bind** (the assignment names them). I recorded their hashes
  at the worktree, which is identical to `11d4bc3` for these paths:
  - `docs/commander-ratings.md` `0ab4b7d541baf4f8e642634f316628f9cb372d68dcdbbc047a305f5a1fb704bb`,
    which equals the ledger's `design` binding;
  - `docs/ledgers-v2.md` `a7e05ddfc072c493f8f9152064e444e4b285e070a7dfcdbd279e80fc4aa49eb1`,
    which equals the ledger's `addendum` binding;
  - `docs/research/command-responsibility-v1.md`
    `208b796a3f60ffc869a6686a12241a4356b4e94655128fb84bc88433dc33d0dd`;
  - `generalship/command.py` `58ffe17ebc42cc3d2ec5950e55d56a243caf662460df86059c845ade62ef6954`.

  The assignment calls the addendum `docs/ledgers-v2.md`, but the manifest binds
  `docs/research/ledgers-v2.md` (the extraction record). I read both. The ledger binds the first.

## Commands run (offline)

| Command | Result |
| --- | --- |
| `make check` | exit 0; "Ran 143 tests … OK" |
| `python3 -m generalship command-check --ledger data/command/responsibility-v2.json` | exit 0; 305 engagements, 610 sides, A 512 / B 21 / C 68 / D 9, registry 401, nesting nested 4 / unresolved 2 / not_nested 10 |

I ran no build, packet, evaluation or network command. No agents were spawned. The only file I wrote
is this one.

## Scope actually inspected

**Coverage.** All 25 assigned engagements, both sides (50 sides): VA119–VA122, MO021–MO029, KS003,
KS004, VA076, GA023, AL004, TN032–TN038. For each side I read the following:

- the ledger entry: choice, rule, grade, labels, candidates, successor, superior, echelon, citations
  and rationale;
- the frozen CWSAC listing rows (`cwsac_commanders.csv`, including the `navy` field) and the frozen
  description and `forces_text` (`cwsac_battles.csv`);
- the registry entries the entries use, including the `merge_basis` of Horatio G. Wright and Stephen
  Gano Burbridge, the Schofield `passage_merges` entry and the passage-only Doolittle entry.

**Passages read in context.** I read the cited passages in their surrounding text in the registered
selections:

- Pond: Tom's Brook, and searches of the whole file for Torbert's formation;
- Early: the Winchester/Fisher's Hill report and the Tom's Brook dispatch;
- Britton: the pilot-knob, lexington-little-blue, glasgow, independence-big-blue, big-blue-westport,
  mine-creek-little-osage and newtonia sections, at every cited passage;
- Price's 1864-12-28 report: Glasgow, Independence and Mine Creek;
- Burbridge, the A. E. Jackson dispatches and Gardner, all in full;
- Corse, French, Granger, Doolittle, Sinclair and Rousseau, at the cited passages;
- Cox: its Columbia, Spring Hill and Franklin sections, searched for Thomas's role;
- the MO022, MO023 and VA076 dossiers' responsibility claims and open questions.

**Also checked:**

- the three nesting pairs involving assigned engagements (MO026/MO025, MO026/MO027, TN034/TN035);
- how `contained_pairs` handles records with identical intervals;
- the v1 precedents the memo cites (VA102, KY007, TN011).

**Not inspected:**

- the full OR volumes (`or39-1-full.txt`, `or41-1-full.txt`, `or45-1-full.txt`) and
  `cox-march-full.txt`, beyond what the selections contain;
- Hood's and Forrest's selections beyond the cited quotes, which the checker verifies;
- the 91 carried-forward v1 entries and the other batches' entries.

## Required corrections

### F1. MO022 Confederate: Shelby's choice under rule 3(a) at grade A is not supported, so the side becomes rule 3(c), grade D

Clark and Shelby are both listed as Brigadier General (a tie). Rule 3(a) needs a passage showing one of
them "in command of the side's engaged forces", and grade A needs a passage that *states* it. No
inspected passage does. The passages show two co-equal detachments, which Price ordered and neither
officer commanded over the other.

The plan came from above both brigadiers. Britton, section `glasgow`, p.454, says: "In the plan of
attack it had been arranged that General Shelby should march up and open fire with his artillery on
the Federal position from the west side of the river, while General Clark, who had crossed to the
north side, should attack the Federal force". Price's report, section `price-1864-12-28`, p.632,
gives the orders:

- Clark was sent "to cross the river at Arrow Rock and attack the place the next morning at
  daylight and capture it";
- Shelby was sent "with a small portion of his division and a section of his artillery to attack the
  town from the west side of the river at the same hour, to divert the attention of the enemy".

Shelby fired first only because Clark's crossing was delayed ("Owing to unforeseen difficulties in
crossing the river Brigadier-General Clark was unable to commence the attack for one hour after
Brigadier-General Shelby had engaged them"). Clark's column then made the attack itself (Britton:
"the Confederate force advancing under General Clark").

Shelby therefore commanded a diversionary part of the force. He was not the field commander
directing the operation. There was no command change either: Clark did not take over Shelby's force.
This is unlike VA102, where Milroy commanded the whole engaged force until Schenck arrived and took
command. It is also unlike MO025 and MO026, where one listed officer commanded all of the side's
engaged forces in an earlier, separate phase.

3(a) does not decide the side, and 3(b) has no single senior officer, so rule 3(c) applies.

Exact changes, in `data/command/responsibility-v2.json`, `engagements[MO022].sides.Confederate`:

| Field | Current | New |
| --- | --- | --- |
| `commander_id` | `"cs-joseph-shelby"` | `null` |
| `grade` | `"A"` | `"D"` |
| `rule` | `"3a"` | `"3c"` |
| `echelon` | `"detachment_or_post"` | `"unknown"` |
| `labels` | `["superior_directing"]` | `["responsibility_unresolved", "superior_directing"]` |
| `candidates` | `["cs-john-b-clark"]` | `["cs-john-b-clark", "cs-joseph-shelby"]` |
| `superior`, `superior_citations` | Price | unchanged |

Add this citation to `citations`. The quote occurs verbatim in the source; I checked it by substring
match:

```json
{"source_id": "britton-price-missouri-selections-v2", "section": "glasgow",
 "locator": "p.454 (OCR page markers; not checked against print)",
 "quote": "In the plan of attack it had been arranged that General Shelby should march up and open fire with his artillery on the Federal position from the west side of the river, while General Clark, who had crossed to the north side, should attack the Federal force",
 "battle_id": "MO022"}
```

Replace `rationale` with:

> Both listed brigadier generals (tie). Rule 3(a) does not decide: Price sent two separate detachments, Clark's (his own brigade and 500 of Jackman's) to cross and capture the town and Shelby's (a small portion of his division with artillery) to attack from the west bank 'at the same hour, to divert the attention of the enemy', and Britton says the plan 'had been arranged' with Shelby opening fire from across the river 'while General Clark … should attack the Federal force'. Shelby's guns opened first at sunrise because Clark's crossing was delayed ('Clark was unable to commence the attack for one hour after Brigadier-General Shelby had engaged them'); Clark's column then made the main attack and received the surrender. No inspected passage puts either brigadier over the other or over the side's engaged forces, and no command passed between them, so rule 3(c) applies: grade D, candidates Clark and Shelby. Price ordered both detachments from the main column (superior_directing: Price).

Check the change with `command-check`. Rule 3(c) with a tie, grade D and a null commander pass
`RULE_GRADES` and the tie test. Consequence: the Confederate grade counts move A −1, D +1.

### F2. VA076 Confederate: one candidate's identity rests on surname alone, and the rationale misreads Jackson's dispatches

**(a) Identity.** The candidate `cs-john-c-breckinridge` is mapped, in the rationale's words, "on name
alone". The VA076 passages give only "Breckinridge" (Burbridge) and "Major-General Breckinridge"
(Gardner), with no given name or initials. The addendum allows a passage-only name to merge "only when
a cited passage gives matching initials or the full name", and surname-only matches stay separate.
This is the kind of identity the assignment asks me to flag: it is asserted without a listing field
or a passage.

The Echols candidate is sound. Jackson's cited dispatch names the addressee "Brig. Gen. John Echols",
the full name of the listed John Echols (WV012).

Exact changes:

- In `data/command/commanders-v2.json`, add this passage-only entry:

  ```json
  {"id": "cs-breckinridge", "name": "Breckinridge", "side": "Confederate", "cwsac_names": [],
   "passage_citation": {"dossier": {"claim_id": "shooting-of-wounded-prisoners", "citation_index": 1},
     "source_id": "or39-1-gardner-saltville-selections-v1",
     "quote": "paroled by Major-General Breckinridge", "battle_id": "VA076"}}
  ```

- In `engagements[VA076].sides.Confederate.candidates`, replace `"cs-john-c-breckinridge"` with
  `"cs-breckinridge"`.
- Rebind the registry hash in the ledger's `bindings.registry`.

**(b) Rationale accuracy.** The rationale says Jackson's "dispatches of October 1-2 are signed
'Brigadier-General, Commanding' at Saltville and addressed to Echols as his superior". Only the
October 1 dispatch is addressed to Echols ("A. E. JACKSON, Brigadier- General^ Commaiiding. Brig. Gen.
John Echols."). The October 2, 5 p.m. dispatch is addressed to "Capt. H. T. Stanton, Assistant
Adjutant- General". The address alone does not state that Echols was Jackson's superior.

In `rationale`, replace:

> and his dispatches of October 1-2 are signed 'Brigadier-General, Commanding' at Saltville and addressed to Echols as his superior.

with:

> and his dispatches of October 1-2 are signed 'Brigadier-General, Commanding' at Saltville; the October 1 dispatch is addressed to 'Brig. Gen. John Echols' (the October 2 dispatch to Capt. H. T. Stanton).

Also replace:

> Candidates Echols and Breckinridge are mapped to the registry's John Echols (Jackson's addressee 'Brig. Gen. John Echols') and John C. Breckinridge on name alone.

with:

> Candidate Echols is the registry's John Echols (Jackson's addressee 'Brig. Gen. John Echols'); candidate Breckinridge is a passage-only entry ('Major-General Breckinridge', Gardner), not identified with the listed John C. Breckinridge because no inspected VA076 passage gives his initials or full name.

The choice (Jackson), grade C, rule 2 and label are unchanged.

### F3. TN032 US: the rationale misstates the declared rank order

The rationale says "'Lieutenant Commander' is not in the declared navy rank order". The ledger's own
`rank_order.navy` and `RANK_ORDER_V2` in `generalship/command.py` include it: `['Admiral', 'Rear
Admiral', 'Flag Officer', 'Captain', 'Commander', 'Lieutenant Commander', 'Lieutenant', 'Master']`.
The addendum says the same: "Lieutenant Commander, Lieutenant and Master below Commander".

In `engagements[TN032].sides.US.rationale`, replace:

> 'Lieutenant Commander' is not in the declared navy rank order; no rank comparison is needed here.

with:

> 'Lieutenant Commander' is in the declared v2 navy rank order; army and navy ranks are never compared (rule 5), so no rank comparison is made here.

The choice, grade D and `joint_command` are unchanged.

## Checked without change (per side, brief)

- **VA119, VA120, VA122 (Confederate); VA119, VA120 (US).** Rule 2 at grade A is supported:
  - Early ordered the divisions up when firing began and ordered the retreat;
  - Sheridan advanced with VI and XIX Corps and directed Thoburn;
  - Grant appears only after the fact.
- **VA121.**
  - US: Torbert at grade A is supported ("Torbert was in the saddle at dawn …"). The
    `superior_directing` label for Sheridan rests on "I directed Torbert to attack at daylight".
  - Confederate: Rosser at grade B is correct. Early's dispatch shows two separate commands (Rosser
    and Lomax) under Early, who "remained here" at New Market. No passage states that Rosser commanded
    the side's engaged forces, and none contradicts the listing.
- **VA122 US.** Wright under rule 3(a) at grade A, with `command_changed` and successor Sheridan, is
  well supported ("Major General Wright, commanding the army temporarily, Major-General Sheridan
  being temporarily absent").
- **MO021.** Supported on both sides:
  - Ewing "assumed command of the Federal forces at Pilot Knob" on the 26th, before the frozen
    27th. Rosecrans's `superior_directing` label is within the theater, and it is consistent with
    TN034 (Thomas) and TN038 (Halleck and Grant not labelled).
  - Price ordered the assault.
- **MO023, MO024, MO027, MO029.** Supported:
  - At MO024 Britton says outright: "General Curtis, who was present on the field directing the
    general movements of his forces". Neither Moonlight nor Blunt is called the Federal commander,
    so the TN011/KY007 pattern is not triggered.
  - At MO027, Curtis ordered the dawn attack.
  - At MO029, Britton has Curtis's other brigades "under General Curtis, which had not participated
    in the fight", so omitting the label is correct.
- **MO025, MO026.** The rule 3(a) choices are supported:
  - MO025 Confederate: Fagan's pickets and Cabell's brigades made the first combat.
  - MO026 US: Blunt commanded the right wing, which held the Big Blue on the 22nd.
  - MO026 Confederate: Shelby.

  Pleasonton and Marmaduke fought in later, separate phases, so they are candidates, not
  successors. Curtis's `superior_directing` label at MO026 rests on Britton: he "was at the front
  all day", and Blunt "was assigned to the command of his right wing".
- **KS003, KS004.**
  - US: Pleasonton, with superior Curtis ("being the senior officer present, assumed command").
  - Confederate: Marmaduke under rule 3(a). Britton says he "was in command of the Confederate rear
    that day". In context, the quoted withdrawal is the Marais des Cygnes phase, and Britton's "his
    hasty consultation with Generals Fagan, Clark, and Cabell" follows at Mine Creek. Price also has
    "Major-General Marmaduke, in the rear" and Fagan's indorsement that "he would sustain" him.
    Marmaduke's capture as `command_changed` with a null successor is honest: no passage names a
    successor, and the VA052 and NC006 precedent is the same.
- **MO028.** Both sides supported.
  - US: McNeil at grade A, with Pleasonton as superior. Britton: "General Pleasonton ordered McNeil
    to form the Second and Fourth Brigades".
  - Confederate: Price.
- **VA076 US.** Burbridge at grade A is supported. Echelon `unknown` is correct. The merge of
  "Stephen Burbridge" (VA076) with "Stephen Gano Burbridge" (KY011) is sound: US, Brigadier General,
  and the middle name is omitted.
- **GA023.** Both sides supported:
  - US: Corse arrived at 1 a.m., made the dispositions with post commandant Tourtellotte, and was
    in command before the 2 a.m. skirmish fire. His 30–40 minutes insensible is correctly not
    treated as a command change.
  - Confederate: French. Hood's `superior_directing` label rests on the chief-of-staff dispatch.
- **AL004.** Both sides correct:
  - US: rule 2 overturns the listing. Doolittle was "in command during my absence", Granger arrived
    "about 5 p. m., just as the fight was closing" on the 26th, and Doolittle says "The general
    commanding arrived at dark". Grade C, `command_changed` with successor Granger, and Granger as
    candidate all follow. The Doolittle passage-only registry entry is sound.
  - Confederate: Hood at grade A is consistent with the description ("his Army of Tennessee
    demonstrated").
- **TN032.**
  - US: rule 5, grade D is defensible. Sinclair: "Col. C. E. Thompson … was in command of the
    troops, and Lieutenant-Commander King of the gun-boats". No passage shows one officer over
    both. The only error is the F3 wording.
  - Confederate: Forrest supported.
- **TN034–TN036, TN038.** Supported:
  - Schofield held "the command of the troops immediately opposed to Hood" (Cox). Thomas's
    despatches are labelled at TN034 only, and Cox shows no direction from Thomas at Spring Hill or
    Franklin beyond pontoon requests.
  - Hood's army on every Confederate side.
  - At Nashville, Thomas.
- **TN037.** Supported:
  - US: Rousseau is "commanding all of the forces at Murfreesboro", with Milroy as a candidate.
  - Confederate: Forrest, with Hood as superior.
- **TN033.** Supported:
  - US: Gillem at brigade echelon ("Headquarters Brigade, Governor's Guard" matches `forces_text`).
  - Confederate: Breckinridge.
- **Merges used.** Horatio Wright / Horatio G. Wright (VA122) is merged on listing fields: US, Major
  General, middle initial omitted. The Schofield `passage_merges` entry (OK004 passage "Brig. Gen. John
  M. Schofield") is sound.
- **Nesting.**
  - MO026/MO025 `not_nested` and MO026/MO027 `not_nested` are supported by the MO025 and MO026
    descriptions.
  - TN034/TN035 `nesting_unresolved` is defensible. The Columbia description names Spring Hill as
    the next destination but narrates no fighting there, so the `nested` test is not met.

## Advisories (not required)

- **A1. VA121 US echelon.** `corps_or_wing` is inferred from Torbert directing two divisions. The
  rationale admits that no passage names his formation. Pond's casualty tables have a "Cavalry Corps"
  line but do not name Torbert as its commander. Consider `unknown`, or keep the inference as stated.
- **A2. VA076 Confederate candidates.** Burbridge's passages name "Echols, Williams, Vaughn, and, it
  is said, Breckinridge". The ledger records only Echols and Breckinridge. Either add passage-only
  entries for Williams and Vaughn, or state why they are excluded. Do not reuse the VA111 `cs-vaughn`
  entry on surname alone.

  Separately, the frozen and NPS descriptions say "On the morning of October 1, the Federals
  attacked" against the frozen October 2 interval. The rationale records Jackson's dispatch conflict
  but not this one.
- **A3. TN032 US.** If a later reviewer reads Sinclair's finding ("Colonel Thompson and Captain
  Howland are responsible for the destruction") and the description ("the Federals set fire to them")
  as showing the force that compelled the result, rule 5's second case would give Thompson at
  grade C. The rationale already records this alternative. Keep it visible.
- **A4. MO024 US.** Britton's "General Curtis, who was present on the field directing the general
  movements of his forces" (lexington-little-blue section, p.448) states Curtis's command more
  directly than the cited arrival sentence. Consider citing it.
- **A5. Records with identical intervals.** KS003, KS004 and MO028 share the interval 1864-10-25 in
  one campaign. `contained_pairs` excludes identical intervals, as in v1, so no nesting outcome is
  recorded. The descriptions treat them as separate actions (Mine Creek is "about six miles south of
  Trading Post, where the Marais de Cygnes engagement had occurred"). No double counting is evident,
  but views that include all three should know that they fall on one day with overlapping forces
  (Pleasonton's division and Marmaduke's and Fagan's divisions).
- **A6. If F1 is rejected**, at least add the Britton plan passage and the words "to divert the
  attention of the enemy" to the MO022 rationale. Also record the D alternative explicitly.

## Outcome

**Corrections required: F1, F2, F3.** Advisories: A1–A6.

F1 changes a responsible commander and a grade (MO022 Confederate, A→D). F2 changes a candidate's
registry identity and corrects rationale text (VA076 Confederate). F3 is a rationale-text correction
(TN032 US). The other 47 sides were checked and need no change.

This is a separate AI analysis within the scope stated above. It is not human historical
adjudication and not proof of source independence. It does not admit any feature, authorize any fit
or rating run, or change any frozen model input.
