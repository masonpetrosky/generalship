# Separate review: Trans-Mississippi 1863 first passes (AR004, AR005, MO018, MO019, MO020, AR007, OK006, OK007, AR009, KS001, AR010, AR011, KS002, OK005)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. I am a separate
  evidence-reviewer subagent started with fresh context and had no access to the author's
  conversation.
- **Date:** 2026-09-25
- **Prepared commit reviewed:** `29c28113a3f044892a04f83812e150aa7fd2cdd1`, compared with `0e6063c`
  for the registry diff.
- **Review bundle commit (worktree HEAD):** `cd780cb22f42d9ce8f1e830e7f97c0db96b0a713`. The only
  changes after `29c2811` are `assignment.md` and `inputs.json`.
- **Assignment:** `assignment.md`, sha256 `9ca1108ea6e8e124bfc6a6484287fdd8feaa36581d3a3d7d30beed5ddd12064b`
- **Input manifest:** `inputs.json`, sha256 `657b7dc91dfe3aba70ca93c0c692abf6f020ebbf9828ca4dbabb901113eca0dd`
- **Hash verification:** I checked all 162 bound paths two ways: as `git show 29c2811:<path>` and
  as the worktree file. Every one matches its manifest SHA-256, with no mismatches.
- **Outcome: corrections required.** There are 4 required corrections (R1–R4) and 12 advisories
  (A1–A12).

This is an AI review. It is a separate analysis. It is not human historical adjudication, it does not
establish that sources are independent, and it does not admit any feature. I did no research, used
no network and changed no primary artifact. This review file is the only file I wrote.

## Scope actually inspected

- **Rules and context:**
  - `AGENTS.md`, `docs/evidence-contract.md` and `docs/cohort-v2.md`, all in full.
  - The research-depth and missingness sections of `docs/methodology.md`.
  - From `docs/sources.md`: the cohort-v2 author-group paragraph, the W61-R14 Britton/Price note and
    the Trans-Mississippi 1863 entry.
  - `README.md`, `docs/roadmap.md`, the other memos, the other dossiers and history files, and the
    earlier review bundles: verified by hash only. I opened one earlier review (Gulf) for format.
- **Memos:** I read all eight named memos in full. Their count tables match the dossiers:
  - 126 claims and 15 null unknowns (one per record, two in OK005);
  - 673 citation occurrences (113, 104, 84, 144, 47, 90, 56 and 35);
  - exactly three independence groups per record;
  - all seven dimensions in every record.
- **Dossiers:** I read every claim of all 14 dossiers.
  - For every text citation I read the quote inside its section, with about 170–220 characters
    either side.
  - Where attribution, date or scope turned on more text, I read further:
    - the full Marmaduke January and May 1863 selections;
    - the Vandever May 4 dispatch to Davidson;
    - Price's addenda return and his November 25 letter;
    - the Pine Bluff and Springfield compiled returns;
    - the ends of Davidson's and Cabell's reports;
    - Britton's Baxter Springs chapter, searched for the band, Henning, Tough and Blunt;
    - Britton's Prairie Grove and Cane Hill chapters, searched for Jewell, Herron's guns and
      Herron's attack decision;
    - Cooper's report, searched for the spies;
    - Phillips's papers, searched for the Fourteenth Kansas and his name.
  - I checked CSV citations against the printed frozen battle, force and commander rows for all 14
    records.
  - I checked the NPS text snapshots in full for AR004 and AR005, and field by field (Forces,
    Casualties, Commanders, Description and Results) for the other 12.
