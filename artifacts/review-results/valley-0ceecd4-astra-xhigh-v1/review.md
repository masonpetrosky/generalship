# Valley Campaign separate source review

**Outcome: one required phase-tag correction; otherwise the bounded extraction is accepted.** No new historical research, source recovery or numerical reconciliation is required for this first pass. The finding concerns one claim's temporal classification, not its quoted passage, the frozen battle results or the baseline.

Reviewer: GPT-6 Astra (`gpt-6-astra`), `xhigh`, fresh-context task `/root/valley_review`, 2026-09-20. Reviewed prepared commit `0ceecd4d4682eabbd58c498d202001ce760c9507` against `6fd4278f4f1eb7867e75d03ef436c46bd2fa37a3` under `assignment.md`. All 55 paths in `inputs.json` matched both their declared SHA-256 hashes and the prepared commit. The input manifest SHA-256 is `74bcfa8428fd7007e92ba2cf8ef8552e3246a097b9ea783d3ff0e5697fe7ade9`; assignment SHA-256 is `c52233b8e9b519777c4b92557327add31497670b1e87f216a31cbb5ea0af8edc`.

## Inspected scope

I read all seven dossiers, including every claim, rationale, citation, boundary note and open question; all six retained NPS summaries; Princeton's empty HTML template; Allan's catalog title/creator/date/publisher/identifier, title/preface and all six selected battle passages with their embedded footnotes. I checked every cited frozen cell and all seven battle, fourteen force and fifteen commander rows. I also read the repository instructions, methodology, evidence contract, roadmap, source guidance, Valley memo and generated report, and inspected the two small code/test changes.

| Record | Claims | Null unknowns | Citation occurrences | Families |
| --- | ---: | ---: | ---: | ---: |
| VA101 — Kernstown | 10 | 2 | 15 | 2 |
| VA102 — McDowell | 9 | 2 | 14 | 2 |
| WV009 — Princeton Court House | 10 | 4 | 9 | 1 |
| VA103 — Front Royal | 10 | 2 | 12 | 2 |
| VA104 — Winchester | 9 | 2 | 14 | 2 |
| VA105 — Cross Keys | 10 | 3 | 14 | 2 |
| VA106 — Port Republic | 10 | 2 | 13 | 2 |
| **Total** | **68** | **17** | **91** | **Two across the batch** |

All seven dimensions occur in each dossier. The unknowns are seven opening strengths, five information states, four logistics states and Princeton terrain. All are null with empty citations. I reviewed entailment and attribution as well as mechanically checking all 91 quote occurrences against their declared cells or sections.

Parent HTML was checked through text extraction and section boundaries. All six NPS text derivatives replay exactly using the declared HTMLParser transformation. All seven Allan half-open Unicode selections replay exactly with whitespace-only normalization; OCR errors, split words, headers and footnotes remain intact. I read short contexts before and after each selected battle passage. For the temporal finding below, I additionally read parent OCR ranges `[476300,479832)` and `[487300,498800)` covering adjacent portions of pp.157–158 and 160–163. This was bounded context inspection, not a whole-book or print review.

## Required correction

**VALLEY-R1 — Leave the Port Republic transfer's phase unresolved.** In `data/evidence/VA106.json`, claim `linked-battles-no-double-credit`, lines 123–135, `phase: "post_outcome"` is not established relative to the assigned Port Republic engagement. The claim concerns movement from Cross Keys and bridge burning, not an event demonstrated to follow Port Republic's outcome. The NPS Port Republic summary does not supply a reliable clock for that transfer. Its placement after a retreat sentence is insufficient to establish chronology. The retained Cross Keys summary describes part of Ewell's force crossing to assist the defeat at Port Republic; Allan's adjoining account distinguishes early transfers, an order during failed attacks to withdraw the remaining force and burn the bridge, and arrivals around the Federal retreat. These are changing phases rather than a single demonstrated post-outcome event. In contrast, the next-day transfer can remain subsequent context in the June 8 Cross Keys dossier.

Evidence inspected:

- `nps-va106-v1`, **Description**, SHA-256 `65db5af36912f652b034b05e589371a4fbb60fe05c4dbfd2c9f46c57a44d9f04`: the existing cited transfer/bridge-burning sentence.
- `nps-va105-v1`, **Description**, SHA-256 `a4d0ddd83bd5b87c502505cb51c3ba10fc4e391277f33530950df4b2fac093f0`: the next-day crossing to assist at Port Republic.
- `allan-valley-1880-ocr-v1`, adjoining OCR pp.157–158 and 160–163, SHA-256 `1c09a2648e25423f72a528667c1dc3aab12063db951b17505ee0dd580da62f28`: ordered early transfers, later concentration and rearguard withdrawal. These remain Allan's retrospective account; original orders were not inspected.

