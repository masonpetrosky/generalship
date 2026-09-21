# Burnside campaign: separate AI source review

**Outcome: no required corrections within the assigned first-pass scope.** All
47 claims, including ten null unknowns, and all 73 citation occurrences were
reviewed against the retained evidence. The source-attributed descriptions and
explicit disputes are acceptable as drafts; this does not adjudicate the history
or admit model features.

Reviewer: fresh-context subagent `/root/burnside_review`, GPT-6 Astra,
`xhigh` reasoning. Review date: **2026-09-20**. Prepared commit:
`0b3337fea1ee57375d5999d49f5f58f3d1bcc4a3`; comparison commit:
`a22ac6dc079956e477178130a0e9e72e6f6bcc01`. Assignment and exact per-path
SHA-256 bindings are retained in [assignment.md](assignment.md) and
[inputs.json](inputs.json). The latter's SHA-256 is
`04df5052b95d7ccf77f7154a8b042e4f96af83ecc7069708daf7ab529ebf96dd`.
All **35 bound input hashes** matched both the prepared Git objects and the
working files inspected.

## Actual inspection

| Dossier | Claims reviewed | Citation occurrences | Null unknowns |
| --- | ---: | ---: | ---: |
| NC002 — Roanoke Island | 9 | 16 | 1 |
| NC003 — New Berne | 9 | 14 | 2 |
| NC004 — Fort Macon | 10 | 16 | 2 |
| NC005 — South Mills | 10 | 16 | 2 |
| NC006 — Tranter's Creek | 9 | 11 | 3 |
| **Total** | **47** | **73** | **10** |

I read every claim, rationale, citation and open question, all seven dimensions
per dossier, the campaign memo and relevant repository contracts. I inspected
the five complete retained NPS summaries; Woodbury's catalog metadata, title and
complete preface; and all six selected narrative sections: Roanoke information
(OCR pp.32–33), Roanoke weather (p.37), New Berne approach (pp.55–56), Fort Macon
(pp.71–74, including the following page header), South Mills (pp.80–84), and
Tranter's Creek (p.90). This included the retained naval-vessel footnote,
Lockwood report reference, Hawkins quotation and subsequent naval action.
I checked adjacent parent boundaries and OCR page markers, plus all five frozen
battle rows, ten force rows and ten commander rows. No print facsimile, map,
original report, manuscript, whole book or additional source family was inspected.

All five HTML-to-text extractions reproduced byte-for-byte using the declared
script/style exclusion and text-node/boundary rules. The seventh historical
section in the Woodbury selection is its title/preface: all seven historical
sections reproduced exactly from the registered half-open Unicode offsets and
whitespace-only normalization. Section inventory, local transcription note and
parent hashes were checked. Thus all **six text derivatives** replayed, without
repairing OCR. All five prepared packets contain the matching assigned record,
current dossier and full source registry.

## Evidence assessment

- **Roanoke:** the landing count, imported forces-engaged estimates, casualty
  categories and captured prisoners remain distinct. The NPS field surrender by
  Shaw does not silently transfer Wise's principal listing or erase naval support.
  Woodbury's Tom interview and weather narrative are attributed retrospective
  claims, without an invented intelligence value or command effect.
- **New Berne:** wet landing, muddy marching and sailors hauling howitzers are
  supported by the retained passage. Neither these descriptions nor its language
  about spirits becomes a readiness score. The 1,080/1,085 casualty difference,
  blank frozen strengths and live zero display remain unresolved.
- **Fort Macon:** the approximate five-hundred-person garrison is not a matched
  opening population. Bridge delay, siege preparation and Parke's assigned role
  are supported; Lockwood's constrained naval participation remains in context.
  April 26 versus April 25, the unrepaired OCR `23th`, and 490 versus 442 casualties
  remain explicit. Woodbury's killed/wounded counts are not equated with the
  broader aggregates.
- **South Mills:** the fuller expedition roster does not establish identical
  participation or numerical strength. The canal-name/objective discrepancy and
  Woodbury's favorable result characterization remain separate from the frozen
  inconclusive result. Hawkins's charge is attributed, without validated fault
  or motive. The later Musser naval obstruction is not credited to Reno's April 19
  action; the 150/139 totals are not silently reconciled with Woodbury's Union losses.
- **Tranter's Creek:** formation names and the twenty-five-person gun crew do not
  become total strength. Potter's order and Osborne/Osborn's action remain
  distinct. The 40-versus-zero casualty discrepancy, logistics/information gaps
  and return without pursuit are preserved without speculative opportunity costs.

The thirteen new source records consistently retain **two families per battle**:
NPS/CWSAC and one interested Woodbury history. The preface supports the disclosed
non-eyewitness status and dependence on officers' assistance/papers. Quoted reports,
formats and repeated appearances add no witnesses. Neither family bookkeeping nor
this review proves independence. The December 1866 preface and 1867 publication
remain separate from unknown narrative composition dates.

## Verification and remaining limits

`make check` passed **82 tests** and the offline pipeline check, reporting
`artifacts_written: false`. I independently confirmed preservation of all **203
prior source records / 200 raw paths**, all **ten earlier dossiers and five
archived dossier files**, the cohort, both admission proposals and the complete
baseline artifact. The current registry is **216 records / 213 raw paths**.
The generated report matched an in-memory rendering; all 34 receipt input hashes
and seven output hashes matched, without running a tracked-artifact build or packet
command.

Coverage is **15/127 dossiers, 112 without, and 5/36 complete frozen groups by
dossier presence**. Both admission proposals still promote **zero rows** (v1:
18 blocked / 22 excluded; v2: 7 blocked / 33 excluded). The unchanged baseline
has **23 eligible engagements in 13 groups**, Brier **0.2768816348133779** versus
equal odds **0.25**; additional dossier coverage has not improved that result.
Sorting incomplete frozen campaigns by earliest engagement date and label confirms
**New Madrid/Island No. 10 and Memphis — MO012/TN004**, beginning February 28,
1862, as next.

Matched opening populations, original contemporary information, casualty/date/canal
reconciliation and print verification remain deferred. This separate AI review
fulfills only the demonstrated source-review scope; it is not human historical
adjudication, source independence, feature admission or permission to deepen the
parked investigations. No primary evidence was edited, and no commit or push was
made by this reviewer.
