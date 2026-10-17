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

## Status

- 2026-10-17, batch 1a: Wertingen (B363a), Günzburg (B363b) and Haslach (B363c) drafted from Bodart, Alombert
  and Colin (t. II, t. III vol. 1) and Krauss; primary-verified. 73 records registered (the three OCR parents,
  two selections, 34 page images with figure transcriptions).
- 2026-10-17, batch 1b: the Ulm phase, Parsdorf (B364a), Elchingen (B364b), Memmingen (B364c), Herbrechtingen
  (B364d), Ulm (B365a), Neresheim (B365b), Trochtelfingen (B365d) and Eschenau (B366a), drafted from Bodart,
  Alombert and Colin (t. II, t. III vols. 1 and 2) and Krauss; primary-verified. 100 records registered (the
  t. III vol. 2 OCR parent, three selections, 48 page images with figure transcriptions).
- Next: Italy (B365c Verona, B367a Caldiero, B367b Pojano, B369b Castelfranco; Koch, Angeli), then Tyrol and
  Vorarlberg (B368a Scharnitz, B368d Dornbirn) and the Danube and Moravia entries (B368b Mariazell, B368c
  Dürnstein, B369a Ober-Hollabrunn, B369c Austerlitz, B370a Steken; Schönhals, Correspondance).
