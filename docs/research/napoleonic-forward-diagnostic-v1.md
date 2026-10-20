# Napoleonic 1813 forward diagnostic v1

Primary-verified, exploratory analysis after the completed benchmark. No refit or recalibration.

**The saved forecasts overpredict French/allied wins on average, while retaining useful ordering within these 37 compiler records.** Coverage and recorded outcome shares also change. This supports designing one training-only temporal calibration comparison; it does not establish that a calibration repair will generalize or justify a commander model.

## Scope and source authority

The [accepted bounded scope](../../data/napoleonic/forward-diagnostic-v1/scope.json) binds the completed run and frozen inputs. A is France and its allies; outcomes are Bodart’s recorded winners. The forward model was trained through 1812 on 157 eligible entries and scored on 37 eligible 1813 entries. This memo retains all 64 development entries in 1813, including the 27 exclusions. All 52 final entries remain reserved and unused numerically. The 1813 result has now informed this exploratory diagnosis and is not a fresh validation set for a future change.

## Coverage and recorded outcomes

| Period / subset | Entries | Recorded A wins | A-win share |
| --- | ---: | ---: | ---: |
| through_1812 / all | 209 | 144 | 68.90% |
| through_1812 / eligible | 157 | 107 | 68.15% |
| through_1812 / excluded | 52 | 37 | 71.15% |
| 1813 / all | 64 | 18 | 28.12% |
| 1813 / eligible | 37 | 13 | 35.14% |
| 1813 / excluded | 27 | 5 | 18.52% |

Paired coverage falls from 157/209 (75.12%) through 1812 to 37/64 (57.81%) in 1813. The lower recorded A-win share persists in the complete 1813 development frame (18/64); eligibility raises it to 13/37. This is descriptive selection, not a missing-data adjustment. Missing or ambiguous force extracts are not zero forces or zero outcomes.

| 1813 campaign | Eligible / all | Excluded | Recorded A wins, eligible | Mean saved probability | AUC pairs | AUC |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| liberation 1813 | 29 / 52 | 23 | 10 | 0.628286 | 190 | 0.826316 |
| peninsula 1813 | 8 / 12 | 4 | 3 | 0.607911 | 15 | 0.600000 |

The machine-readable [diagnostic](../../artifacts/napoleonic-forward-diagnostic-v1.json) retains side dispositions, all 27 excluded identities with reasons and recorded labels, and all 37 saved forecasts with losses. It preserves the original populations; no missing force is inferred.

## Force balance and discrimination

`x = (A-B)/(A+B)` uses the two frozen printed personnel totals. These are entry-level compiler figures; exact state time and complete combatant/all-ranks coverage remain unestablished.

| Eligible period | Mean x | Median x | Minimum | Maximum |
| --- | ---: | ---: | ---: | ---: |
| through_1812_training | 0.021548 | 0.007937 | -0.853933 | 0.854305 |
| 1813_test | -0.092049 | -0.090909 | -0.688889 | 0.428571 |

| A force relative to B | Through 1812: wins / entries | 1813: wins / entries |
| --- | ---: | ---: |
| smaller | 38 / 77 | 4 / 26 |
| equal | 0 / 1 | 1 / 1 |
| larger | 69 / 79 | 8 / 10 |

The 1813 A side is smaller in 26/37 entries, versus 77/157 earlier. Its win share also falls within the broad smaller-force stratum (38/77 to 4/26). These coarse strata do not hold exact force balance or historical context fixed; they cannot separate a historical mechanism from source, case-mix or coding changes. Each equal-force stratum has only one entry.

On the saved 1813 forecasts, AUC is **0.791667**: 247 concordant and 0 tied pairs among 13 recorded wins × 24 losses = 312 pairs. AUC gives half credit to exact ties. These pairs share entries and are not independent observations. Pooled AUC includes cross-campaign pairs; Peninsula has only eight cases and AUC 0.600000. No confidence or uniform-transfer claim follows.

The training force-balance AUC is 0.779720 (4161 concordant and 21 tied of 5350 pairs). This is an in-sample descriptive association, not another validation result. The saved forward slope is positive, so force balance and its saved probabilities give identical test ordering.

## Calibration and exact Brier accounting

Mean saved probability is **0.623880** versus recorded A-win share **0.351351**: an average overprediction of 27.25 percentage points. The original fixed bins show where that discrepancy occurs; the highest bin is much closer to its observed share. No new bins, recalibrated forecasts or fitted intercept are created.

| Original probability bin | Entries | Mean probability | Recorded A-win share |
| --- | ---: | ---: | ---: |
| 0.0–0.2 | 0 | unknown | unknown |
| 0.2–0.4 | 3 | 0.350040 | 0.000000 |
| 0.4–0.6 | 12 | 0.509591 | 0.250000 |
| 0.6–0.8 | 15 | 0.670521 | 0.266667 |
| 0.8–1.0 | 7 | 0.837221 | 0.857143 |

Bins are left-closed/right-open, including 1 in the final bin. Empty means remain unknown.

