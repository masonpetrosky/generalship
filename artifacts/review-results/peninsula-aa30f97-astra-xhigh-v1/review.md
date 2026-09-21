# Peninsula first pass: separate source review

**Decision: no required corrections.** The sixteen dossiers are acceptable as
bounded, source-attributed first-pass drafts within the inspected scope. This
decision does not resolve their historical disputes, establish source independence,
admit model features, or require another research-depth cycle.

Reviewer: separate AI task `/root/peninsula_review`, GPT-6 Astra
(`gpt-6-astra`), `xhigh`, fresh context; reviewed 2026-09-20. Prepared commit:
`aa30f97e0329e6c2714acdb04ab5b8840835ba51`; comparison commit:
`c316ae69530df14fff1675cc6c35dec4aef7cb32`. HEAD matched the prepared commit.
All 80 paths in [inputs.json](inputs.json) matched both their declared SHA-256
values and the prepared Git objects.

The assignment and supplied primary results were inputs, not substitutes for the
independent checks below. Their SHA-256 bindings are:

- `assignment.md`: `11b98b04b1dcdd7de071c2da6fa5288bd9fbe32cc46aa27b3aa1415dd6e7e602`
- `inputs.json`: `800829e9d681d066d2864d6a252f1d9b120323173c5ced166be49ec7a660d95a`
- `primary-validation.json`: `4bf1e6f55f20cef484a0609c3ccd93aef93f2c53c74d3ae86203b29b16b50293`

## Actual inspection

I read all **152 claims and 209 citation occurrences**, including their values,
statuses, phases, rationales, boundary notes and open questions. All sixteen
dossiers cover the seven required dimensions. Their **39 null unknowns** comprise
16 opening strengths, 15 information states, six logistics states, and Hampton
Roads' terrain and assigned objectives. Unknown claims have null values and no
fabricated citations.

| Dossier | Claims | Unknowns | Citations |
| --- | ---: | ---: | ---: |
| VA008 | 10 | 5 | 12 |
| VA009 | 9 | 2 | 11 |
| VA010 | 9 | 3 | 11 |
| VA011 | 9 | 2 | 13 |
| VA012 | 10 | 2 | 13 |
| VA013 | 9 | 2 | 12 |
| VA014 | 9 | 2 | 13 |
| VA015 | 10 | 3 | 12 |
| VA016 | 10 | 3 | 13 |
| VA017 | 9 | 2 | 12 |
| VA018 | 9 | 2 | 13 |
| VA019 | 10 | 2 | 15 |
| VA020 | 9 | 2 | 13 |
| VA020A | 10 | 2 | 17 |
| VA020B | 10 | 2 | 17 |
| VA021 | 10 | 3 | 12 |
| **Total** | **152** | **39** | **209** |

Source inspection covered all fifteen retained NPS battle summaries, VA020's empty
HTML template, the complete retained 1862 Drewry's Bluff history, Webb's catalog
metadata, title and complete preface, and all twelve selected battle/context
passages. I checked adjacent OCR context at every selection boundary, including
the Jackson report footnote, and the HTML selection boundaries. I also read all
sixteen frozen battle rows and their force and commander row sets, and checked the
cited cells. I read the campaign memo, generated report, governing documentation,
source metadata, and the small report/test changes.

This was digital text, HTML, OCR and CSV review. I did not inspect print, maps,
original orders, strength/casualty returns or the original documents quoted by
Webb; I did not read his whole book. No network research or additional source
family was used. Earlier dossiers were checked for preservation, not re-reviewed
for historical entailment.

## Evidence assessment

The claims are supported at their stated, attributed level. In particular:

- **Population and timing:** `reported-force-scope` preserves vessel counts,
  formation labels and imported totals without converting them into matched
  opening personnel. Williamsburg, Beaver Dam Creek and Gaines' Mill retain
  their imported estimates without validating an opening boundary. Live zeros
  remain missingness problems. VA019 `hospital-population-scope` correctly keeps
  Webb's 2,500 sick/wounded and 500 medical personnel/attendants separate from
  NPS's more-than-2,500 wounded and from newly incurred battle casualties
  (`webb-peninsula-selections-v1`, `savage-hospital`, OCR p.141;
  `nps-va019-v1`, Description).
