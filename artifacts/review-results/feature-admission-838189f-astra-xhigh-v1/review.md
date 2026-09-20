# Separate feature-admission design review

**Verdict: accept.** The specification at commit `838189f32b6ce1deec3daa14251c5ebf784626fc` can guide a later offline, non-promoting validator and admission manifest. I found no required design correction. This does not approve any Shiloh feature, change model inputs, or validate an unwritten implementation.

Reviewer: `/root/admission_contract_review`; GPT-6 Astra (`gpt-6-astra`), `xhigh`; fresh context; 2026-09-20T18:58:21.543784+00:00. The dispatch configuration is retained in `dispatch.json`. This is separate AI analysis, not human historical adjudication or independent historical corroboration.

## Findings and design assessment

There are **zero actionable findings and zero unresolved review findings**. No exact correction is proposed.

- **Positive and negative paths:** The ordered gates and explicit invalid > excluded > blocked precedence are implementable. Lines 200-202 resolve first-review waiting as eligible_candidate, distinct from an adverse unresolved review. Synthetic accepted, waiting, adverse, altered-binding and leakage fixtures are required; no historical positive admission is claimed. (`docs/feature-admission.md:186-207`; `docs/feature-admission.md:235-268`).
- **Review binding and replay:** Candidate, profile, boundary, source snapshot and proposal bindings are required. The proposal/final-manifest split avoids a self-hash cycle, requires unchanged approved content, and mandates bounded follow-up for substantive corrections. Metadata aliases bind full entries and immutable snapshots. Future implementation must enforce these requirements; no existing admission implementation was validated. (`docs/feature-admission.md:61-102`; `docs/feature-admission.md:229-240`).
- **Retrospective timing and leakage:** Historical state, document dates, research/publication dates, command knowledge and the research cutoff are distinct. Later reporting is allowed only with an established earlier referent and clean derivation. Post-boundary descendants and unknown potentially outcome-dependent derivation fail closed. Target provenance is separate and score-driven coding/selection is prohibited. (`docs/feature-admission.md:11-32`; `docs/feature-admission.md:104-138`).
- **Population, overlap, uncertainty and scenarios:** Boundary and spatial/population rules are symmetric across sides. Estimates retain precision separately from estimation status. Transforms require acyclic provenance, compatible time/population and evidenced membership/overlap. Only individually applicable alternatives may enter coherent joint scenarios; scenarios are full refits, not extra observations or a rescue for wrong-scope evidence. (`docs/feature-admission.md:36-59`; `docs/feature-admission.md:140-184`).
- **Dependence, coverage, evaluation and estimands:** Aliases and reused returns cannot count as independent votes. The complete 127/36 frame, side/field coverage and complete-row coverage stay distinct. Common-row/fold comparisons, expanded-coverage evaluation and training-set differences must be disclosed. Predictive residuals do not imply command effects; unsupported information-set and causal profiles remain excluded. (`docs/feature-admission.md:25-32`; `docs/feature-admission.md:163-167`; `docs/feature-admission.md:209-227`).

The acceptance matrix is a future implementation requirement, not a claim that the positive path currently runs. A concrete schema, deterministic serialization, gate evaluator, release replay and rejection of production test stubs still need implementation and tests. This distinction is sufficient for the bounded design request.

## All 13 worked cases

| Case | Expected status | Review of the proposed use |
| --- | --- | --- |
| S01 | `excluded` | Whole-engagement totals cannot be relabeled as opening availability; later participation is not the opening population. |
| S02 | `blocked` | Paper total and nested Wallace count need boundary/population/omission review before subtraction can support an opening total. |
| S03 | `blocked` | Summary, detail and image represent one p.112 return; source dependence checks alone do not establish opening applicability. |
| S04 | `blocked` | The competing Confederate pre-battle totals have unresolved muster/composition applicability and cannot yet form an admitted range or scenario pair. |
| S05 | `excluded` | After-battle returns and casualty-based reverse reconstruction are excluded for the opening target. |
| S06 | `excluded` | The mixed-phase 7,545 total is excluded; the estimated 735 remains a separate unresolved candidate and must not be added twice. |
| S07 | `excluded` | The April 7 7,553/7,552 discrepancy remains visible; neither value is an April 6 opening alternative. |
| S08 | `excluded` | The 17,918 recap and nested/mixed-date components cannot become a simultaneous opening population. |
| S09 | `excluded` | Different reported contingents and phases cannot fill the null exact crossing count or opening strength. |
| S10 | `excluded` | The proposed availability/readiness inference is excluded. Ammen Savannah arrival itself is April 5, not a post-boundary event; its location and diary/report distinction do not establish Pittsburg opening availability. Crittenden arrival does not date completed debarkation. |
| S11 | `excluded` | An undefined supply profile plus null evidence cannot produce a numerical predictor. |
| S12 | `excluded` | Causal allocation is unsupported; issue, receipt, death, notification and effective authority are distinct. |
| S13 | `excluded` | The recorded outcome remains in its target channel and cannot be an opening predictor. |

The case statuses describe proposed uses or transformations, not blanket judgments on every constituent record. In particular, S06 preserves a separate possible review path for the 735 estimate, and S10 does not make Ammen’s April 5 Savannah arrival a post-boundary event. These observations are consistent with the case-scope explanation at `docs/research/shiloh-admission-examples.md:18-21`.

