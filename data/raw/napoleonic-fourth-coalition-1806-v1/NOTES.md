# Running notes: Napoleonic first pass, fourth-coalition 1806 (23 entries)

Working notes for resuming an interrupted pass. Not evidence; the evidence is in `data/sources.json`,
the files beside this one, and `data/napoleonic/evidence/<ID>.json`.

## Plan (set 2026-10-17)

The group is the war of 1806 against Prussia and Saxony, with Russia from November, by Bodart's
entries from Saalfeld (10 October) to Golymin and the siege of Breslau (December 1806 to January
1807). Batches follow the campaign:

| Batch | Entries |
| --- | --- |
| 2a | Saalfeld B371b, Jena B372a, Auerstedt B373a |
| 2b | Erfurt B373b, Halle B374a, Spandau B374b, Prenzlau B374c, Stettin B374d, Pasewalk B375a, Boldekow B375b, Küstrin B375c, Anklam B375d, Wolgast B375e |
| 2c | Lübeck B376a, Ratkau B376b, Magdeburg B376c, Hameln B376d, Nienburg B377a |
| 2d | Groß-Glogau B377b, Breslau B378b |
| 2e | Czarnowo B377c, Pultusk B377d, Golymin B378a |

Per-entry ceiling: Bodart plus at most two further families. Batch 2a uses one family for each side:

| Work | IA item | Covers |
| --- | --- | --- |
| Foucart, Campagne de Prusse (1806): Iéna, 1887 (French documentary history from the archives de la guerre) | campagnedepruss01foucgoog | Saalfeld to Auerstedt, side A's documents |
| Höpfner, Der Krieg von 1806 und 1807, Theil 1, Bd. 1, 1850 (Prussian history from the war archive) | derkriegvonundi00hpgoog | Saalfeld to Auerstedt, side B |

Foucart's t. I ends with the documents of 14 October and his observations, and Höpfner's Bd. 1 with
chapter 10 (to p. 490) and its appendices. Candidates for the later batches, downloaded but not registered, read only on their
title pages and contents: Foucart, Campagne de Prusse (1806): Prenzlow-Lubeck, 1890
(campagnedepruss00foucgoog), and Höpfner Theil 1, Bd. 2 (2nd edition, 1855; 10595282bsb), whose
contents begin with the retreat to 17 October and Halle, for 2b-2c; Höpfner Theil 2, Bd. 4
(bub_gb_9PVKAAAAcAAJ, 1851; also bub_gb_ccATAAAAYAAJ), on Silesia with Glogau and Breslau, for 2d;
Foucart, Campagne de Pologne (Pultusk et Golymin), 1882 (t. I is campagnedepolog02foucgoog and t. II
campagnedepolog01foucgoog), and Höpfner Theil 2, Bd. 3 (10594714bsb, 1851; bub_gb_l74TAAAAYAAJ, 2nd
edition, 1855), for 2e. Editions of one work are one family; record which edition each claim uses.

## Procedure notes

- Leaf offsets, from the page boundaries of each item's djvu.xml and checked on the images: Foucart
  t. I n = printed + 20 throughout the pages read; Höpfner Bd. 1 n = printed + 20 to p. 315 and + 21
  from p. 316. Höpfner's leaf 336 carries the OCR of p. 317, out of order, before pp. 316 and 317 on
  leaves 337 and 338 (no image of those leaves is registered). All 44 images were served larger than
  1600 px and downscaled.
- Page of a quote in the OCR selections: from the djvu.xml page boundaries, checked against the OCR
  page numbers or running heads, which the OCR sometimes misreads ('4G2' for Foucart p. 462, '459'
  for Höpfner p. 455 on leaf 476).
- The selections' section names (`saalfeld-10-oct`, `jena`, `auerstedt`, ...) are listed in each
  selection record; 16 of the 17 sections are cited. Foucart's `second-bulletin` is not: the 2nd
  Bulletin is cited from the transcriptions of its pp. 522 and 524.
- 18 of the 44 transcriptions record a check of the figures on the Internet Archive's full-size page
  image. The OCR misreads some figures that the images settle: Foucart p. 635 '75' (OCR '(5') and
  p. 678 footnote 2 '26' (OCR '86').
- In renderings of OCR passages, counts, dates, ordinals, regiment numbers and list enumerators are
  elided ('...') or marked '(OCR)', and number words may stay marked '(OCR)', as in 1805. Every figure
  in a strength claim or a loss record is read from a registered page image.
- Batch 2b is split in two: 2b-i (Erfurt, Halle, Spandau and Prenzlau) and 2b-ii (Stettin to
  Wolgast). It uses Foucart's t. II (Prenzlow-Lubeck, 1890; campagnedepruss00foucgoog) and
  Höpfner's Bd. 2 (2nd edition, 1855; 10595282bsb), both registered in 2b-i. Their selections
  already hold the 2b-ii sections: Foucart's `stettin-pasewalk-30-oct`, `bulletin-24`,
  `anklam-park-31-oct`, `anklam-park-1-nov`, `kuestrin-2-nov`, `anklam-wolgast-2-nov` and
  `bulletin-25`, and Höpfner's `capitulations-after-prenzlau` and `kuestrin`. A passage outside
  them needs a new selection version or a page transcription from the image; Wolgast cites
  Foucart's pp. 618-621 and 628 that way.
