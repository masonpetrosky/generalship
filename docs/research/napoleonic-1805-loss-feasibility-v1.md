# 1805 loss-measurement feasibility pilot v1

Primary-verified source encoding. One existing compiler family; no separate review.

**No-go for one common loss-based grade across the complete 22-entry group.** The source supports a component table with explicit gaps. It does not support replacing win/loss with one comparable severity or victory-quality number for every entry.

Of **22 entries / 44 sides**, 35/44 sides have some numerical personnel-loss observation; 14/22 entries have observations on both sides. Numerical presence is not a common definition. Killed-and-wounded figures are paired in **6/22 entries**, prisoner figures in **1/22**, and an explicit source-declared killed/wounded-plus-prisoner composition on both sides in **1/22**. No single defined all-ranks component covers the full group.

## Scope and decision

The owner accepted this bounded audit of the earliest frozen development group, `third-coalition 1805`, selected before assessing its loss availability. The exact [scope](../../data/napoleonic/loss-pilot-v1/scope.json) and [protocol](../../data/napoleonic/loss-pilot-v1/protocol.json) retain all 22 land-cohort IDs, including entries without figures. The source’s broader war/year heading also contains naval entries; those were already outside the frozen land group and are not silently added. This source group spans multiple theaters and is not treated as one command appointment.

The intended check is measurement feasibility: a whole-group measure needs the same explicit personnel definition and compatible population/time interpretation on both sides of every entry, without filling unknowns with zero, adding overlapping subsets or mixing people and equipment. This is a coverage/definition rule, not a statistical sample-size threshold. Narrower coverage is published even when the whole-group rule fails.

The pilot ends here. The component evidence is useful, but there is no outcome score, utility weight, model fit, new admitted input, commander effect or campaign contribution estimate. The 52 final-evaluation entries remain unused numerically. The uncorrected benchmark, failed probability-correction branch, stopped appointment branch and paused opening research are unchanged.

## Grain, completeness and comparability

One row is one frozen entry side. A is France and its allies; B is the opposing side. Printed winner/loser columns are retained as provenance, never inferred from casualties. There are zero duplicate side keys. Empty cells mean unknown; no explicit all-ranks zero is printed in the encoded observations. A dash remains null.

| All-ranks category | Sides with a figure / 44 | Paired entries / 22 | Interpretation |
| --- | ---: | ---: | --- |
| killed | 0 | 0 | No separate all-ranks count; combined figures are not split. |
| wounded | 0 | 0 | No separate all-ranks count; officer-only tables do not supply it. |
| killed_and_wounded | 16 | 6 | Explicit combined category; retains approximate qualifiers. |
| captured | 15 | 1 | Explicit numerical prisoner/captivity claim; mostly prisoners is not a count. |
| missing | 0 | 0 | No separately quantified all-ranks category. |
| reported_personnel_total | 28 | 10 | Printed aggregate or unclassified headline loss; compositions differ. |

The separate killed and wounded unknowns concern **all ranks**. Detailed officer tables are visible on the images but omitted from the old raw transcription; this pilot preserves headline officer subsets and does not promote their breakdowns into all-ranks counts.

Missing numerical loss observations occur on **8/22 A sides and 1/22 B sides**. This is source coverage asymmetry, not evidence of zero losses. All nine missing side keys remain in the JSON. The ten co-reported personnel-total pairs have heterogeneous definitions; they are not ten validated common attrition labels.

| Printed engagement type | Entries | Any numerical pair | Killed/wounded pair | Prisoner pair |
| --- | ---: | ---: | ---: | ---: |
| GEFECHT | 10 | 6 | 3 | 1 |
| KAPITULATION | 4 | 1 | 0 | 0 |
| SCHLACHT | 2 | 2 | 2 | 0 |
| TREFFEN | 5 | 4 | 1 | 0 |
| TREFFEN und KAPITULATION | 1 | 1 | 0 | 0 |

The paired killed/wounded IDs are `B363a`, `B363b`, `B365c`, `B367a`, `B368c`, `B369c`. Verona (`B365c`) is the only entry with both numerical prisoner counts and both printed killed/wounded-plus-prisoner totals. This describes source-local components, not a validated historical attrition model or a representative sample of the whole cohort.

## Every side and retained gap

All figures are people. `ca.` is retained as approximate. A reported total can subsume earlier components; never add all columns. Composition, material, officer/national subsets, qualifiers and exact evidence IDs are retained in the [140-quantity source record](../../data/napoleonic/loss-pilot-v1/observations.json). The source-page link opens the inspected facsimile. Complete quotations follow below.

