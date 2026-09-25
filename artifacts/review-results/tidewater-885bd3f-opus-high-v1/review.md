# Longstreet's Tidewater Operations: separate source review (Opus 5.5, high)

- **Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), reasoning effort `high`. This was a fresh-context
  subagent. The author's conversation was not an input.
- **Date:** 2026-09-25
- **Reviewed commit:** `885bd3f97721982d5e431e2e720a2a93dc492b65`. **Previous commit:**
  `1bca6a0f7eeee9c12b9edfcfcaae01183576a90b`. **Bundle/worktree HEAD:** `b884e79bd4c9628ad27b766859f12c32ed78ce87`.
  Its only differences from 885bd3f are the assignment and inputs.json files.
- **Assignment** sha256 `541ded32390b029b28aa29dd3c987713cb5c2fcdba6a6d94f5722c8769366e1c`. **inputs.json**
  sha256 `e7329b8ea655de7a25e168a227f9765d4bb3ca9ec0271d1c5ae489ae57edf39f`. I checked all **44/44** bound input
  hashes against both the worktree and `git show 885bd3f:<path>`: **no mismatch**.
- **Outcome: corrections required.** The findings are TW-R1 to TW-R5. Notes TW-N1 to TW-N4 are optional.
- This is an AI review. It is a separate analysis, not human historical adjudication, independent
  corroboration, or feature admission. I did no network access, new research, extra source families or agents.
  This file is the only one I wrote.

## Scope actually inspected

- **Governing documents:** AGENTS.md, the evidence contract, the Tidewater memo and the prepared-commit diffs of
  README, methodology, roadmap, sources.md, cli.py, test_evidence.py, pilot-report and research-queue. I
  skimmed the full README, methodology and roadmap only where the diff touched them.
- **Dossiers:** all 4 frozen dossiers (NC010, NC011, VA031, VA030) and every claim: **38 claims, 4 null unknowns
  and 187 citation occurrences**. Each dossier has all 7 dimensions and 3 families (nps-cwsac, plus Foster and
  D. H. Hill for NC010 and NC011, or Peck and French for VA030 and VA031). I checked the value, status, phase,
  rationale and every citation against the text.
- **Sources read in full:** the 4 NPS text summaries and all 4 OR XVIII selections: Foster's six sections
  including the p.184 footnote, both Hill sections, Peck's May 5 report, and French's report with Longstreet's
  indorsement.
- **Parent OCR context:** I read the text around every selection boundary and the page markers in
  `or18-illinois-ocr-v1`. I did not read the whole volume.
- **Frozen rows:** the battle, force and commander CSV rows for all four IDs. The side-specific bounds are
  blank. The battle-level `Divisions (45,000 total)` / `45000` is shared by VA030 and VA031.
- **Registry and pipeline files:** the 12 new source records, receipt.json, the 4 research packets and
  battles.json. Baseline, admission-check and cohort were checked through the diff and hashes.

## Mechanical results (all pass)

- **Replays:** all 4 NPS HTML→text derivatives replay byte-for-byte under the recorded HTMLParser transform. All
  4 OR selections replay exactly: each of their 14 sections equals the recorded half-open character range of
  the parent, whitespace-collapsed. The parent hash and metadata are unchanged from 1bca6a0 and its raw file is
  untouched.
- **Quotes and locators:** all 187 quotes occur exactly (once per section for OR sources). CSV quotes sit in the
  exact row and cell, and NPS quotes in the named field. Every OR locator matches my independent page-marker map:
  - Foster starts on p.183, with `184 NORTH CAROLINA` → 184. The footnote precedes the p.185 marker.
  - The April 5 report starts on p.211, and April 23 is on p.212. The April 30 report runs pp.212–216.
  - Hill's report runs pp.188–189. Hill's letter is on p.1007, between the `COREESPONDENCE … 1007` and `1008`
    markers.
  - Peck runs pp.274–280, including `280 NOUTia` → 280.
  - French runs pp.324–326, including `Chap. XXX.] 325` → 325. The indorsement runs pp.326–327.
- **Counts:**
  - Registry: 373 records / 370 paths, with the previous 361 / 358 preserved as an identical prefix. All 373
    hashes match.
  - Dossiers: 76/127, 51 without. There are 19/36 complete campaign groups by presence.
  - The research queue changes only these four statuses.
- **Unchanged files:** all 72 older dossiers and 47 history files are byte-identical; the diff adds only 4
  dossiers. Also unchanged: cohort, both admission proposals, admission-check, baseline and battles.json.
- **Baseline:** 23 battles / 13 groups, with strength Brier 0.2768816348133779 against 0.25. There are 0
  promoted rows.
- **Receipt:** 137 input, 373 source and 7 output hashes all match.
- **Packets:** each packet has 3 JSON blocks. The dossier block equals the dossier and the registry block equals
  sources.json. The assigned-record block matches battles.json for dates, result, blank strengths and listed
  commanders.