- Leaf offsets in 2b, from the djvu.xml page boundaries and the running heads: Foucart t. II n =
  printed + 33 to p. 304, + 35 for pp. 305-480 (a plate at leaves 338-339) and + 37 from p. 481;
  Höpfner Bd. 2 n = printed + 7 throughout (pp. 1-396). Images are downscaled to 1600 px; small
  figures are checked on full-resolution crops.
- Attribution in 2b: every statement's subject or author must be in the claim's own quotes, so
  claims cite the letter heading and, where printed, the signature, and for the 1st corps's
  journal its closing attribution '(Journal du 1er corps.)'. Its corps number is OCR-only and is
  elided in renderings. A paragraph in a Foucart footnote with no attribution of its own is
  Foucart's, not the journal's. Where Höpfner refers to the subject only by a pronoun, also cite
  the nearest sentence that names it.
- Höpfner's general source statement is in the preface of Bd. 1 (the post-war judicial inquiries);
  his place sections rarely name sources. Do not attribute a place's account to the inquiry records
  beyond what that preface says.
- *Campagne de Pologne* t. I (Foucart, 1882; campagnedepolog02foucgoog), registered in 2c-iv, is
  in Foucart's family. Leaf offsets from its djvu.xml page boundaries: n = printed + 23 to p. 305,
  + 25 for pp. 306-512, + 27 for pp. 513-528 and + 29 from p. 529; the four registered images
  (pp. 132, 133, 215 and 216) were checked. P. 215 carries no printed number: the chapter heading
  '3 ET 4 DÉCEMBRE.' stands at its head, and the next leaf, n239, carries p. 216's running head.
  T. II (campagnedepolog01foucgoog), registered in 2d-ii, is at n = printed + 11 for the eight
  pages registered (pp. 93-97, 108, 112 and 113), checked on the images; its title page is image
  n12, not registered.
  In 2e-i, t. I pp. 372-376, 390-401 and 439-440 were registered (n = printed + 25), and t. II's
  unnumbered summary return of December 1806 on leaf n486, the first text page after the
  half-title 'SITUATIONS' on n484. In 2e-ii, t. I pp. 462-473 (n = printed + 25) and 514-517
  (n = printed + 27) were registered, checked on the images. T. I p. 461 (its leaf n486), with
  the heading and dateline of the major general's letter to the grand-duc de Berg (Lopaczyn,
  26 December, 9 a.m.) that ends on p. 462, was read on the image and not registered. In 2e-iii,
  t. I pp. 458-461 and 474-493 (n = printed + 25), p. 461 among them, and p. 518 (n = printed +
  27) were registered, checked on the images.
- Höpfner Theil 2, Bd. 4 (1851; bub_gb_9PVKAAAAcAAJ), registered in 2d-i: leaf n = printed + 12
  for pp. 15-31 and for the Breslau pages registered in 2d-ii (p. 36 to p. 118), checked on the
  images. Chapter 15 opens the volume's text, and chapter 16, on
  the governor-general of Silesia and the siege and capitulation of Breslau, begins on p. 33.
  Völderndorff's fourth book has its own pagination (11748199bsb, n = printed + 333), noted in
  case it replaces a family later.
- Höpfner Theil 2, Bd. 3 (1851; 10594714bsb, Bayerische Staatsbibliothek), registered in 2e-i:
  leaf n = printed + 10 for pp. 23-24 and 82-95 (2e-i), pp. 107-119 (2e-ii) and pp. 101-102 and
  122-126 (2e-iii), checked on the images. The title page (n5) and the
  preface to the second part (n7-n8) were read on the images and are not registered. The second
  edition (1855; bub_gb_l74TAAAAYAAJ) was compared in the OCR only. The image of p. 26 (n36: the
  army's totals by the report of 23 October and Höpfner's comment on them) was downloaded in 2e-i
  and not registered: p. 109 gives the Russian force at Pultusk, so the entry did not need it,
  and the image was moved out of this directory in 2e-ii.
