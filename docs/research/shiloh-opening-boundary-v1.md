# Shiloh opening boundary and population proposal, v1

Research date: 2026-09-20. **Bounded proposal; separate review pending. No feature
admission, model-input change or canonical opening strength.**

The [v2 admission proposal](../../data/admission/shiloh-opening-v2.json) uses the
existing immutable evidence snapshot. It defines a proposed contact rule and
availability policy, documents the remaining geographic and membership gaps,
and revisits the 18 observations blocked by the original census. The original
[v1 proposal](../../data/admission/shiloh-opening-v1.json) and default ledger stay
unchanged. Use v2 explicitly; it is not a release or a replacement baseline.

The [research record](../../design/shiloh-opening-boundary-v1/research-record.json)
binds every candidate, profile, boundary, quantity and input file. Its 51 exact
passage anchors cover 26 source/section pairs in 16 source records, with raw-file
and full metadata SHA-256 hashes, document dates and null historical knowledge
times. This pass inspected pinned text, not new facsimiles or external sources.
A quote's presence establishes provenance, not historical truth or independence.

## Proposed boundary B0

Use **immediately before the first hostile contact of the April 6 assault,
including reconnaissance and picket contact**. Do not begin at the later general
advance, a commander's arrival, first artillery fire, or the main camp attack.
This is retrospective state reconstruction under the reviewed prediction
profile, not a tactical replacement time, campaign boundary or historical
information-set forecast.

Beauregard's April 11 account nominates a reconnaissance party meeting advance
pickets, reported at **5 a.m. April 6**, followed by movement reported at **5:30**
([`or-beauregard-shiloh-report:p386`](../../data/raw/shiloh/or-beauregard-shiloh-report.txt)).
Grant's April 9 account describes Sunday pickets being attacked before the five
local divisions formed their lines
([`or-grant-shiloh-report:p109`](../../data/raw/shiloh/or-grant-shiloh-report.txt)).
These support the proposed event ordering. They do not prove that Beauregard's
encounter was the earliest qualifying contact, synchronize clocks or supply an
exact timestamp. Keep 5 a.m. as an attributed report; no time zone is invented.
The actual first-contact identification remains a research gate, including
whether earlier patrol/outpost encounters belong to the same engagement.

The date-only machine field is April 6, inherited from v1; it does not establish
intraday membership. A report dated after the battle can describe earlier state,
but report/forwarding dates never substitute for a muster date or command receipt.
For example, the “before battle” heading on the Confederate return is retained
without converting it to a verified B0 census.

## Proposed area and availability policy

The geographic mapping task is the **Pittsburg Landing west-bank camps and
landing, immediate attack approaches, contiguous outposts, reserves and ford
guards** at B0. Crump's Landing, Savannah and the opposite bank are outside this
proposed local area. These exclusions are conditional on this declared local
profile; a larger concentration/opportunity profile would be a different proposal.
They do not assert that every individual in an out-of-area formation was absent.
No rejected aggregate is converted into a numerical zero.

Beauregard p.386 places the attack lines between Owl and Lick creeks, describes
supporting reserves, and names cavalry/artillery guards at Greer's, Tanner's and
Borland's fords. This gives named spatial questions, **not a surveyed perimeter**.
The machine `area` and both `members_by_side` remain null. No map or complete
unit-location inventory was recovered in this pass. In particular, the treatment
of creek-edge guards, approach columns, transport passengers and naval combat
crews still needs explicit resolution. Do not silently exclude afloat people or
assume every person in a paper return occupied the proposed land area.

Apply the same rule to both sides: count combat-unit people physically available
inside the eventual area at B0, including officers, infantry, artillery crews,
cavalry, reserves and outposts; exclude people known to be absent, hospitalized,
on noncombatant duty or outside the area. **Being in the first firing line or
later participating is not required.** Lack of ammunition or incomplete equipment
stays a separate qualitative claim; it is not a numerical readiness deduction.
A detailed definition for uncertain medical/duty cases remains necessary before
any full membership partition can be accepted.

This matters for the Sixteenth Iowa and Fifteenth Michigan. Reed describes the
former remaining at the landing and the latter arriving April 5 without
ammunition. Michigan's report also places its arrival the day before the battle.
Those passages prevent an automatic “not at Prentiss's front” or “unready”
exclusion, but do not prove the numbers available at B0. The respective anchors
are `reed-1909-union-audit-v1:p60-second-brigade`, `:pp60-61-michigan`, and
`michigan-ag-1862-fifteenth-v1:p41`. The competing Michigan participation accounts
remain unresolved; neither arrival nor casualties establishes an opening count.

## Changes to the 18 blocked mappings

The table groups the exact candidate IDs recorded individually in the research
record. These are proposed uses of unchanged observations, not corrections to
the historical counts. `before` means the reported state predates B0; it does
not approve carrying a stale return forward. No candidate has a complete
membership set, a numeric adjustment, a transform or a source-choice weight.

