# Command-responsibility ledger v2, batch 3 of 8: separate review

## Record

| Field | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`, a fresh-context subagent. The author's conversation was not an input. |
| Date | 2026-09-25 |
| Prepared commit reviewed | `11d4bc3168b83917a8efc233bf8d0bdc9ccbf372` (against `96110cf`) |
| Bundle commit (worktree HEAD) | `dddcefeb2b7adbe2b46607fb4128fed60b87319e` |
| `assignment.md` sha256 | `9bfa4b4e5787cdfc4241a09ad2cb33b52348e5dc5e4deb485fb77adaf24a5ce5` (verified) |
| `inputs.json` sha256 | `20dd666ac4408478002a6f1f08bccd5a047de96185b320a9a546a31f458959d0` (verified) |
| Outcome | **Corrections required**: C1–C6. Advisories A1–A10. |

**Input verification.** All 25 paths bound in `inputs.json` match their recorded sha256, both as
`git show 11d4bc3:<path>` and in this worktree. There are no mismatches. Key hashes:

- `data/command/responsibility-v2.json`: `1271ea87…753a`
- `data/command/commanders-v2.json`: `cdf72348…e8c`
- `data/raw/cwsac_battles.csv`: `952b5d08…f1f`
- `data/raw/cwsac_commanders.csv`: `6c587c29…00e`

**Documents the assignment names that `inputs.json` does not bind.** I read these and hashed them at
`11d4bc3`:

- `docs/commander-ratings.md`: `0ab4b7d541baf4f8e642634f316628f9cb372d68dcdbbc047a305f5a1fb704bb`
- `docs/ledgers-v2.md` (the scope addendum): `a7e05ddfc072c493f8f9152064e444e4b285e070a7dfcdbd279e80fc4aa49eb1`
- `docs/research/command-responsibility-v1.md`: `208b796a3f60ffc869a6686a12241a4356b4e94655128fb84bc88433dc33d0dd`
- `generalship/command.py`: `58ffe17ebc42cc3d2ec5950e55d56a243caf662460df86059c845ade62ef6954`

The assignment cites `docs/ledgers-v2.md`, but the manifest binds `docs/research/ledgers-v2.md`, the
extraction record (`e9986d9b…030`). I read both. The bundle should bind the addendum too.

For the 28 engagements, the bound dossier files match the ledger's `bindings.dossiers` hashes. The
checker verified this.

**Checks run (offline).**

- `make check`: exit 0. `Ran 143 tests … OK`.
- `python3 -m generalship command-check --ledger data/command/responsibility-v2.json`: exit 0.
  - 305 engagements, 610 sides.
  - Grades A 512, B 21, C 68, D 9.
  - 401 registry commanders.
  - Nesting: nested 4, not_nested 10, nesting_unresolved 2.
  - `rated: false`.

I ran no build, packet or evaluation commands. I modified nothing except this file, and did no
network access or new research.

## Coverage actually inspected

For all 28 assigned engagements, and both sides of each (56 sides), I read:

- the full ledger entry: choice, grade, rule, echelon, labels, candidates, successor, superior,
  citations and rationale;
- the frozen CWSAC listing rows (rank, navy);
- the frozen battle description and forces rows;
- the dossier's `responsibility` claim with its citations;
- the registry entries of every ID the batch uses. For passage-only and merged entries, I also read
  the citation or basis.

I computed contained-interval pairs with `generalship.command.contained_pairs`. Only LA010 ⊃ LA009
involves this batch.

**Source sections I opened and read around the cited quotes:**

- `or15-davis-galveston-selections-v2` (Davis report)
- `britton-border-1-marmaduke-1863-first-selections-v1` `hartville` (whole section)
- `orn13-mccrady-fort-mcallister-selections-v1`
- `or14-beauregard-charleston-harbor-selections-v1`, both sections
- `jones-charleston-1863-selections-v1`:
  - `morris-island-july-10-11`
  - `wagner-july-18`
  - `grimballs-landing-july-16`
  - `wagner-siege-and-evacuation`
  - `sumter-assault-and-second-bombardment`
- `irwin-west-louisiana-1863-selections-v1` `irish-bend`, `opelousas-vermilion`
- `irwin-taylor-louisiana-1863-selections-v1` `harrowing-la-fourche`, `fordoche`
- `irwin-port-hudson-selections-v1` `plains-store`
- `britton-indian-territory-1863-selections-v1` `cabin-creek`
- `or22-1-williams-cabin-creek-selections-v1`
- `or22-1-price-little-rock-selections-v1` `price-1863-11-20`
- `or26-1-dowling-sabine-pass-selections-v1`
- `or26-1-crocker-sabine-pass-selections-v1`
- `or26-1-green-louisiana-selections-v1`
- `britton-indian-territory-north-1863-selections-v1` `baxter-springs`

For the remaining cited sections, I judged the reading from the quoted text and the dossier's
statement of the passage, not from the surrounding section. The checker confirms that those quotes
occur. These are:

- the Magruder, Drayton, Du Pont and Gillmore reports;
- Irwin `bisland`, `twenty-seventh-of-may` and `surrender`;
- the Taylor, McNeil, Marmaduke, Vandever, Stickney, Cooper, Cabell, Davidson, Clayton, Ewing,
  Quantrill, Semmes and Westcott reports;
- Britton `springfield`, `honey-springs`, `backbone-mountain` and `lawrence`.

The 91 carried-forward v1 entries were out of scope.

## Required corrections

### C1. MO019 US: the rationale misdates Merrill's arrival

- **Problem.** The rationale says Merrill's column "reached Hartville only on the 11th". Britton's
  cited `hartville` section says the column left Houston at noon on the 9th, "where they arrived the
  next morning at sunrise", which is the 10th. It then camped nine miles west and fought on the 11th.
- **Grade.** The grade is unaffected. No passage states Merrill's command at the 9th's garrison
  capture, so B stands.
- **Change.** In `engagements[MO019].sides.US.rationale`, replace "reached Hartville only on the
  11th" with: "reached Hartville on the morning of the 10th, after the garrison's capture on the
  9th (Britton: 'where they arrived the next morning at sunrise'), and fought there on the 11th".
- **Citations.** None change. Grade B cites only the listing.

### C2. SC004 Confederate: `superior_directing` rests on a truncated quote

- **Problem.** The superior citation ends at "…concentration at strategic points in this vicinity of
  all available troops". Beauregard's sentence continues "for the defense of the several land
  approaches to the position". The same report says the Union land forces "made no attempt to
  co-operate actually with the naval attack."
- **Why it matters.** The passage shows land-front precautions, not direction of the April 7 harbor
  engagement. The rationale itself concedes that "the inspected passages do not show him directing
  the fight itself". SC005 declines the label on comparable allocation evidence.
- **Changes to `engagements[SC004].sides.Confederate`:**
  - `labels` → `["responsibility_unresolved"]`
  - `superior` → `null`
  - `superior_citations` → `[]`
- **Rationale.** Replace the sentence "Beauregard ordered the concentration … directing the fight
  itself." with: "Beauregard's precautions concentrated troops 'for the defense of the several land
  approaches to the position', and the Union land forces 'made no attempt to co-operate actually
  with the naval attack'. No inspected passage shows him directing the April 7 harbor engagement, so
  superior_directing is not recorded (as at SC005)."
- **Unchanged.** Ripley (grade C) and candidate Beauregard stay as they are.

### C3. LA008 US: the second superior citation is about a different operation

- **Problem.** "From New Iberia Banks ordered Grover to send a detachment" introduces Kimball's
  expedition to the Avery salt-works on Petit Anse Island. Irwin: "to destroy the famous Avery
  salt-works… On the 17th of April, Grover accordingly despatched Kimball on this errand". That was
  not the Vermilion engagement.
- **Evidence for the label.** The frozen description directly supports `superior_directing: Banks`.
- **Change 1.** Replace `superior_citations[1]` with
  `{"source_id": "arnold-cwsac-battles", "row_key": {"battle": "LA008"}, "column": "description", "quote": "Banks, in pursuit, sent two columns, on different roads, toward Vermillion Bayou on the morning of April 17.", "battle_id": "LA008"}`
  (verified to resolve).
- **Change 2.** In the rationale, replace "Banks directed the pursuit and ordered Grover's
  detachments" with: "Banks directed the pursuit and sent two columns toward Vermillion Bayou on the
  17th (description); he himself marched by Saint Martinsville".

### C4. OK006 US: grade A is not supported at first combat

- **Problem.** No inspected passage states that Williams commanded the side's engaged forces when the
  fighting began, about noon on July 1.
- **Evidence:**
  - Williams: "I concluded to accompany this train on the route," (p.379). He names
    "Lieutenant-Colonel [Theodore H.] Dodd, commanding escort to the train,".
  - Britton: "The escort to the train was commanded by Lieutenant-Colonel Theo dore H. Dodd, Second
    Colorado Infantry" (p.94). This escort included Foreman's detachment, which made the first
    contact.
  - Both say the forces were united "under him" only that evening. Britton: "to unite under him all
    the troops that could be spared from the immediate defence of the train" (p.96).
  - "the ranking officer present" states rank, not command.
  - The frozen description has Williams leading the train: "Col. James M. Williams of the First
    Kansas Colored Infantry led a Union supply train from Fort Scott, Kansas, to Fort Gibson,
    Oklahoma (then Indian Territory)."
- **Reading.** The sources therefore disagree about who commanded the train force at first combat. No
  passage names Dodd over all the engaged forces either: Williams's own howitzer also fired. So the
  listed Williams stays.
- **Rule.** Grade table: C when "inspected sources disagree about who commanded". Checker: rule 2
  with grade C needs the label.
- **Changes to `engagements[OK006].sides.US`:**
  - `grade` → `"C"`
  - `labels` → `["responsibility_unresolved"]`
  - `candidates` → `["us-theodore-h-dodd"]`
- **Citations to add.** All verified to resolve:
  - `{"dossier": {"claim_id": "command-roles", "citation_index": 1}, "source_id": "or22-1-williams-cabin-creek-selections-v1", "quote": "Lieutenant-Colonel [Theodore H.] Dodd, commanding escort to the train,", "battle_id": "OK006"}`
  - `{"source_id": "or22-1-williams-cabin-creek-selections-v1", "section": "williams-1863-07", "locator": "p.379 (OCR page markers; not checked against print)", "quote": "I concluded to accompany this train on the route,", "battle_id": "OK006"}`
  - `{"source_id": "britton-indian-territory-1863-selections-v1", "section": "cabin-creek", "locator": "p.96 (OCR page markers; not checked against print)", "quote": "to unite under him all the troops that could be spared from the immediate defence of the train", "battle_id": "OK006"}`
  - `{"source_id": "arnold-cwsac-battles", "row_key": {"battle": "OK006"}, "column": "description", "quote": "Col. James M. Williams of the First Kansas Colored Infantry led a Union supply train from Fort Scott, Kansas, to Fort Gibson, Oklahoma (then Indian Territory).", "battle_id": "OK006"}`
- **Rationale.** Replace the last sentence with: "At first contact on July 1 the escort, including
  Foreman's skirmishers, was under Dodd, and Williams accompanied the train with his own regiment and
  section; the forces were united under Williams only that evening. The description has Williams
  leading the train. Sources disagree about who commanded at first combat and no passage names
  another officer over all the engaged forces, so the listed Williams is kept (rule 2, grade C,
  responsibility_unresolved, Dodd as candidate)."
- **Registry entry to add to `commanders-v2.json`:**
  `{"id": "us-theodore-h-dodd", "name": "Theodore H. Dodd", "side": "US", "cwsac_names": [], "passage_citation": {"dossier": {"claim_id": "command-roles", "citation_index": 1}, "source_id": "or22-1-williams-cabin-creek-selections-v1", "quote": "Lieutenant-Colonel [Theodore H.] Dodd, commanding escort to the train,", "battle_id": "OK006"}}`
- **Echelon.** It stays `unknown`.

### C5. Registry `cs-johnson-hagood`: the merge basis misstates its cited quote

- **Problem.** The `passage_merges[0].basis` says "the passage names 'General Johnson Hagood'".
  However, the cited quote is "General Hagood relieved General Taliaferro in command of Wagner…",
  which is surname only.
- **Evidence for the merge.** The full name appears in a Jones section the SC007 dossier cites
  (`reported-force-scope` #7, `wagner-siege-and-evacuation`).
- **Change 1.** Replace the `citation` with
  `{"dossier": {"claim_id": "reported-force-scope", "citation_index": 7}, "source_id": "jones-charleston-1863-selections-v1", "quote": "commanded succes- sively by Brigadier Generals Taliaferro, Johnson Hagood, A. H. Colquitt, and T. L. Clingman", "battle_id": "SC007"}`
  (verified).
- **Change 2.** Set `basis` to: "the passage names Brigadier Generals 'Taliaferro, Johnson Hagood, …'
  as successive commanders on Morris Island, matching the listed Johnson Hagood; the same history's
  'General Hagood relieved General Taliaferro in command of Wagner' names that officer".
- **Unchanged.** The SC007 successor stays `cs-johnson-hagood`.

### C6. Registry `cs-william-b-taliaferro`: the passage citation does not name the officer

- **Problem.** The quote "he was assigned to the com- mand of Battery Wagner on the 13th." does not
  contain the name the entry asserts. The full name appears in the preceding sentence of the same
  cited section.
- **Change.** Set `passage_citation.quote` to "Brigadier General William B. Taliaferro, who was on duty
  at Savannah when the descent was made on Morris Island". Keep the same dossier reference
  (`reported-force-scope` #2, `wagner-july-18`; verified).

After applying C4–C6, the registry and ledger bindings need re-hashing, and `command-check` needs to be
re-run.

## Advisories (not required)

**A1. Surname-only identities for superiors and successors (systemic, cross-batch).**

- In this batch, three IDs rest on a surname-only passage, with no full name or initials in that
  engagement's own listing, description or cited sections:
  - LA007 Confederate successor `cs-alfred-mouton` (Irwin: "Mouton rode up");
  - OK006 Confederate superior `cs-douglas-h-cooper` (Britton: "General Cooper");
  - LA009 Confederate superior `cs-franklin-gardner` (Irwin: "Gardner sent out Miles").
- The addendum keeps surname-only name matches separate. The other superiors in this batch have a
  full name in the engagement's own description or report (Du Pont, Banks, Taylor, Mouton at
  LA013/LA016, Steele, Price, Blunt, Emory).
- Across the new entries, 99 sides map a successor or superior to a listed ID from another
  engagement. Because the practice is systemic, I have not made it a batch-local correction. The
  primary should decide it once across all batches: either passage-only IDs such as `cs-mouton` and
  `cs-cooper`, or a documented contextual-identity rule.

**A2. SC009 Confederate grade A is thin.**

- The only stating passage is that Elliott "forwarded the demand to General Beauregard, who replied…".
  That shows Beauregard's authority over Sumter's surrender. It does not show his command of the works
  engaged first: the Moultrie and Sullivan's Island batteries on the evening of the 7th.
- Jones, a source the dossier already cites, puts those works in Ripley's First Military Division
  ("Brigadier General Ripley commanding"). That passage is dated July 10, not September 7.
- GA002 Confederate applied a stricter "implies but does not state" standard, which gave B. Consider B
  for consistency, and record Ripley in the rationale.

**A3. SC009 US: `us-quincy-gilmore` is kept separate from `us-quincy-a-gillmore`.**

The surnames differ (Gilmore vs Gillmore), so the stated listing-field rule correctly keeps them apart.
The SC009 passages all name "General Gillmore". If a merge is wanted, it needs an explicit passage
basis. As it stands, the ID is only a candidate here.

**A4. SC004 Confederate: a stronger citation is available for Ripley.**

Beauregard's October 15 report, in a section the dossier cites, names "Brig. Gen. E. S. Eipley, Col. William Butler, and Col. Alfred Bliett, who commanded at that period respect- ively in this military district the batteries on Sullivan’s Island and Fort Sumter" (OCR as printed: "Eipley" for Ripley,
"Bliett" for Rhett). Citing it would strengthen Ripley's
command. The grade stays C.

**A5. SC005 US: an uncited Jones passage.**

Jones says the Federal losses were reported by "General Strong, who commanded in person on both
occasions". This is subordinate context under rule 2, but the rationale does not mention it. Adding
it would keep the passage visible.

**A6. TX006 Confederate: Odlum's role.**

Dowling reports the works were "visited by Capt. F. H. Odium, commanding post" (OCR "Odium"; the signature block reads "Odlum"), and addresses the
report to him. No inspected passage shows Odlum directing, so leaving the label off is right. The
rationale already flags this. Recording Odlum as context in the rationale is enough.

**A7. LA009 Confederate: Powers's identity and Irwin's sequence.**

- **Identity.** It rests on the description ("Col. Frank P. Powers"). Irwin's "Colonel S. P. Powers
  of the 14th Arkansas" is linked by the event, not by the name. The rationale says so.
- **Sequence.** Irwin also frames "the battle of Plains Store" as the action brought on by Miles's
  sortie, which differs from the description's sequence. First contact is still Powers's in both.

**A8. Echelons that could be less `unknown`.**

- AR011 Confederate: the frozen forces field reads "division", and MO020 and AR007 give Marmaduke
  `division`.
- MO019 US: the forces field reads "Detachment of infantry, cavalry, and artillery".

`unknown` is permitted, so this is optional.

**A9. Superior labels resting on "sent the expedition".**

LA012 Confederate (Taylor), OK006 Confederate (Cooper) and GA002 US (Du Pont ordered the attack)
follow the MS001 precedent of a superior ordering the operation from within the theater. They are
acceptable. The reviews should apply the same threshold in every batch.

**A10. Bundle manifest.**

`inputs.json` omits four documents the assignment names: `docs/commander-ratings.md`,
`docs/ledgers-v2.md`, `docs/research/command-responsibility-v1.md` and `generalship/command.py`. Their
hashes at `11d4bc3` are listed above. Future bundles should bind them.

## Entries checked without findings

- TX003: US D, rule 5 third case; Confederate Magruder A.
- MO018: Brown A with `command_changed` → Crabb; Marmaduke A.
- MO019 Confederate.
- GA002: Drayton A with superior Du Pont; Anderson B.
- SC005: Gillmore A; Graham C, candidate Beauregard.
- SC007: Gillmore A; Taliaferro C, with `command_changed` → Hagood, `superior_directing` Beauregard,
  candidate Beauregard.
- SC009 US: Dahlgren C, candidate Gilmore.
- LA006: Banks A; Taylor A.
- LA007: Grover A; Taylor A with `command_changed` → Mouton.
- LA008 Confederate.
- MO020, AR007.
- LA009: Augur A with superior Banks; Powers A under rule 3(a), candidate Miles, superior Gardner.
- LA010: Banks A; Gardner A.
- LA012, LA013.
- LA015: Grover A under rule 3(a), candidate Weitzel; Green A.
- LA016: Leake C, candidate and superior Dana; Green A with superior Mouton.
- OK006 Confederate: Watie A with superior Cooper.
- OK007, AR009.
- KS001: US D under rule 6; Quantrill A.
- TX006: Crocker C with `joint_command`, candidate Franklin; Dowling A.
- AR010: Davidson A with superior Steele; Dobbin C with `command_changed` → Marmaduke, candidate
  Marmaduke, superior Price.

  The AR010 Confederate reading follows the design's definition of first combat: "the side's first
  combat within the frozen interval". Price's report dates Dobbin's contest of the crossing to
  "Early on the morning of the 10th", before Marmaduke was sent across.
- AR011.
- KS002: Pond A under rule 3(a), candidate Blunt; Quantrill A.
- FL004.

**Nesting.** For LA010 ⊃ LA009, `nested` is right. The frozen forces fields place the 1st Division,
XIX Corps, and the Port Hudson garrison detachment inside LA010's force scope. The reason also keeps
the separate casualty accounting visible.

**Merges used by this batch.** These are sound:

- the `us-quincy-a-gillmore` merge of "Qunicy Gillmore" and "Quincy Gillmore" (listing fields);
- `cs-alfred-mouton` ← "Jean Alfred Mouton" (LA013 description; the given name contains the listed
  one);
- `us-frederick-steele` ← "Fred Steele";
- `us-christopher-c-augur` ← "C. C. Augur".

## Scope statement

This is an AI review of the ledger's extraction against the passages the design allows. It is not
human historical adjudication, independent corroboration or proof of source independence. It admits
no feature, authorizes no evaluation or rating fit, and changes no frozen model input. The primary
should check each finding against its passage before applying it.
