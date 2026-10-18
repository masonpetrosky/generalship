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
  them needs a new selection version.
- Leaf offsets in 2b, from the djvu.xml page boundaries and the running heads: Foucart t. II n =
  printed + 33 to p. 304, + 35 for pp. 305-480 (a plate at leaves 338-339) and + 37 from p. 481;
  Höpfner Bd. 2 n = printed + 7 throughout (pp. 1-396). Images are downscaled to 1600 px; small
  figures are checked on full-resolution crops.
- Attribution in 2b: every statement's subject or author must be in the claim's own quotes, so
  claims cite the letter heading and, where printed, the signature, and for the 1st corps's
  journal its closing attribution '(Journal du 1er corps.)'. Its corps number is OCR-only and is
  elided in renderings. A paragraph in a Foucart footnote with no attribution of its own is
  Foucart's, not the journal's.
- Höpfner's general source statement is in the preface of Bd. 1 (the post-war judicial inquiries);
  his place sections rarely name sources. Do not attribute a place's account to the inquiry records
  beyond what that preface says.

## Status

- 2026-10-17 and 18, batch 2a: Saalfeld, Jena and Auerstedt drafted from Bodart, Foucart and
  Höpfner; primary-verified. 92 records registered (two OCR parents, two selections, 44 page images
  with figure transcriptions). About 6.2 million tokens.
- 2026-10-18, sub-batch 2b-i: Erfurt, Halle, Spandau and Prenzlau drafted from Bodart, Foucart t. II
  and Höpfner Bd. 2; primary-verified. 70 records registered (two OCR parents, two selections, 33
  page images with figure transcriptions). About 2.4 million tokens.
- Next: sub-batch 2b-ii, Stettin B374d, Pasewalk B375a, Boldekow B375b, Küstrin B375c, Anklam
  B375d and Wolgast B375e, from the same volumes.
