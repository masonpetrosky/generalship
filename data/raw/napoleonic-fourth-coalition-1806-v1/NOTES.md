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

## Status

- 2026-10-17 and 18, batch 2a: Saalfeld, Jena and Auerstedt drafted from Bodart, Foucart and
  Höpfner; primary-verified. 92 records registered (two OCR parents, two selections, 44 page images
  with figure transcriptions). About 6.2 million tokens.
- Next: batch 2b, from Erfurt to Wolgast, which needs Foucart's t. II and Höpfner's Bd. 2 or other
  families.
