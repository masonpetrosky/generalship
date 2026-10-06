# Napoleonic frame v1: Bodart's entries for 1792–1815

Status: **built and frozen, 2026-10-06; primary-verified.** This design applies the owner's scoping
decisions of 2026-10-06 ([scoping note](napoleonic-scoping.md),
[record](../data/napoleonic/owner-decision-scoping-2026-10-06.json)). It fixes how the frozen
Napoleonic frame is built from Bodart's *Kriegs-Lexikon* before any research or modelling. The frame
is not a model input and admits no feature.

- Frame: [`data/napoleonic/frame-v1.json`](../data/napoleonic/frame-v1.json)
- Cohort: [`data/napoleonic/cohort-v1.json`](../data/napoleonic/cohort-v1.json)
- Overrides: [`data/napoleonic/frame-overrides-v1.json`](../data/napoleonic/frame-overrides-v1.json)
- Transcription record:
  [`data/napoleonic/transcription-resolutions-v1.json`](../data/napoleonic/transcription-resolutions-v1.json)
- Builder: `generalship/napoleonic.py`; `python3 -m generalship napoleonic-frame` writes the frame
  and the cohort, and `make check` fails if either does not rebuild.

## 1. Source

- **The work.** Gaston Bodart, *Militär-historisches Kriegs-Lexikon (1618–1905)*, Wien und Leipzig:
  C. W. Stern, 1908.
- **The copy.** Internet Archive item `bub_gb_A0kNAAAAYAAJ` (Google scan, Public Domain Mark). Pages
  337–339 were read from a second copy, `bub_gb_Eo4DAAAAYAAJ`, where the pinned scan hides an edge.
- **Pinned files**, under `data/raw/bodart-1908-v1/`:
  - the OCR text;
  - IA's page index and OCR search text;
  - the page-number map and item metadata;
  - page images of pp. 45–48 and 267–490, downscaled to 1600 px as for Livermore, and pp. 337–339 of
    the second copy.
- **Transcription.** The frame is built from a manual transcription of the page images
  (`bodart-1908-transcription-v1`, one section per printed page). It is not built from the OCR,
  which garbles years and figures.

## 2. Transcription and its verification

- **Two independent readings.** Each of the 227 pages (pp. 45–48 and 268–490) was transcribed twice,
  independently, from the page images alone, under one written brief:
  - one line per entry header, location and paragraph;
  - `left | centre | right` rows for the tables;
  - figures exactly as printed;
  - small-print officer-loss tables are not transcribed.
- **Comparison.** The readings were compared entry by entry. 27 pages had at least one flag. The
  primary settled each disagreement, and each of the 113 spots the base reading marked uncertain,
  against the full-resolution scan, or the second copy for pp. 337–339. The OCR was a third vote that
  never decided.
- **Arithmetic.** Printed components were checked against printed totals. Of 7 flags, 6 were checker
  artifacts and 1 is a printed mismatch (Nauders, B329b), kept as printed.
- **Audit.** After reconciliation the primary checked every entry on a seeded random sample of 15 pages
  against the page images (`random.Random(20261006).sample(range(268, 491), 15)`). The check covered
  the header, location, sides and printed figures of 42 entries.
  - No frame field was wrong. That bounds the per-entry rate of remaining frame-field errors at 6.9%
    (one-sided 95%).
  - One punctuation slip was found and corrected.
  - The checker had already seen the frame listings, so this is a check against the images, not a
    blind third transcription.
- **Remaining uncertainty.** One reading stays marked: the Turkish garrison of Fort Abukir, B339d,
  "5.000[?]". Its first digit is damaged in both copies.

## 3. Unit, identity and fields

- **Unit.** One frame record per Bodart entry: 708 entries on pp. 268–490.
- **ID.** `B` plus the printed page on which the entry begins, plus a letter for its position on that
  page. For example, Austerlitz, the third entry beginning on p. 369, is `B369c`. IDs never change;
  corrections are new versions.
- **Fields as printed:**
  - the date text and the type words;
  - the place, alternative names, category and location;
  - the running head of the page;
  - the winner's and loser's force text and the printed "unter …" commander text;
  - each side's strength and loss statements, where the mechanical extraction finds them. 68 in-frame
    entries have no strength statement extracted.
  - Dossiers read the full entry text, not these extracts.
