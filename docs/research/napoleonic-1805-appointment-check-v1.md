# 1805 German-command appointment and objective check v1

Primary-verified source check, 2026-10-20. The owner accepted a bounded examination
of the [existing campaign pilot](../../data/napoleonic/methods-v1/campaign-pilot.json)
against its pinned pre-operation material. The target remains the French overall
command in the German operations; this is not a new campaign sweep or rating run.

**Result: earlier operational direction and stated aims are recoverable, but the
imperial appointment comparison remains not estimable.** The sources distinguish
preparation orders, Murat's reported lieutenant appointment and specific task
orders, public aims, and the Emperor's announced personal presence. They do not
provide one interchangeable command-start date, a complete assigned objective
vector or an eligible replacement pool under the same authority.

The new [source supplement](../../data/napoleonic/appointment-check-v1/record.json)
preserves **nine passages in seven contexts from one existing source family**,
with exact quotes, source/metadata hashes, character and line locators, English
interpretations and use limits. The frozen methods pilot, dossiers, source
registry and prepared packets retain their bytes. Its original nulls are not
silently filled, and no model input is admitted.

## Scope and stopping rule

Use the existing Alombert and Colin family, `alombert-colin-1805`, specifically
the retained tome-II parent `alombert-colin-t2-ocr-v1`. Read its earlier
preparation/order contexts and make one targeted follow-up for the decisive
appointment/mandate gap. That follow-up checks the nomination/general-command
wording, Murat's immediate letter context and relevant task/title/personal-command
contexts. Stop here. Three families is the existing ceiling, not a quota: no
second family or new fetch was needed for this scoped check.

The current numerical partition remains **273 development entries in 13 groups**
and **52 reserved-final entries in three groups**. This is one source-check case
within the development group's existing pilot, not a replacement engagement
cohort or a corpus-wide estimate of evidence yield. No final-reservation dossier
or outcome feedback selects the findings.

The parent is a French official history printing earlier documents, not an
original order book inspected in an archive. Multiple letters in it are not new
independent source families. The older October local directives were re-read
through the frozen pilot as context; no new passage from them is adopted here.
Tome-II keyword results and selected surrounding blocks are not a complete
reading of that volume or a demonstration that the wider literature is silent.

## What the pinned material supports

All passage IDs below refer to the supplement. Line locators are one-based in
the exact pinned OCR; character ranges are zero-based, half-open Unicode
character indices. They do not assert verified printed page numbers.

| Evidence | Narrow supported observation | Limit for the proposed comparison |
| --- | --- | --- |
| `p001`, lines 364–366, introductory narrative | The historians report an August onset of movement toward the Rhine. | A retrospective movement marker is not a formal appointment, earliest authority or an inherited-resource boundary. |
| `p002`, lines 12587–12596, Emperor to Berthier | An order requests an organized representation of Austrian troops/armies. | Direction to collect/organize information is not the information actually received or a replacement opportunity. |
| `p003`–`p004`, lines 7863–7870 and 7887–7890, another Emperor–Berthier letter | Route direction for Marmont and biscuit/provision preparation at Würtzbourg, with speed of operations as a stated purpose. | Proposed routes, arrival and supply are not observed execution, an achieved advantage, a usable resource total or the full campaign objective vector. These clips belong to one letter. |
| `p005`–`p006`, lines 18376–18378 and 18394–18397, Murat to Berthier | Murat reports being named lieutenant to command in the Emperor's absence, then asks whether he should attend to other corps' cantonments and actually take general command. | Nomination and an explicit scope question coexist. No affirmative reply, original grant or effective handover is supplied by these adopted clips. They are from the same letter. |
| `p009`, lines 19921–19928, Murat to Leval | Murat directs cavalry movement orders and surveillance around specified Rhine positions and the Basel bridge. | Positive task direction must be retained; it does not establish unrestricted general authority, execution, a local people count or earliest appointment. Regimental identifiers are not headcounts. |
| `p007`, lines 28415–28417, speech to the Senate | The Emperor announces an intention to head the army, help allies promptly and defend his peoples' interests. | These are public stated aims and rationale, not proof of execution, an externally assigned measurable objective vector or an appointment instrument. |
| `p008`, lines 48400–48403, corps order | The order announces the Emperor's arrival at Strasbourg and that he comes to take personal command. | A personal-presence announcement does not establish his earliest superior authority, a precise transfer from Murat or a boundary before preparation. |

The most consequential finding is the combination of `p005`, `p006` and `p009`.
It would be wrong to read only the appointment language and install Murat as
unrestricted commander. It would also be wrong to use his question as proof
that he exercised no authority: the task order is positive evidence of reported
direction. Under [command-unit specification v1](../napoleonic-command-units-v1.md),
these are scoped authority observations with a still-unresolved general mandate.
They are not a global person/army mapping or an automatic alternative incumbent
for the original imperial target.

Similarly, `p002`–`p004` establish reported imperial direction in material presented
as August/September, before the existing October local-order examples. They do
not establish the first day that authority began. Choosing the later arrival or
personal-command announcement as campaign t0 would leave earlier imperial
preparation outside the comparison and could treat its results as inherited.
This is a methodological consequence of the observed role distinctions, not
a new causal estimate of what that preparation accomplished.

