# Napoleonic development blocker inventory v1

Mechanical inventory; primary verification covers fields, hashes, counts and selection, not historical entailment.

**Next bounded campaign: `peninsula 1812`.** Selection uses existing citation/image metadata under the fixed 12-entry cap. Inspect its existing pages before adopting a mapping.

Scope: **273 entries / 546 sides / 13 complete development groups**. The 52 reserved entries in 3 groups are counted from the partition; their dossiers were not opened by this inventory.

The development dossiers contain 4,057 claims, 945 explicit unknowns and 129 disputed claims. Brief-v3 records: 224/273; earlier drafts retain their original brief.

Dossier boundary states: tactical `{'null': 273}`; campaign `{'null': 273}`. Typed quantity field states: `{'absent': 273}`.

The indexed measurement packages cover 8/546 sides (the stopped Naples pilot); 538 sides have no mapping in those packages. Recorded non-null selections among the indexed sides: `{'selected_boundary': 0, 'selected_strength': 0, 'selected_person_id': 0, 'army_id': 0}`. These are record-presence counts, not admission decisions.

## Complete campaign comparison

Pages = distinct registered non-Bodart image IDs directly linked from strength/responsibility citations. Shared = pages cited by more than one entry. Missing links are citation references without this direct metadata link, not a count of unavailable or uninspected pages. Unknown/disputed = claims, not missing sides. No outcome values enter selection.

| Campaign | Entries | Unknown / disputed claims | Both dimensions cite non-frame sources | Pages / shared | Missing direct links | Selection |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `fifth-coalition 1809` | 36 | 162 / 16 | 31/36 | 83 / 2 | 0 | above_12_entry_batch_bound, non_frame_dimension_citations_missing |
| `fourth-coalition 1806` | 23 | 9 / 5 | 23/23 | 360 / 38 | 380 | above_12_entry_batch_bound, non_frame_image_links_missing |
| `fourth-coalition 1807` | 19 | 53 / 7 | 19/19 | 79 / 3 | 0 | above_12_entry_batch_bound |
| `liberation 1813` | 52 | 302 / 7 | 39/52 | 88 / 15 | 0 | above_12_entry_batch_bound, non_frame_dimension_citations_missing |
| `peninsula 1808` | 17 | 68 / 0 | 16/17 | 60 / 0 | 0 | above_12_entry_batch_bound, non_frame_dimension_citations_missing |
| `peninsula 1809` | 19 | 79 / 3 | 19/19 | 62 / 0 | 0 | above_12_entry_batch_bound |
| `peninsula 1810` | 11 | 27 / 13 | 11/11 | 32 / 1 | 0 | eligible |
| `peninsula 1811` | 19 | 63 / 31 | 19/19 | 53 / 9 | 0 | above_12_entry_batch_bound |
| `peninsula 1812` | 8 | 24 / 12 | 8/8 | 24 / 0 | 0 | selected |
| `peninsula 1813` | 12 | 13 / 2 | 12/12 | 56 / 0 | 0 | eligible |
| `russia-1812 1812` | 31 | 139 / 29 | 26/31 | 77 / 5 | 0 | above_12_entry_batch_bound, non_frame_dimension_citations_missing |
| `third-coalition 1805` | 22 | 4 / 4 | 22/22 | 161 / 13 | 540 | above_12_entry_batch_bound, non_frame_image_links_missing |
| `third-coalition 1806` | 4 | 2 / 0 | 4/4 | 54 / 0 | 57 | stopped_pilot, non_frame_image_links_missing |

## Next inspection scope

Keep all **8 entries / 16 sides**, using **24 non-Bodart pages** already cited in the two dimensions, plus the existing Bodart references. IDs: `B430a`, `B430b`, `B430c`, `B431a`, `B431b`, `B432a`, `B432b`, `B441a`.

Family navigation counts (entries): `{'belmas-sieges-peninsule': 4, 'marmont-memoires': 1, 'oman-peninsular-war': 5, 'suchet-memoires-espagne': 2, 'toreno-levantamiento-guerra': 3}`. Identical image hashes under multiple IDs: `[]`.

Prepare one combined, source-specific population/time/authority table from these existing passages and full pinned pages. Test whether a common opening boundary can support a complete force/person pair for either side. Keep each unresolved side explicit and stop after this complete campaign; no automatic deep-dive queue.

| Entry | Strength / responsibility claim IDs to inspect |
| --- | --- |
| `B430a` Ciudad-Rodrigo | strength: `bodart-strength`, `mediated-french-investment-return`, `allied-local-headcount-unknown`; responsibility: `bodart-command`, `barrie-governor`, `wellington-siege-plan` |
| `B430b` Altafulla | strength: `bodart-strength`, `mathieu-relief-force`, `spanish-own-headcount-unknown`; responsibility: `bodart-command`, `mathieu-lamarque-task`, `eroles-local-command`, `belmas-lacy-attribution`, `lacy-superior-instruction`, `spanish-rally-point` |
| `B430c` Peniscola | strength: `bodart-strength`, `spanish-garrison`, `french-own-local-count-unknown`; responsibility: `bodart-command`, `severoli-local-investment`, `garcia-navarro-governor` |
| `B431a` Badajoz | strength: `bodart-strength`, `belmas-garrison`, `mediated-march15-garrison-table`, `beresford-investing-corps`, `belmas-allied-army`; responsibility: `bodart-command`, `beresford-local-role`, `philippon-governor` |
| `B431b` Salamanca | strength: `bodart-strength`, `belmas-fort-garrison`, `oman-fort-garrison-alternative`, `allied-siege-headcount-unknown`; responsibility: `bodart-command`, `duchemin-local-command`, `clinton-local-wellington-superior` |
| `B432a` Castalla | strength: `bodart-strength`, `spanish-four-part-force`, `suchet-spanish-advance`, `french-local-count-unknown`; responsibility: `bodart-command`, `odonnell-plan`, `harispe-delort-local-scope`, `delort-counterattack` |
| `B432b` Salamanca | strength: `bodart-strength`, `oman-allied-battle-table`, `oman-inferred-french-strength`, `french-own-matched-return-unknown`; responsibility: `bodart-command`, `marmont-bonnet-disposition`, `marmont-bonnet-clausel-succession`, `wellington-pakenham-task` |
| `B441a` Burgos | strength: `bodart-strength`, `french-castle-garrison`, `allied-available-army`, `local-siege-headcount-unknown`; responsibility: `bodart-command`, `dubreton-local-command`, `wellington-siege-direction` |

## Provenance and limits

5,874 strength/responsibility citation references retain dossier/claim IDs, citation indices, sections, locators, quote hashes and source/metadata/image hashes in the companion JSON. 2,609 registered source IDs covering 2,609 distinct raw paths were hash-checked. The scope binds every development dossier, source registry and pilot package; see `data/napoleonic/blocker-inventory-v1/scope.json`.

- Presence and byte/quote checks only; no new historical entailment inspection.
- Absent structured records do not mean absent historical evidence.
- Fewer pages can mean thinner coverage; selected campaign is not representative.
- No side inferred from claim text; source families do not prove independence.
- Final dossiers excluded from this inventory; the reservation is not historical blinding.

No new historical claim, source fetch, feature admission, calibration score, separate review, synthetic job or historical fit. Model rows emitted: 0.