- Grouped renderings: the rendering check reads only R_ names written in a claim's own rationale,
  so a module-level string joining renderings (a letter's heading and dateline) is not seen; write
  the rend(...) call into each claim.
- The ceiling is Bodart plus two families per entry. In this group they are Foucart and
  Höpfner; a Bavarian or Württemberg history would have to replace one of them.

## Status

- 2026-10-17 and 18, batch 2a: Saalfeld, Jena and Auerstedt drafted from Bodart, Foucart and
  Höpfner; primary-verified. 92 records registered (two OCR parents, two selections, 44 page images
  with figure transcriptions). About 6.2 million tokens.
- 2026-10-18, sub-batch 2b-i: Erfurt, Halle, Spandau and Prenzlau drafted from Bodart, Foucart t. II
  and Höpfner Bd. 2; primary-verified. 70 records registered (two OCR parents, two selections, 33
  page images with figure transcriptions). About 2.4 million tokens.
- 2026-10-18, sub-batch 2b-ii: Stettin, Pasewalk, Boldekow, Küstrin, Anklam and Wolgast drafted
  from Bodart, Foucart t. II and Höpfner Bd. 2; primary-verified. 94 records registered (47 page
  images with figure transcriptions). About 3.5 million tokens.
- 2026-10-18, sub-batch 2c-i: Ratkau drafted from Bodart, Foucart t. II and Höpfner Bd. 2;
  primary-verified. 26 records registered (13 page images with figure transcriptions). About
  0.3 million tokens.
- 2026-10-18, sub-batch 2c-ii: Lübeck drafted from Bodart, Foucart t. II and Höpfner Bd. 2;
  primary-verified. 54 records registered (27 page images with figure transcriptions). About
  1.0 million tokens.
- 2026-10-18, sub-batch 2c-iii: Magdeburg drafted from Bodart, Foucart t. II and Höpfner Bd. 2;
  primary-verified. 66 records registered (33 page images with figure transcriptions). About
  1.5 million tokens.
- Correction to the earlier scan: Höpfner's Magdeburg section is pp. 330–336, not 308–336, and
  Hameln and Nienburg are his chapter 19, on the Weser, pp. 339–383, not 340–378. Foucart's
  Magdeburg documents run from p. 276 (Ney's summons of 23 October) to p. 827 (the 31st Bulletin).
- 2026-10-18, sub-batch 2c-iv: Hameln and Nienburg drafted from Bodart, Foucart t. II with
  *Campagne de Pologne* t. I, and Höpfner Bd. 2; primary-verified. 91 records registered (the
  *Campagne de Pologne* t. I OCR parent and 45 page images with figure transcriptions). About
  1.9 million tokens. Batch 2c is complete.
- 2026-10-18, sub-batch 2d-i: Groß-Glogau drafted from Bodart, Foucart (*Campagne de Pologne*
  t. I with t. II) and Höpfner Bd. 4; primary-verified. 53 records registered (the Höpfner Bd. 4
  OCR parent and 26 page images with figure transcriptions). About 2.3 million tokens.
  Völderndorff's Bavarian account (fourth book, pp. 56-66) was read and transcribed, cited as a
  fourth family in the first draft, and withdrawn before commit under the ceiling of Bodart plus
  two families. Its transcriptions are not in the repository.
- 2026-10-18, sub-batch 2d-ii: Breslau drafted from Bodart, Foucart (*Campagne de Pologne* t. II,
  newly registered) and Höpfner Bd. 4; primary-verified. 81 records registered (the t. II OCR
  parent and 40 page images with figure transcriptions). About 1.9 million tokens. Batch 2d is
  complete. Völderndorff and the Lower Silesian Digital Library's siege account stayed out under
  the ceiling.
- 2026-10-18, sub-batch 2e-i: Czarnowo drafted from Bodart, Foucart (*Campagne de Pologne* t. I
  and t. II) and Höpfner Bd. 3 (1851 edition, newly registered); primary-verified. 73 records
  registered (the Höpfner Bd. 3 OCR parent and 36 page images with figure transcriptions). About
  3.7 million tokens. The one targeted follow-up, for side A's strength, found t. II's summary
  return, which gives the 3rd corps but not the troops engaged.
- 2026-10-18, sub-batch 2e-ii: Pultusk drafted from Bodart, Foucart (*Campagne de Pologne* t. I
  and t. II) and Höpfner Bd. 3; primary-verified. 58 records registered (29 page images with figure
  transcriptions: Höpfner pp. 107-119 and *Campagne de Pologne* t. I pp. 462-473 and 514-517).
  About 1.2 million tokens. The one targeted follow-up, Lannes's and Corbineau's letters of
  28 December (pp. 514-517), added Lannes's revised losses and Corbineau's figures and hearsay, but
  no strength for the 3rd division of Davout's corps.
- 2026-10-18, sub-batch 2e-iii: Golymin drafted from Bodart, Foucart (*Campagne de Pologne* t. I
  and t. II) and Höpfner Bd. 3; primary-verified. 64 records registered (32 page images with figure
  transcriptions: Höpfner pp. 101-102 and 122-126 and *Campagne de Pologne* t. I pp. 458-461,
  474-493 and 518). About 2.1 million tokens. The one targeted follow-up, the grand-duc de Berg's
  letter of 28 December (p. 518), added his statement that Buxhœvden's whole corps had fought at
  Golymin, which Corbineau's letter of the same day denies (in Höpfner only troops of the 7th
  Division were there, by our reading), but no strength for either side. Batch 2e, and with it the group's first pass, is complete.
- Next: the group check of the 23 drafts together, bounded as for `third-coalition 1805`, then
  the README's status line, then `fourth-coalition 1807` (19 entries).
