# Separate review: Gulf and Louisiana 1862-63 first passes (LA001-LA010, LA012, LA013, LA015, LA016)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. Separate evidence-reviewer
  subagent started with fresh context. It had no access to the author's conversation.
- **Date:** 2026-09-25
- **Prepared commit reviewed:** `be711a9045e1bc71c6a869423d1c0994b9931818`, compared with
  `badefa6b3c7d8d914a616217be81551cc931864a`
- **Review bundle commit (worktree HEAD):** `86c9f725a29dcefb7e0ea5b770d0fb3bc4cd4752`. Its only
  changes after `be711a9` are `assignment.md` and `inputs.json`.
- **Assignment:** `assignment.md`, sha256 `631fe7ba1d0df16a75d26b890f4031abe45cea8a8da731115e49817553adbcdd`
- **Input manifest:** `inputs.json`, sha256 `07d080efd661d6873b9f09388846eb50e794d1061e10057a3277c4fd89b13b91`
- **Hash verification:** all 88 bound paths match their manifest SHA-256, both as
  `git show be711a9:<path>` and in the worktree. There were no mismatches.
- **Outcome: corrections required.** There are 4 required corrections (R1-R4) and 10 advisories (A1-A10).

This is an AI review. It is a separate analysis, not human historical adjudication. It does not
establish that sources are independent, and it does not admit any feature. I did no research, used
no network and changed no primary artifact. This is the only file I wrote.

## Scope actually inspected

- **Rules and context:** I read `AGENTS.md`, `docs/evidence-contract.md` in full, the research-depth
  and missingness sections of `docs/methodology.md`, `docs/cohort-v2.md` in full, and the cohort-v2
  source-family paragraph and new Gulf entry in `docs/sources.md`. `README.md` and
  `docs/roadmap.md` were verified by hash only; I did not read them.
- **Memos:** I read all six campaign memos in full and checked their count tables against the
  dossiers. Claims, unknowns and citations match in every memo.
- **Dossiers:** I read every claim of all 14 dossiers (126 claims, 14 null unknowns, 625 citations).
  - For every text citation I read the quote in its surrounding passage, normally about 230-300
    characters either side, after collapsing whitespace. Where the attribution, date or scope
    depended on more text, I read further: Mahan pp.58, 71-73 and 88-89; Duncan pp.527-531;
    Breckinridge pp.76-77; Irwin pp.32-34, 116-117, 122-125, 225-229, 239 and 253-254; Mouton
    pp.177-178.
  - CSV and NPS citations were checked against printed frozen battle, force and commander rows for
    all 14 records and the Description, Forces and Casualties fields of all 14 NPS text snapshots.
- **Source registry:** I read all 50 records added at `be711a9`, confirmed that no existing record
  changed, and read the reused parents (`or6-illinois-ocr-v1`, `irwin-nineteenth-corps-ocr-v1`,
  `mahan-gulf-inland-text-v1`) and `or34-1-taylor-red-river-selections-v1`.
  - All 16 new selection files were reproduced exactly from their parents' recorded character
    ranges. This includes the Duncan and Lovell selections against the 1861 Volume VI parent
    (`data/raw/gulf-blockade-1861-v1/or6-full.txt`).
  - I checked the catalog metadata fields (volume, date, contributor, scan date) and the OCR title
    strings for OR XV, OR XXVI Part 1 and ORN 19.
- **Validation:** `make check` ran offline and passed. The unit tests ran 134 tests with `OK`,
  `python3 -m generalship check` exited 0, and `artifacts_written` is false. I ran no build, packet
  or network command.
- **Not inspected:** the NPS HTML originals (hash only), the full OR/ORN/Irwin/Mahan parents outside
  the cited spans, the admission and baseline artifacts (hash only), and `generalship/cli.py` and
  `tests/test_evidence.py` (hash, and run through `make check`).

## Required corrections

### R1: LA005 `recorded-result`, a confusion statement attributed to the right-bank troops against Mouton's own report

Mouton (p.177) writes that when "Ralston's battery was so severely injured by the enemy's, and their
ammunition giving out, they were compelled to fall back, which was done in some confusion, owing to
the loss of their commander."

- The antecedent of "they" and "their commander" is ambiguous. On p.178 Mouton reports that "Captain
  Ralston, commanding the battery, was wounded and captured".
- On the same page he says Colonel Armant "commanded the troops and disposed of them with ability
  and judgment, availing himself of every cover and protection at hand and falling back in perfect
  order."
- The dossier's "the right-bank troops fell back in some confusion after losing their commander"
  resolves the ambiguity one way and omits the contrary statement.

