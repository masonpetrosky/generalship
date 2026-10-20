# Napoleonic compiler-strength benchmark v1

Status: preparation only; primary verification is recorded in the research log.
The owner accepted a descriptive benchmark dataset and exact run proposal on
2026-10-20. No historical outcome fit is authorized by that acceptance.

## Target and scope

The question for a future run is how Bodart's printed personnel totals relate to
his recorded winners within the frozen development frame. This is a diagnostic of
one compiler's selected engagement records. It does not reconstruct first hostile
contact, a commander's information, army continuity, tactical effects or campaign
contribution. The strict opening profile and stopped historical pilots are unchanged.

Use all 273 development entries in the 13 complete groups fixed by methods v1,
with one record per engagement and exactly two side records (546 sides). Side A
is France and its allies; B is the opponent. The 52 reserved-final entries are
excluded from the new table, eligibility decisions and numerical evaluation.
Binding the unchanged frame/transcription, which also contain those entries,
does not make the historically familiar final events blind.

Only the frozen `winner_strength_printed` and `loser_strength_printed` fields
are numerically encoded. The source's left/right convention maps them to A/B;
it is not a fitted feature. Each field is checked in its actual entry context.
The retained source-column convention and quotations reveal outcomes even without
a separate target column. This is outcome-unused preparation, not blinding. The
runner reads only the two whitelisted primary personnel values as features.
Missing extracts mean **not extracted by frame v1**, not proof that Bodart gives
no figure. Do not repair the frame, fill an extract from a later passage, infer
people from battalions or guns, or borrow a dossier's preferred figure.

## Quantities, ambiguity and eligibility

Retain the entire printed field, exact passage/section, source and page-image
hashes, frozen interval, units, components, qualifiers, footnotes and limitations.
Amounts and numerical tokens retain their literal spellings. Approximation is a
source qualifier, not an invented error interval. Dotted/spaced thousands require
groups of three digits; malformed `10.0000` stays unresolved. Equipment, formation
counts and officer subsets are distinct from a whole-side personnel total.
The printed field retains every component; typed quantities cover recognized
unit tokens and are not exhaustive atomic extraction.

The primary profile accepts exactly one positive, unambiguously printed personnel
total at an unspecified whole-entry state: an initial `N M.` total, a printed
`= N M.` / `zus. N M.` total, or a personnel cell explicitly labelled
`Gesamt-Stärke`. The last explicit aggregate may subsume earlier components; it
never licenses adding them again. Published sums are kept as published; the
component list is not proof of complete combatant coverage. Plain `M.` does not
establish whether officers, train or artillery crews are included.

For Gesamt-Stärke cells, use their printed column and gun labels, never the
magnitude of a number. Bodart's left column can place guns before people; the
right column can place guns after people. Retain both quantities and the whole
row. A gun label with two possible parses remains ambiguous.

Infantry/cavalry-only counts, organizational units, non-strength extracts,
malformed notation, explicitly dated phases, surviving/remnant figures and
multiple unaggregated totals are retained but excluded from the primary profile.
No maximum, minimum, average, preferred-source vote or imputation chooses a value.
An eligible pair requires eligible totals on both sides. Every excluded entry
and every reason remains in the 273-entry denominator; reasons can overlap.
This profile admits a compiler-description dataset only, not an enriched predictor
to the frozen baseline or a source-backed opening-force selection.

## Fixed future evaluation

The executable proposal binds the dataset, scope, protocol, source snapshot,
design and exact executing Python files. There is one fixed force-only logistic
model, with `x = (A - B) / (A + B)` and ridge penalty 1 on intercept and slope,
using the existing standard-library optimizer. Comparators are equal odds and a
training-only Laplace-smoothed A-win prior. There is no commander term, tuning,
feature selection or historical ranking.

Main evaluation leaves one complete frozen development campaign group out.
Dependence views leave an entire development war out and train through 1812 to
predict the fixed 1813 development entries. They answer different prediction
questions and retain their own exact test/train denominators. Empty test groups
are reported; a fold with fewer than two training rows is not estimable.

Publish the primary population and these fixed sensitivities in every evaluation:

1. Exclude all entries explicitly printed indecisive.
2. Exclude all four printed non-combat capitulations.
3. Exclude pairs with an approximate selected total or a numeric footnote marker
   anywhere in the cited strength passage (including just outside a parenthesis).
   This is conservative entry-context annotation screening; it does not adjudicate
   that every note applies to each individual total. Field and context markers
   remain separate in the dataset, and each referenced note is retained.

Every sensitivity refits its own training population and scores all three models
on the same rows. Publish log loss, Brier score and calibration bins under battle
and equal-held-out-group weighting, individual group results, folds, predictions,
and concentration of the force-versus-prior log-loss difference by engagement.
Bootstrap paired loss differences by held-out group (10,000 resamples, seed
20261020, percentile 95% interval), with both weightings recomputed in each draw.
These intervals resample held-out loss contributions; they do not propagate source
uncertainty or refit the training sets.
Only the campaign-held-out view gets this bootstrap; coarse war/forward views
retain their small replication count without a confidence claim. Report negative
or unimproved results. There is no pass/fail skill rule or selection of the best
sensitivity after looking at scores.

Bodart selects on losses/consequence and sometimes assigns an indecisive winner
using relative strength. Excluding explicitly indecisive entries does not prove
that other labels are independent of strength, and does not remove selection or
shared-source error. A predictive gain would describe these records only.

## Run gate and stopping rule

Preparation, checks and `make reproduce` never load historical outcomes into a fit
or invoke the runner. Tests fit only constructed cases. The runner rejects missing,
false or mismatched owner authorization before reading outcome labels or calling
the optimizer. No owner run authorization is created here. A future authorization
must bind the exact proposal hash and state the approved command and scope.

The prepared proposal is the end of this task. Preserve every prior source,
dossier, packet, pilot, admission contract, model input and numerical result.
No final-set extraction, historical model fit, new source search, calibration
scoring, subagent or separate review is part of preparation.