Exact proposed replacements in that claim:

```json
"phase": "unresolved",
"rationale": "The related June 8 and June 9 engagements remain separate frozen records with changing populations. The cited transfer and bridge burning are not established as occurring after Port Republic’s outcome; precise timing remains unresolved. Shared troops are not independent army observations, and campaign success is not an extra victory credited to both."
```

Retain the claim ID, value, dimension, status and citation. Primary verification and the repository's documented versioning/reproduction process should carry this correction into the prepared VA106 packet and receipt. Preserve this original review and its bound inputs. No new source snapshot, historical timing resolution or feature admission is necessary. I found no other required corrections.

## Substantive extraction assessment

The Kernstown force-field **3,800** versus narrative **3,400** discrepancy is retained without adopting either as a matched opening population. Ashby-mediated information and the estimated **3,000** Union troops are explicitly retrospective attributions, not a verified message chain. Kimball's field command in Shields's absence is supported, and the live heading's rank discrepancy is not silently adopted.

McDowell's hill/access description and artillery constraint are supported by Allan's full passage. The broken word across pp.74–75 still supports Schenck's senior command and approval of Milroy's attack. The casualty alternatives **720 / surgeon's 556 / live 756** remain visible.

Princeton retains the May 15–17 interval, missing numerical strength, one source family and four unknown dimensions. The reported **129** is correctly treated as incomplete, with Wharton unreported; force-table zeroes do not establish complete Confederate losses. The literal narrative **March 25** Winchester date is contrasted with VA104's **May 25**, and neither the later Lewisburg action nor Winchester becomes another Princeton outcome. The empty live page establishes no historical fact; an unsuccessful keyword lookup establishes no book-wide absence.

Front Royal preserves live zero strength versus frozen **4,063**, supports the bridge damage and local command distinctions, and does not add approximately **900** surrendered people to aggregate losses or opening strength. Winchester's Banks estimate is a quoted belief within Allan, not measured opposing strength or a separately inspected report. The road approaches and subordinate actions are supported.

Cross Keys preserves Ewell's divisional role, Trimble's local action, the live rank/name errors, and **951 / 972** casualty alternatives. Port Republic preserves sequential arrivals, local versus parent command and **1,818 / 1,800** losses. The June 8 and June 9 records remain distinct without additive army populations or campaign credit. Apart from R1, these interpretations keep inherited state, commander-created circumstances, tactical outcomes and campaign contribution appropriately unresolved or separate.

Allan's 1880 catalog/title/preface support the recorded edition and interested retrospective authorship. The May 1 preface does not date the narrative sections. Embedded reports are not separately inspected originals. NPS/CWSAC is one family, and Allan is one family; independence between them is unestablished.

## Mechanical verification and remaining limits

- All **259** preceding source records retain their metadata; all **256** preceding raw paths are byte-identical to the previous commit. The current registry has **273 records / 270 paths**. Existing Allan metadata, full OCR and Hancock selections are preserved.
- All **44 protected files** are byte-identical: 33 older dossiers, five historical revisions, the cohort, both admission proposals, and `baseline.json`, `battles.json` and `admission-check.json`.
- Independent counts confirm **40/127** dossiers, **87 without**, and **8/36** complete frozen campaigns by dossier presence. These are coverage counts, not historical or review completeness.
- The next incomplete group by earliest frozen engagement date and campaign label is **Confederate Heartland Offensive [June-October 1862]**, beginning **1862-06-07**: **TN005, TN006, KY007, KY008, KY009**.
- Every packet's three JSON blocks match its current assigned battle, dossier and registry. All receipt hashes verify: **59 inputs, 273 sources, seven outputs**.
- Offline `make check` passed **82 tests**, followed by a successful pipeline check with `artifacts_written: false`. The baseline remains **23 eligible engagements / 13 groups**, strength Brier **0.2768816348133779** versus equal-odds **0.25**. Both admission proposals are unchanged; **zero rows are promoted** and the emitted-row list is empty. Coverage has not improved the baseline result.

No network access, new source families, agents, build/packet commands, primary-artifact edits, commits or pushes were performed. Only this review was written. The previous dossiers were checked for preservation, not re-reviewed for entailment. No original orders, returns, manuscripts, maps or printed pages were inspected. Mechanical checks cannot resolve R1 or adjudicate historical truth. This AI review fulfills only its demonstrated separate-analysis scope; it does not establish independent corroboration, human historical adjudication, causal effects or feature admission.