| Entry / place | Side (printed column) | Killed + wounded | Captured | Reported total / unsplit loss | Source / scope note |
| --- | --- | ---: | ---: | ---: | --- |
| B363a Wertingen | A (winner) | ca. 500 | unknown | unknown | [p. 363](../../data/raw/bodart-1908-v1/p363.jpg) |
| B363a Wertingen | B (loser) | 400 | 1,600 | 2,000 | [p. 363](../../data/raw/bodart-1908-v1/p363.jpg) |
| B363b Günzburg | A (winner) | ca. 700 | unknown | unknown | [p. 363](../../data/raw/bodart-1908-v1/p363.jpg) |
| B363b Günzburg | B (loser) | 800 | 1,000 | 1,800 | [p. 363](../../data/raw/bodart-1908-v1/p363.jpg) |
| B363c Haslach | A (loser) | 600 | 900 | 1,500 | [p. 363](../../data/raw/bodart-1908-v1/p363.jpg) |
| B363c Haslach | B (winner) | unknown | unknown | 1,100 | [p. 363](../../data/raw/bodart-1908-v1/p363.jpg) |
| B364a Parsdorf | A (winner) | unknown | unknown | unknown | [p. 364](../../data/raw/bodart-1908-v1/p364.jpg); No side-A loss figure is stated; absence is not a zero. |
| B364a Parsdorf | B (loser) | unknown | unknown | ca. 1,600 | [p. 364](../../data/raw/bodart-1908-v1/p364.jpg) |
| B364b Elchingen | A (winner) | ca. 1,000 | unknown | unknown | [p. 364](../../data/raw/bodart-1908-v1/p364.jpg) |
| B364b Elchingen | B (loser) | unknown | unknown | 4,000 | [p. 364](../../data/raw/bodart-1908-v1/p364.jpg) |
| B364c Memmingen | A (winner) | unknown | unknown | unknown | [p. 364](../../data/raw/bodart-1908-v1/p364.jpg); No loss figure is stated for the French; no zero is inferred from capitulation. |
| B364c Memmingen | B (loser) | unknown | 6,000 | unknown | [p. 364](../../data/raw/bodart-1908-v1/p364.jpg); Explicit captivity statement |
| B364d Herbrechtingen | A (winner) | unknown | unknown | unknown | [p. 364](../../data/raw/bodart-1908-v1/p364.jpg); No side-A loss figure is stated. |
| B364d Herbrechtingen | B (loser) | unknown | unknown | ca. 2,500 | [p. 364](../../data/raw/bodart-1908-v1/p364.jpg) |
| B365a Ulm | A (winner) | unknown | unknown | ca. 1,000 | [p. 365](../../data/raw/bodart-1908-v1/p365.jpg); Explicit blockade/bombardment losses, 12–17 October |
| B365a Ulm | B (loser) | unknown | 24,000 | unknown | [p. 365](../../data/raw/bodart-1908-v1/p365.jpg); Captivity with conditional officer return; The 59 guns exclude the fortress guns by the source wording; the omitted fortress quantity stays unknown. |
| B365b Neresheim | A (winner) | unknown | unknown | unknown | [p. 365](../../data/raw/bodart-1908-v1/p365.jpg); No side-A loss figure is stated. |
| B365b Neresheim | B (loser) | unknown | 1,100 | unknown | [p. 365](../../data/raw/bodart-1908-v1/p365.jpg) |
| B365c Verona | A (winner) | ca. 800 | 100 | ca. 900 | [p. 365](../../data/raw/bodart-1908-v1/p365.jpg) |
| B365c Verona | B (loser) | ca. 400 | 800 | 1,200 | [p. 365](../../data/raw/bodart-1908-v1/p365.jpg); The printed aggregate has an approximate component; the aggregate is not independently precise. |
| B365d Trochtelfingen | A (winner) | unknown | unknown | unknown | [p. 365](../../data/raw/bodart-1908-v1/p365.jpg); No side-A loss figure is stated. |
| B365d Trochtelfingen | B (loser) | unknown | 1,700 | unknown | [p. 365](../../data/raw/bodart-1908-v1/p365.jpg); Explicit captivity statement |
| B366a Eschenau | A (winner) | unknown | unknown | unknown | [p. 366](../../data/raw/bodart-1908-v1/p366.jpg); The dash/absence in the printed loss layout is retained as unknown, not zero. |
| B366a Eschenau | B (loser) | unknown | unknown | 1,500 | [p. 366](../../data/raw/bodart-1908-v1/p366.jpg) |
| B367a Caldiero | A (loser) | 6,300 | 1,700 | 8,000 | [p. 367](../../data/raw/bodart-1908-v1/p367.jpg) |
| B367a Caldiero | B (winner) | 5,700 | unknown | 5,700 | [p. 367](../../data/raw/bodart-1908-v1/p367.jpg); The prisoner row is a dash. The displayed total repeats killed-and-wounded; no explicit numerical prisoner zero is supplied. |
| B367b Pojano | A (winner) | unknown | unknown | 600 | [p. 367](../../data/raw/bodart-1908-v1/p367.jpg) |
| B367b Pojano | B (loser) | 400 | 1,800 | 2,200 | [p. 367](../../data/raw/bodart-1908-v1/p367.jpg) |
| B368a Scharnitz | A (winner) | unknown | unknown | ca. 400 | [p. 368](../../data/raw/bodart-1908-v1/p368.jpg) |
| B368a Scharnitz | B (loser) | unknown | unknown | ca. 1,500 | [p. 368](../../data/raw/bodart-1908-v1/p368.jpg); The total is mostly prisoners (zumeist Gefg.); the number of prisoners and killed/wounded split remain unknown. |
| B368b Mariazell | A (winner) | unknown | unknown | unknown | [p. 368](../../data/raw/bodart-1908-v1/p368.jpg); No side-A loss figure is stated. |
| B368b Mariazell | B (loser) | unknown | unknown | 4,000 | [p. 368](../../data/raw/bodart-1908-v1/p368.jpg); Mostly prisoners (meist Gefg.) does not give a numerical prisoner count. |
| B368c Dürnstein | A (loser) | 5,000 | 1,600 | 6,600 | [p. 368](../../data/raw/bodart-1908-v1/p368.jpg); For loss-percentage arithmetic only, the pilot reads the explicit 25,000/8,000 strength-table row. The older benchmark has no selected denominator here and remains unchanged; no new predictor is admitted. |
| B368c Dürnstein | B (winner) | 4,000 | unknown | 4,000 | [p. 368](../../data/raw/bodart-1908-v1/p368.jpg); The prisoner row is dashes; it remains null despite the displayed total equalling killed-and-wounded.; For loss-percentage arithmetic only, the pilot reads the explicit 25,000/8,000 strength-table row. The older benchmark has no selected denominator here and remains unchanged; no new predictor is admitted. |
| B368d Dornbirn | A (winner) | unknown | unknown | unknown | [p. 368](../../data/raw/bodart-1908-v1/p368.jpg); No numerical personnel-loss figure is stated for this side. |
| B368d Dornbirn | B (loser) | unknown | unknown | unknown | [p. 368](../../data/raw/bodart-1908-v1/p368.jpg); Conditional free withdrawal; no prisoner count; No numerical personnel-loss figure is stated for this side. |
| B369a Ober-Hollabrunn | A (winner) | unknown | unknown | ca. 2,000 | [p. 369](../../data/raw/bodart-1908-v1/p369.jpg) |
| B369a Ober-Hollabrunn | B (loser) | unknown | 1,800 | ca. 3,000 | [p. 369](../../data/raw/bodart-1908-v1/p369.jpg); The non-prisoner remainder is not explicitly classified as killed and wounded and is not filled by subtraction. |
| B369b Castelfranco | A (winner) | unknown | unknown | 600 | [p. 369](../../data/raw/bodart-1908-v1/p369.jpg) |
| B369b Castelfranco | B (loser) | 400 | 4,400 | 4,800 | [p. 369](../../data/raw/bodart-1908-v1/p369.jpg); Fighting plus capitulation |
| B369c Austerlitz | A (winner) | 10,000 | unknown | 10,000 | [p. 369](../../data/raw/bodart-1908-v1/p369.jpg); The prisoner row is a dash, retained as null; the printed total repeats the killed/wounded number. |
| B369c Austerlitz | B (loser) | 16,000 | 20,000 | 36,000 | [p. 369](../../data/raw/bodart-1908-v1/p369.jpg) |
| B370a Steken | A (loser) | unknown | unknown | ca. 1,000 | [p. 370](../../data/raw/bodart-1908-v1/p370.jpg) |
| B370a Steken | B (winner) | unknown | unknown | 800 | [p. 370](../../data/raw/bodart-1908-v1/p370.jpg) |

