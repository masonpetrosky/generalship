# Cockpit Point: bounded first pass

Prepared 2026-09-20. [VA100](../../data/evidence/VA100.json) is the sole frozen
engagement in **Blockade of the Potomac River [October 1861-January 1862]**.
The new draft has **10 claims across all seven dimensions**, including **three
explicit unknowns**: opening personnel, combat logistics and contemporary information.
Separate campaign review is pending. No model feature is admitted.

Coverage becomes **7/127 draft dossiers**, **120 without a dossier**, and **2/36
source campaigns with every member represented**. Dossier presence, source review
and historical adjudication are different measures. Previous dossiers remain unchanged.

## Evidence and limits

One retained source family, **NPS/CWSAC**, supports this pass: the pinned Arnold
battle/force/commander rows, the current NPS battle detail, and the Cockpit Point
section of NPS's Potomac Heritage history page. These are related government
summaries, not independent corroboration. Four new source records retain two HTML
parents and their normalized text selections under `data/raw/cockpit-point-v1/`.
The [registry](../../data/sources.json) now has **188 entries / 185 raw paths**;
all previous 184 entries and 181 raw paths are preserved.

Both retained text selections were read in full. Text was extracted with the
registry's documented HTMLParser transformation and checked against the saved
HTML. No map, image, original report or print facsimile was inspected. The Potomac
page's displayed September 30, 2025 update date is metadata, not the date of the
historical events or of an underlying contemporary document. Source document
dates remain null. The exact sources, URLs and SHA-256 hashes are in the registry.

The single targeted Navy-history follow-up sought a separate account of the
January action, vessel roles and the later March operation. Anacostia's attempted
DANFS URL was inaccessible through the web tool. Yankee's DANFS page appeared in
search results, but opening it timed out; direct retrieval then failed certificate
verification in Python and returned HTTP 404 using curl with normal TLS checks.
No Navy text is retained as assertion evidence. Search snippets and other discovery
leads are not inspected original reports or additional source families. The attempted
URLs were `https://www.history.navy.mil/research/histories/ship-histories/danfs/a/anacostia.html`
and `https://www.history.navy.mil/research/histories/ship-histories/danfs/y/yankee-i.html`.
The original-report/crew-return search and separately authored scholarship are deferred.
The three-family ceiling is not a quota; this limited draft records what is known
from one family and stops without asserting independent confirmation.

## Interpretive boundaries

- Two gunboats and a battery garrison do not establish personnel counts. The
  pinned narrative's 37 heavy guns refer to the river-wide position in December,
  not a January 3 Cockpit Point census. No numerical strength is admitted.
- The live detail page has a zero force total with blank side values, an empty
  Description field and a campaign-like date span. Preserve these source defects;
  the frozen engagement remains January 3, 1862.
- Wyman and French are listed commanders, not automatically verified on-site
  decision makers or recipients of performance credit. Combat supply conditions
  and pre-action information remain unknown.
- The pinned result is **Inconclusive** and the live detail says **Indecisive**.
  The NPS narrative's unsuccessful effort to dislodge the batteries and the
  later March evacuation are separate propositions. March is contextual material
  beyond the frozen engagement and source campaign label; it does not turn
  January into a Union victory or add another modeled success.

The unchanged baseline still uses **23/127 engagements across 13 groups**, with
Brier **0.276882 versus 0.250000** for equal odds. The frozen cohort, six earlier
dossiers, all raw inputs and both admission proposals are unchanged; zero new
features or promoted rows result from this pass.

After one bounded source review, proceed to **Jackson's Operations Against the
B&O Railroad [January 1862]**, whose complete frozen membership is **Hancock
(MD001), January 5, 1862**. This is the earliest remaining group under the standing
chronological rule. No extra Cockpit Point investigation is required to move on.
