# Best-estimate ledger: separate review, batch 1 of 4

**Outcome: corrections required** (findings R1–R7; advisories A1–A9).

| Field | Value |
| --- | --- |
| Reviewer | Separate Claude subagent, fresh context, no access to the author's conversation |
| Model / effort | `claude-opus-5-5` (Claude Opus 5.5), reasoning effort `high` |
| Date | 2026-09-25 |
| Prepared commit reviewed | `4fd1b512f9e4db0402537bfe577031a6cc6939f6` (against `5151b5700f50fc494b167cc7c4d742c8fc17cc13`) |
| Bundle commit / worktree HEAD | `a8b422c35f4493a706854802cfbf5fb295f0fbc9`. `git diff 4fd1b51 a8b422c` touches only the two bundle files, so every other path read here equals the prepared commit |
| Assignment | `assignment.md` sha256 `e8eac8d4aa7aa4e09c8c06e52de93cee13238e1f3636e47834bbca0bd58a9255` (verified) |
| Input manifest | `inputs.json` sha256 `3c3d44031bacf0e03bb86c936b63bd653ee3cb7c887a350425dcfc622490c388` (verified) |
| Input hashes | All 25 bound paths match `git show 4fd1b51:<path>` and the worktree. **No mismatch** |
| Unbound files also read | `docs/strength-estimates.md` `795212ad…4ba3` (equals the ledger's design binding); `docs/feature-admission-reported-strength.md` `0699152d…c048`; `docs/research/reported-strength-scoping-v1.md` `aa8bb163…a1a`. Dossiers were checked through the ledger's own dossier bindings (`estimate-check` passes). Examples: KY005 `1cb8213c…dfdd`, TN002 `4b8100e7…fc05`, NC002 `de65f380…b7be`, TN003 `fb622c81…0ee`, MS016 `d5e4f027…e78e`, VA017 `dd25a6aa…eaea` |
| Checks run offline | `make check`: 107 tests OK, exit 0. `python3 -m generalship estimate-check`: exit 0, 91 in scope / 36 out of scope, grades A/B/C/D 62/25/23/72, fit-eligible 21/31/40, 6 post-start exclusions. No build or packet command was run, and no primary artifact was modified |

This is an AI review. It is not historical adjudication, not independent corroboration, and not feature admission. It authorizes no fit.

## Scope actually inspected

The review covered all 25 assigned engagements: KY005, KY006, TN001, NC002, TN002, MO012, NC003, NC004, VA101, TN003, MS016, VA102, VA012, WV009, VA103, VA104, VA013, NC006, TN004, TN005, VA105, VA106, VA016, VA017 and VA021. For each side I checked the following:

- **Inputs and passages.** Every recorded input (69 inputs across the 25 engagements). Each quote was resolved through `citation_text` and read in about ±500 characters of passage context. Longer passages were read for the Garfield January 11 and 14 reports (KY005), the Grant chapter XXII rows 412/445 (TN002), the OR 10.1 returns (TN003) and the Grant chapter XXVI row 547 (MS016).
- **Estimates.** Every estimate was replayed with `generalship/estimates.py`, and proposed changes were replayed the same way.
- **Inventory.** Every dossier `strength` claim with all its citations, and the frozen CWSAC forces rows. For TN003, all 40 typed quantities (id, entity, value, basis, period, scope) were listed and compared with their inventory reasons.
- **Figures in other claims.** A regex scan of the non-strength claims in 24 of the dossiers, all except TN003, for missed troop figures.
- **Livermore.** The transcription sections p78, p79, p80, p82, p83, p84 and p85, each compared against its **page image** (`livermore-p78/79/80/82/83/84/85.jpg`).
- **Not done.** No other Livermore pages and no OCR text were read. There was no network access and no new source.

## Required corrections

Each correction was replayed with the unchanged estimator. The "result" lines give the reproduced values.

### R1: KY005 Middle Creek, US: our completed sum adds a later arrival

- **Evidence.**
  - Garfield, 11 January (`or7-garfield-selections-v1`, section `garfield-1862-01-11`): "at 1 o'clock p. m. we engaged his force … Fought them until dark. Having been re-enforced by 700 men irom Paintsville, drove tbe enemy from all their positions."
  - Garfield, 14 January (`garfield-1862-01-14`): the fight opens around noon, and "At 4 o'clock the re-enforcement under Lieutenant Colonel Sheldon, of the Forty-second Ohio, came iu sight".
  - The 700 therefore arrived during the action, not before it. The input note "reinforcement joining before the action" contradicts both reports.
  - Design §4 rule 6 says "A sum never adds an initial force to later arrivals", and requires one state time. The bound dossier's own rationale says "do not sum them".
- **Changes** (engagement KY005, side US):
  1. Delete input `us-sum` (the `completed_sum` of `us-left` and `us-reinf`).
  2. Input `us-reinf`, field `note`: "reinforcement from Paintsville that arrived during the action (11 Jan: after 'Fought them until dark'; 14 Jan: 'At 4 o'clock the re-enforcement … came in sight')".
  3. Side `null_reason`: "No candidate value. Garfield's departing force (1,100) and a reinforcement that arrived during the action (700) are partial, with unstated basis, and design §4 rule 6 forbids summing them. His 'Not more than 900 … actually engaged' is a one-sided engaged-basis upper bound, recorded beside the null."
  4. `rationale`: "No Union candidate: Garfield's components are partial and cannot be summed across an arrival. Confederate from Garfield estimates and the NPS narrative."
- **Result.**
  - US: grade D, point, low and high null, method `grade_D_no_candidate`, labels `[whole_engagement_leakage]`.
  - Confederate: unchanged at C 1,880 (1,250–2,500), but `basis_mixed` drops. Labels become `[opponent_estimate_point, single_input, whole_engagement_leakage]`.
  - `nested`: `{"sets": [], "excluded_post_start_information": false}`.

### R2: TN002 Fort Donelson, US: a starting force is used as the whole-interval force

- **Evidence.**
  - `us-start` quotes "I started from Fort Henry with 15,000 men…". That is the force at the start.
  - The same source (row 445, input `us-final`) gives "On the day Fort Donelson fell I had 27,000 men to confront the Confederate lines and guard the road". Within the frozen interval 1862-02-11 to 02-16, the side's force therefore grew beyond the starting 15,000.
  - Design §1 targets the whole force over the interval. Tier-2 §3 items 5–6 treat an initial force and later arrivals as separate parts. Design §4 rule 7 names partial-scope figures as lower bounds.
  - The ledger itself codes the analogous KY005 departing force, `us-left`, as `partial_scope`.
- **Change** (engagement TN002, side US, input `us-start`):
  - `codes`: `[]` → `["partial_scope"]`
  - `bound`: `null` → `"lower"`
  - `class`: `"B"` → `"bound"`
  - `note`: "starting force from Fort Henry; the same chapter reports 27,000 in the lines by the day the fort fell, so this is part of the whole-interval force"
  - Update `rationale` accordingly.
- **Result.**
  - US: C 27,000 (18,900–35,100), `point_basis` `unknown`, `point_groups`/`range_groups` `[us-final]`. Labels `[basis_mixed, compiled_dependence, post_start_information, single_input, whole_engagement_leakage]`. The 15,000 lower bound falls below `low` and has no effect.
  - Confederate: unchanged.
  - `nested`: `{"sets": ["set3_ABC"], "excluded_post_start_information": true}`. The row leaves the fits as post-start.

### R3: NC002 Roanoke Island, US: a narrative restatement is given the table basis and linked as a reproduction

- **Evidence.**
  - `us-nps-landed` quotes the NPS **Description**: "Burnside landed 7,500 men on the southwestern side of Roanoke Island". It states a landed population, not forces engaged.
  - The bound dossier claim contrasts the two: "The NPS narrative describes 7,500 Union men landing on February 7, whereas its structured table calls the numbers forces engaged."
  - Tier-2 §3 item 3 says a basis is never inferred from the role or the source.
  - The ledger memo's stated implementation choice is that NPS narrative restatements "are not recorded as reproductions", because linking them "would merge an engaged-basis figure with an unstated one".
- **Change** (engagement NC002, side US, input `us-nps-landed`):
  - `basis`: `"reported_engaged"` → `"unknown"`
  - `reproduction_of`: `"us-cw"` → `null`
  - `class`: `"A"` → `"B"`
- **Result.**
  - US: A 7,500 (7,130–7,880), engaged. `range_groups` `[us-cw, us-nps-landed]`. Labels `[compiled_dependence, derivation_unknown, whole_engagement_leakage]`: `single_input` drops.
  - `nested`: unchanged, set A.

### R4: TN003 Shiloh, Confederate: returns with unstated muster dates are coded as engagement-matched

- **Evidence.**
  - The bound dossier's typed quantities record `confederate-before` (40,335) as "Before Shiloh; underlying muster date unstated". They record `confederate-report-136-total` (38,773) as "Heading describes forces that marched April 3; exact muster date unstated". The present total 46,425 comes from the same report 136 table.
  - Livermore p.80 note 1 adopts the same undated field-return "effective total".
  - Tier-2 §3 item 2 says `engagement_link_unknown` "includes a return with an unstated muster date". Tier-2 §8 says "An unestablished state date is `blocked: engagement_link_unknown`". The extractor's policy 4, which accepts a return the source ties to the force, cannot override that explicit clause.
- **Change** (engagement TN003, side Confederate): add `"engagement_link_unknown"` to `codes` and set `class` `"A"` → `"C"` for each of `cs-return-before`, `cs-lv-eff`, `cs-r136-eff` and `cs-r136-present`.
- **Result.** No estimate changes. The point stays with `cs-cw` on `reported_engaged`, and the effective and present candidates lie on other stated bases (rule 5). Estimate: A 44,970 (42,720–47,220), labels unchanged. Only the input classes change.

### R5: MS016 Corinth: the figures' period is part of the frozen interval, and this is not coded

- **Evidence.**
  - The passage reads: "Beauregard had, during the month of May, 1862, … probably not much over 50,000 effective men. We estimated his strength at 70,000. Our own was, in round numbers, 120,000."
  - The frozen interval is 1862-04-29 to 1862-06-10. The bound dossier's rationale says the memoir gives these "without an exact estimation date".
  - Whether the figures are limited to part of the interval is therefore unresolved (tier-2 §3 item 2). `us-grant-own` currently carries no code and is class B.
- **Change** (engagement MS016): add `"interval_unresolved"` to `codes` for:
  - US `us-grant-own` (`class` `"B"` → `"C"`);
  - Confederate `cs-grant-50000` and `cs-grant-70000` (class stays `"C"`).

  (`engagement_link_unknown` would give the same class and labels.)
- **Result.**
  - US: C 120,000 (84,000–156,000), unknown basis, labels `[applicability_unresolved, basis_mixed, single_input, whole_engagement_leakage]`.
  - Confederate: C 37,500 (25,000–70,000). `applicability_unresolved` is added to its labels.
  - `nested`: unchanged, `set3_ABC` and not excluded.

### R6: TN002 inventory: the Livermore reason is inaccurate and incomplete

- **Evidence.** The p.78–79 page images show that note 4 contains:
  - "16,623 were killed, wounded, and captured, and at least 2000 more escaped";
  - present for duty in Buckner's division, 4,481 (January 31), and in Tilghman's, 3,830 (January 21);
  - Floyd's brigade, 1,286, "after the battle";
  - Johnson's division, "at least 7500" at average regimental strength;
  - the 30th Mississippi's battle loss of 532;
  - "This gives a total of at least 17,530".

  The recorded reason, "note 4 lower bound of 17,530 uses post-battle captures", misdescribes the 17,530 and omits the other figures.
- **Change** (engagement TN002, `inventory.livermore.reason`): "Note 4 (pp.78–79) figures not entered: 16,623 killed, wounded and captured and at least 2,000 escaped are losses and captures of this engagement; Buckner 4,481 (Jan 31) and Tilghman 3,830 (Jan 21) are partial-scope earlier returns; Floyd's brigade 1,286 is an after-battle return; Johnson's division 'at least 7500' is a regimental-average estimate. The note's 'at least 17,530' is a one-sided bound built from those components, the after-battle return and the note's battle-loss figure (bound-only; post-start); not entered."

### R7: VA017 inventory: part of the Livermore entry is not inventoried

- **Evidence.** Page image p.84 carries the continuation of p.83 note 7 for the Gaines' Mill Confederate army. It gives dated statements of numbers less losses before June 27, a "Total … 51,908", and "These additions would bring the total to about 57,000".
  - The inventory's `pages` field is `[82, 83]`, and its reason ("component lines precede the entered totals") does not cover these figures.
  - `livermore-transcription-v1` omits note 7, so these figures cannot be cited as inputs now.
- **Change** (engagement VA017):
  - `inventory.livermore.pages` → `[82, 83, 84]`.
  - Append to `inventory.livermore.reason`: "; p.84 note 7 (Confederate): component statements dated April 16–June 27 less prior losses, 'Total 51,908' (rank-and-file figures; officers and artillery probably excluded, so partial) and 'about 57,000' after estimated additions. Not entered because the registered transcription omits note 7."
- **Effect if later entered.** Checked by replay with a hypothetical C input: basis unknown, prior losses. The Confederate point would become 57,000, and the row would stay excluded as post-start, because the `cs-cw` group remains in the median.

### Consequential updates (arithmetic only, after R1–R5)

- Side grades A/B/C/D become 62/23/24/73.
- Fit-eligible rows: A 21, A–B 30, A–C 38.
- Post-start exclusions: 7.
- Newly covered fit-eligible rows: 16. Common rows: 22.
- `docs/research/strength-estimates-ledger-v1.md` should update these counts and the rows for KY005 (→ incomplete), TN002 (→ excluded, post-start) and MS016 (US C).

## Advisories (no required change)

- **A1, MS016.** "probably not much over 50,000" could be read as a one-sided bound. If it is coded that way, rule 4 rests on 70,000 alone: point 52,500, low 35,000, high 70,000. The approximate-value reading used is defensible, so this is left open.
- **A2, bound field.** Partial-scope inputs carry `bound: null`: KY005 `us-left` and `us-reinf`, and TN003 `us-atenn-pfd`. Design §4 rule 7 treats partial figures as lower bounds, so `"lower"` would be more consistent. There is no effect in this batch, because of grade D or a basis mismatch.
- **A3, TN003 `us-force-sunday`.** The input is recorded as 32,000–32,000, "thirty-two thousand". The passage and dossier quantity `force-sunday-engaged` read "thirty-three thousand or thirty-two thousand" (32,000–33,000). Keeping 32,000 as the conservative lower bound is fine, but say so in `note`. It has no effect: it is below `low`.
- **A4, VA101 `cs-desc`.** "his 3,400-man division" names a formation, while CWSAC gives the side 3,800. `scope_unresolved` is arguable, and would only add `applicability_unresolved` to the Confederate range.
- **A5, VA016 Livermore.** The printed present-for-duty total 16,808 (June 20) is a whole-side sum on another basis, not a "component line". Record it as a `present_for_duty` input or name it in the reason. It has no estimate effect.
- **A6, transcription fidelity.**
  - p84 and p85 (composite entry) omit the deduction and subtotal lines: 12,920; 4,150; 17,070; 98,032; 4,528; 65,204; 4,945; 11,045; 88,113; 1,365.
  - p78 and p79 omit most of note 4.
  - The TN003 Livermore reason does not mention the Army of the Ohio 20,000 line or the note 3 figures (44,895; 1,000; 5,463).

  VA021 is not affected, because its entry is composite and unusable. These gaps do conflict with the transcription note's claim that notes bearing on formation are transcribed.
- **A7, Livermore exclusions.** VA017 US note 6 excludes French's and Meagher's brigades, "as they arrived after the battle was decided". TN003 note 4 excludes the 6th division in the same way. I accepted both as the source's population, but they sit close to the R2 whole-interval issue. Keep them in view for consistency.
- **A8, outside this batch.** TN006 `cs-nps-desc` and KY009 `us-nps-desc` are NPS narrative inputs linked as reproductions on `reported_engaged`, the R3 pattern. They were not inspected here.
- **A9, bundle.** `inputs.json` binds neither the design, the tier-2 design, the scoping memo nor the dossiers. Their hashes were read at the verified commit and are recorded above.

## Items confirmed without change

The following were checked and need no change:

- **Livermore readings.** Every value checked against the page images is correct: p78 27,000 and 21,000; p79 62,682; p80 40,335; p82 15,631, 16,356 and 36,790; p83 34,214 and 57,018.
- **Roles.** Grant's figure adopted by Livermore is correctly coded `adversary_or_hearsay_estimate`. Pillow's relayed own report is correctly an own report.
- **Loss timing.** Correct for VA017: the US figures deduct only June 26 losses (`prior_engagements_only`), while the Confederate figure adds June 28–July 1 losses (`not_prior`).
- **Rule-4 arithmetic.** Correct for KY005 CS, TN001 CS and MS016 CS.
- **Grouping.** The CWSAC/Livermore groups are correct: VA016, both sides B with unknown basis; VA017.
- **Grade D sides.** These reasons are accurate, and no usable figure was found in the inspected sources:
  - KY006 US;
  - MO012: only a post-outcome surrender count;
  - NC003, NC004 US, VA012, WV009, VA013, NC006, TN004, TN005;
  - VA021: only the composite entry.
- **TN003 quantities.** All of the non-entered typed quantities are components, reinforcements, partial-phase or post-battle figures, as their reason states.
- **Remaining sides.** All other sides reproduce under design §§3–5 from correctly read inputs.
