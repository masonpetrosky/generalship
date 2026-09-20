# Agate dispatch and the later 46th Ohio overnight account, v1

Prepared 2026-09-20 against preservation base `798b5c5cc152ba6561b6f5565e5e623db1a31442`.
This is an additive research comparison, not a dossier revision or feature admission.

Historical reprints provide an inspectable April 9 dispatch, but the original
*Cincinnati Gazette* issue has not been obtained. The opening reports Saturday
skirmishing without supplying the B/K overnight story later printed in Reid's
*Ohio in the War* II p.286. It therefore does not identify that story's original
witness, picket post, or a continuous firing chain into Sunday. The absence is
bounded to the five opening pages inspected here, not the entire dispatch or
all Reid papers, and does not refute the later account.

## What was inspected

- Frank Moore, editor, *The Rebellion Record*, fourth volume, G. P. Putnam,
  New York: **1864 title imprint**, despite the Internet Archive catalog's 1862
  date and the running headers' 1862. Retained title and Documents pp.385–389,400
  (one-based PDF pages 13,525–529,540). Page 385 begins “Cincinnati Gazette
  Account”; p.400 ends with “Agate.” The intervening pp.390–399 were not visually
  collated; no full-article fidelity or exhaustive absence claim is made.
- Ledyard Bill, compiler, *Pen-pictures of the War*, New York, **1864 title
  imprint and copyright**: retained title, verso and p.258 (PDF pages 9,10,264).
  Its heading credits J. Whitelaw Reid and dates the text April 9, 1862.
- Reused Reid II p.286 facsimile and the frozen `p286-saturday-night` section
  in `reid-1868-regimental-posts-v1`.

The [research record](../../design/shiloh-agate-comparison-v1/research-record.json)
binds **5 assertions, 16 passage anchors / 12 distinct source-section pairs**,
11 new selected historical text sections, one reused section and **11 inspected
page images** (10 new). Every passage has a source ID, section/page locator,
raw SHA-256, source-metadata SHA-256 and facsimile links. Whole downloaded PDFs
are held in task scratch; their hashes and origin URLs bind the selected images
in the registry and [search log](../../design/shiloh-agate-comparison-v1/search-log.json).
No model recollection or modern transcription supplies assertion text.

## Findings and limits

| ID | Inspected evidence | Supported conclusion and limit |
| --- | --- | --- |
| AG01 | `moore-agate-dispatch-v1`: `p385-heading`, `p385-opening`, `p400-signature`; `bill-reid-dispatch-v1`: `p258-heading`, `p258-opening`; title/verso images | The Gazette/Agate account and Reid-attributed opening share distinctive wording. This supports the identification of the dispatch in these reprints, not original newspaper fidelity, publication date or independent corroboration. |
| AG02 | Moore `p386-method`, `p386-warning` | The author says he combined observation with testimony and was at Crump's on Sunday morning before traveling upstream after hearing fire. This is self-reported method/location; it does not establish personal observation of the 46th Ohio pickets or name the later account's informants. |
| AG03 | Moore `p386-friday-saturday` | An April fourth skirmish is followed by a night without further demonstration, then more skirmishing on Saturday. In this sequence the quiet night is Friday night. It supplies no closure of Saturday-night contact, exact Saturday clock, post, duration or firing continuity. |
| AG04 | Moore opening pp.385–389, especially `p386-friday-saturday`, `p388-regiment`, `p388-dawn`; Reid `p286-saturday-night` | The dispatch opening names the 46th Ohio in McDowell's brigade and separately describes Prentiss/Hildebrand pickets at dawn. It supplies no B/K constant overnight feeling or sunrise cavalry-officer narrative in these five pages. Membership and generic skirmishing cannot establish the later story's provenance or same-post identity. |
| AG05 | Bill `p258-opening`, `p258-warning`; Moore `p386-method`, `p386-friday-saturday` and page context | Bill moves directly from the matching opening to the Sunday-morning account, omitting intervening material present in Moore. This is a local omission relative to Moore, not proof of the direction of copying or a complete collation. |

The dispatch's April 9 dateline is kept distinct from the two reprints' 1864
publication year, event dates and command knowledge. Moore prints month/day;
the normalized `1862-04-09` document date uses the report context and Bill's
explicit matching date. Moore p.386 also describes writing within twenty-four
hours of the close of the fight. These statements remain as printed; no actual
composition hour is inferred or the dateline silently changed. The following
Hurlbut report on p.400 is a separate document with its own April 12 date.

The two reprints and Reid's later compilation remain conservatively grouped in
`reid-ohio-in-war`. This does not prove that one copied another or that the same
informant supplied both texts. It prevents reprints of one account from counting
as new independent witnesses. The dispatch's force estimates, rhetoric, tactical
judgments and reported clocks are not validated or admitted by this comparison.

## Search boundary and next evidence

The original newspaper issue and manuscript remain uninspected. Modern search
leads point to *Cincinnati Gazette* April 14, 1862 and a *Mishawaka Enterprise*
April 26 reprint; these are **discovery leads, not verified issue dates**. A separate
web lead has an April 8 / via Cairo April 11 dateline and different opening;
its relationship to this April 9 account is unresolved. Archive.org Gazette
items inspected in metadata proved to be 1863/1865 issues. Direct LOC and Oregon
newspaper search endpoints returned HTTP 403. No archive outreach or purchase
was made. The search log separates these leads from retained assertion evidence.

The useful next action is to seek an inspectable original Gazette issue or the
named contemporary newspaper reprint, then compare the dateline, signature,
prebattle paragraphs and omissions before calling the original recovered.
The manuscript contributor behind Reid II p.286 remains a separate open lead.

## Preservation and model coverage

All **164 prior source entries / 161 raw paths** and **141 protected files** are
bound for preservation; nothing in a prior research or review bundle is rewritten.
Twelve new registry entries bring the total to **176 entries / 173 raw paths**.
The new offline [reference audit](../../design/shiloh-agate-comparison-v1/reference-audit.py)
checks source bindings, dates, coverage, preservation and admission invariants.

The Shiloh dossier stays at **62 claims / 40 quantities / 26 events**, including
three unknown claims, and the project retains three draft dossiers. The frame
stays **127 engagements / 36 campaigns**; admission v1 remains **18 blocked /
22 excluded**, v2 **7 blocked / 33 excluded**, with zero complete, emitted or
promoted rows. The baseline remains **23 engagements / 13 eligible groups**,
Brier **0.2768816348133779**, worse than equal odds **0.25**. No historical
feature, causal effect or commander ranking is validated by this source work.

Separate review is pending at preparation. Its actual response and primary
assessment will be retained separately; no independent review is asserted here.
