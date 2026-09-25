# Separate review: Price's Missouri Expedition, Mobile Bay, Mobile and Wilson's Raid first passes

**Outcome: corrections required** (4 required corrections, 9 advisories).

This is an AI review. It is a separate analysis. It is not human historical adjudication, proof that
sources are independent, or admission of any feature. The primary agent should check each finding
against the cited passages before changing any evidence.

## Reviewer record

| Item | Value |
| --- | --- |
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), `high` reasoning effort, fresh-context `evidence-reviewer` subagent |
| Date | 2026-09-25 |
| Prepared commit reviewed | `5d5bc1c2eb9152227a63ea8a92f3850a40bd124f` |
| Previous commit (diff base) | `b8d19758f70f04d12cf6c22a5bc4d569af78af03` |
| Assignment bundle commit (worktree HEAD) | `27ee4e505b5bbffa0f348e8305f418fe00a6d611` |
| `assignment.md` SHA-256 | `d7bc35047aaa5658023b77ebd117f606cd8ddf55e63461aaaa85fb688fb00c8f` (verified) |
| `inputs.json` SHA-256 | `bef672c6edcb5ecd72e74a2ed7371dea51cdec8a31ed177c29c23539a2cf7ca1` (verified) |
| Input hashes | All 81 paths in `inputs.json` match both `git show 5d5bc1c…:<path>` and the worktree. No mismatch. |
| `make check` (offline) | Passed. 134 unit tests OK; `python3 -m generalship check` exited 0 (127 pilot battles, 23 eligible, 233 draft dossiers). |

I did no network research, opened no extra source families, spawned no agents and ran no build or
packet commands. This file is the only one I wrote.

## Scope actually inspected

- **Instructions and docs.** `AGENTS.md`, `docs/methodology.md`, `docs/evidence-contract.md`,
  `docs/cohort-v2.md`, the four first-pass memos and the `docs/sources.md` diff at the prepared
  commit.
