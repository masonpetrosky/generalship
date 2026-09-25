# Generalship

**An evidence-first research project for measuring historical command performance.**

The long-term aim is to compare what commanders accomplished with the opportunities
and constraints they faced, including the advantages they created before battle.
Every result should be traceable from commander to campaign to engagement to
disputed assumptions and supporting passages.

Inspired by [Ethan Arsht's military rankings](https://github.com/ethanarsht/military_rankings),
this project starts with a reproducible battle-level baseline, then builds toward
campaign-level contribution. A battle residual is **not** an estimate of how many
wins a commander caused. No validated commander ranking exists here yet.

## What works today

- A frozen **127-engagement / 36-campaign** American Civil War pilot, selected by
  dates and theaters before modeling, including defeats and inconclusive outcomes.
- Four pinned, checksum-verified CWSAC tables from Jeffrey B. Arnold's
  [American Civil War Battle Data](https://acw-battle-data.readthedocs.io/en/latest/).
- An offline import and audit pipeline: unique keys, referential integrity,
  dates, force ranges, missingness, outcome codes, and cohort membership.
- A small regularized logistic baseline using relative force size. Evaluation
  holds out whole campaigns and compares with equal odds and a training-only prior.
- One hundred ten draft dossiers, including all frozen East Tennessee Campaign records,
  with exact source passages, explicit unknowns, command questions, and
  inherited/created distinctions. See the [coverage table](artifacts/pilot-report.md#draft-evidence-dossiers).
- A [Shiloh research memo](docs/research/shiloh.md), original reports/orders, two
  independently authored histories, and return-table scans. The follow-up
  [Confederate return audit](docs/research/shiloh-confederate-returns.md) and
  [Union availability audit](docs/research/shiloh-union-availability.md), followed
  by the [Ohio reinforcement audit](docs/research/shiloh-ohio-reinforcements.md),
  bring it to 40 typed troop observations and 26 events, preserving population,
  timing, missingness and printed discrepancies.
- A reproducible report, battle predictions, exclusion reasons, research queue,
  and input/output hash receipt. No runtime dependencies beyond Python 3.11+.

## Run it

From the repository root:

```sh
make check                         # tests + source/evidence/pipeline validation
make reproduce                     # regenerate the committed artifacts offline
python3 -m generalship admission-check # offline proposal audit; no promotion
python3 -m generalship inspect TN003
python3 -m generalship packet TN003 # prepare a research assignment; makes no AI call
make review-bundle                 # frozen Shiloh sources/scans + reviewer prompt ZIP
```

`python3 -m generalship fetch` can restore missing pinned upstream CSVs. Normal
checks and builds make no network requests. The checked-in historical snapshots are
restored from Git, not silently refreshed. Run from another directory with
`python3 -m generalship --root /path/to/generalship check` when the package is on
the Python path. Optional editable installation: `python3 -m pip install -e .`.

## First result

Only **23 of 127 engagements** currently have two numerical force estimates and a
decisive result suitable for this baseline. The other engagements remain visible
in the research queue. Do not treat missing strengths as zero or invent them.

On those 23 engagements across 13 eligible campaign groups, the strength model's
held-out Brier score is **0.276882**, compared with **0.250000** for equal odds
(lower is better). This small, selected subset does not show an improvement over
equal odds. It motivates source enrichment and better evaluation; it does not
validate a ranking or prove force size is generally uninformative.

Read the [generated pilot report](artifacts/pilot-report.md) for coverage and
evaluation details. The live NPS Antietam page's zero-strength table and Shiloh's
changing forces/command illustrate why reliable dossiers come before new rankings.

## Research direction

**Current priority: comparable coverage across the 127 engagements.** We have
one hundred ten draft dossiers and 17 engagements without one. Shiloh's repeated source
traces are parked with their unknowns intact; its depth is not the template for
every battle. Use a bounded first pass of up to three source families and one
targeted follow-up, then move on and review by complete source campaign.

The [bounded river-campaign pass](docs/research/river-campaign-first-pass-v1.md)
adds Fort Henry, Fort Donelson and Corinth, carrying forward Shiloh unchanged.
The three new drafts passed separate Astra `xhigh` source review; no model inputs
are admitted. The [Cockpit Point first pass](docs/research/cockpit-point-first-pass-v1.md)
now covers the complete frozen Potomac blockade group. Astra `xhigh` accepted
all 10 new claims with no required corrections; one source family and three
unknowns remain explicit. The [Hancock first pass](docs/research/hancock-first-pass-v1.md)
adds 11 claims from two source families, retaining chronology and casualty disputes;
Astra `xhigh` accepted all 11 claims with no required corrections.
The [Eastern Kentucky pass](docs/research/eastern-kentucky-first-pass-v1.md) adds
Middle Creek and Mill Springs with 22 claims and three explicit unknowns;
Astra `xhigh` accepted all 22 claims with no required corrections.
The [Burnside campaign pass](docs/research/burnside-first-pass-v1.md) adds five
drafts with 47 claims, ten explicit unknowns and two source families per battle.
Astra `xhigh` accepted all 47 claims with no required corrections.
The [New Madrid/Memphis pass](docs/research/mississippi-joint-first-pass-v1.md) adds
two drafts with 21 claims, five explicit unknowns and two families per battle.
Astra `xhigh` accepted all 21 claims with no required corrections.
The [Peninsula pass](docs/research/peninsula-first-pass-v1.md) adds all sixteen
frozen records: 152 claims, 39 explicit unknowns and one or two families per record.
Astra `xhigh` accepted all 152 claims with no required corrections.
The [Valley pass](docs/research/valley-first-pass-v1.md) adds seven dossiers,
68 claims, 17 explicit unknowns and 91 citations. Astra `xhigh` reviewed the complete
batch; its one timing-tag correction is fixed and verified by the primary.
The [Heartland Offensive pass](docs/research/heartland-first-pass-v1.md) adds five
dossiers, 54 claims, 6 explicit unknowns and 157 citations. Opus 5.5 `high` reviewed
the complete batch; its one Perryville scope correction is fixed and verified by the primary.
The [Northern Virginia pass](docs/research/northern-virginia-first-pass-v1.md) adds six
dossiers, 56 claims, 7 explicit unknowns and 143 citations. Opus 5.5 `high` reviewed the
batch; its two locator/scope corrections are fixed and verified by the primary.
The [Maryland pass](docs/research/maryland-first-pass-v1.md) adds three dossiers
(Antietam's existing draft unchanged), 29 claims, 4 explicit unknowns and 86 citations.
Opus 5.5 `high` reviewed them; its four required corrections are fixed and verified by the primary.
The [Iuka and Corinth pass](docs/research/iuka-corinth-first-pass-v1.md) adds three
dossiers, 28 claims, 3 explicit unknowns and 91 citations. Opus 5.5 `high` reviewed the
batch; its eight required corrections are fixed and verified by the primary.
The [Stones River pass](docs/research/stones-river-first-pass-v1.md) adds two dossiers,
20 claims, 2 explicit unknowns and 79 citations. Opus 5.5 `high` reviewed both; its five
required corrections are fixed and verified by the primary.
The [Fredericksburg pass](docs/research/fredericksburg-first-pass-v1.md) adds VA028: 10
claims, 1 explicit unknown and 44 citations. Opus 5.5 `high` reviewed it; its seven
required corrections are fixed and verified by the primary.
The [Goldsboro pass](docs/research/goldsboro-first-pass-v1.md) adds three dossiers,
28 claims, 4 explicit unknowns and 75 citations. Opus 5.5 `high` reviewed them; its five
required corrections are fixed and verified by the primary.
The [Forrest West Tennessee pass](docs/research/forrest-west-tennessee-first-pass-v1.md) adds
two dossiers, 18 claims, 2 explicit unknowns and 72 citations. Opus 5.5 `high` reviewed them;
its three required corrections are fixed and verified by the primary.
The [Vicksburg 1862–63 pass](docs/research/vicksburg-1862-first-pass-v1.md) adds two
dossiers, 19 claims, 2 explicit unknowns and 69 citations. Opus 5.5 `high` reviewed them;
its six required corrections are fixed and verified by the primary.
The [Middle Tennessee pass](docs/research/middle-tennessee-first-pass-v1.md) adds five
dossiers, 46 claims, 7 explicit unknowns and 149 citations. Opus 5.5 `high` reviewed them;
its four required corrections are fixed and verified by the primary.
The [Tidewater pass](docs/research/tidewater-first-pass-v1.md) adds four
dossiers, 39 claims, 4 explicit unknowns and 194 citations. Opus 5.5 `high` reviewed them;
its five required corrections are fixed and verified by the primary.
The [Rappahannock cavalry pass](docs/research/rappahannock-cavalry-first-pass-v1.md) adds one
dossier, 9 claims, 1 explicit unknown and 78 citations. Opus 5.5 `high` reviewed it;
its four required corrections are fixed and verified by the primary.
The [Vicksburg 1863 pass](docs/research/vicksburg-1863-first-pass-v1.md) adds ten
dossiers, 92 claims, 10 explicit unknowns and 383 citations. Opus 5.5 `high` reviewed them;
its nine required corrections are fixed and verified by the primary.
The [Chancellorsville pass](docs/research/chancellorsville-first-pass-v1.md) adds three
dossiers, 27 claims, 3 explicit unknowns and 131 citations. Opus 5.5 `high` reviewed them;
its ten required corrections are fixed and verified by the primary.
The [Streight's Raid pass](docs/research/streights-raid-first-pass-v1.md) adds one
dossier, 9 claims, 1 explicit unknown and 49 citations. Opus 5.5 `high` reviewed it;
its three required corrections are fixed and verified by the primary.
The [Gettysburg Campaign pass](docs/research/gettysburg-first-pass-v1.md) adds ten
dossiers, 90 claims, 10 explicit unknowns and 336 citations. Opus 5.5 `high` reviewed them;
its eleven required corrections are fixed and verified by the primary.
The [Tullahoma pass](docs/research/tullahoma-first-pass-v1.md) adds one
dossier, 9 claims, 1 explicit unknown and 54 citations. Opus 5.5 `high` reviewed it;
its seven required corrections are fixed and verified by the primary.
The [Morgan's Raid pass](docs/research/morgans-raid-first-pass-v1.md) adds three
dossiers, 28 claims, 3 explicit unknowns and 149 citations. Opus 5.5 `high` reviewed them;
its five required corrections are fixed and verified by the primary.
The [Chickamauga Campaign pass](docs/research/chickamauga-first-pass-v1.md) adds three
dossiers, 27 claims, 3 explicit unknowns and 147 citations. Opus 5.5 `high` reviewed them;
its eight required corrections are fixed and verified by the primary.
The [East Tennessee Campaign pass](docs/research/east-tennessee-first-pass-v1.md) adds two
dossiers, 19 claims, 2 explicit unknowns and 80 citations. Separate review is pending.
Next: **the five-record Bristoe Campaign**. See the
[current roadmap](docs/roadmap.md) and
[first-pass protocol](docs/methodology.md#research-depth-and-coverage).
The history below preserves completed work and deferred questions.

The first [Shiloh research pass](docs/research/shiloh.md),
[Confederate return audit](docs/research/shiloh-confederate-returns.md) and
[Union availability audit](docs/research/shiloh-union-availability.md), and
[Ohio reinforcement audit](docs/research/shiloh-ohio-reinforcements.md) are complete
as drafts: 62 claims preserve competing returns, reinforcement phases, dated
orders and disputed responsibility. Nelson/Ammen and regimental reports now
separate crossing, landing, formation and participation. Conflicting clocks, the
untraced Sunday 600-person figure, mixed-date estimates and Reed's 7,553/7,552
discrepancy remain explicit alongside earlier source disputes. No canonical
opening strength or adjudicated command attribution has been established. A
fresh-context GPT-6 Astra `xhigh` [source review](artifacts/review-results/TN003-a42f063-astra-xhigh-v1/review.md)
checked all 62 claims, 40 quantities, 26 events and 26 supplied scan selections.
The [primary assessment](artifacts/review-results/TN003-a42f063-astra-xhigh-v1/primary-assessment.md)
accepts four findings for a versioned correction pass: estimation provenance,
section-specific document dates, same-return dependence and Crittenden arrival
wording. The [versioned correction pass](docs/research/shiloh-review-corrections.md)
implements them with dossier schema v3 and three source-metadata revisions.
The focused review and validator follow-up are accepted. Thirty-five of 65 cited source/section
pairs remain text/CSV-only. The [prepared packet](artifacts/research/TN003.md)
and [dossier](data/evidence/TN003.json) preserve the open questions. Expand by complete
campaign, retaining ordinary engagements and failures in the frame.

The [self-contained review handoff](docs/research/shiloh-review-handoff.md) preserves
the frozen assignment separately from the actual response and execution record.
The default reviewer is a fresh-context Claude Opus 5.5 `high` subagent in the same
task, under [AGENTS.md](AGENTS.md); it replaced GPT-6 Astra `xhigh` on 2026-09-24,
and earlier Astra reviews keep their recorded scope. No manual chat handoff is required. This AI
review fulfills the bounded separate-review step, not historical adjudication or
feature admission. The [feature-admission design](docs/feature-admission.md) now
has a separate Astra `xhigh` design review with no required corrections. Its
[13 Shiloh examples](docs/research/shiloh-admission-examples.md) preserve source
versions, population, time and estimand restrictions. They emit no features.
The [review and primary assessment](artifacts/review-results/feature-admission-838189f-astra-xhigh-v1/primary-assessment.md)
record the exact scope and remaining historical limits.

The [offline admission validator](docs/admission-validator.md) is implemented,
with Astra `xhigh` implementation review and focused follow-up accepted. The
[review record](artifacts/review-results/admission-implementation-1264e21-followup-v1/primary-assessment.md)
preserves three findings and their verified fixes. Its complete-frame ledger checks all
40 Shiloh troop observations: 18 blocked, 22 excluded and zero complete rows.
No model inputs are promoted. Actual feature release still requires reviewed
boundary/population mappings and a separate immutable admission manifest.

A separate [opening-boundary and population proposal](docs/research/shiloh-opening-boundary-v1.md)
now uses 51 pinned passage anchors to revisit the 18 blocked observations. Its
explicit v2 ledger has **7 blocked / 33 excluded**, with no complete rows;
the default v1 ledger is preserved. The first-contact identification, mapped
area and full populations remain unresolved. Astra `xhigh`
[accepted the bounded proposal](artifacts/review-results/shiloh-opening-330599b-astra-xhigh-v1/primary-assessment.md)
with one nonblocking precision clarification; no historical feature is admitted.

The [contact-and-location packet](docs/research/shiloh-contact-location-v1.md)
adds nine participant opening accounts, 16 inspected book-page facsimiles and
two maps. It preserves conflicting contact clocks, earlier skirmishes and map
phase limits. The separate Astra `xhigh` review found two literal transcription
errors, now [corrected in new source versions](docs/research/shiloh-contact-location-corrections-v1.md)
with primary verification. The dossier and model inputs remain unchanged.

The [April 3–5 contact-chain audit](docs/research/shiloh-precontact-segmentation-v1.md)
recommends April 3–4 as precursor encounters under an explicit continuity rule,
with weaker event-specific closure for April 3.
The Saturday Howell link remains unresolved; no complete opening boundary or
new feature is admitted. Ten assertions bind 24 passages across 19 inspected pages.
Separate Astra `xhigh` review found one finding with two literal wording errors,
now [corrected in a new source version](docs/research/shiloh-precontact-segmentation-corrections-v1.md)
and closed by primary image verification.

The [Howell attribution trace](docs/research/shiloh-howell-trace-v1.md) now finds
Medkirk's retrospective Saturday account and disputed testimony selections in
Worthington, and verifies Reed's clause in the 1903 printing. Seven assertions
bind 14 passages across 12 inspected pages and three HTML sources. The source
chain to Reed and Saturday-to-Sunday continuity remain unknown.

Separate Astra `xhigh` [review and primary assessment](artifacts/review-results/shiloh-howell-67b5c30-astra-xhigh-v1/primary-assessment.md)
accepted the bounded Howell packet with no required corrections; historical
provenance and continuity questions remain open.

The [regimental and post comparison](docs/research/shiloh-regimental-posts-v1.md)
adds Reid's report of overnight activity at an unnamed 46th Ohio picket line,
Lemmon's 72d account, Worthington's post relationships and the map cited by Medkirk.
The map depicts April 6–7 phases, not Saturday's post sequence. Seven assertions
bind 21 anchors across 16 inspected pages; the registry has 151 entries / 148 raw
paths at preparation. Post identity and continuity remain unresolved, with zero feature admission.

Separate Astra `xhigh` review covered the full packet and found two literal map
transcription errors, now [corrected in a new version](docs/research/shiloh-regimental-posts-corrections-v1.md)
and closed by primary image verification. The registry at that stage is 152 entries / 149
raw paths; the historical conclusions and model inputs are unchanged.

The [Reid provenance trace](docs/research/shiloh-reid-provenance-v1.md) identifies the publisher collection process and Miller's general editorial role, but no original 46th Ohio witness. Lindsey supplies a later wording parallel with independence unestablished. Five assertions bind 11 anchors / 10 source-locator pairs, ten retained page images and one text-only LOC catalog snapshot. All earlier evidence is preserved; the registry at that stage has 164 entries / 161 raw paths and zero feature admission. Separate Astra `xhigh` [review and primary assessment](artifacts/review-results/shiloh-reid-1c498e0-astra-xhigh-v1/primary-assessment.md) accept all five bounded assertions with two nonblocking catalog clarifications: use the retained Agate letters label and provider page/line locators; material format and printed pagination remain unverified.

The [Agate comparison](docs/research/shiloh-agate-comparison-v1.md) locates two historical reprints with 1864 title imprints, supporting a Reid/Agate account dated April 9, 1862. Its inspected opening reports Saturday skirmishing but does not supply the later B/K overnight narrative or identify its witness/post. The original Gazette issue remains uninspected. Five assertions bind 16 anchors / 12 source-section pairs across 11 inspected images; the registry at that packet has 176 entries / 173 raw paths, with zero feature admission. Separate Astra `xhigh` [review and primary assessment](artifacts/review-results/shiloh-agate-73e26d4-astra-xhigh-v1/primary-assessment.md) accept all five bounded historical assertions; the sole documentation inventory finding is corrected and closed by primary verification. The original issue, overnight witness and continuity remain unresolved.

Then define a campaign replacement boundary and outcomes before fitting enriched
models. Battle execution and campaign contribution are separate estimands; adding
them together would double count. Partial pooling, opponent/army context,
measurement uncertainty, disputed-input scenarios, and a source-exploration UI
remain planned work, not implemented capabilities.

## Read next

- [Methodology and limitations](docs/methodology.md)
- [Evidence contract and review workflow](docs/evidence-contract.md)
- [Reviewed feature-admission design](docs/feature-admission.md)
- [Source provenance and original-project audit](docs/sources.md)
- [Milestones and next tasks](docs/roadmap.md)
- [Source manifest](data/sources.json) and [frozen cohort](data/pilot/cohort.json)

Project code is MIT-licensed. Third-party data retains its own terms and attribution;
see [NOTICE](NOTICE.md). No paid services, scheduled jobs, or hosted CI are needed.
