# Shiloh precontact packet: separate review and literal correction, v1

Date: 2026-09-20. The [fresh-context Astra `xhigh` review](../../artifacts/review-results/shiloh-precontact-327d222-astra-xhigh-v1/review.md)
inspected prepared commit `327d222195b5526423390c25f59b8330a21e88c0`: all
**10 assertions / 24 anchors / 26 selected historical sections in nine new texts /
19 page images**. It requested one literal-transcription finding, **PS-R1**, with
two wording corrections. No other required finding was returned.

The working recommendation remains: treat April 3–4 as precursor encounters on
the reported return/reset evidence, with **weaker event-specific closure for
April 3**. The April 5 Howell link remains unresolved. This is conditional research
guidance, not a completed boundary, historical adjudication or feature admission.
See the [unchanged prepared memo](shiloh-precontact-segmentation-v1.md) for the
rule, source distinctions, limits and next research action.

The primary independently inspected an enlarged selection from the registered
OR I.X.2 p.391 image. Jordan's first paragraph in the lower April 4 letter reads:

| Preserved v1 text | Corrected v2 text |
|---|---|
| `in support of the movement` | `to the support of the movement` |
| `by Generals Hardee and Bragg.` | `by Major-Generals Hardee and Bragg.` |

`or-april4-march-orders-v2` contains exactly those two replacements. Its
`correction_of` binds the v1 source ID, raw SHA-256 and complete metadata SHA-256.
Dates, dependence group, other wording and interpretation are unchanged. The
[correction manifest](../../design/shiloh-precontact-segmentation-corrections-v1/source-corrections.json)
binds the actual reviewer response and page image, all **111 prior source entries**,
and the original research record. The v1 source and prepared record remain immutable.

When replaying the prepared packet, substitute the v2 source for the four cited
sections of the v1 order source and apply the exact quote overlay to **one PS05
anchor**. The other 23 anchor quotations remain unchanged. All **24 anchors**
resolve with unchanged document dates. This is an explicit content correction,
not a `metadata_only` migration or a silent change to the frozen packet.

The registry now contains **112 entries / 109 raw paths**. The additional version
is not another witness. The draft dossier remains 62 claims / 40 quantities /
26 events; no dossier or admission proposal changed. Admission v1 is still
18 blocked / 22 excluded, v2 7 blocked / 33 excluded, with zero complete,
emitted or promoted rows. The baseline remains 23 engagements / 13 groups,
Brier 0.2768816348133779 versus 0.25 for equal odds; no model improvement.

```sh
python3 design/shiloh-precontact-segmentation-v1/reference-audit.py
python3 design/shiloh-precontact-segmentation-corrections-v1/reference-audit.py
make check
make reproduce
make packet
```

The [primary assessment](../../artifacts/review-results/shiloh-precontact-327d222-astra-xhigh-v1/primary-assessment.md)
closes PS-R1 through image inspection and exact-change verification. The actual
review keeps its original `changes_requested` decision. No second separate review
of the corrected file is claimed. The reviewer first found the missing rank word;
the primary flagged the support phrase, and the reviewer then independently
rechecked both against the image. That discovery sequence is retained.