## Findings and impact on use

**High: incomplete and unequal category coverage.** The source has numerical observations for 35/44 sides, while a common killed/wounded pair exists for 6/22 entries. Using only those six changes the evaluated population; filling missing counts with zero invents outcomes. Keep component-specific denominators and exclusions. Confidence is high for this inspected source encoding; historical accuracy remains unadjudicated.

**High: capture, release and loss periods differ.** Memmingen and Trochtelfingen explicitly put the named forces into captivity. Ulm describes captivity with conditional officer return and reports French losses for the blockade/bombardment of 12–17 October. Dornbirn allows conditional free withdrawal to Bohemia for the named Austrian force; its 4,000 strength is not a quantified prisoner loss. Castelfranco combines fighting and capitulation. These facts remain separate statements rather than one interchangeable measure of permanent force destruction. The corresponding quoted entries and page images are retained below.

**High: nested figures and unspecified composition.** Hollabrunn’s 1,800 prisoners are within an approximately 3,000 personnel-loss total; no killed/wounded remainder is inferred by subtraction. Austerlitz’s 6,000 Austrian losses are within the 36,000 coalition total. Officer subsets, guns, flags/eagles, ammunition wagons and horses remain separate. Ten printed personnel sums reconcile arithmetically; that alone does not establish unique people or interchangeable historical loss definitions.

**Medium for source arithmetic, high for an unqualified loss-rate grade: printed percentages and denominators can disagree.** Haslach prints 1,500 losses, 6,000 strength and 32%; the ratio of the printed counts is 25%. Dürnstein prints 6,600 French losses, 8,000 strength and 88%; the count ratio is 82.5%. Caldiero prints 8,000 French total losses, 46,000 strength and 18.4%; the count ratio is 17.391304%. The discrepancies are visible in the original images. We retain the counts and percentages without selecting a corrected historical value or assuming that every small residual is an error. Rounded figures and an unreported alternative denominator remain possible explanations, not established repairs.

## All printed-percentage arithmetic checks

Counts divided by printed compiler strengths, not opening exposure or effective combatants. The older benchmark did not select the Dürnstein strength row; this pilot reads its explicit 25,000 / 8,000 row directly for arithmetic only. This new observation does not revise the old frame, prepared benchmark or model inputs. The Austerlitz national subset uses its explicit 16,000 Austrian denominator. No missing casualty number is reconstructed from a percentage. Percentage-point differences are diagnostics, not corrections or precision estimates.

| Entry | Side / population | Measure | Printed loss / strength | Printed % | Count ratio % | Difference pp |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| B363a | B / whole_side | reported_personnel_total | 2,000 / 8000 | 25 | 25.000000 | +0.000000 |
| B363c | A / whole_side | reported_personnel_total | 1,500 / 6000 | 32 | 25.000000 | +7.000000 |
| B364b | B / whole_side | reported_personnel_total | 4,000 / 8000 | 50 | 50.000000 | +0.000000 |
| B367a | A / whole_side | killed_and_wounded | 6,300 / 46000 | 14.7 | 13.695652 | +1.004348 |
| B367a | A / whole_side | captured | 1,700 / 46000 | 3.7 | 3.695652 | +0.004348 |
| B367a | A / whole_side | reported_personnel_total | 8,000 / 46000 | 18.4 | 17.391304 | +1.008696 |
| B367a | B / whole_side | killed_and_wounded | 5,700 / 49000 | 12 | 11.632653 | +0.367347 |
| B367a | B / whole_side | reported_personnel_total | 5,700 / 49000 | 12 | 11.632653 | +0.367347 |
| B368c | A / whole_side | killed_and_wounded | 5,000 / 8000 | 63 | 62.500000 | +0.500000 |
| B368c | A / whole_side | captured | 1,600 / 8000 | 25 | 20.000000 | +5.000000 |
| B368c | A / whole_side | reported_personnel_total | 6,600 / 8000 | 88 | 82.500000 | +5.500000 |
| B368c | B / whole_side | killed_and_wounded | 4,000 / 25000 | 16 | 16.000000 | +0.000000 |
| B368c | B / whole_side | reported_personnel_total | 4,000 / 25000 | 16 | 16.000000 | +0.000000 |
| B369c | A / whole_side | killed_and_wounded | 10,000 / 65000 | 15.3 | 15.384615 | -0.084615 |
| B369c | A / whole_side | reported_personnel_total | 10,000 / 65000 | 15.3 | 15.384615 | -0.084615 |
| B369c | B / whole_side | killed_and_wounded | 16,000 / 83000 | 19.3 | 19.277108 | +0.022892 |
| B369c | B / whole_side | captured | 20,000 / 83000 | 24.1 | 24.096386 | +0.003614 |
| B369c | B / whole_side | reported_personnel_total | 36,000 / 83000 | 43.4 | 43.373494 | +0.026506 |
| B369c | B / austrian_subset_of_side_B | reported_personnel_total | 6,000 / 16000 | 38 | 37.500000 | +0.500000 |

## Existing alternatives and interpretation limits

The pilot links all 22 existing dossiers by hash and retains their outcome-claim IDs/statuses. The following existing disputed outcome claims remain visible as pointers. Their underlying non-Bodart passages were **not re-inspected in this pilot** and are not promoted into new numerical alternatives or resolved by the arithmetic above.

| Entry | Existing disputed claim | Existing dossier |
| --- | --- | --- |
| B363c | `side-a-victory-claim` | [unchanged draft](../../data/napoleonic/evidence/B363c.json) |
| B364a | `date-of-captures` | [unchanged draft](../../data/napoleonic/evidence/B364a.json) |
| B367a | `koch-indecisive` | [unchanged draft](../../data/napoleonic/evidence/B367a.json) |

