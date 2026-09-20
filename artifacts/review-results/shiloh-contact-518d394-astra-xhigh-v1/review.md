# Separate AI review: Shiloh contact and location packet v1

**Decision: corrections required for two literal transcriptions.** Both findings
are low severity and leave the 14 attributed assertions, all quoted passage
anchors, reported numbers and clocks, map-phase interpretation, unresolved
boundary, and no-admission decision unchanged. No substantive historical or
implementation correction was identified within the inspected scope.

This is the actual separate analysis of reviewer task
`/root/shiloh_contact_review`, using `gpt-6-astra` with `xhigh` reasoning and
fresh context, on 2026-09-20. It is an AI source review, not human historical
adjudication, independent historical testimony, or permission to admit a feature.

## Frozen inputs

Reviewed commit: `518d3941fb9227ea9d4f2f6d960fd9b80a45f648`.
Parent: `1312a22808e65ee0866a85f2e82aab4c63397f01`.
The four supplied hashes were verified before review:

| Input | SHA-256 |
|---|---|
| `data/sources.json` | `5e5051afb0c548fbb3fe8f604fcc89f23c6b80e8be7c804c256ff64d5c94d233` |
| `data/evidence/TN003.json` | `fb622c81b48110d1d7b25212b5c3f10881c4a7724a9ccbb93ef793816cf100ee` |
| `design/shiloh-contact-location-v1/research-record.json` | `225d791de6ccac0ac5835868d890e6ea76b75a560f1697c60aa5ce282b31a1ad` |
| `docs/research/shiloh-contact-location-v1.md` | `e9701fbf84b0f698c9cf03671f87a2002f6119ec0473ba8762ef5c2cf120ccdf` |

The machine-readable companion binds the other inspected implementation files,
the 32 new source records and all 19 cited source/section pairs. The source
registry, assertion references, dates, and hashes were checked rather than
taken on trust from the author’s inspection counts.

## Required corrections

### CL-R1 — Restore “commandant” in the Prentiss transcription

- Severity: low / P3. Required for unqualified acceptance of the new manual
  transcription; no substantive assertion or boundary change.
- Location: `data/raw/shiloh/contact-location-v1/or-prentiss-opening-v1.txt`,
  line 11, section `p277-saturday`.
- Current text: `information received from the commander thereof`.
- Exact correction: `information received from the commandant thereof`.
- Evidence: the lower Prentiss paragraph of
  `or10-1-contact-p277-facsimile-v1`, printed p.277 / PDF p.301. The printed
  line break splits `com-` / `mandant`; joining that wrap yields `commandant`.
  The whole-page OCR also retains `commandant`, but the page image is the
  controlling evidence for this finding.
- Image SHA-256:
  `9339a7377ed2e05cc318d2080d507fea637090da2a62769cd547d3fe86964d69`.
  Transcript SHA-256:
  `a5402045eba1c4741f2576272cf28be60265016d51f200fdd044c9a16c9d6662`.

The declared transformation permits whitespace and line-wrap normalization,
not substitution of a different word. This word is outside CL03's exact
company-count anchor and does not change CL03 or CL04. Preserve the v1 bytes
and record the correction through a new versioned source and an explicit,
hash-bound correction record.

### CL-R2 — Remove the added “s” from the Frémaux legend label

- Severity: low / P3. Required for unqualified acceptance of the selected
  label transcription; no map-position or phase change.
- Location: `data/raw/shiloh/contact-location-v1/loc-85690890-readings-v1.txt`,
  line 11, section `title-legend`.
- Current text: `Hornets nest`.
- Exact correction: `Hornet nest`.
- Evidence: the star-symbol legend entry on `loc-85690890-map-v1`, inspected
  at original-image pixels `[2060, 450, 2440, 800]`, top-left origin.
  The handwritten label reads `Hornet nest`; no terminal `s` is present.
- Image SHA-256:
  `0434116f5a4d11a8765293596c265fce2ff8f0d1fb734db5e9c919a9fd329d76`.
  Transcript SHA-256:
  `44b15a6b4f24effa5cdb01749b3e0f08a2471bc2bd6d4736140399500da855fc`.