- **Next group:** confirmed independently as **Cavalry Operations along the Rappahannock [March 1863], VA029**. It
  is the earliest start (1863-03-17) among incomplete groups.
- **`make check`:** exit 0, 82 tests OK and `artifacts_written: false`. I ran no build or packet command.

## Verified without correction

- **VA030 nested in VA031:** the VA030 interval (Apr 13–15) lies inside VA031's (Apr 11–May 4). All boundary
  notes say so. The 1,160 siege total is neither added nor assigned; VA030 has no engagement count.
- **Casualty differences:** frozen versus live values are correctly transcribed: Fort Anderson 7 / 0, Washington
  100 / 0, VA031 152 (1,160) / 0, VA030 (1,160) / 0.
- **Force scopes:** NPS 12,000 and 25,000 v. 20,000; Foster 13,000, 13–14,000, 7,000 and 1,200; Peck's mail
  40–60,000, "one-half", 15,000 + 15,000 and 10,000. They are kept separate and none is adopted.
- **April 24 dispute:** NPS ("easily repulsed") and Peck ("driven in confusion") are preserved as `disputed`.
- **OCR readings:** Peck's "10th" date and "1802" are reported as OCR readings rather than corrected. So are
  the "0 officers" quote and "H. H. HILL".
- **Command statements:**
  - Hill's statements on Whiting, Robertson and Garnett are quoted accurately.
  - Longstreet's "no … particular censure" and his 75-man statement are labeled a counterfactual and not
    adopted.
- **Ranks:** the frozen and live Brigadier General for Foster and Peck against their Major-General signatures,
  live Colonel Hill, and live Major General Longstreet are all correctly cited. None is adopted.
- **Disclosed groupings:** the compiler's footnote is counted with Foster, and Longstreet's indorsement with
  French. This is disclosed in open_questions, the memo and the source dependency notes, and is not treated as
  corroboration.
- **No attribution overreach:** no automatic sole credit, probability, morale score or additive credit appears.

## Required corrections

**TW-R1: NC011 `recorded-result` and the memo narrow Foster's causal judgment.** Foster (p.216) credits
the Kinston movement "with this latter movement" (Spinola at Swift Creek), *together with* Hill's information
of Heckman's reinforcement and Hill's failure after fourteen days. Only then does he conclude "in all probability
caused him to retreat". The value's "his combined movements" and the memo's "to his own movements" drop two of
the three stated grounds. That overstates Foster's self-credit.
- **Replace the value sentence** with: "Foster says the main body withdrew with the artillery on the night of the
  15th. He judges that the Kinston and Swift Creek movements, together with Hill's information of Heckman's
  brigade's arrival and Hill's failure to gain a single advantage after fourteen days of close siege, in all
  probability caused the retreat."
- **Add three p.216 citations to `foster-1863-04-30`:**
  - "The movement toward Kinston with this latter movement,"
  - "together with the enemy’s information of the accession of strength of Heckman’s brigade"
  - "after fourteen days of close siege of Washington General Hill had failed to obtain a single advantage"
- **Append to the rationale:** "The inspected reports do not date Prince's and Spinola's movements relative to the
  withdrawal on the night of the 15th."
- **In the memo, replace** "attributes Hill's retreat "in all probability" to his own movements" with
  "attributes Hill's retreat "in all probability" to the Kinston and Swift Creek movements together with
  Hill's information of Heckman's reinforcement and his failure to gain an advantage".

**TW-R2: the memo misstates French's surprise judgment, and VA031 `surprise-and-warning` is incomplete.**
French (p.325) poses a dilemma: "if the garrison was surprised, they were negligent; if not surprised, they did
not offer a sufficient resistance". He does not find that the garrison was surprised. Only Longstreet's
indorsement (p.327) says the command "seems to have been completely surprised".
- **In the value, replace** "French says the Hill's Point garrison was negligent if surprised" with "French
  says the Hill's Point garrison was negligent if surprised and, if not, offered insufficient resistance".
- **Add the citation** `french-1863-04-22`, p.325: "if not surprised, they did not offer a sufficient
  resistance."
- **In the rationale, replace** "the surprise judgments are French's and Longstreet's" with "French's judgment
  is conditional on surprise; only Longstreet's indorsement judges the command surprised".
- **In the memo, replace** "French and Longstreet's indorsement judge the Hill's Point garrison surprised"
  with "French judges the Hill's Point garrison negligent if surprised and insufficiently resistant if not;
  Longstreet's indorsement judges it completely surprised".

**TW-R3: VA031 `union-works` has an `inherited` tag that covers material that is not inherited.** The claim
includes Peck's Confederate siege works, which were built inside the Apr 11–May 4 interval. Peck also says the
Union work went on "From that time until the present" (p.275), meaning up to his May 5 report. The tag holds only
for the Union works that existed before April 11.
- **Split the claim (preferred).** Keep `union-works` as terrain, supported, `inherited`.
  - **New value:** "Peck says he was ordered to Suffolk on September 22 (OCR year '1802'), found no artificial
    defenses, began Fort Dix on the 25th, and from that time until his May 5 report worked to place the line of
    the river and swamp in a state of defense."
  - **Add the citation** p.275: "From that time until the present I spared no pains".
  - **New rationale:** "Only Union works existing before the frozen April 11 start are tagged inherited; they may
    be commander-created under a campaign boundary. Peck says the work continued until the present, so works
    added during the siege are not separable here and are not covered by this tag. No map verification or
    numerical effect."
