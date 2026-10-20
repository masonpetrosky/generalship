# Roadmap

This file holds the current priority, the decisions waiting on the owner and the status of each
milestone. Completed work is recorded in the [research log](research-log.md), which also keeps
everything this roadmap recorded up to 2026-10-06. Registered sources are listed in
[source additions](source-additions.md).

## Current priority: the French Revolutionary and Napoleonic Wars

The owner chose the Napoleonic Wars on 2026-09-25 and decided the seven scoping questions on
2026-10-06 ([scoping note](napoleonic-scoping.md),
[record](../data/napoleonic/owner-decision-scoping-2026-10-06.json)):

- **Frame:** Bodart's 1908 *Kriegs-Lexikon*, every entry for 1792–1815 in the wars France fought,
  frozen as printed.
- **First cohort:** the 1805–1815 campaigns.
- **Sides:** France and its allies against their opponents.
- **Outcome:** Bodart's recorded winner.
- **Sources:** each side's own public-domain sources.
- **Research:** strength and responsibility researched in full.

**Done (2026-10-06):** the frame is built and frozen ([design](napoleonic-frame.md)).

- Bodart's scan is pinned, and pp. 268–490 are transcribed twice from the page images, reconciled
  and audited.
- The frame holds **663 engagements** of 1792–1815 in France's wars, out of 708 entries.
- **Cohort v1** holds the **325 land engagements of 1805–1815** in 16 campaign groups.

**Done (2026-10-06 and 2026-10-16):** the evidence path. Napoleonic drafts have their own
directory and a validator bound to cohort v1, and a campaign group's packet is written from the
frame. Brief v2 adds the coded posture and fortification dimensions of decision 7, and the source
check now rebuilds every selection from its parent.

**Done (2026-10-18):** the bounded
[methods checkpoint](research/napoleonic-methods-checkpoint-v1.md). Its design/code were pushed
before execution. Five fixed synthetic scenarios ran with 100 recoveries and 20 validation
repetitions each; no historical outcome was fitted. The army-only scenario improves prediction
with zero commander effects. Planted commander effects are weakly recovered on conservative
printed labels. Actual commander–army identification is not assessed without a verified army
registry, and the worked campaign specification remains not estimable. All results and nulls
are retained. Compact packets, brief v3's checklist and reproducible research screens are in
use. Calibration is a prepared, unscored 47-task sample; no separate reviewer or subagent ran.

**First-pass research coverage complete (2026-10-19):** all 325 entries in all 16 complete groups, primary-verified. The dossiers hold 4,846 claims and 1,085 explicit unknowns; coverage is not reconciliation or feature admission:

| Group | Drafts | Recorded usage |
| --- | ---: | ---: |
| `third-coalition 1805` | 22 | about 14.6 million tokens |
| `third-coalition 1806` (Naples) | 4 | about 2.3 million tokens |
| `fourth-coalition 1806` | 23 | about 28.4 million tokens |
| `fourth-coalition 1807` | 19 | unavailable; no complete meter exposed |
| `peninsula 1808` | 17 | unavailable; no complete meter exposed |
| `peninsula 1809` | 19 | unavailable; no complete meter exposed |
| `fifth-coalition 1809` | 36 | unavailable; no complete meter exposed |
| `peninsula 1810` | 11 | unavailable; no complete meter exposed |
| `peninsula 1811` | 19 | unavailable; no complete meter exposed |
| `peninsula 1812` | 8 | unavailable; no complete meter exposed |
| `russia-1812 1812` | 31 | unavailable; no complete meter exposed |
| `liberation 1813` | 52 | unavailable; no complete meter exposed |
| `peninsula 1813` | 12 | unavailable; no complete meter exposed |
| `liberation 1814` | 34 | unavailable; no complete meter exposed |
| `peninsula 1814` | 3 | unavailable; no complete meter exposed |
| `hundred-days-1815 1815` | 15 | unavailable; no complete meter exposed |