Using population variances/covariance (`1/n`), the exact identity is `Brier = (mean(p)-mean(y))² + Var(p) + Var(y) - 2 Cov(p,y)`. Relative to fixed equal odds:

| Arithmetic term | Brier difference |
| --- | ---: |
| Difference in squared mean bias | +0.052175701 |
| Prediction variance minus twice covariance | -0.051118820 |
| Total: force minus equal odds | +0.001056881 |

The terms reconcile force Brier 0.251056881 with equal odds 0.250000000. This is arithmetic accounting, not a causal attribution or a reliability/resolution estimate from fitted bins. Useful ordering and poor average calibration can coexist. It does not prove that an intercept-only repair would work on another period. Original forward log loss remains 0.691121738 versus equal odds 0.693147181; neither score is replaced.

## Same-row sensitivity comparison

The already-executed unqualified-total model has 133 training entries and 30 test entries. The seven removed test entries are retained in the diagnostic. Comparing the same 30 entries separates the arithmetic effect of removing cases from the difference between the two saved models.

| Saved forecasts / test subset | Entries | Log loss | Brier |
| --- | ---: | ---: | ---: |
| primary_all | 37 | 0.691121738 | 0.251056881 |
| primary_common | 30 | 0.713348147 | 0.260451334 |
| primary_removed | 7 | 0.595865700 | 0.210794941 |
| unqualified_saved_common | 30 | 0.716775370 | 0.262276003 |

| Difference: unqualified common minus primary all | Case removal | Same-row saved models | Total |
| --- | ---: | ---: | ---: |
| log_loss | +0.022226409 | +0.003427223 | +0.025653632 |
| brier | +0.009394453 | +0.001824669 | +0.011219122 |

The primary-all score also equals `(30 × primary_common + 7 × primary_removed) / 37`. Most of the worsening here comes from case removal in this arithmetic comparison. The small remaining difference uses two saved models with different training populations; it is not a causal effect of a source annotation. No variant is selected or refitted.

## Five largest errors: inspected source passages

The five largest primary forward log losses cover both 1813 campaigns, so the scope’s campaign augmentation adds no entry. Each complete transcription entry, applicable notes and pinned page image was re-inspected by the primary. All five are recorded A losses. Their totals, side assignments and outcomes match the inspected pages; no mechanical correction was found in this purposive sample. This does not verify the other 32 test entries or adjudicate historical truth.

Text source: `bodart-1908-transcription-v1`, raw SHA-256 `bf12437b6d19226ce127ce5d81e59d20358a5b1999ffe00f5ac6a8f8c20ef986`. The [primary inspection record](../../data/napoleonic/forward-diagnostic-v1/evidence-checks.json) retains locators, English renderings, note applicability, source metadata hashes and the five image hashes.

### B447b: Möckern

A/B printed personnel: 50,000 / 24,000; saved probability 0.843979; log loss 1.857765.

> Sieg der Russen und Preußen (43 Btln., 36 Esk., 4 Kosaken-Regimenter, 130 Gesch. = 19.000 Inft., 5.000 Kav. zus. 24.000 M.) unter Gen. d. Kav. Gf. Wittgenstein über die Franzosen (71 Btln., 31 Esk., 116 Gesch. = 46.000 Inft., 4.000 Kav. zus. 50.000 M.) unter Vizekönig von Italien Pz. Eugen Beauharnais.

Bodart reports a Russian/Prussian victory with 24,000 personnel against 50,000 French personnel. The printed aggregates include 19,000 infantry plus 5,000 cavalry and 46,000 infantry plus 4,000 cavalry respectively; formations and guns are separate.

No applicable strength footnote. The full entry and casualty rows were checked; losses are not force totals.

Locator: Bodart (1908), p447, entry B447b; complete outcome/strength sentence; section `p447`. Image [`bodart-1908-p447-image-v1`](../../data/raw/bodart-1908-v1/p447.jpg), SHA-256 `2a15fc941eb9dc4c965eb5669d54bb410eeb7539a31e7c4e4631f81c9d2e3872`.

### B457a: Vera

A/B printed personnel: 38,000 / 32,000; saved probability 0.734165; log loss 1.324880.

> Sieg der Anglo-Portugiesen und Spanier (32.000 M.) unter Generalissimus FM. Lord Wellington über die Franzosen (38.000 M.) unter Marschall Soult.

Bodart reports an Anglo-Portuguese/Spanish victory with 32,000 personnel against 38,000 French personnel under Soult.

The entry includes untranscribed officer-loss tables. The page-bottom Dennewitz strength note concerns a different entry and is not attached to Vera.

Locator: Bodart (1908), p457, entry B457a; complete outcome/strength sentence; section `p457`. Image [`bodart-1908-p457-image-v1`](../../data/raw/bodart-1908-v1/p457.jpg), SHA-256 `aa9e4b6c8ee0ea4e4fe370bbf772e19237e39ae5a58c39df5487f8b521c7f781`.

### B459d: Wartenburg

