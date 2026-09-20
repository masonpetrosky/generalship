# Shiloh frozen-bundle source review

Three material metadata/contract corrections and one minor wording correction are proposed. The checked source selections do not justify choosing a canonical strength or resolving the existing historical disputes. No substantive transcription mismatch was found in the selected passages/cells compared across all 26 supplied images.

This completed **AI review** was performed by **`/root/shiloh_source_review`**, dispatched as **GPT-6 Astra (`gpt-6-astra`), xhigh**, with fresh context, on **2026-09-20**. The identity/model/effort are those supplied by the actual subagent dispatch. This is a separate analysis, not human historical adjudication, proof of source independence, a dossier-status change or feature admission.

## Findings

### TN003-R1 — material: Keep source estimation status separate from printed numerical precision

**Affected fields:** `quantities[id in affected_quantity_ids].estimate_kind`; `proposed quantities[*].estimation_status`; `docs/evidence-contract.md: Estimate kinds and estimated-entry precision rule`.

**Claims:** `eighteenth-wisconsin-return-omission`, `reed-sixth-division-reconstruction`, `reed-ohio-estimates-and-discrepancy`.

**Quantities:** `reed-eighteenth-wisconsin-estimate`, `reed-mccook-detail-engaged`, `reed-mccook-recap-engaged`, `reed-crittenden-engaged`, `reed-sixth-reconstruction`, `reed-ohio-total-engaged`.

**Current representation:**

```json
[
  {
    "quantity_id": "reed-eighteenth-wisconsin-estimate",
    "estimate_kind": "reported_exact",
    "lower": 735,
    "upper": 735,
    "note": "Asterisk means Estimated. reported_exact preserves printed precision only, not an exact measured population."
  },
  {
    "quantity_id": "reed-mccook-detail-engaged",
    "estimate_kind": "reported_exact",
    "lower": 7553,
    "upper": 7553,
    "note": "Printed 7,553; marked Approximated. Different from 7,552 in recap and note j. reported_exact retains printed precision, not measurement accuracy."
  },
  {
    "quantity_id": "reed-mccook-recap-engaged",
    "estimate_kind": "reported_exact",
    "lower": 7552,
    "upper": 7552,
    "note": "Printed 7,552, supported by secondhand estimate in note j; differs from detail by one. reported_exact retains printed precision, not measurement accuracy."
  },
  {
    "quantity_id": "reed-crittenden-engaged",
    "estimate_kind": "reported_exact",
    "lower": 3825,
    "upper": 3825,
    "note": "Marked Approximated. Fourteenth Brigade lacks March/April reports in this compilation. reported_exact retains printed precision, not measurement accuracy."
  },
  {
    "quantity_id": "reed-sixth-reconstruction",
    "estimate_kind": "reported_exact",
    "lower": 7545,
    "upper": 7545,
    "note": "Printed exact total contains estimates and mixed dates. Not a corrected original return or a single-time census."
  },
  {
    "quantity_id": "reed-ohio-total-engaged",
    "estimate_kind": "reported_exact",
    "lower": 17918,
    "upper": 17918,
    "note": "Includes estimated and differently timed components; uses 7,552, not detail 7,553. Overlaps all component observations. reported_exact retains printed precision, not measurement accuracy."
  }
]
```

The records comply with the current contract: reported_exact denotes precision as printed. Nevertheless, the single enum cannot express an explicitly estimated non-round integer or a total containing estimated components. Those states are available only in prose, unlike the typed approximate status for Wagner. This is a contract gap before machine-readable evidence selection, not a finding that the printed numbers or their notes are false. No uncertainty interval can be invented from the asterisk.

**Inspected evidence:**

