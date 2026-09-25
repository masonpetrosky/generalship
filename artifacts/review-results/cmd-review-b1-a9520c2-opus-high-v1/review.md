# Command-responsibility ledger: separate review, batch 1 of 4

**Outcome: corrections required.** There are seven required corrections (B1-R1 to B1-R7) and
seven advisories (B1-A1 to B1-A7).

## Record

| Field | Value |
| --- | --- |
| Reviewer | Separate `evidence-reviewer` subagent, started with fresh context. The author's conversation was not an input. |
| Model and effort | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high` |
| Date | 2026-09-25 |
| Prepared commit reviewed | `a9520c2d5628c25b49437f4f54bfc78268a85393`, against `16a32116067912a1b5cb380097d75092a2a430b4` |
| Worktree HEAD (assignment bundle) | `cb8747415ceef74ec979bd11b63542f1c81fb4d7`. It adds only `assignment.md` and `inputs.json` to `a9520c2`. |
| Assignment | `assignment.md`, sha256 `cd6ad99ac3347999e3721b5690f4671116c6ea342698989a91368937b816d4b2` (verified) |
| Input manifest | `inputs.json`, sha256 `11f34d78cb94fd48165b789ec37c0e0ff8ad82f6acee3d1d7e90581f9b5e3a62` (verified) |
| Input hashes | All 24 paths match both `git show a9520c2:<path>` and the worktree. There were **0 mismatches**. |
| Design read | `docs/commander-ratings.md`, sha256 `0ab4b7d5…04bb`. It is not in the manifest, but it is unchanged between `a9520c2` and HEAD. The ledger's `bindings.design` hash is replayed by the checker. |

**Commands run (offline).**

- `make check`: exit 0, 126 tests OK. The embedded command-check reported 91 engagements and
  182 sides, graded A 149, B 15, C 15 and D 3. Nesting was 2 nested, 6 not nested and
  1 unresolved.
- `python3 -m generalship command-check`: the same result.

I ran no build, packet, evaluation or network commands. To confirm that the replacement quotes
below pass the checker, I applied them **in memory only** and ran `command.check(ledger=…)`.
With R1–R6 and the R7 superior citation applied, it passes: A 152, B 12, C 15, D 3. The one
extra step was binding the source `or7-thomas-selections-v1` in `bindings.cited_sources`
(metadata and raw digests from `verify_sources`). Separately, `resolve` confirms the R7 registry
quote. No primary file was modified.

## Scope actually inspected

**Documents and code.** I read the following:

- AGENTS.md;
- the design, §§1–8 in full (§2 closely);
- the ledger memo;
- `generalship/command.py` and `citation_text` in `generalship/evidence.py`.

**Ledger entries.** For all 25 assigned engagements and both sides (50 sides), I read the full
ledger entry: choice, rule, grade, labels, candidates, successor, superior, echelon, citations
and rationale.

**Listings and registry.** I checked each side against:

- its frozen CWSAC description;
- its CWSAC commander rows (rank and `navy` fields);
- the registry entries for all 55 commander IDs involved, including merge bases and passage-only
  citations.

**Dossiers and sources.** I read every `responsibility` claim in the 25 bound dossiers, and
listed every source each dossier cites. I read the surrounding text of these cited sections in
full:

- **NPS pages:** NC002, NC004, VA012 and its Drewry history, TN002, KY006, VA102 (heading),
  VA103, VA013 and TN005;
- **Woodbury:** all sections (Roanoke, New Bern, Fort Macon, Tranter's Creek);
- **Grant memoir selections:** rows 392–445 (Henry, Donelson);
- **Allan:** all battle sections (Kernstown, McDowell, Front Royal, Winchester, Cross Keys,
  Port Republic);
- **Webb:** Hanover, Beaver Dam, Gaines' Mill and Malvern sections;
- **Mahan:** Island No. 10 and Memphis sections;
- **Cist:** Chattanooga section;
- **Thomas's report:** the opening-combat portion;
- **Garfield's reports:** keyword passages.

**Nesting.** I recomputed contained-interval pairs over the whole cohort. Only NC004⊃NC005 and
VA018⊃VA017 touch assigned records. Each involves an inconclusive record, which is out of scope,
so no in-scope nesting pair involves an assigned engagement. The ledger's nine recorded pairs
are correct in that respect.

**Not inspected.** I did not inspect the following:

- other batches' engagements;
- TN003 beyond its ledger-cited passages and the design's parked Shiloh provenance questions;
- print editions (all OCR caveats in the sources stand);
- any source outside the dossiers' cited families.

## Required corrections

Each correction gives the engagement, side, field and new value, and quotes the passage that
supports it. Quotes are verbatim from the registered source, OCR errors included. The quotes for
R1–R7 pass the checker in memory, as described above.

### B1-R1: VA102 US. Schenck took command after the first combat (rule 4)

**The misreading.** The ledger reads Allan's "who, as senior, **now** commanded" as command when
the fighting began. Allan's own sequence says otherwise:

- Milroy directed the first Federal combat. His skirmishers and artillery engaged the
  Confederate reconnoitring party on Sitlington's hill.
- "While the Confederates were thus employed", Milroy "had been reinforced by the arrival of
  Schenck's brigade".
- Only then did Schenck, "as senior, now" command, and approve the assault.

**Dating.** The reconnaissance, the planned night flanking march for "the morrow" and the
assault fall on one day in Allan's narrative. That day is May 8, from the frozen description.

This is rule 4's case of "a superior arriving and taking command after the first combat". The
live NPS heading also lists only Milroy: "Brigadier General Robert Milroy [US]".

**Replacement** (`engagements[VA102].sides.US`):

- `commander_id`: `"us-robert-milroy"`
- `rule`: `"3a"`
- `grade`: `"A"`
- `echelon`: `"brigade"`
- `labels`: `["command_changed"]`
- `successor`: `"us-robert-schenck"`
- `candidates`: `["us-robert-schenck"]`
- `citations`:
  - Both listing rank rows ("Brigadier General").
  - Three quotes via `{"dossier": {"claim_id": "senior-command-and-attack", "citation_index": 0}}`,
    source `allan-valley-selections-v1`:
    - "Gen. Milroy sent out parties of skirmishers through tlie forest which covered the western side and base of Sitlington's hill, and also opened witli a section of artillery"
    - "IVIilroy had been reinforced by the arrival of Schenck's brigade"
    - "with the approval of Gen. Schenck, who, as senior, now com-"
  - `arnold-cwsac-battles` VA102 `description`: "Milroy seized the initiative and assaulted the
    Confederate position on Sitlington's Hill".
- `rationale`: "Both listed brigadier generals. Allan has Milroy's skirmishers and artillery
  engage the Confederate reconnaissance, then Milroy 'reinforced by the arrival of Schenck's
  brigade', after which Schenck 'as senior, now commanded' and approved the assault (rule 3(a);
  rule 4, successor Schenck). The skirmish is not separately dated in the selection; the
  same-day sequence rests on Allan's narrative and the May 8 frozen interval."

### B1-R2: TN002 Confederate. The inspected command transfer needs `command_changed`

The ledger's own citation shows a change of command within the interval. Grant row 425 opens
with the council held after the failed breakout: "A council of war was held by the enemy at which
all agreed that it would be impossible to hold out longer." He then writes "Floyd turned over the
command to Pillow, who declined it. It then devolved upon Buckner". Row 444 dates the flight to
"the night of the 15th", after the side's first combat.

Whoever commanded at first combat, Buckner did not: the command "devolved upon" him at the end.
Rule 4 therefore applies even though rule 3(c) leaves the first commander unresolved.

**Replacement** (`engagements[TN002].sides.Confederate`):

- `labels`: `["responsibility_unresolved", "command_changed"]`
- `successor`: `"cs-simon-b-buckner"`
- Keep `grade: "D"`, `commander_id: null` and all three candidates.
- Add a citation via `{"dossier": {"claim_id": "confederate-command-transfer",
  "citation_index": 0}}` (`grant-memoirs-river-selections-v1`): "A council of war was held by the
  enemy at which all agreed that it would be impossible to hold out longer."
- Append to `rationale`: "The transfer to Buckner followed the council after the failed
  breakout, so a command change within the interval is shown (rule 4, successor Buckner) although
  the commander at first combat is unresolved."

### B1-R3: NC004 US. `superior_directing` for Burnside

Woodbury, which the dossier cites (section `fort-macon-siege`), shows Burnside directing this
operation in the theater and present at its end:

- he "therefore decided to make a com- plete investment of the fort, and, by a combined attack by
  land and sea, force its surrender";
- he was "as fre- quently at Beaufort and Carolina City as affairs at Newbern permitted";
- "General Burnslde, who was now present and desired to prevent a loss of life, again sum- moned
  Colonel White to surrender".

The frozen description says "Maj. Gen. Ambrose E. Burnside's army advanced on Fort Macon". This is
a superior directing, not a contradiction of the Parke listing (rule 2, second bullet). It is a
stronger case than the ledger's own labels at NC006 (Potter) and TN005 (Mitchel).

**Replacement** (`engagements[NC004].sides.US`):

- `labels`: `["superior_directing"]`
- `superior`: `"us-ambrose-e-burnside"`
- `superior_citations`: two quotes via `{"dossier": {"claim_id": "assigned-siege-command",
  "citation_index": 0}}` (`woodbury-burnside-selections-v1`):
  - "General Burnside therefore decided to make a com- plete investment of the fort, and, by a combined attack by land and sea, force its surrender."
  - "General Burnslde, who was now present and desired to prevent a loss of life, again sum- moned Colonel White to surrender"
- Keep Parke, grade A.
- Append to `rationale`: "Burnside decided the investment and combined attack and was present to
  summon the surrender (superior_directing: Burnside)."

### B1-R4: NC004 Confederate. Grade B→A, because a dossier-cited passage states White's command

The ledger says only the NPS heading names White. In the same Woodbury section (already cited by
the dossier), White is:

- the commandant summoned to surrender;
- the officer who "marched out his command, and surrendered to General Parke the fort which he
  had so persistently defended".

That states his command of the defending garrison throughout the siege. Nothing inspected
contradicts it.

**Replacement** (`engagements[NC004].sides.Confederate`):

- `grade`: `"A"`
- Add a citation via `{"dossier": {"claim_id": "assigned-siege-command",
  "citation_index": 0}}` (`woodbury-burnside-selections-v1`): "Colonel White hung out the white
  flag, obtained honorable terms of capitula- tion, marched out his command, and surrendered to
  General Parke the fort which he had so persistently defended."
- `rationale`: "A cited passage states the command (Woodbury: White marched out his command and
  surrendered the fort he had defended). Woodbury's 'Colonel' differs from the listed rank
  'Lieutenant Colonel'; identity is not in doubt."

### B1-R5: KY006 US. Grade B→A, because Thomas's report states his command at the first combat

The ledger's rationale says "no inspected passage states or contradicts the command". Thomas's
report of January 31, cited by the dossier, gives this sequence:

- The brigade commander Manson "informed me in person that the enemy were advancing in force".
- Thomas then "directed him to join his brigade im- mediately and hold the enemy in check until I
  could order up the other troops".

The frozen description adds: "The Rebels attacked Thomas at Logan's Crossroads at dawn on January
19."

**Replacement** (`engagements[KY006].sides.US`):

- `grade`: `"A"`
- Add a citation via `{"dossier": {"claim_id": "warning-and-command-chain",
  "citation_index": 1}}` (`or7-thomas-selections-v1`): "I directed him to join his brigade im-
  mediately and hold the enemy in check until I could order up the other troops".
- Add a citation from `arnold-cwsac-battles` KY006 `description`: "The Rebels attacked Thomas at
  Logan's Crossroads at dawn on January 19."
- `rationale`: "A cited passage states the command."
- Add `or7-thomas-selections-v1` to `bindings.cited_sources`.

### B1-R6: VA013 Confederate. Grade B→A and echelon `brigade`, because Webb states Branch's command at first contact

Webb (section `hanover-contact-and-support`, cited by the dossier) describes the opening
collision: "About noon, the cavalry … encountered a portion of Branch's brigade". The 25th New
York then "came in direct col- lision with a portion of Branch's command". Later the Federals
faced "Branch's whole command" and "Branch's large brigade".

**Replacement** (`engagements[VA013].sides.Confederate`):

- `grade`: `"A"`
- `echelon`: `"brigade"`
- Add two citations via `{"dossier": {"claim_id": "porter-and-martindale",
  "citation_index": 0}}` (`webb-peninsula-selections-v1`):
  - "came in direct col- lision with a portion of Branch's command"
  - "Branch's large brigade"
- `rationale`: "A cited passage states the command."

### B1-R7: Registry `us-ormsby-mitchel`. The passage citation does not name the officer; TN005 US cites no passage naming the superior

The registry entry's `passage_citation.quote` is "for an expedition against Chattanooga under the
command of Negley." That quote names Negley, not Mitchel. A passage-only identity must rest on a
passage that names the officer (design §2, identity registry).

The TN005 US ledger side labels Mitchel `superior_directing`, but none of its quotes names him.
The NPS quote begins "he ordered".

**Replacements:**

- **Registry** (`us-ormsby-mitchel.passage_citation.quote`, same dossier reference
  `command-roles` index 3, `cist-heartland-selections-v1`): "On May 29th, Mitchel concentrated
  Negley's command from Columbia". The quote occurs in the cited section. The registry hash
  binding in the ledger must then be updated.
- **Ledger** (`engagements[TN005].sides.US.superior_citations`): add `arnold-cwsac-battles`
  TN005 `description`: "After Mitchel received command of all Federal troops between Nashville
  and Huntsville, on May 29, he ordered Brig. Gen. James Negley with a small division to lead an
  expedition to capture Chattanooga."

## Advisories (not required)

- **B1-A1. MO012 US: record the rule-5 dispute.** The ledger bases its rule-5 choice on the
  frozen description (Pope's crossing). Mahan, cited by the dossier, says "At ten o'clock that
  evening the island and garrison surrendered to the navy". That is the same kind of wording the
  ledger treats as decisive for Foote at TN001.
  - The Pope choice is still well supported. Mahan also says "New Madrid, with its works, was taken
    by General Pope before the arrival of the flotilla", so the side's first combat within the
    interval was army-only. The frozen description and Mahan also put the 7,000 men "caught between
    the swamps and the river" after the army's crossing.
  - Suggested change: add both Mahan quotes. Use `surrender-date-and-scope-difference` index 2
    and `river-bends-and-escape-route` index 0; both pass the checker. Note the dispute in the
    rationale. The grade stays C with Foote as a candidate.
- **B1-A2. Apply one `superior_directing` standard.** TN005 (Mitchel, who ordered the expedition
  from Huntsville) and NC006 (Potter, who ordered a reconnaissance) are labelled. KY005 has the
  same pattern but no label: "Union Brig. Gen. Don Carlos Buell directed Col. James Garfield to
  force Marshall to retreat". KY006 is similar: Thomas is "carrying out the instruc- tions of the
  general commanding the department".
  - The design excludes "a departmental or national superior who was not directing this operation
    in the field".
  - Either keep labels only where the superior directs the operation in the field (as NC004 now
    does under B1-R3, and as MS001 does), or label the KY005 Buell case as well. Record which
    standard is used.
- **B1-A3. VA103 and VA104 Confederate (Jackson, grade B).** Allan's cited sections contain
  command evidence that the rationales do not mention:
  - VA103: "Col. Crutchfield, chief of artillery for Jackson" during the Front Royal fight, and
    "Gen. Jack- son, without waiting for more, dashed with this force up the turnpike".
  - VA104: "These orders (to move on Winchester), Gen. Trimble says, were sent by Jackson" to
    Ewell's division. This is secondhand and dated the day before.
  - These may support grade A. B is defensible, but the VA104 rationale should say that a
    passage shows Jackson ordering Ewell's division.
- **B1-A4. KY005 Confederate: stronger dated citation.** Garfield's report of January 11 gives
  the command on the battle day: "we moved toward the main body of the enemy at tbe Forks of
  Middle Creek, under command of Mar- shall." The ledger's current quote ("led another force into
  southeast Kentucky") describes events a month earlier.
- **B1-A5. Echelons.** Only where the listed passages support it:
  - KY006 US `division`: forces_text "1st Division, Army of the Ohio, and Brig. Gen. A. Schoepf's
    Brigade", and the report heading "Flbst Division".
  - VA106 Confederate `army`: "freeing his army to reinforce Lee".
  - NC006 US `detachment_or_post` instead of `regiment`. Woodbury gives a mixed force: "Eight
    companies of the 24th Massachusetts under Lieutenant Colonel F. A. Osborn, a squadron of
    Colonel Mix's cavalry and a battery of two steel Wiard guns".
  - `unknown` remains acceptable in each case.
- **B1-A6. NC006 US.** The Potter quote sits in `citations`, not `superior_citations`. GA003,
  TN021 and TN028 put the superior's quote in `superior_citations`. Consider moving it for
  consistency. The checker allows either.
- **B1-A7. Follow-on updates.** After the corrections, regenerate the memo's counts:
  - grades become A 152, B 12, C 15, D 3;
  - `command_changed` rises by 2 (VA102 US, TN002 CS);
  - `superior_directing` rises by 1 (NC004 US);
  - check whether VA102 is a primary row that changes the commander table (Milroy for Schenck).

## Sides checked with no correction

For each side below, the choice, grade, labels, candidates, echelon and citation support were
checked against the evidence listed above. I agree with each, subject to any advisory noted.

- **KY005:** US Garfield (A, brigade). Confederate Marshall (A; see B1-A4).
- **KY006:** Confederate Crittenden (A, army).
- **TN001:**
  - US Foote (C, rule 5 second case). Supported further by Grant row 401: the troops "were
    delayed … This delay made no difference in the result."
  - Confederate Tilghman (A). Grant row 401 says "Tilghman had sent his entire command, with the
    exception of about one hundred men left to man the guns".
- **NC002:**
  - US Burnside (A).
  - Confederate Shaw (C, `responsibility_unresolved`, Wise as candidate). The rule 2
    contradiction and grade are correctly applied. Woodbury adds context but no listed officer:
    the US Flag Officer's gunboats and a Confederate fleet "under the command of Captain W. F.
    Lynch" engaged on Feb 7.
- **TN002:** US Grant (C, rule 5 second case, army).
- **MO012:**
  - US Pope (see B1-A1).
  - Confederate McCown (A, 3(a), `command_changed` to Mackall).
- **NC003:** US Burnside (A). Confederate Branch (A).
- **NC004:** US Parke (A; see B1-R3 for the label).
- **VA101:**
  - US Kimball (A). Shields only receives reports in the inspected text, so no
    `superior_directing` label is needed.
  - Confederate Jackson (A, division).
- **TN003:** both sides (A; Johnston to Beauregard, `command_changed`). Checked on their cited
  passages only, per the parked Shiloh scope.
- **MS016:** US Halleck (A; field command assumed April 11, before the interval). Confederate
  Beauregard (A).
- **VA102:** Confederate Jackson (A, army).
- **VA012:**
  - US Rodgers (A, flotilla).
  - Confederate Farrand (C, rule 5 second case with 3(a)), as the design anticipates. The park
    history names only Farrand, and none of the other three listed officers appears in the
    inspected text.
- **WV009:** US Cox (A). Confederate Marshall (A, army; the registry merge of "Humphery" and
  "Humphrey" is sound on the listing fields).
- **VA103:** US Kenly (A, detachment_or_post; Allan: "The Federal com- mander").
- **VA104:** US Banks (A, army).
- **VA013:** US Porter (A, corps; Webb: "the corps commander").
- **NC006:**
  - US Osborn (A, `superior_directing` Potter).
  - Confederate Singletary (A, `command_changed`, successor null because none is named).
- **TN004:**
  - US: grade D, `joint_command`. Mahan credits both the rams and the gunboats.
  - Confederate Montgomery (C, flotilla).
- **TN005:**
  - US Negley (A).
  - Confederate Leadbetter (C, `responsibility_unresolved`). No passage says Kirby Smith took
    command on arriving on the 8th, so `command_changed` is correctly absent.
- **VA105:** US Frémont (A, army). Confederate Ewell (A, division; Allan: "Ewell carefully
  disposed his troops").
- **VA106:** US Tyler (A). Confederate Jackson (A; Allan: Jackson "ordered an attack upon
  Tyler").
- **VA016, VA017:** US Porter (A, corps). Confederate Lee (A, army).
- **VA021:** US McClellan (A). Confederate Lee (A).

**Registry.** The passage-only entries Shaw, Leadbetter and Potter are sound. Mitchel is not (see
B1-R7). The merges "Lawrence O'B." / "O'Bryan Branch" and "Humphery" / "Humphrey Marshall" rest
on the listing fields, as the design allows.

## Limits

- This is an AI separate review of batch 1 within the scope stated above.
- It is not human historical adjudication, independent corroboration or proof of source
  independence. It does not admit features or authorize any fit.
- Several corrections rely on retrospective narratives: Allan (1880), Woodbury (1867), Webb
  (1881) and Grant's memoirs, all digital OCR not checked against print. Those caveats carry into
  the ledger.
- B1-R1 rests on the order of events in Allan's narrative. The selection does not separately date
  the skirmish, and the rationale says so.
- The primary agent should check these findings before changing the ledger or registry, and
  should rebind hashes afterwards.
