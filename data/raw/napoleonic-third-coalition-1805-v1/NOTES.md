# Running notes: Napoleonic first pass, third-coalition 1805 (22 entries)

Working notes for resuming an interrupted pass. Not evidence; the evidence is in `data/sources.json`,
the files beside this one, and `data/napoleonic/evidence/<ID>.json`.

## Plan (set 2026-10-06)

Per-entry ceiling: Bodart plus at most two further families. Candidate families, found on the Internet
Archive and checked for public-domain status (published before 1930):

| Work | IA item | Covers |
| --- | --- | --- |
| Alombert and Colin, La campagne de 1805 en Allemagne, t. III (two volumes) and t. IV, Section historique (French official history) | alombert-la-campagne-de-1805-en-allemagne-v-3-pt-1, v-3-pt-2, v-4 | Ulm campaign (Wertingen to Eschenau), Mariazell, Durnstein |
| Krauss, 1805. Der Feldzug von Ulm, 1912 (Austrian general; Kriegsarchiv files; uses Alombert-Colin for the French side) | 1805ieachtzehnhu00krau | Ulm campaign |
| Schoenhals, Der Krieg 1805 in Deutschland, 1873 (after Austrian original sources) | derkriegindeuts00schgoog | Mariazell, Durnstein, Hollabrunn, Austerlitz, Steken |
| Angeli, Erzherzog Carl als Feldherr, Bd. III, 1897 (Austrian, after original files) | erzherzogcarlvo03carlgoog | Italy 1805, Tyrol and Vorarlberg, Archduke Ferdinand |
| Koch, Memoires de Massena, t. V, 1850 | mmoiresdemassen00massgoog | Italy 1805 (French side) |
| Correspondance de Napoleon Ier, t. XI | correspondancede11napouoft | Austerlitz, Hollabrunn, others |

Bodart's own source list for 1805 names Angeli, Koch, Saint-Cyr, Rustow, Schneidawind, Stutterheim and the
Kriegsarchiv's Kriegschronik (not found on the IA). Rustow (1859 Zurich edition), Mayerhoffer (1905 lecture
sketch, garbled OCR) and Einsiedel (1812) were looked at and not used: neither side's own history.

## Procedure notes

- Page image n for a printed page: Krauss n = printed + 13 at p. 341 (checked); Alombert t. III vol. 1 n = leaf
  of the OCR page index (p. 293 = n300, checked). Always confirm the printed page number on the image.
- The IA `_hocr_pageindex.json.gz` / `_hocr_searchtext.txt.gz` were used only as locating tools, not registered.
- Selections are regenerated from collapsed-text phrase anchors; `selection_character_ranges` in the registry give
  the half-open raw ranges so a selection can be rebuilt from its parent.

- Leaf offsets checked on the images: t. II n = printed + 17 (pp. 162-166); t. III vol. 1 n = printed + 7
  (pp. 29-54, 313-329, 507-516); Krauss n = printed + 13 (pp. 341-409).
- Every figure in a strength value or a recorded loss is read from a registered page image. OCR digits may
  stand inside a cited passage but are never restated in a value; figures seen only in the OCR are listed as
  deferred in the dossier's open questions.
- Batch 1b offsets, checked on the images: t. II n = printed + 17 (p. 161); t. III vol. 1 n = printed + 7
  (pp. 67-103, 217, 229); t. III vol. 2 n = printed - 593 for pp. 661-774 and printed - 601 for pp.
  1199-1255; Krauss n = printed + 13 (pp. 449-499).
- The IA serves the t. II and t. III vol. 2 page images at 794 x 1123 pixels, so `sips -Z 1600` enlarges
  them; the t. III vol. 1 and Krauss images are served larger and downscaled. Record which in
  `snapshot_transform` (the registration script's `served` field). The four t. II images of batch 1a say
  "downscaled" in error; see the erratum in `docs/source-additions.md`.
- In renderings of OCR passages, counts, times and dates are elided ('...') or marked '(OCR)'. Number
  words in the OCR ('trois', 'drei') count as OCR figures too.
- Batch 1c offsets, checked on the images: Koch t. V (mmoiresdemassen00massgoog) n = printed + 10 (pp.
  80-376); Angeli Bd. III (erzherzogcarlvo02angegoog) n = printed + 16 (pp. 73-183). All 29 images were
  served larger than 1600 px and downscaled.
- Angeli: the registered copy is erzherzogcarlvo02angegoog (University of Michigan). The plan table's
  erzherzogcarlvo03carlgoog is another copy of Bd. III and was not used.
- Page of a quote in the OCR selections: Koch's from the running heads; Angeli's from the section's first
  page plus the Google watermark lines ('Digitized by VjOOQIC') before the quote, one per page end.
  Confirm on the image when a figure matters.
- Ordinals and number words in the OCR ('erste', 'einen', 'zweiten'; 'first') count as OCR figures. A
  battle day read on a page image may be used in a value. Page numbers in Angeli's source notes are read
  in the OCR and marked so wherever they are cited.
- Batch 1d offsets, checked on the images: Moriggl (bub_gb_mz5BAAAAYAAJ) n = printed + 10 (pp. 89-93),
  printed + 16 (pp. 300-348) and printed + 18 (pp. 363-438); Victoires et conquêtes t. XV
  (bub_gb_UNgLhuBKzUAC) n = printed + 29 (pp. 215-219). All 24 images were served larger than 1600 px
  and downscaled.
- Moriggl's Fraktur OCR garbles letters and page numbers. The page of a quote in the OCR selection comes
  from the page marks mapped for pp. 298-439, checked on the images at pp. 430-439. The parent repeats pp.
  348-349 once in a second, more garbled OCR; quotes are not taken from that copy.
- Moriggl's order of battle of the Grande Armée at its crossing of the Rhine (pp. 89-93, with a
  recapitulation on p. 94) gives every corps by division. Pp. 89, 92 and 93 are registered; the other
  pages can be registered if a later entry needs them. Its date is the crossing, not the engagement.
