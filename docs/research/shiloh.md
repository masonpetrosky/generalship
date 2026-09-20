# Shiloh: first source-enrichment pass

Research date: 2026-09-20. **Draft, not independently reviewed.**

Shiloh cannot yet support a single defensible opening-strength row or a simple
allocation of its two-day result to Grant and Johnston. The sources distinguish
paper returns, men engaged during a day, arriving reinforcements, and after-battle
effectives. They also distinguish formal authority from who directed particular
forces. This pass makes those distinctions inspectable; it does not settle them.

The [dossier](../../data/evidence/TN003.json) now contains **22 claims, 12 troop
observations, and seven chronology events**, against seven claims in the
[preserved first draft](../../data/evidence/history/TN003.v1.json). Eight new text
snapshots and two table facsimiles are pinned in the [source registry](../../data/sources.json).
The frozen cohort, original source tables, and baseline predictions are unchanged.

## What the force numbers actually describe

| Account | Number | Population and timing | Why it is not automatically opening strength |
|---|---:|---|---|
| NPS summary | US 65,085; CS 44,968 | Whole-engagement “forces engaged” | Does not separate April 6 from April 7 or arrival phases |
| Union field-return abstract | 44,895 | Present for duty in returns dated April 4–5 | Includes Wallace away from the April 6 battle, and explicitly omits some strengths |
| Same abstract, Third Division | 7,564 | Present for duty, April 4 | Compiler says this division was not in the battle of April 6 |
| Jordan/Beauregard return | 40,335 | Confederate effective total **before** battle | Own footnote says it disagrees with two following reports; muster date unstated |
| Same return | 29,636 | Confederate effective total **after** battle | Not an April 7 opening count or a simple casualty measure; forwarded April 21 |
| Force’s later estimate | 32,000–33,000 | Union officers, NCOs and privates actually engaged **over Sunday** | Interpretive estimate with a corrected exclusion in its calculation |
| Force’s Monday reinforcements | About 20,000 / 6,500 / 1,400 | Buell / Lew Wallace / other regiments | Not a census at one time; not necessarily all first arrivals on Monday |
| Army staff-ride narrative | 5,800 | Wallace’s division arriving after dark April 6 | Narrative does not reconcile this count with the paper return or Force |
| Army staff-ride narrative | About 600 | Nelson’s leading contingent west of the river and in line by 18:00 April 6 | A leading contingent, not the whole division or army |

Sources: [NPS snapshot](../../data/raw/nps-tn003.txt);
[Union return, Official Records I.X.1 p.112](../../data/raw/shiloh/or-union-return-april4-5.txt);
[Confederate return, p.396](../../data/raw/shiloh/or-confederate-return.txt);
[Force, pp.178–180](../../data/raw/shiloh/force-1881-shiloh.txt);
[Gudmens, pp.85 and 113](../../data/raw/shiloh/gudmens-shiloh-handbook.txt).

The Union return’s footnotes matter as much as its total. It omits strengths of
two regiments and one battery in the Sixth Division, and omits division staffs.
Subtracting Wallace’s 7,564 from 44,895 produces **37,331 as arithmetic**, but does
not repair those omissions, synchronize the return dates, or establish which men
could fight at first contact. That subtotal is deliberately not a new observation.
The [full page scan](../../data/raw/shiloh/or-union-return.png) preserves the headings
and notes that OCR alone can scramble.

The Confederate return has its own warning: its before/after columns disagree
with reports Nos.136 and 137. Its [scan](../../data/raw/shiloh/or-confederate-return.png)
also separates cavalry from infantry and artillery. We retain 40,335 as this
return’s account, without silently replacing NPS’s 44,968 or declaring either correct.
The after-battle muster date remains null; the April 21 forwarding date is separate.

Force illustrates why a second history is not an automatic adjudicator. His prose
excludes the Fifteenth Michigan from Sunday, but footnote 3 says that exclusion is
a mistake and records Sunday casualties. He also quotes other authors’ totals,
then distinguishes “present for duty” from combatants. His 32,000–33,000 estimate
is retained as a disputed later interpretation. We have not directly inspected
every report or biography he cites, and do not present them as newly read sources.

## Reinforcements and command are sequences

| Phase | Evidence established by this pass | Still unresolved |
|---|---|---|
| March 20 | Halleck orders Grant to keep forces together until joining Buell, avoid engagement, and await fortification/orders | Receipt time, later modifications, and the exact landing-specific order summarized by NPS |
| April 5 | Halleck gives Buell separate command, with Grant authorized to take general command if attacked | Receipt and how general authority translated into particular battlefield decisions |
| April 6, reported 14:30 | Beauregard’s April 11 report dates Johnston’s death to this time; the handbook describes staff carrying the news | Exact notification and effective assumption times for Beauregard |
| April 6 evening | Handbook places Nelson’s leading brigade opposite the landing at 17:00 and about 600 in line by 18:00 | Primary unit reports needed to audit the times, crossing rate and contingent size |
| April 6 after dark | Handbook says Lew Wallace arrived too late to fight that day | Population behind 5,800 and responsibility for the delay |
| April 7 early morning | Buell reports Nelson/Crittenden advancing soon after 05:00 and McCook arriving during deployment | A common readiness time for all reinforcements cannot be inferred |
| After the battle | Buell describes limited pursuit; Grant reports the main Confederate army retreating in good order | Campaign achievement requires later operations and objectives, not another copy of the battle result |