- **Source registry:**
  - I listed all 50 records added at `29c2811` (compared with `0e6063c`) and confirmed that no
    existing record changed.
  - I read every field that matters (author, edition, group, dependency note, section date map,
    inspection note, parent) for all 22 selections.
  - I checked the NPS records by sample (OK005 text and HTML) and by their shared template.
  - All 22 selection files reproduce exactly from their parents' recorded character ranges under
    the declared whitespace-collapse transform. Parent hashes match, the section date maps have
    exactly the selected sections, and no headings are undeclared.
  - The Britton volume I parent is `britton-border-1-ocr-v1` (sha256 `03f4b2af…`). Both new volume I
    selections bind to it. The drafting IDs `britton-civil-war-border-1-ocr-v1` and
    `ia-britton-civil-war-border-1-metadata-v1` are absent from the registry, so the merge
    deduplication holds.
  - I listed every registry record by the authors in question (Shelby, Hindman, Marmaduke, McNeil,
    Vandever, both Williamses, Cooper, Cabell, Ewing, Davidson, Price, Clayton, Quantrill, Phillips
    and Blunt) and by section name to check group reuse.
- **Validation:** `make check` ran offline and passed. The unit tests ran 134 tests with `OK`,
  `python3 -m generalship check` exited 0, and `artifacts_written` is false. I ran no build, packet
  or network command.
- **Not inspected:**
  - the NPS HTML originals, other than the OK005 record metadata (hash only);
  - the full Official Records and Britton parents outside the selected ranges;
  - the admission and baseline artifacts (hash only);
  - `generalship/cli.py` and `tests/test_evidence.py` (hash only, and run through `make check`);
  - the memos, dossiers and history files of other campaigns (hash only).

## Required corrections

### R1: MO018 `reported-force-scope`, Marmaduke's 1,000 and 270 misstated as the force that struck Springfield

The dossier says "Marmaduke says he struck with about 1,000 men under Shelby and 270 under
MacDonald". The January 18 dispatch reads: "I marched from Lewisburg, Ark., December 31, 1862, via
Yellville, Ark., … to strike tlie enemy in rear or flank, with 1,000 men, under Shelby, and 270 men,
under MacDonald."

The February 1 report gives the same columns as "about 1,000 effective men, some wi thout horses"
and "about 270 effective men" on the morning of December 31 at Lewisburg. These are departure
strengths from a week before the attack, not a count of the force engaged on January 8. The word
"about" comes from the February 1 report, which the claim does not cite.

**In `value`, replace**

> Marmaduke says he struck with about 1,000 men under Shelby and 270 under MacDonald, and that the Federal force was 4,200.

**with**

> Marmaduke's January 18 dispatch says he marched from Lewisburg on December 31, 1862 with 1,000 men under Shelby and 270 under MacDonald, and his February 1 report gives the same columns on leaving Lewisburg as about 1,000 effective men, some without horses, and about 270 effective men; he puts the Federal force at Springfield at 4,200.

**Add to `rationale`:**

> Marmaduke's 1,000 and 270 are departure strengths at Lewisburg on December 31, not a count of the force engaged on January 8.

**Add citations:**

- `or22-1-marmaduke-springfield-hartville-selections-v1`, section `marmaduke-1863-01-18`, locator
  `pp.194-195 (OCR page markers; not checked against print)`: "I marched from Lewisburg, Ark., December 31, 1862,"
- The same source, section `marmaduke-1863-02-01`, locator `p.196 (OCR page markers; not checked against print)`: "with his Missouri brigade, about 1,000 effective men, some wi thout horses"
- The same source, section and locator: "about 270 effective men, marched from camp near Lewisburg,"

The memo's "Marmaduke's 1,000 under Shelby and 270 under MacDonald" may optionally add "on leaving
Lewisburg, December 31".

### R2: OK007 `reported-force-scope`, a statement of the troops' feeling attributed to Cooper as his own comparison

Cooper (p.460) writes that the Choctaws came back wet and disheartened, "and j there was a general
feeling among the troops that with such ammuni- tion it was useless to contend with a foe doubly
superior in numbers, arms, and munitions, with artillery ten times superior to ours". The "doubly
superior" comparison is what he reports his troops felt. The dossier's "speaks of a foe doubly
superior …" presents it as Cooper's own strength assessment.

**In `value`, replace**

> and speaks of a foe doubly superior in numbers with artillery ten times superior.

**with**

> and reports a general feeling among his troops, after their ammunition failed in the wet, that it was useless to contend with a foe doubly superior in numbers, arms and munitions, with artillery ten times superior.