- `reed-1909-union-audit-v1`, `p96`, SHA-256 `87e1da1572aaceb0bb73422f008e411872174de01153d9d80a4659ceabdaee2f`: “18th Wisconsin* (note d) | 35 | 700 | 735” Visual comparison: `data/raw/shiloh/reed-1909-union-p96-facsimile-v1.png`.
- `reed-1909-union-audit-v1`, `p97`, SHA-256 `87e1da1572aaceb0bb73422f008e411872174de01153d9d80a4659ceabdaee2f`: “* Estimated.” Visual comparison: `data/raw/shiloh/reed-1909-union-p97-facsimile-v1.png`.
- `reed-1909-ohio-strength-v1`, `p100`, SHA-256 `9af7a9d42181a4cba1e3f7fffc0d73a3bd26c4b48aced3a9f3241711e939167a`: “Number Second Division engaged at Shiloh Apr. 7* | 7,553” Visual comparison: `data/raw/shiloh/reed-reinforcement-p100-facsimile-v1.png`.
- `reed-1909-ohio-strength-v1`, `p101`, SHA-256 `9af7a9d42181a4cba1e3f7fffc0d73a3bd26c4b48aced3a9f3241711e939167a`: “* Approximated. Note j.” Visual comparison: `data/raw/shiloh/reed-reinforcement-p101-facsimile-v1.png`.
- `reed-1909-ohio-strength-v1`, `p111-note-j`, SHA-256 `9af7a9d42181a4cba1e3f7fffc0d73a3bd26c4b48aced3a9f3241711e939167a`: “I estimate McCook's present for duty at 7,552.” Visual comparison: `reviews/TN003-a42f063-v1/pages/reed-p111.png`.
- `reed-1909-ohio-strength-v1`, `p102`, SHA-256 `9af7a9d42181a4cba1e3f7fffc0d73a3bd26c4b48aced3a9f3241711e939167a`: “Total Army of the Ohio | 17,918” Visual comparison: `data/raw/shiloh/reed-reinforcement-p102-facsimile-v1.png`.

**Exact proposed changes:**

```json
[
  {
    "field": "quantities[id=reed-eighteenth-wisconsin-estimate].estimation_status",
    "current": null,
    "proposed": "explicit_estimate"
  },
  {
    "field": "quantities[id=reed-mccook-detail-engaged].estimation_status",
    "current": null,
    "proposed": "explicit_estimate"
  },
  {
    "field": "quantities[id=reed-mccook-recap-engaged].estimation_status",
    "current": null,
    "proposed": "explicit_estimate"
  },
  {
    "field": "quantities[id=reed-crittenden-engaged].estimation_status",
    "current": null,
    "proposed": "explicit_estimate"
  },
  {
    "field": "quantities[id=reed-sixth-reconstruction].estimation_status",
    "current": null,
    "proposed": "aggregate_includes_estimates"
  },
  {
    "field": "quantities[id=reed-ohio-total-engaged].estimation_status",
    "current": null,
    "proposed": "aggregate_includes_estimates"
  }
]
```

Add estimation_status as a separate, validated field; allow explicit_estimate, aggregate_includes_estimates, reported_without_explicit_estimation_qualifier, and unknown. Preserve lower/upper, printed precision, source qualifiers, existing disputed alternatives, and null uncertainty bounds. reported_without_explicit_estimation_qualifier must not mean independently measured or accurate. Any migration must be versioned; these recommendations are not a modification of the frozen schema.

**Remaining uncertainty:** The sources provide neither defensible error bounds nor a reconciled true strength. Additional source needed to make this correction: **no**. No additional source is needed to encode the printed qualifiers; estimating their historical error needs further evidence.

### TN003-R2 — material: Scope report dates to their sections in mixed report/diary/compiler sources

**Affected fields:** `data/sources.json: or-ammen-crossing-v1.document_date`; `data/sources.json: or-nelson-reinforcements-v1.document_date`; `proposed source sections[].document_date`.

**Claims:** `ammen-crossing-sequence`, `ammen-night-formation`, `nelson-action-strength`, `nelson-march-paper-strength`.

**Quantities:** `nelson-taken-into-action`, `nelson-thirtysixth-taken-into-action`, `nelson-march-abstract`.

**Events:** `ammen-savannah-arrival`, `ammen-night-reassembly`.

**Current representation:**

```json
[
  {
    "source_id": "or-ammen-crossing-v1",
    "document_date": "1862-04-10",
    "document_date_note": null
  },
  {
    "source_id": "or-nelson-reinforcements-v1",
    "document_date": "1862-04-10",
    "document_date_note": null
  }
]
```

The dossier prose correctly withholds a diary composition date and exact March muster day. Both source records nevertheless expose an unqualified source-wide April 10 document_date. A consumer must read prose to avoid applying the report date to the diary, attached table, or compiler abstract. April 12 and 16 datelines on adjacent pages belong to other letters and do not cure this. The current quantity dates are not being accused of this conflation; the correction is to source metadata and its contract.

**Inspected evidence:**