A/B printed personnel: 15,000 / 16,000; saved probability 0.672010; log loss 1.114773.

> Sieg der Preußen (27 Btln., 7 Esk., 32 Gesch. = 16.000 M.) unter Gen.-Lt. v. York über die Franzosen (13.500 Inft., 1.500 Kav., 24 Gesch. = 15.000 M.) unter Div.-Gen. Gf. Bertrand.

Bodart reports a Prussian victory with 16,000 personnel against 15,000 French personnel: 13,500 infantry plus 1,500 cavalry. The 32 and 24 guns are separate equipment quantities.

Footnote 1 applies to the Prussian casualty row, not to strength. No applicable strength qualifier was found.

Locator: Bodart (1908), p459, entry B459d; complete outcome/strength sentence; section `p459`. Image [`bodart-1908-p459-image-v1`](../../data/raw/bodart-1908-v1/p459.jpg), SHA-256 `07560d466f1ae5e7dd2000c0be9c417f513ee1ed0d536eb885bc01420d55f740`.

### B455b: Hagelberg

A/B printed personnel: 11,000 / 12,000; saved probability 0.665721; log loss 1.095780.

> Sieg der Preußen (10.400 Inft., 1.600 Kav., 11 Gesch. = 12.000 M.) unter GM. von Hirschfeld über die Franzosen (10 000 Inft., 1.000 Kav., 22 Gesch. = 11.000 M.) unter Div.-Gen. Baron Girard.

Bodart reports a Prussian victory with 12,000 personnel: 10,400 infantry plus 1,600 cavalry, against 11,000 French personnel: 10,000 infantry plus 1,000 cavalry. The 11 and 22 guns are separate.

The French infantry uses spaced thousands (10 000). The Dresden casualty note elsewhere on the page does not qualify this entry.

Locator: Bodart (1908), p455, entry B455b; complete outcome/strength sentence; section `p455`. Image [`bodart-1908-p455-image-v1`](../../data/raw/bodart-1908-v1/p455.jpg), SHA-256 `b2b05971054e44942bf7e42a9d8c6a4addcf5258f66e69a7097910f37584d28b`.

### B448a: Castalla

A/B printed personnel: 15,000 / 17,000; saved probability 0.654924; log loss 1.063991.

> Sieg der Anglo-Spanier (14.000 Inft., 3.000 Kav., 20 Gesch. = 17.000 M.) unter Gen.-Lt. Sir Murray über die Franzosen (12.000 Inft., 3.000 Kav., 12 Gesch. = 15.000 M.) unter Marschall Suchet.

Bodart reports an Anglo-Spanish victory with 17,000 personnel: 14,000 infantry plus 3,000 cavalry, against 15,000 French personnel: 12,000 infantry plus 3,000 cavalry. Guns are separate.

The approximate French loss below the strength passage is a casualty figure, not a strength qualifier. No applicable strength note was found.

Locator: Bodart (1908), p448, entry B448a; complete outcome/strength sentence; section `p448`. Image [`bodart-1908-p448-image-v1`](../../data/raw/bodart-1908-v1/p448.jpg), SHA-256 `3a67444bba7752d9f6944676322b1c2ec371f37151d4c7bd04668104382ee136`.

## Decision and stopping point

**Recommended next action: design one development-only rolling-forward calibration comparison before any further fit.** Specify the eligible year/campaign folds and minimum training support, a single training-only calibration alternative and fixed comparators, paired scores and coverage, and a decision rule before execution. Use earlier development folds to assess whether a correction travels through time; treat this already-inspected 1813 check as exploratory. Bind a separate proposal and obtain exact owner run authorization before any new historical fit. Do not consume the 52 reserved entries to choose the method.

The observed bias supplies a concrete reason to design that test. It does not identify a historical cause, guarantee recalibration success, admit a feature or support commander ratings. One compiler family, selection, strength-dependent winner coding, uncertain populations, rounded figures, missing pairs and only two 1813 groups remain limits. Existing inspected conventions and exact source passages remain in the [original context](../../data/napoleonic/benchmark-v1/context.json). Wider strict-opening extraction and the stopped appointment branch remain parked.

## Reproduction and primary verification

- `python3 -m generalship.napoleonic_forward_diagnostic` verifies bound inputs, all saved-run arithmetic, denominator membership, final separation, pair-count AUC, Brier and paired-score identities, source quotations/image hashes, and both generated diagnostic files. Derived floating-point values allow absolute rounding error up to `2e-12`; types, counts, identities and SHA-256 bindings match exactly. `--write` regenerates only this memo and its JSON. It never invokes a fitter or recalibration.
- `make check` and `make reproduce` include this saved-forecast path. All 37 forecasts and 27 exclusions are retained; no previous run, frozen input, source record or prepared packet changes.
- Original run SHA-256 `35ed5cc7066cf40287e26afc03b16409a9012e81157b472abf212727faa5d505`; the diagnostic JSON binds its own code, scope and actual passage-check record as well as the original inputs. Verification is primary, with no separate review, subagent or second-opinion prompt.