Bodart’s selection rule, rounded totals, available rather than necessarily engaged strengths and potentially strength-dependent winner coding remain limits. A casualty figure is a source claim, and one compiler family is not independent corroboration. Attrition cannot supply the strategic value of an objective, pursuit, territory, readiness or later campaign contribution without their own evidence and definitions. No scalar utility or commander credit is invented. There is no historical model or uncertainty interval in this pilot.

There is no modern freshness/trend question for this fixed 1908 archive: raw and metadata hashes are checked instead. The assessment does not estimate feasibility across all 273 development entries from this single complete source group. Wider extraction and historical adjudication do not follow automatically from the remaining gaps.

## Inspected source conventions

The convention passages below were re-inspected on printed pp. 45–47. Entry passages were inspected on pp. 363–370: **11 pinned images, 72 entry/footnote passages and seven convention passages**, all from the same family. The transcription omits the detailed officer tables; the audit’s all-ranks scope and separate headline officer subsets preserve that limitation.

### selection

Primary English rendering: Entries may be selected for major consequences or the number of troops assembled or losses; the stated combined-loss threshold is 2,000 men. This is a selected record frame.

> Es wurden also solche Gefechte aufgenommen, welche große Folgen nach sich zogen (z. B. Beendigung des Feldzuges, Aufhebung einer Belagerung, Einnahme einer Hauptstadt, Kapitulation u. dgl. mehr) oder ohne Rücksichtnahme auf derlei Folgewirkungen solche Gefechte, welche entweder durch die Versammlung einer großen Streiterzahl auf dem Schlachtfelde oder aber infolge ihrer großen Verluste der Aufnahme würdig erschienen. Als Basis für den durch großen Verlust für die Aufnahme einzunehmenden Standpunkt diente dem Verfasser die Gesamtverlustziffer von 2000 Mann auf beiden Seiten zusammengenommen.

`bodart-1908-transcription-v1`, `p045`; Bodart (1908), explanatory remarks, printed p. 45. Image `bodart-1908-p045-image-v1` SHA-256 `7ca32589efda96eac031bd4f2ed110211367746731ce6bc013164bbb2807f61f`.

### columns

Primary English rendering: The winner is placed on the left and the defeated side on the right.

> Der Platz des Siegers bei den Gegenüberstellungen ist stets auf der linken Seite, der des Besiegten rechts zu suchen.

`bodart-1908-transcription-v1`, `p046`; Bodart (1908), explanatory remarks, printed p. 46. Image `bodart-1908-p046-image-v1` SHA-256 `d16ea1189cb338f3664aca0988a91755237bbbb96aa423e0d25c47733df06ef9`.

### winner-rule

Primary English rendering: For so-called indecisive battles, Bodart treats as winner the side holding the field or achieving its aim, even with greater losses; failing those criteria, the side obtaining the same result with fewer troops is awarded victory.

> Bei sogenannten unentschiedenen Schlachten wurde jene Partei als Sieger betrachtet, welche das Schlachtfeld behauptete oder den durch das Gefecht gesuchten Zweck erreichte, wenn auch ihre materielle Einbuße eine größere war. Falls die genannten Momente nicht vorhanden waren, wurde jener Partei der Sieg eingeräumt, welche mit einer Minderzahl denselben Erfolg erzielte, wie ihr Gegner mit einer größeren Streiterzahl.

`bodart-1908-transcription-v1`, `p046`; Bodart (1908), explanatory remarks, printed p. 46. Image `bodart-1908-p046-image-v1` SHA-256 `d16ea1189cb338f3664aca0988a91755237bbbb96aa423e0d25c47733df06ef9`.

### available-strength

Primary English rendering: Strength includes forces available for the battle and capable of being brought up in an emergency, rather than only those actually fighting; nearby troops could affect the opponent and events.

> Bei den Stärkeangaben wurden stets jene Streitkräfte angeführt, welche für die Schlacht disponibel waren und daher im Notfalle noch herangezogen werden konnten und nicht bloß jene, welche wirklich in den Kampf kamen. Der Autor ging hier von der Erwägung aus, daß schon das Vorhandensein einer Anzahl von Truppen an einem dem Kampfplatze nicht allzu entfernten Orte den Gegner in seinen Dispositionen beeinträchtigen und auf den Gang der Ereignisse beeinflußend einwirken konnte,

`bodart-1908-transcription-v1`, `p046`; Bodart (1908), explanatory remarks, printed p. 46. Image `bodart-1908-p046-image-v1` SHA-256 `d16ea1189cb338f3664aca0988a91755237bbbb96aa423e0d25c47733df06ef9`.

### unengaged-strength

Primary English rendering: Such troops were therefore included even when they took no part in the fighting or decision.

> daher solche Truppen, wenn sie auch an dem Kampf und der Entscheidung keinen Anteil nahmen, einbezogen wurden.

`bodart-1908-transcription-v1`, `p047`; Bodart (1908), explanatory remarks, printed p. 47. Image `bodart-1908-p047-image-v1` SHA-256 `de36dbb9e2526d6549e2e011361dc76c9fe5f940f9fef2c3eedda711342c8c4c`.

### rounding

Primary English rendering: Strength and loss figures were rounded upward: a number below 50 men to 50, and one below 100 men to 100.

> Die Stärke- und Verlustziffern wurden vom Autor nach oben abgerundet u. zw. in der Weise, daß eine Zahl von weniger als 50 Mann auf 50, eine solche von weniger als 100 Mann auf 100 abgerundet wurde.

`bodart-1908-transcription-v1`, `p047`; Bodart (1908), explanatory remarks, printed p. 47. Image `bodart-1908-p047-image-v1` SHA-256 `de36dbb9e2526d6549e2e011361dc76c9fe5f940f9fef2c3eedda711342c8c4c`.

### percentage-denominator

Primary rendering: Bodart says the loss percentages are calculated from total troop numbers. The pilot compares printed ratios only and does not repair conflicting figures.

> Da die Verlustangaben als absolute Ziffern für die Größe der erlittenen Einbuße keinen Maßstab für die vergleichende Beurteilung bieten, wurde bei allen Verlusten der Perzentsatz derselben von der Gesamt-Streiterzahl ermittelt, wodurch ein sofortiger Vergleich der gegnerischen Verluste nach deren relativer Menge ermöglicht ist.