The [research log](research-log.md) retains every batch, whole-group check and correction.
No first-cohort entry remains without a draft. The
[Hundred Days pass](research/hundred-days-1815-first-pass-v1.md) completes the group including
Italy, Belgian battles and frontier sieges, preserving strength, timing, command and closure
alternatives. Exact army identities, authority clocks and matched original local returns remain
unresolved. No additional first-pass or historical deep dive is queued merely because an old
packet retains an unknown.
This is source research; the final numerical evaluation reservation below remains unchanged.
The [1808 pass](research/peninsula-1808-first-pass-v1.md) records two source-family effort
overruns; its dossier screen does not erase them. Fix source-family assignments before substantive
reading in every new pass, as the [1809 pass](research/peninsula-1809-first-pass-v1.md) did.
Earlier usage rates describe the old workflow and are not a measured forecast for the new one.
There is no usage cap; the main session researches, drafts and verifies each group, as the
[2026-10-16 decision](../data/napoleonic/owner-decision-research-mode-2026-10-16.json) requires.

**Done (2026-10-19):** a bounded [strength/command ledger design](napoleonic-ledgers-v1.md),
worked on the smallest complete development group, `third-coalition 1806` (four entries/eight
sides). It indexes 31 strength/responsibility claims with 43 strength and 28 command-role
observations; 46 distinct cited passages were re-inspected on 26 pinned images. The
[result](../artifacts/napoleonic-ledger-design-v1.md) leaves all eight opening mappings blocked,
with null army identities and null force/person selections. No input was admitted or historical
outcome fitted.

**Done (2026-10-19):** the same entries' [boundary/membership specification](napoleonic-boundaries-v1.md),
with 40 adopted passages on 23 re-inspected pinned images, 29 events, 18 source-specific orderings,
seven scenarios and 30 membership cases. Six local component candidates, seven conditional
exclusions and 17 unresolved cases preserve the distinction between troops at contact, distant
posts, later departures and later presence. All eight complete opening/force mappings remain
unresolved; no force, person or army is selected. The old design and dossier bytes are unchanged.

**Done (2026-10-19):** the same entries' [person/authority and army-continuity mapping](napoleonic-authority-v1.md).
All 28 prior roles and two capitulation examples are mapped from 41 passages on 24 pinned images.
Four source-local co-references are supported; eight identity hypotheses and all 12 same-side
inter-engagement continuity pairs remain unresolved. Reported organization, troop command,
superior direction, acting government and delegated negotiation stay distinct. No complete
opening force/person/army pair is emitted. **Stop this four-entry measurement pilot here.**

**Done (2026-10-19):** the mechanical [development blocker inventory](../artifacts/napoleonic-blocker-inventory-v1.md)
covers all 273 entries/546 sides in 13 complete groups. Both dossier replacement boundaries are
null throughout and typed quantity arrays are absent; separate Naples packages cover eight
blocked sides. These are record-presence findings, not absent-evidence or admission judgments.
The 52 reserved-final dossiers are excluded. The fixed 12-entry batch cap and existing-page
comparison select `peninsula 1812`: eight entries with 24 directly linked non-Bodart strength
and command pages, versus 32 pages for 1810 and 56 for 1813.

**Done (2026-10-19):** the complete `peninsula 1812`
[combined population/time/authority pass](../artifacts/napoleonic-peninsula-1812-measurement-v1.md).
All 59 strength/responsibility claims are indexed from 56 passages on 28 re-inspected images.
There are 32 numerical strength observations, seven explicit strength unknowns, 43 authority
appearances and six local associations between troop totals and named roles. **All 16 opening mappings remain
blocked; zero complete opening pairs or model rows. Stop this campaign pass here.**

**Done (2026-10-20):** the [measurement-feasibility checkpoint](research/napoleonic-measurement-feasibility-v1.md)
assesses both completed groups (12 entries/24 sides). Substantive population, boundary and
authority gaps remain beyond the deliberately null selections. Seven of 16 Peninsular sides
explicitly lack a matched own-side local count; the six co-report associations never cover both
sides of an entry. These purposive groups do not estimate corpus-wide feasibility. The checkpoint
recommends pausing wider strict-opening extraction until the command unit and authority rules
are defined; the opening target, reservation and admission/run gates remain unchanged.

**Done (2026-10-20):** the [operational-unit and authority specification](napoleonic-command-units-v1.md)
defines the appointment/force comparison unit, organizational levels, continuity/containment
rules and use-specific authority evidence. Six existing cases distinguish council/local
direction, expedition scope, troop command/delegation, later columns, reserve/sector tasks
and succession. No new person/army identity, opening selection or model row is created.
The specification stops here; wider strict-opening extraction remains paused.

