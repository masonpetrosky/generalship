# Best-estimate side strength: focused follow-up review

Review prepared commit `0e5800b3a931305bf3762434b2280b61d3322ef0` against `cff43ea92a82493987df3a37657ae296e6b5f0c9`. Sibling inputs.json binds
23 paths at the prepared commit. You are a separate Claude Opus 5.5 `high` reviewer
with fresh context. The primary's conversation is not an input. Verify input hashes against
`git show 0e5800b3a931305bf3762434b2280b61d3322ef0:<path>` first.

Scope: a focused follow-up of the first design review,
`artifacts/review-results/strength-estimates-design-fff4103-opus-high-v1/review.md`
(R1–R10, A1–A7), against the corrected `docs/strength-estimates.md`, the roadmap/README text
and that directory's `correction.json` and `primary-assessment.md`. Read the evidence
contract, `docs/feature-admission.md`, `docs/feature-admission-reported-strength.md`, the
scoping memo and `generalship/baseline.py` as needed.

For each of R1–R10 say whether it is fully applied, partially applied or not applied. Check
the adopted advisories. Then look for **new** problems the corrections introduced:
internal inconsistencies among §§1–7 (classes, grades, labels, bases, rules, checker),
undefined or contradictory cases in the rules, and anything still decided after extraction.
Work through at least these cases against the §3 table and §4 rules and report the outcome
each produces: (i) a side whose only inputs are an opponent estimate and a one-sided own
bound; (ii) two class-A candidates on different bases; (iii) a class-B unknown-basis figure
with a class-A figure on another basis; (iv) identical CWSAC and Livermore values (rule 2);
(v) a grade-C post-start figure as the sole input. Do not reopen accepted choices unless a
correction created a defect.

Design review only: no estimate, dossier, source or model input is proposed. No network,
new research or agents. Run `make check` offline; no build or packet commands. Write only
`artifacts/review-results/strength-estimates-followup-0e5800b-opus-high-v1/review.md`; do not edit other files, commit or push. Give required corrections as exact
replacement text, or say there are none; list advisories separately. Return the path and
outcome. An AI design review is not approval of any estimate.
