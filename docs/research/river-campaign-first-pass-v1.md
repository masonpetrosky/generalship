# Cumberland and Tennessee river campaign: bounded first pass

Prepared 2026-09-20. Three new **drafts** complete dossier presence for all four
engagements in the frozen source campaign **Federal Penetration up the Cumberland
and Tennessee Rivers [February-June 1862]**. Shiloh is carried forward unchanged.
This does not establish historical completeness, comparable research depth,
feature eligibility or campaign success. Separate campaign review is pending.

| Engagement | Claims | Explicit null claims | First-pass source families |
| --- | ---: | ---: | --- |
| [Fort Henry, TN001](../../data/evidence/TN001.json) | 10 | 1 | NPS/CWSAC; Grant memoir |
| [Fort Donelson, TN002](../../data/evidence/TN002.json) | 11 | 1 | NPS/CWSAC; Grant memoir |
| [Shiloh, TN003](../../data/evidence/TN003.json) | 62 | 3 | Prior dossier/reviews retained; no new research |
| [Corinth, MS016](../../data/evidence/MS016.json) | 12 | 2 | NPS/CWSAC; Grant memoir |

All seven dimensions appear in each new draft. Opening strength remains explicitly
unknown for all three; Corinth also leaves Halleck's contemporary information set
unknown despite retaining Grant's recalled warning. Supported claims are attributed
source assertions, not historical adjudication. Null boundaries and prose estimates
supply no predictors. Overall coverage is **6/127 drafts**, **121 without dossiers**.
This is the first complete frozen campaign with dossier presence (1/36); review
coverage and model eligibility must be counted separately.

## Sources and inspection

The [registry](../../data/sources.json) binds eight new records under
`data/raw/river-campaign-v1/`: four retained HTML downloads and four text snapshots.
All 176 previous entries and 173 raw paths are preserved; totals are **184/181**.

- **NPS/CWSAC:** inspected all three current NPS detail summaries and the matching
  pinned Arnold battle rows. HTML/text pairs and the CSV share `nps-cwsac`.
  Page dates display February–June 1862, a campaign-like span; every strength table
  displays zero. Henry/Donelson rank fields also conflict with the Brigadier General
  wording in their narratives. These fields do not establish event timing or rank.
- **Grant memoir:** inspected 24 retained full paragraphs in chapters XXI, XXII and
  XXVI of Project Gutenberg eBook 4367. Section IDs record zero-based local
  p/h1/h2/h3 extraction indices, not printed page numbers. Whitespace is normalized;
  quotes are checked within individual sections. The downloaded book is retained
  with its header/license, but full-book inspection is not claimed. The memoir's
  chapters and Grant's existing report share `or-grant`; no extra independent
  witnesses are created. Chapter composition dates and original print pagination
  remain unverified. The preface date is not assigned to the narrative.

All new inspection is **digital text only**. No facsimile, terrain map, separately
authored modern scholarship or original wartime report is claimed as inspected in
this pass. Grant is an interested retrospective participant whose judgments about
morale, opponents and counterfactual victories are not adopted. Counting two
families does not prove they are historically independent.

## Per-battle stopping record

| Battle | Consequential gap and one targeted follow-up | Result and deferred work |
| --- | --- | --- |
| TN001 | Tried eHistory's OR VII p.137 lead for Tilghman's report to clarify garrison versus rear guard | Page inaccessible in the web tool; no report passage retained. Opening membership and print confirmation deferred. |
| TN002 | Tried eHistory's OR VII p.159 lead for Grant's report to clarify force timing | Page inaccessible in the web tool; no report passage retained. Matched opening counts and original orders deferred. |
| MS016 | Checked the current NPS Corinth I detail against the pinned row's dates, missing strength and raid wording | Current page gives campaign-like dates, zero troops and a siege/evacuation narrative. Opening grain and the inherited wording remain unresolved. |

The unsuccessful report URLs were `https://ehistory.osu.edu/books/official-records/007/0137`
and `https://ehistory.osu.edu/books/official-records/007/0159`. They are discovery
leads only: their page contents, report attribution and completeness were not
verified. The retained source URLs and hashes are in the registry. Searches and
uncited discovery snippets are not additional assertion evidence. The three-family
ceiling is not a quota; two retained families suffice to record a bounded draft.
No further first-pass source chase follows from these open questions.

## What the drafts preserve

- **Henry:** Grant's proposed 17,000-person expedition, approximately 2,800 in the
  fort/camp and roughly 100 left at the guns refer to different populations. Flooded
  terrain, transport constraints and joint naval/army roles remain attributed.
- **Donelson:** the 15,000-person marching column, 27,000 reported at the fall with
  road guards, and 12,000–15,000 recalled surrender estimate cannot become one
  opening-strength range. Grant's contextual 21,000 enemy reconstruction uses
  prisoners, casualties and escapes; it is not a directly observed opening return.
- **Corinth:** Grant distinguishes a retrospective roughly 50,000 effective enemy
  estimate from a reported 70,000 estimate and a rounded 120,000 Union total. His
  formal second-in-command title and claimed limited practical authority remain
  distinct. His uncertain late-May warning does not prove Halleck received it.

The live/pinned casualty summaries also differ: Henry 146 versus 119, Donelson
19,832 versus 17,398, and Corinth 2,000 versus unknown. These are observations of
source fields, not reconciled casualty populations or model inputs. The frozen
Corinth row's April 29–June 10 interval may include pursuit; Grant describes the
pursuing column returning June 10, but the table's rationale is unestablished.
Its “although the raid ultimately failed” wording remains an unexplained source
issue. No silent repair or substitution of the October Corinth battle occurs.

## Review, preservation and next action

One fresh-context Astra `xhigh` campaign review will inspect all **33 new claims**
and their retained source context, and verify preservation of the fourth dossier.
The new review does not re-review all 62 Shiloh claims; its earlier review records
remain the evidence for their stated scopes. Correct extraction defects without
opening new historical investigations. All dossiers remain drafts after AI review.

The frozen cohort, Shiloh dossier, both admission proposals and baseline must remain
byte-identical. Baseline eligibility stays **23/127 across 13 groups**, Brier
**0.276882 versus 0.250000** for equal odds; zero historical features are admitted.

After review, proceed to the earliest remaining complete source campaign:
**Blockade of the Potomac River [October 1861-January 1862]**, containing **Cockpit
Point (VA100)**. Preserve all campaign groups regardless of outcome or fame.
