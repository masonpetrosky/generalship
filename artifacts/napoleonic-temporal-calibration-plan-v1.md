# Prepared temporal calibration test v1

Primary-verified preparation only. No historical label was loaded into a fit, no historical forecast was generated and no run authorization was created.

## Fixed question and method

Test one ridge-1 additive logit offset, estimated from the latest fully completed campaign completion-year block. Its base force model uses earlier completed groups and stays fixed after correction. Compare it with the same uncorrected base, a force model fitted on all available groups, expanding/recent Laplace priors and equal odds. All six models score identical test entries within each population.

Group completion is the maximum known end date of every development member, including ineligible members. A missing end blocks the entire group. Groups finishing on or after January 1 are unavailable for that year. This is a retrospective temporal safeguard, not proof of source publication or a historical information set.

The base groups must also finish strictly before the earliest known start of every calibration member. An unknown calibration start or overlap makes the entire paired fold not estimable, with no alternate block. Every scorable prepared fold satisfies this guard.

## Frozen group availability

Locators refer to the unchanged prepared dataset’s `battle_id.end_date` fields. These are metadata checks, not fresh source adjudication or a change to the frozen groups.

| Frozen group | Entries | Last recorded end | Controlling entry locator(s) |
| --- | ---: | --- | --- |
| fifth-coalition 1809 | 36 | 1809-08-16 | B412b.end_date |
| fourth-coalition 1806 | 23 | 1807-01-06 | B378b.end_date |
| fourth-coalition 1807 | 19 | 1807-08-20 | B386a.end_date |
| liberation 1813 | 52 | 1814-05-14 | B484a.end_date |
| peninsula 1808 | 17 | 1809-02-20 | B393c.end_date |
| peninsula 1809 | 19 | 1809-12-10 | B415c.end_date |
| peninsula 1810 | 11 | 1812-08-25 | B437b.end_date |
| peninsula 1811 | 19 | 1812-01-09 | B429b.end_date |
| peninsula 1812 | 8 | 1812-10-21 | B441a.end_date |
| peninsula 1813 | 12 | 1813-12-13 | B467b.end_date |
| russia-1812 1812 | 31 | 1812-12-18 | B446a.end_date |
| third-coalition 1805 | 22 | 1805-12-05 | B370a.end_date |
| third-coalition 1806 | 4 | 1807-02-06 | B379c.end_date |

Date provenance: `bodart-1908-transcription-v1`, raw SHA-256 `bf12437b6d19226ce127ce5d81e59d20358a5b1999ffe00f5ac6a8f8c20ef986`; frame SHA-256 `af6016fc4d8505de0e5ebba4d3cd106178a07dd542c4c6ab7ed34770f1af75ea`. This task checks the frozen metadata and its temporal use; it performs no new page inspection or date correction.

## Every population and annual fold

Counts below are eligibility and planned-fit counts, never predictive results. Each scorable fold uses one base force fit, one offset fit and one expanding force fit. Fixed minimum support is ten base and ten calibration rows; this is a pragmatic floor, not evidence of adequate statistical precision. There is no fallback to another window.

### primary

194/273 eligible; 79 excluded. All identities, role assignments and exclusions remain in the JSON.

| Test cohort year | Region | Calibration completion year | Base | Calibration | Available expanding | Deferred earlier eligible | Test eligible / all | Status |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1805 | warmup | unknown | 0 | 0 | 0 | 0 | 14 / 22 | not_estimable |
| 1806 | warmup | 1805 | 0 | 14 | 14 | 0 | 15 / 27 | not_estimable |
| 1807 | warmup | 1805 | 0 | 14 | 14 | 15 | 13 / 19 | not_estimable |
| 1808 | decision | 1807 | 14 | 28 | 42 | 0 | 14 / 17 | planned |
| 1809 | decision | 1807 | 14 | 28 | 42 | 14 | 47 / 55 | planned |
| 1810 | decision | 1809 | 42 | 61 | 103 | 0 | 11 / 11 | planned |
| 1811 | decision | 1809 | 42 | 61 | 103 | 11 | 13 / 19 | planned |
| 1812 | decision | 1809 | 42 | 61 | 103 | 24 | 30 / 39 | planned |
| 1813 | reused_1813_secondary | 1812 | 103 | 54 | 157 | 0 | 37 / 64 | planned |

### exclude_indecisive

194/273 eligible; 79 excluded. All identities, role assignments and exclusions remain in the JSON.

| Test cohort year | Region | Calibration completion year | Base | Calibration | Available expanding | Deferred earlier eligible | Test eligible / all | Status |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1805 | warmup | unknown | 0 | 0 | 0 | 0 | 14 / 22 | not_estimable |
| 1806 | warmup | 1805 | 0 | 14 | 14 | 0 | 15 / 27 | not_estimable |
| 1807 | warmup | 1805 | 0 | 14 | 14 | 15 | 13 / 19 | not_estimable |
| 1808 | decision | 1807 | 14 | 28 | 42 | 0 | 14 / 17 | planned |
| 1809 | decision | 1807 | 14 | 28 | 42 | 14 | 47 / 55 | planned |
| 1810 | decision | 1809 | 42 | 61 | 103 | 0 | 11 / 11 | planned |
| 1811 | decision | 1809 | 42 | 61 | 103 | 11 | 13 / 19 | planned |
| 1812 | decision | 1809 | 42 | 61 | 103 | 24 | 30 / 39 | planned |
| 1813 | reused_1813_secondary | 1812 | 103 | 54 | 157 | 0 | 37 / 64 | planned |