**Add to `rationale`:**

> The 'doubly superior' comparison is the troops' feeling as Cooper reports it, not a count.

**Add citation:** `or22-1-cooper-honey-springs-selections-v1`, section `cooper-1863-08-12`, locator
`p.460 (OCR page markers; not checked against print)`: "there was a general feeling among the troops that with such ammuni- tion it was useless to contend with"

### R3: AR007 `casualty-records`, 19 enemy dead placed in the Chalk Bluff record without the scope Vandever gives

Vandever's May 4 dispatch to Davidson (p.278) says "In one place, after a gallant charge made by
Colonel Glover, … there were 19 of the enemy's dead piled together." It continues: "The engagement
at Chalk Bluff, on the morning of the 2d, was also disastrous to the enemy". He does not say where
the charge took place, and his "also" separates it from the Chalk Bluff engagement.

The dispatch goes on to say that he fought the enemy every day from April 26 until May 2. The
charge may therefore belong to the pursuit before the frozen interval of May 1–2. The dossier's
unqualified "19 enemy dead lay together after one charge" reads as a Chalk Bluff figure.

**In `value`, replace**

> and on May 4 that 19 enemy dead lay together after one charge.

**with**

> and on May 4 that in one place, which he does not name, 19 enemy dead lay together after a charge by Glover's Third Missouri Cavalry, before calling the Chalk Bluff engagement of the 2d also disastrous to the enemy.

**Add to `rationale`:**

> Vandever does not place the charge that left 19 dead, and his 'also' distinguishes it from the May 2 engagement at Chalk Bluff, so the figure may belong to the earlier pursuit.

**Add citations:** `or22-1-vandever-chalk-bluff-selections-v1`, section `vandever-1863-05-04-to-davidson`,
locator `p.278 (OCR page markers; not checked against print)`:

- "In one place, after a gallant charge made by Colonel Glover,: with the Third Missouri Volunteer Cavalry,"
- "The engagement at Chalk Blhff, on the morning of the 2d, was also disastrous to the enemy,"

The existing quote "there were 19 of the ene-; my's dead piled together." stays. The memo's "19 enemy
dead after one charge" may optionally add "(place unstated)".

### R4: sentences whose source statement is not cited within the claim

Each sentence below is accurate to the selected text, but no citation in that claim supports it.
In the first two cases the unsupported sentence carries a dispute or a killing that the assignment
asks to be recorded as reported. Add these citations; the values need no change.

**(a) KS002 `casualty-records`.** The value says Britton reports "the fourteen bandsmen and others
were murdered" and that "Britton places all three [Blunt, Henning, Tough] alive after the fight".
Neither statement has a citation. Add from `britton-indian-territory-north-1863-selections-v1`,
section `baxter-springs`:

- locator `p.220 (the running head for p.220 reads "22O" in OCR; OCR page markers; not checked against print)`: "all the members of the band, fourteen in number, and the driver, and James O'Neal, special artist for Frank Leslie 's Illustrated Newspaper, were murdered."
- locator `p.221 (OCR page markers; not checked against print)`: "Major Henning took half a dozen mounted men from the camp, and with Captain Tough returned to the high ground on the prairie"
- locator `p.224 (OCR page markers; not checked against print)`: "General Blunt followed the bandits, keeping in sight of them until they crossed the Neosho River twelve miles south,"

**(b) AR005 `command-roles`.** "Britton says Herron decided to cross Illinois Creek and attack" and
"[Blunt] arrived on the Union right in the afternoon" are not cited in this claim; the support sits
in other claims. Add from `britton-border-1-prairie-grove-selections-v1`, section `prairie-grove`:

- locator `p.409 (OCR page markers; not checked against print)`: "he determined to attack it at once, hoping that the artillery firing would bring up the Kansas General with his division."
- locator `p.418 (the running head for p.418 reads "41 8" in OCR; OCR page markers; not checked against print)`: "some of his troops on the extreme right heard distant rumbling sounds toward the west"
- the same locator: "General Blunt was seen approaching at the head of three thousand cavalry and twenty pieces of artillery,"