`bodart-1908-transcription-v1`, `p046`; Bodart (1908), explanatory remarks, printed p. 46, loss-percentage paragraph. Image `bodart-1908-p046-image-v1` SHA-256 `d16ea1189cb338f3664aca0988a91755237bbbb96aa423e0d25c47733df06ef9`.

## Entry passages and facsimile locators

All entry citations use `bodart-1908-transcription-v1`, raw SHA-256 `bf12437b6d19226ce127ce5d81e59d20358a5b1999ffe00f5ac6a8f8c20ef986`. Every citation in the observation JSON retains its own source metadata hash and image hash. Generic table headers are anchored to their exact entry and line; matching words on another entry are insufficient.

### B363a: Wertingen

[Inspected p. 363](../../data/raw/bodart-1908-v1/p363.jpg), image `bodart-1908-p363-image-v1`; SHA-256 `6d4a58c8a4780455d104131362386f7879092967739b963572a178873bea34a2`.

`B363a:L1` — Bodart (1908), printed p. 363, B363a, transcription text line 1; table columns retained

> Sieg der Franzosen (7.000 Reiter) unter M. Pz. Murat über die Österreicher (9 Btln., 2 Esk. = 8.000 M.) unter FML. Fh. v. Auffenberg.

`B363a:L2` — Bodart (1908), printed p. 363, B363a, transcription text line 2; table columns retained

> Fz. Verl.: ca. 500 M. (24 Offz.) tot u. verw. | Öst. Verl.: 400 M. tot u. verw. 1.600 „ (52 Offz.) (Gefg.) zus. 2.000 M. (= 25%) 6 Kan., 3 Fahnen.

### B363b: Günzburg

[Inspected p. 363](../../data/raw/bodart-1908-v1/p363.jpg), image `bodart-1908-p363-image-v1`; SHA-256 `6d4a58c8a4780455d104131362386f7879092967739b963572a178873bea34a2`.

`B363b:L1` — Bodart (1908), printed p. 363, B363b, transcription text line 1; table columns retained

> Sieg der Franzosen (20.000 M.) unter Marschall Ney über die Österreicher (15.000 M.) unter Erzhz. Ferdinand v. Österreich.

`B363b:L2` — Bodart (1908), printed p. 363, B363b, transcription text line 2; table columns retained

> Fz. Verl.: ca. 700 M. (43 Offz.) tot u. verw. | Öst. Verl.: 800 M. tot u. verw. 1.000 „ Gefg. zus. 1 800 M., 1 Kan.

### B363c: Haslach

[Inspected p. 363](../../data/raw/bodart-1908-v1/p363.jpg), image `bodart-1908-p363-image-v1`; SHA-256 `6d4a58c8a4780455d104131362386f7879092967739b963572a178873bea34a2`.

`B363c:L1` — Bodart (1908), printed p. 363, B363c, transcription text line 1; table columns retained

> Sieg der Österreicher (25.000 M.) unter FML. Fürst Schwarzenberg über die Franzosen (6.000 M.) unter Div.-Gen. Dupont.

`B363c:L2` — Bodart (1908), printed p. 363, B363c, transcription text line 2; table columns retained

> Österr. Verl.: 1.100 M. | Franz. Verl.: 600 M. (43 Offz.) tot u. verw. 900 „ Gefg. zus. 1.500 M. (= 32%) 11 Kan., 2 Adler, 17 Munitionswägen.

### B364a: Parsdorf

[Inspected p. 364](../../data/raw/bodart-1908-v1/p364.jpg), image `bodart-1908-p364-image-v1`; SHA-256 `e24bf0152dfc10008226856656782c3cb125ce7b427a068941052a6221771c3e`.

`B364a:L1` — Bodart (1908), printed p. 364, B364a, transcription text line 1; table columns retained

> Sieg der Bayern unter GM. Wrede über die Österreicher unter FML. Fh. von Kienmayer.

`B364a:L2` — Bodart (1908), printed p. 364, B364a, transcription text line 2; table columns retained

> Österr. Verl.: ca. 1.600 M., 9 Kanonen.

### B364b: Elchingen

[Inspected p. 364](../../data/raw/bodart-1908-v1/p364.jpg), image `bodart-1908-p364-image-v1`; SHA-256 `e24bf0152dfc10008226856656782c3cb125ce7b427a068941052a6221771c3e`.

`B364b:L1` — Bodart (1908), printed p. 364, B364b, transcription text line 1; table columns retained

> Sieg der Franzosen (16.000 M.) unter Marschall Ney über die Österreicher (8.000 M.) unter FML. Gf. Riesch.

`B364b:L2` — Bodart (1908), printed p. 364, B364b, transcription text line 2; table columns retained

> Franz. Verl.: ca. 1.000 M. (54 Offz.) tot u. verw. | Österr. Verl.: 4.000 M. (= 50%).

### B364c: Memmingen

[Inspected p. 364](../../data/raw/bodart-1908-v1/p364.jpg), image `bodart-1908-p364-image-v1`; SHA-256 `e24bf0152dfc10008226856656782c3cb125ce7b427a068941052a6221771c3e`.

`B364c:L1` — Bodart (1908), printed p. 364, B364c, transcription text line 1; table columns retained

> Die Franzosen (20.000 M.) unter Marschall Soult zwingen 11 Bataillone Österreicher (6 000 M.) unter GM. Gf. Spangen zur Kapitulation, wonach diese österreichische Division in Kriegsgefangenschaft geriet.

### B364d: Herbrechtingen

[Inspected p. 364](../../data/raw/bodart-1908-v1/p364.jpg), image `bodart-1908-p364-image-v1`; SHA-256 `e24bf0152dfc10008226856656782c3cb125ce7b427a068941052a6221771c3e`.

`B364d:L1` — Bodart (1908), printed p. 364, B364d, transcription text line 1; table columns retained

> Sieg der Franzosen (8.000 M.) unter Marschall Pz. Murat über die Österreicher (4.000 M.) unter FML. Pz. v. Hohenzollern.

`B364d:L2` — Bodart (1908), printed p. 364, B364d, transcription text line 2; table columns retained

> Österr. Verl.: ca. 2.500 M., 2 Fahnen.

`B364d:L3` — Bodart (1908), printed p. 364, B364d, transcription text line 3; table columns retained