**Change `value` to:**

> The frozen result reads Union victory and the live result Union Victory. Irwin says Mouton's force was compelled to retreat after a short engagement. Mouton says that when Ralston's battery was badly injured and out of ammunition "they" fell back in some confusion owing to the loss of their commander; he reports Ralston, commanding the battery, wounded and captured, and says Armant, who commanded the troops, fell back in perfect order. NPS says the withdrawal opened this portion of the Lafourche.

**Add to `rationale`:**

> Mouton's report does not make clear whether the confused withdrawal was the battery's or the right-bank infantry's; the two statements are kept as written.

**Add these citations:**

- `or15-mouton-la-fourche-selections-v1`, section `mouton-1862-11-04`, locator `p.178 (OCR page markers; not checked against print)`: "commanding the battery, was wounded and captured."
- The same source, section and locator: "falling back in perfect order"

### R2: LA003 `reported-force-scope`, Breckinridge's 3,400 described without its "own troops" scope, and the militia exclusion omitted

- Breckinridge's 3,400 refers to "My own troops having suffered severely from the effects Of exposure
  at Vicksburg" (p.76). He had already said that Ruggles "was already at Camp Moore, in command of a
  small force".
- Irwin's 3,600 is "including Ruggles". The two figures therefore have different stated populations
  and are not simply two values for one July 30 total.
- Breckinridge's 2,600 excludes both "some 200 Partisan Rangers" and "about the same number of
  militia" (p.77). The dossier mentions only the rangers.

**In `value`, replace**

> had no more than 3,400 on the march

**with**

> said his own troops from Vicksburg numbered no more than 3,400 on the march

**and replace**

> besides some 200 partisan rangers

**with**

> besides some 200 partisan rangers and about the same number of militia under Hardee who did not arrive in time

**Replace the `rationale` sentence**

> Breckinridge's July 30 figure differs between them.

**with**

> Breckinridge's 3,400 is stated for his own troops from Vicksburg, while Irwin attributes to him 3,600 including Ruggles; the figures differ in stated scope and are not reconciled.

The `status` can stay `disputed` because the Union and Confederate figures still differ by source.

**Add these citations:**

- `or15-breckinridge-baton-rouge-selections-v1`, section `breckinridge-1862-09-30`, locator `p.76 (OCR page markers; not checked against print)`: "My own troops having suffered severely"
- The same source and section, locator `p.77 (OCR page markers; not checked against print)`: "nor about the same number of militia hastily collected by Col. D. C. Hardee"

### R3: LA007 `casualty-records`, the nominal-list 353 described as a battle-only loss

Irwin gives the nominal-list 353 "In the battle of Irish Bend". His next sentences qualify it:

- He says it is "agreeing with the first statement covering the three days".
- He adds: "Of this total Dwight's brigade lost 3 killed and 9 wounded on the 13th, i killed and 5
  wounded on the 17th, and only 2 killed and 13 wounded in the battle."

Both 353 figures therefore include April 13 and April 17. April 17 is LA008. The dossier value calls
the second figure "the nominal-list loss for the battle", and its rationale treats only Grover's
return as spanning three days.

**In `value`, replace**

> the nominal-list loss for the battle as 6 officers and 43 men killed, 17 officers and 257 men wounded and 30 missing, also 353

**with**

> the nominal-list loss, headed as for the battle, as 6 officers and 43 men killed, 17 officers and 257 men wounded and 30 missing, also 353, which he says agrees with the three-day statement and which includes Dwight's losses of April 13 (3 killed, 9 wounded) and April 17 (1 killed, 5 wounded)

**Replace the `rationale` sentence**

> Grover's 353 spans three days and overlaps LA008's April 17.

**with**

> Both 353 figures span April 13, 14 and 17 by Irwin's account and overlap LA008's April 17; neither is a battle-only total.

**Add these citations:**

- `irwin-west-louisiana-1863-selections-v1`, section `irish-bend`, locator `p.117 (OCR page markers; not checked against print)`: "agreeing with the first statement covering the three days,"
- The same source, section and locator: "Of this total Dwight's brigade lost 3 killed and 9 wounded on the 13th, i killed and 5 wounded on the 17th,"

### R4: The New Orleans memo is stale after the Volume VI deduplication

`docs/research/new-orleans-1862-first-pass-v1.md` conflicts with the registry and with
`docs/sources.md`:

- It still says "Volume VI is newly pinned from the University of Illinois scan
  `warofrebellion06unit` with catalog metadata and full OCR".
- It still says "This pass adds **9 source records**", including "the OR Volume VI catalog metadata
  and full OCR".