**(c) AR004 `command-roles`.** "Jewell leading the charge in which he was mortally wounded" is
attributed to Britton but not cited. Add from `britton-border-1-prairie-grove-selections-v1`, section
`cane-hill`:

- locator `p.392 (OCR page markers; not checked against print)`: "offered to lead the charge."
- locator `p.393 (OCR page markers; not checked against print)`: "In this volley, Colonel Jewell, Sergeant Ritchey of Company K, several enlisted men of the Sixth Kansas, fell, mortally wounded."

**(d) OK007 `crossing-intelligence`.** "Cooper says spies who had enlisted in his brigade reached
Fort Gibson" is not cited. Add `or22-1-cooper-honey-springs-selections-v1`, section
`cooper-1863-08-12`, locator `p.458 (OCR page markers; not checked against print)`: "obtained permission to enlist in this brigade, had reached Gibson ;"

I verified that every quote proposed in R1–R4 occurs exactly once in the named section.

## Advisories (no change required)

- **A1: stale merge wording (Britton volume I).**
  - Both new volume I selection records (`britton-border-1-prairie-grove-selections-v1` and
    `britton-border-1-marmaduke-1863-first-selections-v1`) still end their `dependency_note` with
    "The same parent … is registered by the parallel Trans-Mississippi 1862 pass; the two
    registrations are one record to deduplicate."
  - The Prairie Grove memo still says the pass "adds **9 records**" and names the drafting IDs. After
    deduplication it added 7, and the eight memos sum to 52 against the registry's 50.
  - `docs/sources.md` documents the deduplication and the drafting IDs, so nothing is hidden. A
    `metadata_only` successor for the two records, or a memo note giving 7 and 50, would remove the
    stale wording.
- **A2: Britton author-group names.**
  - The new volume I selections are in `britton-civil-war-border-1899`, but their parent and the
    1861 volume I selections are in `britton-civil-war-border`. The Trans-Mississippi 1862 selection
    is in `britton-civil-war-on-border-1899`.
  - The volume II selections' notes say "Same author group as the Britton volume I and earlier
    volume II selections". That is true of the new records only.
  - `docs/sources.md` (W61-R14) declares all three names one witness family. No new dossier cites
    two Britton groups, so no record is double counted.
- **A3: Price group note.** The Price selection's `dependency_note` names the Camden and 1864 Missouri
  groups as the same author but omits `price-lexington-report`. That link is covered by the W61-R14
  note in `docs/sources.md`.
- **A4: AR011 details.**
  - `water-mules-and-property` records Marmaduke's "about 300 negroes (men, women, and children)"
    without his next sentence, "The women and children I could not bring away." (`marmaduke-1863-10-26`,
    p.730). Adding it keeps the number of people carried off from being overstated.
  - The garbled compiled Union return (`us-casualty-return`, p.725) has a legible row label,
    "Freedman 5". That suggests the compiled return itself lists the freedmen, which bears on the
    rationale's "Whether the frozen US 56 includes the freedmen is not established". It is worth a
    sentence; it is not a resolution.
- **A5: OK005.**
  - Phillips's February 24 report says "The Fourteenth Kansas, which was to be the backbone of the
    expedition, was not sent". Yet his relayed February 14 report credits "my advance under Major
    Willetts, Fourteenth Kansas", and Britton and the itinerary list Willetts's battalion. The
    tension is presumably regiment versus battalion. It could be noted under strength.
  - The frozen description names "Col. John F. Phillips". The inspected reports are headed
    "Col. William A. Phillips". This is an identity error in the frozen text, not a commander row.
  - The live Forces field reads "0 total (US ; CS ;)", not blank.
  - The memo's "Neither counts Willette's advance" is ambiguous, because Britton's "about one
    thousand" explicitly includes Willetts's battalion.