## Inspected evidence and exact coverage

- Read all three primary design files and the six required repository context files at the review commit.
- Inspected **13/13 cases**, **26/62 claims**, **27/40 quantities**, and **8/26 events**, including their population/time/estimation qualifications. Selected IDs are enumerated in `review-result.json`.
- Independently verified **115 citation occurrences**: **79 claim citations + 36 quantity-estimation citations**. Every citation object matches the selected dossier records; every quote occurs in the exact selected section or CSV cell; every source-entry/raw hash and section-aware document date matches.
- Read the pinned passage bodies behind **29 distinct source/locator pairs**. They resolve to **28 distinct text/CSV bodies**, because both NPS locators use one unsectioned snapshot. The full source/locator inventory and source hashes are retained in `review-result.json`.
- Verified **21 bound source entries**: **17 directly cited + 4 linked facsimiles**, with **zero images newly reviewed visually**. Metadata aliases and scans are not counted as new witnesses.
- Verified **10 excluded + 3 blocked** design cases, **zero admitted values/features and zero emitted rows**. Independently counted the frozen frame as **127 engagements / 36 source campaign groups**. The bound baseline records **23 eligible engagements / 13 campaigns**, Brier **0.2768816348133779**, versus **0.25** for equal odds.

The inspected passages include `or-union-return-april4-5:p112` and `or-union-return-detail-v3:p112` for the paper totals/omissions; `or-confederate-return:p396` and reports `136:p398` / `137:p399` for differing populations; `reed-1909-union-audit-v1:p96`, `:p97`, `:p111-union-notes` for estimated and later additions; `reed-1909-ohio-strength-v1:p100`, `:p101`, `:p102`, `:p111-note-j` for the McCook discrepancy and reconstruction; and Ammen, Nelson, Grose and Crittenden sections for document/event/participation distinctions. Exact registered source IDs, locators and raw/metadata SHA-256 values are in the structured review. The outcome cell is `arnold-cwsac-battles`, row `battle=TN003`, column `results_text`.

Checks were read-only Python assertions over hashes, references, section dates, counts and cohort metadata. I did not rerun the existing 52-test suite reported in the assignment or treat it as admission-engine validation. No network fetching, image re-transcription, model fitting or historical promotion was performed.

## Unresolved limits

- No exact Shiloh pre-contact definition, engagement area or availability mapping has been established; no canonical opening total or boundary-specific historical feature is approved.
- The p.112 omissions and mixed return dates, Confederate composition/muster and Monday-arrival accounting, and the unreconciled before/after returns remain historical research questions.
- Reed mixed-date and mixed-phase reconstructions, the Sixth Division ten-person comparison residual and McCook 7,553/7,552 discrepancy remain unresolved; no preferred value, uncertainty distribution or scenario probability is established.
- Nelson/Grose contingents and clocks, the handbook 600-person derivation and exact Sunday crossing count remain unresolved; arrival, debarkation, formation and action are distinct.
- Command receipt, effective transfer, responsibility and replacement estimands remain unresolved. No causal commander credit, readiness score or battle/campaign addition is approved.
- This review inspected text/CSV passages and byte/metadata bindings; it did not visually re-review any image. The prior 35/65 text/CSV-only source-section coverage statement is retained from the existing review record, not independently recounted here.
- Quote membership and hash identity are reference-integrity checks, not historical truth, entailment, source independence or human adjudication. AI historical knowledge is not removed by this review.
- No admission engine, production positive-path replay, feature release or enriched evaluation exists in the reviewed change. Future schema/code and acceptance fixtures still require implementation and validation.

## Exact reviewed bindings

| Input | SHA-256 |
| --- | --- |
| `docs/feature-admission.md` | `b858b7a27f3617408779c928ea545da814b31229ff2c40caf64927773f320c99` |
| `docs/research/shiloh-admission-examples.md` | `fc1a32a0ace7580d2782f3f0046a0dbb528e17286d33e2bc0adfe8bed6acaaff` |
| `design/feature-admission-v1/shiloh-examples.json` | `397fb1b0d126b35e182071a50cc878270cf05be9e7ef524ee86e6f1cf40638f5` |
| `data/evidence/TN003.json` | `fb622c81b48110d1d7b25212b5c3f10881c4a7724a9ccbb93ef793816cf100ee` |
| `data/sources.json` | `3430c1ef145256fc8edd8638fdf565f7f0c0ae4e5feed237b3cd5db6cf4322e7` |
| `data/pilot/cohort.json` | `17d08348ed1399a0f0033ded3b1ba40c541d342b6aeed920cf2c26818ee6adc8` |
| `artifacts/baseline.json` | `592b62bef69b4f76a626fa7c06f17f8813b02bcf4c6753601d4ad2b413e09595` |

The evidence snapshot is `e92eefd5dad99e019fd2f905a2fd9b46053db47f`; the dossier, registry, cohort and baseline bindings match that snapshot as well as the review commit. Context-file hashes and every cited source-entry/raw hash are retained in `review-result.json`. Subsequent packaging or documentation changes do not broaden this review to altered design content.

Only `review.md` and `review-result.json` were written by this reviewer. No commit or push was made.