Sources: [Halleck orders, O.R. I.X.2 pp.50–51 and 94](../../data/raw/shiloh/or-halleck-orders.txt);
[Beauregard report, I.X.1 pp.385–388](../../data/raw/shiloh/or-beauregard-shiloh-report.txt);
[Buell report, pp.291–296, selected pages](../../data/raw/shiloh/or-buell-shiloh-report.txt);
[Grant report, pp.109–110](../../data/raw/shiloh/or-grant-shiloh-report.txt);
[Army handbook excerpts](../../data/raw/shiloh/gudmens-shiloh-handbook.txt).

The order to Wallace is a responsibility dispute, not merely a missing timestamp.
The Army handbook says the written order was lost and recounts conflicting later
versions: Grant’s staff described a route near the river, while Wallace’s staff
described taking position on the army’s right. Grant’s own report attributes delay
to the route. This pass records the dispute without treating the handbook’s causal
explanation or Grant’s complaint as a measured command effect.

The NPS statement that Beauregard was unaware of Buell’s arrival also becomes more
precise when read beside his report. Beauregard says a special dispatch gave him
hope that Buell’s main force would not arrive in time, and that the next morning’s
firing assured him of the junction. That is evidence of what he later said he
believed. The underlying dispatch, receipt, other intelligence and feasible
alternatives still need to be reconstructed.

Halleck’s fortification language complicates the original NPS attribution of the
unfortified camp to Grant. An instruction, its receipt, the authority to implement
it, and implementation are separate facts. Finding the order does not by itself
prove disobedience or establish the counterfactual benefit of a different camp.

## Implications for the replacement boundary

Both replacement dates remain null. A useful **tactical** candidate is immediately
before initial contact on April 6, but an estimand must specify whether it replaces
Grant, Johnston, or a particular subordinate, which forces are actually available,
and which future arrivals are uncertain at that moment. April 7 reinforcements and
after-battle returns cannot be supplied as opening facts known with certainty.

A **campaign** boundary must precede the preparation or concentration being
evaluated. It also needs an authority scope: Halleck’s constraints, Buell’s separate
army, subordinate decisions and the Confederate command transition cannot all be
assigned to one name. This pass has not yet established that boundary or a suitable
replacement population. The inherited/created tags remain hypotheses.

Beauregard’s stated objective was to strike Grant before Buell joined and remove
captured resources while retaining Corinth. Buell and Grant describe limits on
pursuit after the Union victory. These observations show why occupying the field,
destroying an enemy army and achieving a campaign objective need separate outcomes.
They do not provide weights for adding tactical and campaign scores.

## Source dependence and extraction limits

The sources are more varied than the original NPS summaries, but their number is
not an independence score. Force explicitly says official reports are his main
source; the Army handbook also draws on Official Records and later histories.
Jordan’s return and Beauregard’s report share a command reporting chain. The scans
and transcriptions are two representations of the same documents. NPS and the
CWSAC tables remain one source family.

Original reports are participants’ accounts, published later in an official
compilation. They can be selective, mistaken or self-justifying. We preserved
attributions rather than converting their explanations into objective causes.
The handbook is useful for chronology and disputes, but its teaching narrative is
not a substitute for auditing underlying records. Its appendix heading says
**present**, while narrative numbers need separate interpretation; we did not sum
appendix entries into a supposedly comparable engaged total.

Table totals/notes were transcribed from rendered pages. Report excerpts preserve
normalized embedded OCR, including some misspellings. The manifest records parent
download URLs and hashes, transformations, document/publication dates, and source
dependencies. Full books are not vendored. Quote checks now enforce the declared
section for these new snapshots, so a passage elsewhere in the same document cannot
accidentally satisfy a wrong-page citation. Checks still do not prove entailment,
historical truth, or source independence. No independent review has occurred.

## Next work that can start immediately

1. Inspect Confederate reports Nos.136 and 137 flagged by the return, retain their
   definitions, and trace NPS’s 44,968 before deciding which comparisons are valid.
2. Audit the Union return’s missing units and actual arrival/engagement reports,
   starting with the Fifteenth Michigan correction and Wallace’s detachments.
3. Audit Nelson/Ammen crossing times and Buell’s divisional returns; distinguish
   arrival at Savannah, the opposite bank, the landing and the fighting line.
4. Have an independent historical reviewer examine these claims and boundary
   proposals, retaining unresolved disagreements. Then define feature admission.

The broader campaign remains the next expansion unit. Fort Henry, Fort Donelson
and Corinth have not been researched by this Shiloh-only pass. The frozen pilot
still has **23 baseline-eligible engagements out of 127**, and the unchanged model
still performs worse than equal odds on its held-out Brier score. Richer evidence
has not yet been shown to improve predictions or identify a commander’s contribution.
