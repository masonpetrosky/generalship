# Operations Near Cache River (1862): bounded first pass

Prepared 2026-09-25 under the full-war research frame ([cohort v2](../cohort-v2.md)). The single
**frozen record** in **Operations Near Cache River, Arkansas [July 1862]** now has a draft
dossier: **9 claims, 1 explicit null unknown and 47 citation occurrences**. All seven dimensions
are represented. The dossier is a draft; no features are admitted.

| Record | Dates (frozen) | Claims | Unknowns | Citations | Families |
| --- | --- | ---: | ---: | ---: | ---: |
| AR003 — Hill's Plantation (Cache River) | 1862-07-07 | 9 | 1 | 47 | 3 |

Drafted alongside the [White River](white-river-1862-first-pass-v1.md) and
[Boston Mountains](boston-mountains-1862-first-pass-v1.md) passes. Existing dossiers, reviews and
historical revisions are unchanged. Dossier presence is not first-pass acceptance, separate
review or model eligibility.

## Inspection and stopping record

Read the frozen battle, force and commander rows and the retained NPS page in full. The live page
labels the campaign "Operations Near Cacke River Arkansas" and styles Hovey and Hindman Brigadier
General; neither is adopted. NPS/CWSAC and the Arnold tables are one family. The OR Volume XIII
parent is registered with the Boston Mountains pass. The Hill's Plantation report list (Nos. 1–6)
was read.

- **Hovey** (`hovey-cache-river-1862-report`): July 7, 1862 report, No. 4 (pp.143–145), read in
  full. The compiled return that follows was not selected.
- **Hindman** (`hindman-mclemores-cove-reports`, the author's existing group): general report dated
  Richmond, June 19, 1863. Selected: the heading (p.28), the Saint Charles passage (pp.34–36; used
  for AR002) and the passage from June 24 to Curtis's arrival at Helena (pp.36–37). Hindman was not
  on the field and says no report of the affair was ever received. The intervening paragraphs on
  p.36 were read and not selected. pp.29–33 and 38–44 were not read beyond their first lines.

The following were read but not selected: Curtis's No. 1 report on the action.

Not inspected:

- Steele's, Benton's, Baker's and Wood's reports;
- the compiled Union return;
- any Rust or Parsons report (Hindman says none was received);
- maps.

No targeted follow-up was used. Stop after this batch.

The pass adds **4 source records**:

- one NPS HTML/text pair;
- two OR XIII selections (Hovey, Hindman). The Hindman selection also serves AR002.

## Decisions and limits

- **Scope.** Curtis's march to Helena and the Round Hill and Bayou De View skirmishes are context.
- **Opening strength remains unknown.** The frozen bounds are blank and the live field reads zero.
  The inspected figures are:
  - Hovey: a little less than 400 with Harris, joined at the close by about 200 cavalry, against
    about 2,000 Texans with a larger reserve under Rust;
  - Hindman: Rust's whole command at about 5,000 effectives. This is not an engaged count.

  None is adopted.
- **Disputes preserved.**
  - Losses: frozen 308 (US 63; CS 245) against live 313 (US 63; CS 250). Hovey's 6 killed and 57
    wounded sum to 63 (a computation). His 123 Confederate dead found and the prisoners' estimate
    of over 200 dead match neither CS figure.
  - Duration: Hindman's "about thirty minutes", secondhand, stands against Hovey's longer
    narrative, which gives no clock time.
- **Command roles.**
  - Hovey directed the reconnaissance and the corn-field stand, and Benton led the pursuit.
  - Hindman held district command at a distance.
  - Both sources name Rust, who is not a listed commander, on the field. Parsons is not named for
    July 7 in the inspected passages.
  - No listed commander receives automatic sole credit.
- **Tags.** All claims are `unresolved` or `post_outcome`.

The null unknown is the opening strength. No morale/readiness score, probability, causal effect or
new commander ranking is introduced. The cohort, admission proposals and baseline are unchanged,
with zero promoted rows.

## Validation

`python3 -m generalship check` passes. Every quote occurs in its cited section, and `gs.MISSES` is
empty. `python3 -m unittest discover -s tests` passes (134 tests).

## Separate review

Pending. No review is claimed.
