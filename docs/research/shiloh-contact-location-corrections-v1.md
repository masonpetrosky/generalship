# Shiloh contact packet: literal corrections, v1

Date: 2026-09-20. The separate fresh-context GPT-6 Astra `xhigh`
[review](../../artifacts/review-results/shiloh-contact-518d394-astra-xhigh-v1/review.md)
inspected prepared commit `518d3941fb9227ea9d4f2f6d960fd9b80a45f648` and
identified two low-severity transcription errors. The primary agent independently
confirmed both against enlarged original images and applied exactly these changes:

| Finding | Preserved source | Corrected source | Exact replacement |
|---|---|---|---|
| CL-R1 | `or-prentiss-opening-v1` | `or-prentiss-opening-v2` | `commander thereof` → `commandant thereof` (OR p.277) |
| CL-R2 | `loc-85690890-readings-v1` | `loc-85690890-readings-v2` | `Hornets nest` → `Hornet nest` (Frémaux legend) |

The [correction manifest](../../design/shiloh-contact-location-corrections-v1/source-corrections.json)
binds the actual review outputs, original research record, all 85 existing
source entries and both corrected versions. A `correction_of` object in each new
source identifies the original source, raw hash and complete metadata hash.
This is a content correction, not a `metadata_only` revision. Its exact
replacement and metadata preservation are checked by the bounded audit below;
no new generic source-schema behavior is introduced.

Use the two explicit source substitutions with the
[original packet](shiloh-contact-location-v1.md) when reading the corrected
excerpts. Its original machine record, source bindings, images, catalog snapshots
and reviewer response remain unchanged. The audit replays all **38 anchors**
against the corrected source selection and checks unchanged document dates and
map-image parents. Neither corrected word appears in an assertion's exact quote.
The 14 attributed assertions, two map interpretations and five open research
gates are unchanged. No dossier, quantity, event, boundary or membership changes.

There are now **87 source entries / 84 distinct raw paths**: the preparation's
85/82 plus two corrected text versions. These additions are not extra witnesses.
The prepared TN003 assignment and generated quality/receipt files include them.
The v1/v2 ledgers still show 18 blocked / 22 excluded and 7 blocked / 33 excluded,
with zero complete or promoted rows. Baseline remains 23 engagements / 13 groups,
Brier 0.2768816348133779 versus 0.25 for equal odds.

```sh
python3 design/shiloh-contact-location-v1/reference-audit.py
python3 design/shiloh-contact-location-corrections-v1/reference-audit.py
make check
make reproduce
make packet
```

The [primary assessment](../../artifacts/review-results/shiloh-contact-518d394-astra-xhigh-v1/primary-assessment.md)
closes both literal findings based on the primary image checks and exact-change
verification. The immutable review retains its original `corrections_required`
decision. There was no second reviewer run of the corrected source files; this
is primary verification of the reviewer's exact requested edits, not a claimed
additional independent review. Historical truth, first-contact timing, geographic
area, afloat policy and complete populations remain unresolved.