- **Attribution and chronology:** VA009's Keyes ammunition statement, VA010's
  Sumner/Heintzelman command ambiguity, VA011's initial concept versus arrival
  instructions, and VA018's reported hesitation remain Webb's retrospective
  account and embedded quotations. They are not presented as separately inspected
  messages or verified contemporary knowledge. VA014 retains the reported
  Johnston-to-Smith sequence without an invented assumption clock and flags the
  live rank inconsistency. VA021 distinguishes McClellan's orders from Humphreys's
  placement role (`malvern-position-and-command`, OCR p.154).
- **Conditions and outcomes:** Natural ground and prepared defenses remain
  distinct. Local ammunition exhaustion and end-of-action ammunition limits do
  not become opening readiness. Oak Grove's local advance versus the frozen
  withdrawal wording remains an explicit scope dispute. Beaver Dam and Malvern
  retain their frozen Union results alongside subsequent withdrawals. Casualty
  discrepancies are preserved without silently replacing the frozen values.
  Retrospective criticism, counterfactual opportunities and campaign-success
  rhetoric are not adopted as causal measurements.
- **June 30 overlap:** VA020/VA020A/VA020B remain three frozen records describing
  overlapping operations, not additive wins, casualties or command credit.
  `arnold-cwsac-battles`, VA020A `description`, expressly permits treating White
  Oak Swamp as part of Glendale. The current VA020 exclusion reasons are exactly
  `inconclusive_outcome` and `missing_numeric_strength`; its raw `operation` is
  `0`. The dossiers correctly avoid claiming an implemented aggregate/overlap
  exclusion. The cross-sector claims identify their scope and do not resolve
  future admission boundaries.

Fourteen land dossiers use `nps-cwsac` and `webb-peninsula-1881`; Hampton Roads
and Drewry's Bluff use only `nps-cwsac`. HTML/text copies and embedded officer
quotations add no families. Independence remains unestablished. Webb's catalog
and OCR title support 1881; his preface ends November 1881 without a day. His
participant-memory and War Department compilation disclosures are represented
accurately. Narrative section dates remain null. Hampton Roads' reported access
failures were not retried; search snippets supply no retained evidence.

## Mechanical verification and limits

All **17 text derivatives** replayed exactly from their retained parents: fifteen
NPS battle summaries, the Drewry selection and the sectioned Webb selection.
All **13 half-open Unicode ranges** reproduced the stored historical sections
using only whitespace collapse. The June 30 selection retains
`* Jackson's Report, iv., p. 42.`; that locator does not independently authenticate
the report. The Webb parent SHA-256 is
`b6280976621a6d70345167fab1ad7c7dd38090231757129c728454379ab14baa` and selection SHA-256 is
`3be92161e849b9dc70641460db2a1bc39ca56b9186992747f41aeb3dbaaaa2be`.
The new NPS source identities and hashes are bound in the verified source registry
and input manifest. VA020 has no battle data labels; VA020A has structured fields
but no narrative. Neither absence is filled with invented evidence.

Independent preservation checks confirmed **259 source records / 256 raw paths**;
all **223 prior records / 220 prior paths** are unchanged. All 17 earlier current
dossiers and five historical dossier revisions are byte-identical to the comparison
commit. The cohort, both admission proposals and protected admission snapshots
are unchanged. Every registry file hash matched. All sixteen prepared packets'
three JSON blocks matched the current imported record, dossier and registry;
the receipt's **52 input, 259 source and seven output hashes** matched.

Coverage independently recomputes to **33/127 dossiers, 94 without, and 7/36
complete source campaigns by dossier presence**. Ordering incomplete campaigns by
earliest engagement date and campaign label selects **Jackson's Valley Campaign
[March-June 1862]**, starting 1862-03-23: VA101, VA102, WV009, VA103, VA104, VA105
and VA106. Coverage does not change the admission constraints for that group.

`make check` passed offline: **82 tests**, followed by successful
source/evidence/pipeline validation with `artifacts_written: false`. Read-only
admission checks retain v1's **18 blocked / 22 excluded** and v2's **7 blocked /
33 excluded**, with **zero promoted rows**. The unchanged baseline has **23
eligible engagements in 13 groups** and Brier **0.2768816348133779**, worse than
equal odds at **0.25**. More draft coverage does not demonstrate improvement.

There are no required replacements or unresolved extraction findings from this
review. Historical strength, casualty, authority, information and source-dependence
questions remain as documented. This separate AI analysis fulfills only the
demonstrated bounded review scope, not human historical adjudication or feature
admission. I wrote only this review; I did not mutate evidence, run build/packet
commands, commit or push.