- It still says "The assignment noted that another pass may register Volume VI in parallel; the
  primary should deduplicate."

The registry has only 7 new New Orleans records: two NPS pairs, the Duncan, Lovell and Mahan
selections. `or6-duncan-forts-selections-v1` and `or6-lovell-new-orleans-selections-v1` use the
existing `or6-illinois-ocr-v1`, registered in the 1861 West pass. The six memo counts add up to 52;
the registry and `sources.md` have 50.

**Replace**

> Volume VI is newly pinned from the University of Illinois scan `warofrebellion06unit` with catalog metadata and full OCR.

**with**

> Volume VI is the University of Illinois scan `warofrebellion06unit` already registered in the 1861 West pass (`or6-illinois-ocr-v1`); this pass's byte-identical copy was deduplicated to it.

**Replace**

> This pass adds **9 source records**: … the OR Volume VI catalog metadata and full OCR; …

**with**

> This pass adds **7 source records**: two NPS HTML/text pairs; the Duncan and Lovell selections (reusing the registered Volume VI parent); the Mahan New Orleans selection (reusing the registered parent).

**Replace**

> The OR parent is in `or-series-i-volume-vi`. The assignment noted that another pass may register Volume VI in parallel; the primary should deduplicate.

**with**

> The reused OR parent is in `or-series-i-volume-vi`. Its registry inspection note predates this pass; the New Orleans inspection is recorded in the Duncan and Lovell selection records.

## Advisories (not required)

- **A1: LA001 `forts-river-and-obstructions`, distance disagreement.** The cited Mahan sentence on p.58
  is preceded by "twenty miles from the Head of the Passes, and ninety below New Orleans." NPS says
  "approximately seventy miles". Consider adding the Mahan figure and noting the difference.
- **A2: LA001 `casualty-records`, scope of Mahan's garrison loss.** Mahan's "14 killed and 39 wounded"
  follows a paragraph beginning "When taken possession of, Fort Jackson was found to have suffered
  greatly." Whether it covers Fort St. Philip is unstated, and the rationale should say so.
  - Lovell's May 22 report says the fleet passed "with fourteen ships", against Duncan's thirteen.
  - Lovell is not a LA001 family, so this can stay a memo note.
- **A3: LA002 and LA004, zero casualties in the frozen force tables.** The frozen force rows carry
  `casualties` 0 for each side. The claims cite only `casualties_text` ("None" and "None known") and
  the live zeros. Note that the frozen-table zeros are not measured zeros either.
- **A4: LA003, a missing Van Dorn estimate.** Irwin (p.33) says Van Dorn estimated Breckinridge's
  division, including 1,000 under Ruggles, "at 6,000 men". This is a planning expectation, relevant to
  `expected-attack-and-the-arkansas` or the strength scope list.