> † österr. GM. Gf. O'Donell.

### B365a: Ulm

[Inspected p. 365](../../data/raw/bodart-1908-v1/p365.jpg), image `bodart-1908-p365-image-v1`; SHA-256 `1e1084717356d124a5c88914bfa2949fd13dd49813d3b06f751364426ad0257a`.

`B365a:L1` — Bodart (1908), printed p. 365, B365a, transcription text line 1; table columns retained

> Die Franzosen unter Napoleon I. (80.000 M.) zwingen die Österreicher (24.000 M.) unter FML. Fh. v. Mack zur Kapitulation, wonach diese österreichische Armee in Kriegsgefangenschaft geriet. Den Offizieren wurde unter der Bedingung, bis zur Auswechslung nicht gegen Frankreich zu dienen, die Rückkehr nach Österreich gestattet. Die Franzosen erbeuteten außer den Festungskanonen Ulms 59 Geschütze, 26 Fahnen, 300 Munitionswägen, 3.000 Pferde.

`B365a:L2` — Bodart (1908), printed p. 365, B365a, transcription text line 2; table columns retained

> Franz Verl. während der kurzen Blokade und Beschießung (12.—17./10.): ca. 1.000 M. (54 Offz.)

### B365b: Neresheim

[Inspected p. 365](../../data/raw/bodart-1908-v1/p365.jpg), image `bodart-1908-p365-image-v1`; SHA-256 `1e1084717356d124a5c88914bfa2949fd13dd49813d3b06f751364426ad0257a`.

`B365b:L1` — Bodart (1908), printed p. 365, B365b, transcription text line 1; table columns retained

> Sieg der Franzosen unter M. Pz. Murat über die Österreicher (4.000 M.) unter FML. Fh. v. Werneck.

`B365b:L2` — Bodart (1908), printed p. 365, B365b, transcription text line 2; table columns retained

> Österr. Verl.: 1.100 M. Gefg., 2 Fahnen.

### B365c: Verona

[Inspected p. 365](../../data/raw/bodart-1908-v1/p365.jpg), image `bodart-1908-p365-image-v1`; SHA-256 `1e1084717356d124a5c88914bfa2949fd13dd49813d3b06f751364426ad0257a`.

`B365c:L1` — Bodart (1908), printed p. 365, B365c, transcription text line 1; table columns retained

> Sieg der Franzosen (ca. 12.000 M.) unter Marschall Masséna über die Österreicher unter FML. Fh. v. Vukassovich.

`B365c:L2` — Bodart (1908), printed p. 365, B365c, transcription text line 2; table columns retained

> Franz. Verl.: ca. 800 M. (39 Offz.) tot u. verw. 100 „ Gefg. zus. ca. 900 M. | Öst. Verl.: ca. 400 M. (24 Offz.) tot u. verw. 800 „ Gefg. zus. 1.200 M., 7 Kanonen.

### B365d: Trochtelfingen

[Inspected p. 365](../../data/raw/bodart-1908-v1/p365.jpg), image `bodart-1908-p365-image-v1`; SHA-256 `1e1084717356d124a5c88914bfa2949fd13dd49813d3b06f751364426ad0257a`.

`B365d:L1` — Bodart (1908), printed p. 365, B365d, transcription text line 1; table columns retained

> Die Franzosen unter M. Pz. Murat zwingen die Österreicher (1.700 M. [4 Gen. 71 Offz.], 28 Kan., 28 Munitionswägen) unter FML. Fh. v. Werneck sich kriegsgefangen zu ergeben.

### B366a: Eschenau

[Inspected p. 366](../../data/raw/bodart-1908-v1/p366.jpg), image `bodart-1908-p366-image-v1`; SHA-256 `5cd5619fe0c80f57c8d497a4d6dd6cba05eacd49681b2fd38e8044c8a3984977`.

`B366a:L1` — Bodart (1908), printed p. 366, B366a, transcription text line 1; table columns retained

> Sieg der Franzosen unter Marschall Pz. Murat über die Österreicher (3.000 M.) unter Erzhz. Ferdinand v. Österreich.

`B366a:L2` — Bodart (1908), printed p. 366, B366a, transcription text line 2; table columns retained

> — | Österr. Verl.: 1.500 M., 23 Kan.

### B367a: Caldiero

[Inspected p. 367](../../data/raw/bodart-1908-v1/p367.jpg), image `bodart-1908-p367-image-v1`; SHA-256 `0d3de1f4d1b87fe744ae358efba0d37ae6c4f8c71191d61e7af6e95ec688db33`.

`B367a:L1` — Bodart (1908), printed p. 367, B367a, transcription text line 1; table columns retained

> Österreicher | Franzosen

`B367a:L2` — Bodart (1908), printed p. 367, B367a, transcription text line 2; table columns retained

> FM. Erzhz. Karl v. Österreich | Marschall Masséna

`B367a:L3` — Bodart (1908), printed p. 367, B367a, transcription text line 3; table columns retained

> Streitkräfte:

`B367a:L4` — Bodart (1908), printed p. 367, B367a, transcription text line 4; table columns retained

> 79 Btln. 42.000 | Infanterie | 39.000 Btln. 81

`B367a:L5` — Bodart (1908), printed p. 367, B367a, transcription text line 5; table columns retained

> 52 Esk. 7.000 | Kavallerie | 7.000 Esk. 68

`B367a:L6` — Bodart (1908), printed p. 367, B367a, transcription text line 6; table columns retained

> 49.000 | Gesamt-Stärke | 46.000

`B367a:L7` — Bodart (1908), printed p. 367, B367a, transcription text line 7; table columns retained

> Verluste:

`B367a:L8` — Bodart (1908), printed p. 367, B367a, transcription text line 8; table columns retained

> 12·0% = 5.700 (2 Gen. 120 Offz.) | tot und verwundet | (2 Gen. 134 Offz.) 6.300 = 14·7%

`B367a:L9` — Bodart (1908), printed p. 367, B367a, transcription text line 9; table columns retained

> — | gefangen | — — 1.700 = 3·7%

`B367a:L10` — Bodart (1908), printed p. 367, B367a, transcription text line 10; table columns retained

> 12·0% = 5.700 (2 Gen. 120 Offz.) | Gesamt-Verlust | (2 Gen. 134 Offz.) 8.000 = 18·4%