- **Dossiers.** All 15: MO021–MO029, KS003, KS004, AL003 and AL005–AL007.
  - I read every claim's value, status, phase and rationale.
  - I read every citation (551 occurrences) in the context of its section, about 180 characters
    either side. Where support was doubtful, I read the wider passage (up to several thousand
    characters).
  - I recounted claims, unknowns, citations, phases and cited families. The counts match the memos
    (Price's Missouri: 99 claims, 11 unknowns, 398 citations; Mobile Bay: 9, 1, 56; Mobile: 18, 2,
    93; Wilson's Raid: 9, 1, 45).
  - Each dossier cites exactly three families.
- **Frozen Arnold rows.** The battle, force and commander rows for all 15 records, compared with each
  dossier.
- **NPS text snapshots.** The retained snapshots for the 14 records that have one. MO022 has only the
  empty-template HTML. I did not read the NPS HTML files beyond their role as hash-bound parents.
- **Source records.** All 44 records added at the prepared commit, plus the four registered parents
  that the selections now point to: `britton-civil-war-border-2-ocr-v1`, `or39-1-illinois-ocr-v1`,
  `mahan-gulf-inland-text-v1` and `jordan-pryor-forrest-ocr-v1`.
- **Selections.** For all 9 selections, each `parent_sha256` resolves to the named parent.
  Re-extracting every section from `selection_character_ranges` with the documented transform
  (split/join whitespace) reproduces the snapshot text exactly.
  - This includes the Britton volume II and OR XXXIX Part 1 selections that were deduplicated at
    merge.
  - The Page selection's parent hash `ca9440d3…` is `or39-1-illinois-ocr-v1`.
  - The Britton selection's parent hash `f49c5735…` is `britton-civil-war-border-2-ocr-v1`.
- **Not inspected:**
  - the full OCR parents beyond the selected ranges and their title and boundary text;
  - the catalog-metadata JSON bodies;
  - every source family the memos list as deferred.

## Required corrections

### PRV-R1: MO023 `scouts-and-intelligence`, field `value` (reversed direction)

Britton says the couriers **from** Sanborn did not reach Blunt:

> "nor did the couriers from General Sanborn reach him."
> (`britton-price-missouri-selections-v1`, section `lexington-little-blue`, p.443)

Earlier on the same page Britton says Blunt himself "sent couriers with despatches stating his
position and movements to General Sanborn". He does not say whether those couriers arrived. The
dossier's "his couriers to Sanborn did not arrive" reverses the direction and states an outcome
Britton does not give.

- **Replace** "and that his couriers to Sanborn did not arrive."
- **With** "and that couriers from Sanborn did not reach him."
- **Citations.** Keep the existing citation. Optionally add the source ID
  `britton-price-missouri-selections-v1`, section `lexington-little-blue`, locator
  `p.442 (OCR page markers; not checked against print)`, with the quote "sent couriers with
  despatches stating his position and movements to General Sanborn". If you add it, the value may
  read "that Blunt sent couriers to Sanborn but no couriers from Sanborn reached him".

### PRV-R2: MO021 `command-roles`, field `value` (attribution overstated and uncited)

Price's report is passive at this point: "until about 2 p. in., when a charge was ordered and made in
the most gallant manner" (p.629). It does not say who ordered the charge, and the dossier cites no
passage for "ordered the charge".

- **Replace** "Price says he directed Marmaduke to take Shepherd's Mountain and ordered the charge;"
- **With** "Price says he directed Marmaduke to take Shepherd's Mountain and that a charge was ordered
  about 2 p.m., without naming who ordered it;"
- **Add citation:**
  - source ID: `or41-1-price-missouri-selections-v1`
  - section: `price-1864-12-28`
  - locator: `p.629 (the running head for p.629 reads "G29" in OCR; OCR page markers; not checked against print)`
  - quote: "when a charge was ordered and made in the most gallant manner"

### PRV-R3: AL007 `casualty-records`, field `value`, and the Wilson's Raid memo (OCR reading misstated)

The May 3 OCR reads "t’loosaod seven hundred prisoners, including 150" (`wilson-1865-05-03`, p.351).
The dossier and memo both describe this as "about 'seven hundred prisoners'", which drops the legible
"t’loosaod" (thousand).

- The detailed report's garbled "2^700" is consistent with a count in the thousands, and the frozen
  CS figure is 2,700.
- So the memo's framing of this number as a dispute with the frozen CS 2,700 is not supported.
- The word "officers" after 150 does not appear in the OCR.

**Dossier change (`data/evidence/AL007.json`, claim `casualty-records`, field `value`):**

- **Replace** "and a garbled count of about 'seven hundred prisoners, including 150' officers;"
- **With** "and a prisoner count garbled in OCR as 't’loosaod seven hundred prisoners, including 150'
  (the thousands figure and the word after 150 are illegible);"
- The existing citation quote "t’loosaod seven hundred prisoners, including 150" is already exact and
  should be kept.

**Memo change (`docs/research/wilson-raid-first-pass-v1.md`, "Disputes preserved", Casualties
bullet):**

- **Replace** `Wilson's partly legible "46 killed" and "seven hundred prisoners, including 150"
  against the frozen CS 2,700.`
- **With** `Wilson's partly legible "46 killed" (Long's division) and a prisoner count garbled as
  "t’loosaod seven hundred … including 150", whose thousands figure is illegible, so it is not
  recorded as disagreeing with the frozen CS 2,700.`

### PRV-R4: `britton-price-missouri-selections-v1`, fields `independence_group` and `dependency_note`

After merge deduplication, this selection's parent is `britton-civil-war-border-2-ocr-v1`, whose
group is **`britton-civil-war-border-1899`**. The Camden Britton selection uses the same group. This
selection still carries **`britton-civil-war-on-border-1899`**, so one book on one parent now appears
under two group names.

Its dependency note also says "No earlier registry group for this author", which is no longer true in
the merged registry. The validator did not catch the group mismatch.

Following the evidence contract's metadata-correction rule, add a `metadata_only` revision
`britton-price-missouri-selections-v2`:

- Keep the same `path`, `sha256`, `format`, `parent_source_id`, `parent_sha256`, sections, ranges and
  section dates.
- `supersedes`: `{"source_id": "britton-price-missouri-selections-v1", "metadata_sha256": "c44ed0f78e06bcc932985bfdee86bf371aa468c0d78e1805cdd9fef2df47349f"}`.
  This hash is my computation over the v1 entry serialized with sorted keys, compact separators and
  UTF-8 with `ensure_ascii=False`. The primary should recompute it.
- `revision_kind`: `metadata_only`.
- `revision_note`: "PRV-R4: independence group aligned with registered parent after merge
  deduplication; same pinned raw bytes."
- `independence_group`: `britton-civil-war-border-1899`.
- `dependency_note`: replace the sentence "No earlier registry group for this author." with "Same book,
  parent and group (`britton-civil-war-border-1899`) as the Camden selection; one witness family
  across both campaigns."

Then repoint the Britton citations in the 11 Price's Missouri dossiers to the v2 ID, with quotes,
sections and locators unchanged. The Price memo's "(new independence group
`britton-civil-war-on-border-1899`)" should point to the corrected group. If the primary prefers a
different mechanism for records not yet reviewed, it should document that choice. The corrected
group value is what this finding requires.