## Dates, source roles and objectives

**All new normalized document dates, event times and command-receipt times remain
null.** The supplement preserves literal OCR headings. Some digits are visibly
corrupt, including a year rendered `105` and another rendered `1895`; neither is
silently repaired from historical familiarity. Running-page digits are also
unreliable. No new facsimile was inspected. The exact source-character/line
locators and hashes make these text readings inspectable without presenting them
as image-verified chronology.

An order's document heading, a narrated earlier arrival and the effective
assumption of authority are different referents. Even a later image check of a
heading would not, by itself, establish appointment or transfer time. Original
orders/appointment instruments behind this edited history remain uninspected.
The source snapshot preserves its original metadata/inspection note; the new
supplement records the additional reading rather than rewriting that note.

The speech supplies two reusable public aims: prompt help to allies and defence
of the peoples' interests. The supply order supplies a narrower operational
purpose. None is discarded merely because it is public or issuer-stated. Their
timing, measurability and relationship to the proposed replacement boundary are
not yet established, and they do not enumerate the complete German campaign's
assigned objectives or opportunity set. Do not turn subsequent battle results
into prior objectives or assume that every aim stated by the incumbent was an
inherited constraint at campaign onset.

## Remaining mapping and research decision

| Required field/use | Disposition after this check |
| --- | --- |
| Reported superior operational direction | Supported as scoped source observations, `p002`–`p004`. |
| Public stated aims | Retained as issuer-stated rationale, `p007`; complete assigned campaign-objective vector remains null. |
| Murat's lieutenant role | Reported nomination and task direction, `p005`/`p009`, with the explicit general-scope question in `p006`. Original grant and effective start/end remain null. |
| Imperial appointment start and comparison t0/t1 | Unestablished. No conventional boundary is selected in this check. |
| Eligible replacements under the same authority | Null. A printed marshal or lieutenant role does not make someone eligible to replace the Emperor under unchanged authority. |
| Inherited resources/information and non-battle opportunities | Not reconstructed. A preparation directive is not an inherited total or proof of receipt. |
| Persistent army/person IDs, feature admission and contribution estimate | No new mapping/admission; contribution estimate remains null and `estimable` is false. |

The distinction between an imperial overall command and a delegated military
appointment matters for the counterfactual. These documents combine military
direction with the Emperor's own public policy statement. **The inference is
methodological:** a replacement contrast must say which authority is retained
and replaced; it cannot quietly use an ordinary marshal pool as though political
and superior military authority were already held fixed. The sources inspected
here do not establish such a pool. This is not a claim that an imperial-command
counterfactual could never be defended.

Stop the present imperial-pilot check here and retain its not-estimable result.
**Recommendation: make any next pilot a separately specified delegated
operational appointment.** Murat's lieutenant role is a concrete candidate
because the sources report nomination and contain task orders while exposing
the mandate question. A next task would ask whether the same pinned
correspondence can establish that delegation's effective scope/window, with
the Emperor's superior authority explicitly retained. That is a change of
target requiring its own versioned scope, not a silent revision of this pilot
or evidence that Murat belongs in the Emperor's replacement pool. No new
source-fetch, troop-count batch or numerical run is queued by this result.

## Verification and preservation

The primary read every adopted passage with its surrounding heading/context,
checked the reported nomination against its continuation and positive task
evidence, and retained the genre, uncertainty and dependence limits. A data audit
replays exact context/quote ranges, raw and canonical metadata hashes, line
locators, all evidence references, counts and null/non-promotion fields. It checks
the new source supplement; the ordinary suite continues to check the existing
repository contracts. Neither check establishes historical truth or causal
identification. There was no separate review or subagent.

Exact bindings:

| Object | SHA-256 |
| --- | --- |
| `data/napoleonic/appointment-check-v1/record.json` | `831e720abc760802eda4eaa0e3b7f7c6dcee18075ed339782edb04373fb193bd` |
| Parent `alombert-colin-t2-ocr-v1` raw file | `77fc16cee44e26789d8f0efbdded7c108b67fbfe55b28422663e22567e376823` |
| Complete parent metadata, canonical JSON | `db1b7e146aeae1434ccce1a0ee4ffff7b8d9957ffc2135f2c71bf53e37215794` |
| Immutable original `campaign-pilot.json` | `b0f24a4c21d02a3dcf623d16b8928d2f0bb8cb0c654823a125aa06f9d8ea6ffa` |

The supplement also binds the exact methods/unit specification, evaluation
partition and registry byte hashes. Raw inputs and earlier versioned records
are preserved. The general receipt changes to include the new evidence file;
no previous numerical report is changed. Validation and preservation results
are recorded in the [research log](../research-log.md#1805-german-command-appointment-and-objective-check-v1-2026-10-20).
The source-range audit, all 356 existing tests, `make check` and `make reproduce`
passed. Of 8,008 protected prior files, 8,007 remain byte-identical; only the
general receipt changed, by exactly one added evidence-input binding.
No calibration score, synthetic job, historical fit or feature admission ran.