`B367a:L11` — Bodart (1908), printed p. 367, B367a, transcription text line 11; table columns retained

> — | † fz. Brig.-Gen. Brun.

### B367b: Pojano

[Inspected p. 367](../../data/raw/bodart-1908-v1/p367.jpg), image `bodart-1908-p367-image-v1`; SHA-256 `0d3de1f4d1b87fe744ae358efba0d37ae6c4f8c71191d61e7af6e95ec688db33`.

`B367b:L1` — Bodart (1908), printed p. 367, B367b, transcription text line 1; table columns retained

> Sieg der Franzosen (ca. 12.000 M.) unter Marschall Masséna über die Österreicher (ca. 4.000 M.) unter GM. Hillinger.

`B367b:L2` — Bodart (1908), printed p. 367, B367b, transcription text line 2; table columns retained

> Franz. Verl.: 600 M. | Österr. Verl.: 400 M. tot u. verw. 1.800 „ Gefg.) zus. 2.200 M.

### B368a: Scharnitz

[Inspected p. 368](../../data/raw/bodart-1908-v1/p368.jpg), image `bodart-1908-p368-image-v1`; SHA-256 `97bbaa03059aa4fa28573529707691cff16e6d01a537fd9aeb47e22ce8b47079`.

`B368a:L1` — Bodart (1908), printed p. 368, B368a, transcription text line 1; table columns retained

> Sieg der Franzosen (ca. 13.000 M.) unter Marschall Ney über die Österreicher (ca. 3.000 M.) unter Oberstlt. Swinburne.

`B368a:L2` — Bodart (1908), printed p. 368, B368a, transcription text line 2; table columns retained

> Franz. Verl.: ca. 400 M. (16 Offz.) | Österr. Verl.: ca. 1.500 M. (zumeist Gefg.) 16 Kanonen, 1 Fahne.

### B368b: Mariazell

[Inspected p. 368](../../data/raw/bodart-1908-v1/p368.jpg), image `bodart-1908-p368-image-v1`; SHA-256 `97bbaa03059aa4fa28573529707691cff16e6d01a537fd9aeb47e22ce8b47079`.

`B368b:L1` — Bodart (1908), printed p. 368, B368b, transcription text line 1; table columns retained

> Sieg der Franzosen (ca. 15.000 M.) unter Marschall Davoust über die Österreicher (7.000 M.) unter GM. Gf. Meerveldt.

`B368b:L2` — Bodart (1908), printed p. 368, B368b, transcription text line 2; table columns retained

> Österr. Verl.: 4.000 M. (meist Gefg.), 16 Kan.

### B368c: Dürnstein

[Inspected p. 368](../../data/raw/bodart-1908-v1/p368.jpg), image `bodart-1908-p368-image-v1`; SHA-256 `97bbaa03059aa4fa28573529707691cff16e6d01a537fd9aeb47e22ce8b47079`.

`B368c:L1` — Bodart (1908), printed p. 368, B368c, transcription text line 1; table columns retained

> Russen und Österreicher | Franzosen

`B368c:L2` — Bodart (1908), printed p. 368, B368c, transcription text line 2; table columns retained

> Gen. Kutusow | Marschall Mortier

`B368c:L3` — Bodart (1908), printed p. 368, B368c, transcription text line 3; table columns retained

> Streitkräfte:

`B368c:L4` — Bodart (1908), printed p. 368, B368c, transcription text line 4; table columns retained

> 25.000 | — | 8.000

`B368c:L5` — Bodart (1908), printed p. 368, B368c, transcription text line 5; table columns retained

> Verluste:

`B368c:L6` — Bodart (1908), printed p. 368, B368c, transcription text line 6; table columns retained

> 16% = 4.000 | tot und verwundet | ( — 66 Offz.) 5.000 = 63%

`B368c:L7` — Bodart (1908), printed p. 368, B368c, transcription text line 7; table columns retained

> — — | gefangen | (1 Gen. 53 „ ) 1.600 = 25%

`B368c:L8` — Bodart (1908), printed p. 368, B368c, transcription text line 8; table columns retained

> 16% = 4.000 | Gesamt-Verlust | (1 Gen. 119 Offz.) 6.600 = 88%

`B368c:L9` — Bodart (1908), printed p. 368, B368c, transcription text line 9; table columns retained

> — | Verl. an Trophäen: | 5 Kanonen, 2 Adler.

`B368c:L10` — Bodart (1908), printed p. 368, B368c, transcription text line 10; table columns retained

> † öst. FML. Fh. v. Schmidt.

### B368d: Dornbirn

[Inspected p. 368](../../data/raw/bodart-1908-v1/p368.jpg), image `bodart-1908-p368-image-v1`; SHA-256 `97bbaa03059aa4fa28573529707691cff16e6d01a537fd9aeb47e22ce8b47079`.

`B368d:L1` — Bodart (1908), printed p. 368, B368d, transcription text line 1; table columns retained

> Die Franzosen (16 Btln., 4 Esk. = 15.000 M.) unter Marschall Augereau nötigen die Österreicher (9 Btln. = 4.000 M.) unter FML. Fh. v. Jellachich zur Kapitulation, wonach den Österreichern gegen die Verpflichtung, ein Jahr lang nicht gegen Frankreich zu dienen, bewilligt wurde, frei nach Böhmen abzuziehen.

### B369a: Ober-Hollabrunn

[Inspected p. 369](../../data/raw/bodart-1908-v1/p369.jpg), image `bodart-1908-p369-image-v1`; SHA-256 `7199f5bc5e8587de01e24832d122f2487a9f355cd21f10ba563cfa7fabeb7f7e`.

`B369a:L1` — Bodart (1908), printed p. 369, B369a, transcription text line 1; table columns retained

> Sieg der Franzosen (24.000 Inft., 6.000 Kav. = 30.000 M.) unter M. Pz. Murat über die Russen und Österreicher (5.500 Inft., 1.500 Kav., 12 Kan.) unter Gen.-Lt. Fst. Bagration.

`B369a:L2` — Bodart (1908), printed p. 369, B369a, transcription text line 2; table columns retained

> Franz. Verl.: (2 Gen. 55 Offz.) ca. 2.000 M. | Russ.-Österr. Verl.: ca. 3.000 M. (wor. 1.800 Gefg.), 12 Kanonen.

### B369b: Castelfranco