**Done (2026-10-20):** the bounded [1805 appointment/objective check](research/napoleonic-1805-appointment-check-v1.md)
retains nine passages in seven contexts from one existing Alombert–Colin family, with one
targeted appointment/mandate follow-up. Imperial preparation direction, public aims, Murat's
reported nomination/scope question and task orders, and an announced personal-command event
stay distinct. No new normalized date or comparison boundary is selected. The overall imperial
pilot remains not estimable; its original record and all model inputs remain unchanged.

**Done (2026-10-20):** the separately scoped [Murat delegation check](research/napoleonic-murat-delegation-v1.md)
retains 13 passages in ten contexts from one existing family. Specific delegated tasks,
conditional cross-corps coordination and prescribed relative time conditions are supported;
general-command scope and an effective appointment window remain unresolved. The Emperor's
superior authority is retained. No original pilot is revised, no replacement eligibility is
inferred and no resource/outcome extraction begins. The source check stops here.

**Done (2026-10-20):** the [Rastatt window go/no-go decision](research/napoleonic-rastatt-window-decision-v1.md)
re-inspects one existing passage/context. **No-go for the historical comparison on current
evidence; this candidate is closed at the window gate.** The prescribed stopping condition
governs headquarters residence, not every protection/observation/reporting duty. Source-relative
event rules are permissible, but the operative start, observed authority coverage and closure
are unestablished. Alternative conventions do not supply those observations. Retained superior
authority and earlier preparation are explicit; no analytical window, model row or feature is
selected. All earlier records remain unchanged.

**Research disposition:** retain the positive task observations and stop this pilot branch.
No new Rastatt/Murat tenure search or alternative-window packet is queued from its remaining
unknowns. Reopening needs a separately justified decision. Further resource/outcome extraction,
source fetching, wider strict-opening research and numerical runs remain unqueued.

**Done (2026-10-20):** the Napoleonic evidence explorer covers all 325 engagement dossiers
and 16 complete campaign groups. It presents the 4,846 claims, including 1,085 explicit
unknowns and 140 disputed claims, with source passages/hashes, original scope notes and
separate research/measurement/admission explanations. This is a read-only interface;
it does not select model inputs, resolve identities or reopen the stopped research branch.

