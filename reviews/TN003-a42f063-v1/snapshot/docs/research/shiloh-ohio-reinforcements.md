# Shiloh: Army of the Ohio crossing and reinforcement audit

Research date: 2026-09-20. **Draft; no independent historical review.**

The primary reports describe successive boatloads, regimental landings, nighttime
formation and later brigade arrivals. They do not establish one synchronized
Sunday-evening or Monday-dawn army strength. Nelson's clocks are internally
difficult to reconcile, the handbook's 600-person estimate remains untraced, and
Reed's strength reconstruction mixes dates, estimates and late arrivals. This
audit preserves those limitations while making the sequence inspectable.

## Inspected sources

The parent *Official Records*, Series I, Volume X, Part I (GPO, 1884), is the
[same inspected volume](https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf)
used by the earlier audits, SHA-256
`86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978`.
Printed page + 24 gives the one-based PDF page. The second parent is
[Reed's revised 1909 history](https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf),
SHA-256 `31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96`;
printed page + 2 gives its PDF page.

Twelve sectioned text snapshots and five full-page facsimiles were added to the
[registry](../../data/sources.json). Each has its own SHA-256, parent hash,
locator, author, edition, transformation and dependence note. Existing raw inputs
are unchanged. Transcripts retain selected passages and table columns, with
whitespace normalized and line-wrap hyphens removed after visual inspection.

| Source ID / snapshot | Locator | Document date / limits |
|---|---|---|
| [`or-nelson-reinforcements-v1`](../../data/raw/shiloh/or-nelson-reinforcements-v1.txt) | Report 103, pp.323-327 | April 10 report; attached April 6-7 action table and compiler's March return have separately stated scopes |
| [`or-ammen-crossing-v1`](../../data/raw/shiloh/or-ammen-crossing-v1.txt) | Report 104, pp.327-330,333-334, selected passages | April 10 report; separately printed diary has event labels but an unestablished composition date |
| [`or-grose-crossing-v1`](../../data/raw/shiloh/or-grose-crossing-v1.txt) | Report 105, p.337 | April 8; eight-company Sunday contingent |
| [`or-anderson-crossing-v1`](../../data/raw/shiloh/or-anderson-crossing-v1.txt) | Report 106, pp.338-339 | April 9; Sixth Ohio landing |
| [`or-jones-crossing-v1`](../../data/raw/shiloh/or-jones-crossing-v1.txt) | Report 107, p.339 | April 8; Twenty-fourth Ohio landing and midnight return |
| [`or-edward-mccook-crossing-v1`](../../data/raw/shiloh/or-edward-mccook-crossing-v1.txt) | Report 116, p.354 | April 10; Second Indiana Cavalry and detached orderlies |
| [`or-crittenden-reinforcements-v1`](../../data/raw/shiloh/or-crittenden-reinforcements-v1.txt) | Report 117, pp.354-355 | April 15; night landing, morning position and excluded cavalry |
| [`or-alexander-mccook-reinforcements-v1`](../../data/raw/shiloh/or-alexander-mccook-reinforcements-v1.txt) | Report 90, pp.302-303 | April 9; Savannah and Pittsburg are distinct arrivals |
| [`or-wood-reinforcements-v1`](../../data/raw/shiloh/or-wood-reinforcements-v1.txt) | Report 130, pp.376-377 | April 10; staggered embarkation/debarkation |
| [`or-garfield-reinforcements-v1`](../../data/raw/shiloh/or-garfield-reinforcements-v1.txt) | Report 131, p.380 | April 9; afternoon landing/front arrival, under fire but not engaged in his account |
| [`or-buell-reinforcements-v2`](../../data/raw/shiloh/or-buell-reinforcements-v2.txt) | Report 87, pp.291-292 | April 15; supplements the earlier immutable Buell snapshot |
| [`reed-1909-ohio-strength-v1`](../../data/raw/shiloh/reed-1909-ohio-strength-v1.txt) | pp.100-102,111 note j | Later compilation; its quoted Buell letter is secondhand, undated and not independently inspected |

The facsimiles preserve OR [p.326](../../data/raw/shiloh/or-reinforcement-p326-facsimile-v1.png)
and [p.327](../../data/raw/shiloh/or-reinforcement-p327-facsimile-v1.png), and Reed
[p.100](../../data/raw/shiloh/reed-reinforcement-p100-facsimile-v1.png),
[p.101](../../data/raw/shiloh/reed-reinforcement-p101-facsimile-v1.png) and
[p.102](../../data/raw/shiloh/reed-reinforcement-p102-facsimile-v1.png).
Reports from Nelson's command share `or-nelson`; other Army of the Ohio reports
retain `or-buell`. These grouping choices flag dependence, not proof that accounts
within or across groups are independent. Reed's compilation, a transcript and a
scan cannot be counted as separate corroboration of an underlying return.

## Arrival, crossing and participation timeline

All clocks are attributed reported local times, not synchronized observations.
Qualitative phrases remain qualitative; no timezone conversion is invented.

| Date / reported time | Location and formation | What the passage says | Limit |
|---|---|---|---|
| April 5, before noon | Savannah; Ammen's Tenth Brigade | Diary says reached Savannah before 12 m. | Diary composition date unknown; not Pittsburg arrival |
| April 5, evening | Savannah; Buell | Buell reports his own evening arrival and Nelson's arrival the same day | Whole division readiness is not established |
| April 6, 13:00 / 13:30 | Leaving Savannah | Ammen report says 13:00 for Tenth Brigade; Nelson says 13:30 for division | Different authors/scopes; no common departure clock selected |
| April 6, afternoon | Opposite Pittsburg Landing, then river crossing | Ammen diary says Nelson crossed first with part of Thirty-sixth Indiana; only three or four companies per boat in his account | No personnel load, crossing rate or exact clock supplied |
| April 6, 17:00 | Pittsburg Landing | Nelson places his column head up the bank; Anderson says Sixth Ohio disembarked about 17:00 | Nelson also describes a four-hour march after 13:30; the handbook instead places 17:00 at the opposite bank |
| April 6, about 17:30 | Landing / river hill; Twenty-fourth Ohio | Jones says landed and immediately formed in line | Landing and formation do not show when it first fired |
| April 6, before dusk | Near landing battery; Thirty-sixth Indiana | Grose says eight companies, about 400 strong, formed and then supported a battery | Two companies left on other duty; no exact 18:00 headcount |
| April 6, 18:30 | Near landing; Nelson/Ammen contingent | Nelson dates repulse and restoration of line to 18:30 | Participant's action account, not independently verified clock or causal effect |
| April 6, by 21:00 | West of river; Nelson's infantry | Nelson says all infantry across | Does not include his three batteries or cavalry regiment as a whole |
| April 6, about 21:00 | Pittsburg Landing; Crittenden | Reports arrival, followed by debarkation; boats needed again for McCook | Third Kentucky Cavalry remained opposite the landing for lack of transport |
| April 6, about 22:00 to midnight | Ammen's advanced line | Diary says forming about 22:00; Twenty-fourth Ohio rejoined about midnight | Reassembly/deployment occurs after crossing; midnight boundary not forced to an exact date/time |
| April 6, 19:00; April 7, 05:00 | Savannah, then Pittsburg Landing; Alexander McCook | Reports Savannah at 19:00, then landing at 05:00 with Rousseau disembarking | Kirk and Gibson followed in stages; Second Kentucky Cavalry guarded baggage |
| April 7, 04:00-05:30, different accounts | Nelson's division and Ammen's brigade | Nelson says rousing at 04:00 and action at 05:20; Grose says movement at 05:30; Buell says advance soon after 05:00 | Different stages/units and unreconciled clocks, not an inferred uncertainty interval |
| April 7, about 05:00 | Crittenden's field position | Crittenden says Buell conducted his division to its position; McCook arrived on its right later | Positioning is not a whole-army simultaneous headcount |
| April 7, early morning / by noon | Savannah / Pittsburg Landing; Wood and Wagner | Wood says Savannah early; Wagner's brigade fully debarked by noon | Arrival at the fighting line is a further stage; excludes other brigade and arms |
| April 7, 13:30 / about 15:00 | Landing / front; Garfield | Reports three regiments debarked at 13:30, reached front about 15:00, were under artillery fire but not engaged | Presence and the author's category of engagement differ; no brigade strength supplied |
| April 7, evening | Crossing; Second Indiana Cavalry | Edward McCook says regiment crossed then; only detached orderlies had been in action | Do not encode every member as absent from battle or confuse the two McCooks |

The timeline retains an important distinction from the earlier whole-army wording:
**Savannah arrival, opposite-bank arrival, landing, formation and fighting are not
interchangeable.** Buell's report also describes Bartlett, Mendenhall and Terrill's
batteries arriving during the night/early morning; it does not say Nelson's own
three batteries marched with his Sunday infantry. Detailed battery action clocks
are outside this bounded audit.

## Sunday evening: what is counted and what is missing

The [handbook p.113](../../data/raw/shiloh/gudmens-shiloh-handbook.txt) places the
leading brigade opposite Pittsburg Landing at 17:00 and about 600 in line by
18:00. The new reports support Sunday participation by an arriving contingent,
but do not verify that exact clock-and-population pair.

Grose reports about **400 in eight companies** formed after crossing; two other
companies were left behind. Ammen's diary places **part** of the Sixth Ohio with
the Thirty-sixth Indiana, with the remainder behind the line. Anderson describes
his regiment supporting the battery, while Ammen's shorter report calls the Sixth
Ohio a reserve. These are source descriptions of roles and stages, not grounds
to count every regiment as simultaneously firing.

Nelson's action table lists **380** for Thirty-sixth Indiana and **598** for Sixth
Ohio across the April 6-7 battle. Adding 598 to 400, or replacing either with the
handbook's 600, would mix populations and periods. Nor is 400 minus 380 a casualty
calculation. The original 600 observation remains, now explicitly disputed; a new
null claim marks the unresolved exact Sunday contingent and its source derivation.

Nelson's **13:30 + four hours = 17:30** is a diagnostic arithmetic comparison.
The same passage says the head was up the landing bank at **17:00**. Rounding,
unit stages, recollection or textual problems may matter; this audit does not
choose among them or silently move the event to the opposite bank. Independent
review must retain the original wording when considering a resolution.

## Strength figures and their populations

| Source | Count | Population / date | Why it is not a shared dawn force |
|---|---:|---|---|
| Grose, OR p.337 | About 400 | Eight Thirty-sixth Indiana companies formed Sunday evening | One contingent, approximate, not a timed army census |
| Nelson, OR pp.325-326 | 4,541 | Division taken into action; table headed April 6-7 | Whole-action scope; repeated by Reed from this report |
| Same table | 380 | Thirty-sixth Indiana taken into action | Component overlaps 4,541; does not adjudicate Grose's 400 |
| OR compiler, p.327 | 6,724 | Nelson division March present-for-duty abstract | Includes 890 cavalry; six division staff excluded; exact muster day not stated |
| Reed, pp.100-101 | 5,535 | Nelson infantry for duty under March 31 heading | Different composition and source treatment from the broader March abstract; unreconciled |
| Reed, p.100 | 9,118 | McCook for duty, April 30 | Post-battle return, not an April 7 observation |
| Reed detail / recap | 7,553 / 7,552 | Reconstructed McCook April 7 engaged | Explicit approximation and one-person printed discrepancy |
| Reed, p.101 | 3,825 | Reconstructed Crittenden April 7 engaged | Approximated; Fourteenth Brigade has no March/April reports in this compilation |
| Reed, p.102 | 2,000 | Wagner, arriving late April 7 | Estimated; does not include Garfield or whole Wood division |
| Reed, p.102 | 17,918 | Army of the Ohio recap | Mixed estimates and arrival phases; includes Wagner's late arrival |
| Buell letter quoted by Reed, p.111 | 18,000-19,000 | Retrospectively recalled, unqualified strength | Letter and date uninspected; not a newly recovered primary return |
| [Force pp.178-180](../../data/raw/shiloh/force-1881-shiloh.txt) | About 20,000 | Monday reinforcements from Buell's army | Separate later-history estimate; no numerical reconciliation established |

Nelson's nine action rows sum to **4,541**. The compiler's March abstract gives
**255 officers + 6,469 men = 6,724**, with the six staff explicitly outside that
total. These are source-specific arithmetic checks, not evidence the populations
are comparable. The April 30 McCook observation is explicitly tagged post-outcome.

Reed's recap adds **7,552 + 4,541 + 3,825 + 2,000 = 17,918**. The detail row's
7,553 would instead produce **17,919**. Both printed McCook readings remain;
17,919 is only a diagnostic sum, not a corrected source observation. The recap's
components overlap its total and must not be counted again.

Note j explains that the Second, Fifth and Sixth Division estimates use returns
from **March 20, March 31 and April 30**, compared with Nelson's returns and
report. Reed's existing note (r) takes present for duty as engaged without removing
noncombatants. Accordingly, the table cannot be promoted into a precisely dated
firing-line census merely because its columns contain integers. His quoted Buell
letter is useful as a lead, but an original letter or archival locator must be
recovered before treating it as separately inspected primary evidence.

## Migration, verification and next action

The preceding audits were checkpointed in commit **`6fb01c9`** before this pass.
The 43-claim Union-availability dossier is preserved byte-for-byte as
[TN003.v4.json](../../data/evidence/history/TN003.v4.json), SHA-256
`9ec051462243589cea1efa14ccdffc22cea7c55452483672b7e75acfa5d463dd`.
The new revision links to that archive and keeps schema version 2. The earlier
archive chain and all 33 earlier source records/files remain unchanged.

The draft now has **62 claims, 40 troop observations, 26 events and three explicit
unknowns**. Nineteen claims, eleven observations and twelve events were added.
All 29 earlier observations remain byte-equivalent as JSON values. Existing
claim/event IDs persist; the handbook crossing interpretation and related arrival
rationales were amended rather than deleting inconvenient estimates. No review
record, feature admission, replacement boundary or commander credit was invented.

Validation completed with **38 passing tests** and the offline contract check;
`make reproduce` and `make packet` regenerated the report, receipt and packet.
The generated report was inspected. Comparison with `6fb01c9` confirmed all 33
earlier source records and raw bytes, all 29 earlier quantities, the archive
chain, cohort and baseline predictions are unchanged. All 50 source hashes,
both parent PDF hashes and the receipt's input/output hashes matched. Repeating
packet generation produced identical bytes; `git diff --check` passed.
The generated report and current packet preserve the disputes above. Automated
checks establish hashes, citations and contracts; they do not establish historical
truth or independent entailment. Baseline coverage remains **23/127 engagements
in 13 eligible campaign groups**, within the **36-campaign** frame. Predictions
are unchanged and Brier remains **0.276882**, worse than equal odds **0.250000**.

The next useful step is an independent historical/source-entailment review of
this version, including a sample of transcriptions and the proposed population
distinctions. Focus on the crossing clocks and 600-person derivation, mixed-date
strength reconstruction, missing unit returns, and the earlier Michigan and
Confederate discrepancies. Unresolved claims may remain disputed after review.
A reviewed feature-admission contract and a defined comparison population are
still required before any enriched predictor reaches the model.