- **Move the existing p.278 citation** "10 miles of batteries, covered- ways, and rifle-pits" to a new claim,
  `confederate-siege-works` (terrain, supported, `unresolved`).
  - **Value:** "Peck describes the Confederate siege works as not less than 10 miles of batteries, covered ways
    and rifle-pits."
  - **Rationale:** "An opposing commander's post-siege description of works built within the engagement
    interval; not inherited. No map verification or numerical effect."
- **Alternative:** if the primary prefers not to add a claim, set `union-works` to `unresolved` and put the same
  scope statement in its rationale.

**TW-R4: the VA031 `hill-point-work` link to Hill's Point is uncited, and the memo overstates it as a
dispute.** The cited p.324 sentence ("work built for the defense of the river when we held Suffolk") does not
name Hill's Point. French makes the identification only through sequence, in heavily garbled OCR:
1. There are two battery sites.
2. Stribling's guns are put "in the voik" (p.324).
3. On the 19th, "In the Hill's Point Battery were Stribling's battery" (p.325).

The corrections are:
- **Add two citations** to `french-1863-04-22`:
  - p.324: "to put the guns of Stribling’s battery in the voik."
  - p.325: "In the Hill’s Point Battery were Stribling’s battery,"
- **Prepend to the rationale:** "French does not name Hill's Point in the sentence on the work's origin; the
  identification is inferred from the report's sequence in garbled OCR."
- **In the memo, replace** "the Hill's Point work was a battery built on April 13 (NPS, VA030) or a work built
  when the Confederates held Suffolk (French)" with "NPS (VA030) says a battery was constructed on Hill's
  Point on April 13, while French's sequence places Stribling's guns in a river work built when the Confederates
  held Suffolk; these may conflict, but whether they describe the same work is not established".

The dossier's `supported` status and its "not established" rationale may stay.

**TW-R5: NC010 `casualty-records` silently corrects an OCR reading, and its scope is unstated.** The cited
OCR reads "2 killed and I 4 wounded", but the value and the memo say "2 killed and 4 wounded". Reading the "I"
as a margin artifact is plausible: the same paragraph has stray "|", "i" and "j" marks at its line edges. It is
still an unverified reading, and "14" is not excluded without print.
- **In the value, replace** "Foster reports his loss as only 2 killed and 4 wounded" with "Foster reports his
  loss as only 2 killed and 4 wounded (OCR '2 killed and I 4 wounded'; the 'I' is read as a margin artifact,
  not checked against print)".
- **Append to the rationale:** "Foster's figure covers the whole New Berne attack and the compiler's footnote
  only the 92nd New York; neither scope is shown to equal the frozen 7."
- **In the memo, add** "(OCR 'I 4')" after "4 wounded at New Berne".

**Count effect if all adopted:** 39 claims, 4 unknowns, and 187 + 3 + 1 + 1 + 2 = **194 citations**. NC011
becomes 48 citations; VA031 becomes 12 claims and 62 citations. The primary must propagate these counts to the
memo, README, roadmap, cli.py report text and regenerated artifacts, and should re-check each quote before
editing.

## Optional notes (not required)

- **TW-N1:** VA031 `recorded-result` omits Peck's officer count. It could add "(OCR '0 officers')" for
  symmetry with "10th". Similarly, French's "on the night of the 10th" (p.324, after "the 15th") is an
  uncited OCR date.
- **TW-N2:** the sources contain differences that are not recorded:
  - Foster's April 5 garrison (sixteen infantry companies) differs from his April 30 list (8 + 8 + 2
    companies).
  - Hill says "sixteen days" of siege and Foster "fourteen days".
  - Peck gives a heavy Hill's Point work "in progress" on the 18th (p.276).
  - None changes a claim, and all could stay deferred.
- **TW-N3:** `casualty-records` status is inconsistent across the four dossiers. NC010 and VA031 are `disputed`,
  while NC011 (100 / 0) and VA030 are `supported`, despite the same kind of frozen/live difference. Consider
  harmonizing.
- **TW-N4:** Peck's "10,000, with a pontoon train under the immediate command of General French" (VA030) is
  ambiguous: "under French" may modify the force rather than the train. Peck's Confederate loss components
  (400 + 500–600 + 500) sum to 1,400–1,500 against his printed "at least 1,500"; the figure is correctly
  retained as printed.

## Limits

I checked extraction and entailment against OCR selections that were not checked against print. No
manuscripts, returns, maps, navy reports or print were inspected. Automatic and manual passage checks do not
establish historical truth or source independence. No finding here admits a feature or changes frozen inputs.