- **A6: MO020, an ambiguous NPS antecedent.** "sought to strike Brig. Gen. John McNeil, with his
  combined force of about 2,000 men, at Bloomfield" does not say whose force "his" is. The live Forces
  field (US 2000) supports the McNeil reading. The value could say "NPS appears to give McNeil's
  combined force as about 2,000".
- **A7: AR005, Britton's Herron gun count.**
  - The value says Britton has "Herron brought twenty guns into action". p.409 says Herron's
    "artillery companies were bringing up his twenty pieces of artillery". p.420 has "General
    Herron's eighteen guns".
  - "was bringing up twenty guns (eighteen elsewhere)" would keep Britton's internal difference
    visible.
- **A8: MO019 rationale.** "Marmaduke's 'General Merrill' is his rank error" adjudicates. Suggested
  wording: "differs from Britton's 'Colonel Merrill' and the frozen rank of Colonel".
- **A9: OK006 hedge.** Britton writes that "Colonel Watie seems to have made very little effort to
  rally his men". The value drops "seems".
- **A10: the `commander_created` criterion.**
  - The single tag (AR011, Clayton's cotton-bale works) is sound as a hypothesis. The works were
    built on the morning of the attack on Clayton's explicit order.
  - The agency evidence comes from Clayton and his own inclosure (Talbot), which is one report
    family.
  - Other ground chosen during an action stays `unresolved`: Cabell's ambush dispositions ("I placed
    Monroe's regiment in ambush"), Shoup's ridge and Merrill's line. That is consistent only if the
    rule is "works constructed on an explicit order" rather than "ground selected". The Little Rock
    memo could state the rule.
- **A11: fourth-family reads.**
  - McNeil's May 12 report (AR007), Dobbin's report (AR010) and Pond's report (KS002) were read in
    full, so these records were inspected in four families.
  - The ceiling limits inspection effort, not citation. Leaving the reports uncited is conservative,
    and each is recorded in the dossier's open questions and in the memo. That is acceptable.
  - Pond is a frozen commander and Dobbin covers the crossing directly. They are the natural first
    targets if these records are revisited, as the memos already say.
- **A12: MO018, the year printed on the No. 9 return.** The return's heading prints "January 2-11,
  1862" (evidently a misprint for 1863). The value gives "January 2-11" without the printed year.
  A note would keep the printed text visible.

## Answers to the assignment's source-choice questions

- **One report author per record:**
  - Every record other than the four below uses NPS/CWSAC, Britton and one Official Records report
    author.
  - Cape Girardeau (McNeil and Marmaduke), Chalk Bluff (Vandever and Marmaduke), Bayou Fourche
    (Davidson and Price) and Pine Bluff (Clayton and Marmaduke) use one Union and one Confederate
    author instead.
  - The memos record the Britton volume II search that found no treatment of these four. The
    choice is sound for a first pass.
- **Indorsements, inclosures, relays and compiled returns:** each is a separate section inside its
  selection, with its own date or null. None is counted as an extra family. Covered here: Holmes's
  and Kirby Smith's indorsements; Banks's and Talbot's inclosures; Cooper's General Orders No. 25;
  Thayer's relay; the Indian Brigade itinerary; and the No. 9, addenda and Pine Bluff returns.
- **Author groups:**
  - McNeil (`mcneil-kirksville-1862-reports`), Cooper (`cooper-indian-territory-1862-reports`),
    Hindman (`hindman-mclemores-cove-reports`) and Price (`price-missouri-1864-reports`) reuse
    existing groups.
  - `marmaduke-1863-reports` is new and holds all three Marmaduke selections. No earlier Marmaduke
    record exists.
  - James M. Williams's group is correctly kept separate from John S. Williams's.
- **Killings at Lawrence and Baxter Springs:** these are recorded as reported, and the boundary notes
  and rationales keep them out of ordinary combat casualties. The captives killed on the later march
  are not added. R4(a) supplies the missing citations for the Baxter Springs statements.
- **Phases:** no claim is tagged `inherited`. Every null unknown has no citations. No strength is
  adopted as an opening force, and every expedition-wide total is left unassigned.

## Finding IDs

R1, R2, R3, R4, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12