- Another Moriggl item (bub_gb_8HpBAAAAcAAJ), whose OCR has none of the engagement names, was not used.
- Batch 1e offsets, checked on the images: Alombert and Colin t. IV
  (alombert-la-campagne-de-1805-en-allemagne-v-4) n = printed + 15 (pp. 125-166 and 650-770); Schönhals
  (derkriegindeuts00schgoog) n = printed + 4 (pp. 127-137). The IA serves t. IV's images at 794 x 1123
  pixels and Schönhals's at 804 x 1292, so `sips -Z 1600` enlarges both.
- t. IV's OCR misreads figures often, above all 1 as 4 and 5 or 6 as 8. On p. 166 it reads '488' for 155,
  '403' for 103, '1,309' for 1,300, '85' for 65, '104' for 101, '4,600 à 4,700' for 1,600 à 1,700 and
  '020' for 920; on p. 769 it reads the officers' total as '1x6', whose first digit is indistinct on the
  image and is read as 4 from the column sum (426). The print's 1 has a flag and no cross-stroke. Never
  take a t. IV figure from the OCR.
- Regiment numbers are ordinals. In a value or an OCR rendering they stand only where a page image cited
  in the same claim prints them (p. 166 for the 4e léger, the 100e, the 103e and the 4e dragons; p. 769 for
  the 9e léger, the 32e, the 96e and the 1er hussards); elsewhere they are generalised or elided as
  '... (OCR)'. Archive call numbers such as XI-46 and XIII-61 are identifiers, not figures. Words in
  square brackets in a rendering paraphrase the context and carry no OCR figure.
- Schönhals's OCR page numbers are often garbled ('1*5' for 145); the page of a quote comes from the page
  numbers mapped against the Google watermarks and is confirmed on the image where a figure matters.
- t. IV's p. 770, viewed and not registered, is the 7th corps' approximate return of 4 brumaire an XIV
  (26 October), dated at Fribourg. It bears on side A's strength at Dornbirn (B368d); see the research log.

## Status

- 2026-10-17, batch 1a: Wertingen (B363a), Günzburg (B363b) and Haslach (B363c) drafted from Bodart, Alombert
  and Colin (t. II, t. III vol. 1) and Krauss; primary-verified. 73 records registered (the three OCR parents,
  two selections, 34 page images with figure transcriptions).
- 2026-10-17, batch 1b: the Ulm phase, Parsdorf (B364a), Elchingen (B364b), Memmingen (B364c), Herbrechtingen
  (B364d), Ulm (B365a), Neresheim (B365b), Trochtelfingen (B365d) and Eschenau (B366a), drafted from Bodart,
  Alombert and Colin (t. II, t. III vols. 1 and 2) and Krauss; primary-verified. 100 records registered (the
  t. III vol. 2 OCR parent, three selections, 48 page images with figure transcriptions).
- 2026-10-17, batch 1c: Italy, Verona (B365c), Caldiero (B367a), Pojano (B367b) and Castelfranco (B369b),
  drafted from Bodart, Koch (t. V) and Angeli (Bd. III); primary-verified. 62 records registered (the two
  OCR parents, two selections, 29 page images with figure transcriptions). Angeli's source notes cite
  Koch's pages for all four actions, so the two are not independent there.
- 2026-10-17, batch 1d: Tyrol and Vorarlberg, Scharnitz (B368a) and Dornbirn (B368d), drafted from
  Bodart, Moriggl (1861) and Victoires et conquêtes (t. XV, 1819); primary-verified. 52 records registered
  (the two OCR parents, two selections, 24 page images with figure transcriptions). Both entries' targeted
  follow-up, for side A's strength, used Moriggl's order of battle at the Rhine crossing.
- 2026-10-17, batch 1e: the Danube, Mariazell (B368b) and Dürnstein (B368c), drafted from Bodart,
  Alombert and Colin (t. IV) and Schönhals (1873); primary-verified. 46 records registered (the two OCR
  parents, two selections, 21 page images with figure transcriptions). The targeted follow-ups, for side
  A's strength at both, searched t. IV's appendix of situations for returns of the 3rd and 6th corps.
- Next: B369a Ober-Hollabrunn, B369c Austerlitz and B370a Steken (Schönhals, the Correspondance t. XI and
  others still to be chosen), then verify the group.