The declared normalization of case, spacing, superscripts and punctuation does
not justify adding a letter. Do not replace the observed spelling with a
familiar modern place-name spelling. Preserve the image, catalog and v1
readings; create a corrected source version and a bound correction record.

These are the only required corrections. They block unqualified transcription
acceptance of the two affected v1 readings, not retention of this packet as
source-attributed research. Neither finding authorizes any change to the
frozen dossier, admission proposals or model inputs. The primary agent must
assess the findings and bind any later correction separately.

## Coverage actually inspected

| Scope | Inspected coverage |
|---|---|
| Attributed assertions | 14/14, CL01–CL14 |
| Exact passage anchors | 38/38 checked against retained section text and claim context |
| Cited source/section pairs | 19/19 |
| Anchors compared to new page images | 34/38, representing 18/19 source/section pairs |
| Text-only remainder | Four Beauregard anchors in the existing `p386` section; no new scan inspection |
| Participant-report context | Nine reports across all 16 retained OR OCR pages |
| Supplied book-page images | 16/16: twelve OR and four Reed pages |
| Maps | 2/2 full-image overviews, with enlarged selected regions |
| Catalog snapshots and map readings | 2/2 catalog JSON snapshots and 2/2 selected-reading files |
| New source bindings | 32/32 records and raw-file hashes |
| Preservation | All 53 earlier registry entries and their raw bytes; all ten preserved-file bindings |

The twelve OR images are pp.90–92, 277–278, 280, 282–285 and 602–603.
The four Reed images are pp.13, 59–60 and 68. I checked the selected excerpts,
headings, dates and their nearby page context visually; this is not a complete
character-by-character verification of all text on every full page.

The nine full reports were read in the retained, explicitly uncorrected OCR
context: Buckland 90–92; Ricker 92; Prentiss 277–280; Quinn 280–282; Moore 282;
Woodyard 283–284; Van Horn 284–285; Allen 285–286; Hardcastle 602–604.
Pages 279, 281, 286 and 604 were read as OCR only. Neighboring report fragments
were visible in those pages; they were not treated as a newly reviewed complete
source or a basis for new historical claims. I did not inspect the cached parent
PDFs or any additional book-page images.

Map inspection used full-image overviews plus native-pixel crops, generated in
memory without changing source files: Union legend `[480,480,2410,1900]`,
Union W. H. L. Wallace region `[5450,3250,6750,4100]`, Frémaux lines/fords
`[990,795,1880,1575]`, and Frémaux legend `[2060,450,2440,800]`.
These pixel windows are inspection locators, not surveyed coordinates. Not every
map label was read; no georeferencing or full force-location inventory was made.

## Substantive assessment

CL01–CL02 properly distinguish earlier April 3–5 encounters from the proposed
April 6 boundary. Buckland's April 5 dateline and “yesterday” establish the
attributed April 4 account, while Ricker's printed `[?]` remains visible and
its machine date remains null. Reed's earlier-contact narrative remains a later
compilation and a lead to underlying reports. Nothing here establishes a new
engagement segmentation automatically.

CL03–CL09 preserve disagreements about the Saturday patrol composition,
Sunday order and departure sequence, who issued orders, which pickets were
supported, and the clock for initial fire. Prentiss's November report explicitly
follows captivity; it is not mislabeled as an April account. Quinn's order time
is not converted into a contact time. Van Horn literally calls 3 a.m. the attack
time; that awkward wording should remain. Moore and Woodyard's later movement
and junction are not made into a first-contact point. Allen's statement is an
attributed claim to first enemy fire, not an adjudicated first shot. The full
OCR context did not supply an omitted qualification that reverses these bounded
interpretations.

CL10 distinguishes Hardcastle's advanced parties, cavalry shots, infantry
screen fire and later battalion withdrawal. The stated distances are source
reports, not survey control. The cavalry's location, identity and purpose of
fire remain unresolved. The incomplete dateline supports leaving the exact
document date null. No casualty or later-participation count is introduced as
an opening population.

CL11–CL12 correctly identify Reed's 4:55 and field-name placements as
retrospective reconstruction. Repeated statements in Reed do not multiply
corroboration. The supplied pages do not establish an independent clock
calibration or a georeferenced correspondence of the field descriptions. The
Saturday-night Wood/Hardee arrangement and battery location are attributed
relative positions, not a complete opening census.