### exclude_no_combat

193/273 eligible; 80 excluded. All identities, role assignments and exclusions remain in the JSON.

| Test cohort year | Region | Calibration completion year | Base | Calibration | Available expanding | Deferred earlier eligible | Test eligible / all | Status |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1805 | warmup | unknown | 0 | 0 | 0 | 0 | 14 / 22 | not_estimable |
| 1806 | warmup | 1805 | 0 | 14 | 14 | 0 | 14 / 27 | not_estimable |
| 1807 | warmup | 1805 | 0 | 14 | 14 | 14 | 13 / 19 | not_estimable |
| 1808 | decision | 1807 | 14 | 27 | 41 | 0 | 14 / 17 | planned |
| 1809 | decision | 1807 | 14 | 27 | 41 | 14 | 47 / 55 | planned |
| 1810 | decision | 1809 | 41 | 61 | 102 | 0 | 11 / 11 | planned |
| 1811 | decision | 1809 | 41 | 61 | 102 | 11 | 13 / 19 | planned |
| 1812 | decision | 1809 | 41 | 61 | 102 | 24 | 30 / 39 | planned |
| 1813 | reused_1813_secondary | 1812 | 102 | 54 | 156 | 0 | 37 / 64 | planned |

### unqualified_totals

163/273 eligible; 110 excluded. All identities, role assignments and exclusions remain in the JSON.

| Test cohort year | Region | Calibration completion year | Base | Calibration | Available expanding | Deferred earlier eligible | Test eligible / all | Status |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1805 | warmup | unknown | 0 | 0 | 0 | 0 | 10 / 22 | not_estimable |
| 1806 | warmup | 1805 | 0 | 10 | 10 | 0 | 13 / 27 | not_estimable |
| 1807 | warmup | 1805 | 0 | 10 | 10 | 13 | 7 / 19 | not_estimable |
| 1808 | decision | 1807 | 10 | 20 | 30 | 0 | 14 / 17 | planned |
| 1809 | decision | 1807 | 10 | 20 | 30 | 14 | 40 / 55 | planned |
| 1810 | decision | 1809 | 30 | 54 | 84 | 0 | 11 / 11 | planned |
| 1811 | decision | 1809 | 30 | 54 | 84 | 11 | 13 / 19 | planned |
| 1812 | decision | 1809 | 30 | 54 | 84 | 24 | 25 / 39 | planned |
| 1813 | reused_1813_secondary | 1812 | 84 | 49 | 133 | 0 | 30 / 64 | planned |

## Decision population and limits

The primary decision region is 1808–1812: **115/141 entries, five annual folds and seven complete source groups**. All 26 excluded entries remain visible. The 1805–1807 warmup retains 68 entries (42 eligible), with no outer score. The reused 1813 region retains 37/64 test entries and 27 exclusions as secondary diagnostics only; its score cannot change the continuation decision.

All development outcomes were exposed by prior work. This is an exploratory follow-up fixed before its own execution, not a fresh confirmation. The same calibration block repeats in 1808–1809 and 1810–1812 when later complete groups are unavailable; it is not necessarily the immediately preceding start-year cohort. Earlier test outcomes can become later training data after their whole group completes. Overlapping training and operations remain dependencies.

Two eligible development entries starting in 1813 finish in 1814; their IDs remain development under the existing reservation. No final ID is reclassified. Whole-entry personnel figures still have uncertain population/time and are not contemporary opening-force forecasts.

## Fixed continuation rule

On the primary 1808–1812 region, the candidate must lower log loss and not worsen Brier against every comparator under both battle and equal-campaign weighting. It must also lower log loss against expanding force in at least three of five years. The unqualified-total sensitivity vetoes continuation if either score worsens against expanding force under either weighting. A missing required score yields not assessable. Numerical tolerance is `1e-12`.

This is a pragmatic exploratory continuation rule, not a significance test, feature-admission contract or the methods-v1 commander-rating gate. No bootstrap confidence claim is proposed for five annual folds/seven source groups. Publish every score, paired difference, yearly/group result, fixed calibration bin and case contribution, including failures. No alternative window, offset penalty or best sensitivity is selected after results.

## Bound execution proposal and stop

The exact proposal binds the code, design, inputs and this plan: [proposal](../data/napoleonic/temporal-calibration-v1/run-proposal.json); [full design](../docs/napoleonic-temporal-calibration-v1.md); [plan JSON](napoleonic-temporal-calibration-plan-v1.json). A future authorized run proposes **72 parameter fits across 24 scorable population/year folds** (two force fits and one one-parameter offset per fold). This preparation performs zero.

`python3 -m generalship.napoleonic_temporal_calibration` verifies the prepared plan and proposal. `--write` restores only the two plan files; frozen input/code changes cannot silently rebind the proposal. `make check` and `make reproduce` never invoke the historical runner.

Preparation stops here. A separate exact owner run authorization is required before any historical fit. All 52 final entries remain unused numerically. Original sources, dossiers, measurements, model inputs, runs and diagnostics retain their bytes. Wider opening extraction, the appointment branch and the unscored extraction-review sample remain parked. No separate reviewer, subagent or second-opinion prompt ran.
