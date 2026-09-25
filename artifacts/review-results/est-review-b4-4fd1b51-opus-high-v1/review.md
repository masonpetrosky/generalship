# Best-estimate ledger, separate review: batch 4 of 4

## Record

| Field | Value |
| --- | --- |
| Reviewer | Separate reviewer subagent. Fresh context, started from the assignment file only; the author's conversation was not an input |
| Model / effort | Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high` |
| Date | 2026-09-25 |
| Prepared commit | `4fd1b512f9e4db0402537bfe577031a6cc6939f6` |
| Previous commit | `5151b5700f50fc494b167cc7c4d742c8fc17cc13` (the only commit between them is `4fd1b51`, "Add the draft best-estimate side-strength ledger and checker") |
| Bundle / worktree HEAD | `266bcbdca528ab97f7238d70b0a070db3565fbe9` |
| `assignment.md` sha256 | `cc80e1fb357bb71759747abee1e0efba618be3e6098874520920fd67ae4f0785` (verified) |
| `inputs.json` sha256 | `3c3d44031bacf0e03bb86c936b63bd653ee3cb7c887a350425dcfc622490c388` (verified) |
| Input hashes | All 25 paths in `inputs.json` match `git show 4fd1b51:<path>` and the worktree. **No mismatch.** Key hashes: ledger `3408b06a…5b29ba`, `estimates.py` `4135ba25…0bf17`, Livermore transcription `e9fc742f…d3225`, `cwsac_forces.csv` `a462f6be…d7dd5` |
| Also read (named by the assignment, not bound in `inputs.json`) | `docs/strength-estimates.md` `795212ad…4ba3` (equals the ledger's design binding), `docs/feature-admission-reported-strength.md` `0699152d…c9f48`, `docs/research/reported-strength-scoping-v1.md` `aa8bb163…a89a1a`. These files are identical at `4fd1b51` and HEAD |
| Outcome | **Corrections required**: R1–R7 below. Advisories A1–A10 are listed separately |

This is an AI review. It is a separate analysis, not human historical adjudication,
independent corroboration, feature admission or authorization of any fit.

## Commands run (offline)

- `make check`: exit 0; 107 tests, OK.
- `python3 -m generalship estimate-check`: 91 in scope and 36 out of scope. Side grades
  A/B/C/D are 62/25/23/72. Fit-eligible rows are 21/31/40, with 6 excluded as post-start.
  `fitted: false`, 0 promoted rows. The ledger replays as recorded.
- I ran no build, packet or network command. To inspect the ledger, I read it in memory
  with the repository's own functions (`_passage`, `citation_text`, `estimate_side`),
  which also recomputed the effect of each proposed correction. The inspection dumps and
  the `make check` log went to `/tmp`, outside the repository. The only file I wrote in
  the worktree is this review.

## Scope actually inspected

- **Engagements:** all 21 assigned records, in ledger order: IN001, OH001, OH002, TN018,
  GA003, GA004, TN019, TN020, VA040, VA042, TN021, TN022, WV012, TN023, TN024, GA005,
  TN025, TN026, TN027, TN028 and TN029. I checked both sides of each.
- **Inputs:** every ledger input on those 42 sides, 62 in all. For each one I read the
  quote and its surrounding passage text, as resolved from the bound dossier citation or
  the frozen CSV cell. I checked each input's side, printed value, bounds, basis, codes,
  `loss_timing`, `bound`, `reproduction_of` and class. I read every citation in each
  dossier's `reported-force-scope` and `opening-personnel-unknown` claims; these are the
  only strength claims in the 21 dossiers, and none has typed quantities.
- **Frozen CWSAC data:** the `cwsac_forces.csv` rows for all 42 sides, and the
  `cwsac_battles.csv` dates for the 21 records.
- **Livermore:** the `livermore-transcription-v1` sections p105, p106 and p107. I checked
  them against the page images `livermore-p105.jpg`, `livermore-p106.jpg` and
  `livermore-p107.jpg`, including the footnotes.
- **Not inspected:** source passages beyond the bound selections, and other batches'
  engagements. I looked at the MD002 and MS006 inputs only as a consistency comparison
  for R5.

## Required corrections

Each correction gives the ledger input and field, the new value and the recomputed
result. I computed each result with the ledger's own `estimate_side` and `estimate_row`;
only these fields changed. I checked the class, grade and label outcomes against design
§§3–5 and did not re-derive the rules.

### R1 — OH002 Salineville: a Union figure is recorded as a Confederate opponent estimate

- **Evidence:** the input `cs-shackelford-375` quotes "he had about 375 fresh men and
  horses and three pieces of artillery". The passage (or23-1 Shackelford, p.643) reads
  "I met Major Rue, feeding… He at once reported to me for orders, remarking that he had
  about 375 fresh men…". "He" is Major Rue, a Union officer reporting to Shackelford, and
  the dossier claim says "Major Rue brought about 375 fresh men". The figure is part of
  the **US** force, and the Confederate side should not carry it as an
  `adversary_or_hearsay_estimate`.
- **Correction, Confederate side:** remove input `cs-shackelford-375`.
- **Correction, US side:** add input `us-rue`, with the same `source_id`, `ref`,
  `printed` (375/375), `document_key` and `independence_group`, and:
  - `basis` `unknown`;
  - `codes` `["partial_scope"]`;
  - `loss_timing` `none`;
  - `adjustments` `[]`;
  - `bound` `"lower"`;
  - `class` `"bound"`;
  - `note` "Major Rue's Union detachment only".
- **Correction, inventory:** in `reported-force-scope`, replace `cs-shackelford-375` with
  `us-rue`.
- **Result:** no estimate change. US stays A 2,600 (2,470–2,730) and CS stays A 400
  (380–420). This corrects a side attribution only.

### R2 — GA003 Davis' Cross Roads: Hindman's column is part of the Confederate force

- **Evidence:** `cs-hindman-column` ("putting a column of 15,000 troops in motion") is
  Hindman's own column. Two other cited passages present Cleburne's division as a separate
  component of the attack:
  - Hindman's report (citation 2): his instructions were "to unite at Davis' with
    Cleburne's division, of Hill's corps, and attack";
  - Cist (citation 5): "Cleburne will attack in front the moment your guns are heard",
    with Walker's corps ordered to join Cleburne at Dug Gap.

  Tier-2 §3 item 1 makes a figure "that the source, or another cited passage, presents as
  one part of that side's force" `partial_scope`. The ledger codes it as a class B
  whole-side figure (`codes: []`).
- **Correction, Confederate side, `cs-hindman-column`:**
  - `codes`: `["partial_scope"]`;
  - `bound`: `"lower"`;
  - `class`: `"B"` → `"bound"`;
  - `note`: "Hindman's column only; Cleburne's division at Dug Gap was a separate part".
- **Result:**
  - The Confederate side changes from **B 15,000 (12,750–34,500)** to **C 30,000
    (21,000–39,000)**, `point_basis` `unknown`.
  - The labels become `applicability_unresolved`, `basis_mixed`, `single_input` and
    `whole_engagement_leakage`; point and range groups are `[cs-cist]`.
  - The 15,000 lower bound sits below `low` and has no effect.
  - The row stays in `set3_ABC`, and the US side is unchanged.
  - The rationale text needs updating.

### R3 — TN019 Blountsville: a figure for the force at Zollicoffer sets the Confederate range

- **Evidence:** `cs-foster-est` ("They are reported as about 6,000 strong") comes from
  Foster's September 19 dispatch. It describes "a large force of rebels… stationed at
  Zollicoffer… mostly infantry", which Foster planned to attack "to-morrow". Jones's
  report (citation 6) shows that action at Zollicoffer on September 20. The frozen record
  is Blountsville on September 22, where the Confederate force was the "1st Tennessee
  Cavalry Regiment and Artillery (approx. 1,200)". The dossier's own rationale says:
  "Earlier reports concern other places and dates."
- **Why it matters:** the source ties the figure to another place, date and body of
  troops, so the link is not merely uncertain. It is `other_engagement`, as the ledger
  already codes TN023 `us-stevenson`. As coded now, it raises the Confederate `high` from
  1,260 to 6,000 under rule 5.
- **Correction, Confederate side, `cs-foster-est`:**
  - `codes`: `["adversary_or_hearsay_estimate", "other_engagement"]`;
  - `class`: `"C"` → `"unusable"`;
  - `note`: "force at Zollicoffer, September 19; not the Blountsville force".
- **Result:**
  - The Confederate side changes from A 1,200 (1,140–**6,000**) to **A 1,200
    (1,140–1,260)**, with the same labels.
  - The row stays incomplete, because the US side is grade D.

### R4 — TN020 Blue Springs: "did not fall far short of 15,000" is a one-sided bound

- **Evidence:** `us-williams` quotes "which did not fall far short of 15,000 men". That
  phrase means "nearly 15,000", which tier-2 §3 item 4 lists as a one-sided printed bound
  (`one_sided_bound`).
- **Consistency:** the ledger codes the parallel phrases this way elsewhere in the batch:
  - OH001 `cs-duke-cap`, "scarcely nineteen hundred";
  - TN023 `us-burnside`, "but little over 5,000".

  By contrast, IN001's "did not vary far from 3,000" is two-sided and correctly remains a
  value.
- **Correction, US side, `us-williams`:**
  - `codes`: `["adversary_or_hearsay_estimate", "one_sided_bound"]`;
  - `bound`: `"upper"`;
  - `class`: `"C"` → `"bound"`.
- **Result:**
  - The US side changes from **C 11,250 (7,500–15,000)** to **grade D**.
  - `null_reason`: "No usable candidate value in any inspected source; Williams's
    'did not fall far short of 15,000' and 'at least 5,000' are opponent one-sided
    bounds, and the Ninth Corps 6,000 is a partial arrival figure."
  - The row stays incomplete, because the Confederate side is grade D.

### R5 — WV012 Droop Mountain: the opponent estimate's basis and Jackson's earlier estimate

- **R5a, evidence:** `us-echols-est` quotes "The force of the enemy engaged was about
  7,000", so the passage states the engaged basis. Tier-2 §4 reads the basis from the
  cited passage, and the ledger records a stated basis on opponent estimates elsewhere:
  - MS006 `us-bowen-est` ("the enemy's force engaged exceeded 20,000") is
    `reported_engaged`;
  - GA004 `us-bragg-est` is `reported_effective`.

  The 7,000 is coded `unknown`.
- **R5a, correction:** US side, `us-echols-est`, `basis`: `"unknown"` →
  `"reported_engaged"`.
- **R5b, evidence:** `us-jackson-est` quotes "The estimate of Colonel Jackson placing
  their numbers at 3,500 was correct at the time when made…". The same sentence continues:
  "but they were re-enforced during the night previous to the battle". So the source
  presents 3,500 as the Union force before reinforcements arrived, which is one part of
  the force at the engagement, not the force brought to it.
- **R5b, correction:** US side, `us-jackson-est`:
  - `codes`: `["adversary_or_hearsay_estimate", "partial_scope"]`;
  - `bound`: `"lower"`;
  - `class`: `"C"` → `"bound"`;
  - `note`: "Union force before the overnight reinforcement, per Echols".
- **Result:**
  - The US side changes from **C 2,630 (1,750–7,000), basis `unknown`** to **C 5,250
    (3,500–7,000), `point_basis` `reported_engaged`**. The method stays
    `rule4_opponent_only`. The labels become `opponent_estimate_point`, `single_input`
    and `whole_engagement_leakage`.
  - The Confederate side stays A 1,700 (1,620–4,000), but `basis_mixed` is removed.
  - The row stays in `set3_ABC`.
  - With R5a alone, the US side would be C 5,250 (1,750–7,000).
  - The current point, 2,630, falls below Jackson's pre-reinforcement figure. That
    implausibility traces to these two coding errors, not to the rule.

### R6 — TN027 Mossy Creek: the Confederate scope is unresolved in the cited passages

- **Evidence:** `cs-martin` quotes "I engaged the enemy at 9 a.m. with all my guns and
  2,000 men". That is the force of Martin's own cavalry command. Two bound passages say
  Confederate infantry also supported the attack:
  - Sturgis's 3.15 p.m. dispatch (citation 3) reports "the mass of his cavalry and a
    division of infantry and two batteries of artillery";
  - the frozen force text (citation 0) reads "Sturgis reported that the Confederate
    cavalry was supported by a brigade of infantry".

  The dossier marks the claim `disputed`. The cited passages therefore do not settle
  whether Martin's command was the whole Confederate force. Tier-2 §3 item 1 codes that
  case `scope_unresolved`; the ledger codes the input as class A with `codes: []`.
- **Correction, Confederate side, `cs-martin`:**
  - `codes`: `["scope_unresolved"]`;
  - `class`: `"A"` → `"C"`;
  - `note`: "Martin's own command; Sturgis and the frozen field report Confederate
    infantry support".
- **Result:**
  - The Confederate side changes from **A 2,000 (1,900–2,100)** to **C 2,000
    (1,400–2,600)**.
  - The labels become `applicability_unresolved`, `compiled_dependence`,
    `derivation_unknown` and `whole_engagement_leakage`.
  - The row stays incomplete, because the US side is grade D.

### R7 — GA004 and TN024: footnote figures in Livermore entries are not inventoried

Design §7 requires every figure in a matching Livermore entry to be an input or to be
recorded with a reason. Both inventories say only "component lines precede the totals".
The page images carry total-level footnote figures that the inventories do not mention,
and the transcription omits those footnotes ("some notes are omitted"). None of them
changes an estimate:

- **GA004** has no inventory reason for two figures in p.106 note 2:
  - "General Longstreet's estimate of 5000 as the number carried into action", which
    covers his corps only;
  - "General Longstreet's estimate (p. 458) of 59,242 as the number engaged
    September 20", which covers one day and "omits the troops from Buckner's command".

  If it were an input, the 59,242 would be a lower bound on the engaged basis. It is
  below `low` (63,010), so it would have no effect.
- **TN024** has no inventory reason for p.107 note 1: "If it should be excluded, it
  would reduce the number engaged to about 51,000." This is an alternative total that
  Livermore rejects.

**Corrections:**

- GA004 `inventory.livermore.reason`: "component lines precede the totals; p.106 note 2
  gives Longstreet's 5000 carried into action (his corps only, partial) and his 59,242
  engaged on September 20 (one day, omitting Buckner's troops: partial interval and
  scope); p.105 notes 3–4 give component and adjustment estimates; the notes are not in
  livermore-transcription-v1".
- TN024 `inventory.livermore.reason`: "component lines precede the totals; p.107 note 1
  gives about 51,000 engaged if the 2d division, 14th corps were excluded, an alternative
  Livermore rejects; p.106 notes 4–5 and p.107 notes 3–5 give component estimates; the
  notes are not in livermore-transcription-v1".

### Aggregate effect of R1–R7

| Measure | Now | After R1–R7 |
| --- | --- | --- |
| Side grades A/B/C/D | 62/25/23/72 | 61/24/24/73 |
| Fit-eligible rows (sets A/AB/ABC) | 21/31/40 | 21/31/40 (unchanged) |
| Rows excluded as `post_start_information` | 6 | 6 (unchanged) |

Five rows of the memo table in `docs/research/strength-estimates-ledger-v1.md` would need
updating: GA003, TN019, TN020, WV012 and TN027. The ledger's rationale fields would also
need updating.

## Advisories (no class, grade, point, range or label change as the ledger stands)

- **A1 — IN001:** `cs-nps-raid` (2,450 on July 2) and `cs-duke` (2,460) are raid-start
  figures. Extractor policy 4 names departures as `engagement_link_unknown`; the ledger
  codes them `scope_unresolved`. Both codes fall in row 4, so the outcome is the same.
- **A2 — OH001:** `us-hobson` (2,500 on July 6 at Lebanon) predates the engagement.
  Hobson also says "but a small portion of my command was here", so the figure is not a
  valid lower bound on the Union force at Buffington.
  - Suggested coding: `codes` `["partial_scope", "engagement_link_unknown"]`, `bound`
    null.
  - It has no effect now, because its basis (`unknown`) does not match `point_basis`.
- **A3 — OH002:**
  - The inventory reason "Duke's column sizes are partial" is inaccurate. The two
    reorganized brigades were the whole command after Buffington, but each figure is
    one-sided ("a little more than four hundred"). The figures also predate Salineville,
    and Duke, not an eyewitness, reports them. Suggested reason: "one-sided and
    pre-engagement".
  - `cs-shackelford-400` describes the state after Way's fight at Salineville on the
    same day. It could carry `loss_timing` `not_prior`. It is an opponent estimate below
    `high`, so there is no effect.
- **A4 — TN019:** Jones's figure for the Union force `us-jones` ("Their force engaged
  to-day…", September 20 at Zollicoffer) also belongs to the other action. Its stated
  basis is engaged. Suggested coding: add `other_engagement`, with `basis`
  `reported_engaged`. The US side stays grade D.
- **A5 — TN020:** `us-ninth-corps` is an arrival figure dated September 30, before the
  engagement. Suggested coding: add `engagement_link_unknown`. There is no effect.
- **A6 — TN022:** `us-hatch` records `reproduction_of: us-cw`. That direction is reversed,
  since an 1863 report cannot reproduce the modern CWSAC table, and no passage shows the
  dependence.
  - Keeping the link is conservative, because it stops two equal figures counting as
    two inputs.
  - Suggestion: record it on `us-cw` instead (`reproduction_of: us-hatch`), with a note
    that the dependence is inferred from equal values. The grouping and estimate are
    unchanged.
- **A7 — GA004 `cs-lv` and TN024 `us-lv`:** Livermore prints "Total engaged", but both
  totals are sums of effectives lines. I checked the arithmetic against the page images:
  - p.106: 30,871 + 15,253 + 5,942 + 9,365 + 4,895 = 66,326;
  - p.107: 53,820 + 2,539 = 56,359.

  The ledger follows the printed label, which is consistent with the scoping memo, so
  this is not a required correction. If GA004 `cs-lv` were read as `reported_effective`,
  the Confederate `high` would change from 69,640 to 73,500 and `basis_mixed` would
  drop. The primary should decide which reading to use and apply it the same way to
  both totals.
- **A8 — Upper bounds on part of a side:**
  - TN024 `us-hooker` ("less than ten thousand", Hooker's force) and TN029 `us-wolford`
    ("at most 900", Wolford's division) are coded `bound: "upper"`. A cap on one part of
    a side does not cap the whole side; rule 7 admits partial figures only as lower
    bounds. Set `bound` to null.
  - TN027 `us-martin-est` ("Up to this time… not greater than 4,000") is limited to part
    of the interval, and Martin later reports a larger force. Add `partial_interval` and
    set `bound` to null.
  - None has an effect now, but each would wrongly cap `high` if the bases aligned.
- **A9 — TN026:** `us-desc` ("Parke sent… Shackelford on with about 4,000") is a
  departure figure, which policy 4 names. The description does go on to put Shackelford
  at Bean's Station and says he "deployed his force", which arguably ties the figure to
  the engagement.
  - If the primary codes it `engagement_link_unknown`, the US side becomes C 4,000
    (2,800–5,200).
  - The row is incomplete either way. The primary should decide.
- **A10 — TN025:** `us-burnside` (12,000 effectives in Knoxville) is dated to the start
  of the siege, about 11 days before the Fort Sanders assault. `engagement_link_unknown`
  could sit beside `scope_unresolved`. The class and labels are the same either way.

## Confirmed without correction

- **Frozen CWSAC figures:** IN001, OH001, OH002, TN019, TN022 and TN027 match
  `cwsac_forces.csv`. Each is referenced by an input, and the table basis and
  `derivation_unknown` are applied as the policy states. The TN027 `cs-cw`
  `source_role_unresolved` coding matches the ambiguous attribution in the frozen text.
- **IN001:** the US figure 400 and the Confederate figure 1,800 are correct, and the
  range from the Burnside 3,000 opponent estimate is mechanically correct.
- **OH001:** 3,000 and 1,700 are correct. Duke's "scarcely 1,900" is correctly a
  one-sided bound. Duke's figures for Judah and Hobson and the 8,000–10,000 hearsay are
  correctly recorded with reasons.
- **GA004:**
  - The US point is 55,000 (52,250–61,130): Cist's 55,000 and Livermore's 58,222 on the
    effective basis.
  - The Confederate point is 66,330 (63,010–69,640) on the engaged basis.
  - The Livermore US "Total engaged 53,919" is correctly partial scope. Per p.105, it
    covers infantry and artillery, with cavalry listed separately.
  - `us-cist-pfde` (the September 20 return) is correctly `post_engagement_state`.
  - Bragg's September 27 return (38,846) is correctly recorded as post-engagement.
- **TN024:**
  - The Confederate 44,010 includes Stevenson's December 10 return (p.107), so it is
    correctly `post_engagement_state`. The row is therefore excluded as post-start.
  - "Deduct Johnson's brigade…" removes absent units, not losses, so `loss_timing`
    `none` is correct.
- **TN023:** the Confederate side is C 20,000 (14,000–26,000). That is Longstreet's
  planned force, `engagement_link_unknown`, with the opponent estimate correctly dropped
  from the point. `us-stevenson` is correctly `other_engagement`. The US side is correctly
  grade D, with a one-sided bound only.
- **TN025:** the Confederate side is a rule-4 opponent point, 16,130 (10,750–21,500),
  computed correctly from the printed range 20,000–23,000.
- **Grade D sides:** I found no usable figure in the inspected passages for these sides,
  and their recorded reasons are accurate:
  - both sides of TN018, VA040, VA042, TN021, GA005, TN028 and TN029;
  - the US side of TN019, TN023 and TN027;
  - the Confederate side of TN020 and TN026.

  GA005's Confederate 4,157 counts "bayonets" (infantry only), so it is correctly
  partial scope.
- **Inventory:** apart from R1's reassignment and R7's footnotes, every strength-claim
  citation and figure in the 21 dossiers is referenced by an input or has a reason. The
  21 dossiers have no typed quantities.

## Limits

- I judged coding only against the bound passages, the design, the tier-2 codes and
  the extractor policies. I did not re-derive the rules or propose new sources.
- R2, R5b and R6 turn on scope as the cited passages present it. They are not
  historical findings about which troops fought.
- The GA004 and TN024 footnote figures in R7 were read from the page images. The
  registered transcription omits them.
- The primary agent should check these findings before changing evidence. Nothing here
  admits a feature, changes frozen inputs or authorizes the design §6 evaluation.
