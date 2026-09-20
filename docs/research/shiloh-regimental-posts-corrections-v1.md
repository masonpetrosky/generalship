# Shiloh regimental/post comparison: review and literal corrections

September 20, 2026. The [actual fresh-context Astra `xhigh` review](../../artifacts/review-results/shiloh-posts-dc669f4-astra-xhigh-v1/review.md)
covered prepared commit `dc669f4ddb8388eea9c9029738f4f6b6e65c069c`: all **7 assertions,
21 anchors / 19 distinct source-section pairs, 17 new historical sections and
16 retained page images**. It returned two required literal findings and no
additional comments. Historical interpretations remain supported within their
explicit unresolved limits; this is separate AI analysis, not historical adjudication.

The primary independently inspected the retained p.503 image and enlarged title
and caption details from the hash-matched parent PDF, page 533. Both findings
are accepted and corrected in `buell-battles-leaders-map-posts-v2`:

| Finding | Preserved v1 reading | Corrected v2 reading | Occurrences |
|---|---|---|---:|
| SHILOH-RP-R1, `p503-camps` | `All changes referred to` | `All camps referred to` | 1 |
| SHILOH-RP-R2, `p503-title` | `U. S. Vols.` | `U. S. Vol.` | 2 |

The map maker's final provenance sentence concerns camps. Restoring that noun
matters to literal fidelity, although the packet's bounded interpretation already
treated this as a camp/map provenance claim. The abbreviation fixes add no new
historical information. All other text, section dates, dependencies and image
references are identical. The source's `correction_of` binds the v1 raw and complete
metadata hashes. Neither the frozen v1 file nor its research record is overwritten.

The [correction manifest](../../design/shiloh-regimental-posts-corrections-v1/source-corrections.json)
binds the actual review, preserved packet, all **151 pre-correction registry
entries**, direct image and new source. Replaying the packet substitutes v2 for
the seven map sections, with explicit quote corrections to **two RP06 anchors**.
All **21 anchors** resolve and retain their document dates. The other 19 anchor
quotations are unchanged. This is one corrected source version, not another witness.
The registry now has **152 entries / 149 raw paths**.

The [primary assessment](../../artifacts/review-results/shiloh-posts-dc669f4-astra-xhigh-v1/primary-assessment.md)
closes both findings through image inspection and exact-change verification.
The review retains its original `requires_literal_corrections` verdict; no second
separate review of the corrected file is claimed. Both discrepancies were found
by the separate reviewer and then independently confirmed by the primary.

The [prepared comparison](shiloh-regimental-posts-v1.md) remains the historical
research record: Reid gives an overnight lead on an unnamed 46th Ohio picket
line; the inspected 72d accounts do not fill Saturday's gap; Worthington's post
relationships remain disputed and approximate; the map depicts April 6–7.
No established post match, continuous firing chain, exact first contact, mapped
area or complete populations follows. Next trace the contributor or original
evidence behind Reid II p.286's overnight narrative.

TN003 remains draft at **62 claims / 40 quantities / 26 events**. The frame remains
127 engagements / 36 campaigns, with three draft dossiers. Admission v1 remains
18 blocked / 22 excluded and v2 7 blocked / 33 excluded, with zero complete,
emitted or promoted rows. The baseline remains 23 engagements / 13 groups,
Brier **0.2768816348133779** versus **0.25** for equal odds: no improvement.

Validation: `make check` (82 tests), `make reproduce`, `make packet`, the original
packet audit and correction replay. Parent re-render verification reproduced all
13 new facsimiles exactly; earlier 133 source entries, 130 raw paths and 109 bound
files were compared with the base commit. These checks establish preservation
and mechanical consistency, not the historical truth of the accounts.