## Advisories

These are not required for extraction correctness.

- **PRV-A1 (MO028, Marmiton reading).** Price never names Shiloh Creek, Charlot's farm or the Marmiton
  for this stand.
  - His passage runs from Shelby holding "at the crossing of the Osage until the train could be placed
    in safety" to "I again formed the unarmed men … on the prairie beyond the river" until nightfall.
  - Treating that stand as the same one as Britton's Shiloh Creek stand is a reasonable
    interpretation. Part of Price's account may also cover the Little Osage action, which this pass
    treats as context.
  - `place-of-the-stand` is correctly marked disputed. However, the rationales of
    `reported-force-scope` and `hold-until-night` do not flag the inference.
  - Suggested addition to both rationales: "Price does not name the place; identifying his 'prairie
    beyond the river' line with Britton's Shiloh Creek stand is an interpretation, and part of his
    account may cover the Little Osage action."
- **PRV-A2 (MO021, frozen description not accounted for; minor uncited phrase).**
  - The frozen and NPS description says "Price, considering the possible time involved, had dismissed
    the possibility of mounting guns on the high ground to compel the fort to surrender or to shell
    the garrison into submission".
  - Britton gives a different reason: Mackey "advised that the fort be reduced by bombardment", and
    "His views were concurred in by General Price". The council chose to assault because "it was
    currently reported among the Confederate officers that a large part of the Federal gar rison was
    colored soldiers" and some officers wanted to avenge Ewing's order.
  - These are competing accounts of why bombardment was rejected. They could be added to
    `fortification-intelligence` or to a new disputed claim.
  - Separately, "a company of Black men" in `reported-force-scope` is supported but uncited. The
    quote to add is "a company of negroes was also organized" (`pilot-knob`, p.395).
- **PRV-A3 (memos: stale source counts and groups).**
  - The Price memo says the pass adds 27 records and a new Britton group. At merge it added 25, and
    the group already existed.
  - The Mobile Bay memo says 6 records and a "new parent" for OR XXXIX, and asks for reconciliation
    at merge. At merge it added 4, and reconciliation is done.
  - `docs/sources.md` documents the deduplication, and the 44 total is correct. A one-line pointer in
    each memo would stop the memos contradicting the registry.
- **PRV-A4 (same-author cross-references).** Under the `docs/sources.md` rule, groups by the same
  author are one witness family.
  - `or41-1-price-missouri-selections-v1` says "No earlier registry group for this author in this
    worktree". The merged registry has `price-camden-1864-report`, whose note makes the same claim.
  - `or49-1-wilson-selma-selections-v1` does not mention `wilson-south-side-raid-reports` (James H.
    Wilson, 1864).
  - Reciprocal notes would help any cross-campaign independence count.