| Observation IDs (without `TN003-`) | Proposed disposition | Inspected basis and remaining limit |
| --- | --- | --- |
| `union-paper-total` | Excluded for direct opening use | OR p.112 includes Wallace's 7,564 in 44,895; Grant locates that division at Crump's Landing. The abstract also omits two regiments, one battery and division staff. Subtracting Wallace does not repair the other gaps. |
| `wallace-april4-return` | Excluded | Earlier whole-division paper population; Grant p.109 places it at Crump's. Wallace p.170 reports a later movement order and night junction. This is a location/scope exclusion, not one inferred solely from failure to fight Sunday. |
| `reed-wallace-detached`, `reed-fiftysixth-return`, `reed-sixtyeighth-return`, `reed-wallace-cavalry-return` | Excluded (4) | Reed pp.92–93 gives the April 4 rows and Crump's guard. Wallace p.170 names the two Ohio regiments and gun. Reject direct substitution into the local opening population. Exact detachment census, individual exceptions and gun identity remain unresolved. |
| `nelson-march-abstract`, `reed-nelson-march31` | Excluded (2) | Earlier paper counts of a division whose described departure from Savannah occurs later Sunday; batteries remained there. OR pp.323–327 and Reed pp.100–101 do not turn 6,724 or 5,535 into a local opening count. No claim of zero detached individuals. |
| `handbook-nelson-leading`, `grose-sunday-eight-companies` | Excluded (2) | Handbook p.113's roughly 600 is an evening state. Grose p.337's roughly 400 follows the later brigade march/crossing, supported by Ammen's report p.328. Conflicting clocks and the 600-person derivation remain open. |
| `reed-sixth-reconstruction` | Excluded | Reed's 7,545 includes the later Twenty-third Missouri arrival (p.111 note e; Prentiss p.278), while note r treats for-duty people as engaged and retains noncombatants. It is a mixed-phase reconstruction, not an unchanged April 5 opening return. |
| `confederate-before` | Blocked | The 40,335 “before” effective total lacks a verified B0 population, muster/derivation and bridge to report 136. The relative heading remains insufficient for `at_boundary`. |
| `confederate-report-136-total`, `-infantry`, `-artillery`, `-cavalry` | Blocked (4) | April 3 is the march heading, not an established muster. The effective/for-duty populations are not equated; Hill's Monday footnote does not establish inclusion or a subtraction. Branch totals overlap the army total. |
| `sixth-april5-abstract` | Blocked | The dated 5,463 is pre-B0, but unnamed omissions, population, carry-forward and unit-location membership remain open. It is also only one division. |
| `reed-eighteenth-wisconsin-estimate` | Blocked | Reed places the regiment in camp April 5, but that does not establish the referent/derivation of his estimated 735 or its exact combatant membership. Its null period and estimation marker remain unchanged. |

The first six rows change **11 candidates from blocked to excluded**. Seven
remain blocked. The other **22 previously excluded mappings are retained
unchanged**; they were not newly reviewed as 22 historical transcriptions here.
Every candidate now binds the new boundary, so earlier reviews cannot silently
approve the changed proposal.

## Unresolved alternatives and prohibited shortcuts

- **Confederate 40,335 versus 38,773:** preserve both sources and their dependence
  through the same army reporting chain. They are not a range or two usable
  scenarios until population, timing and derivation are individually applicable.
  The report-136 Hill footnote does not authorize a guessed subtraction. Its
  infantry warning does not establish how the artillery or cavalry were counted.
- **Union 44,895 minus Wallace:** a paper arithmetic residual does not prove the
  local combatant population. Original omissions, division staffs, noncombatants,
  dated returns and exceptions all still matter. No derived candidate is created.
- **Sixth Division 5,463 plus 735:** an estimated omitted regiment is not a complete
  repair. The two unnamed regiments and battery in OR p.112 are not equated with
  Reed's later additions; the ten-person comparison residual remains unresolved.
- **Late arrivals or casualty reconstruction:** post-contact counts cannot become
  opening predictors through subtraction, survivors-plus-losses or hindsight.
- **Transport, reserve and unready populations:** landing, disembarkation,
  formation, equipment and action are separate events. Do not replace missing
  membership evidence with a readiness score or later combat record.

The only scenario selects no candidates and retains the complete frame. There
are no numerical alternatives yet established as applicable, and none is chosen
because of the recorded outcome, reputation or a model score. This is an
exploratory, retrospectively authored proposal; it is not claimed to be blind to
historical outcomes.

## Coverage and reproducibility

The [v2 ledger](../../artifacts/admission/shiloh-opening-v2-check.json) contains
**127 engagements / 36 campaign groups**, three available dossiers and one
engagement with candidates. All **40 Shiloh quantities** remain represented:
**7 blocked, 33 excluded, zero eligible candidates, zero complete rows and zero
emitted/promoted rows**. These are mechanical dispositions conditional on the
proposal, not 33 historical falsehoods or an increase in modeled coverage.

The default v1 ledger remains **18 blocked / 22 excluded**. The 62 claims, 40
quantities, 26 events, registry (53 entries / 50 raw paths), original source
files, cohort and prepared TN003 packet remain unchanged. Baseline coverage is
still 23 engagements / 13 groups and Brier 0.2768816348133779 versus equal odds
0.25. Neither this evidence-use work nor software review improves that result.

```sh
python3 -m generalship admission-check data/admission/shiloh-opening-v2.json
python3 design/shiloh-opening-boundary-v1/reference-audit.py
make check
make reproduce
```

The bounded audit checks the saved report against a fresh offline validation,
all passage/metadata/file bindings, preservation of old mappings and original
inputs, and the complete denominator. It cannot check historical entailment.
Separate reviewer dispatch and the actual response will be preserved with their
exact input commit and hashes; no reviewer approval is supplied by this document.

## Next evidence needed

The first priority is a **contact-and-location evidence packet**: inspect the
full opening sections of the Prentiss/brigade/patrol accounts and contemporary
positions/maps, identify the earliest qualifying contact (including earlier
outpost encounters), and map both sides' outposts, approach echelons, reserves
and ford guards. These are research leads, not passages inspected in this pass.
Resolve the transport/afloat rule explicitly; retain unknowns where the evidence
cannot locate or enumerate people.

Then recover original unit returns and population definitions for the seven
blocked observations, preserving the Confederate accounting dispute, Union
omissions and estimates. New material requires versioned sources, a new frozen
snapshot/proposal and review. Continue the campaign's other engagements rather
than selecting only an easily scored Shiloh total. An actual feature release and
enriched modeling remain separate work.