[Inspected p. 369](../../data/raw/bodart-1908-v1/p369.jpg), image `bodart-1908-p369-image-v1`; SHA-256 `7199f5bc5e8587de01e24832d122f2487a9f355cd21f10ba563cfa7fabeb7f7e`.

`B369b:L1` — Bodart (1908), printed p. 369, B369b, transcription text line 1; table columns retained

> Sieg der Franzosen (14 Btln., 12 Esk. = 9.000 M.) unter Div.-Gen. Gouvion St. Cyr über die Österreicher (4 800 M.) unter GM. Pz. Rohan.

`B369b:L2` — Bodart (1908), printed p. 369, B369b, transcription text line 2; table columns retained

> Fz. Verl.: 600 M. (1 Stb.-, 15 Offz.) | Öst. Verl.: 400 M. (1 Gen. 17 Offz.) tot u. verw. 4.400 „ gerieten infolge Kapitulation zus. 4.800 M. in Kriegsgefangenschaft.

### B369c: Austerlitz

[Inspected p. 369](../../data/raw/bodart-1908-v1/p369.jpg), image `bodart-1908-p369-image-v1`; SHA-256 `7199f5bc5e8587de01e24832d122f2487a9f355cd21f10ba563cfa7fabeb7f7e`.

`B369c:L1` — Bodart (1908), printed p. 369, B369c, transcription text line 1; table columns retained

> Franzosen | Russen und Österreicher

`B369c:L2` — Bodart (1908), printed p. 369, B369c, transcription text line 2; table columns retained

> Napoleon I. | Gen. Kutusow

`B369c:L3` — Bodart (1908), printed p. 369, B369c, transcription text line 3; table columns retained

> Streitkräfte:

`B369c:L4` — Bodart (1908), printed p. 369, B369c, transcription text line 4; table columns retained

> 97 Btln. 50.000 | Infanterie | 67.000 Btln. 114

`B369c:L5` — Bodart (1908), printed p. 369, B369c, transcription text line 5; table columns retained

> 121 Esk. 15.000 | Kavallerie | 16.000 Esk. 148

`B369c:L6` — Bodart (1908), printed p. 369, B369c, transcription text line 6; table columns retained

> 282 Gesch. 65.000 | Gesamt-Stärke | 83.000 [1] Gesch. 300

`B369c:L7` — Bodart (1908), printed p. 369, B369c, transcription text line 7; table columns retained

> Verluste:

`B369c:L8` — Bodart (1908), printed p. 369, B369c, transcription text line 8; table columns retained

> 15·3% = 10.000 (14 Gen. 80 Stb.-, 514 Offz.) | tot und verw. | (9 Gen. 293 Offz.) 16.000 = 19·3%

`B369c:L9` — Bodart (1908), printed p. 369, B369c, transcription text line 9; table columns retained

> — | gefangen | (9 „ 820 „ ) 20.000 = 24·1%

`B369c:L10` — Bodart (1908), printed p. 369, B369c, transcription text line 10; table columns retained

> 15·3% = 10.000 (608 Offz.) | Ges.-Verl. | (1.131 Offz.) 36.000 [2] = 43·4%

`B369c:L11` — Bodart (1908), printed p. 369, B369c, transcription text line 11; table columns retained

> 1 Adler | Verl. an Trophäen: | 186 Kan. (= 62%), 45 Fahnen, 400 Munitionswägen.

`B369c:L12` — Bodart (1908), printed p. 369, B369c, transcription text line 12; table columns retained

> Gefallene Generale:

`B369c:L13` — Bodart (1908), printed p. 369, B369c, transcription text line 13; table columns retained

> † fz. Brig.-Gen. Valhubert | † russ. Gen.-Lt. Gf. Essen; † österr. GM. v. Juerczik.

`B369c:N1` — Bodart (1908), printed p. 369, note [1] for B369c

> [1] hiev. 21 Btln., 28 Esk. = 16.000 Österreicher.

`B369c:N2` — Bodart (1908), printed p. 369, note [2] for B369c

> [2] wov. österr. Verl.: 6.000 M. (= 38%).

### B370a: Steken

[Inspected p. 370](../../data/raw/bodart-1908-v1/p370.jpg), image `bodart-1908-p370-image-v1`; SHA-256 `f41d1ab5da1e9c6e278930cdd86ffad627448fdc33139592e691593c3f3b3fef`.

`B370a:L1` — Bodart (1908), printed p. 370, B370a, transcription text line 1; table columns retained

> Sieg der Österreicher (17 Btln., 2.000 Reiter, 40 Kan. = 11.000 M.) unter Erzhz. Ferdinand v. Österreich über die Bayern (10 Btln., 8 Esk. = 7.000 M.) unter GM. Wrede.

`B370a:L2` — Bodart (1908), printed p. 370, B370a, transcription text line 2; table columns retained

> Österr. Verl.: 800 M. | Bayr. Verl.: ca. 1.000 M.

## Reproduction and primary checks

- [Measurement JSON](../../artifacts/napoleonic-1805-loss-pilot-v1.json), [source observations](../../data/napoleonic/loss-pilot-v1/observations.json), [audit module](../../generalship/napoleonic_losses.py) and [executed companion notebook](napoleonic-1805-loss-audit-v1.ipynb). The notebook recomputes the principal coverage counts from the saved side records.
- Scope SHA-256 `f76e09e714ac7b4d75eda1cac153a5983bd6b951b8e245b0947c9e8ea71eacc5`; protocol SHA-256 `05158992955cea30b2e429e968ea256ca7a048bfce9c3be5ad83223b8d427f17`; observation SHA-256 `6aab931bff48695c71e4d2a9ef4e52d56e5e081a97494afaadd15f2b5cc776b8`. The generated JSON also binds the exact audit code.
- `python3 -m generalship.napoleonic_losses` checks all fixed input hashes, 22 entry IDs / 44 side keys, 140 quantities/literals/units, exact entry-anchored quotes and image bindings, all subsets, all missing-category lists, ten printed sums, 19 percentage diagnostics and all 22 dossier pointers/statuses. Source interpretation is primary verification, not a separate historical review.
- `--write` regenerates only this report and its measurement JSON from the immutable source record. `make check` and `make reproduce` include this offline path. It makes no network request, model call or historical fit and does not modify a dossier, packet, frozen benchmark or previous result.