- **PRV-A5 (AL007, Taylor's departure).** Wilson's May 3 OCR contains "Taylor had left at3" (garbled).
  The Taylor bullet in the memo and the dossier compares only NPS and Jordan (2 p.m.). Wilson's
  partial reading could be noted as a third, garbled account.
- **PRV-A6 (AL003 result completeness).** `recorded-result` covers Powell, Gaines and Morgan but not
  the Tennessee's surrender. Mahan's "the United States flag hoisted on board the Tennessee at ten
  o'clock" (`mobile-bay`, p.244) is quoted only incidentally, and NPS's "forced the Confederate naval
  forces … to surrender" is not cited.
- **PRV-A7 (MO024 wording).** Britton says Fagan's division was brought "to the support of Marmaduke
  and Shelby". The value "Marmaduke, Shelby and then Fagan crossing" slightly overstates that. Fagan
  is not said to have crossed.
- **PRV-A8 (consequential gaps; the source choices are sound).** See the next section. The pass's
  choices are defensible under the three-family ceiling and are disclosed. For later admission
  decisions, note two limits:
  - In every Price's Missouri record, the Union side rests on NPS and on Britton, who depends on the
    Union reports.
  - AL006 has no Confederate family, apart from the Liddell dispatches that Andrews quotes.
- **PRV-A9 (MO022).** The frozen description's Hereford Hill, Harding's destruction of stores and the
  three-day stay are covered or properly treated as context. The "boost to … morale" sentence is
  rightly not used.

## Assessment of the questioned source choices

- **No Union commander's report for Price's expedition.** Acceptable within the bound. The memo and
  every dossier disclose it as the consequential gap. Britton's dependence on those reports is
  recorded, so the pass does not count Britton as independent Union corroboration.
- **Page instead of Granger at Mobile Bay.** Sound. Page supplies the only Confederate primary account
  for all phases, and Mahan covers Granger's landing and siege. Granger's land strength stays unknown,
  as recorded.
- **Gibson at Spanish Fort and Andrews at Fort Blakely.** Sound. Gibson is the defending commander.
  Andrews is a participant history, correctly recorded as not independent of Canby.
  - Gibson's garbled Union estimate (".0,000 muskets") is quoted as read and not adopted.
  - The garbled columns of the comparative casualty statement are quoted without assignment.
- **Jordan and Pryor at Selma.** Sound. It gives the only Confederate-side account, and its dependence
  on Forrest and its citation of Andrews are recorded.
- **Price's report dated 1864 where the OCR reads 1861.** Sound. The report narrates the 1864
  expedition and states "I arrived there on the 2d of December, 1864". The volume imprint is 1893.
  The section date `1864-12-28` is justified, and the transcription note keeps the OCR reading.
- **Marmiton reading.** Defensible and correctly disputed as to place. See PRV-A1.

## Rule checks

- No strength is adopted as an opening force. Each record's only null unknown is its opening
  strength, and live NPS zeros are not treated as measured absence.
- Phases are only `unresolved` or `post_outcome`. None is `inherited`, a conservative choice the
  memos disclose. Results and casualties are `post_outcome`.
- No listed commander receives automatic credit. Frozen ranks are kept, and live ranks are recorded
  but not adopted. The Marmaduke rank inconsistency across the frozen KS003, KS004, MO025 and MO026
  rows is reported correctly.
- Overlapping records are not double counted:
  - the MO025/MO026 boundary, the MO027/MO026 boundary, and KS004/KS003/MO028 with the Little Osage
    action as context;
  - the AL005/AL006 intervals;
  - AL003's phases kept inside one record;
  - campaign totals such as Canby's 4,924 prisoners and Price's "at least 5,000 new recruits" kept as
    context.
- The three-family ceiling is respected in all 15 dossiers. Families are grouped correctly, apart from
  the group-name inconsistency in PRV-R4.
- No morale or readiness score, probability, causal effect or ranking appears in any dossier.

## Finding IDs

- **Required:** PRV-R1, PRV-R2, PRV-R3, PRV-R4.
- **Advisory:** PRV-A1 through PRV-A9.
- **Unresolved historical questions** are left as the memos record them. This review does not
  adjudicate them.