- **A5: LA008, bridge-burning chronology.**
  - Irwin p.122 ("On the 1 6th he marched twenty miles, crossed the Vermilion River, … and burned the
    bridges behind him") and Taylor's rest "from Thursday afternoon until midday on Friday" place the
    burning on April 16.
  - Irwin p.124 ("Before Grover could overtake them, the bridges were in flames") and NPS ("reached
    the bayou while the bridge was burning", the morning of April 17) place it on the 17th.
  - The contact is "Early in the afternoon" in Irwin and "morning" in NPS.
  - Consider recording the date and clock difference in `contact-at-the-crossing` or
    `burned-bridge-and-heights`. It need not be resolved.
- **A6: LA010, two wording points.**
  - In `reported-force-scope`, "His footnote says the May and June returns only carry March forward"
    should say the *Union* monthly and tri-monthly returns, as the memo does.
  - In `command-roles`, the "July 7" date of Gardner's council comes from Irwin pp.225-226, outside
    the selection, whose surrender section begins "That evening". It can be dated from Miles's July 7
    field report instead, or the date can be dropped.
  - The rationale's "appear to include the surrendered garrison" is an inference. Keep it hedged.
- **A7: LA013, date of Mouton's order.** NPS dates Mouton's order to take Donaldsonville June 28.
  Green's July 3 report cites Mouton's order "of the 26th ultimo". The objectives claim cites both
  without noting the difference.
- **A8: "later" assistant adjutant-general.** The `open_questions` in LA003 and LA005-LA008 call
  Irwin "the corps' later assistant adjutant-general". The inspected passages do not establish his
  role at the time of the April 1863 Teche events. The registry notes more carefully say "styled on
  the OCR title page". Use that wording, or drop "later" for LA006-LA008.
- **A9: Registry notes.**
  - The Mahan selection's dependency note says Mahan quotes "M. L. Smith's report". The passage quotes
    General M. L. Smith's judgment without calling it a report.
  - The St. James committee record's `source_kind` (`official_report_compilation`) describes the ORN
    container, not a civilian report.
  - The committee's statements of Farragut's stated reason and threat relay Farragut's own
    communications. On those points it is not independent of the Farragut family, and its dependency
    note could say so.
- **A10: Taylor group label.** Placing Taylor's April 23, 1863 report in `taylor-red-river-1864-reports`
  is sound under the cohort-v2 rule that one author's groups are one family. The dependency note
  explains it. No tool or reviewer should infer the report's date or campaign from the group name.

## Answers to the assignment's source questions (section 4)

- **Registry accuracy.**
  - Editions and imprints (OR VI 1882, OR XV 1886, OR XXVI Part 1 1889, ORN 19 1905, Irwin 1892,
    Mahan 1898 issue of the 1883 text) match the OCR titles and catalog metadata I checked.
  - The rule that catalog dates are not the imprint is applied correctly.
  - Section dates are mapped per report, and undated items are null: Farragut's printed proclamation
    and Green's June 28 casualty statement.
  - Inspection notes match the selections that were reproduced.
  - Exceptions are the minor A9 points and the stale memo (R4).
- **Taylor's 1863 report in the existing Taylor group:** sound (see A10).
- **Rewritten dependency notes on the new Irwin and Mahan selection records:**
  - They are appropriate and, apart from A9, accurate for each selection.
  - Each names the report family the passage quotes or relies on: Breckinridge, Mouton, Taylor,
    Miles and the surgeon's return, Stickney and Green, and Duncan and Lovell through "the testimony
    of the Confederate officers".
  - The Port Hudson note correctly marks Irwin as partly a participant ("the writer of these lines";
    named commissioner).
- **LA004 without a history family:** sound.
  - It uses three families (NPS/CWSAC, Farragut's documents and the St. James committee), within the
    ceiling, and the gap is recorded.
  - The two ORN documents are opposing interested accounts in a shared container. They are
    independent in authorship but not on every point (see A9).
- **April 28 fort surrender recorded only in LA001:** sound. It is the forts' outcome, and LA002's
  boundary note excludes it. LA002's "The city surrendered on April 28" (NPS) concerns the city and is
  correctly kept as a disputed city-surrender date.
- **Port Hudson siege strengths as the main gap:** sound.
  - No garrison return was inspected. Irwin's "about seven thousand" has no stated source.
  - The besiegers' figures are Irwin's own. The Union returns carried March forward.
  - No strength is adopted. The unknowns stay null.
- **Volume VI parent deduplicated to the 1861 West registration:**
  - The deduplication is sound. The Duncan and Lovell selections reproduce exactly from
    `data/raw/gulf-blockade-1861-v1/or6-full.txt`.
  - The parent's inspection field still describes only the Santa Rosa reading. Because registry
    records are immutable, that is acceptable, provided the memo says so (R4).

## Rules check across all 14 dossiers

- **Opening strengths:** none adopted. Every `opening-personnel-unknown` claim is null with no
  citations. Imported bounds (LA005 CS 1,392, LA012 US 838) are described with their basis and are
  not validated as opening forces.
- **Disputes:**
  - Disputes are marked, including figure disagreements, the frozen/live result differences (LA004,
    LA013) and the gun-count and retreat-distance differences (LA015).
  - Arithmetic anomalies are preserved as printed: Irwin's "212" for components that sum to 121
    (LA016), and OCR "000", "i,icxD" and "/".
- **Phases:** no claim is tagged `inherited`. All are `unresolved` or `post_outcome`, with rationales
  explaining why pre-existing ground was not tagged `inherited`.
- **Commander credit:** no automatic credit. Frozen versus live ranks are noted without adopting
  either (Farragut's rank; Powers's initials in LA009; Weitzel shown as not directing the action in
  LA015).
- **Overlaps:** multi-day and overlapping totals are not added across records. The exceptions are
  the LA007/LA008 overlap, whose scope must be tightened (R3), and Plains Store, which is correctly
  excluded from the LA010 totals.
- **Three-family ceiling:** respected. Every dossier cites exactly NPS/CWSAC plus two further
  families, and the groupings are correct. Arnold and NPS are one family, and Irwin is one family
  across all five selections.

## Finding IDs

- **Required:** R1, R2, R3, R4
- **Advisories:** A1, A2, A3, A4, A5, A6, A7, A8, A9, A10