- `or-ammen-crossing-v1`, `p327-heading`, SHA-256 `df186eb4f91fdb6dbc87cbf8e86e526f6d3f18c8dcc9730a858e7d3dc4ef9b93`: “April 10, 1862.” Visual comparison: `data/raw/shiloh/or-reinforcement-p327-facsimile-v1.png`.
- `or-ammen-crossing-v1`, `p329-diary-heading`, SHA-256 `df186eb4f91fdb6dbc87cbf8e86e526f6d3f18c8dcc9730a858e7d3dc4ef9b93`: “Col. Jacob Ammen's diary of march to and battle at Pittsburg Landing, Tenn. [Extracts.]” Visual comparison: `reviews/TN003-a42f063-v1/pages/or-p329.png`.
- `or-ammen-crossing-v1`, `transcription-scope`, SHA-256 `df186eb4f91fdb6dbc87cbf8e86e526f6d3f18c8dcc9730a858e7d3dc4ef9b93`: “Diary extracts on pp.329 onward have event-date labels but their composition/submission date is not established here.” Text inspection only; no corresponding page image comparison.
- `or-nelson-reinforcements-v1`, `p323-heading`, SHA-256 `e75987c53540b8ad09b7cf108204b7f7f9e6343b09da01570e862dba309986ed`: “Camp on the Field of Battle, April 10, 1862.” Visual comparison: `reviews/TN003-a42f063-v1/pages/or-p323.png`.
- `or-nelson-reinforcements-v1`, `p327-march-return`, SHA-256 `e75987c53540b8ad09b7cf108204b7f7f9e6343b09da01570e862dba309986ed`: “Abstract from return of the Fourth (Nelson's) Division, Army of the Ohio, for the month of March, 1862.” Visual comparison: `data/raw/shiloh/or-reinforcement-p327-facsimile-v1.png`.

**Exact proposed changes:**

```json
[
  {
    "source_id": "or-ammen-crossing-v1",
    "field": "document_date",
    "current": "1862-04-10",
    "proposed": null
  },
  {
    "source_id": "or-ammen-crossing-v1",
    "field": "document_date_note",
    "current": null,
    "proposed": "Mixed report and separately printed diary. April 10, 1862 dates the report only; diary composition/submission date is unknown. Event dates are distinct."
  },
  {
    "source_id": "or-ammen-crossing-v1",
    "field": "document_dates_by_section",
    "current": null,
    "proposed": {
      "p327-heading": "1862-04-10",
      "p328-report": "1862-04-10",
      "p329-diary-heading": null,
      "p330-diary": null,
      "p333-diary": null,
      "p334-diary": null
    }
  },
  {
    "source_id": "or-nelson-reinforcements-v1",
    "field": "document_date",
    "current": "1862-04-10",
    "proposed": null
  },
  {
    "source_id": "or-nelson-reinforcements-v1",
    "field": "document_date_note",
    "current": null,
    "proposed": "April 10, 1862 dates Nelson's report. Preparation dates of the attached action table and compiler March abstract are not established; their event/reporting periods remain separate."
  },
  {
    "source_id": "or-nelson-reinforcements-v1",
    "field": "document_dates_by_section",
    "current": null,
    "proposed": {
      "p323-heading": "1862-04-10",
      "p323-crossing": "1862-04-10",
      "pp323-324-action": "1862-04-10",
      "p324-night": "1862-04-10",
      "p324-morning": "1862-04-10",
      "p324-artillery": "1862-04-10",
      "p325-strength": "1862-04-10",
      "p326-return": null,
      "p327-march-return": null
    }
  }
]
```

**Remaining uncertainty:** Diary composition/submission date, attached-table preparation date and exact March muster day remain unknown; no receipt or command-knowledge date is supplied. Additional source needed to make this correction: **no**. Supplied evidence suffices to keep uncertain dates null; recovering the dates requires new sources.

### TN003-R3 — material: Unify the dependence group of two transcriptions of the same OR p.112 return

**Affected fields:** `data/sources.json: or-union-return-detail-v2.independence_group`; `data/sources.json: or-union-return-detail-v2.facsimile_source_id`.

**Claims:** `union-return-strength`, `sixth-division-return-components`, `reed-sixth-division-reconstruction`.

**Quantities:** `union-paper-total`, `wallace-april4-return`, `sixth-april5-abstract`.

**Current representation:**

```json
{
  "or-union-return-detail-v2.independence_group": "or-grant",
  "or-union-return-april4-5.independence_group": "or-union-returns",
  "or-union-return-scan.independence_group": "or-union-returns",
  "or-union-return-detail-v2.facsimile_source_id": null
}
```

The same parent hash, printed page and overlapping Sixth Division row establish document identity, not merely possible historical dependence. Splitting these representations across groups contradicts the registry purpose and makes a group-based evidence count misleading. Distinct groups do not prove independence even after this correction.

**Inspected evidence:**

- `or-union-return-april4-5`, `p112`, SHA-256 `e7b9aee495475a62721a811490c442f8019bc689a02dd841db0a5fbd60f8727e`: “Total Sixth Division | 245 | 5,218 | 5,463 | [blank]” Visual comparison: `data/raw/shiloh/or-union-return.png`.
- `or-union-return-detail-v2`, `p112`, SHA-256 `70099ece7f07cf264d777f3e9d80e49ec40c230b5c671962e3cdc0dbfd4f2c94`: “Total Sixth Division | 245 | 5,218 | 5,463” Visual comparison: `data/raw/shiloh/or-union-return.png`.
- `or-union-return-detail-v2`, `transcription-scope`, SHA-256 `70099ece7f07cf264d777f3e9d80e49ec40c230b5c671962e3cdc0dbfd4f2c94`: “Additional selected detail from the already pinned full-page facsimile or-union-return.png.” Text inspection only; no corresponding page image comparison.

**Exact proposed changes:**

```json
[
  {
    "source_id": "or-union-return-detail-v2",
    "field": "independence_group",
    "current": "or-grant",
    "proposed": "or-union-returns"
  },
  {
    "source_id": "or-union-return-detail-v2",
    "field": "facsimile_source_id",
    "current": null,
    "proposed": "or-union-return-scan"
  }
]
```

**Remaining uncertainty:** Dependencies between different original army reports remain unresolved. The correction establishes only that these are representations of the same return. Additional source needed to make this correction: **no**. 

### TN003-R4 — minor: Describe Crittenden's 21:00 as arrival at the landing, before debarkation

**Affected fields:** `claims[id=crittenden-arrival-phases].value`.

**Claims:** `crittenden-arrival-phases`.

**Events:** `crittenden-night-landing`.

**Current representation:**

```json
"Crittenden reports landing about 21:00 April 6, deployment about 05:00 April 7, and the Third Kentucky Cavalry remaining opposite the landing for lack of transport."
```

The source separates reaching the landing from subsequent debarkation. The claim says landing at 21:00, which can be read as completion of disembarkation; its rationale and event note already preserve the correct sequence. Tighten the headline to match them. No exact completion time is recoverable.

**Inspected evidence:**

- `or-crittenden-reinforcements-v1`, `p355`, SHA-256 `235b01590b21cbf161ebe63162db73cf45184bd234f4025deae555040f317391`: “We reached Pittsburg Landing at about 9 o'clock p. m. By order of General Buell my command was debarked as soon as it could be done, it being important to send back the boat, that McCook's division might be brought up for the battle of the next day.” Text inspection only; no corresponding page image comparison.

**Exact proposed changes:**

```json
[
  {
    "field": "claims[id=crittenden-arrival-phases].value",
    "current": "Crittenden reports landing about 21:00 April 6, deployment about 05:00 April 7, and the Third Kentucky Cavalry remaining opposite the landing for lack of transport.",
    "proposed": "Crittenden reports reaching Pittsburg Landing about 21:00 April 6, with debarkation following as soon as practicable; he reports being conducted to his position about 05:00 April 7 and the Third Kentucky Cavalry remaining opposite the landing for lack of transport."
  }
]
```

**Remaining uncertainty:** Completion of debarkation, clocks shared across authors, and the exact time the entire division was ready are unestablished. Additional source needed to make this correction: **no**. Supplied text supports the wording change; no p.355 image is supplied, so its transcription remains image-unverified.

## Coverage and byte identity

| Category | Inspected | Not reviewed | Cannot verify |
|---|---:|---:|---:|
| Claim entailment, rationale/status/phase | 62/62 | 0 | 0 |
| Typed quantities and citation links | 40/40 | 0 | 0 |
| Events and entity/claim references | 26/26 | 0 | 0 |
| Supplied scan selections | 26/26 (13 table + 13 supplementary) | 0 | 0 |
| Explicit unknowns | 3/3, all retained null | 0 | 0 |

Coverage is complete for the bounded assignment; **image-level transcription coverage across all cited passages is partial**. `review-result.json` names the exact sections/cells checked on every image and lists all image-unverified cited sections. The scan sample is purposive; no extraction-error rate is inferred. “Checked” does not certify every page cell or unexcerpted paragraph. No full parent volume was opened.

Inspected cited evidence comprises 32 source artifacts and 65 unique cited source/section pairs (unsectioned NPS and the exact CSV locator count as pairs); 30 pairs have supplied image comparisons, while 35 are text/CSV-only. All numeric source disagreements remain disagreements, not transcription failures.

`python3 verify_bundle.py` passed for all **106 payload files**. The dossier and source registry hashes were also recomputed separately.

- Bundle: `TN003-a42f063-v1`
- Evidence commit: `a42f06390651eea01d952a7cb7c329f410a6f9ab`
- Dossier SHA-256: `1107b7149f9aa3877478e003a01ae2383b5d0729a15d6a90106e427350d49780`
- Source registry SHA-256: `a71f16285be84504048826255c0abcb49488c5d96f8e048ca5259ad523cc0e8b`
- Original ZIP SHA-256 supplied by dispatch: `f1e1f7bc2aec3074b02408649fd29184ba380bfd2486d77f2184341f6aff8a13`; the reviewer did **not** independently open/hash the original ZIP.

The supplied historical passages were read before the author’s research memos, and scan comparisons were completed before reading those memos. Prior dossier archives were hash-verified only. Source IDs and hashes, per-row evidence, decisions and all image hashes are retained in the completed JSON.

## What remains unresolved

- **TN003-D1:** 40,335/29,636 versus 38,773/32,212, infantry subtotal discrepancies, Hill/Carroll/cavalry accounting, effective/PFD definitions and NPS 44,968 remain unresolved. Preserve values and unknown underlying muster dates; no numerical repair or casualty subtraction.
- **TN003-D2:** Original Prentiss attachment A, full two-regiment/one-battery omission identities and the 899-versus-889 ten-man residual remain unresolved. Late additions are not automatically the unnamed original omissions.
- **TN003-D3:** Michigan Sunday fighting versus Reed recap exclusion; Force Sunday casualty allocation versus Michigan two-day sentence; 750, 730, about 230 and 869 are different scopes. No canonical opening count.
- **TN003-D4:** Lost order and route responsibility, primary accounting for the 1,727 guards, the 43-person arithmetic residual, secondhand 5,000 and the 6,500/5,800 derivations remain unresolved; 7,564 paper and 5,837 convention-based engaged are not interchangeable.
- **TN003-D5:** Nelson 13:30/four hours/17:00, handbook opposite-bank arrival at 17:00 and about 600 by 18:00, regimental landings and next-morning 05:20/05:30 are not one synchronized clock. About 400 and 380 differ in scope; no casualty inference.
- **TN003-D6:** Nelson 6,724 for March, Reed 5,535 for March 31 and 4,541 taken into action; mixed-date Ohio reconstruction; 7,553/7,552; late Wagner 2,000; 17,918 versus Force about 20,000; and the original/date of Buell's quoted letter remain unreconciled.
- **TN003-D7:** Order receipt/modification, camp-selection authority, effective succession, dispatch knowledge, tactical and campaign replacement boundaries remain unset. Phase labels are hypotheses; no commander credit is established.

The three null claims remain justified: no army-wide numerical logistics/readiness record; no complete mapping of the original Sixth Division omissions; no exact common-time Sunday Nelson contingent. Ammen’s supplied p.334 scan contains an additional limited account of 60 rounds per man before April 7. Its diary composition date is unknown, and that sentence is outside the selected text snapshot. It does not establish actual ammunition distribution across the army or authorize a readiness score; the JSON preserves this as inspected supplementary context, not a new quantity.

Source dependence remains substantive. Nelson and subordinates share a reporting environment; Ammen’s report and diary are one author; Reed, Force and the handbook draw on prior reports; a scan and transcript are one representation family; Michigan’s underlying returns and possible casualty-account dependencies are untraced. Even corrected independence groups do not certify independent testimony.

## Required corrections and next review boundary

Reconcile **R1–R4** and preserve this review unchanged. Apply accepted corrections only in versioned metadata/evidence/contract records with a documented migration; retain the original raw files, bundle and competing numbers. R1 and R2 are limits of the existing machine-readable contract, not accusations that the carefully qualified dossier prose has already admitted false predictors.

The completed, fully scoped AI review can satisfy this bounded separate-review step after primary reconciliation. Further source-independent or human specialist review may help adjudicate missing records and historical disputes before selecting particular strengths or causal attributions. **Another human review is not an automatic prerequisite to designing feature admission.**

**Recommendation:** proceed to design the feature-admission contract with estimation provenance, section-specific document dates, same-document dependence, overlap rules, explicit unknowns and post-outcome exclusions. Preserve unsettled command/replacement boundaries and reject automatic credit from commander lists. This review does not approve any enriched feature or canonical opening-strength row.

No frozen model inputs changed. The supplied baseline remains **23/127 engagements, 13 eligible campaign groups within 36 campaigns**, with Brier **0.276882 versus 0.250000** for equal odds. This review does not improve those results or establish causality.