CL13–CL14 accurately preserve the existing Beauregard text's 5 a.m. contact,
5:30 movement, echelon descriptions and already-forward cavalry/four pieces,
while avoiding the inference that Maney's ordered reinforcement was completed
before contact. This was a text/context review of `p386`, not a fresh visual
transcription check of Beauregard.

The Union map's blue morning/red night distinction and north-to-right
orientation are visible. The W. H. L. Wallace initials are legible when enlarged.
The red Lew Wallace, Buell and gunboat symbols cannot establish morning
locations. The Frémaux map includes the four Confederate command lines and
legible Tanner/Greer ford labels, but its April 6–7 title and symbol legend
provide no contact-specific clock. The endorsement is visible and agrees with
the retained catalog description. The Union catalog explicitly attributes its
date to Stephenson's 1989 catalog; neither catalog's 1862 label proves a
pre-contact production or knowledge date. Catalog snapshots support archival
metadata, not historical truth. The small CL-R2 spelling error does not alter
any of these conclusions.

No agreement among reports, maps, catalog entries, page images or
transcriptions is counted as extra independent testimony. The dependence
groups and narrative cautions are adequate for this non-admitting packet;
they are not proof that different groups are independent. The afloat rule,
ford guards, exact perimeter, first qualifying contact and both complete
membership sets remain unresolved. No morale/readiness score, causal effect,
win probability, canonical strength or command-credit allocation is added.

## Offline validation and implementation assessment

- `python3 design/shiloh-contact-location-v1/reference-audit.py`: passed.
  The 14 assertions, 38 anchors, 19 pairs, 32 new source bindings, 53 preserved
  metadata bindings, context binding and ten preserved-file hashes passed.
- `make check`: passed, 82 tests plus `generalship check`; no artifacts written
  by that CLI check. The tests include offline build and migration checks.
- Independent parent comparison: the prior 53 complete registry entries and
  every referenced raw file are unchanged from
  `1312a22808e65ee0866a85f2e82aab4c63397f01`.
- The previous boundary audit passed in a temporary archive of its own reviewed
  commit, `330599b8882ef9974f4641056c4c1091b0013912`. It was not run against
  the expanded current registry.
- In a temporary archive of the exact reviewed commit, `make reproduce` and
  `make packet` passed. All nine compared generated outputs, including the
  receipt, pilot report and TN003 packet, are byte-identical to the checked-in
  outputs. No reviewed input or production artifact was overwritten.
- `git diff --check`: passed. A concurrent primary-agent NOTICE edit and
  primary-owned dispatch/preservation files are outside this frozen review.

The migration-test adjustment keeps equality for each migrated source entry
and the registry's other fields while allowing subsequent additions. Missing,
changed or duplicated entries in that retained subset still fail equality;
the source validator separately checks registry integrity. The original fifty
entries retain their ordered comparison, the historical migration still emits
53 records, and numeric/event/unknown preservation checks remain intact. This
is an appropriate removal of a stale whole-registry size freeze, not removal
of the historical preservation contract. The report change accurately labels
the new review as pending at the frozen commit.

Both admission ledgers retain the 127-engagement / 36-campaign frame: v1 has
18 blocked / 22 excluded observations and v2 has 7 blocked / 33 excluded, with
zero complete or promoted rows. The frozen dossier remains 62 claims / 40
quantities / 26 events. Baseline coverage stays 23 engagements / 13 groups;
Brier remains 0.2768816348133779 against 0.25 for equal odds. The result is
unimproved, as the memo reports.

## Remaining limits

This purposive packet review does not estimate an extraction error rate. Exact
passage matching and visual agreement do not establish historical truth or
authorial independence. The four text-only Beauregard anchors and unverified
context OCR retain their narrower inspection status. No new external sources,
network fetches, parent-PDF inspection, complete map inventory, field survey,
historical clock adjudication or enriched model experiment was performed.

CL-R1 and CL-R2 remain unresolved in these immutable review outputs. Subsequent
primary assessment and corrected source versions must be recorded separately.
The existing five research gates remain open; this review authorizes neither
feature admission nor a release manifest.