- **Fields derived mechanically:**
  - start and end dates. Impossible printed dates are flagged and never corrected, for example Speyer
    "31./9." 1792 (B269d).
  - each side's national contingents (section 5);
  - the war (section 4) and whether the entry is in the frame;
  - side A and the outcome (section 5);
  - flags:
    - `naval` (type word SEE…);
    - `indecisive_printed` (Bodart's "Unentschiedenes …");
    - `no_combat_printed` ("ohne Schwertstreich");
    - the side method, including `later_clause` where a side is named only in a later clause.

## 4. Membership and wars

**Rule.** An entry is in the frame if all of the following hold:

- its start year is 1792–1815;
- it belongs to a war in which France was a belligerent;
- it is an engagement: Bodart's three conventions (Alkmaar 1799, El-Arisch 1800, Cintra 1808) are
  agreements and stay outside;
- one side is France or a force fighting with it.

Two entries in France's wars fail the last test and are recorded as overrides. One is Lemnos 1807,
Russian against Turkish fleets. The other is Copenhagen 1807, a British attack on neutral Denmark.

**Wars.** Each entry's war is taken from its page's running head. Where a page names two wars, the
entry's belligerents, place and year decide.

- Royalist entries go to the Vendée war; Spanish, Portuguese or Iberian entries to the Peninsular War.
- Egyptian places in 1801 go to the British expedition.
- The years each war covers in Bodart limit the choice.

| Bodart's war (running head) | Key | France fought | In frame |
| --- | --- | --- | --- |
| Erster Koalitionskrieg | first-coalition | yes | 181 |
| Bürgerkrieg in der Vendée | vendee | yes (the Republic against the royalists) | 16 |
| Expedition nach Ägypten, Neapel, Irland | egypt-naples-ireland | yes | 14 |
| Zweiter Koalitionskrieg | second-coalition | yes | 112 |
| Englische Expedition nach Ägypten (1801) | british-egypt-1801 | yes | 8 |
| Dritter Koalitionskrieg; Krieg gegen England und Neapel | third-coalition | yes | 30 |
| Krieg gegen Preußen und Rußland; Krieg gegen Schweden | fourth-coalition | yes | 42 |
| Krieg auf der Pyrenäischen Halbinsel | peninsula | yes | 91 |
| Krieg gegen Österreich / Feldzug 1809 gegen Österreich | fifth-coalition | yes | 37 |
| Feldzug 1812 gegen Rußland | russia-1812 | yes | 31 |
| Befreiungskriege | liberation | yes | 86 |
| Feldzug 1815 | hundred-days-1815 | yes | 15 |
| Polnische Insurrektion 1792; Polnischer Insurrektionskrieg 1794 | russo-polish-1792, polish-1794 | no | 0 |
| Englisch-dänischer Seekrieg (1801) | anglo-danish-1801 | no | 0 |
| Schwedisch-russischer Krieg 1808–1809 | finnish-1808 | no | 0 |
| Russisch-türkischer Krieg | russo-turkish-1806 | no | 0 |
| Amerikanisch-englischer Krieg | anglo-american-1812 | no | 0 |

**A consistency check on the heads.** Bodart prints each entry by its end date. A page head names
the wars on that page, so it can mislabel an entry at a war boundary.

- The builder lists France's opponents for each war. It stops on any entry whose opponents fall
  outside that list, and on any Spanish or Portuguese troops outside the Peninsular War in 1808–1814.
- Five entries were stopped. Each is decided by an override with its reason:
  - Saalfeld 1806: the Prussian war, not Naples.
  - Amantea 1806–07 (Calabria): the war against Naples, not Prussia.
  - Riga 1812: the 1812 campaign, not the Peninsula.
  - Toulouse and Bayonne 1814: the Peninsular War, not the Befreiungskriege.
- Pages 489–490 print the 1813–14 head "Krieg auf der Pyrenäischen Halbinsel — Befreiungskriege"
  over 1815 entries. A recorded head correction gives them the 1815 campaign.

**Out of frame (45 of 708 entries):**

- 37 in wars France did not fight;
- 3 before 1792 (1791);
- 3 conventions;
- 2 where France was not engaged.

Out-of-frame entries stay in the same file with their reason, so the denominators stay visible.

## 5. Sides and outcome

**Winner and loser.** Bodart puts the winner on the left of his tables and names the winner first in
his prose (p. 46).

- The builder reads the first paragraph by its grammatical form:
  - "Sieg der X über die Y";
  - "Die X zwingen die Y …";
  - "Vor X kapituliert Y";
  - "Die Y ergibt sich an X";
  - "Die Y übergibt …";
  - "Unentschiedenes Treffen zwischen den X und den Y";
  - "Siegreiche Gefechte der X gegen die Y".
- It falls back to the first table row, winner left. Where both exist they must not contradict each
  other.
- Each side's force text runs from its first nation word to its commander, terms or the end of its
  clause, outside parentheses.
- Four entries name a side only in a later clause (B287d, B293c, B427c, B482c). They are flagged, and
  each was checked against its printed paragraph.

**Nations.** A lexicon of Bodart's words maps force text to contingents: Franzosen, Österreicher,
Preußen, Russen, Engländer, Spanier, Rheinbundtruppen and others.

- A clause such as "nach dem russischen Feldzuge" names no force and is ignored.
- French royalists and émigrés are not France.

**Side A** is France and the forces fighting with it in that engagement. Side B is their opponents.
In the Vendée, side A is the Republic. Side A is decided as follows:

- **French troops named on one side** decide it: 633 of the 663 in-frame entries.
- **Otherwise an ally table decides**, a frame convention from the alliance periods (26 entries). It
  is not taken from Bodart.

  | Nation | Counted with France |
  | --- | --- |
  | Spain | 1796–1807 |
  | Batavian Republic and Holland | 1796–1810 |
  | Italian and Polish troops | 1797–1814 |
  | Bavaria and Württemberg | 1805–1812 |
  | Baden | 1805–1812 |
  | Hesse and Rheinbund troops | 1806–1812 |
  | Saxony and Westphalia | 1807–1812 |
  | Denmark | 1808–1813 |
  | Austria and Prussia | 1812 |
  | Irish insurgents | 1798 |

  - The table is checked against every Bodart entry that names French troops. A nation it counts
    with France must never be named against the French in its window.
  - The windows end in 1812 for the states that changed sides in 1813, so no 1813 entry depends on
    them.
- **Otherwise an override decides** (4 entries):
  - Condé 1794: the garrison surrenders "unter der Bedingung … nicht gegen Frankreich zu dienen".
  - Tolentino, Ancona and Gaëta 1815: Murat's Neapolitans against Austria in Bodart's 1815 campaign.

`french_troops_named` records whether Bodart's text names French troops on side A.

**Outcome.** The outcome is 1 if side A is Bodart's winner. Side A won 366 of the 663 in-frame
entries.

**Indecisive battles.** Bodart gives no draws. He calls four entries indecisive and still puts a
winner first: the side that held the field or reached its aim, or else the side with fewer troops.

- Dossiers record a source dispute where they find one.
- The run design, fixed before modelling, decides how disputed entries enter any test.

**Naval entries** are in the frame (17) and are not rated.

## 6. Campaign groups

A campaign group is the entry's war together with the calendar year of its start date, for example
`peninsula 1811`. The frame has 29 groups. Groups are mechanical and frozen. They are the held-out
units of any rating run and the batches of first-pass research.

## 7. Cohort v1

The first research cohort is every in-frame land entry whose start year is 1805–1815: **325 entries in
16 campaign groups.**

| Group | Entries | Group | Entries |
| --- | --- | --- | --- |
| third-coalition 1805 | 22 | peninsula 1810 | 11 |
| third-coalition 1806 | 4 | peninsula 1811 | 19 |
| fourth-coalition 1806 | 23 | peninsula 1812 | 8 |
| fourth-coalition 1807 | 19 | russia-1812 1812 | 31 |
| peninsula 1808 | 17 | peninsula 1813 | 12 |
| fifth-coalition 1809 | 36 | liberation 1813 | 52 |
| peninsula 1809 | 19 | liberation 1814 | 34 |
| peninsula 1814 | 3 | hundred-days-1815 1815 | 15 |

Side A in the cohort:

- named French troops: 300;
- the ally table: 22;
- overrides: 3.

Four cohort entries are surrenders "ohne Schwertstreich" (Spandau, Stettin, Küstrin and Nienburg,
1806). Research proceeds by complete campaign group.

## 8. Overrides

[`frame-overrides-v1.json`](../data/napoleonic/frame-overrides-v1.json) holds:

- the head correction for pp. 489–490;
- 15 entry overrides, each with its reason:
  - two misprinted years, checked on the page images: Pojano printed "1905" (B367b) and Peterswalde
    printed "1809" (B459a), restored to 1805 and 1813;
  - Condé's winner (B296b);
  - Lemnos and Copenhagen, outside the frame;
  - the five war corrections of section 4;
  - the three Neapolitan entries of 1815.

An override without a reason, or one naming an unknown entry, stops the build.

## 9. Limits

- **Selection.** Bodart's own rule selects the frame: consequences, or at least 2,000 combined losses.
- **Strengths.** Bodart's strengths are forces available for the battle and are rounded up. They are
  one source among several, not the strength answer.
- **Winners.** Bodart's winner is his judgment, and it is frozen. Indecisive battles follow his stated
  rule. Disputes are recorded, not resolved, in the frame.
- **Wars and sides.** Wars come from running heads, checked by belligerents. Side A for 30 entries
  without named French troops rests on the ally convention or on overrides; each is listed.
- **Extraction.** Force, commander and figure texts are mechanical extracts of the transcription. The
  derived fields were primary-verified as follows:
  - every in-frame entry's nations, side A and war were reviewed in a full listing;
  - the cohort's force and commander texts were reviewed in a full listing.

  The extracts are conveniences. Dossiers cite the printed entry.
