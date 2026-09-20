# Shiloh: Union return and April 6 availability audit

Research date: 2026-09-20. **Draft; no independent historical review.**

This memo preserves the 43-claim Union-availability revision, archived as
[TN003.v4.json](../../data/evidence/history/TN003.v4.json). The subsequent
[Ohio reinforcement audit](shiloh-ohio-reinforcements.md) documents the current
62-claim, 40-observation, 26-event draft. Counts and validation below refer to this
earlier revision.

The audit identifies a specific omitted regiment in Reed's account of the April 5
return, distinguishes counted units from units at the front, and traces a later
accounting bridge for Wallace. It does **not** identify all three omissions named
by the original compiler or establish one Union opening-strength total. Reed's
Fifteenth Michigan narrative and summary table conflict, and the Sixth Division
comparison has a ten-man residual. These remain evidence problems, not values to
repair by assumption.

## Inspected passages and provenance

The [source registry](../../data/sources.json) records the SHA-256 of every snapshot
and its parent, author, edition, transformation, report date and dependence limits.
Eight new sectioned text snapshots and four full-page table scans were added.
All 21 earlier source records and raw artifacts remain unchanged.

| Source ID and local snapshot | Inspected locator | Scope |
|---|---|---|
| [`or-union-return-detail-v2`](../../data/raw/shiloh/or-union-return-detail-v2.txt) | OR I.X.1 p.112, PDF p.136 | Sixth Division brigade and unattached rows, supplementing the earlier immutable snapshot and scan |
| [`or-wallace-availability-v1`](../../data/raw/shiloh/or-wallace-availability-v1.txt) | Report 34, pp.169-170, PDF pp.193-194 | April 12 account of named detachments, nightfall arrival and overnight deployment |
| [`or-prentiss-availability-v1`](../../data/raw/shiloh/or-prentiss-availability-v1.txt) | Report 78, pp.277-278, PDF pp.301-302 | November 17 account, attachment A, Sixteenth Iowa exception and Twenty-third Missouri arrival |
| [`or-chambers-availability-v1`](../../data/raw/shiloh/or-chambers-availability-v1.txt) | Report 84, p.286, PDF p.310 | April 24 account of Sixteenth Iowa reserve duty and redirection |
| [`or-reid-availability-v1`](../../data/raw/shiloh/or-reid-availability-v1.txt) | Report 85, p.288, PDF p.312 | Fifteenth Iowa arrival after firing began; report date unstated in inspected heading |
| [`or-rousseau-michigan-v1`](../../data/raw/shiloh/or-rousseau-michigan-v1.txt) | Report 91, pp.307 and 310, PDF pp.331 and 334 | April 12 report of the April 7 battle and Oliver's joining contingent |
| [`reed-1909-union-audit-v1`](../../data/raw/shiloh/reed-1909-union-audit-v1.txt) | pp.60-61, 92-93, 96-98, 111-112; printed page + 2 = PDF page | Selected narrative, return heading, table columns, estimated-entry notes, detachment footnote and population convention |
| [`michigan-ag-1862-fifteenth-v1`](../../data/raw/shiloh/michigan-ag-1862-fifteenth-v1.txt) | Printed p.41 = PDF p.45; title PDF p.5; report heading PDF p.9 | Report for 1862, dated December 24 and published 1863; arrival and two-day casualties |

Exact parent downloads inspected:

- [Official Records I.X.1, 1884](https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf): `86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978`.
- [Reed, revised 1909](https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf): `31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96`.
- [Michigan report for 1862, published 1863](https://archive.org/download/annualreportofad00mich/annualreportofad00mich.pdf): `f25789cebc7cc9af4b9c9c603502f65d1f2165ae6d616fb73db0ccca6eb57fe6`.

The separately registered Reed facsimiles preserve entire printed pages
[93](../../data/raw/shiloh/reed-1909-union-p93-facsimile-v1.png),
[96](../../data/raw/shiloh/reed-1909-union-p96-facsimile-v1.png),
[97](../../data/raw/shiloh/reed-1909-union-p97-facsimile-v1.png) and
[98](../../data/raw/shiloh/reed-1909-union-p98-facsimile-v1.png), rotated for reading.
They are representations of the same source, not four independent witnesses.
Reed explicitly compiled from Official Records. The state report has another
institutional origin, but its underlying regimental records and dependence on
other casualty accounts have not been traced. No count of sources is a count of
independent confirmations.

## Unit-by-phase evidence table

Counts below retain their source populations. A blank opening count remains
unknown; paper strength, arrival and participation are different observations.

| Formation | Return or count evidence | April 5 / first-contact relevance | Later phase | Remaining limit |
|---|---|---|---|---|
| Eighteenth Wisconsin | Reed p.96: **735**, explicitly estimated | Reed pp.60,111 says arrived Saturday afternoon, missed the morning return, camped with Prentiss and fought Sunday | Sunday participation described by Reed | Source-described omission identified; not a recovered original return or complete mapping of p.112's two unnamed regiments |
| Sixteenth Iowa | Reed p.96: **785**; included in Second Brigade's April 5 return | Reed says remained at landing; Prentiss excepts it from the advance | Chambers says Grant ordered reserve duty beside Fifteenth Iowa, then support for McClernand | Counting it in a brigade does not place it at Prentiss's first contact |
| Fifteenth Iowa | Reed p.96: **782**, estimated; p.111 says not in April 5 return | Reid reports Sunday arrival and firing already underway when he reported to Prentiss | Disembarked, received ammunition, then deployed | April 6 addition cannot automatically fill an unnamed April 5 omission slot; opening count unknown |
| Twenty-third Missouri | Reed p.96: **575**, estimated | Prentiss says it had just disembarked when joining his reformed line | Prentiss says **9.05 a.m.**; Reed says about 9 | Retrospective clock and later-morning participation; not first-contact availability |
| Fifteenth Michigan | Reed p.97: **750 estimated for duty**, **730 engaged as reported by commander**; Michigan report gives **869 names on March rolls** | State report and Reed narrative place arrival April 5; Reed describes Sunday movement without ammunition | Reed describes later Sunday fighting at an unidentified place; Rousseau reports **about 230** joining early April 7 | Different populations; Reed's summary excludes it from Sunday, contradicting his narrative; no original Oliver report inspected |
| Fourteenth Wisconsin | Reed p.97: **750 estimated**, with p.111 tracing estimate to March 31 departmental return | Reed says arrived Sunday night | Fought Monday with Smith | Do not transfer its arrival timing to Fifteenth Michigan because both occupy the unassigned table |
| Fifty-sixth Ohio | Reed p.93: **701 for duty** in Third Division return | Wallace reports detachment at Crump's Landing after Sunday's order | Guard duty separates it from the marching force | April 4 paper count is not a verified April 6 detachment muster |
| Sixty-eighth Ohio | Reed p.93: **424 for duty** | Same named detachment in Wallace's report | Guard at Crump's Landing | Same date/population limitation |
| Third battalions, Eleventh Illinois and Fifth Ohio Cavalry | Reed p.93: **276 + 283 = 559 for duty** | Reed's footnote includes both cavalry battalions among troops left behind | Outside his 5,837 engaged figure | Primary detachment personnel return not recovered |
| One gun and train guard | Wallace names one Thurber gun; Reed names one Buel gun and train guard | Reed includes these in **1,727** left at Crump's Landing | Personnel subtotal not separately printed | **43** is only the arithmetic residual after named infantry/cavalry; not a measured crew or train-guard count |
| Other original Sixth Division omissions | OR p.112: strengths of **two regiments and one battery** unreported | Compiler gives no names | Later compilation contains arrivals and estimates | Full set of original identities and strengths remains **unknown** |

The matrix does not assign command credit or blame. Qualitative lack of equipment
or ammunition remains a source claim, not an invented readiness score.

## What the Sixth Division arithmetic establishes

Prentiss's November report describes an attached return marked A. The compiler's
p.277 footnote says it is embodied in p.112. The attachment itself has not been
recovered, so the later revised abstract cannot be treated as the original form.

| Component | OR p.112 | Reed pp.96-97 | Diagnostic comparison |
|---|---:|---:|---|
| First Brigade | 2,790 | 2,790 | Same printed total |
| Second Brigade | 1,774 | 2,509 | Reed's 437 + 552 + 785 = 1,774; his estimated Eighteenth Wisconsin adds 735 |
| Unbrigaded infantry | No separate row | 1,357 | Estimated 782 Fifteenth Iowa + 575 Twenty-third Missouri; both described as Sunday arrivals |
| Unattached versus artillery/cavalry | 899 (41 officers, 858 men) | 263 + 626 = 889 (41 officers, 848 men) | Similar aggregate role is a comparison hypothesis; **ten men differ**, identity/composition not proved equal |
| Division | 5,463 | 7,545 | Difference **2,082**; three added infantry entries sum to **2,092**, offset by the ten-man difference |

This localizes a discrepancy; it does not explain it. In particular, Reed's three
added infantry entries do not identify the compiler's two regiment slots and one
battery slot. Both totals are retained. His April 5 heading includes later arrivals
and estimated additions, so it cannot be used as an unchanged dated return.

## Fifteenth Michigan: arrival supported, casualty day unresolved

The Michigan report's inspected p.41 says the regiment arrived "the day before the
battle of April 6 and 7." Its casualty sentence yields **33 killed, 64 wounded,
seven missing** across "that action." These match the numbers in
[Force's footnote 3](../../data/raw/shiloh/force-1881-shiloh.txt), but the state report
does not assign all losses to Sunday. Matching numbers do not prove Force used
this report or validate his day-specific claim.

Reed pp.60-61 describes early Sunday movement, an ammunition problem, return to
the landing and renewed fighting at an undetermined location. Yet pp.97-98 group
the Fifteenth Michigan with the Fourteenth Wisconsin as unassigned infantry,
deduct both from April 6 presence and add both as April 7 reinforcement. This
internal conflict is preserved. Neither Force's uncorrected exclusion nor Reed's
**39,830** Sunday aggregate becomes a canonical opening total.

Rousseau's report offers a separate, narrower observation: **about 230** officers
and men joined him early on April 7. The dated report opening establishes that
day. This cannot be subtracted from 750, 730 or 869 to infer casualties, missing
men, combat effectiveness or Sunday strength.

## Wallace: a traceable bridge, not a harmonized total

| Account | Count | What it describes |
|---|---:|---|
| OR p.112 / Reed p.93 | 7,564 | Third Division present for duty, April 4 |
| Reed p.93 footnote | 1,727 | Infantry, cavalry, gun and train guard left at Crump's Landing |
| Reed pp.93,98 | 5,837 | "Actually engaged" / April 7 reinforcement, using his population convention |
| [Force pp.178-180](../../data/raw/shiloh/force-1881-shiloh.txt) | 6,500 | Later approximate Monday reinforcement estimate; basis untraced |
| [Army handbook p.85](../../data/raw/shiloh/gudmens-shiloh-handbook.txt) | 5,800 | Narrative count for division arriving after dark; derivation unverified |

Within Reed, **7,564 - 1,727 = 5,837**. The two named infantry regiments and
cavalry entries sum to **701 + 424 + 559 = 1,684**. The remaining **43** is an
arithmetic residual, not an independently reported personnel subtotal. This bridge
makes a roughly 5,800 account plausible, but proximity does not establish the
handbook's source or explain Force's 6,500. Reed's adjacent "Wallace says 5,000"
is retained as a secondhand research lead, not newly inspected Wallace evidence.

Wallace's April 12 report names the two Ohio regiments and a gun left behind.
It distinguishes arrival a little after nightfall, deployment about 1 o'clock at
night, and artillery fire after daybreak. These improve the phase sequence without
settling the disputed order, route or responsibility. The original report and
Reed use different battery command names; this audit does not treat the wording
alone as proof of an identity match or an additional gun.

Reed p.112 note (r) explicitly treats present for duty as engaged and does not
remove noncombatants. His usage therefore differs from a count of men at the
firing line or a narrower combatant estimate. No source total is averaged with
another, and no whole-day participation total is relabeled first-contact strength.

## Migration, validation and remaining work

The preceding 28-claim Confederate-return revision is preserved byte-for-byte as
[TN003.v3.json](../../data/evidence/history/TN003.v3.json), SHA-256
`b2da0882ed391a78b34b91382958ddcc5483ab34e908f2382fb36719adccafce`.
The current dossier links to it, continuing the earlier archive chain. Schema
version remains 2; existing IDs and all 20 earlier typed observations remain.
This revision has **43 claims, 29 observations and 14 events**: 15 claims, nine
observations and seven events were added. An explicit unknown preserves the
unresolved original omissions. Estimated entries retain their printed precision
with explicit notes; `reported_exact` does not mean measured exactly.

The report and prepared assignment are regenerated with `make reproduce` and
`make packet`. `make check` passes **38 tests**, including source hashes, exact
section passages, archive integrity and offline reproducibility. Preservation
checks compare against the immediately preceding working state, including the
Confederate follow-up, rather than only against Git HEAD. These are consistency
checks, not independent historical review.

All 21 previous source records and files match, all 20 previous typed observations
are unchanged, and the new archive matches the preceding dossier hash. The quality
artifact differs only in source hashes; every build-receipt hash matches and the
prepared packet regenerates identically. All three inspected parent PDF hashes
were rechecked against the registry.

The frozen frame remains **127 engagements in 36 campaigns**. Baseline coverage
is still **23/127 engagements in 13 eligible campaign groups**. Predictions remain
byte-identical, with held-out Brier **0.276882**, worse than equal odds **0.250000**.
No model inputs, feature admission, replacement boundaries or commander attribution
were changed. Richer evidence has not improved model coverage or performance.

The next bounded source audit can examine Nelson/Ammen's April 6 crossing and
Buell's divisional returns, separating Savannah, opposite-bank arrival, landing,
deployment and fighting. A reviewer can already examine the current immutable
packet for the Michigan conflict, Sixth Division omission mapping and residual,
Wallace population definitions, and the earlier Confederate return discrepancies.
The missing original forms and unresolved source disagreements remain visible
even if that next phase succeeds.