**Done (2026-10-20):** the [measurement-comparison view](https://masonpetrosky.github.io/generalship/napoleonic/comparisons/index.html)
covers the existing 12 pilot engagements / 24 sides in Naples 1806 and Peninsula 1812.
It presents all 82 strength observations (including nine unknown counts and one gun count)
and 73 command-role observations with population/time/scope, recorded compatibility findings,
boundary and identity notes, and exact supporting passages/images/hashes. All 24 opening
mappings remain unresolved. The read-only view uses existing records; wider extraction stays paused.

**Done (2026-10-20):** the separate [compiler-strength benchmark preparation](napoleonic-benchmark-v1.md)
covers all 273 development entries / 546 sides. **194 pairs (71.1%)** have eligible
printed personnel totals; 82 side extracts are missing and 32 ambiguous. The
[report](../artifacts/napoleonic-benchmark-v1.md) retains every entry, population/time/units,
source passages and hashes. Its fixed sensitivities retain 194, 193 and 163 pairs;
the printed-indecisive exclusion removes none and cannot establish label independence.
The [run proposal](../data/napoleonic/benchmark-v1/run-proposal.json) binds the dataset,
design, protocol and executing code. No historical fit ran or run authorization was
created during that preparation. This compiler-description target does not relax the opening profile,
attribute command effects or use the 52 final-evaluation entries.

**Done (2026-10-20):** the owner authorized and the primary executed the exact
[compiler-strength benchmark run](research/napoleonic-benchmark-run-v1.md), preserving
the frozen proposal and every input. On 194 eligible pairs, campaign-held-out log loss
is 0.559365 for force size versus 0.680716 for the training prior; war-held-out scores
also improve. **The forward check is weak:** 37 entries in 1813 nearly tie equal odds
on log loss and are slightly worse on Brier. The unqualified-total sensitivity is
worse on both metrics in its 30-entry forward check; its separate 163-entry
campaign-weighted interval against the prior includes zero. All four fixed populations and three evaluations are published,
with calibration, uncertainty and error concentration. The 52 final entries remain
reserved. No commander model, feature admission, wider extraction or final evaluation
is queued by this descriptive result.

**Evaluation reserved before a historical outcome fit:** development is 1805–1813 (273 entries,
13 intact groups); 1814–1815 is reserved for final numerical evaluation (52 entries, three groups).
These events have already been transcribed and seen; this is not historical blinding. The
[versioned design](napoleonic-methods-v1.md#4-evaluation-decisions-fixed-before-a-napoleonic-outcome-fit)
keeps the frame unchanged, fixes comparator and sensitivity rules, and records the severe limit
of only three final groups. A complete rating design, resolved ledgers and exact owner
run authorization are still required.

## Open owner decisions

- **Graded outcomes:** see [owner ideas](#owner-ideas-to-design-later). Bodart's loss figures
  could supply the margins later.

## The American Civil War: where things stand

- **Frame.** [Cohort v2](cohort-v2.md): every engagement in the pinned CWSAC list, 384 in 119
  campaign groups. The 127-engagement 1862–1863 pilot (cohort v1) is kept as it was frozen.
- **Evidence.** All 384 engagements have a draft dossier. The dossiers hold 3,577 claims, 461
  explicit unknowns and 16,090 citations. Every dossier had a separate AI review before
  2026-10-06; see [review policy](#review-policy). An [extraction audit](extraction-audit.md) of
  150 random claims found no material error (Wilson 95% interval 0–2.5%) and 8 minor ones, all fixed.
- **Explorer.** A static site, built by `python3 -m generalship site` and published on
  [GitHub Pages](https://masonpetrosky.github.io/generalship/), traces each commander to their
  engagements, claims, quoted passages and pinned sources.
- **Ledgers.** The v1 ledgers cover the 91 decisive, non-aggregate pilot engagements and the v2
  ledgers the 305 in scope ([addendum](ledgers-v2.md)). Each names one responsible commander per
  side and gives a graded strength estimate. [Strength ledger v3](ledgers-v3.md) fills 99 of the
  262 sides that had no usable figure from upstream tables; the other 163 are modelled (grade E,
  [design](strength-imputation.md)).
- **Runs.** Rating runs 1–4 and two estimate evaluations; see the README's results table. Run 4
  ([memo](research/commander-ratings-v4.md)) was pre-registered with a context comparator,
  estimated τ, leakage handling and a bootstrap rule, and found no improvement under that rule.
  The runs are exploratory diagnostics outside the [admission contract](feature-admission.md), and
  the frozen baseline is unchanged.

## Milestones

| Milestone | Status |
| --- | --- |
| 0. Working research foundation | Complete (infrastructure only) |
| 1. First reviewed campaign dossiers | Coverage complete. Cross-engagement identities, replacement boundaries and information sets remain |
| 2. Baseline audit and expanded coverage | Full-war coverage done. Arsht reproduction route, independent extraction sample and paired comparison rows remain |
| 3. Enriched prediction and command inference | Exploratory historical ratings only. Napoleonic measurement specification, synthetic checkpoint and final-set reservation done; historical army/appointment identification and causal design remain |
| 4. Inspectable research interface | Static explorer plus source/population/time/authority comparisons for the 12 measurement-pilot entries. Opportunity-adjusted estimates, wider disputes views and scenario toggles remain |

### Milestone 0: working research foundation (complete)

- A public repository, a Python package and CLI, and local test and reproduction commands.
- A frozen 127-engagement Civil War cohort of complete source campaign groups.
- Pinned inputs, attribution, integrity checks and exclusion accounting.
- A force-size logistic baseline with campaign-held-out evaluation and comparators.
- Deterministic coverage, predictions, research queue, report and hash receipt.

"Complete" applies to this infrastructure milestone only. Historical validation, AI extraction
quality, command attribution and better estimates of generalship have not been established.

### Milestone 1: first reviewed campaign dossiers

Deliverables:

- Campaign records and resolved commander and army identities. Command ledgers carry a commander
  registry; cross-engagement army identities remain unresolved.
- Source-dependent alternative estimates and a typed quantity schema. The schema (v3) is in use
  for Shiloh; historical reconciliation remains.
- Explicit replacement boundaries and contemporary information sets.
- Named review records and an extraction-error audit. Review records exist for every batch through
  2026-10-06, indexed in one disposition vocabulary. [Extraction audit v1](extraction-audit.md),
  done by the primary, found 0 material and 8 minor errors in 150 random claims; an independent
  extraction sample remains (Milestone 2).
- A feature-admission mapping tied to immutable sources and dossier versions.

Acceptance requires that:

- every admitted fact has traceable evidence;
- source alternatives remain visible;
- a population or timing disagreement is resolved or kept as a dispute;
- the v1 opening profile excludes post-boundary state and participation, including indirect use
  through transformations.

### Milestone 2: baseline audit and expanded coverage

- Document an exact reproduction route for the original Arsht analysis and its access and
  redistribution terms, as a track separate from the reduced baseline.
- Enrich the frozen cohort by complete campaigns, adding credible troop estimates without
  selecting only famous or easily scored battles.
- Audit coverage by outcome, commander, campaign, engagement scale and evidence quality.

Acceptance requires an immutable cohort, an exclusion ledger, an independent extraction sample,
and paired comparison rows defined before model selection. Sparse evidence must not quietly
become mediocre commander scores.

### Milestone 3: enriched prediction and command inference

- Predefine the campaign estimand and the causal graph.
- Add justified conditions and opponent and army context.
- Investigate whether commander assignment is confounded.
- Fit hierarchical partial-pooling alternatives only when coverage supports them.
- Evaluate on grouped held-out campaigns and a locked final test set, and check temporal
  generalization separately.
- Report calibration and clustered uncertainty.

Acceptance requires:

- better out-of-sample prediction on comparable rows;
- results robust to source and coding sensitivities;
- a separately defended causal interpretation.

A familiar-looking list of great generals is not evidence of correctness.

### Milestone 4: inspectable research interface

- An explorer that traces commander → campaign → engagement → assumption → passage. A static
  version exists (2026-10-06): commander, campaign, engagement, claim, passage, source and hash
  pages, rebuilt and published from each pushed commit. Since 2026-10-20 it also covers all
  325 Napoleonic dossiers and 16 groups, retaining unknowns, disputes and scope limits.
- Cumulative results, opportunity-adjusted estimates, coverage, uncertainty and source disputes,
  each shown separately.
- Scenario toggles that explain what changes.
- No double counting of battles and campaigns, and no unqualified cross-era rankings.

## Review policy

Owner policy since 2026-10-06 ([AGENTS.md](../AGENTS.md#review-policy)): there is no separate
design or evidence review step. The primary agent verifies its own work against the sources and
checks before committing, and that work is labelled primary-verified.

Earlier work had separate AI reviews:

- Claude Opus 5.5 `high`, from 2026-09-24 to 2026-10-06;
- GPT-6 Astra `xhigh`, before 2026-09-24.

Those reviews remain records of their own scope. A separate review runs only when the owner asks
for one.

## Deferred implementation choices

- **Research authoring and paid automation:** policies remain undecided.
- **External researchers:** evidence packets also work with an external researcher of the
  user's choice.
- **Extraction libraries:** LangExtract or another library can be evaluated later, against a
  measured need for source alignment.
- **Frozen-ledger corrections:** corrections to a dossier that a frozen ledger binds are installed
  under the [replay design](ledger-replay.md). Each frozen ledger replays in a temporary view that
  presents the archived bytes it binds.

## Owner ideas to design later

- **Graded outcomes, not win/loss only** (owner, 2026-09-25): "we should probably not reward the
  same reward for a pyrrhic victory as we would for Hannibal at Cannae. Both are wins, but one is
  much more beneficial."
  - **Now:** the ratings score every decisive result as 1 or 0.
  - **Possible design:** grade how much a result achieved, for example from loss ratios relative
    to force, each army's share of losses, pursuit or destruction of the beaten force, and
    strategic follow-through.
  - **Open questions:**
    - which margins are source-backed often enough to avoid omitting battles;
    - how to keep commander-created advantages (mediators) separate from the result;
    - how to avoid double counting a campaign's outcome in its battles;
    - how an ordinal or continuous outcome changes the held-out test.
  - **Before any run:** it needs a versioned design and owner authorization. It does not change
    existing runs.
