# Shiloh review context

**Draft evidence; no review performed.**

Bundle: `TN003-a42f063-v1`. Evidence commit: `a42f06390651eea01d952a7cb7c329f410a6f9ab`.
Dossier SHA-256: `1107b7149f9aa3877478e003a01ae2383b5d0729a15d6a90106e427350d49780`.

This text companion is complete for supplied claim/text comparison. Image-level
transcription review requires opening the PNGs in the ZIP. All 50 registered
source files are bundled, including uncited baseline/context files; they are
not 50 independent historical witnesses. Full parent PDFs are not included.

## Review index

| Claim ID | Draft status | Quantity IDs | Event IDs |
|---|---|---|---|
| strength-total | supported | nps-union-total, nps-confederate-total | - |
| fortification-choice | supported | - | - |
| await-buell | supported | - | halleck-concentration-order |
| command-transfer | supported | - | johnston-death |
| buell-awareness | supported | - | - |
| result | supported | - | - |
| logistics-unknown | unknown | - | - |
| union-return-strength | supported | union-paper-total, wallace-april4-return | - |
| confederate-return-before | disputed | confederate-before | - |
| confederate-return-after | disputed | confederate-after | - |
| force-opening-estimate | disputed | force-sunday-engaged | - |
| force-corrected-exclusion | disputed | - | - |
| force-monday-reinforcements | supported | force-buell, force-wallace, force-other | - |
| wallace-handbook-strength | supported | handbook-wallace | wallace-late-arrival |
| nelson-evening-crossing | disputed | handbook-nelson-leading | nelson-leading-crossing |
| buell-divisions-arrive | supported | - | april7-deployment |
| union-command-authority | supported | - | union-command-order |
| wallace-order-dispute | disputed | - | wallace-late-arrival |
| confederate-assigned-objective | supported | - | - |
| confederate-delay-account | supported | - | - |
| reported-exhaustion | supported | - | - |
| pursuit-and-campaign | supported | - | limited-pursuit |
| confederate-report-136 | disputed | confederate-report-136-total, confederate-report-136-infantry, confederate-report-136-artillery, confederate-report-136-cavalry | - |
| confederate-report-137 | disputed | confederate-report-137-total, confederate-report-137-infantry, confederate-report-137-artillery, confederate-report-137-cavalry | - |
| confederate-report-136-monday-arrival | supported | - | - |
| confederate-report-137-composition-change | supported | - | - |
| confederate-return-total-discrepancies | disputed | - | - |
| confederate-report-137-internal-arithmetic | disputed | - | - |
| prentiss-return-attachment | supported | - | - |
| sixth-division-return-components | supported | sixth-april5-abstract | - |
| sixteenth-iowa-counted-not-at-front | supported | - | - |
| eighteenth-wisconsin-return-omission | supported | reed-eighteenth-wisconsin-estimate | eighteenth-wisconsin-arrival |
| fifteenth-iowa-sunday-arrival | supported | - | fifteenth-iowa-arrival |
| twentythird-missouri-sunday-arrival | supported | - | twentythird-missouri-joins |
| reed-sixth-division-reconstruction | disputed | reed-sixth-reconstruction | - |
| sixth-division-original-omission-identities | unknown | - | - |
| michigan-arrival-and-casualty-scope | supported | - | michigan-arrival |
| reed-michigan-sunday-conflict | disputed | - | michigan-arrival |
| rousseau-michigan-monday-contingent | supported | rousseau-michigan-contingent | michigan-joins-rousseau |
| wallace-detachment-orders | supported | - | wallace-crumps-detachment |
| wallace-reed-detachment-counts | supported | reed-wallace-detached, reed-wallace-engaged, reed-fiftysixth-return, reed-sixtyeighth-return, reed-wallace-cavalry-return | wallace-crumps-detachment |
| wallace-reported-night-deployment | supported | - | wallace-late-arrival, wallace-night-readiness |
| reed-participation-population-rule | supported | - | - |
| nelson-crossing-clock-dispute | disputed | - | nelson-savannah-departure |
| ammen-crossing-sequence | supported | - | ammen-savannah-arrival, nelson-savannah-departure |
| ohio-leading-regimental-landings | supported | - | ohio-regiments-sunday-landing |
| grose-sunday-contingent | supported | grose-sunday-eight-companies | grose-sunday-formation |
| nelson-night-infantry-crossing | supported | - | nelson-infantry-crossing-complete |
| nelson-separated-arms | supported | - | nelson-infantry-crossing-complete, nelson-cavalry-evening-crossing |
| nelson-action-strength | supported | nelson-taken-into-action, nelson-thirtysixth-taken-into-action | - |
| nelson-march-paper-strength | supported | nelson-march-abstract | - |
| crittenden-arrival-phases | supported | - | crittenden-night-landing |
| mccook-staged-arrival | supported | - | mccook-savannah-arrival, mccook-landing-and-brigade-arrivals |
| wood-late-brigade-arrivals | supported | - | wood-brigades-land-and-advance |
| garfield-present-not-engaged | supported | - | wood-brigades-land-and-advance |
| reed-nelson-return-basis | supported | reed-nelson-march31 | - |
| reed-mccook-postbattle-return | supported | reed-mccook-april30 | - |
| reed-ohio-estimates-and-discrepancy | disputed | reed-mccook-detail-engaged, reed-mccook-recap-engaged, reed-crittenden-engaged, reed-wagner-late-estimate, reed-ohio-total-engaged | - |
| reed-buell-letter-secondhand | supported | - | - |
| nelson-sunday-exact-crossed-strength | unknown | - | - |
| ammen-night-formation | supported | - | ammen-night-reassembly |
| nelson-morning-phase-clocks | disputed | - | nelson-morning-advance |

## Current dossier

```json
{
  "schema_version": 2,
  "battle_id": "TN003",
  "status": "draft",
  "tactical_replacement_at": null,
  "campaign_replacement_at": null,
  "boundary_note": "Tactical and campaign replacement dates remain unset. The phase records distinguish report dates, event dates and population definitions. Proposed boundaries and unresolved authority are discussed in docs/research/shiloh.md. No research quantity is admitted to modeling. The Confederate-return follow-up is documented in docs/research/shiloh-confederate-returns.md; printed totals and arithmetic discrepancies remain alternatives for review.",
  "claims": [
    {
      "id": "strength-total",
      "dimension": "strength",
      "value": "NPS lists US 65,085 and Confederate 44,968 as forces engaged; these are not verified opening strength.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Whole-engagement totals may include reinforcements; do not condition opening expectations on later arrivals.",
      "citations": [
        {
          "source_id": "nps-tn003",
          "locator": "Forces Engaged",
          "quote": "110053 total (US 65085; CS 44968;)"
        }
      ]
    },
    {
      "id": "fortification-choice",
      "dimension": "terrain",
      "value": "NPS attributes the absence of fortification to Grant.",
      "phase": "commander_created",
      "status": "supported",
      "rationale": "NPS attribution remains a hypothesis about responsibility. Halleck’s March 20 fortification instruction is now available; receipt, implementation, camp-selection authority and later orders require review before attributing an avoidable failure to Grant.",
      "citations": [
        {
          "source_id": "nps-tn003",
          "locator": "Description",
          "quote": "Grant did not choose to fortify his position; rather, he set about drilling his men many of which were raw recruits."
        }
      ]
    },
    {
      "id": "await-buell",
      "dimension": "objectives",
      "value": "NPS says Grant was ordered to await Buell at Pittsburg Landing. Halleck’s March 20 order directly requires concentration until joining Buell and avoiding engagement, but does not itself name Pittsburg Landing.",
      "phase": "inherited",
      "status": "supported",
      "rationale": "Direct order establishes a superior’s constraint and includes fortification language. Its issue date is not proof of receipt time; later modifications and the exact landing-specific order remain to be traced.",
      "citations": [
        {
          "source_id": "nps-tn003",
          "locator": "Description",
          "quote": "Grant received orders to await Buell's Army of the Ohio at Pittsburg Landing."
        },
        {
          "source_id": "or-halleck-orders",
          "section": "p50-51-march20",
          "locator": "p50-51-march20",
          "quote": "By all means keep your forces together until you connect with General Buell, who is now at Columbia, and will move on Waynesborough with three divisions. Don't let the enemy draw you into an engagement now. Wait till you are properly fortified and receive orders."
        }
      ]
    },
    {
      "id": "command-transfer",
      "dimension": "responsibility",
      "value": "Beauregard’s April 11 report dates Johnston’s death to 2:30 p.m. April 6 and says chief command then devolved upon him. The Army handbook describes staff carrying the news to Beauregard; his exact receipt and effective-assumption times remain unestablished.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Distinguish a reported time of death from the time the successor learned of it and exercised authority. Neither commander receives an automatic share of the two-day residual.",
      "citations": [
        {
          "source_id": "nps-tn003",
          "locator": "Description",
          "quote": "Johnston had been mortally wounded earlier and his second in command, Gen. P.G.T. Beauregard, took over."
        },
        {
          "source_id": "or-beauregard-shiloh-report",
          "section": "p387",
          "locator": "p387",
          "quote": "Our commander-in-chief, General A. S. Johnston, fell mor tally wounded, and died on the field at 2.30 p. m."
        },
        {
          "source_id": "or-beauregard-shiloh-report",
          "section": "p387",
          "locator": "p387",
          "quote": "The chief command then devolved upon me"
        },
        {
          "source_id": "gudmens-shiloh-handbook",
          "section": "p100",
          "locator": "p100",
          "quote": "Staff officers quickly rode to Beauregard at the intersection of the Pittsburg- Corinth Road and Purdy-Hamburg Road and told him of Johnston’s death."
        }
      ]
    },
    {
      "id": "buell-awareness",
      "dimension": "information",
      "value": "NPS describes Beauregard as unaware of Buell’s arrival. Beauregard’s own April 11 account says he hoped, from a special dispatch, that Buell’s main force could not reach the field in time, and says April 7 firing assured him of the junction.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "The report is evidence of Beauregard’s retrospective account of his belief, not proof of his complete information set or of reasonable ignorance. Recover the dispatch and its receipt before adjudicating intelligence responsibility.",
      "citations": [
        {
          "source_id": "nps-tn003",
          "locator": "Description",
          "quote": "Beauregard was unaware of the arrival of Buell's army"
        },
        {
          "source_id": "or-beauregard-shiloh-report",
          "section": "p387",
          "locator": "p387",
          "quote": "hoping, from news received by a special dispatch, that delays had been encountered by General Buell in his march from Columbia, and that his main force, therefore, could not reach the field of battle in time to save General Grant's shat tered fugitive forces from capture or destruction on the following day."
        },
        {
          "source_id": "or-beauregard-shiloh-report",
          "section": "p387",
          "locator": "p387",
          "quote": "About 6 o'clock on the morning of April 7, however, a hot fire of musketry and artillery, opened from the enemy's quarter on our ad vanced line, assured me of the junction of his forces"
        }
      ]
    },
    {
      "id": "result",
      "dimension": "outcome",
      "value": "Union victory",
      "phase": "post_outcome",
      "status": "supported",
      "rationale": "Source outcome is distinct from campaign contribution.",
      "citations": [
        {
          "source_id": "arnold-cwsac-battles",
          "row_key": {
            "battle": "TN003"
          },
          "column": "results_text",
          "quote": "Union victory"
        }
      ]
    },
    {
      "id": "logistics-unknown",
      "dimension": "logistics",
      "value": null,
      "phase": "unresolved",
      "status": "unknown",
      "rationale": "Numerical ammunition availability, ration distribution, and combat readiness by formation and phase remain unestablished. Qualitative participant claims of exhaustion below do not justify an invented readiness score.",
      "citations": []
    },
    {
      "id": "union-return-strength",
      "dimension": "strength",
      "value": "The compiled April 4–5 return lists 44,895 present for duty, including 7,564 in the Third Division. Its notes exclude that division from April 6 fighting, omit strengths for two Sixth Division regiments and one battery, and omit division staffs.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "A paper return with different dates and explicit omissions is not a census of opening combatants. Subtracting 7,564 gives a partial subtotal, not a corrected opening estimate. The handbook explicitly identifies Lew Wallace’s division as the Third Division in the separately cited wallace-handbook-strength claim.",
      "citations": [
        {
          "source_id": "or-union-return-april4-5",
          "section": "p112",
          "locator": "p112",
          "quote": "Grand total | 1,987 | 42,908 | 44,895 | 62"
        },
        {
          "source_id": "or-union-return-april4-5",
          "section": "p112",
          "locator": "p112",
          "quote": "Total Third Division | 314 | 7,250 | 7,564 | 12"
        },
        {
          "source_id": "or-union-return-april4-5",
          "section": "p112",
          "locator": "p112",
          "quote": "Third Division note: Return dated April 4; the division not in the battle of April 6."
        },
        {
          "source_id": "or-union-return-april4-5",
          "section": "p112",
          "locator": "p112",
          "quote": "Sixth Division note: Return dated April 5; strength of two regiments and one battery not reported on the original.\nGrand-total note: Division staff not included in this abstract."
        }
      ]
    },
    {
      "id": "confederate-return-before",
      "dimension": "strength",
      "value": "Jordan’s return, forwarded by Beauregard April 21, reports an effective total before battle of 40,335, including 4,382 cavalry. Its footnote says both columns disagree with the following reports Nos. 136 and 137.",
      "phase": "unresolved",
      "status": "disputed",
      "rationale": "This is one retrospective return’s definition, not an adjudicated count of men engaged. Its own disagreement warning must travel with the number. Reports 136/137 are now inspected in the follow-up claims; the conflict remains unresolved and this original observation is preserved.",
      "citations": [
        {
          "source_id": "or-confederate-return",
          "section": "p396",
          "locator": "p396",
          "quote": "Columns: Command | Commander | Effective total before battle | Effective total after battle."
        },
        {
          "source_id": "or-confederate-return",
          "section": "p396",
          "locator": "p396",
          "quote": "Grand total | 40,335 | 29,636"
        },
        {
          "source_id": "or-confederate-return",
          "section": "p396",
          "locator": "p396",
          "quote": "Cavalry | Brig. Gen. F. Gardner | 4,382 | 4,081"
        },
        {
          "source_id": "or-confederate-return",
          "section": "p396",
          "locator": "p396",
          "quote": "Footnote to both effective-total columns: These columns do not agree with the effective totals in reports Nos. 136 and 137, following."
        }
      ]
    },
    {
      "id": "confederate-return-after",
      "dimension": "strength",
      "value": "The same return reports an effective total after battle of 29,636.",
      "phase": "post_outcome",
      "status": "disputed",
      "rationale": "After-battle strength is neither April 7 opening strength nor a simple casualty count. It cannot become a pre-battle predictor. Report 137 prints 32,212 for its April 10 return, but the two dates/populations are not shown equivalent; retain this 29,636 separately.",
      "citations": [
        {
          "source_id": "or-confederate-return",
          "section": "p396",
          "locator": "p396",
          "quote": "Columns: Command | Commander | Effective total before battle | Effective total after battle."
        },
        {
          "source_id": "or-confederate-return",
          "section": "p396",
          "locator": "p396",
          "quote": "Grand total | 40,335 | 29,636"
        }
      ]
    },
    {
      "id": "force-opening-estimate",
      "dimension": "strength",
      "value": "Force estimates 32,000–33,000 Union officers, noncommissioned officers and privates actually engaged on Sunday; this is a later interpretive estimate, not an opening return.",
      "phase": "unresolved",
      "status": "disputed",
      "rationale": "Force explains differences between present-for-duty and combatant counts, but his calculation also depends on a corrected unit exclusion. Preserve as a disputed source estimate; it measures participation over Sunday, not availability at first contact.",
      "citations": [
        {
          "source_id": "force-1881-shiloh",
          "section": "pp178-180",
          "locator": "pp178-180",
          "quote": "Probably all were true, and thirty-three thousand or thirty-two thousand is the number of officers, non-commissioned officers, and privates actually engaged in Sunday's battle on the National side."
        }
      ]
    },
    {
      "id": "force-corrected-exclusion",
      "dimension": "strength",
      "value": "Force’s text excludes the Fifteenth Michigan from Sunday; footnote 3 explicitly says this is a mistake and gives that regiment’s Sunday casualties.",
      "phase": "unresolved",
      "status": "disputed",
      "rationale": "Retain Force's correction but not his uncorrected exclusion. The Michigan 1862 report supports April 5 arrival and the same casualty totals over April 6-7; it does not establish the footnote's Sunday-only allocation. Reed's narrative supports Sunday presence but his table conflicts. No original Oliver report has been inspected.",
      "citations": [
        {
          "source_id": "force-1881-shiloh",
          "section": "pp178-180",
          "locator": "pp178-180",
          "quote": "The statement includes the Fourteenth Wisconsin and the Fifteenth Michigan, neither of which arrived till after the close of Sunday's battle."
        },
        {
          "source_id": "force-1881-shiloh",
          "section": "pp178-180",
          "locator": "pp178-180",
          "quote": "This is a mistake as to the Fifteenth Michigan, which lost, Sunday, 33 killed, 64 wounded, and 7 missing."
        }
      ]
    },
    {
      "id": "force-monday-reinforcements",
      "dimension": "strength",
      "value": "Force gives approximate Monday reinforcements of 20,000 from Buell, 6,500 from Lew Wallace, and 1,400 from other regiments.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "These are rounded later-history figures. Monday participation is not proof that everyone first arrived Monday or was deployable at dawn. The Army handbook’s 5,800 for Wallace and the April 4 return’s 7,564 are retained as different observations. Reed's separate 5,837 engaged account does not establish the basis of Force's 6,500. Reed's separate 17,918 Army of the Ohio reconstruction includes estimated and late-arriving components and does not adjudicate Force's about 20,000.",
      "citations": [
        {
          "source_id": "force-1881-shiloh",
          "section": "pp178-180",
          "locator": "pp178-180",
          "quote": "The reinforcements of Monday numbered, of Buell's army, about twenty thousand; Lewis Wallace, sixty-five hundred; other regiments, about fourteen hundred."
        }
      ]
    },
    {
      "id": "wallace-handbook-strength",
      "dimension": "strength",
      "value": "The Army handbook describes Wallace’s division as 5,800 men who arrived after dark April 6 and did not fight that day.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Reed supplies a separate 7,564 - 1,727 = 5,837 accounting bridge. This is close to 5,800 but does not prove the handbook's derivation or explain Force's 6,500. Preserve each source population and the disputed explanation of delay.",
      "citations": [
        {
          "source_id": "gudmens-shiloh-handbook",
          "section": "p85",
          "locator": "p85",
          "quote": "Lew Wallace did not arrive at the battlefield until after dark on 6 April. Due to the vague orders and Wallace’s marching decisions, the 3d Division’s 5,800 men did not fight that day."
        }
      ]
    },
    {
      "id": "nelson-evening-crossing",
      "dimension": "strength",
      "value": "The Army handbook places Nelson’s leading brigade across the river from Pittsburg Landing at 17:00 April 6, and about 600 men west of the river and in line by 18:00.",
      "phase": "unresolved",
      "status": "disputed",
      "rationale": "Preserve the handbook account and original 600 observation. Primary accounts now distinguish reported 17:00 and 17:30 landings, partial boatloads, a roughly 400-man regiment, and all infantry across by 21:00. Neither the common clock nor the derivation of 600 at 18:00 is established.",
      "citations": [
        {
          "source_id": "gudmens-shiloh-handbook",
          "section": "p113",
          "locator": "p113",
          "quote": "At 1700 Nelson’s lead brigade, commanded by COL Jacob Ammen, arrived across the river from Pittsburg Landing. Nelson arranged for boats in the river to start moving his men across, and by 1800 he had about 600 men west of the river and in line."
        }
      ]
    },
    {
      "id": "buell-divisions-arrive",
      "dimension": "responsibility",
      "value": "Grant reports Crittenden and McCook arriving during the night. Buell says only Nelson and Crittenden were on the ground when they moved soon after 5 a.m. April 7, with McCook arriving during deployment.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Arrival in the vicinity, Savannah, Pittsburg Landing, disembarkation, line deployment and fighting are distinct events. Crittenden reports about 21:00 at the landing; McCook reports 05:00 April 7 while Rousseau disembarked and the rest followed. Retain the original Grant/Buell accounts without a division-wide readiness timestamp.",
      "citations": [
        {
          "source_id": "or-grant-shiloh-report",
          "section": "p109",
          "locator": "p109",
          "quote": "During the night the divisions under Generals Crittenden and Mc- Cook arrived."
        },
        {
          "source_id": "or-buell-shiloh-report",
          "section": "p293",
          "locator": "p293",
          "quote": "Soon after 5 o'clock on the morning of the 7th General Nelson's and General Crittenden's divisions, the only ones yet arrived on the ground, moved promptly forward to meet the enemy."
        },
        {
          "source_id": "or-buell-shiloh-report",
          "section": "p293",
          "locator": "p293",
          "quote": "By this time McCook's division arrived >n the ground, and was immediately formed on the right of Crittenden's."
        }
      ]
    },
    {
      "id": "union-command-authority",
      "dimension": "responsibility",
      "value": "Halleck’s April 5 order says Buell will exercise separate command unless attacked, in which case Grant may take general command. Grant’s report acknowledges Buell’s distinct army and field role.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Formal authority, tactical direction, and personal decision responsibility must be distinguished. Issue date does not establish receipt time. No equal division of battle credit follows from these names.",
      "citations": [
        {
          "source_id": "or-halleck-orders",
          "section": "p94-april5",
          "locator": "p94-april5",
          "quote": "You will act in concert, but he will exercise his separate command, unless the enemy should attack you. In that case you are authorized to take the general command."
        },
        {
          "source_id": "or-grant-shiloh-report",
          "section": "p109",
          "locator": "p109",
          "quote": "General Buell, coming on the field with a distinct army long under Jiis command"
        }
      ]
    },
    {
      "id": "wallace-order-dispute",
      "dimension": "responsibility",
      "value": "The Army handbook says the written order sent to Wallace was lost and summarizes conflicting recollections: a river-side route versus taking position on the army’s right.",
      "phase": "unresolved",
      "status": "disputed",
      "rationale": "This is a sourced account of a dispute, not inspection of the missing order. Responsibility for delay remains unresolved; later recollections require their own dates and incentives.",
      "citations": [
        {
          "source_id": "gudmens-shiloh-handbook",
          "section": "p84",
          "locator": "p84",
          "quote": "Wallace handed the order to one of his staff officers, Captain Frederick Knefler, who put it under his sword belt. Sometime during the day the orders fell out of the belt, an event that would haunt Wallace for the rest of his life."
        },
        {
          "source_id": "gudmens-shiloh-handbook",
          "section": "p84",
          "locator": "p84",
          "quote": "After the battle there was a controversy about Wallace’s movements to the battle. Grant and his staff officers said the order told Wallace to take “the road nearest to and parallel with the river.” Wallace and his staff of - ficers, however, said the order told them to “come up and take position on the right of the Army.”"
        }
      ]
    },
    {
      "id": "confederate-assigned-objective",
      "dimension": "objectives",
      "value": "Beauregard’s report describes the objective as striking Grant before Buell joined, then removing captured resources while retaining Corinth as the strategic point.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Retrospective stated objective, not a recovered complete set of prior orders. A campaign evaluation must distinguish destruction/capture, concentration timing, and retention of Corinth.",
      "citations": [
        {
          "source_id": "or-beauregard-shiloh-report",
          "section": "p385",
          "locator": "p385",
          "quote": "It was then determined to assume the offensive, and strike a sudden blow at the enemy, in position under General Grant on the west bank of the Tennessee, at Pittsburg, and in the direction of Savannah, before he was re-enforced by the army under General Buell, then known to be advancing for that purpose"
        },
        {
          "source_id": "or-beauregard-shiloh-report",
          "section": "p385",
          "locator": "p385",
          "quote": "It was never contemplated, however, to retain the position thus gained and abandon Corinth, the strategic point of the campaign."
        }
      ]
    },
    {
      "id": "confederate-delay-account",
      "dimension": "logistics",
      "value": "Beauregard reports planning an early April 5 attack, delayed until April 6 after difficult marching and rain on the night of April 4.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Preserve the report’s planned date and stated causes. A delayed attack may reflect both inherited weather and command decisions; causal classification requires an earlier replacement boundary.",
      "citations": [
        {
          "source_id": "or-beauregard-shiloh-report",
          "section": "p385",
          "locator": "p385",
          "quote": "It was expected we should be able to reach the enemy's lines in time to attack iim early on the 5th instant."
        },
        {
          "source_id": "or-beauregard-shiloh-report",
          "section": "p386",
          "locator": "p386",
          "quote": "storm on the night of the 4th, which drenched the troops in bivouac; hence our forces did not reach the intersection of the roads from Pitts- burg and Hamburg, in the immediate vicinity of the enemy, until late Saturday afternoon."
        }
      ]
    },
    {
      "id": "reported-exhaustion",
      "dimension": "logistics",
      "value": "Both Grant and Beauregard describe fatigue and rain as constraints; Beauregard additionally says his men fought over twelve hours without food.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Participant explanations for decisions, not measured army-wide readiness. No numerical exhaustion score or common coefficient is inferred.",
      "citations": [
        {
          "source_id": "or-grant-shiloh-report",
          "section": "p109",
          "locator": "p109",
          "quote": "My force was too much fatigued from two days' hard fighting and exposure in the open air to a drenching rain during the intervening night to pursue immediately."
        },
        {
          "source_id": "or-beauregard-shiloh-report",
          "section": "p387",
          "locator": "p387",
          "quote": "Darkness was close at hand ; officers and men were, exhausted by a combat of over twelve hours without food, and jaded by the march of the preceding day through mud and water."
        }
      ]
    },
    {
      "id": "pursuit-and-campaign",
      "dimension": "outcome",
      "value": "Buell reports limited April 7 pursuit and says he lacked cavalry and road knowledge; Grant reports that subsequent pursuit found the main Confederate army had retreated in good order.",
      "phase": "post_outcome",
      "status": "supported",
      "rationale": "Battlefield victory does not imply destruction of the opposing army or completion of the Corinth campaign. These are attributed accounts, not a quantitative campaign contribution.",
      "citations": [
        {
          "source_id": "or-buell-shiloh-report",
          "section": "p295",
          "locator": "p295",
          "quote": "The pursuit was continued iio farther that day. I was without cav alry, and the different corps had become a good deal scattered in a pursuit over a country which screened the movements of the enemy, and the roads of which I knew practically nothing."
        },
        {
          "source_id": "or-grant-shiloh-report",
          "section": "p109",
          "locator": "p109",
          "quote": "General Sherman, however, followed the enemy, finding that the main part of the army had retreated in good order."
        }
      ]
    },
    {
      "id": "confederate-report-136",
      "dimension": "strength",
      "value": "Report 136 prints an effective total of 38,773, with 34,727 infantry, 1,973 artillery and 2,073 cavalry. Its separate Present For duty columns show 2,587 officers and 37,011 enlisted men; Present Total/Aggregate are 46,425/49,444, and Present and absent Total/Aggregate are 57,252/59,774. The heading describes forces that marched April 3. Both returns are submitted/forwarded under Bragg with a bracketed June 30 date.",
      "phase": "unresolved",
      "status": "disputed",
      "rationale": "Retain the column labels and printed figures as separate populations, not interchangeable strength definitions. Effective total is not officers plus enlisted men For duty. The April 3 march heading and Monday-arrival footnote do not establish a single underlying muster or April 6 opening population. Submission/forwarding date does not establish when command knew these numbers. Same reporting chain as the earlier return, not independent review.",
      "citations": [
        {
          "source_id": "or-confederate-report-136-v1",
          "section": "p398",
          "locator": "Official Records I.X.1, report No. 136, printed p.398; selected table columns or printed note",
          "quote": "Grand total | 2,587 | 37,011 | 38,773"
        },
        {
          "source_id": "or-confederate-report-136-v1",
          "section": "p398",
          "locator": "Official Records I.X.1, report No. 136, printed p.398; selected table columns or printed note",
          "quote": "Total infantry | 2,379 | 33,270 | 34,727"
        },
        {
          "source_id": "or-confederate-report-136-v1",
          "section": "p398",
          "locator": "Official Records I.X.1, report No. 136, printed p.398; selected table columns or printed note",
          "quote": "Total artillery | 83 | 1,857 | 1,973"
        },
        {
          "source_id": "or-confederate-report-136-v1",
          "section": "p398",
          "locator": "Official Records I.X.1, report No. 136, printed p.398; selected table columns or printed note",
          "quote": "Cavalry | 125 | 1,884 | 2,073"
        },
        {
          "source_id": "or-confederate-report-136-v1",
          "section": "p398",
          "locator": "Official Records I.X.1, report No. 136, printed p.398; selected table columns or printed note",
          "quote": "Field return of the Confederate forces that marched from Corinth to the Tennessee River, April 3, 1862."
        },
        {
          "source_id": "or-confederate-report-136-v1",
          "section": "p398",
          "locator": "Official Records I.X.1, report No. 136, printed p.398; selected table columns or printed note",
          "quote": "Columns: Command | Present, For duty, Officers | Present, For duty, Enlisted men | Present, Effective total."
        },
        {
          "source_id": "or-confederate-report-136-v1",
          "section": "p398",
          "locator": "Official Records I.X.1, report No. 136, printed p.398; selected table columns or printed note",
          "quote": "Columns: Command | Present, Total | Present, Aggregate | Present and absent, Total | Present and absent, Aggregate."
        },
        {
          "source_id": "or-confederate-report-136-v1",
          "section": "p398",
          "locator": "Official Records I.X.1, report No. 136, printed p.398; selected table columns or printed note",
          "quote": "Grand total | 46,425 | 49,444 | 57,252 | 59,774"
        },
        {
          "source_id": "or-confederate-report-136-v1",
          "section": "p398",
          "locator": "Official Records I.X.1, report No. 136, printed p.398; selected table columns or printed note",
          "quote": "Respectfully submitted and forwarded.\n[JUNE 30, 1862.]\nBRAXTON BRAGG,\nGeneral, Commanding."
        }
      ]
    },
    {
      "id": "confederate-report-137",
      "dimension": "strength",
      "value": "Report 137 prints an effective total of 32,212, with 26,697 infantry, 1,682 artillery and 3,833 cavalry. Its separate Present For duty columns show 2,184 officers and 29,910 enlisted men; Present Total/Aggregate are 44,588/47,493, and Present and absent Total/Aggregate are 60,961/64,500. The heading dates the after-battle return April 10. Both returns are submitted/forwarded under Bragg with a bracketed June 30 date.",
      "phase": "post_outcome",
      "status": "disputed",
      "rationale": "Retain the column labels and printed figures as separate populations, not interchangeable strength definitions. Effective total is not officers plus enlisted men For duty. This after-battle return cannot be an opening predictor. Printed infantry rows disagree with their subtotal; no silent repair. Submission/forwarding date does not establish when command knew these numbers. Same reporting chain as the earlier return, not independent review.",
      "citations": [
        {
          "source_id": "or-confederate-report-137-v1",
          "section": "p399",
          "locator": "Official Records I.X.1, report No. 137, printed p.399; selected table columns or printed note",
          "quote": "Grand total | 2,184 | 29,910 | 32,212"
        },
        {
          "source_id": "or-confederate-report-137-v1",
          "section": "p399",
          "locator": "Official Records I.X.1, report No. 137, printed p.399; selected table columns or printed note",
          "quote": "Total infantry | 1,855 | 24,692 | 26,697"
        },
        {
          "source_id": "or-confederate-report-137-v1",
          "section": "p399",
          "locator": "Official Records I.X.1, report No. 137, printed p.399; selected table columns or printed note",
          "quote": "Total artillery | 70 | 1,634 | 1,682"
        },
        {
          "source_id": "or-confederate-report-137-v1",
          "section": "p399",
          "locator": "Official Records I.X.1, report No. 137, printed p.399; selected table columns or printed note",
          "quote": "Cavalry | 259 | 3,584 | 3,833"
        },
        {
          "source_id": "or-confederate-report-137-v1",
          "section": "p399",
          "locator": "Official Records I.X.1, report No. 137, printed p.399; selected table columns or printed note",
          "quote": "Field return of the Army of the Mississippi after the battle of Shiloh (April 10, 1862)."
        },
        {
          "source_id": "or-confederate-report-137-v1",
          "section": "p399",
          "locator": "Official Records I.X.1, report No. 137, printed p.399; selected table columns or printed note",
          "quote": "Columns: Command | Present, For duty, Officers | Present, For duty, Enlisted men | Present, Effective total."
        },
        {
          "source_id": "or-confederate-report-137-v1",
          "section": "p399",
          "locator": "Official Records I.X.1, report No. 137, printed p.399; selected table columns or printed note",
          "quote": "Columns: Command | Present, Total | Present, Aggregate | Present and absent, Total | Present and absent, Aggregate."
        },
        {
          "source_id": "or-confederate-report-137-v1",
          "section": "p399",
          "locator": "Official Records I.X.1, report No. 137, printed p.399; selected table columns or printed note",
          "quote": "Grand total | 44,588 | 47,493 | 60,961 | 64,500"
        },
        {
          "source_id": "or-confederate-report-137-v1",
          "section": "p399",
          "locator": "Official Records I.X.1, report No. 137, printed p.399; selected table columns or printed note",
          "quote": "Respectfully submitted and forwarded.\n[JUNE 30, 1862.]\nBRAXTON BRAGG,\nGeneral, Commanding."
        }
      ]
    },
    {
      "id": "confederate-report-136-monday-arrival",
      "dimension": "strength",
      "value": "Report 136 attaches to First Corps infantry a footnote that Colonel Hill's Tennessee regiment came upon the field during the engagement on Monday.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "The footnote complicates treating the April 3 heading as one opening population. It supplies neither a regimental headcount nor a numerical adjustment; the table alone does not settle inclusion or exact arrival time.",
      "citations": [
        {
          "source_id": "or-confederate-report-136-v1",
          "section": "p398",
          "locator": "Official Records I.X.1, report No. 136, printed p.398; selected table columns or printed note",
          "quote": "* Colonel Hill's regiment (Tennessee) came upon the [field] during the engagement on Monday."
        },
        {
          "source_id": "or-confederate-report-136-v1",
          "section": "p398",
          "locator": "Official Records I.X.1, report No. 136, printed p.398; selected table columns or printed note",
          "quote": "Infantry, First Corps* | 561 | 8,440 | 9,024"
        }
      ]
    },
    {
      "id": "confederate-report-137-composition-change",
      "dimension": "strength",
      "value": "Report 137 attributes differences in aggregates and totals from the preceding return to killed, wounded and missing, and to the arrival of Carroll's brigade and previously detached cavalry.",
      "phase": "post_outcome",
      "status": "supported",
      "rationale": "This is the return’s explanation, without a numerical bridge or arrival dates. The populations differ; subtracting the two effective totals is not a casualty estimate. It does not reconcile either return with p.396.",
      "citations": [
        {
          "source_id": "or-confederate-report-137-v1",
          "section": "p399",
          "locator": "Official Records I.X.1, report No. 137, printed p.399; selected table columns or printed note",
          "quote": "NOTE.-The difference in aggregates and totals between this and the preceding return is accounted for thus: First, by killed, wounded, and missing in battle, and the arrival of Carroll's brigade and a portion of the cavalry, heretofore detached."
        }
      ]
    },
    {
      "id": "confederate-return-total-discrepancies",
      "dimension": "strength",
      "value": "The printed effective grand totals differ: report 136 has 38,773 versus p.396 before-battle 40,335 (1,562 fewer); report 137 has 32,212 versus p.396 after-battle 29,636 (2,576 more). These are arithmetic comparisons, not corrected strengths.",
      "phase": "unresolved",
      "status": "disputed",
      "rationale": "Dates and populations are not shown equivalent. The p.396 muster dates remain null; report 137’s April 10 date cannot be transferred to it. Report 137’s composition note does not numerically explain the p.396 discrepancy. NPS 44,968 remains separately untraced.",
      "citations": [
        {
          "source_id": "or-confederate-return",
          "section": "p396",
          "locator": "Official Records I.X.1, printed p.396, Inclosure E",
          "quote": "Grand total | 40,335 | 29,636"
        },
        {
          "source_id": "or-confederate-report-136-v1",
          "section": "p398",
          "locator": "Official Records I.X.1, report No. 136, printed p.398; selected table columns or printed note",
          "quote": "Grand total | 2,587 | 37,011 | 38,773"
        },
        {
          "source_id": "or-confederate-report-137-v1",
          "section": "p399",
          "locator": "Official Records I.X.1, report No. 137, printed p.399; selected table columns or printed note",
          "quote": "Grand total | 2,184 | 29,910 | 32,212"
        }
      ]
    },
    {
      "id": "confederate-report-137-internal-arithmetic",
      "dimension": "strength",
      "value": "Report 137’s four printed infantry effective rows sum to 26,797, whereas its infantry subtotal is 26,697. Its infantry enlisted For duty rows sum to 24,290, whereas the printed subtotal is 24,692.",
      "phase": "post_outcome",
      "status": "disputed",
      "rationale": "Arithmetic diagnostics on the inspected print, not authority to emend it. The printed effective branch subtotals sum to the printed grand total 32,212; replacing the infantry subtotal by a row sum would change that total. Original unit returns or an independently checked edition are needed to investigate which figures are wrong. No claim that every other column reconciles.",
      "citations": [
        {
          "source_id": "or-confederate-report-137-v1",
          "section": "p399",
          "locator": "Official Records I.X.1, report No. 137, printed p.399; selected table columns or printed note",
          "quote": "Infantry, First Corps | 461 | 7,198 | 7,582\nInfantry, Second Corps | 590 | 8,453 | 9,118\nInfantry, Third Corps | 425 | 4,305 | 4,865\nInfantry, Reserve Corps | 379 | 4,334 | 5,232\nTotal infantry | 1,855 | 24,692 | 26,697"
        }
      ]
    },
    {
      "id": "prentiss-return-attachment",
      "dimension": "strength",
      "value": "Prentiss says his November 17 report transmits a field return marked A describing the morning of the engagement; the compiler says it is embodied in p.112.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "The report is retrospective. The underlying attachment is not recovered; the compiler abstract still leaves omitted formations unnamed.",
      "citations": [
        {
          "source_id": "or-prentiss-availability-v1",
          "section": "p277",
          "locator": "p277",
          "quote": "I have the honor to transmit field return of the force which was subject to my control, as it appeared upon the morning of the engagement, the same being marked A."
        },
        {
          "source_id": "or-prentiss-availability-v1",
          "section": "p277",
          "locator": "p277",
          "quote": "Embodied in revised statement, p. 112."
        }
      ]
    },
    {
      "id": "sixth-division-return-components",
      "dimension": "strength",
      "value": "The p.112 Sixth Division abstract prints 2,790 in the First Brigade, 1,774 in the Second, 899 unattached and 5,463 total; it does not identify its two omitted regiments or one battery.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "These dated return aggregates are not an opening census. Preserve the original compiler omission note and division-staff exclusion.",
      "citations": [
        {
          "source_id": "or-union-return-detail-v2",
          "section": "p112",
          "locator": "p112",
          "quote": "1st Brigade | 119 | 2,671 | 2,790\n2d Brigade | 85 | 1,689 | 1,774\nUnattached | 41 | 858 | 899\nTotal Sixth Division | 245 | 5,218 | 5,463"
        },
        {
          "source_id": "or-union-return-detail-v2",
          "section": "p112",
          "locator": "p112",
          "quote": "Return dated April 5; strength of two regiments and one battery not reported on the original."
        }
      ]
    },
    {
      "id": "sixteenth-iowa-counted-not-at-front",
      "dimension": "strength",
      "value": "Reed says the Sixteenth Iowa was counted on April 5 but remained at the landing; Chambers says on Sunday it was preparing to join Prentiss when Grant redirected it to reserve duty and then McClernand.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Administrative assignment and inclusion in a return do not prove availability at Prentiss's first contact. Prentiss also excepts this regiment and cavalry from the advance. No exact readiness time is inferred.",
      "citations": [
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p60-second-brigade",
          "locator": "p60-second-brigade",
          "quote": "The colonel reported for duty and handed in his morning report, so that his regiment is included in Miller's report of present for duty."
        },
        {
          "source_id": "or-chambers-availability-v1",
          "section": "p286",
          "locator": "p286",
          "quote": "while my regiment was preparing to join General Prentiss' division, as was previously ordered, an aide of General Grant ordered my regiment in line on the right of the Fifteenth Iowa Volunteers, to act as a reserve and prevent stragglers from reaching the river."
        },
        {
          "source_id": "or-prentiss-availability-v1",
          "section": "p278-sixteenth",
          "locator": "p278-sixteenth",
          "quote": "excepting only the Sixteenth Iowa, which had been sent to the field the day previous without ammunition, and the cavalry, which was held in readiness to the rear"
        }
      ]
    },
    {
      "id": "eighteenth-wisconsin-return-omission",
      "dimension": "strength",
      "value": "Reed explicitly identifies the Eighteenth Wisconsin as arriving April 5 after the morning return, camping with Prentiss, and fighting Sunday; he adds an estimated 735 for duty.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "This identifies a source-described omission, but does not establish a one-to-one mapping of all unnamed p.112 omissions. The 735 is a later estimated table entry, not a recovered original muster.",
      "citations": [
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p111-union-notes",
          "locator": "p111-union-notes",
          "quote": "(d) The Eighteenth Wisconsin arrived on the field April 5, 1862. It is not included in the returns made by the Sixth Division April 5, but it joined the Second Brigade of that division and encamped on the left of the brigade Saturday evening and was engaged as left regiment of Prentiss's division on Sunday."
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p96",
          "locator": "p96",
          "quote": "18th Wisconsin* (note d) | 35 | 700 | 735"
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p97",
          "locator": "p97",
          "quote": "* Estimated."
        }
      ]
    },
    {
      "id": "fifteenth-iowa-sunday-arrival",
      "dimension": "strength",
      "value": "Reid reports the Fifteenth Iowa arrived Sunday morning and disembarked after firing had begun along Prentiss's lines; Reed says it was absent from the April 5 return.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Arrival, disembarkation, ammunition issue and combat deployment are different phases. No strength at first contact or exact arrival clock is supplied.",
      "citations": [
        {
          "source_id": "or-reid-availability-v1",
          "section": "p288",
          "locator": "p288",
          "quote": "arrived at Pittsburg on Sunday morning"
        },
        {
          "source_id": "or-reid-availability-v1",
          "section": "p288",
          "locator": "p288",
          "quote": "found a heavy fire of artillery and musketry already commenced along his lines."
        },
        {
          "source_id": "or-reid-availability-v1",
          "section": "p288",
          "locator": "p288",
          "quote": "The regiment was rapidly disembarked, ammunition distributed, and the men for the first time loaded their guns."
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p111-union-notes",
          "locator": "p111-union-notes",
          "quote": "It is not included in the Sixth Division returns of April 5."
        }
      ]
    },
    {
      "id": "twentythird-missouri-sunday-arrival",
      "dimension": "strength",
      "value": "Prentiss reports the Twenty-third Missouri joined after disembarking as he reformed at 9.05 a.m.; Reed describes an April 6 arrival about 9 a.m.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "This is later-morning participation, not presence at first contact; the clock remains attributed to Prentiss's November account.",
      "citations": [
        {
          "source_id": "or-prentiss-availability-v1",
          "section": "p278-twentythird",
          "locator": "p278-twentythird",
          "quote": "at 9.05 a. m. reformed"
        },
        {
          "source_id": "or-prentiss-availability-v1",
          "section": "p278-twentythird",
          "locator": "p278-twentythird",
          "quote": "At this point the Twenty-third Missouri Infantry, commanded by Colonel Tindall, which had just disembarked from a transport, and had been ordered to report to me as a part of the Sixth Division, joined me."
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p111-union-notes",
          "locator": "p111-union-notes",
          "quote": "(e) The Twenty-third Missouri arrived on the field Sunday morning, April 6, 1862, and reported to General Prentiss at the “Hornets' Nest” about 9 a. m. and fought with him the remainder of the day."
        }
      ]
    },
    {
      "id": "reed-sixth-division-reconstruction",
      "dimension": "strength",
      "value": "Reed prints 7,545 for the Sixth Division, including estimated additions and April 6 arrivals under an April 5 return heading. It is not a replacement for the p.112 total of 5,463.",
      "phase": "unresolved",
      "status": "disputed",
      "rationale": "His 735 for Eighteenth Wisconsin plus 782 for Fifteenth Iowa plus 575 for Twenty-third Missouri equals 2,092, while 7,545 minus 5,463 equals 2,082. His artillery and cavalry total 889 versus p.112 unattached 899. The ten-man discrepancy and the mapping of original omissions remain unresolved; arithmetic is diagnostic, not an explanation.",
      "citations": [
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p97",
          "locator": "p97",
          "quote": "Total Sixth Division | 347 | 7,198 | 7,545"
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p96",
          "locator": "p96",
          "quote": "15th Iowa* (note c) | 32 | 750 | 782\n23d Missouri* (note e) | 35 | 540 | 575"
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p96",
          "locator": "p96",
          "quote": "Total artillery | 9 | 254 | 263"
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p97",
          "locator": "p97",
          "quote": "1st and 2d Battalions, 11th Illinois | 32 | 594 | 626"
        },
        {
          "source_id": "or-union-return-detail-v2",
          "section": "p112",
          "locator": "p112",
          "quote": "Unattached | 41 | 858 | 899"
        }
      ]
    },
    {
      "id": "sixth-division-original-omission-identities",
      "dimension": "strength",
      "value": null,
      "phase": "unresolved",
      "status": "unknown",
      "rationale": "The inspected compiler abstract and later compilation do not establish all three original omission identities. Eighteenth Wisconsin is explicitly absent from Reed's account of the April 5 return, but late-arrival additions cannot be assigned automatically to the two original unnamed regiment slots or the battery slot.",
      "citations": []
    },
    {
      "id": "michigan-arrival-and-casualty-scope",
      "dimension": "strength",
      "value": "Michigan's report for 1862 says the Fifteenth Infantry reached Pittsburg Landing the day before the April 6-7 battle and lost 33 killed, 64 wounded and seven missing in that action.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "The report supports an April 5 arrival account and two-day casualty totals. Matching Force's numbers does not establish his Sunday-only allocation or direct source dependence. The 869 March roll names are not opening combatants.",
      "citations": [
        {
          "source_id": "michigan-ag-1862-fifteenth-v1",
          "section": "p41",
          "locator": "p41",
          "quote": "It reached Pittsburgh Landing, on the Tennessee river, the day before the battle of April 6 and 7, and its participation in that action cost the Regiment a loss of two officers and 31 men killed, 1 officer and 63 privates wounded, and 7 missing."
        }
      ]
    },
    {
      "id": "reed-michigan-sunday-conflict",
      "dimension": "strength",
      "value": "Reed's narrative places the Fifteenth Michigan on the field Sunday, initially without ammunition; his recapitulation excludes both unassigned infantry regiments from April 6 and adds them as April 7 reinforcements.",
      "phase": "unresolved",
      "status": "disputed",
      "rationale": "The p.97 unassigned infantry are Fourteenth Wisconsin and Fifteenth Michigan. The conflict prevents adopting Reed's 39,830 as a reconciled April 6 total. His 750 estimated for duty and 730 commander-reported engaged do not establish opening availability.",
      "citations": [
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "pp60-61-michigan",
          "locator": "pp60-61-michigan",
          "quote": "The regiment moved out upon the field early Sunday morning"
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "pp60-61-michigan",
          "locator": "pp60-61-michigan",
          "quote": "again joined the fighting line at some place not now determined."
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p97",
          "locator": "p97",
          "quote": "14th Wisconsin* (note g) | 30 | 720 | 750\n15th Michigan* (note h) | 30 | 720 | 750"
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p98",
          "locator": "p98",
          "quote": "Deduct Third Division and unassigned infantry not on the field Apr. 6. | 9,064"
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p98",
          "locator": "p98",
          "quote": "And by unassigned infantry. | 1,500"
        }
      ]
    },
    {
      "id": "rousseau-michigan-monday-contingent",
      "dimension": "strength",
      "value": "Rousseau reports that Colonel Oliver joined his brigade early April 7 with about 230 officers and men of the Fifteenth Michigan.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "The report opening dates the action to the 7th. This is a joining contingent, not the whole regiment's Sunday strength; do not subtract it from other counts to infer casualties or stragglers.",
      "citations": [
        {
          "source_id": "or-rousseau-michigan-v1",
          "section": "p310",
          "locator": "p310",
          "quote": "he joined us early in the morning with about 230 officers and men of his regiment"
        },
        {
          "source_id": "or-rousseau-michigan-v1",
          "section": "p307",
          "locator": "p307",
          "quote": "the part taken by my brigade in the battle at this place on the 7th instant."
        }
      ]
    },
    {
      "id": "wallace-detachment-orders",
      "dimension": "strength",
      "value": "Wallace's April 12 report says the Fifty-sixth and Sixty-eighth Ohio and one gun from Thurber's battery were detached to prevent surprise at Crump's Landing.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Names and purpose are passage-backed; this passage gives no personnel total. Reed separately adds cavalry and a train guard. Wallace's account does not adjudicate responsibility for the delayed march.",
      "citations": [
        {
          "source_id": "or-wallace-availability-v1",
          "section": "p170",
          "locator": "p170",
          "quote": "As it also directed me to leave a force to prevent surprise at Crump's Landing, the Fifty-sixth Ohio and Sixty-eighth Ohio Regiments were detached for that purpose, with one gun from Lieutenant Thurber's battery."
        }
      ]
    },
    {
      "id": "wallace-reed-detachment-counts",
      "dimension": "strength",
      "value": "Reed reports 1,727 left at Crump's Landing and 5,837 actually engaged; his component table reports 701 for the Fifty-sixth Ohio, 424 for the Sixty-eighth Ohio, and 559 cavalry for duty.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "7,564 minus 1,727 equals 5,837 within Reed's account. Named infantry and cavalry sum to 1,684; the residual 43 is arithmetic, not an independently reported gun/train-guard count. The report does not explain Force's 6,500; numerical proximity to the handbook's 5,800 is not proven derivation. Reed's secondhand Wallace 5,000 remains an untraced lead.",
      "citations": [
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p93",
          "locator": "p93",
          "quote": "* 2 regiments of infantry, 2 battalions of cavalry, 1 gun of Buel's battery, and train guard—a total of 1,727—were left at Crumps Landing, making the number actually engaged at Shiloh 5,837. Wallace says 5,000."
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p93",
          "locator": "p93",
          "quote": "56th Ohio* | 32 | 669 | 701"
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p93",
          "locator": "p93",
          "quote": "68th Ohio* | 29 | 395 | 424"
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p93",
          "locator": "p93",
          "quote": "Total cavalry | 28 | 531 | 559"
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p98",
          "locator": "p98",
          "quote": "Reenforced Apr. 7 by the Third Division (see ante). | 5,837"
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p92-heading",
          "locator": "p92-heading",
          "quote": "LEW. WALLACE'S (THIRD) DIVISION. (Return of Apr. 4.)"
        }
      ]
    },
    {
      "id": "wallace-reported-night-deployment",
      "dimension": "responsibility",
      "value": "Wallace says he joined a little after nightfall, disposed his brigades and batteries about 1 o'clock at night, and opened artillery fire shortly after daybreak.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Arrival, readiness and fighting are distinct stages. The night bridges April 6-7; no precise arrival clock or resolved blame is inferred.",
      "citations": [
        {
          "source_id": "or-wallace-availability-v1",
          "section": "p170",
          "locator": "p170",
          "quote": "delayed my junction with the main army until a little after night-fall."
        },
        {
          "source_id": "or-wallace-availability-v1",
          "section": "p170",
          "locator": "p170",
          "quote": "About 1 o'clock at night my brigades and batteries were disposed, forming the extreme right, and ready for battle."
        },
        {
          "source_id": "or-wallace-availability-v1",
          "section": "p170",
          "locator": "p170",
          "quote": "Shortly after daybreak Captain Thompson opened fire"
        }
      ]
    },
    {
      "id": "reed-participation-population-rule",
      "dimension": "strength",
      "value": "Reed explicitly takes present for duty as engaged and does not remove noncombatants.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "His engaged totals use a declared convention and cannot silently substitute for men at the firing line, synchronized opening combatants, or Force's narrower account.",
      "citations": [
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p112-note-r",
          "locator": "p112-note-r",
          "quote": "The “present for duty,” has been taken, in each case, as the number engaged in the battle."
        },
        {
          "source_id": "reed-1909-union-audit-v1",
          "section": "p112-note-r",
          "locator": "p112-note-r",
          "quote": "No attempt has been made to eliminate the noncombatants"
        }
      ]
    },
    {
      "id": "nelson-crossing-clock-dispute",
      "dimension": "strength",
      "value": "Nelson reports a 13:30 April 6 departure, a four-hour march, the column head at Pittsburg Landing at 17:00, and action at 18:30; these do not establish a reconciled crossing clock.",
      "phase": "unresolved",
      "status": "disputed",
      "rationale": "13:30 plus four hours is 17:30 before allowing crossing time, whereas the same report says 17:00 at the landing. This is a source timing tension, not permission to correct either clock. The handbook instead places 17:00 at the opposite bank. Approximation, stages and textual error remain possible.",
      "citations": [
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "p323-crossing",
          "locator": "p323-crossing",
          "quote": "at 1.30 p. m. on Sunday, April 6"
        },
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "p323-crossing",
          "locator": "p323-crossing",
          "quote": "in four hours. At 5 the head of my column marched up the bank at Pittsburg Landing"
        },
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "pp323-324-action",
          "locator": "pp323-324-action",
          "quote": "This was at 6.30 p. m."
        }
      ]
    },
    {
      "id": "ammen-crossing-sequence",
      "dimension": "strength",
      "value": "Ammen reports departure from Savannah at 13:00 April 6. His separately printed diary describes arrival at Savannah before noon April 5, Nelson crossing first with part of the Thirty-sixth Indiana, and boatloads of three or four companies.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "The April 10 report and diary extracts are separate accounts by one author; the diary composition date is unknown. Boatloads are not measured personnel totals or crossing rates. No arrival clock is inferred from the reported departure.",
      "citations": [
        {
          "source_id": "or-ammen-crossing-v1",
          "section": "p328-report",
          "locator": "p328-report",
          "quote": "April 6, at 1 o'clock p. m., the Tenth Brigade marched from Savannah"
        },
        {
          "source_id": "or-ammen-crossing-v1",
          "section": "p330-diary",
          "locator": "p330-diary",
          "quote": "reached Savannah, Tenn., before 12 m."
        },
        {
          "source_id": "or-ammen-crossing-v1",
          "section": "p333-diary",
          "locator": "p333-diary",
          "quote": "General Nelson went over on the first boat with a part of the Thirty-sixth Indiana"
        },
        {
          "source_id": "or-ammen-crossing-v1",
          "section": "p333-diary",
          "locator": "p333-diary",
          "quote": "only three or four companies could cross on a boat."
        }
      ]
    },
    {
      "id": "ohio-leading-regimental-landings",
      "dimension": "strength",
      "value": "Anderson reports the Sixth Ohio disembarked about 17:00 April 6; Jones reports the Twenty-fourth Ohio landed about 17:30 and initially formed on the river hill.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Regimental landing is separate from deployment and first firing. These reports complicate the handbook sequence rather than establish one common clock or a headcount at 18:00.",
      "citations": [
        {
          "source_id": "or-anderson-crossing-v1",
          "section": "p339",
          "locator": "p339",
          "quote": "The regiment was disembarked at about 5 o'clock on the evening of the 6th instant"
        },
        {
          "source_id": "or-jones-crossing-v1",
          "section": "p339",
          "locator": "p339",
          "quote": "We landed at this place about 5.30 p. m. of the 6th, and were immediately formed in line of battle on the river hill."
        }
      ]
    },
    {
      "id": "grose-sunday-contingent",
      "dimension": "strength",
      "value": "Grose reports the Thirty-sixth Indiana formed after crossing Sunday in eight companies about 400 strong, with two companies left behind on other duty.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "This is the reported leading regimental contingent, not the whole brigade, Nelson division, or a precise 18:00 census. Nelson's separate 380 taken-into-action row has a two-day scope; retain both without treating their difference as losses.",
      "citations": [
        {
          "source_id": "or-grose-crossing-v1",
          "section": "p337",
          "locator": "p337",
          "quote": "two companies having been left behind on other duty"
        },
        {
          "source_id": "or-grose-crossing-v1",
          "section": "p337",
          "locator": "p337",
          "quote": "my regiment was formed (the eight companies about 400 strong)"
        }
      ]
    },
    {
      "id": "nelson-night-infantry-crossing",
      "dimension": "strength",
      "value": "Nelson says all his division's infantry were across by 21:00 April 6.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Infantry completion is not the arrival of every arm of the division, nor proof all fought Sunday. Ammen's later nighttime formation and return of Twenty-fourth Ohio are separate phases.",
      "citations": [
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "p324-night",
          "locator": "p324-night",
          "quote": "By 9 p. m. the infantry of my division were all across the river"
        }
      ]
    },
    {
      "id": "nelson-separated-arms",
      "dimension": "logistics",
      "value": "Nelson reports leaving his three batteries at Savannah. Edward McCook reports the Second Indiana Cavalry stayed on the opposite bank until Monday evening, with detached orderlies the only portion in action.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Transport constraints and administrative assignment are source-qualified facts; no invented readiness score or command effect follows. The cavalry exception is not zero participation for every person.",
      "citations": [
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "p324-artillery",
          "locator": "p324-artillery",
          "quote": "I was compelled to leave the three batteries of my division at Savannah."
        },
        {
          "source_id": "or-edward-mccook-crossing-v1",
          "section": "p354",
          "locator": "p354",
          "quote": "remained there till the evening of the 7th, when they crossed to this side."
        },
        {
          "source_id": "or-edward-mccook-crossing-v1",
          "section": "p354",
          "locator": "p354",
          "quote": "The only portion of my command in the action were men detailed as orderlies"
        },
        {
          "source_id": "or-buell-reinforcements-v2",
          "section": "p292",
          "locator": "p292",
          "quote": "I discovered it to be impracticable for artillery, and General Nelson was directed to leave his to be carried forward by steamers."
        }
      ]
    },
    {
      "id": "nelson-action-strength",
      "dimension": "strength",
      "value": "Nelson reports 4,541 taken into action; the accompanying table covers April 6-7 and gives 380 for the Thirty-sixth Indiana.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "The nine infantry rows sum to 4,541, but this is neither the leading Sunday contingent nor a contemporaneous dawn count. Reed repeats the 4,541 from Nelson rather than independently confirming it. Cavalry orderlies are noted separately in the casualty columns; no unreported personnel addition is inferred.",
      "citations": [
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "p325-strength",
          "locator": "p325-strength",
          "quote": "It went into action 4,541 strong,"
        },
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "p326-return",
          "locator": "p326-return",
          "quote": "36th Indiana | 380"
        },
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "p326-return",
          "locator": "p326-return",
          "quote": "April 6 and 7, 1862."
        },
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "p326-return",
          "locator": "p326-return",
          "quote": "Total in division | 4,541"
        }
      ]
    },
    {
      "id": "nelson-march-paper-strength",
      "dimension": "strength",
      "value": "The compiler's March return abstract prints 6,724 present for duty in Nelson's division, including 890 cavalry; it excludes six division staff.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "The heading gives a reporting month, not an exact muster day. This broader administrative count is distinct from 4,541 taken into action and Reed's March 31 infantry compilation. No subtraction is adopted as a corrected battlefield force.",
      "citations": [
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "p327-march-return",
          "locator": "p327-march-return",
          "quote": "Total | 255 | 6,469 | 6,724 | 9,526 | 18"
        },
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "p327-march-return",
          "locator": "p327-march-return",
          "quote": "for the month of March, 1862."
        },
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "p327-march-return",
          "locator": "p327-march-return",
          "quote": "Cavalry | 32 | 858 | 890"
        },
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "p327-march-return",
          "locator": "p327-march-return",
          "quote": "The division staff (6) not embraced in columns of figures."
        }
      ]
    },
    {
      "id": "crittenden-arrival-phases",
      "dimension": "strength",
      "value": "Crittenden reports landing about 21:00 April 6, deployment about 05:00 April 7, and the Third Kentucky Cavalry remaining opposite the landing for lack of transport.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "This separates boat arrival, debarkation, field position and excluded cavalry. McCook reaching the field later is a relative sequence, not a synchronized whole-army readiness time.",
      "citations": [
        {
          "source_id": "or-crittenden-reinforcements-v1",
          "section": "p355",
          "locator": "p355",
          "quote": "We reached Pittsburg Landing at about 9 o'clock p. m."
        },
        {
          "source_id": "or-crittenden-reinforcements-v1",
          "section": "p355",
          "locator": "p355",
          "quote": "At about 5 a. m. we were conducted to our position by General Buell in person."
        },
        {
          "source_id": "or-crittenden-reinforcements-v1",
          "section": "p354-cavalry",
          "locator": "p354-cavalry",
          "quote": "except Jackson's cavalry, which marched at once to the landing opposite Pittsburg Landing"
        },
        {
          "source_id": "or-crittenden-reinforcements-v1",
          "section": "p354-cavalry",
          "locator": "p354-cavalry",
          "quote": "no transportation could be furnished"
        }
      ]
    },
    {
      "id": "mccook-staged-arrival",
      "dimension": "strength",
      "value": "Alexander McCook reports Savannah arrival at 19:00 April 6, Pittsburg Landing arrival at 05:00 April 7 while Rousseau disembarked, and subsequent arrivals of the other brigades.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "A commander and one disembarking brigade do not establish division-wide readiness. The Second Kentucky Cavalry was left guarding baggage. Grant's general night-arrival statement remains alongside these more specific stages.",
      "citations": [
        {
          "source_id": "or-alexander-mccook-reinforcements-v1",
          "section": "p302",
          "locator": "p302",
          "quote": "arriving at Savannah at 7 p. m. on the 6th instant"
        },
        {
          "source_id": "or-alexander-mccook-reinforcements-v1",
          "section": "p303",
          "locator": "p303",
          "quote": "Arriving at Pittsburg Landing at 5 o'clock a. m. on the 7th instant, finding General Rousseau's brigade disembarking"
        },
        {
          "source_id": "or-alexander-mccook-reinforcements-v1",
          "section": "p303",
          "locator": "p303",
          "quote": "As soon as the remainder of Colonel Kirk's brigade arrived"
        },
        {
          "source_id": "or-alexander-mccook-reinforcements-v1",
          "section": "p303",
          "locator": "p303",
          "quote": "a portion of Colonel Gibson's brigade arrived"
        },
        {
          "source_id": "or-alexander-mccook-reinforcements-v1",
          "section": "p302",
          "locator": "p302",
          "quote": "except the Second Regiment of Kentucky Cavalry, which I was forced to leave to guard the baggage."
        }
      ]
    },
    {
      "id": "wood-late-brigade-arrivals",
      "dimension": "strength",
      "value": "Wood reports reaching Savannah early April 7, Wagner's brigade fully debarked by noon, and his own arrival at 13:00; transport was not immediately available for his cavalry and artillery.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Debarkation does not establish when Wagner reached the fighting line. Buell's late-battle/pursuit description and Garfield's later arrival remain separately scoped; no complete Wood division is added to a dawn population.",
      "citations": [
        {
          "source_id": "or-wood-reinforcements-v1",
          "section": "p377",
          "locator": "p377",
          "quote": "Savannah was reached early on the morning of the 7th"
        },
        {
          "source_id": "or-wood-reinforcements-v1",
          "section": "p377",
          "locator": "p377",
          "quote": "The brigade had fully debarked by 12 m."
        },
        {
          "source_id": "or-wood-reinforcements-v1",
          "section": "p377",
          "locator": "p377",
          "quote": "my own arrival, at 1 p. m."
        },
        {
          "source_id": "or-wood-reinforcements-v1",
          "section": "p377",
          "locator": "p377",
          "quote": "impossible to get transportation immediately for the artillery and cavalry of my division"
        }
      ]
    },
    {
      "id": "garfield-present-not-engaged",
      "dimension": "strength",
      "value": "Garfield reports his three regiments debarked at 13:30 April 7 and reached the front about 15:00; he says they were under artillery fire but not engaged.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Presence, exposure to fire and the author's engagement category remain distinct. His brigade has no admitted strength here; Reed's estimate for Wood includes only Wagner. Do not encode missing strength as zero.",
      "citations": [
        {
          "source_id": "or-garfield-reinforcements-v1",
          "section": "p380",
          "locator": "p380",
          "quote": "debarked at the Pittsburg Landing at 1.30 o'clock p. m. of Monday, the 7th instant."
        },
        {
          "source_id": "or-garfield-reinforcements-v1",
          "section": "p380",
          "locator": "p380",
          "quote": "which I reached about 3 o'clock p. m."
        },
        {
          "source_id": "or-garfield-reinforcements-v1",
          "section": "p380",
          "locator": "p380",
          "quote": "My command was for some time under fire from the batteries of the enemy, but as he was then in retreat, and the tide of battle soon swept farther to the front, we were not engaged."
        }
      ]
    },
    {
      "id": "reed-nelson-return-basis",
      "dimension": "strength",
      "value": "Reed prints 5,535 for duty for Nelson under a March 31 return heading, separately from the 4,541 taken from Nelson's report.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Reed's listed infantry composition differs from the compiler's broader March total of 6,724. The remaining unit/date/accounting differences are not reconciled. Neither is a Sunday-evening crossing census.",
      "citations": [
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p101",
          "locator": "p101",
          "quote": "Total Fourth Division | 5,535 | 4,541"
        },
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p100",
          "locator": "p100",
          "quote": "NELSON'S (FOURTH) DIVISION. (Returns of Mar. 31.)"
        },
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p101",
          "locator": "p101",
          "quote": "General Nelson's report (10 War Records, 326)."
        }
      ]
    },
    {
      "id": "reed-mccook-postbattle-return",
      "dimension": "strength",
      "value": "Reed prints 9,118 present for duty for McCook from an April 30 return, separately from his reconstructed April 7 engaged estimate.",
      "phase": "post_outcome",
      "status": "supported",
      "rationale": "The underlying return date is after the battle. It must not be supplied as a prebattle observation or mechanically substituted for the reconstruction.",
      "citations": [
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p100",
          "locator": "p100",
          "quote": "(Return of Apr. 30.)"
        },
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p100",
          "locator": "p100",
          "quote": "Total Second Division | 332 | 8,786 | 9,118"
        }
      ]
    },
    {
      "id": "reed-ohio-estimates-and-discrepancy",
      "dimension": "strength",
      "value": "Reed's Army of the Ohio reconstruction prints 7,553 for McCook in the detail but 7,552 in the recap; the recap adds Nelson 4,541, Crittenden 3,825 and Wagner 2,000 to total 17,918.",
      "phase": "unresolved",
      "status": "disputed",
      "rationale": "The one-person discrepancy is retained. The McCook/Crittenden estimates draw on mixed-date returns; Wagner is an estimated late arrival. Using 7,553 would give 17,919, a diagnostic calculation, not a corrected total. Components overlap the total and cannot be added again. No number is a synchronized April 7 dawn census.",
      "citations": [
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p100",
          "locator": "p100",
          "quote": "Number Second Division engaged at Shiloh Apr. 7* | 7,553"
        },
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p102",
          "locator": "p102",
          "quote": "Second Division | 7,552"
        },
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p101",
          "locator": "p101",
          "quote": "Number Fifth Division engaged at Shiloh Apr. 7* | [blank] | 3,825"
        },
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p102",
          "locator": "p102",
          "quote": "Twenty-first Brigade† | 2,000"
        },
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p102",
          "locator": "p102",
          "quote": "Total Army of the Ohio | 17,918"
        },
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p101",
          "locator": "p101",
          "quote": "* Approximated. Note j."
        },
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p102",
          "locator": "p102",
          "quote": "Arrived at Shiloh just before the battle ended. Estimated."
        }
      ]
    },
    {
      "id": "reed-buell-letter-secondhand",
      "dimension": "strength",
      "value": "Reed quotes an undated letter on file in which Buell recalls 18,000-19,000 and estimates McCook at 7,552, while Reed notes meager returns and estimation from March 20, March 31 and April 30.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "The underlying letter and its date have not been inspected. Retain the unqualified recalled strength as a secondhand account, not a dated primary return or a new typed population. Force's about 20,000 remains a separate estimate.",
      "citations": [
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p111-note-j",
          "locator": "p111-note-j",
          "quote": "The Second, Fifth, and Sixth Divisions are estimated from returns of March 20, March 31, and April 30, 1862."
        },
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p111-note-j",
          "locator": "p111-note-j",
          "quote": "I do not know whether the information was available at the time of rendering my report, but I have had it in my mind that my strength was between 18,000 and 19,000."
        },
        {
          "source_id": "reed-1909-ohio-strength-v1",
          "section": "p111-note-j",
          "locator": "p111-note-j",
          "quote": "I estimate McCook's present for duty at 7,552."
        }
      ]
    },
    {
      "id": "nelson-sunday-exact-crossed-strength",
      "dimension": "strength",
      "value": null,
      "phase": "unresolved",
      "status": "unknown",
      "rationale": "The inspected primary reports identify successive companies/regiments and about 400 in Grose's formed regiment, but do not establish the handbook's about 600 at 18:00 or an exact common-time Sunday contingent. Its original derivation remains untraced; do not add partial arrivals to whole-regiment returns.",
      "citations": []
    },
    {
      "id": "ammen-night-formation",
      "dimension": "responsibility",
      "value": "Ammen's diary describes forming an advanced line about 22:00 April 6 and receiving the Twenty-fourth Ohio back about midnight.",
      "phase": "unresolved",
      "status": "supported",
      "rationale": "Formation and reassembly are later than landing and infantry crossing completion; exact diary composition date is unestablished. No independent synchronized readiness clock is asserted.",
      "citations": [
        {
          "source_id": "or-ammen-crossing-v1",
          "section": "p334-diary",
          "locator": "p334-diary",
          "quote": "About 10 o'clock at night we commenced forming our new line of battle"
        },
        {
          "source_id": "or-ammen-crossing-v1",
          "section": "p334-diary",
          "locator": "p334-diary",
          "quote": "The Twenty-fourth Ohio Volunteer Infantry was brought back about midnight and formed my second line and reserve."
        }
      ]
    },
    {
      "id": "nelson-morning-phase-clocks",
      "dimension": "responsibility",
      "value": "Nelson reports rousing his men at 04:00 April 7 and commencing action at 05:20; Grose reports his regiment moving with the brigade at 05:30.",
      "phase": "unresolved",
      "status": "disputed",
      "rationale": "These attributed clocks and unit scopes are not synchronized. Preserve them with Buell's soon-after-05:00 advance rather than selecting a precise common start.",
      "citations": [
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "p324-morning",
          "locator": "p324-morning",
          "quote": "At 4 a. m. I roused up the men quietly"
        },
        {
          "source_id": "or-nelson-reinforcements-v1",
          "section": "p324-morning",
          "locator": "p324-morning",
          "quote": "At 5.20 I found them, and the action commenced with vigor."
        },
        {
          "source_id": "or-grose-crossing-v1",
          "section": "p337",
          "locator": "p337",
          "quote": "until 5.30 o'clock the next morning, when we were ordered and moved forward with the brigade"
        }
      ]
    }
  ],
  "open_questions": [
    "Recover Prentiss attachment A or the underlying return to identify all two-regiment/one-battery omissions; resolve the ten-man unattached difference between p.112 and Reed. Do not equate late additions with missing original slots.",
    "Explain the p.396 versus reports 136/137 strength differences, report 137's printed infantry subtotal discrepancies, and how Hill/Carroll/detached cavalry enter the returns. Trace NPS's 44,968 separately; no comparable opening strength is selected.",
    "Audit Reed's 1,727 guard total and untraced secondhand Wallace 5,000; trace Force's 6,500 and the handbook's 5,800. Preserve 7,564 PFD and 5,837 compiled engaged as different populations.",
    "Independently review Nelson/Ammen and regimental clock differences, the handbook's 600-person derivation, and the boundary between landing, deployment and engagement. No synchronized Sunday-evening or Monday-dawn army strength is selected.",
    "Establish receipt/modification of Halleck’s March 20 and April 5 instructions; locate the precise order to await Buell at Pittsburg Landing.",
    "Trace Beauregard’s special dispatch and staff notification of Johnston’s death; do not equate death time with effective command transfer.",
    "Recover the Fifteenth Michigan original report/returns to audit Sunday participation, ammunition and Force's day-specific casualty claim; resolve Reed's narrative/table conflict. Wallace order responsibility remains disputed.",
    "Recover the original Buell letter quoted by Reed; audit the mixed March/April return reconstruction, McCook's 7,553/7,552 discrepancy, missing brigade returns and the inclusion of late Wagner arrivals before selecting any Army of the Ohio comparison population.",
    "Obtain independent historical review of these extractions and proposed boundaries before any feature-admission design."
  ],
  "revision": "shiloh-ohio-reinforcement-audit-2026-09-20",
  "supersedes": {
    "path": "data/evidence/history/TN003.v4.json",
    "sha256": "9ec051462243589cea1efa14ccdffc22cea7c55452483672b7e75acfa5d463dd"
  },
  "entities": [
    {
      "id": "grant",
      "name": "Ulysses S. Grant",
      "kind": "person",
      "side": "US"
    },
    {
      "id": "buell",
      "name": "Don Carlos Buell",
      "kind": "person",
      "side": "US"
    },
    {
      "id": "halleck",
      "name": "Henry W. Halleck",
      "kind": "person",
      "side": "US"
    },
    {
      "id": "lew-wallace",
      "name": "Lew (Lewis) Wallace",
      "kind": "person",
      "side": "US"
    },
    {
      "id": "johnston",
      "name": "Albert Sidney Johnston",
      "kind": "person",
      "side": "CS"
    },
    {
      "id": "beauregard",
      "name": "P. G. T. Beauregard",
      "kind": "person",
      "side": "CS"
    },
    {
      "id": "union-shiloh",
      "name": "Union forces at Shiloh (source-defined scope)",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "army-tennessee",
      "name": "Army of the Tennessee",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "army-ohio",
      "name": "Army of the Ohio",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "wallace-division",
      "name": "Third Division, Army of the Tennessee (Lew Wallace)",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "nelson-leading-contingent",
      "name": "Nelson division leading contingent west of river",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "other-union-regiments",
      "name": "Other Union regiments in Force’s reinforcement account",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "army-mississippi",
      "name": "Confederate Army of the Mississippi",
      "kind": "formation",
      "side": "CS"
    },
    {
      "id": "army-mississippi-infantry",
      "name": "Army of the Mississippi infantry (source-defined return population)",
      "kind": "formation",
      "side": "CS"
    },
    {
      "id": "army-mississippi-artillery",
      "name": "Army of the Mississippi artillery (source-defined return population)",
      "kind": "formation",
      "side": "CS"
    },
    {
      "id": "army-mississippi-cavalry",
      "name": "Army of the Mississippi cavalry (source-defined return population)",
      "kind": "formation",
      "side": "CS"
    },
    {
      "id": "sixth-division",
      "name": "Sixth Division, Army of the Tennessee (Prentiss)",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "sixteenth-iowa",
      "name": "Sixteenth Iowa Infantry",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "eighteenth-wisconsin",
      "name": "Eighteenth Wisconsin Infantry",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "fifteenth-iowa",
      "name": "Fifteenth Iowa Infantry",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "twentythird-missouri",
      "name": "Twenty-third Missouri Infantry",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "fifteenth-michigan",
      "name": "Fifteenth Michigan Infantry",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "fiftysixth-ohio",
      "name": "Fifty-sixth Ohio Infantry",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "sixtyeighth-ohio",
      "name": "Sixty-eighth Ohio Infantry",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "wallace-cavalry",
      "name": "Third battalions, Eleventh Illinois and Fifth Ohio Cavalry (Reed table)",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "wallace-crumps-guard",
      "name": "Wallace detachments left at Crump's Landing (Reed-defined population)",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "nelson",
      "name": "William Nelson",
      "kind": "person",
      "side": "US"
    },
    {
      "id": "ammen",
      "name": "Jacob Ammen",
      "kind": "person",
      "side": "US"
    },
    {
      "id": "nelson-division",
      "name": "Fourth Division, Army of the Ohio (Nelson)",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "ammen-brigade",
      "name": "Tenth Brigade, Fourth Division, Army of the Ohio (Ammen)",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "thirtysixth-indiana",
      "name": "Thirty-sixth Indiana Infantry",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "sixth-ohio",
      "name": "Sixth Ohio Infantry",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "twentyfourth-ohio",
      "name": "Twenty-fourth Ohio Infantry",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "second-indiana-cavalry",
      "name": "Second Indiana Cavalry",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "crittenden-division",
      "name": "Fifth Division, Army of the Ohio (Thomas L. Crittenden)",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "mccook-division",
      "name": "Second Division, Army of the Ohio (Alexander McD. McCook)",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "wood-division",
      "name": "Sixth Division, Army of the Ohio (Thomas J. Wood)",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "wagner-brigade",
      "name": "Twenty-first Brigade, Sixth Division, Army of the Ohio (Wagner)",
      "kind": "formation",
      "side": "US"
    },
    {
      "id": "garfield-brigade",
      "name": "Twentieth Brigade, Sixth Division, Army of the Ohio (Garfield)",
      "kind": "formation",
      "side": "US"
    }
  ],
  "quantities": [
    {
      "id": "nps-union-total",
      "claim_id": "strength-total",
      "citation_index": 0,
      "entity_id": "union-shiloh",
      "unit": "people",
      "lower": 65085,
      "upper": 65085,
      "basis": "reported_engaged",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-06",
        "end": "1862-04-07",
        "label": "Whole engagement"
      },
      "location": "Shiloh",
      "scope": "NPS total for US forces",
      "recorded_at": null,
      "note": "Source precision is not historical certainty; opening availability unestablished."
    },
    {
      "id": "nps-confederate-total",
      "claim_id": "strength-total",
      "citation_index": 0,
      "entity_id": "army-mississippi",
      "unit": "people",
      "lower": 44968,
      "upper": 44968,
      "basis": "reported_engaged",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-06",
        "end": "1862-04-07",
        "label": "Whole engagement"
      },
      "location": "Shiloh",
      "scope": "NPS total for CS forces",
      "recorded_at": null,
      "note": "Different definition/source from Jordan’s effective return; do not substitute silently."
    },
    {
      "id": "union-paper-total",
      "claim_id": "union-return-strength",
      "citation_index": 0,
      "entity_id": "army-tennessee",
      "unit": "people",
      "lower": 44895,
      "upper": 44895,
      "basis": "present_for_duty",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-04",
        "end": "1862-04-05",
        "label": "Dates of underlying returns"
      },
      "location": "Multiple divisional locations, including Wallace away from Pittsburg",
      "scope": "Compiled divisional return aggregates with explicit omissions",
      "recorded_at": null,
      "note": "Contains Wallace’s 7,564; excludes some Sixth Division strengths and division staffs. Not opening combatants."
    },
    {
      "id": "wallace-april4-return",
      "claim_id": "union-return-strength",
      "citation_index": 1,
      "entity_id": "wallace-division",
      "unit": "people",
      "lower": 7564,
      "upper": 7564,
      "basis": "present_for_duty",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-04",
        "end": "1862-04-04",
        "label": "Return dated April 4"
      },
      "location": "Wallace’s divisional station, not April 6 Pittsburg line",
      "scope": "Officers and men present for duty in Third Division",
      "recorded_at": "1862-04-04",
      "note": "Return explicitly says division not in April 6 battle; no assumption all were available for the march."
    },
    {
      "id": "confederate-before",
      "claim_id": "confederate-return-before",
      "citation_index": 1,
      "entity_id": "army-mississippi",
      "unit": "people",
      "lower": 40335,
      "upper": 40335,
      "basis": "reported_effective",
      "estimate_kind": "reported_exact",
      "period": {
        "start": null,
        "end": null,
        "label": "Before Shiloh; underlying muster date unstated"
      },
      "location": "Army participating in Shiloh operation",
      "scope": "Infantry, artillery and cavalry in Jordan’s return",
      "recorded_at": "1862-04-21",
      "note": "Filed April 21; disagreement with other returns explicitly unresolved."
    },
    {
      "id": "confederate-after",
      "claim_id": "confederate-return-after",
      "citation_index": 1,
      "entity_id": "army-mississippi",
      "unit": "people",
      "lower": 29636,
      "upper": 29636,
      "basis": "reported_effective",
      "estimate_kind": "reported_exact",
      "period": {
        "start": null,
        "end": null,
        "label": "After Shiloh; underlying muster date unstated"
      },
      "location": "Army after Shiloh, exact muster location unestablished",
      "scope": "Effective total after battle in Jordan’s return",
      "recorded_at": "1862-04-21",
      "note": "Post-outcome observation; the April 21 forwarding date does not establish an underlying muster date. This is not an April 7 opening estimate."
    },
    {
      "id": "force-sunday-engaged",
      "claim_id": "force-opening-estimate",
      "citation_index": 0,
      "entity_id": "union-shiloh",
      "unit": "people",
      "lower": 32000,
      "upper": 33000,
      "basis": "reported_engaged",
      "estimate_kind": "range",
      "period": {
        "start": "1862-04-06",
        "end": "1862-04-06",
        "label": "Participation over Sunday, not first-contact strength"
      },
      "location": "Shiloh",
      "scope": "Officers, noncommissioned officers and privates Force considers actually engaged",
      "recorded_at": null,
      "note": "Historical estimate range, not confidence interval. Interpretation rests partly on a footnote-corrected calculation."
    },
    {
      "id": "force-buell",
      "claim_id": "force-monday-reinforcements",
      "citation_index": 0,
      "entity_id": "army-ohio",
      "unit": "people",
      "lower": 20000,
      "upper": 20000,
      "basis": "reported_reinforcements",
      "estimate_kind": "approximate",
      "period": {
        "start": "1862-04-07",
        "end": "1862-04-07",
        "label": "Monday reinforcement account; not exact arrival window"
      },
      "location": "Shiloh",
      "scope": "Reinforcements as grouped by Force",
      "recorded_at": null,
      "note": "Rounded later estimate; not all necessarily first arrived Monday. No sum is admitted as dawn availability."
    },
    {
      "id": "force-wallace",
      "claim_id": "force-monday-reinforcements",
      "citation_index": 0,
      "entity_id": "wallace-division",
      "unit": "people",
      "lower": 6500,
      "upper": 6500,
      "basis": "reported_reinforcements",
      "estimate_kind": "approximate",
      "period": {
        "start": "1862-04-07",
        "end": "1862-04-07",
        "label": "Monday reinforcement account; not exact arrival window"
      },
      "location": "Shiloh",
      "scope": "Reinforcements as grouped by Force",
      "recorded_at": null,
      "note": "Rounded later estimate; not all necessarily first arrived Monday. No sum is admitted as dawn availability."
    },
    {
      "id": "force-other",
      "claim_id": "force-monday-reinforcements",
      "citation_index": 0,
      "entity_id": "other-union-regiments",
      "unit": "people",
      "lower": 1400,
      "upper": 1400,
      "basis": "reported_reinforcements",
      "estimate_kind": "approximate",
      "period": {
        "start": "1862-04-07",
        "end": "1862-04-07",
        "label": "Monday reinforcement account; not exact arrival window"
      },
      "location": "Shiloh",
      "scope": "Reinforcements as grouped by Force",
      "recorded_at": null,
      "note": "Rounded later estimate; not all necessarily first arrived Monday. No sum is admitted as dawn availability."
    },
    {
      "id": "handbook-wallace",
      "claim_id": "wallace-handbook-strength",
      "citation_index": 0,
      "entity_id": "wallace-division",
      "unit": "people",
      "lower": 5800,
      "upper": 5800,
      "basis": "reported_reinforcements",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-06",
        "end": "1862-04-06",
        "label": "Arrival after dark in handbook narrative"
      },
      "location": "Shiloh",
      "scope": "Division arriving after dark; strength basis not specified",
      "recorded_at": null,
      "note": "Reported number as written, not validated exact headcount; conflicts in scope or magnitude with Force and field return remain."
    },
    {
      "id": "handbook-nelson-leading",
      "claim_id": "nelson-evening-crossing",
      "citation_index": 0,
      "entity_id": "nelson-leading-contingent",
      "unit": "people",
      "lower": 600,
      "upper": 600,
      "basis": "reported_present",
      "estimate_kind": "approximate",
      "period": {
        "start": "1862-04-06",
        "end": "1862-04-06",
        "label": "By 18:00 as reported by handbook"
      },
      "location": "West bank of Tennessee River, in line",
      "scope": "Leading contingent of Nelson’s division",
      "recorded_at": null,
      "note": "Not Nelson’s complete division or Buell’s army; approximate number and source-reported time."
    },
    {
      "id": "confederate-report-136-total",
      "claim_id": "confederate-report-136",
      "citation_index": 0,
      "entity_id": "army-mississippi",
      "unit": "people",
      "lower": 38773,
      "upper": 38773,
      "basis": "reported_effective",
      "estimate_kind": "reported_exact",
      "period": {
        "start": null,
        "end": null,
        "label": "Heading describes forces that marched April 3; exact muster date unstated; Monday-arrival footnote retained"
      },
      "location": "Corinth-to-Tennessee River operation; no single muster location stated",
      "scope": "Report 136 printed grand total, infantry/artillery/cavalry in Present, Effective total column",
      "recorded_at": "1862-06-30",
      "note": "Recorded_at is the bracketed submission/forwarding date. Preserve printed value; no feature admission. Not verified April 6 opening availability; footnote mentions a Monday arrival."
    },
    {
      "id": "confederate-report-136-infantry",
      "claim_id": "confederate-report-136",
      "citation_index": 1,
      "entity_id": "army-mississippi-infantry",
      "unit": "people",
      "lower": 34727,
      "upper": 34727,
      "basis": "reported_effective",
      "estimate_kind": "reported_exact",
      "period": {
        "start": null,
        "end": null,
        "label": "Heading describes forces that marched April 3; exact muster date unstated; Monday-arrival footnote retained"
      },
      "location": "Corinth-to-Tennessee River operation; no single muster location stated",
      "scope": "Report 136 printed infantry subtotal in Present, Effective total column",
      "recorded_at": "1862-06-30",
      "note": "Recorded_at is the bracketed submission/forwarding date. Preserve printed value; no feature admission. Not verified April 6 opening availability; footnote mentions a Monday arrival."
    },
    {
      "id": "confederate-report-136-artillery",
      "claim_id": "confederate-report-136",
      "citation_index": 2,
      "entity_id": "army-mississippi-artillery",
      "unit": "people",
      "lower": 1973,
      "upper": 1973,
      "basis": "reported_effective",
      "estimate_kind": "reported_exact",
      "period": {
        "start": null,
        "end": null,
        "label": "Heading describes forces that marched April 3; exact muster date unstated; Monday-arrival footnote retained"
      },
      "location": "Corinth-to-Tennessee River operation; no single muster location stated",
      "scope": "Report 136 printed artillery subtotal in Present, Effective total column",
      "recorded_at": "1862-06-30",
      "note": "Recorded_at is the bracketed submission/forwarding date. Preserve printed value; no feature admission. Not verified April 6 opening availability; footnote mentions a Monday arrival."
    },
    {
      "id": "confederate-report-136-cavalry",
      "claim_id": "confederate-report-136",
      "citation_index": 3,
      "entity_id": "army-mississippi-cavalry",
      "unit": "people",
      "lower": 2073,
      "upper": 2073,
      "basis": "reported_effective",
      "estimate_kind": "reported_exact",
      "period": {
        "start": null,
        "end": null,
        "label": "Heading describes forces that marched April 3; exact muster date unstated; Monday-arrival footnote retained"
      },
      "location": "Corinth-to-Tennessee River operation; no single muster location stated",
      "scope": "Report 136 printed cavalry subtotal in Present, Effective total column",
      "recorded_at": "1862-06-30",
      "note": "Recorded_at is the bracketed submission/forwarding date. Preserve printed value; no feature admission. Not verified April 6 opening availability; footnote mentions a Monday arrival."
    },
    {
      "id": "confederate-report-137-total",
      "claim_id": "confederate-report-137",
      "citation_index": 0,
      "entity_id": "army-mississippi",
      "unit": "people",
      "lower": 32212,
      "upper": 32212,
      "basis": "reported_effective",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-10",
        "end": "1862-04-10",
        "label": "After-battle return dated April 10 in heading; underlying unit muster timing unverified"
      },
      "location": "Army of the Mississippi after Shiloh; exact muster location unstated",
      "scope": "Report 137 printed grand total, infantry/artillery/cavalry in Present, Effective total column",
      "recorded_at": "1862-06-30",
      "note": "Recorded_at is the bracketed submission/forwarding date. Preserve printed value; no feature admission. Post-outcome; composition changes and internal arithmetic discrepancies remain unresolved. Printed branch subtotal is not replaced by the sum of corps rows. No April 10 date is imputed to the separate p.396 return."
    },
    {
      "id": "confederate-report-137-infantry",
      "claim_id": "confederate-report-137",
      "citation_index": 1,
      "entity_id": "army-mississippi-infantry",
      "unit": "people",
      "lower": 26697,
      "upper": 26697,
      "basis": "reported_effective",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-10",
        "end": "1862-04-10",
        "label": "After-battle return dated April 10 in heading; underlying unit muster timing unverified"
      },
      "location": "Army of the Mississippi after Shiloh; exact muster location unstated",
      "scope": "Report 137 printed infantry subtotal in Present, Effective total column",
      "recorded_at": "1862-06-30",
      "note": "Recorded_at is the bracketed submission/forwarding date. Preserve printed value; no feature admission. Post-outcome; composition changes and internal arithmetic discrepancies remain unresolved. Printed branch subtotal is not replaced by the sum of corps rows. No April 10 date is imputed to the separate p.396 return."
    },
    {
      "id": "confederate-report-137-artillery",
      "claim_id": "confederate-report-137",
      "citation_index": 2,
      "entity_id": "army-mississippi-artillery",
      "unit": "people",
      "lower": 1682,
      "upper": 1682,
      "basis": "reported_effective",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-10",
        "end": "1862-04-10",
        "label": "After-battle return dated April 10 in heading; underlying unit muster timing unverified"
      },
      "location": "Army of the Mississippi after Shiloh; exact muster location unstated",
      "scope": "Report 137 printed artillery subtotal in Present, Effective total column",
      "recorded_at": "1862-06-30",
      "note": "Recorded_at is the bracketed submission/forwarding date. Preserve printed value; no feature admission. Post-outcome; composition changes and internal arithmetic discrepancies remain unresolved. Printed branch subtotal is not replaced by the sum of corps rows. No April 10 date is imputed to the separate p.396 return."
    },
    {
      "id": "confederate-report-137-cavalry",
      "claim_id": "confederate-report-137",
      "citation_index": 3,
      "entity_id": "army-mississippi-cavalry",
      "unit": "people",
      "lower": 3833,
      "upper": 3833,
      "basis": "reported_effective",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-10",
        "end": "1862-04-10",
        "label": "After-battle return dated April 10 in heading; underlying unit muster timing unverified"
      },
      "location": "Army of the Mississippi after Shiloh; exact muster location unstated",
      "scope": "Report 137 printed cavalry subtotal in Present, Effective total column",
      "recorded_at": "1862-06-30",
      "note": "Recorded_at is the bracketed submission/forwarding date. Preserve printed value; no feature admission. Post-outcome; composition changes and internal arithmetic discrepancies remain unresolved. Printed branch subtotal is not replaced by the sum of corps rows. No April 10 date is imputed to the separate p.396 return."
    },
    {
      "id": "sixth-april5-abstract",
      "claim_id": "sixth-division-return-components",
      "citation_index": 0,
      "entity_id": "sixth-division",
      "unit": "people",
      "lower": 5463,
      "upper": 5463,
      "basis": "present_for_duty",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-05",
        "end": "1862-04-05",
        "label": "Return date in compiler abstract"
      },
      "location": "Sixth Division administrative return",
      "scope": "Includes reported brigade and unattached totals; explicit unnamed omissions",
      "recorded_at": null,
      "note": "Not opening combatants; date of compiler preparation is not the return date."
    },
    {
      "id": "reed-sixth-reconstruction",
      "claim_id": "reed-sixth-division-reconstruction",
      "citation_index": 0,
      "entity_id": "sixth-division",
      "unit": "people",
      "lower": 7545,
      "upper": 7545,
      "basis": "present_for_duty",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-05",
        "end": "1862-04-06",
        "label": "April 5 heading with April 6 arrivals explicitly added in notes"
      },
      "location": "Sixth Division, source compilation",
      "scope": "Later reconstruction including estimated entries and arrivals",
      "recorded_at": null,
      "note": "Printed exact total contains estimates and mixed dates. Not a corrected original return or a single-time census."
    },
    {
      "id": "reed-eighteenth-wisconsin-estimate",
      "claim_id": "eighteenth-wisconsin-return-omission",
      "citation_index": 1,
      "entity_id": "eighteenth-wisconsin",
      "unit": "people",
      "lower": 735,
      "upper": 735,
      "basis": "present_for_duty",
      "estimate_kind": "reported_exact",
      "period": {
        "start": null,
        "end": null,
        "label": "Estimated entry under April 5 heading; exact observation time unestablished"
      },
      "location": "Prentiss division",
      "scope": "Regiment later added to compiled table",
      "recorded_at": null,
      "note": "Asterisk means Estimated. reported_exact preserves printed precision only, not an exact measured population."
    },
    {
      "id": "rousseau-michigan-contingent",
      "claim_id": "rousseau-michigan-monday-contingent",
      "citation_index": 0,
      "entity_id": "fifteenth-michigan",
      "unit": "people",
      "lower": 230,
      "upper": 230,
      "basis": "reported_reinforcements",
      "estimate_kind": "approximate",
      "period": {
        "start": "1862-04-07",
        "end": "1862-04-07",
        "label": "Early morning April 7, report context"
      },
      "location": "Rousseau brigade at Shiloh",
      "scope": "Officers and men joining Oliver; a contingent, not whole-regiment strength",
      "recorded_at": "1862-04-12",
      "note": "About 230 as reported; not Sunday losses or opening availability."
    },
    {
      "id": "reed-wallace-detached",
      "claim_id": "wallace-reed-detachment-counts",
      "citation_index": 0,
      "entity_id": "wallace-crumps-guard",
      "unit": "people",
      "lower": 1727,
      "upper": 1727,
      "basis": "reported_present",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-06",
        "end": "1862-04-06",
        "label": "Left at Crump's Landing when division marched"
      },
      "location": "Crump's Landing",
      "scope": "Two infantry regiments, two cavalry battalions, one gun and train guard",
      "recorded_at": null,
      "note": "Later reported detachment total; not a primary personnel muster. Overlaps the component observations."
    },
    {
      "id": "reed-wallace-engaged",
      "claim_id": "wallace-reed-detachment-counts",
      "citation_index": 4,
      "entity_id": "wallace-division",
      "unit": "people",
      "lower": 5837,
      "upper": 5837,
      "basis": "reported_engaged",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-07",
        "end": "1862-04-07",
        "label": "Reed recapitulation calls this April 7 reinforcement"
      },
      "location": "Shiloh",
      "scope": "Third Division after deduction of Crump's guard",
      "recorded_at": null,
      "note": "Reed p.93 calls this actually engaged. Uses his stated PFD-as-engaged convention, not an opening firing-line census."
    },
    {
      "id": "reed-fiftysixth-return",
      "claim_id": "wallace-reed-detachment-counts",
      "citation_index": 1,
      "entity_id": "fiftysixth-ohio",
      "unit": "people",
      "lower": 701,
      "upper": 701,
      "basis": "present_for_duty",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-04",
        "end": "1862-04-04",
        "label": "Third Division return date; not April 6 detachment muster"
      },
      "location": "Wallace division stations",
      "scope": "Selected component of division return, later identified as detached",
      "recorded_at": null,
      "note": "April 4 administrative strength is not proof every person was in the April 6 guard. Do not add to the overlapping 1,727 or 7,564 totals."
    },
    {
      "id": "reed-sixtyeighth-return",
      "claim_id": "wallace-reed-detachment-counts",
      "citation_index": 2,
      "entity_id": "sixtyeighth-ohio",
      "unit": "people",
      "lower": 424,
      "upper": 424,
      "basis": "present_for_duty",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-04",
        "end": "1862-04-04",
        "label": "Third Division return date; not April 6 detachment muster"
      },
      "location": "Wallace division stations",
      "scope": "Selected component of division return, later identified as detached",
      "recorded_at": null,
      "note": "April 4 administrative strength is not proof every person was in the April 6 guard. Do not add to the overlapping 1,727 or 7,564 totals."
    },
    {
      "id": "reed-wallace-cavalry-return",
      "claim_id": "wallace-reed-detachment-counts",
      "citation_index": 3,
      "entity_id": "wallace-cavalry",
      "unit": "people",
      "lower": 559,
      "upper": 559,
      "basis": "present_for_duty",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-04",
        "end": "1862-04-04",
        "label": "Third Division return date; not April 6 detachment muster"
      },
      "location": "Wallace division stations",
      "scope": "Selected component of division return, later identified as detached",
      "recorded_at": null,
      "note": "April 4 administrative strength is not proof every person was in the April 6 guard. Do not add to the overlapping 1,727 or 7,564 totals."
    },
    {
      "id": "grose-sunday-eight-companies",
      "claim_id": "grose-sunday-contingent",
      "citation_index": 1,
      "entity_id": "thirtysixth-indiana",
      "unit": "people",
      "lower": 400,
      "upper": 400,
      "basis": "reported_present",
      "estimate_kind": "approximate",
      "period": {
        "start": "1862-04-06",
        "end": "1862-04-06",
        "label": "After crossing and forming, Sunday evening"
      },
      "location": "Pittsburg Landing",
      "scope": "Eight companies, two others left on other duty",
      "recorded_at": "1862-04-08",
      "note": "About 400, not an exact 18:00 census; overlaps later whole-action regiment observation."
    },
    {
      "id": "nelson-taken-into-action",
      "claim_id": "nelson-action-strength",
      "citation_index": 0,
      "entity_id": "nelson-division",
      "unit": "people",
      "lower": 4541,
      "upper": 4541,
      "basis": "reported_engaged",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-06",
        "end": "1862-04-07",
        "label": "Report/table scope: April 6 and 7 battle"
      },
      "location": "Shiloh",
      "scope": "Division taken into action, nine listed infantry regiments",
      "recorded_at": "1862-04-10",
      "note": "Not the Sunday leading contingent or a dawn readiness count; repeated by Reed from this report."
    },
    {
      "id": "nelson-thirtysixth-taken-into-action",
      "claim_id": "nelson-action-strength",
      "citation_index": 1,
      "entity_id": "thirtysixth-indiana",
      "unit": "people",
      "lower": 380,
      "upper": 380,
      "basis": "reported_engaged",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-06",
        "end": "1862-04-07",
        "label": "Attached table headed battle April 6 and 7"
      },
      "location": "Shiloh",
      "scope": "Regimental row within the overlapping 4,541 total",
      "recorded_at": null,
      "note": "Do not subtract from Grose's about 400 to infer losses. Attached table has no independently established preparation date."
    },
    {
      "id": "nelson-march-abstract",
      "claim_id": "nelson-march-paper-strength",
      "citation_index": 0,
      "entity_id": "nelson-division",
      "unit": "people",
      "lower": 6724,
      "upper": 6724,
      "basis": "present_for_duty",
      "estimate_kind": "reported_exact",
      "period": {
        "start": null,
        "end": null,
        "label": "Return for month of March 1862; exact muster day unstated"
      },
      "location": "Nelson division administrative return",
      "scope": "Infantry brigade and cavalry aggregates; division staff excluded",
      "recorded_at": null,
      "note": "Includes 890 cavalry; not a census of crossing or battlefield participation."
    },
    {
      "id": "reed-nelson-march31",
      "claim_id": "reed-nelson-return-basis",
      "citation_index": 0,
      "entity_id": "nelson-division",
      "unit": "people",
      "lower": 5535,
      "upper": 5535,
      "basis": "present_for_duty",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-03-31",
        "end": "1862-03-31",
        "label": "Reed heading: returns of March 31"
      },
      "location": "Nelson division, later compiled infantry rows",
      "scope": "For-duty infantry compilation; not the broader OR March population",
      "recorded_at": null,
      "note": "Source/date/composition differences from 6,724 remain unresolved."
    },
    {
      "id": "reed-mccook-april30",
      "claim_id": "reed-mccook-postbattle-return",
      "citation_index": 1,
      "entity_id": "mccook-division",
      "unit": "people",
      "lower": 9118,
      "upper": 9118,
      "basis": "present_for_duty",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-30",
        "end": "1862-04-30",
        "label": "Reed heading: return of April 30"
      },
      "location": "McCook division administrative return",
      "scope": "Post-battle for-duty total, distinct from April 7 estimate",
      "recorded_at": "1862-04-30",
      "note": "Post-outcome observation; cannot enter a predecision feature as known battlefield strength."
    },
    {
      "id": "reed-mccook-detail-engaged",
      "claim_id": "reed-ohio-estimates-and-discrepancy",
      "citation_index": 0,
      "entity_id": "mccook-division",
      "unit": "people",
      "lower": 7553,
      "upper": 7553,
      "basis": "reported_engaged",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-07",
        "end": "1862-04-07",
        "label": "Reed detail: April 7 engaged"
      },
      "location": "Shiloh",
      "scope": "Reed retrospective reconstruction, not synchronized availability",
      "recorded_at": null,
      "note": "Printed 7,553; marked Approximated. Different from 7,552 in recap and note j. reported_exact retains printed precision, not measurement accuracy."
    },
    {
      "id": "reed-mccook-recap-engaged",
      "claim_id": "reed-ohio-estimates-and-discrepancy",
      "citation_index": 1,
      "entity_id": "mccook-division",
      "unit": "people",
      "lower": 7552,
      "upper": 7552,
      "basis": "reported_engaged",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-07",
        "end": "1862-04-07",
        "label": "Reed recap: battle engaged"
      },
      "location": "Shiloh",
      "scope": "Reed retrospective reconstruction, not synchronized availability",
      "recorded_at": null,
      "note": "Printed 7,552, supported by secondhand estimate in note j; differs from detail by one. reported_exact retains printed precision, not measurement accuracy."
    },
    {
      "id": "reed-crittenden-engaged",
      "claim_id": "reed-ohio-estimates-and-discrepancy",
      "citation_index": 2,
      "entity_id": "crittenden-division",
      "unit": "people",
      "lower": 3825,
      "upper": 3825,
      "basis": "reported_engaged",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-07",
        "end": "1862-04-07",
        "label": "Reed detail: April 7 engaged"
      },
      "location": "Shiloh",
      "scope": "Reed retrospective reconstruction, not synchronized availability",
      "recorded_at": null,
      "note": "Marked Approximated. Fourteenth Brigade lacks March/April reports in this compilation. reported_exact retains printed precision, not measurement accuracy."
    },
    {
      "id": "reed-wagner-late-estimate",
      "claim_id": "reed-ohio-estimates-and-discrepancy",
      "citation_index": 3,
      "entity_id": "wagner-brigade",
      "unit": "people",
      "lower": 2000,
      "upper": 2000,
      "basis": "reported_engaged",
      "estimate_kind": "approximate",
      "period": {
        "start": "1862-04-07",
        "end": "1862-04-07",
        "label": "Reed: late April 7 arrival"
      },
      "location": "Shiloh",
      "scope": "Reed retrospective reconstruction, not synchronized availability",
      "recorded_at": null,
      "note": "Explicitly estimated rounded point; only Wagner included for Wood. Not a dawn reinforcement count; no uncertainty interval supplied."
    },
    {
      "id": "reed-ohio-total-engaged",
      "claim_id": "reed-ohio-estimates-and-discrepancy",
      "citation_index": 4,
      "entity_id": "army-ohio",
      "unit": "people",
      "lower": 17918,
      "upper": 17918,
      "basis": "reported_engaged",
      "estimate_kind": "reported_exact",
      "period": {
        "start": "1862-04-07",
        "end": "1862-04-07",
        "label": "Reed recap: Army of the Ohio battle total"
      },
      "location": "Shiloh",
      "scope": "Reed retrospective reconstruction, not synchronized availability",
      "recorded_at": null,
      "note": "Includes estimated and differently timed components; uses 7,552, not detail 7,553. Overlaps all component observations. reported_exact retains printed precision, not measurement accuracy."
    }
  ],
  "events": [
    {
      "id": "halleck-concentration-order",
      "date": "1862-03-20",
      "time_label": "Issue date only; receipt time unknown",
      "entity_ids": [
        "halleck",
        "grant"
      ],
      "claim_ids": [
        "await-buell"
      ],
      "note": "A superior’s constraint; not yet a campaign replacement boundary."
    },
    {
      "id": "union-command-order",
      "date": "1862-04-05",
      "time_label": "Issue date only; receipt time unknown",
      "entity_ids": [
        "halleck",
        "grant",
        "buell"
      ],
      "claim_ids": [
        "union-command-authority"
      ],
      "note": "Separate command plus conditional general authority; distinguish authorization from actual tactical direction."
    },
    {
      "id": "johnston-death",
      "date": "1862-04-06",
      "time_label": "About 14:30, source-reported local time",
      "entity_ids": [
        "johnston",
        "beauregard"
      ],
      "claim_ids": [
        "command-transfer"
      ],
      "note": "Time is the reported death, not a measured timestamp for Beauregard’s notification or effective assumption."
    },
    {
      "id": "nelson-leading-crossing",
      "date": "1862-04-06",
      "time_label": "17:00 opposite landing; about 600 in line by 18:00, handbook account",
      "entity_ids": [
        "nelson-leading-contingent",
        "buell"
      ],
      "claim_ids": [
        "nelson-evening-crossing"
      ],
      "note": "Preserved handbook account of leading contingent. Primary clocks and its 600-person basis remain unresolved; see separately attributed arrival events."
    },
    {
      "id": "wallace-late-arrival",
      "date": "1862-04-06",
      "time_label": "After dark; no precise clock time adopted",
      "entity_ids": [
        "lew-wallace",
        "wallace-division"
      ],
      "claim_ids": [
        "wallace-handbook-strength",
        "wallace-order-dispute",
        "wallace-reported-night-deployment"
      ],
      "note": "Absence from Sunday fighting is separable from disputed responsibility for the delay."
    },
    {
      "id": "april7-deployment",
      "date": "1862-04-07",
      "time_label": "Soon after 05:00 for Nelson/Crittenden; McCook later during deployment",
      "entity_ids": [
        "buell",
        "army-ohio"
      ],
      "claim_ids": [
        "buell-divisions-arrive"
      ],
      "note": "Buell’s sequence does not establish that the entire reinforcement total was on the line at dawn."
    },
    {
      "id": "limited-pursuit",
      "date": "1862-04-07",
      "time_label": "After main battle; subsequent reconnaissance described separately",
      "entity_ids": [
        "grant",
        "buell",
        "army-mississippi"
      ],
      "claim_ids": [
        "pursuit-and-campaign"
      ],
      "note": "Preserve distinction between occupying the field and destroying the opposing force."
    },
    {
      "id": "michigan-arrival",
      "date": "1862-04-05",
      "time_label": "Day before April 6-7 battle; no clock supplied",
      "entity_ids": [
        "fifteenth-michigan"
      ],
      "claim_ids": [
        "michigan-arrival-and-casualty-scope",
        "reed-michigan-sunday-conflict"
      ],
      "note": "Reported landing arrival; Sunday ammunition and participation remain separately qualified."
    },
    {
      "id": "eighteenth-wisconsin-arrival",
      "date": "1862-04-05",
      "time_label": "Saturday afternoon, Reed account",
      "entity_ids": [
        "eighteenth-wisconsin",
        "sixth-division"
      ],
      "claim_ids": [
        "eighteenth-wisconsin-return-omission"
      ],
      "note": "Arrival after the morning return, not an inferred measured opening strength."
    },
    {
      "id": "fifteenth-iowa-arrival",
      "date": "1862-04-06",
      "time_label": "Sunday morning; firing already begun when Reid reported in person",
      "entity_ids": [
        "fifteenth-iowa",
        "sixth-division"
      ],
      "claim_ids": [
        "fifteenth-iowa-sunday-arrival"
      ],
      "note": "Separate transport arrival, disembarkation, ammunition issue and eventual fighting."
    },
    {
      "id": "twentythird-missouri-joins",
      "date": "1862-04-06",
      "time_label": "At Prentiss's reported 9.05 a.m. reformation; Reed says about 9",
      "entity_ids": [
        "twentythird-missouri",
        "sixth-division"
      ],
      "claim_ids": [
        "twentythird-missouri-sunday-arrival"
      ],
      "note": "Attributed retrospective clock, not a verified precise timestamp."
    },
    {
      "id": "wallace-crumps-detachment",
      "date": "1862-04-06",
      "time_label": "After reported 11.30 order; no independent dispatch/receipt clock",
      "entity_ids": [
        "lew-wallace",
        "fiftysixth-ohio",
        "sixtyeighth-ohio",
        "wallace-crumps-guard"
      ],
      "claim_ids": [
        "wallace-detachment-orders",
        "wallace-reed-detachment-counts"
      ],
      "note": "Primary named detachment and later compiled count remain distinct evidence."
    },
    {
      "id": "wallace-night-readiness",
      "date": "1862-04-07",
      "time_label": "About 1 o'clock at night, Wallace account",
      "entity_ids": [
        "lew-wallace",
        "wallace-division"
      ],
      "claim_ids": [
        "wallace-reported-night-deployment"
      ],
      "note": "Date follows the narrated April 6 nightfall arrival. No exact arrival or causal responsibility inferred."
    },
    {
      "id": "michigan-joins-rousseau",
      "date": "1862-04-07",
      "time_label": "Early morning, Rousseau account",
      "entity_ids": [
        "fifteenth-michigan",
        "army-ohio"
      ],
      "claim_ids": [
        "rousseau-michigan-monday-contingent"
      ],
      "note": "About 230 joining officers and men, not a whole-regiment or day-one denominator."
    },
    {
      "id": "ammen-savannah-arrival",
      "date": "1862-04-05",
      "time_label": "Before noon, Ammen diary",
      "entity_ids": [
        "ammen",
        "ammen-brigade"
      ],
      "claim_ids": [
        "ammen-crossing-sequence"
      ],
      "note": "Savannah arrival is not Pittsburg arrival; diary composition date unknown."
    },
    {
      "id": "nelson-savannah-departure",
      "date": "1862-04-06",
      "time_label": "13:00 Ammen; 13:30 Nelson; no common clock selected",
      "entity_ids": [
        "nelson",
        "ammen-brigade",
        "nelson-division"
      ],
      "claim_ids": [
        "ammen-crossing-sequence",
        "nelson-crossing-clock-dispute"
      ],
      "note": "Leading brigade and division scopes differ; retain reported times."
    },
    {
      "id": "ohio-regiments-sunday-landing",
      "date": "1862-04-06",
      "time_label": "About 17:00 Sixth Ohio; about 17:30 Twenty-fourth Ohio, respective reports",
      "entity_ids": [
        "sixth-ohio",
        "twentyfourth-ohio"
      ],
      "claim_ids": [
        "ohio-leading-regimental-landings"
      ],
      "note": "Different regiments and clocks; no sum of simultaneously ready troops."
    },
    {
      "id": "grose-sunday-formation",
      "date": "1862-04-06",
      "time_label": "After crossing, before dusk; no exact clock given",
      "entity_ids": [
        "thirtysixth-indiana"
      ],
      "claim_ids": [
        "grose-sunday-contingent"
      ],
      "note": "About 400 in eight companies formed, not the whole brigade."
    },
    {
      "id": "nelson-infantry-crossing-complete",
      "date": "1862-04-06",
      "time_label": "By 21:00, Nelson report",
      "entity_ids": [
        "nelson-division"
      ],
      "claim_ids": [
        "nelson-night-infantry-crossing",
        "nelson-separated-arms"
      ],
      "note": "Infantry only; batteries and cavalry have different transport histories."
    },
    {
      "id": "ammen-night-reassembly",
      "date": "1862-04-06",
      "time_label": "About 22:00 line forming; Twenty-fourth Ohio back about midnight",
      "entity_ids": [
        "ammen-brigade",
        "twentyfourth-ohio"
      ],
      "claim_ids": [
        "ammen-night-formation"
      ],
      "note": "April 6 night extending toward April 7; qualitative midnight boundary not artificially resolved."
    },
    {
      "id": "crittenden-night-landing",
      "date": "1862-04-06",
      "time_label": "About 21:00 at landing, Crittenden report",
      "entity_ids": [
        "crittenden-division"
      ],
      "claim_ids": [
        "crittenden-arrival-phases"
      ],
      "note": "Debarkation followed; cavalry excluded. Deployment reported about 05:00 next day."
    },
    {
      "id": "mccook-savannah-arrival",
      "date": "1862-04-06",
      "time_label": "19:00, Alexander McCook report",
      "entity_ids": [
        "mccook-division"
      ],
      "claim_ids": [
        "mccook-staged-arrival"
      ],
      "note": "Savannah, not battlefield; cavalry left as baggage guard."
    },
    {
      "id": "mccook-landing-and-brigade-arrivals",
      "date": "1862-04-07",
      "time_label": "05:00 commander arrival with Rousseau disembarking; other brigades follow",
      "entity_ids": [
        "mccook-division"
      ],
      "claim_ids": [
        "mccook-staged-arrival"
      ],
      "note": "Not a whole-division readiness clock."
    },
    {
      "id": "nelson-morning-advance",
      "date": "1862-04-07",
      "time_label": "04:00 rousing and 05:20 action, Nelson; 05:30 movement, Grose",
      "entity_ids": [
        "nelson-division",
        "thirtysixth-indiana"
      ],
      "claim_ids": [
        "nelson-morning-phase-clocks"
      ],
      "note": "Attributions and unit scopes preserved; no precise common start adopted."
    },
    {
      "id": "wood-brigades-land-and-advance",
      "date": "1862-04-07",
      "time_label": "Wagner debarked by noon, Wood account; Garfield 13:30 landing and about 15:00 front",
      "entity_ids": [
        "wagner-brigade",
        "garfield-brigade",
        "wood-division"
      ],
      "claim_ids": [
        "wood-late-brigade-arrivals",
        "garfield-present-not-engaged"
      ],
      "note": "Landing, front arrival, exposure and engagement are different stages."
    },
    {
      "id": "nelson-cavalry-evening-crossing",
      "date": "1862-04-07",
      "time_label": "Evening, Edward McCook report",
      "entity_ids": [
        "second-indiana-cavalry"
      ],
      "claim_ids": [
        "nelson-separated-arms"
      ],
      "note": "Orderlies participated separately; no invented exact hour or personnel total."
    }
  ]
}
```

## Cited source snapshots

Full selected-text snapshots follow, including their editorial scope notes.
CSV evidence includes the complete cited row. Full original CSVs remain in the ZIP.

### arnold-cwsac-battles

Path: `data/raw/cwsac_battles.csv`.
SHA-256: `952b5d08402a7b77a42de709a87cd96540e460dd6fd4911d30574b5ad3585f1f`.

```json
[
  {
    "battle": "TN003",
    "url": "http://www.nps.gov/abpp/battles/tn003.htm",
    "battle_name": "Shiloh",
    "other_names": "Pittsburg Landing",
    "state": "TN",
    "locations": "Hardin County, TN",
    "campaign": "Federal Penetration up the Cumberland and Tennessee Rivers [February-June 1862]",
    "start_date": "1862-04-06",
    "end_date": "1862-04-07",
    "operation": "0",
    "assoc_battles": "",
    "results_text": "Union victory",
    "result": "Union",
    "forces_text": "Army of the Tennessee and Army of the Ohio (65,085) [US]; Army of the Mississippi (44,968) [CS]",
    "strength": "",
    "casualties_text": "23,746 total (US 13,047; CS 10,699)",
    "casualties": "23746",
    "description": "As a result of the fall of Forts Henry and Donelson, Confederate Gen. Albert Sidney Johnston, the commander in the area, was forced to fall back, giving up Kentucky and much of West and Middle Tennessee. He chose Corinth, Mississippi, a major transportation center, as the staging area for an offensive against Maj. Gen. Ulysses S. Grant and his Army of the Tennessee before the Army of the Ohio, under Maj. Gen. Don Carlos Buell, could join it. The Confederate retrenchment was a surprise, although a pleasant one, to the Union forces, and it took Grant, with about 40,000 men, some time to mount a southern offensive, along the Tennessee River, toward Pittsburg Landing. Grant received orders to await Buell's Army of the Ohio at Pittsburg Landing. Grant did not choose to fortify his position; rather, he set about drilling his men many of which were raw recruits. Johnston originally planned to attack Grant on April 4, but delays postponed it until the 6th. Attacking the Union troops on the morning of the 6th, the Confederates surprised them, routing many. Some Federals made determined stands and by afternoon, they had established a battle line at the sunken road, known as the \"Hornets Nest.\" Repeated Rebel attacks failed to carry the Hornets Nest, but massed artillery helped to turn the tide as Confederates surrounded the Union troops and captured, killed, or wounded most. Johnston had been mortally wounded earlier and his second in command, Gen. P.G.T. Beauregard, took over. The Union troops established another line covering Pittsburg Landing, anchored with artillery and augmented by Buell's men who began to arrive and take up positions. Fighting continued until after dark, but the Federals held. By the next morning, the combined Federal forces numbered about 40,000, outnumbering Beauregard's army of less than 30,000. Beauregard was unaware of the arrival of Buell's army and launched a counterattack in response to a two-mile advance by William Nelson's division of Buell's army at 6:00 am, which was, at first, successful. Union troops stiffened and began forcing the Confederates back. Beauregard ordered a counterattack, which stopped the Union advance but did not break its battle line. At this point, Beauregard realized that he could not win and, having suffered too many casualties, he retired from the field and headed back to Corinth. On the 8th, Grant sent Brig. Gen. William T. Sherman, with two brigades, and Brig. Gen. Thomas J. Wood, with his division, in pursuit of Beauregard. They ran into the Rebel rearguard, commanded by Col. Nathan Bedford Forrest, at Fallen Timbers. Forrest's aggressive tactics, although eventually contained, influenced the Union troops to return to Pittsburg Landing. Grant's mastery of the Confederate forces continued; he had beaten them once again. The Confederates continued to fall back until launching their mid-August offensive.",
    "preservation": "III.1",
    "significance": "A"
  }
]
```

### nps-tn003

Path: `data/raw/nps-tn003.txt`.
SHA-256: `5a368744a4f1e6b231be2aac0903ea86b07e302634fd522dac53b433424a2941`.

````text
Return to Results
Shiloh
Other Name:
Pittsburg Landing
Campaign:
Union Penetration Up the Cumberland & Tennessee Ri
Date(s):
February-June 1862
Principal Commanders:
Lieutenant General Ulysses Grant [US]
Major General Albert Johnston [CS]
Forces Engaged:
110053 total (US 65085; CS 44968;)
Estimated Casualties:
23746 total (US 13047; CS 10699;)
Description:
As a result of the fall of Forts Henry and Donelson, Confederate Gen. Albert Sidney Johnston, the commander in the area, was forced to fall back, giving up Kentucky and much of West and Middle Tennessee. He chose Corinth, Mississippi, a major transportation center, as the staging area for an offensive against Maj. Gen. Ulysses S. Grant and his Army of the Tennessee before the Army of the Ohio, under Maj. Gen. Don Carlos Buell, could join it. The Confederate retrenchment was a surprise, although a pleasant one, to the Union forces, and it took Grant, with about 40,000 men, some time to mount a southern offensive, along the Tennessee River, toward Pittsburg Landing. Grant received orders to await Buell's Army of the Ohio at Pittsburg Landing. Grant did not choose to fortify his position; rather, he set about drilling his men many of which were raw recruits. Johnston originally planned to attack Grant on April 4, but delays postponed it until the 6th. Attacking the Union troops on the morning of the 6th, the Confederates surprised them, routing many. Some Federals made determined stands and by afternoon, they had established a battle line at the sunken road, known as the "Hornets Nest." Repeated Rebel attacks failed to carry the Hornets Nest, but massed artillery helped to turn the tide as Confederates surrounded the Union troops and captured, killed, or wounded most.  Johnston had been mortally wounded earlier and his second in command, Gen. P.G.T. Beauregard, took over. The Union troops established another line covering Pittsburg Landing, anchored with artillery and augmented by Buell's men who began to arrive and take up positions. Fighting continued until after dark, but the Federals  held. By the next morning, the combined Federal forces numbered about 40,000, outnumbering Beauregard's army of less than 30,000. Beauregard was unaware of the arrival of Buell's army and launched a counterattack in response to a two-mile advance by William Nelson's division of Buell's army at 6:00 am, which was, at first, successful. Union troops stiffened and began forcing the Confederates back. Beauregard ordered a counterattack, which stopped the Union advance but did not break its battle line. At this point, Beauregard realized that he could not win and, having suffered too many casualties, he retired from the field and headed back to Corinth. On the 8th, Grant sent Brig. Gen. William T. Sherman, with two brigades, and Brig. Gen. Thomas J. Wood, with his division, in pursuit of Beauregard. They ran into the Rebel rearguard, commanded by Col. Nathan Bedford Forrest, at Fallen Timbers. Forrest's aggressive tactics, although eventually contained, influenced the Union troops to return to Pittsburg Landing. Grant's mastery of the Confederate forces continued; he had beaten them once again. The Confederates continued to fall back until launching their mid-August offensive.
Results:
Union Victory
CWSAC Reference #:
TN003
Preservation Priority:
````

### or-grant-shiloh-report

Path: `data/raw/shiloh/or-grant-shiloh-report.txt`.
SHA-256: `ab226b87fdbafcbe96e01564f596840b2b76fcf0f3cfe3aa83e1b1ee72f6d3cc`.

````text
Ulysses S. Grant: Shiloh report excerpts

## p108-heading
HEADQUARTERS DISTRICT OF WEST TENNESSEE, Pittsburg, April 9, 1862.

## p109
OI.AP. XXII.] PITTSBURG LANDING, OR SHILOH, TENN. 109 best government ever devised, the other for its destruction. It is pleasant to record the success of the army contending for the former principle. On Sunday morning our pickets were attacked and driven in by the enemy. Immediately the five divisions stationed at this place were drawn up in line of battle, ready to meet them. The battle soon waxed warm on the left and center, varying at times to all parts of the line. The most continuous firing of musketry and artillery ever heard on this continent was kept up until night-fall, the enemy having forced the entire line to fall back nearly half way fro/n their camps to the Landing. At a late hour in the afternoon a desperate effort was made by the enemy to turn our left and get possession of the Lauding, transports, &c. This point was guarded by the gunboats Tyler and Lexington, Captains Gwin and Shirk, U: S. Navy, commanding, four 20-pounder Parrott guns and a battery of rifled guns. As there is a deep and impassable ravine for artillery or cavalry, and very difficult for infantry, at this point, no troops were stationed here, except the neces sary artillerists and a small infantry force for their support. Just at this moment the advance of Major-General BuelPs column (a part of the division under General Nelson) arrived, the two generals named both being present. An advance was immediately made upon the point of attack and the enemy soon driven back. In this repulse much is due to the presence of the gunboats Tyler and Lexington, and their able commanders, Captains Gwin and Shirk. During the night the divisions under Generals Crittenden and Mc- Cook arrived. General Lewis Wallace, at Crump's Landing, G miles below, was ordered at an early hour in the morning to hold his division an readiness to be moved in any direction to which it might be ordered. At about 11 o'clock the order was delivered to move it up to Pittsburg, but owing to its being led by a circuitous route did not arrive in time to take part in Sunday's action. During the night all was quiet, and feeling that a great moral ad vantage would be gained by becoming the attacking party, an advance was ordered as soon as day dawned. The result was a gradual repulse of the enemy at all parts of the line from morning until probably 5 o'clock in the afternoon, when it became evident the enemy was re treating. Before the close of the action the advance of General T. J. Wood's division arrived in time to take part in the action. My force was too much fatigued from two days' hard fighting and exposure in the open air to a drenching rain during the intervening night to pursue immediately. Night closed in cloudy and with heavy rain, making the roads impracticable for artillery by the next morning. General Sherman, however, followed the enemy, finding that the main part of the army had retreated in good order. Hospitals of the enemy's wounded were found all along the road as far as pursuit was made. Dead bodies of the enemy and many graves were also found. I inclose herewith report of General Sherman, which will explain more fully the result of this pursuit. Of the part taken by each separate command I cannot take special notice in this report, but will do so more fully when reports of division commanders are handed in. General Buell, coming on the field with a distinct army long under Jiis command, and which did such efficient service, commanded by him-

## p110
110 KY., TEXN., N. MISS., N. ALA., AND SW. VA. [CHAP. XXII. self in person on the field, will be much better able to notice those of his command who particularly distinguished themselves than I possi bly can. 1 feel it a duty, however, to a gallant and able officer, Brig. Gen. W. T. Sherman, to make a special mention. He not only was with his command during the entire two days' action, but displayed great judg ment and skill in the, management of his men. Although severely wounded in the hand the first day his place was never vacant. He was again wounded, and had three horses killed under him. In making this mention of a gallant officer no disparagement is in tended to the other division commanders, Maj. Gens. John A. McCler- nand and Lewis Wallace, and Brig. Gens. 8. A. Hurlbut, B. M. Prentiss, and W. H. L. Wallace, all of whom maintained their places with credit to themselves and the cause. General Prentiss was taken prisoner in the first day's action, and General W. H. L. Wallace severely, probably mortally, wounded. His assistant adjutant-general, Capt. William McMichael, is missing; prob ably taken prisoner. My personal staff are all deserving of particular mention, they having been engaged during the entire two days in conveying orders to every part of the field. It consists of Col. J. D. Webster, chief of staff; Lieut. Col. J. B. McPherson, chief engineer, assisted by Lieuts. W. Jj. B. Jenney and William Kossak ; Capt. J. A. Hawlins, assistant adju tant-general; Capts. W. S. Hilly er, W. K. liowley, and C. B. Lagow, aides-de-camp ; Col G. G. Pride, volunteer aide, and Capt. J. P. Haw kins, chief commissary, who accompanied me upon the field. The medical department, under the direction of Surgeon Hewitt, medical director, showed great energy in providing for the wounded and in getting them from the field regardless of danger. Colonel Webster was placed in special charge of all the artillery and was constantly upon the field. He displayed, as always hereto fore, both skill and bravery. At least in one instance he was the means of placing an entire regiment in a position of doing most valuable serv ice, and where it would not have been but for his exertions. Lieutenant-Colonel McPherson, attached to my staff as chief engi neer, deserves more than a passing notice for his activity and courage. All the grounds beyond our camps for miles have been reconnoitered by him, and plats carefully prepared under his supervision give accu rate information of the nature of approaches to our lines. During the two days' battle he was constantly in the saddle, leading troops as they arrived to points where their services were required. During the en gagement he had one horse shot under him. The country will have to mourn the loss of many brave men who fell at the battle of Pittsburg, or Shiloh, more properly. The exact loss in killed and wounded will be known in a day or two. At present 1 <;an only give it approximately at 1, .">()() killed and 0,500 wounded.* The loss of artillery was great, many pieces being disabled by the enemy's shots and some losing all their horses and many men. There were probably not less than UOO horses killed. The loss of the enemy in killed and left upon the field was greater than ours, in wounded the estimate cannot be made, as many of them must have been sent back to Corinth and other points. The enemy suffered terribly from demoralization and desertion. * But sec revised statement, p. 100.
````

### or-buell-shiloh-report

Path: `data/raw/shiloh/or-buell-shiloh-report.txt`.
SHA-256: `9581e8a1e7dc63d22c9999643183730d3ac22c216b731507bf993d2cafdbd425`.

````text
Don Carlos Buell: Shiloh report excerpts

## p291
CHAP. XXII.] PITTSBURG LANDING, OK SHILOH, TENN. 291 in the direction of General Prentiss' camp. After inarching about 2 miles an officer of General Prentiss' staff ordered us to halt and pre pare for action, which was promptly done. As soon as the regiment was placed in position the enemy opened fire on us from a battery at about 400 yards' distance, which continued without intermission for two hours. We were then ordered to change our position and to en gage a large force of the enemy who were pressing upon the center, which was done. After a severe engagement at the distance of 25 or 30 yards we drove the enemy back, not, however, without serious loss. We held the position assigned us until 4 p. m., fighting almost with out intermission, at which time we were ordered to change our front to i*eet the enemy, who had outflanked us. Here we fought until 5 o'clock, driving the enemy back, although they charged us frequently during the time. Again we were compelled to change our position, and soon after this change we were surrounded and fired upon from front and rear by two batteries and infantry. Here there was a most terrible shower of shot and shell. We repulsed the enemy in our rear and determined to try and reach the main body of the army, which had fallen back to the river, and in the effort to lead our now broken forces back the gallant and much-lamented Colonel Tindall fell, shot through the body, after having done his duty most nobly during the day. After retiring about 200 yards we were met .by a large force of the enemy and compelled to surrender at about 6 p. m., after ten hours' almost incessant fighting. Officers and men behaved nobly. I feel it my duty to mention the gallant conduct of Maj. John McCullough, who displayed great cool ness and bravery throughout the day. Captains Dunlap, Bobinson, and Brown, Adjutant Martin, and Lieu tenants Munn and Simms were wounded ; 30 privates were killed, about 170 wounded, and 375 were taken prisoners.* This report would have been made earlier, but being a prisoner until very recently, I have not been in a situation to make it. Most respectfully, your obedient servant, QUIN MOETON, Lieutenant- Colonel Tic enty -third Regiment Mo. Vols. His Excellency H. K. GAMBLE, Governor of Missouri. No. 87. Report of Maj. Gen. Don Carlos Buell, U. S. Army, commanding Army of the Ohio, with congratulatory orders. HEADQUARTERS ARMY OF THE OHIO, Field of Shiloh, April 15, 1862. SIR : The rear division of the army under my command, which had been delayed a considerable time in rebuilding the Duck Biver Bridge, left Columbia on the 3d instant. I left the evening of that day, and arrived at Savannah on the evening of the 5th. General Nelson, with his division, which formed the advance, arrived the same day. The other divisions marched with intervals of about 6 miles. * Nominal list of casualties shows 27 officers and 463 men killed wounded, and missing. See also revised statement, p. 105.

## p292
292 KY., TENN., N. MISS., N. ALA., AND SW. VA. [CHAP. XXII. On the morning of the Oth the firing of cannon and musketry was heard in the direction of this place. Apprehending that a serious en gagement had commenced, 1 went to General Grant's headquarters to get information as to the best means of reaching the battle-field with the division that had arrived. At the same time orders were dis patched to the divisions in rear to leave their trains and push forward by forced marches. I learned that General Grant had just started, leaving orders for General' Nelson to inarch to the river opposite Pitts- burg Landing to be ferried across. On examination of the road up the river I discovered it to be impracticable for artillery, and General Nel son was directed to leave his to be carried forward by steamers. The impression existed at Savannah that the tiring was only an affair of outposts, the same thing having occurred for the two or three pre vious days; but as it continued I determined to go at once to the scene of action, and accordingly started with my chief of staff, Colonel Fry, on a steamer, which I had ordered to get under steam. As we pro ceeded up the river groups of soldiers were seen upon the west bank, and it soon became evident that they were stragglers from the army that was engaged. The groups increased in size and frequency, until, as we approached the Landing, they amounted to whole companies, and almost regiments, and at the Landing the banks swarmed Avitli a con fused mass of men of various regiments. The number could cot have been less than 4,000 or 5,000, and later in the day it became much greater. Finding General Grant at the Landing I requested him to send steamers to Savannah to bxing up General Critteuden's division, which had ar rived during the morning, and then went ashore with him. The throng of disorganized and demoralized troops increased con tinually by fresh fugitives from the battle, which steadily grew nearer the Landing, and with these were mingled great numbers of teams, all striving to get as near as possible to the river. With few exceptions all efforts to form the troops and move them forward to the fight utterly failed. In the mean time the enemy had made such progress against our troops that his artillery and musketry began to play into the vital spot of the position, and some persons were killed on the bank at the very Landing. General Nelson arrived with Colonel Ammeirs brigade at this opportune moment. It was immediately posted to meet the attack at that point, and, with a battery of artillery which happened to be on the ground and was brought into action, opened fire on the enemy and ; repulsed him. The action of the gunboats also contributed very 'much to that result. The attack at that point was not renewed, night having come on, and the firing ceased on both sides. In the mean time the remainder of General Nelson's division crossed, and General Critteriden's arrived from Savannah by steamers. After examining the ground as well as was possible at night in front of the line on which General Grant's troops had formed and as far to the right as General Sherman's division, I directed Nelson's and Crittenden's "divis ions to form in front of that line, and move forward as soon as it was rly the following inorn- MendenhalPs regular fth Artillery, arrived, during the night of the 6th, and reached the field of battle early in the morning of the 7th. I knew that the other divisions could not arrive in time for the action that day.

## p293
CHAP. XXII.] P1TTSBURG LANDING, OR SHILOH, TENN. 293 The patch of country on which the battles of the 6th and 7th were fought is called Shiloh, from the little church of that name which stands near the center of it. It consists of an undulating table-land, elevated some 80 or 100 feet above the river bottom. Along the Ten nessee Kiver to the east it breaks into abrupt ravines, and towards the south, along Lick Creek, which empties into the Tennessee River some 3 miles above Pittsburg Landing, rises into a range of hills of some height, whose slopes are gradual towards the battle field and somewhat abrupt towards Lick Creek. Owl Creek, rising quite near the source of Lick Creek, flows to the northeast around the battle-field into Snake Creek, which empties into the Tennessee Kiver 4 miles below Lick Creek. The drainage is mainly from the Lick Creek Eidge and the table-land into Owl Creek. Coming from Corinth, the principal road crosses Lick Creek at two points some 12 miles from its mouth, and separates into three or four principal branches, which enter the table-land from the south at a dis tance of about a mile apart. Generally the face of the country is covered with woods, through which troops can pass without great diffi culty, though occasionally the undergrowth is dense. Small farms or cultivated fields of from 20 to 80 acres occur now and then, but as a gen eral thing the country is in forest. My entire ignorance of the various roads and of the character of the country at the time rendered it im possible to anticipate the probable dispositions of the enemy, and the woods were always sufficient to screen his preparatory movements from observation. Soon after 5 o'clock on the morning of the 7th General Nelson's and General Crittenden's divisions, the only ones yet arrived on the ground, moved promptly forward to meet the enemy. Nelson's division, march- in/; in line of battle, soon came upon his pickets, drove them in, and it about 6 o'clock received the fire of his artillery. The division was iere halted and Mendenhall's battery brought into action to reply, ^virile Crittenden's division was being put into position on the right of Nelson's. Bartlett's battery was posted in the center of Crittenden's livision in a commanding position, opposite which the enemy was dis covered to be formed in force. By this time McCook's division arrived >n the ground, and was immediately formed on the right of Crittenden's. Skirmishers were thrown to the front and a strong body of them to guard •tir left flank, which, though somewhat protected by rough ground, it ras supposed the enemy might attempt to turn, and, in fact, did, but »Tas handsomely repulsed, with great loss. Each brigade furnished ts own reserve, and in addition Boyle's brigade, from Crittenden's ivision, though it formed at first in the line, was kept somewhat back •lien the line advanced, to be used as occasion might require. I found n the ground parts of about two regiments — perhaps 1,000 men — nd subsequently a similar fragment came up of General Grant's force, 'he first 1 directed to act with General McCook's attack and the second as similarly employed on the left. I saw other straggling troops of -eneral Grant's force immediately on General McCook's right, and some ring had already commenced there. 1 have no direct knowledge of le disposition of the remainder of General Grant's forces nor is it my rovince to speak of them. Those that came under my direction in the ay 1 have stated rendered willing and efficient service during the day. The force under my command occupied a line of about 1£ miles. In out of Nelson's division was an open field, partially screened toward *s right by a skirt of woods, which extended beyond the enemy's line, ith a thick undergrowth in front of the left brigade of Crittenden's

## p295
CHAI-. XXH.] PITTSBURG LANDING, OR SHILOH, TENN. 295 forward, silenced the battery, and it was captured by General Critten- den's division, the enemy retreating from it. In the mean time the division of General McCook on the right, which became engaged somewhat later in the morning than the divisions on the left, had made steady progress until it drove the enemy's left from the hotly-contested field. The action was commenced in this division by General Rousseau's brigade, which drove the enemy in front of it from his first position and captured a battery. The line of attack of this division caused a considerable widening of the space between it and Crittenden's right. It was also outflanked on its right by the line of the enemy, who made repeated strong attacks on its flanks, but was always gallantly repulsed. The enemy made his last decided stand in front of this division in the woods beyond Sherman's camp. Two brigades of General Wood's division arrived just at the close of the battle, but only one of them (Colonel Wagner's) 'in time to partici pate actively in the pursuit, which it continued for about a mile and until halted by my order. Its skirmishers became engaged for a few minutes with skirmishers (cavalry and infantry) of the enemy's rear guard, which made a momentary stand. It was also fired upon by the enemy's artillery on its right flank, but without effect. It was well- conducted by its commander, and showed great steadiness. The pursuit was continued iio farther that day. I was without cav alry, and the different corps had become a good deal scattered in a pursuit over a country which screened the movements of the enemy, and the roads of which I knew practically nothing. In the beginning of the pursuit, thinking it probable the enemy had retired partly by the Hamburg road, I had ordered Nelson's division to follow as far as Lick Creek, on that road, from which, I afterwards le irned, the direct Corinth road was separated by a difficult ravine which empties into Lick Creek. I therefore occupied myself with ex amining the ground and getting the different divisions into position, which was not effected until some time after dark. The following morning, in pursuance of the directions of General Grant, General Wood was sent forward with two of his brigades and a battery of artillery to discover the position of the enemy, and press him if he should be found in retreat. General Sherman, with about the same force from General Grant's army, was on the same service, and had a spirited skirmish with the enemy's cavalry, driving it back. The main force was found to have retreated beyond Lick Creek, and our troops returned at night. The loss of the forces under my command is 263 killed, 1,816 wounded, 88 missing; total, 2,167.* The trophies are twenty pieces of artillery, a greater number of caissons, and a considerable number of small-arms. Many of the cannon were recaptured from the loss of the previous day. Several stand of colors were also recaptured. There were no idlers in the battle of the 7th. Every portion of the army did its work. The batteries of Captains Terrill and Mendenhall were splendidly handled and served ; that of Captain Bartlett was served with great spirit and gallantry, though with less decisive re sults. I specially commend to the favor of the Government, for their dis tinguished gallantry and good conduct Brig. Gen. A. McD. McCook, commanding Second Division ; Brig. Gen. William Kelson, command ing Fourth Division ; Brig. Gen. Thomas L. Crittenden, commanding * But see revised statement, p. 108.

## p296
296 KY., TENN., N. MISS., N. ALA., AND SW. VA. [CHAP XXII. Fifth Division ; Brig. Gen. Lovell H. Rousseau, commanding Fourth Brigade; Brig. Gen. J. T. Boyle, commanding Eleventh Brigade; Col. Capt. W. R. Terrill, Fifth Artillery ; Capt. John Meiideuhall, Fourth Artillery; Capt. Joseph Bartlett, Ohio Volunteer Battery. For the manv other officers wTho won honorable distinction I refer to the re ports of the division, brigade, and regimental commanders, transmitted herewith, as also for more detailed information of the services of the different corps. I join cordially in the commendations bestowed by those officers on those under their command. The gallantry of many of them came under my personal observation. The members of my staff', Col. James B. Fry, chief of staff; Capt. J. M. Wright, assistant adjutant-general ; Lieut. C. L. Fitzhugh, Fourth Artillery, aide-de-camp ; Lieut. A. F. Rockwell, New York Chasseurs, aide-de-camp; Lieut. T. J. Bush, Twenty-fourth Kentucky, aide-de camp; Capt. J. H. Gilman, Nineteenth Infantry, inspector of artillery; Capt. E. Gay, Sixteenth Infantry, inspector of cavalry; Capt. H. C. Bankhead, Fifth Infantry, inspector of infantry, and Capt. Nathaniel Michler, Topographical Engineers, were distinguished for gallant bear ing throughout the battle, and rendered valuable service. The gallant deportment of my orderlies, Privates A. J. Williamson, Fourth Cavalry, and N. M. Smith, J. R. Hewitt, J. A. Stevenson, and V. B. Hummel, 'of the Anderson Troop, also deserves to be mentioned. I am particularly indebted to Colonel Fry, chief of staff, for valuable assistance in the battle, as well as for the ability and industry with which he has at all times performed the important duties of his position. Surgeon Murray, medical director, always assiduous in the discharge of his duties, was actively engaged on the field in taking the best care of the wounded the circumstances admitted of. Capt. A. C. Gillem, assistant quarter master, is entitled to great credit for his energy and industry in pro viding transportation for the troops from Savannah. Lieut. Col. James Oakes, Fourth Cavalry, inspector of cavalry, and Capt. C. C. Gilbert, First Infantry, acting inspector-general, who have rendered zealous and valuable service in their positions, were detained at Savannah, and unable to be present in the action. The troops which did not arrive in time for the battle, General Thomas' and part of General Wood's divisions (a portion of the latter, as I have previously stated, took part in the pursuit, and the remainder arrived in the evening), are entitled to the highest praise for the untir ing energy with which they pressed forward night and day to share the dangers of their comrades. One of those divisions (General Thomas') had already under his command made its name honorable by one of the most memorable victories of the war — Mill Springs — on which the tide of success seemed to turn steadily in favor of the Union. Very respectfully, your obedient servant, D. C. BUELL, Mojo r- Genera I, Comm anding. Capt, N. H. MCLEAN, Assistant Adjutant- General, Department of the Mississippi.
````

### or-beauregard-shiloh-report

Path: `data/raw/shiloh/or-beauregard-shiloh-report.txt`.
SHA-256: `c87c79162f5ef1a88bc308896b90a4178808a6b505e1b7ee805be535705a692c`.

````text
P. G. T. Beauregard: Shiloh report excerpts

## p385
CHAP. XXII.] PITTSBURG LANDING, OR SHILOH, TENN. 385 HEADQUARTERS ARMY OF THE MISSISSIPPI, Corinth, Miss., April 11, 1862. GENERAL : On the 2d ultimo, having ascertained conclusively, from the movements of the enemy on the Tennessee River and from reliable sources of information, that his aim would be to cut off my communi cations in West Tennessee with the Eastern and Southern States, by operating from the Tennessee River, between Crump's Landing and East-port, as a base, I determined to foil his designs by concentrating all my available forces at and around Corinth. Meanwhile, having called on the Governors of the States of Tennes see, Mississippi, Alabama, and Louisiana to furnish additional troops, some of them (chiefly regiments from Louisiana) soon reached this vicinity, and with two divisions of General Folk's command from Colum bus, and a fine corps of troops from Mobile and Pensacola, under Major- Geueral Bragg, constituted the Army of the Mississippi. At the same time General Johnston, being at Murfreesborough, on the march to form a junction of his forces with mine, was called onto send at least a brigade by railroad, so that we might fall on and crush the enemy, should he attempt an advance from under his gunboats. The call on General Johnston was promptly complied with. His entire force was also hastened in this direction, and by April 1 our united forces were concentrated along the Mobile and Ohio Railroad from Bethel to Corinth and on the Memphis and Charleston Railroad from Corinth to luka. It was then determined to assume the offensive, and strike a sudden blow at the enemy, in position under General Grant on the west bank of the Tennessee, at Pittsburg, and in the direction of Savannah, before he was re-enforced by the army under General Buell, then known to be advancing for that purpose by rapid marches from Nashville via Co in nbia. About the same time General Johnston was advised that such an operation conformed to the expectations of the President. By a rapid and vigorous attack on General Grant it was expected he would be beaten back into his transports and the river, or captured, in time to enable us to profit by the victory, and remove to the rear all the stores and munitions that would fall into our hands in such an event before the arrival of General BuelPs army on the scene. It was never contemplated, however, to retain the position thus gained and abandon Corinth, the strategic point of the campaign. Want of general officers needful for the proper organization of divis ions and brigades of an army brought thus suddenly together and 3ther difficulties in the way of an effective organization delayed the movement until the night of the 2d instant, when it was heard, from a reliable quarter, that the junction of the enemy's armies was near at land. It was then, at a late hour, determined that the attack should 3e attempted at once, incomplete and imperfect as were our prepara- :ions for such a grave and momentous adventure. Accordingly, that light at 1 a. m. the preliminary orders to the commanders of corps #ere issued for the movement. On the following morning the detailed orders of movement, a copy >f which is herewith, marked A, were issued, and the movement, after iome delay, commenced, the troops being in admirable spirits. It was expected we should be able to reach the enemy's lines in time to attack iim early on the 5th instant. The men, however, for the most part, vere unused to marching, and the roads, narrow and traversing a lensely-wooded country, became almost impassable after a severe iain- 25 R R— VOL x

## p386
386 KY., TENN., X. MISS., X. ALA., AXD SW. VA. [CHAP. xxn. storm on the night of the 4th, which drenched the troops in bivouac; hence our forces did not reach the intersection of the roads from Pitts- burg and Hamburg, in the immediate vicinity of the enemy, until late Saturday afternoon. It was then decided that the attack should be made on the next morning, at the earliest hour practicable, in accordance with the orders of movement ; that is, in three lines of battle, the first and second ex tending from Owl Creek, on the left, to Lick Creek, on the right, a distance of about 3 miles, supported by the third and the reserve. The first line, under Major-General Hardee, was constituted of his corps, augmented on his right by Gladden's brigade, of Major-General Bragg's corps, deployed in line of battle, with their respective artillery follow ing immediately by the main road to Pittsburg and the cavalry in rear of the wings. The second line, composed of the other troops of Bragg's corps, followed the first at a distance of 500 yards in the same order as the first. The army corps under General Polk followed the second line, at a distance of about 800 yards, in lines of brigades deployed, with their batteries in rear of each brigade, moving by the Pittsburg road, the left wing supported by cavalry. The reserve, under Briga dier-General Breckinridge, followed closely the third line in the same order, its right wing supported by cavalry. These two corps constituted the reserve, and were to support the front lines of battle, by being deployed, when required, on the right and left of the Pittsburg road, or otherwise act according to the exigencies of the battle. At 5 a. m. on the 6th instant, a reconnoiteriug party of the enemy having become engaged with our advance pickets, the commander of the forces gave orders to begin the movement and attack as determined upon, except that Trabue's brigade, of Breckinridge's division, was de tached and advanced to support the left of Bragg's corps and line of battle when menaced by the enemy, and the other two brigades were directed to advance by the road to Hamburg to support Bragg's right; and at the same time Maney's regiment, of Polk's corps, was advanced by the same road to re-enforce the regiment of cavalry atrd battery of four pieces already thrown forward to watch and guard Greer's, Tan ner's, and Borland's Fords, on Lick Creek. At 5.30 a. m. our lines and columns were in motion, all animated, evidently, by a promising spirit. The front line was engaged at once, but advanced steadily, followed in due order, with equal resolution and steadiness, by the other lines, which were brought successively into ac tion with rare skill, judgment, and gallantry by the several corps com manders as the enemy made a stand, with his masses rallied for the struggle for his encampments. Like an Alpine avalanche our troops moved forward, despite the de termined resistance of the enemy, until after G p. m., when we were in possession of all his encampments between Owl and Lick Creeks but one; nearly all of his field artillery; about 30 flags, colors, and staud- ards ; over 3,000 prisoners, including a division commander (General Prentiss), and several brigade commanders; thousands of small-arms; an immense supply of subsistence, forage, and munitions of war, and a large amount of means of transportation — all the substantial fruits of a complete victory, such, indeed, as rarely have followed the most suc cessful battles ; for never was an army so well provided as that of our enemy. The remnant of his army hud been driven in utter disorder to the immediate vicinity of Pittsburg, under the shelter of the heavy guns of

## p387
CHAP. XXH.l PITTSBURG LANDING, OR SHILOH, TENN. 387 his iron-clad gunboats, and we remained undisputed masters of his well- selected, admirably-provided cantonments, after over twelve hours of obstinate conflict with his forces, who had be^ii beaten from them and the contiguous covert, but only by a sustained onset of all the men we could bring- into action. Our loss was heavy, as will appear from the accompanying return marked B. Our commander-in-chief, General A. S. Johnston, fell mor tally wounded, and died on the field at 2.30 p. m., after having shown the highest qualities of the commander and a personal intrepidity that inspired all around him and gave resistless impulsion to his columns at critical moments. The chief command then devolved upon me, though at the time I was greatly prostrated and suffering from the prolonged sickness with which I had been afflicted since early in February. The respon si bility was one which in my physical condition I would have gladly avoided, though casfr upon me when our forces were successfully pushing the enemy back upon the Tennessee River, and though supported on the immediate field by such corps commanders as Major-Generals Polk, Bragg, and Hardee, and Brigadier- General Breckinridge, commanding the reserve. It was after 6 p. m., as before said, when the enemy's last position was carried, and his forces finally broke and sought refuge behind a commanding eminence covering the Pittsburg Landing, not more than half a mile distant, and under the guns of the gunboats, which opened on our eager columns a fierce and annoying fire with shot and shell of the heaviest description. Darkness was close at hand ; officers and men were, exhausted by a combat of over twelve hours without food, and jaded by the march of the preceding day through mud and water. It was. therefore, impossible to collect the rich and opportune spoils of war scattered broadcast on the field left in our possession, and impracticable to make any effective dis positions for their removal to the rear. I accordingly established my headquarters at the church of Shiloh, in the enemy's encampments, with Major-General Bragg, and directed our troops to sleep on their arms in such positions in advance and rear as corps commanders should determine, hoping, from news received by a special dispatch, that delays had been encountered by General Buell in his march from Columbia, and that his main force, therefore, could not reach the field of battle in time to save General Grant's shat tered fugitive forces from capture or destruction on the following day. During tbe night the rain fell in torrents, adding to the discomforts and harassed condition of the men. The enemy, moreover, had broken their rest by a discharge at measured intervals of heavy shells thrown from the gunboats; therefore on the folio wing morning the troops under my command were not in condition to cope with an equal force of fresh troops, armed and equipped like our adversary, in the immediate posses sion of his depots and sheltered by such an auxiliary as the enemy's gunboats. About 6 o'clock on the morning of April 7, however, a hot fire of musketry and artillery, opened from the enemy's quarter on our ad vanced line, assured me of the junction of his forces, and soon the battle raged with a fury which satisfied me I was attacked by a largely superior force. But from the outset our troops, notwithstanding their fatigue and losses from the battle of the day before, exhibited the most cheer ing, veteran-like steadiness. On the right and center the enemy was repulsed in every attempt he made with his heavy columns in that

## p388
388 KY., TENN., N. MISS., N. ALA., AND SW. VA. [CHAP. XXII. quarter of the field. On the left, however, and nearest to the point of arrival of his re-enforcements, he drove forward line after line of his fresh troops, which were met with a resolution and courage of which our country may be proudly hopeful. Again and again our troops were brought to the charge, invariably to win the position in issue; invariably to drive back their foe. But hour by hour, thus opposed to an enemy constantly re-enforced, our ranks were perceptibly thinned under the unceasing, withering fire of the enemy, and by 12 m. eighteen hours of hard fighting had sensibly exhausted a large number. My last reserves had necessarily been disposed of, and the enemy was evidently receiving fresh re-enforcements after each repulse; ac cordingly about 1 p. m. I determined to withdraw from so unequal a conflict, securing such of the results of the victory of the day before as was then practicable. Officers of my staff were immediately dispatched with the necessary orders to make the best dispositions for a deliberate, orderly withdrawal from the field, and to collect and post a reserve to meet the enemy, should he attempt to push after us. In this connection I will mention particularly my adjutant general, Colonel Jordan, who was of much assistance to me on this occasion, as he had already been on the field of battle on that and the preceding day. About 2 p. in. the lines in advance, which had repulsed the enemy in their last fierce assault on our left and center, received the orders to retire. This was done with uncommon steadiness and the enemy made no attempt to follow. The line of troops established to cover this movement had been dis posed on a favorable ridge commanding the ground of Shiloh Church. From this position our artillery played upon the woods beyond for a while, but upon no visible enemy and without reply. Soon satisfied that no serious pursuit would be attempted this last line was with drawn, and never did troops leave a battle-field in better order ; even the stragglers fell into the ranks and marched off with those who had stood more steadily by their colors. A second strong position was taken up about a mile in rear, where the approach of the enemy was awaited for nearly an hour, but no effort to follow was made, and only a small detachment of horsemen could be seen at a distance from this last position, warily observing our move ments. Arranging through my staff1 officers for the completion of the move ments thus begun, Brigadier-General Breckinridge was left with his command as a rear guard to hold the ground we had occupied the night preceding the first battle, just in front of the intersection of the Pittsburg and Hamburg roads, about 4 miles from the former place, while the rest of the army passed to the rear in excellent order. On the following day General Breckinridge fell back about 3 miles, to Mickey's, which position we continued to hold, with our cavalry thrown considerably forward in immediate proximity to the battle field. Unfortunately, toward night of the 7th instant it began to rain heavily. This continued throughout the night ; the roads became al most impassable in many places, and much hardship and suffering now ensued before all the regiments reached their encampments; but, despite the heavy casualties of the two eventful days of April G and 7, this army is more confident of ultimate success than before its encounter with the enemy.
````

### or-union-return-april4-5

Path: `data/raw/shiloh/or-union-return-april4-5.txt`.
SHA-256: `e7b9aee495475a62721a811490c442f8019bc689a02dd841db0a5fbd60f8727e`.

````text
Army of the Tennessee: abstracts of field returns, April 4–5, 1862

## p112
Abstracts from the field returns of the several divisions of the Army of the Tennessee, Maj. Gen. U. S. Grant commanding.
APRIL 4–5, 1862.
Columns: Command | Present for duty: Officers, Men, Aggregate | Pieces of artillery | Notes by the compiler.
Total First Division | 321 | 6,707 | 7,028 | [not reported]
Total Second Division | 419 | 8,289 | 8,708 | 24
Total Third Division | 314 | 7,250 | 7,564 | 12
Total Fourth Division | 306 | 6,996 | 7,302 | 10
Total Fifth Division | 382 | 8,448 | 8,830 | 16
Total Sixth Division | 245 | 5,218 | 5,463 | [blank]
Grand total | 1,987 | 42,908 | 44,895 | 62
First Division note: From “statement of effective force,” April 5. Pieces of artillery not reported on original.
Second Division note: Return dated April 5.
Third Division note: Return dated April 4; the division not in the battle of April 6.
Fourth and Fifth Division notes: Return dated April 5.
Sixth Division note: Return dated April 5; strength of two regiments and one battery not reported on the original.
Grand-total note: Division staff not included in this abstract.
````

### or-confederate-return

Path: `data/raw/shiloh/or-confederate-return.txt`.
SHA-256: `6c127e6c1945754097a4b54a6efd98a9f7a35e3b009c7b9c5cd49056b0400c0c`.

````text
Army of the Mississippi: field return before and after Shiloh

## p396
[Inclosure E.] Field return of the Army of the Mississippi before and after the battle of Shiloh.
Columns: Command | Commander | Effective total before battle | Effective total after battle.
First Army Corps | Maj. Gen. L. Polk | 9,136 | 6,779
Second Army Corps | General Braxton Bragg | 13,589 | 9,961
Third Army Corps | Maj. Gen. W. J. Hardee | 6,789 | 4,609
Reserve | Brig. Gen. J. C. Breckinridge | 6,439 | 4,206
Total infantry and artillery | 35,953 | 25,555
Cavalry | Brig. Gen. F. Gardner | 4,382 | 4,081
Grand total | 40,335 | 29,636
Difference | 10,699
Footnote to both effective-total columns: These columns do not agree with the effective totals in reports Nos. 136 and 137, following.
Respectfully submitted. THOMAS JORDAN, Assistant Adjutant-General.
Respectfully submitted and forwarded. G. T. BEAUREGARD, General, Commanding Army of the Mississippi.
HEADQUARTERS ARMY OF THE MISSISSIPPI, Corinth, Miss., April 21, 1862.
````

### or-halleck-orders

Path: `data/raw/shiloh/or-halleck-orders.txt`.
SHA-256: `b450b33b8475127a066ec9ab5257624ca818af9d8cd3049db0c5eab9c2501f21`.

````text
Halleck to Grant: March 20 and April 5 orders

## p50-51-march20
SAINT LOUIS, March 20, 1862. Major-General GRANT, Savannah, Tenn.:
Your telegrams of yesterday just received. I do not fully understand you. By all means keep your forces together until you connect with General Buell, who is now at Columbia, and will move on Waynesborough with three divisions. Don't let the enemy draw you into an engagement now. Wait till you are properly fortified and receive orders.
H. W. HALLECK, Major-General.

## p94-april5
SAINT LOUIS, April 5, 1862. Maj. Gen. U. S. GRANT:
The rank of major-general is granted Buell, Pope, McClernand, C. F. Smith, and Wallace. General Buell's force will concentrate at Waynesborough. You will act in concert, but he will exercise his separate command, unless the enemy should attack you. In that case you are authorized to take the general command.
H. W. HALLECK, Major-General.
````

### force-1881-shiloh

Path: `data/raw/shiloh/force-1881-shiloh.txt`.
SHA-256: `b163fbab48f96742ce0584a6b5c29506123728b3edbac6381318e3a4853c70f1`.

````text
M. F. Force: From Fort Henry to Corinth, strength discussion

## preface
PREFACE. I have endeavored to prepare the following narrative from authentic material, contemporaneous, or nearly contemporaneous, with the events described. The main source of information is the official reports of battles and operations. These reports, both National and Confederate, will appear in the series of volumes of Military Reports now in preparation under the supervision of Colonel Scott, Chief of the War Records Office in the War Department. Executive Document No. 66, printed by resolution of the Senate at the Second Session of the Thirty-seventh Congress, contains a number of separate reports of casualties, lists of killed, wounded, and missing, which do not appear in the volumes of Military Reports as now printed. Several battle reports are printed in volume IV., and in the "Companion," or Appendix volume of Moore's Rebellion Record, which are not contained in the volumes of Military Reports as now printed. The reports of the Twentieth Ohio and the Fifty-third Ohio, of the battle of Shiloh, have never been printed. Colonel Trabue's report of his brigade in the battle of Shiloh has never been officially printed; but it is [Pg vi] given in the history of the Kentucky Brigade from Colonel Trabue's retained copy, found by his widow among his papers. The Reports of the Committee on the Conduct of the War contain original matter in addition to what appears in reports of battles and operations. The reports of the Adjutant-Generals of the different States, printed during the war, often supplement the official reports on file in Washington. Some regimental histories, printed soon after the close of the war, contain diaries and letters and narrate incidents which enable us in some cases to fix dates, the place of camps, and positions in battle, which could hardly otherwise be determined with precision. Newspaper correspondents, while narrating what they personally saw, give descriptions which impart animation to the sedate statements of official reports. Colonel William Preston Johnston's life of his father, General A.S. Johnston, can be used in some respects as authority. He served first in the Army of Northern Virginia, and was, most of the war, on the staff of Jefferson Davis. He thus, after his father's death, became possessed of a valuable collection of authentic official papers. When he was preparing the biography, all papers of value in private hands in the South were open to his use. Letters and memoranda preserved by Colonel Charles Whittlesey, and some of my own, have been of service. I am under obligation to Colonel Scott for permission to freely read and copy, in his office, the reports compiled under his direction. To Ex-President Hayes for the loan of a set [Pg vii] of the series of Military Reports, both National and Confederate, so far as printed, though not yet issued. To the Historical and Philosophical Society of Ohio for the unrestricted use of its library. To Colonel Charles Whittlesey of Cleveland, and Major E.C. Dawes, of Cincinnati, for the use of original manuscripts as well as printed reports. M.F. FORCE.

## pp178-180
The number of Johnston's army has already been given as 40,000 men. Badeau says the effective force present in the National camps Sunday morning was 33,000 men. General Sherman makes the number 32,000. William Preston Johnston, in the Life of his father, makes the number of the National troops, the "grand total in Sunday's battle," 41,543. These various statements arise from the different ways of making and reading returns. Forty thousand does not represent the total force which A.S. Johnston led to Shiloh. Forty thousand "present for duty" is exclusive not only of the brigade of detailed teamsters and cooks that General Johnston complained of, but of all regular and permanent details. It appears from some reports which give numbers, that it was also exclusive of temporary details made for the occasion of the battle—hospital men, train guards, ammunition guards, sappers and miners, infantry detailed to act with batteries, etc. It appears from some of the reports, [Pg 179] which state numbers, that the "enlisted men" "present for duty," in the "Field Returns of the Confederate Forces that marched from Corinth to the Tennessee River," comprised only non-commissioned officers and privates, and was therefore exclusive of musicians, buglers, artificers, etc., though enlisted as such. The 40,000, therefore, is the number of the combatants engaged in the battle. The field return is susceptible of further explanations, the character of which does not appear. The field return, for example, gives the "present for duty," in the artillery in Polk's corps, as 20 officers and 331 enlisted men—351 in all; while the official report of the chief of artillery of the corps, of casualties in the battle, giving each battery separately, states the number actually engaged in the battle as 21 officers, 56 non-commissioned officers, and 369 privates, making a total of 446. It is clear, therefore, that the 40,000 is intended as the number of officers, non-commissioned officers, and privates actually engaged in the battle, and a comparison of the reports of General Polk's chief of artillery with the returns suggests that in some way it may not be the full number of combatants engaged. The aggregation of returns making 41,153 present for duty in Grant's army at Pittsburg Landing, Sunday morning, is not a consolidated return, but a collection of footings of regimental returns, the nearest in date attainable to April 6th, for the most part furnished by the War Department to Colonel Johnson, the rest either taken from reports of State adjutant-generals, or else estimated. The statement includes the Fourteenth Wisconsin and the Fifteenth Michigan, neither of which arrived till after the close of Sunday's battle. [3] Deducting the "present for duty" given for these, 1,488, leaves, in round numbers, as in General Johnston's army, [Pg 180] 40,000. But "present for duty" in the returns of the National forces, includes musicians, buglers, artificers, etc.; all men present for the duty for which they were enlisted. The army was clothed with music. There were 72 regiments present, including those which arrived Sunday morning. The field music of 720 companies, with the buglers of cavalry and artillery, made about three thousand men. Besides these there were bands so numerous that an order was shortly afterward made, restricting the number of bands to one to each brigade. Where the battle reports give the number taken into action, the difference in the number given and the number of "present for duty," as given by the War Department to Colonel Johnston, suggests that many had gone on to the sick list, or been detailed, between the date of the return and April 6th; or that many men present for duty were left behind in camp. Probably all were true, and thirty-three thousand or thirty-two thousand is the number of officers, non-commissioned officers, and privates actually engaged in Sunday's battle on the National side. The reinforcements of Monday numbered, of Buell's army, about twenty thousand; Lewis Wallace, sixty-five hundred; other regiments, about fourteen hundred. [3] This is a mistake as to the Fifteenth Michigan, which lost, Sunday, 33 killed, 64 wounded, and 7 missing.
````

### gudmens-shiloh-handbook

Path: `data/raw/shiloh/gudmens-shiloh-handbook.txt`.
SHA-256: `f9598f35502e9081e7bb056e59790c42ff476371984a3ea452e37ac36e395cf5`.

````text
Gudmens and Staff Ride Team: Shiloh handbook excerpts

## p84
of the situation, he ordered his Assistant Adjutant General Captain John Rawlins to send Chief Quartermaster Captain A.S. Baxter to Crump’s Landing to order Wallace’s division forward. When Rawlins gave Baxter the instructions, Baxter thought it best that orders be written, so Rawlins went on the Tigress, found a scrap of paper and a pencil, and drafted the orders. Baxter immediately departed on the Tigress, arriving at Crump’s Landing at 1100. There he found the horse Wallace left and rode to Stoney Lonesome, arriving at 1130. Baxter handed the order to Wallace, who read it and said he was prepared to move. Baxter returned to the Tigress, and Wallace handed the order to one of his staff officers, Captain Frederick Knefler, who put it under his sword belt. Sometime during the day the orders fell out of the belt, an event that would haunt Wallace for the rest of his life. After the battle there was a controversy about Wallace’s movements to the battle. Grant and his staff officers said the order told Wallace to take “the road nearest to and parallel with the river.” Wallace and his staff of - ficers, however, said the order told them to “come up and take position on the right of the Army.” Regardless, Wallace decided to move his division down the Shunpike as he had planned.

## p85
Lew Wallace did not arrive at the battlefield until after dark on 6 April. Due to the vague orders and Wallace’s marching decisions, the 3d Division’s 5,800 men did not fight that day. For the rest of his life Wallace would have to defend his actions on 6 April. Why did he take the Shun - pike? Why did he let his soldiers eat before they marched? Why did he countermarch? Why was he so slow?

## p100
Members of Johnston’s staff wrapped his body, hiding his identity so his loss would not damage morale and started it back to Corinth. Staff officers quickly rode to Beauregard at the intersection of the Pittsburg- Corinth Road and Purdy-Hamburg Road and told him of Johnston’s death. Beauregard was now commander of the Army of the Mississippi.

## p113
At 1700 Nelson’s lead brigade, commanded by COL Jacob Ammen, arrived across the river from Pittsburg Landing. Nelson arranged for boats in the river to start moving his men across, and by 1800 he had about 600 men west of the river and in line.

## p137-heading
Numbers in parentheses: present/killed/wounded/missing K = killed, MW = mortally wounded, W = wounded, C = captured
````

### or-confederate-report-136-v1

Path: `data/raw/shiloh/or-confederate-report-136-v1.txt`.
SHA-256: `28e6ed7c4886cb04d4690469c824bb343f66b6c761f8da3334ef58decdc5d1e7`.

````text
Confederate field return, report No. 136: selected columns

## p398
No. 136.
Field return of the Confederate forces that marched from Corinth to the Tennessee River, April 3, 1862.

Columns: Command | Present, For duty, Officers | Present, For duty, Enlisted men | Present, Effective total.
Infantry, First Corps* | 561 | 8,440 | 9,024
Infantry, Second Corps | 1,000 | 14,590 | 14,868
Infantry, Third Corps | 339 | 4,108 | 4,545
Infantry, Reserve Corps | 479 | 6,132 | 6,290
Total infantry | 2,379 | 33,270 | 34,727
Artillery, First Corps | 20 | 331 | 398
Artillery, Second Corps | 28 | 661 | 661
Artillery, Third Corps | 16 | 284 | 310
Artillery, Reserve Corps | 19 | 581 | 604
Total artillery | 83 | 1,857 | 1,973
Cavalry | 125 | 1,884 | 2,073
Grand total | 2,587 | 37,011 | 38,773

Columns: Command | Present, Total | Present, Aggregate | Present and absent, Total | Present and absent, Aggregate.
Total infantry | 41,457 | 44,159 | 50,088 | 53,334
Total artillery | 2,183 | 2,353 | 2,481 | 2,586
Cavalry | 2,785 | 2,932 | 3,683 | 3,854
Grand total | 46,425 | 49,444 | 57,252 | 59,774

* Colonel Hill's regiment (Tennessee) came upon the [field] during the engagement on Monday.
Respectfully submitted and forwarded.
[JUNE 30, 1862.]
BRAXTON BRAGG,
General, Commanding.

## transcription-scope
Editorial transcription note: Selected columns from the entire printed p.398 / PDF p.422. Hierarchical row/column headings flattened; printed values retained without arithmetic correction. Present sick, extra-duty and in-arrest columns and all absent-category cells are omitted here; they remain visible in the registered full-page facsimile. Present has separate For duty, Sick, Extra duty, In arrest, Effective total, Total and Aggregate columns. Absent has Detached duty, With leave, Without leave and Sick columns. Each category except the three present summary columns is divided into Officers and Enlisted men. The final Present and absent group has Total and Aggregate columns. No definition equating Effective total with officers plus enlisted men For duty is supplied on this page. Square brackets in the Hill footnote and forwarding date are printed in the original compilation. April 3 belongs to the heading's description of the march; an exact underlying muster time is not separately stated.
````

### or-confederate-report-137-v1

Path: `data/raw/shiloh/or-confederate-report-137-v1.txt`.
SHA-256: `675efae865fa9d112b9f8aa6c3585221c8b742fbe092dfc5a130a38b43fb0f72`.

````text
Confederate field return, report No. 137: selected columns

## p399
No. 137.
Field return of the Army of the Mississippi after the battle of Shiloh (April 10, 1862).

Columns: Command | Present, For duty, Officers | Present, For duty, Enlisted men | Present, Effective total.
Infantry, First Corps | 461 | 7,198 | 7,582
Infantry, Second Corps | 590 | 8,453 | 9,118
Infantry, Third Corps | 425 | 4,305 | 4,865
Infantry, Reserve Corps | 379 | 4,334 | 5,232
Total infantry | 1,855 | 24,692 | 26,697
Artillery, First Corps | 18 | 386 | 390
Artillery, Second Corps | 19 | 487 | 504
Artillery, Third Corps | 8 | 272 | 284
Artillery, Reserve Corps | 25 | 489 | 504
Total artillery | 70 | 1,634 | 1,682
Cavalry | 259 | 3,584 | 3,833
Grand total | 2,184 | 29,910 | 32,212

Columns: Command | Present, Total | Present, Aggregate | Present and absent, Total | Present and absent, Aggregate.
Total infantry | 37,153 | 39,673 | 51,515 | 54,859
Total artillery | 2,095 | 2,172 | 2,515 | 2,619
Cavalry | 5,340 | 5,648 | 6,931 | 7,022
Grand total | 44,588 | 47,493 | 60,961 | 64,500

NOTE.-The difference in aggregates and totals between this and the preceding return is accounted for thus: First, by killed, wounded, and missing in battle, and the arrival of Carroll's brigade and a portion of the cavalry, heretofore detached.
Respectfully submitted and forwarded.
[JUNE 30, 1862.]
BRAXTON BRAGG,
General, Commanding.

## transcription-scope
Editorial transcription note: Selected columns from the entire printed p.399 / PDF p.423. Hierarchical row/column headings flattened; printed values retained without arithmetic correction. Present sick, extra-duty and in-arrest columns and all absent-category cells are omitted here; they remain visible in the registered full-page facsimile. Present has separate For duty, Sick, Extra duty, In arrest, Effective total, Total and Aggregate columns. Absent has Detached duty, With leave, Without leave and Sick columns. Each category except the three present summary columns is divided into Officers and Enlisted men. The final Present and absent group has Total and Aggregate columns. No definition equating Effective total with officers plus enlisted men For duty is supplied on this page. Square brackets around the forwarding date are printed in the original compilation. April 10 is the return date in the heading; it is not the later submission/forwarding date. The infantry effective rows sum to 26,797, not the printed 26,697; its enlisted For duty rows sum to 24,290, not the printed 24,692. Those arithmetic diagnostics do not authorize corrected source values. This is a selected-column audit, not a certification of every table cell.
````

### or-wallace-availability-v1

Path: `data/raw/shiloh/or-wallace-availability-v1.txt`.
SHA-256: `d23c3a22984876a9f744f97d4a8acf642a663daf0b215285b38455145a218190`.

````text
Lew Wallace: detachments and arrival, report 34

## p169-heading
No. 34. Reports of Maj. Gen. Lewis Wallace, U. S. Army, commanding Third Division, with communications in reference thereto. HDQRS. THIRD DIVISION, UNITED STATES FORCES, Pittsburg Landing, Tenn., April 12, 1862.

## p170
At 11.30 o'clock the anticipated order arrived, directing me to come up and take position on the right of the army and form my line of battle at a right angle with the river. As it also directed me to leave a force to prevent surprise at Crump's Landing, the Fifty-sixth Ohio and Sixty-eighth Ohio Regiments were detached for that purpose, with one gun from Lieutenant Thurber's battery.
This movement occasioned a counter-march, which delayed my junction with the main army until a little after night-fall.
About 1 o'clock at night my brigades and batteries were disposed, forming the extreme right, and ready for battle.
Shortly after daybreak Captain Thompson opened fire on a rebel battery posted on a bluff opposite my First Brigade, and across a deep and prolonged hollow, traced by a creek and densely wooded on both sides.

## transcription-scope
Selected statements only. The route explanation is Wallace's account, not a resolved causal finding. The report does not quantify the detached men in this passage. Printed pp.169-170 = parent PDF pp.193-194.
````

### or-prentiss-availability-v1

Path: `data/raw/shiloh/or-prentiss-availability-v1.txt`.
SHA-256: `87fad5def660a7a09b3075ba5c99b951cc64561a09154aafb0203bcce623388f`.

````text
Benjamin Prentiss: return attachment and Sixth Division availability, report 78

## p277
No. 78. Report of Brig. Gen. B. M. Prentiss, U. S. Army, commanding Sixth Division. QUINCY, ILL., November 17, 1862.
I have the honor to transmit field return of the force which was subject to my control, as it appeared upon the morning of the engagement, the same being marked A.
[Compiler footnote:] Embodied in revised statement, p. 112.

## p278-sixteenth
Hereupon the entire force, excepting only the Sixteenth Iowa, which had been sent to the field the day previous without ammunition, and the cavalry, which was held in readiness to the rear, was advanced to the extreme front, and thrown out alternately to the right and left.

## p278-twentythird
Being again assailed, in this position deserted, by an overwhelming force, and not being able to hold the ground, I ordered the division to fall back to the line occupied by General Hurlbut, and at 9.05 a. m. reformed to the right of General Hurlbut, and to the left of Brig. Gen. W. H. L. Wallace, who I found in command of the division assigned to Major-General Smith. At this point the Twenty-third Missouri Infantry, commanded by Colonel Tindall, which had just disembarked from a transport, and had been ordered to report to me as a part of the Sixth Division, joined me.

## transcription-scope
Selected report and compiler passages; square-bracketed compiler label is editorial. Prentiss reports after returning from captivity, over seven months after the battle. Attachment A itself is not recovered here. Printed pp.277-278 = PDF pp.301-302.
````

### or-chambers-availability-v1

Path: `data/raw/shiloh/or-chambers-availability-v1.txt`.
SHA-256: `d41b51cef5d5cd0bd334c35f169dc857edfc8e1a03d4fcaa1527d85da190c5e1`.

````text
Alexander Chambers: Sixteenth Iowa Sunday deployment, report 84

## p286
No. 84. Report of Col. Alexander Chambers, Sixteenth Iowa Infantry (of the Second Brigade).
Near Pittsburg Landing, April 24, 1862.
SIR: I have the honor to report that on Sunday morning, April 6, while my regiment was preparing to join General Prentiss' division, as was previously ordered, an aide of General Grant ordered my regiment in line on the right of the Fifteenth Iowa Volunteers, to act as a reserve and prevent stragglers from reaching the river. The line had been formed but a short time when I was ordered to march it, following the Fifteenth Iowa, to General McClernand's division, whose right was giving way.

## transcription-scope
Selected opening paragraph; the heading and dateline omit intervening headquarters lines. Printed p.286 = PDF p.310. Shares the Union reporting environment with Prentiss/Reid; no independence score is implied.
````

### or-reid-availability-v1

Path: `data/raw/shiloh/or-reid-availability-v1.txt`.
SHA-256: `b6192040bb437ea469fa67cb8422460ebe8605186524a5c3e890b7e5ec855f03`.

````text
Hugh Reid: Fifteenth Iowa arrival, report 85

## p288
No. 85. Report of Col. Hugh T. Reid, Fifteenth Iowa Infantry.
I have the honor to report that the Fifteenth Regiment of Iowa Volunteer Infantry from Benton Barracks arrived at Pittsburg on Sunday morning, with orders from General Grant's headquarters to report to General Prentiss. Finding that his headquarters were some 4 miles from the Landing, I proceeded at once to report to him in person, and found a heavy fire of artillery and musketry already commenced along his lines. Orders were received from his aide to bring up my command as soon as possible, and I returned to the river for that purpose. The regiment was rapidly disembarked, ammunition distributed, and the men for the first time loaded their guns.

## transcription-scope
Selected opening of report 85, printed p.288 = PDF p.312. No report date in this inspected heading; recorded_at remains null. This passage does not count opening combatants.
````

### or-rousseau-michigan-v1

Path: `data/raw/shiloh/or-rousseau-michigan-v1.txt`.
SHA-256: `1a5ba21b0cf1aaa8807601e5a02f1bda368df761435031c636526f15cb379fa6`.

````text
Lovell Rousseau: Fifteenth Michigan contingent on April 7, report 91

## p307
No. 91. Report of Brig. Gen. Lovell H. Rousseau, U. S. Army, commanding Fourth Brigade.
HEADQUARTERS FOURTH BRIGADE, Battle-field of Shiloh, Tenn., April 12, 1862.
GENERAL: I have the honor to report to you, as commander of the Second Division of the Army of the Ohio, the part taken by my brigade in the battle at this place on the 7th instant.

## p310
It is due to Colonel Oliver, officers, and men of the Fifteenth Michigan that I say he joined us early in the morning with about 230 officers and men of his regiment, and behaved well during the day of the battle.

## transcription-scope
Selected report opening and later paragraph, printed pp.307 and 310 = PDF pp.331 and 334. The opening establishes April 7 as the battle day being described. About 230 is a joining contingent, not the whole regiment on April 6.
````

### or-union-return-detail-v2

Path: `data/raw/shiloh/or-union-return-detail-v2.txt`.
SHA-256: `70099ece7f07cf264d777f3e9d80e49ec40c230b5c671962e3cdc0dbfd4f2c94`.

````text
Union return: Sixth Division component rows, p.112

## p112
APRIL 4-5, 1862.
Columns: Command | Present for duty: Officers | Men | Aggregate
Sixth Division:
1st Brigade | 119 | 2,671 | 2,790
2d Brigade | 85 | 1,689 | 1,774
Unattached | 41 | 858 | 899
Total Sixth Division | 245 | 5,218 | 5,463
Return dated April 5; strength of two regiments and one battery not reported on the original.
Division staff not included in this abstract.

## transcription-scope
Additional selected detail from the already pinned full-page facsimile or-union-return.png. Complements, does not overwrite, or-union-return-april4-5. The page does not name the omitted formations.
````

### reed-1909-union-audit-v1

Path: `data/raw/shiloh/reed-1909-union-audit-v1.txt`.
SHA-256: `87e1da1572aaceb0bb73422f008e411872174de01153d9d80a4659ceabdaee2f`.

````text
D. W. Reed: Union returns, detachments and late arrivals, revised 1909

## p60-second-brigade
The Sixteenth Iowa arrived at the Landing on Saturday, April 5, 1862. The colonel reported for duty and handed in his morning report, so that his regiment is included in Miller's report of present for duty. Not being fully equipped, the regiment did not go to camp, but remained at Landing; on Sunday it, with the Fifteenth Iowa, was, by order of General Grant, held for a time at the Landing to stop stragglers, and then sent to reinforce McClernand at his fifth line, where they were engaged and lost heavily.
The Eighteenth Wisconsin arrived on the field on Saturday afternoon and went at once into camp, but did not get into the morning report of that day and are not included in Miller's present for duty.

## pp60-61-michigan
The Fifteenth Michigan arrived at Pittsburg Landing April 5, 1862. Arms had been issued to the men, but no ammunition had been supplied. The regiment moved out upon the field early Sunday morning and formed line and stacked knapsacks, at the left of the Eighteenth Wisconsin in Locust Grove, just as Chalmers appeared in front and moved to the attack. Failing to obtain ammunition, Colonel Oliver ordered his men to fix bayonets, as if to charge the approaching Confederates, but reconsidered and about faced his men and returned to the Landing, where he obtained ammunition and again joined the fighting line at some place not now determined. On Monday morning the regiment joined Rousseau's brigade of the Army of the Ohio and fought with conspicuous gallantry all day.

## p61-wisconsin
The Fourteenth Wisconsin arrived upon the field Sunday night, and on Monday joined Smith's brigade of the Army of the Ohio and served with it all day.

## p92-heading
LEW. WALLACE'S (THIRD) DIVISION. (Return of Apr. 4.)

## p93
Selected columns: Command | For duty officers | For duty men | For duty total
68th Ohio* | 29 | 395 | 424
56th Ohio* | 32 | 669 | 701
3d Battalion, 11th Illinois* | 14 | 262 | 276
3d Battalion, 5th Ohio* | 14 | 269 | 283
Total cavalry | 28 | 531 | 559
Total Third Division | 314 | 7,250 | *7,564
* 2 regiments of infantry, 2 battalions of cavalry, 1 gun of Buel's battery, and train guard—a total of 1,727—were left at Crumps Landing, making the number actually engaged at Shiloh 5,837. Wallace says 5,000.

## p96
PRENTISS'S (SIXTH) DIVISION. (Return of Apr. 5.)
Selected columns: Command | For duty officers | For duty men | For duty total
Total First Brigade | 119 | 2,671 | 2,790
61st Illinois | 21 | 416 | 437
18th Missouri | 28 | 524 | 552
16th Iowa (note b) | 36 | 749 | 785
18th Wisconsin* (note d) | 35 | 700 | 735
Total Second Brigade | 120 | 2,389 | 2,509
15th Iowa* (note c) | 32 | 750 | 782
23d Missouri* (note e) | 35 | 540 | 575
Total unbrigaded | 67 | 1,290 | 1,357
Hickenlooper's battery, 5th Ohio | 4 | 133 | 137
Munch's battery, 1st Minnesota | 5 | 121 | 126
Total artillery | 9 | 254 | 263

## p97
Selected columns: Command | For duty officers | For duty men | For duty total
1st and 2d Battalions, 11th Illinois | 32 | 594 | 626
Total Sixth Division | 347 | 7,198 | 7,545
UNASSIGNED (note f).
14th Wisconsin* (note g) | 30 | 720 | 750
15th Michigan* (note h) | 30 | 720 | 750
Total unassigned infantry | 60 | 1,440 | 1,500
15th Michigan: Number engaged as reported by commander | 730
* Estimated.

## p98
RECAPITULATION. Selected for-duty totals:
Total Army of the Tennessee | 48,894
Deduct Third Division and unassigned infantry not on the field Apr. 6. | 9,064
Aggregate, Army of the Tennessee, present at Shiloh Apr. 6 (note p). | 39,830
Officers and men present for duty Apr. 6 (A. of T.). | 39,830
Reenforced Apr. 7 by the Third Division (see ante). | 5,837
And by unassigned infantry. | 1,500

## p111-union-notes
(b) The Sixteenth Iowa arrived at Pittsburg Landing on the 5th of April, 1862, and was assigned to the Sixth Division. The morning report was made and is included in the report of Second Brigade, Sixth Division, for April 5, 1862.
(c) The Fifteenth Iowa arrived at Pittsburg Landing Sunday morning, April 6, 1862, under orders to report to General Prentiss. Upon disembarking from steamboat it was, by General Grant, ordered to duty at the Landing with the Sixteenth Iowa, and later to a position in McClernand's line. It is not included in the Sixth Division returns of April 5.
(d) The Eighteenth Wisconsin arrived on the field April 5, 1862. It is not included in the returns made by the Sixth Division April 5, but it joined the Second Brigade of that division and encamped on the left of the brigade Saturday evening and was engaged as left regiment of Prentiss's division on Sunday.
(e) The Twenty-third Missouri arrived on the field Sunday morning, April 6, 1862, and reported to General Prentiss at the “Hornets' Nest” about 9 a. m. and fought with him the remainder of the day.
(f) Unassigned troops were all present on the 6th or 7th, but had not been assigned to a command and had not been taken up on the returns.
(g) The Fourteenth Wisconsin arrived from Savannah Sunday night, and on Monday fought with Smith's brigade, Army of the Ohio. The number present is estimated from returns of the Department of the Mississippi, March 31, 1862.
(h) The Fifteenth Michigan fought on Monday with the Fourth Brigade, Army of the Ohio.

## p112-note-r
(r) The “present for duty,” has been taken, in each case, as the number engaged in the battle. No attempt has been made to eliminate the noncombatants, because a teamster driving an ammunition wagon or an ambulance is just as necessary as the man with the musket, and just as much a part of the fighting force.

## transcription-scope
Selected narrative, table cells and notes only. Table asterisks on pp.96-97 mean Estimated; p.93 has its own detachment footnote. The full pp.93,96,97,98 scans are separately pinned. Printed pp.60-61,92-93,96-98,111-112 = PDF pp.62-63,94-95,98-100,113-114. Do not read the Sixth Division April 5 heading as an unchanged dated return: its notes include April 6 arrivals and estimates. The p.98 exclusion of unassigned infantry conflicts with the Fifteenth Michigan Sunday narrative. Note (r) states a population convention, not a verified equivalence. The quoted Wallace 5,000 remains secondhand; no underlying statement was inspected in this audit. Confederate notes on pp.111-112 are outside this transcription and audit.
````

### michigan-ag-1862-fifteenth-v1

Path: `data/raw/shiloh/michigan-ag-1862-fifteenth-v1.txt`.
SHA-256: `c143f241b2d96bc563a01f52f996c86634c5da7643952ee96259468f333fd92b`.

````text
Michigan Adjutant General: Fifteenth Infantry arrival and casualties

## report-heading
REPORT. MILITARY DEPARTMENT, MICHIGAN. ADJUTANT GENERAL'S OFFICE, Detroit, Dec. 24th, 1862.

## p41
FIFTEENTH INFANTRY.
This Regiment left its camp at Monroe on the 27th of March last, with 869 names on its rolls. The entire number which had been entered on its records July 1, was 887. It reached Pittsburgh Landing, on the Tennessee river, the day before the battle of April 6 and 7, and its participation in that action cost the Regiment a loss of two officers and 31 men killed, 1 officer and 63 privates wounded, and 7 missing.

## transcription-scope
Opening regimental paragraph only, manually transcribed from printed p.41 (PDF p.45); report heading PDF p.9 and title PDF p.5 inspected. The casualty sentence refers to the April 6-7 battle and does not apportion casualties by day. Names on March rolls are not an April 6 opening-strength count. The underlying regimental returns and any dependency behind Force's footnote are not established.
````

### or-nelson-reinforcements-v1

Path: `data/raw/shiloh/or-nelson-reinforcements-v1.txt`.
SHA-256: `e75987c53540b8ad09b7cf108204b7f7f9e6343b09da01570e862dba309986ed`.

````text
William Nelson: crossing, deployment and strength, report 103

## p323-heading
No. 103. Reports of Brig. Gen. William Nelson, U. S. Army, commanding Fourth Division. HEADQUARTERS FOURTH DIVISION, Camp on the Field of Battle, April 10, 1862.

## p323-crossing
the Fourth Division of the Army of the Ohio, under my command, left Savannah, by order of General Grant, reiterated by General Buell in person, at 1.30 p. m. on Sunday, April 6, and marched by land to the point opposite Pittsburg Landing. The anxiety of the soldiers to take part in the battle which was going on on the left bank of the river enabled me to achieve the distance, notwithstanding the dreadful state of the road over a lately overflowed bottom, in four hours. At 5 the head of my column marched up the bank at Pittsburg Landing and took up its position in the road under the fire of the rebel artillery, so close had they approached the Landing.

## pp323-324-action
The gallantry of the Thirty-sixth Indiana, supported by the Sixth Ohio, under the able conduct of Colonel Ammen, commanding Tenth Brigade, drove back the enemy and restored the line of battle. This was at 6.30 p. m., and soon after the enemy withdrew, owing, I suppose, to the darkness.

## p324-night
By 9 p. m. the infantry of my division were all across the river, and took up their positions as follows:

## p324-morning
At 4 a. m. I roused up the men quietly by riding along the line, and when the line of battle was dressed and the skirmishers well out and the reserves in position, I sent an aide to notify the general that I was ready to commence the action; whereupon the Fourth Division of the Army of the Ohio, in perfect order, as if on drill, moved toward the enemy. At 5.20 I found them, and the action commenced with vigor.

## p324-artillery
You are aware that owing to the want of transportation I was compelled to leave the three batteries of my division at Savannah.

## p325-strength
The loss of the division, I regret to inform you, is heavy. It went into action 4,541 strong,

## p326-return
Return of casualties in the Fourth Division, Army of the Ohio, at the battle of Pittsburg Landing, Tenn., April 6 and 7, 1862.
Selected column: Command | Officers and men taken into action
36th Indiana | 380
6th Ohio | 598
24th Ohio | 550
9th Indiana | 569
6th Kentucky | 484
41st Ohio | 371
1st Kentucky | 522
2d Kentucky | 663
20th Kentucky | 404
Total in division | 4,541
2d Indiana Cavalry: regiment not engaged.
Casualty markers for cavalry: Orderlies.
Compiler footnote: But see revised statement, p. 106.

## p327-march-return
Abstract from return of the Fourth (Nelson's) Division, Army of the Ohio, for the month of March, 1862.
Columns: Command | Present for duty officers | Men | Aggregate | Aggregate present and absent | Pieces of artillery
Tenth (Ammen's) Brigade | 63 | 1,924 | 1,987 | 2,864 | 6
Nineteenth (Hazen's) Brigade | 80 | 1,795 | 1,875 | 2,834 | 6
Twenty-second (Bruce's) Brigade | 80 | 1,892 | 1,972 | 2,648 | 6
Cavalry | 32 | 858 | 890 | 1,180 | [blank]
Total | 255 | 6,469 | 6,724 | 9,526 | 18
The division staff (6) not embraced in columns of figures.

## transcription-scope
Selected report paragraphs and table columns, printed pp.323-327 (PDF pp.347-351). The report is April 10; the casualty table has an April 6-7 scope; the compiler March return has no exact muster day. April 12/16 letters also printed on pp.326-327 are not the dates of these returns. Timing arithmetic is not silently corrected. Other casualty columns remain in the pinned scan. Literal [blank] and table/footnote labels are editorial.
````

### or-ammen-crossing-v1

Path: `data/raw/shiloh/or-ammen-crossing-v1.txt`.
SHA-256: `df186eb4f91fdb6dbc87cbf8e86e526f6d3f18c8dcc9730a858e7d3dc4ef9b93`.

````text
Jacob Ammen: April 10 report and separately printed diary extracts

## p327-heading
No. 104. Report of Col. Jacob Ammen, Twenty-fourth Ohio Infantry, commanding Tenth Brigade, with diary of his march from Nashville. HEADQUARTERS TENTH BRIGADE, FOURTH DIVISION, April 10, 1862.

## p328-report
April 6, at 1 o'clock p. m., the Tenth Brigade marched from Savannah for the battle-field. Arriving at the river opposite Pittsburg Landing the brigade was passed over on steamboats with the greatest practicable expedition, and on reaching the shore thousands of human beings, who had fled from their colors and assembled here, obstructed the road and caused considerable delay.
The Twenty-fourth and Sixth Ohio crossed the river as speedily as possible, and on arriving at the top of the bank the Twenty-fourth was ordered by General Grant to repair to a point one-half mile to the right, on a part of the line of battle threatened by the enemy. The Sixth Ohio was held in reserve.

## p329-diary-heading
Col. Jacob Ammen's diary of march to and battle at Pittsburg Landing, Tenn. [Extracts.]

## p330-diary
April 5.—Marched 9½ miles over bad roads, and reached Savannah, Tenn., before 12 m.

## p333-diary
General Nelson went over on the first boat with a part of the Thirty-sixth Indiana, Colonel Grose. General Nelson ordered me to remain and see my brigade over and give orders to the commanders of the other brigades (Colonels Hazen and Bruce) to bring their brigades after the Tenth.
On each side the boats were crowded with demoralized soldiers, so that only three or four companies could cross on a boat.
The Thirty-sixth Indiana and part of the Sixth Ohio Volunteer Infantry were placed in position behind the crest of the hill, near the battery,

## p334-diary
The remainder of the Sixth was formed in rear of our line of battle, but the Twenty-fourth Ohio Volunteer Infantry was ordered about half a mile to our right, where the enemy was making a desperate attack.
About 10 o'clock at night we commenced forming our new line of battle beyond the crest of the hill, in advance of our old line about 300 yards.
The Twenty-fourth Ohio Volunteer Infantry was brought back about midnight and formed my second line and reserve.

## transcription-scope
Report dateline applies to the report on pp.327-329 only. Diary extracts on pp.329 onward have event-date labels but their composition/submission date is not established here. These are two accounts by the same author, not independent witnesses. Selected passages concern crossings and formation, not proof of morale or blame. Printed page + 24 gives parent PDF locator.
````

### or-grose-crossing-v1

Path: `data/raw/shiloh/or-grose-crossing-v1.txt`.
SHA-256: `45557a169c58c848726a0105e883da9dd682b749c6d603d09d4578209ec09410`.

````text
William Grose: Thirty-sixth Indiana Sunday contingent, report 105

## p337-heading
No. 105. Report of Col. William Grose, Thirty-sixth Indiana Infantry. HDQRS. THIRTY-SIXTH REGIMENT INDIANA VOLUNTEERS, Near Pittsburg Landing, Tenn., April 8, 1862.

## p337
On our march from Savannah on the 6th my regiment had the advance of the column, and four companies forward as an advance guard, under command of Lieutenant-Colonel Carey, leaving four under my command at the head of the column (two companies having been left behind on other duty). On reaching the river with the four companies at the head of the column they were immediately ferried over to join those under Colonel Carey that had passed over before my arrival. On arriving on the south side of the river, under circumstances that looked discouraging to new troops, my regiment was formed (the eight companies about 400 strong) amid great commotion and excitement.
As soon as formed I was ordered to advance, to support Captain Stone's battery, about 150 yards distant from my place of forming, which was done in tolerable order; and as soon as the regiment was in place the firing commenced and continued until near dusk.
lay on our arms until 5.30 o'clock the next morning, when we were ordered and moved forward with the brigade in line of battle.

## transcription-scope
Selected passages, printed p.337 / PDF p.361. About 400 describes eight companies formed Sunday evening. It is not the entire brigade or a precise census at 18:00.
````

### or-anderson-crossing-v1

Path: `data/raw/shiloh/or-anderson-crossing-v1.txt`.
SHA-256: `2b609dc79ebb3d2fcc1d52c97b10271b415d5c7166dfaeb53dcfa3d074f8d725`.

````text
Nicholas Anderson: Sixth Ohio landing, report 106

## p338-heading
No. 106. Report of Lieut. Col. Nicholas L. Anderson, Sixth Ohio Infantry. HDQRS. SIXTH REGIMENT OHIO VOLUNTEERS, Battle-field at Pittsburg Landing, April 9, 1862.

## p339
The regiment was disembarked at about 5 o'clock on the evening of the 6th instant, and marched up the hill as quickly as possible amid the confusion and panic existing among some disorganized regiments at the landing place. I formed line of battle, under your directions, some 200 yards from the river, to support a battery then in danger of being charged by the enemy. The regiment laid on arms all night, two companies acting as skirmishers.
At daylight on the 7th the brigade formed in line of battle, skirmishers in advance, the Sixth Regiment holding the right.

## transcription-scope
Selected opening, printed pp.338-339 / PDF pp.362-363. Approximate landing time is the author's account, not an independently verified clock.
````

### or-jones-crossing-v1

Path: `data/raw/shiloh/or-jones-crossing-v1.txt`.
SHA-256: `a64da854998697a6d6d4cd6bfea1850eb26b360d69b5c4f485d75a3624f45edc`.

````text
Frederick Jones: Twenty-fourth Ohio landing, report 107

## p339-heading
No. 107. Report of Lieut. Col. Frederick C. Jones, Twenty-fourth Ohio Infantry. CAMP NEAR PITTSBURG LANDING, April 8, 1862.

## p339
We landed at this place about 5.30 p. m. of the 6th, and were immediately formed in line of battle on the river hill. After the repulse of the enemy at this point the regiment was moved by your direction about three-quarters of a mile to the right, and was then ordered by General Grant to advance into the woods a short distance, to ascertain, if possible, the position of the enemy's lines.
we halted and remained in position until about midnight, when we received your order to rejoin the brigade at the river.

## transcription-scope
Selected passages, printed p.339 / PDF p.363. Original report includes intermediate movement and gunboat-fire context; no exact landing count is given.
````

### or-edward-mccook-crossing-v1

Path: `data/raw/shiloh/or-edward-mccook-crossing-v1.txt`.
SHA-256: `68d57493f397798415ba132e2e72a4d78013445ca6a6d81c736877f4845a43fa`.

````text
Edward McCook: Second Indiana Cavalry crossing, report 116

## p354
No. 116. Report of Lieut. Col. Edward M. McCook, Second Indiana Cavalry. HEADQUARTERS SECOND INDIANA CAVALRY, On Field of Battle, April 10, 1862.
my regiment arrived opposite to Pittsburg Landing on Sunday evening, the 6th instant, with the rest of General Nelson's division, and in accordance with his orders remained there till the evening of the 7th, when they crossed to this side. The only portion of my command in the action were men detailed as orderlies for the different brigade commanders of this division.

## transcription-scope
Selected report, printed p.354 / PDF p.378. Do not confuse Edward M. McCook with Alexander McD. McCook. The orderly exception prevents coding all cavalry personnel as wholly absent from the action.
````

### or-crittenden-reinforcements-v1

Path: `data/raw/shiloh/or-crittenden-reinforcements-v1.txt`.
SHA-256: `235b01590b21cbf161ebe63162db73cf45184bd234f4025deae555040f317391`.

````text
Thomas Crittenden: boat arrival and cavalry exclusion, report 117

## p354-heading
No. 117. Report of Brig. Gen. Thomas L. Crittenden, U. S. Army, commanding Fifth Division. HEADQUARTERS FIFTH DIVISION, ARMY OF THE OHIO, Field of Shiloh, April 15, 1862.

## p354-cavalry
My command, consisting of the Eleventh and Fourteenth Brigades, under General J. T. Boyle and Col. W. S. Smith, two batteries of artillery, under Captains Mendenhall and Bartlett, and of Jackson's regiment of cavalry, the Third Kentucky, were all embarked in the most rapid manner, except Jackson's cavalry, which marched at once to the landing opposite Pittsburg Landing, and reached that point in good time and ready for the fight. I was very anxious to have this regiment with me on the field, and reported its presence to General Buell; but no transportation could be furnished,

## p355
We reached Pittsburg Landing at about 9 o'clock p. m. By order of General Buell my command was debarked as soon as it could be done, it being important to send back the boat, that McCook's division might be brought up for the battle of the next day.
At about 5 a. m. we were conducted to our position by General Buell in person. My division took its position on the right of General Nelson. General McCook came upon the field a little later and took his position (directed by General Buell, as I am informed) on my right, which placed me in the center of our army.

## transcription-scope
Selected report, printed pp.354-355 / PDF pp.378-379. Arrival, debarkation and line deployment remain separate. Descriptive readiness of opposite-bank cavalry is not evidence it fought.
````

### or-alexander-mccook-reinforcements-v1

Path: `data/raw/shiloh/or-alexander-mccook-reinforcements-v1.txt`.
SHA-256: `59ca8b68925fe217897e50272bcc0e2158325389ae5114b4cdfeb275736fe5ea`.

````text
Alexander McCook: Savannah, landing and staged deployment, report 90

## p302-heading
No. 90. Report of Brig. Gen. Alexander McD. McCook, U. S. Army, commanding Second Division. HDQRS. SECOND DIVISION, ARMY OF THE OHIO, Field of Shiloh, April 9, 1862.

## p302
I hastened forward, arriving at Savannah at 7 p. m. on the 6th instant, with my entire division, except the Second Regiment of Kentucky Cavalry, which I was forced to leave to guard the baggage. After resting my men two hours I marched to the river with General Rousseau's brigade, ordering the other brigades and the artillery to follow immediately.

## p303
Arriving at Pittsburg Landing at 5 o'clock a. m. on the 7th instant, finding General Rousseau's brigade disembarking, I marched forward to a point where I believed it would be of the most service.
As soon as the remainder of Colonel Kirk's brigade arrived I placed his brigade in position as a reserve.
In the mean time a portion of Colonel Gibson's brigade arrived,

## transcription-scope
Selected report, printed pp.302-303 / PDF pp.326-327. Commander arrival and one brigade disembarking do not establish that the whole division was ready at 05:00. Cavalry guard is an explicit scope exclusion.
````

### or-wood-reinforcements-v1

Path: `data/raw/shiloh/or-wood-reinforcements-v1.txt`.
SHA-256: `21570f8903b1535e674efa9d8c478954b69ab7de68c8445d27e2e338641a1357`.

````text
Thomas Wood: April 7 embarkation and staggered arrival, report 130

## p376-heading
No. 130. Report of Brig. Gen. Thomas J. Wood, U. S. Army, commanding Sixth Division. HDQRS. SIXTH DIVISION, ARMY OF THE OHIO, On the Battle-field, near Pittsburg, Tenn., April 10, 1862.

## p377
Savannah was reached early on the morning of the 7th, and so soon as possible the embarkation for the battle-field commenced. Wagner's brigade (the Twenty-first), consisting of the Fifteenth, Fortieth, and Fifty-seventh Indiana and Twenty-fourth Kentucky Volunteers, was first embarked.
The brigade had fully debarked by 12 m., and for its operations from that hour to my own arrival, at 1 p. m., I refer to Colonel Wagner's report, herewith submitted,
The Twentieth Brigade, consisting of the Sixty-fourth and Sixty-fifth Ohio and Thirteenth Michigan Regiments, was embarked so soon as transports were ready, and finding it would be impossible to get transportation immediately for the artillery and cavalry of my division, I accompanied this brigade.

## transcription-scope
Selected report, printed pp.376-377 / PDF pp.400-401. Noon is the reported debarkation of Wagner's brigade, not the arrival time of the entire division on the firing line. Wood's own 13:00 and Garfield's 13:30 brigade debarkation are differently scoped observations.
````

### or-garfield-reinforcements-v1

Path: `data/raw/shiloh/or-garfield-reinforcements-v1.txt`.
SHA-256: `950b5b0d8e5a5a34f9b3a7f55efc142091f2373b571955a0f897e8c090981150`.

````text
James Garfield: landing, advance and non-engagement, report 131

## p380
No. 131. Report of Brig. Gen. James A. Garfield, U. S. Army, commanding Twentieth Brigade. HEADQUARTERS TWENTIETH BRIGADE, In Bivouac, Battle-field, near Pittsburg, Tenn., April 9, 1862.
three regiments under my command—the Thirteenth Michigan and the Sixty-fourth and Sixty-fifth Ohio Volunteer Infantry—debarked at the Pittsburg Landing at 1.30 o'clock p. m. of Monday, the 7th instant.
I immediately moved my column forward about 3 miles to the front of General Buell's position, which I reached about 3 o'clock p. m.
My command was for some time under fire from the batteries of the enemy, but as he was then in retreat, and the tide of battle soon swept farther to the front, we were not engaged.

## transcription-scope
Selected report, printed p.380 / PDF p.404. Garfield reports presence under fire and says not engaged. Do not erase this distinction, infer zero availability at an earlier time, or add his brigade to an estimate that includes only Wagner.
````

### or-buell-reinforcements-v2

Path: `data/raw/shiloh/or-buell-reinforcements-v2.txt`.
SHA-256: `57627b0ea1c1e71c61d213fe4c52b692d292a20ae7c45e43677380ade6da4973`.

````text
Don Carlos Buell: Savannah arrival and artillery transport supplement, report 87

## p291
HEADQUARTERS ARMY OF THE OHIO, Field of Shiloh, April 15, 1862.
I left the evening of that day, and arrived at Savannah on the evening of the 5th. General Nelson, with his division, which formed the advance, arrived the same day.

## p292
I learned that General Grant had just started, leaving orders for General Nelson to march to the river opposite Pittsburg Landing to be ferried across. On examination of the road up the river I discovered it to be impracticable for artillery, and General Nelson was directed to leave his to be carried forward by steamers.
In the mean time the remainder of General Nelson's division crossed, and General Crittenden's arrived from Savannah by steamers.
During the night and early the following morning Captain Bartlett's Ohio battery, Captain Mendenhall's regular battery, and Captain Terrill's regular battery, Fifth Artillery, arrived. General McCook arrived at Savannah during the night of the 6th, and reached the field of battle early in the morning of the 7th.

## transcription-scope
Selected manually checked supplement to or-buell-shiloh-report; previous source remains unchanged. Printed pp.291-292 / PDF pp.315-316. Existing pp.293 and 295-296 excerpts retain forward deployment and late Wood/pursuit descriptions. Command claims remain interested testimony.
````

### reed-1909-ohio-strength-v1

Path: `data/raw/shiloh/reed-1909-ohio-strength-v1.txt`.
SHA-256: `9af7a9d42181a4cba1e3f7fffc0d73a3bd26c4b48aced3a9f3241711e939167a`.

````text
D. W. Reed: Army of the Ohio strength reconstruction and limits

## p100
M'COOK'S (SECOND) DIVISION—continued. (Return of Apr. 30.)
Selected columns: Command | For duty officers | Men | Total
Total Second Division | 332 | 8,786 | 9,118
Separate column: Number engaged as reported by commander
Number Second Division engaged at Shiloh Apr. 7* | 7,553
NELSON'S (FOURTH) DIVISION. (Returns of Mar. 31.)
Selected columns: Command | For duty total | Number engaged as reported by commander
36th Indiana | 508 | 380
6th Ohio | 715 | 598
24th Ohio | 653 | 550
Total Tenth Brigade | 1,876 | 1,528

## p101
Selected columns: Command | For duty total | Number engaged as reported by commander
Total Fourth Division | 5,535 | 4,541
Total Fourth Division present at Shiloh Apr. 7† | [blank] | 4,541
CRITTENDEN'S (FIFTH) DIVISION. (Returns of Mar. 31.)
Smith's (Fourteenth) Brigade.‡
Number Fifth Division engaged at Shiloh Apr. 7* | [blank] | 3,825
WOOD'S (SIXTH) DIVISION. Garfield's (Twentieth) Brigade.∥
* Approximated. Note j.
† General Nelson's report (10 War Records, 326).
‡ No reports for March or April.
∥ No reports for March or April. Not engaged at Shiloh.

## p102
Wagner's (Twenty-first) Brigade.*
Twenty-first Brigade† | 2,000
Total of Sixth Division engaged | 2,000
RECAPITULATION. Number engaged as reported by commander:
Second Division | 7,552
Fourth Division | 4,541
Fifth Division | 3,825
Sixth Division | 2,000
Total Army of the Ohio | 17,918
* No report for March or April.
† Arrived at Shiloh just before the battle ended. Estimated.

## p111-note-j
(j) The Army of the Ohio has very meager returns on file except as to the Fourth Division. The Second, Fifth, and Sixth Divisions are estimated from returns of March 20, March 31, and April 30, 1862. Compared with the Fourth Division returns of same dates and with Nelson's report. (“Present, at Shiloh,” vol. 10, War Records, pp. 325, 326.) General Buell says, in letter on file: “I do not know whether the information was available at the time of rendering my report, but I have had it in my mind that my strength was between 18,000 and 19,000.” He further says: “I estimate McCook's present for duty at 7,552.” Only one brigade (Wagner's) of the Sixth Division was engaged. General Garfield says that his brigade did not reach the field until too late to become engaged. Only Wagner's brigade, estimated at 2,000, is included in present for duty of the Sixth Division.

## transcription-scope
Selected columns/notes, printed pp.100-102 and 111 / PDF pp.102-104 and 113. The p.100 row prints 7,553; p.102 and note j print 7,552. Preserve both. Dates in headings describe underlying returns; note j describes later estimation. Buell's letter is quoted secondhand; its date and original manuscript were not inspected. The arithmetic sum is not a synchronized dawn force. Editorial [blank] indicates absent cells; omitted cells are not zeros. The common p.112 PFD-as-engaged rule is retained in reed-1909-union-audit-v1.
````

## Scan index

Purposive diagnostic sample: all 13 existing table facsimiles plus 13 supplementary narrative/notes pages. No random selection or population extraction-error estimate is implied.

| ID | Image path from bundle root | Locator |
|---|---|---|
| or-union-return-scan | `data/raw/shiloh/or-union-return.png` | Official Records I.X.1 printed p.112 facsimile |
| or-confederate-return-scan | `data/raw/shiloh/or-confederate-return.png` | Official Records I.X.1 printed p.396 facsimile |
| or-confederate-report-136-v1-scan | `data/raw/shiloh/or-confederate-report-136-v1.png` | Official Records I.X.1 printed p.398 facsimile (report 136, v1) |
| or-confederate-report-137-v1-scan | `data/raw/shiloh/or-confederate-report-137-v1.png` | Official Records I.X.1 printed p.399 facsimile (report 137, v1) |
| reed-1909-union-p93-facsimile-v1 | `data/raw/shiloh/reed-1909-union-p93-facsimile-v1.png` | Printed p.93; parent PDF p.95 |
| reed-1909-union-p96-facsimile-v1 | `data/raw/shiloh/reed-1909-union-p96-facsimile-v1.png` | Printed p.96; parent PDF p.98 |
| reed-1909-union-p97-facsimile-v1 | `data/raw/shiloh/reed-1909-union-p97-facsimile-v1.png` | Printed p.97; parent PDF p.99 |
| reed-1909-union-p98-facsimile-v1 | `data/raw/shiloh/reed-1909-union-p98-facsimile-v1.png` | Printed p.98; parent PDF p.100 |
| or-reinforcement-p326-facsimile-v1 | `data/raw/shiloh/or-reinforcement-p326-facsimile-v1.png` | Printed p.326; parent PDF p.350 |
| or-reinforcement-p327-facsimile-v1 | `data/raw/shiloh/or-reinforcement-p327-facsimile-v1.png` | Printed p.327; parent PDF p.351 |
| reed-reinforcement-p100-facsimile-v1 | `data/raw/shiloh/reed-reinforcement-p100-facsimile-v1.png` | Printed p.100; parent PDF p.102 |
| reed-reinforcement-p101-facsimile-v1 | `data/raw/shiloh/reed-reinforcement-p101-facsimile-v1.png` | Printed p.101; parent PDF p.103 |
| reed-reinforcement-p102-facsimile-v1 | `data/raw/shiloh/reed-reinforcement-p102-facsimile-v1.png` | Printed p.102; parent PDF p.104 |
| review-or-p323 | `reviews/TN003-a42f063-v1/pages/or-p323.png` | Printed p.323; PDF p.347 |
| review-or-p324 | `reviews/TN003-a42f063-v1/pages/or-p324.png` | Printed p.324; PDF p.348 |
| review-or-p328 | `reviews/TN003-a42f063-v1/pages/or-p328.png` | Printed p.328; PDF p.352 |
| review-or-p329 | `reviews/TN003-a42f063-v1/pages/or-p329.png` | Printed p.329; PDF p.353 |
| review-or-p330 | `reviews/TN003-a42f063-v1/pages/or-p330.png` | Printed p.330; PDF p.354 |
| review-or-p333 | `reviews/TN003-a42f063-v1/pages/or-p333.png` | Printed p.333; PDF p.357 |
| review-or-p334 | `reviews/TN003-a42f063-v1/pages/or-p334.png` | Printed p.334; PDF p.358 |
| review-or-p337 | `reviews/TN003-a42f063-v1/pages/or-p337.png` | Printed p.337; PDF p.361 |
| review-reed-p60 | `reviews/TN003-a42f063-v1/pages/reed-p60.png` | Printed p.60; PDF p.62 |
| review-reed-p61 | `reviews/TN003-a42f063-v1/pages/reed-p61.png` | Printed p.61; PDF p.63 |
| review-reed-p111 | `reviews/TN003-a42f063-v1/pages/reed-p111.png` | Printed p.111; PDF p.113 |
| review-reed-p112 | `reviews/TN003-a42f063-v1/pages/reed-p112.png` | Printed p.112; PDF p.114 |
| review-michigan-p41 | `reviews/TN003-a42f063-v1/pages/michigan-p41.png` | Printed p.41; PDF p.45 |

## Source registry

```json
{
  "schema_version": 1,
  "sources": [
    {
      "id": "arnold-cwsac-battles",
      "title": "CWSAC battles, digitized by Jeffrey B. Arnold",
      "path": "data/raw/cwsac_battles.csv",
      "format": "csv",
      "primary_key": [
        "battle"
      ],
      "url": "https://raw.githubusercontent.com/jrnold/acw_battle_data/3a6020dbfcbcfc650a268b10a9f155588472432b/build/acw_battle_data/cwsac_battles.csv",
      "download_url": "https://raw.githubusercontent.com/jrnold/acw_battle_data/3a6020dbfcbcfc650a268b10a9f155588472432b/build/acw_battle_data/cwsac_battles.csv",
      "upstream_commit": "3a6020dbfcbcfc650a268b10a9f155588472432b",
      "retrieved_at": "2026-09-20",
      "sha256": "952b5d08402a7b77a42de709a87cd96540e460dd6fd4911d30574b5ad3585f1f",
      "rights": "CC-BY-4.0 per pinned package metadata (version 11.0.0); original NPS summaries attributed to NPS",
      "source_kind": "digitized_government_secondary_history",
      "independence_group": "nps-cwsac",
      "upstream_version": "11.0.0"
    },
    {
      "id": "arnold-cwsac-forces",
      "title": "CWSAC forces, digitized by Jeffrey B. Arnold",
      "path": "data/raw/cwsac_forces.csv",
      "format": "csv",
      "primary_key": [
        "battle",
        "belligerent"
      ],
      "url": "https://raw.githubusercontent.com/jrnold/acw_battle_data/3a6020dbfcbcfc650a268b10a9f155588472432b/build/acw_battle_data/cwsac_forces.csv",
      "download_url": "https://raw.githubusercontent.com/jrnold/acw_battle_data/3a6020dbfcbcfc650a268b10a9f155588472432b/build/acw_battle_data/cwsac_forces.csv",
      "upstream_commit": "3a6020dbfcbcfc650a268b10a9f155588472432b",
      "retrieved_at": "2026-09-20",
      "sha256": "a462f6be964b5d486f9cff4660262f215cffb8197d018654b74aab4e718dd7d5",
      "rights": "CC-BY-4.0 per pinned package metadata (version 11.0.0); original NPS summaries attributed to NPS",
      "source_kind": "digitized_government_secondary_history",
      "independence_group": "nps-cwsac",
      "upstream_version": "11.0.0"
    },
    {
      "id": "arnold-cwsac-commanders",
      "title": "CWSAC commanders, digitized by Jeffrey B. Arnold",
      "path": "data/raw/cwsac_commanders.csv",
      "format": "csv",
      "primary_key": [
        "battle",
        "belligerent",
        "fullname"
      ],
      "url": "https://raw.githubusercontent.com/jrnold/acw_battle_data/3a6020dbfcbcfc650a268b10a9f155588472432b/build/acw_battle_data/cwsac_commanders.csv",
      "download_url": "https://raw.githubusercontent.com/jrnold/acw_battle_data/3a6020dbfcbcfc650a268b10a9f155588472432b/build/acw_battle_data/cwsac_commanders.csv",
      "upstream_commit": "3a6020dbfcbcfc650a268b10a9f155588472432b",
      "retrieved_at": "2026-09-20",
      "sha256": "6c587c2987171764f362513f31eaf7c713b888b806419291c494623ea41800c7",
      "rights": "CC-BY-4.0 per pinned package metadata (version 11.0.0); original NPS summaries attributed to NPS",
      "source_kind": "digitized_government_secondary_history",
      "independence_group": "nps-cwsac",
      "upstream_version": "11.0.0"
    },
    {
      "id": "arnold-cwsac-campaigns",
      "title": "CWSAC campaigns, digitized by Jeffrey B. Arnold",
      "path": "data/raw/cwsac_campaigns.csv",
      "format": "csv",
      "primary_key": [
        "campaign"
      ],
      "url": "https://raw.githubusercontent.com/jrnold/acw_battle_data/3a6020dbfcbcfc650a268b10a9f155588472432b/build/acw_battle_data/cwsac_campaigns.csv",
      "download_url": "https://raw.githubusercontent.com/jrnold/acw_battle_data/3a6020dbfcbcfc650a268b10a9f155588472432b/build/acw_battle_data/cwsac_campaigns.csv",
      "upstream_commit": "3a6020dbfcbcfc650a268b10a9f155588472432b",
      "retrieved_at": "2026-09-20",
      "sha256": "93813220a72767a77a4632905d38718593d401901ae16698973e4ae8b9f555ae",
      "rights": "CC-BY-4.0 per pinned package metadata (version 11.0.0); original NPS summaries attributed to NPS",
      "source_kind": "digitized_government_secondary_history",
      "independence_group": "nps-cwsac",
      "upstream_version": "11.0.0"
    },
    {
      "id": "nps-tn003",
      "title": "NPS battle detail TN003",
      "path": "data/raw/nps-tn003.txt",
      "format": "text",
      "url": "https://www.nps.gov/civilwar/search-battles-detail.htm?battleCode=tn003",
      "retrieved_at": "2026-09-20",
      "sha256": "5a368744a4f1e6b231be2aac0903ea86b07e302634fd522dac53b433424a2941",
      "rights": "U.S. National Park Service government-authored battle summary; no images or logos copied",
      "source_kind": "government_secondary_history",
      "independence_group": "nps-cwsac",
      "snapshot_transform": "Python HTMLParser: omit script/style data, strip nonempty text nodes, join with newlines; retain Return to Results through before Experience More. This is normalized text, not original HTML."
    },
    {
      "id": "nps-md003",
      "title": "NPS battle detail MD003",
      "path": "data/raw/nps-md003.txt",
      "format": "text",
      "url": "https://www.nps.gov/civilwar/search-battles-detail.htm?battleCode=md003",
      "retrieved_at": "2026-09-20",
      "sha256": "d71c7a98380497be518ed6eae2803938d704818cea09cf7360583e1cafdad4e4",
      "rights": "U.S. National Park Service government-authored battle summary; no images or logos copied",
      "source_kind": "government_secondary_history",
      "independence_group": "nps-cwsac",
      "snapshot_transform": "Python HTMLParser: omit script/style data, strip nonempty text nodes, join with newlines; retain Return to Results through before Experience More. This is normalized text, not original HTML."
    },
    {
      "id": "arnold-package-metadata",
      "title": "American Civil War Battle Data package metadata",
      "path": "data/raw/upstream-package.yaml",
      "format": "text",
      "url": "https://raw.githubusercontent.com/jrnold/acw_battle_data/3a6020dbfcbcfc650a268b10a9f155588472432b/rawdata/metadata/datapackage.yaml",
      "download_url": "https://raw.githubusercontent.com/jrnold/acw_battle_data/3a6020dbfcbcfc650a268b10a9f155588472432b/rawdata/metadata/datapackage.yaml",
      "upstream_commit": "3a6020dbfcbcfc650a268b10a9f155588472432b",
      "retrieved_at": "2026-09-20",
      "sha256": "f5823133f2e0d0b839c14d54e066412ce9ac809f1dd38c1d76d0be100d146b07",
      "rights": "CC-BY-4.0",
      "source_kind": "package_metadata",
      "independence_group": "arnold-data-package"
    },
    {
      "id": "or-grant-shiloh-report",
      "title": "Ulysses S. Grant: Shiloh report excerpts",
      "path": "data/raw/shiloh/or-grant-shiloh-report.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "ab226b87fdbafcbe96e01564f596840b2b76fcf0f3cfe3aa83e1b1ee72f6d3cc",
      "author": "Ulysses S. Grant",
      "publication_date": "1884",
      "source_kind": "contemporary_participant_report",
      "independence_group": "or-grant",
      "snapshot_transform": "Selected embedded OCR text extracted with pypdf, whitespace collapsed. Printed-page section markers added. OCR spelling retained; these are not diplomatic transcriptions. Adjacent material on the selected pages is retained for context. Report dateline manually transcribed from visually inspected printed p.108 / PDF p.132; added as p108-heading.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "rights": "Public-domain U.S. government compilation published 1884; nineteenth-century reports. Transformed excerpts, not a new critical edition.",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "document_date": "1862-04-09",
      "limitations": "Participant account written after the outcome; self-justification and retrospective interpretation remain possible."
    },
    {
      "id": "or-buell-shiloh-report",
      "title": "Don Carlos Buell: Shiloh report excerpts",
      "path": "data/raw/shiloh/or-buell-shiloh-report.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "9581e8a1e7dc63d22c9999643183730d3ac22c216b731507bf993d2cafdbd425",
      "author": "Don Carlos Buell",
      "publication_date": "1884",
      "source_kind": "contemporary_participant_report",
      "independence_group": "or-buell",
      "snapshot_transform": "Selected embedded OCR text extracted with pypdf, whitespace collapsed. Printed-page section markers added. OCR spelling retained; these are not diplomatic transcriptions. Adjacent material on the selected pages is retained for context.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "rights": "Public-domain U.S. government compilation published 1884; nineteenth-century reports. Transformed excerpts, not a new critical edition.",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "document_date": "1862-04-15",
      "limitations": "Participant account written after the outcome; self-justification and retrospective interpretation remain possible."
    },
    {
      "id": "or-beauregard-shiloh-report",
      "title": "P. G. T. Beauregard: Shiloh report excerpts",
      "path": "data/raw/shiloh/or-beauregard-shiloh-report.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "c87c79162f5ef1a88bc308896b90a4178808a6b505e1b7ee805be535705a692c",
      "author": "P. G. T. Beauregard",
      "publication_date": "1884",
      "source_kind": "contemporary_participant_report",
      "independence_group": "or-beauregard",
      "snapshot_transform": "Selected embedded OCR text extracted with pypdf, whitespace collapsed. Printed-page section markers added. OCR spelling retained; these are not diplomatic transcriptions. Adjacent material on the selected pages is retained for context.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "rights": "Public-domain U.S. government compilation published 1884; nineteenth-century reports. Transformed excerpts, not a new critical edition.",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "document_date": "1862-04-11",
      "limitations": "Participant account written after the outcome; self-justification and retrospective interpretation remain possible."
    },
    {
      "id": "or-union-return-april4-5",
      "title": "Army of the Tennessee: abstracts of field returns, April 4–5, 1862",
      "path": "data/raw/shiloh/or-union-return-april4-5.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "e7b9aee495475a62721a811490c442f8019bc689a02dd841db0a5fbd60f8727e",
      "author": "War Records compilation of Army of the Tennessee divisional returns",
      "publication_date": "1884",
      "source_kind": "compiled_contemporary_returns",
      "independence_group": "or-union-returns",
      "snapshot_transform": "Manual transcription of division totals and notes from visually inspected printed p.112 / PDF p.136. Column headings expanded horizontally; bracketed missing cells and row labels are editorial. Brigade rows omitted. No missing strengths estimated.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "rights": "Public-domain U.S. government compilation published 1884; nineteenth-century reports. Transformed excerpts, not a new critical edition.",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "document_date": "1862-04-04/1862-04-05",
      "facsimile_source_id": "or-union-return-scan",
      "limitations": "Retrospectively compiled from returns on different dates; includes an absent division and explicitly incomplete returns."
    },
    {
      "id": "or-confederate-return",
      "title": "Army of the Mississippi: field return before and after Shiloh",
      "path": "data/raw/shiloh/or-confederate-return.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "6c127e6c1945754097a4b54a6efd98a9f7a35e3b009c7b9c5cd49056b0400c0c",
      "author": "Thomas Jordan, forwarded by P. G. T. Beauregard",
      "publication_date": "1884",
      "source_kind": "contemporary_staff_return",
      "independence_group": "or-beauregard",
      "snapshot_transform": "Manual transcription of table totals, headings, footnote, signatories and date from visually inspected printed p.396 / PDF p.420. Remarks column and neighboring enclosures omitted; no missing strengths estimated.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "rights": "Public-domain U.S. government compilation published 1884; nineteenth-century reports. Transformed excerpts, not a new critical edition.",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "document_date": "1862-04-21",
      "facsimile_source_id": "or-confederate-return-scan",
      "limitations": "Compiled after battle; own footnote records disagreement. Effective total is not a verified count of individuals actually engaged."
    },
    {
      "id": "or-halleck-orders",
      "title": "Halleck to Grant: March 20 and April 5 orders",
      "path": "data/raw/shiloh/or-halleck-orders.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/2warofrebellion10secrrich/2warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "b450b33b8475127a066ec9ab5257624ca818af9d8cd3049db0c5eab9c2501f21",
      "author": "Henry W. Halleck",
      "publication_date": "1884",
      "source_kind": "contemporary_order",
      "independence_group": "or-halleck",
      "snapshot_transform": "Manually transcribed from visually inspected printed pp.50–51 and 94 / PDF pp.58–59 and 102. Line-wrap hyphenation removed, whitespace normalized. A library stamp overlaps part of the final March 20 sentence; the text is legible on the scan.",
      "parent_download_url": "https://archive.org/download/2warofrebellion10secrrich/2warofrebellion10secrrich.pdf",
      "parent_sha256": "a52c65ca6fd0debeb8ab5c409bf09091f0478a3a2a3f9732f183f30502cbc955",
      "rights": "Public-domain U.S. government compilation published 1884; nineteenth-century reports. Transformed excerpts, not a new critical edition.",
      "edition": "Official Records, Series I, Volume X, Part II, 1884; printed page + 8 = PDF page.",
      "document_date": "1862-03-20/1862-04-05",
      "limitations": "Date of issuance does not by itself establish time of receipt or whether later orders modified the instruction."
    },
    {
      "id": "force-1881-shiloh",
      "title": "M. F. Force: From Fort Henry to Corinth, strength discussion",
      "path": "data/raw/shiloh/force-1881-shiloh.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://www.gutenberg.org/files/24438/24438-h/24438-h.htm",
      "retrieved_at": "2026-09-20",
      "sha256": "b163fbab48f96742ce0584a6b5c29506123728b3edbac6381318e3a4853c70f1",
      "author": "Manning Ferguson Force",
      "publication_date": "1881",
      "source_kind": "participant_authored_later_history",
      "independence_group": "force-1881",
      "snapshot_transform": "HTMLParser text nodes joined and whitespace collapsed; selected preface and pp.178–180 through footnote 3. Original page markers and footnote retained. Public-domain book excerpts, not the full ebook or modern facsimile foreword.",
      "parent_download_url": "https://www.gutenberg.org/files/24438/24438-h/24438-h.htm",
      "parent_sha256": "c0f2182c6330c5b344e119ec856f82625e643ba71f546e6c30b752d8c18676ff",
      "rights": "Underlying 1881 book is public domain in the United States. Text obtained from Project Gutenberg ebook 24438; no modern editorial foreword or artwork included.",
      "edition": "Campaigns of the Civil War, II. Original 1881 work; Gutenberg text from a later facsimile.",
      "dependencies": [
        "Official reports (explicit in preface)",
        "William Preston Johnston biography",
        "Badeau and Sherman figures quoted secondhand"
      ],
      "limitations": "Independently authored, not independent corroboration of official-report inputs. The text corrects its own Fifteenth Michigan exclusion in footnote 3; do not use the uncorrected subtraction as an opening strength."
    },
    {
      "id": "gudmens-shiloh-handbook",
      "title": "Gudmens and Staff Ride Team: Shiloh handbook excerpts",
      "path": "data/raw/shiloh/gudmens-shiloh-handbook.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/DTIC_ADA445681/DTIC_ADA445681.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "f9598f35502e9081e7bb056e59790c42ff476371984a3ea452e37ac36e395cf5",
      "author": "LTC Jeffrey J. Gudmens and the Staff Ride Team, Combat Studies Institute",
      "publication_date": "2004",
      "source_kind": "government_secondary_history",
      "independence_group": "gudmens-handbook",
      "snapshot_transform": "Selected government-authored narrative and table heading extracted with pypdf, whitespace collapsed. Printed pages 84, 85, 100, 113, 137 correspond to PDF pages 96, 97, 112, 125, 149. Modern third-party vignettes omitted. Printed pp.84–85 and 137 visually inspected.",
      "parent_download_url": "https://archive.org/download/DTIC_ADA445681/DTIC_ADA445681.pdf",
      "parent_sha256": "4b583c553a66e0c427b6239078bffb45cd724e37c1025dbf562cd01006431b3b",
      "rights": "U.S. Army Combat Studies Institute government-authored narrative; report cleared for public release. No photos, maps, logos, or third-party vignettes reproduced.",
      "edition": "Combat Studies Institute Press, Fort Leavenworth; DTIC ADA445681. Report documentation says 2004; library catalog data uses 2005.",
      "dependencies": [
        "Official Records",
        "Later participant memoirs and histories; see handbook bibliography"
      ],
      "limitations": "Teaching history with overlapping primary sources, not independent review. Narrative strength and appendix present counts have different scopes; no canonical reconciliation supplied."
    },
    {
      "id": "or-union-return-scan",
      "title": "Official Records I.X.1 printed p.112 facsimile",
      "path": "data/raw/shiloh/or-union-return.png",
      "format": "png",
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "5f885b86e24cdfc13bfe96c066e5b020a747f3b81ffc71896cdf80be0cd383da",
      "rights": "Public-domain U.S. government compilation published 1884; nineteenth-century reports. Transformed excerpts, not a new critical edition.",
      "source_kind": "facsimile_of_registered_return",
      "independence_group": "or-union-returns",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "snapshot_transform": "pdftoppm -f 136 -l 136 -scale-to 1800 -png -singlefile; entire page, unedited."
    },
    {
      "id": "or-confederate-return-scan",
      "title": "Official Records I.X.1 printed p.396 facsimile",
      "path": "data/raw/shiloh/or-confederate-return.png",
      "format": "png",
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "fdf3154912efd3121eb52e0cfdcb8cc5ab04c669a6758513b7547fd86e991e32",
      "rights": "Public-domain U.S. government compilation published 1884; nineteenth-century reports. Transformed excerpts, not a new critical edition.",
      "source_kind": "facsimile_of_registered_return",
      "independence_group": "or-beauregard",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "snapshot_transform": "pdftoppm -f 420 -l 420 -scale-to 1800 -png -singlefile; entire page, unedited."
    },
    {
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "version": 1,
      "author": "Braxton Bragg, submission/forwarding signature; underlying unit compilers not identified on the page",
      "publication_date": "1884",
      "document_date": "1862-06-30",
      "document_date_note": "Submission/forwarding date printed in square brackets, distinct from the date in the heading.",
      "independence_group": "or-beauregard",
      "rights": "Public-domain U.S. government compilation published 1884; nineteenth-century reports. Transformed excerpts, not a new critical edition.",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "dependencies": [
        "Same Army of the Mississippi reporting chain as Jordan/Beauregard; no independent corroboration established."
      ],
      "id": "or-confederate-report-136-v1",
      "title": "Official Records I.X.1 report No. 136: selected Confederate return columns (v1)",
      "path": "data/raw/shiloh/or-confederate-report-136-v1.txt",
      "format": "text",
      "sectioned": true,
      "sha256": "28e6ed7c4886cb04d4690469c824bb343f66b6c761f8da3334ef58decdc5d1e7",
      "source_kind": "contemporary_staff_return",
      "facsimile_source_id": "or-confederate-report-136-v1-scan",
      "snapshot_transform": "Manual selected-column transcription from visually inspected printed p.398 / PDF p.422. Hierarchical headings flattened; row labels expanded; commas and printed values retained. Present For duty (officers/enlisted) and Effective total retained for all command rows; Total/Aggregate columns retained for branch subtotals and grand total. Complete printed footnote/note, signature and bracketed forwarding date retained. Omitted columns and interpretive cautions are segregated in transcription-scope. No arithmetic emendation.",
      "limitations": "Retrospective staff return with multiple population columns; no opening-strength adjudication. Heading dates do not establish contemporary command knowledge. April 3 heading describes the march; Hill footnote mentions Monday arrival without its numerical accounting."
    },
    {
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "version": 1,
      "author": "Braxton Bragg, submission/forwarding signature; underlying unit compilers not identified on the page",
      "publication_date": "1884",
      "document_date": "1862-06-30",
      "document_date_note": "Submission/forwarding date printed in square brackets, distinct from the date in the heading.",
      "independence_group": "or-beauregard",
      "rights": "Public-domain U.S. government compilation published 1884; nineteenth-century reports. Transformed excerpts, not a new critical edition.",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "dependencies": [
        "Same Army of the Mississippi reporting chain as Jordan/Beauregard; no independent corroboration established."
      ],
      "id": "or-confederate-report-136-v1-scan",
      "title": "Official Records I.X.1 printed p.398 facsimile (report 136, v1)",
      "path": "data/raw/shiloh/or-confederate-report-136-v1.png",
      "format": "png",
      "sha256": "2cec00dfd99ed0a66e96977b3578606fd213930c1a3417c43d729bd787e537a5",
      "source_kind": "facsimile_of_registered_return",
      "snapshot_transform": "pypdfium2 PdfDocument(parent)[421].render(scale=3, rotation=90).to_pil().save(...): entire PDF page rendered clockwise so the sideways table reads horizontally; no crop, retouching or cell edits."
    },
    {
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "version": 1,
      "author": "Braxton Bragg, submission/forwarding signature; underlying unit compilers not identified on the page",
      "publication_date": "1884",
      "document_date": "1862-06-30",
      "document_date_note": "Submission/forwarding date printed in square brackets, distinct from the date in the heading.",
      "independence_group": "or-beauregard",
      "rights": "Public-domain U.S. government compilation published 1884; nineteenth-century reports. Transformed excerpts, not a new critical edition.",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "dependencies": [
        "Same Army of the Mississippi reporting chain as Jordan/Beauregard; no independent corroboration established."
      ],
      "id": "or-confederate-report-137-v1",
      "title": "Official Records I.X.1 report No. 137: selected Confederate return columns (v1)",
      "path": "data/raw/shiloh/or-confederate-report-137-v1.txt",
      "format": "text",
      "sectioned": true,
      "sha256": "675efae865fa9d112b9f8aa6c3585221c8b742fbe092dfc5a130a38b43fb0f72",
      "source_kind": "contemporary_staff_return",
      "facsimile_source_id": "or-confederate-report-137-v1-scan",
      "snapshot_transform": "Manual selected-column transcription from visually inspected printed p.399 / PDF p.423. Hierarchical headings flattened; row labels expanded; commas and printed values retained. Present For duty (officers/enlisted) and Effective total retained for all command rows; Total/Aggregate columns retained for branch subtotals and grand total. Complete printed footnote/note, signature and bracketed forwarding date retained. Omitted columns and interpretive cautions are segregated in transcription-scope. No arithmetic emendation.",
      "limitations": "Retrospective staff return with multiple population columns; no opening-strength adjudication. Heading dates do not establish contemporary command knowledge. April 10 after-battle return includes a note on arrivals; two infantry subtotal discrepancies retained. Selected-column audit, not a certification of all cells."
    },
    {
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "version": 1,
      "author": "Braxton Bragg, submission/forwarding signature; underlying unit compilers not identified on the page",
      "publication_date": "1884",
      "document_date": "1862-06-30",
      "document_date_note": "Submission/forwarding date printed in square brackets, distinct from the date in the heading.",
      "independence_group": "or-beauregard",
      "rights": "Public-domain U.S. government compilation published 1884; nineteenth-century reports. Transformed excerpts, not a new critical edition.",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "dependencies": [
        "Same Army of the Mississippi reporting chain as Jordan/Beauregard; no independent corroboration established."
      ],
      "id": "or-confederate-report-137-v1-scan",
      "title": "Official Records I.X.1 printed p.399 facsimile (report 137, v1)",
      "path": "data/raw/shiloh/or-confederate-report-137-v1.png",
      "format": "png",
      "sha256": "57335aa1a9cf578be6ae4abbd11224c07a8703c7420192181cd04ddb5346d114",
      "source_kind": "facsimile_of_registered_return",
      "snapshot_transform": "pypdfium2 PdfDocument(parent)[422].render(scale=3, rotation=90).to_pil().save(...): entire PDF page rendered clockwise so the sideways table reads horizontally; no crop, retouching or cell edits."
    },
    {
      "id": "or-wallace-availability-v1",
      "title": "Lew Wallace: detachments and arrival, report 34",
      "path": "data/raw/shiloh/or-wallace-availability-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "d23c3a22984876a9f744f97d4a8acf642a663daf0b215285b38455145a218190",
      "author": "Lewis Wallace",
      "publication_date": "1884",
      "document_date": "1862-04-12",
      "source_kind": "contemporary_participant_report",
      "independence_group": "or-wallace",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "rights": "Public-domain nineteenth/early-twentieth-century government publication; selected passages and tables, not a new critical edition.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered pages. Line-wrap hyphens removed; whitespace normalized; table column labels and selected cells linearized. Section IDs added. Editorial scope is separate from historical passage sections.",
      "limitations": "Participant report written after the event, published in a later compilation; not independently adjudicated."
    },
    {
      "id": "or-prentiss-availability-v1",
      "title": "Benjamin Prentiss: return attachment and Sixth Division availability, report 78",
      "path": "data/raw/shiloh/or-prentiss-availability-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "87fad5def660a7a09b3075ba5c99b951cc64561a09154aafb0203bcce623388f",
      "author": "Benjamin M. Prentiss",
      "publication_date": "1884",
      "document_date": "1862-11-17",
      "source_kind": "contemporary_participant_report",
      "independence_group": "or-prentiss",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "rights": "Public-domain nineteenth/early-twentieth-century government publication; selected passages and tables, not a new critical edition.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered pages. Line-wrap hyphens removed; whitespace normalized; table column labels and selected cells linearized. Section IDs added. Editorial scope is separate from historical passage sections.",
      "limitations": "Participant report written after the event, published in a later compilation; not independently adjudicated."
    },
    {
      "id": "or-chambers-availability-v1",
      "title": "Alexander Chambers: Sixteenth Iowa Sunday deployment, report 84",
      "path": "data/raw/shiloh/or-chambers-availability-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "d41b51cef5d5cd0bd334c35f169dc857edfc8e1a03d4fcaa1527d85da190c5e1",
      "author": "Alexander Chambers",
      "publication_date": "1884",
      "document_date": "1862-04-24",
      "source_kind": "contemporary_participant_report",
      "independence_group": "or-prentiss",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "rights": "Public-domain nineteenth/early-twentieth-century government publication; selected passages and tables, not a new critical edition.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered pages. Line-wrap hyphens removed; whitespace normalized; table column labels and selected cells linearized. Section IDs added. Editorial scope is separate from historical passage sections.",
      "limitations": "Participant report written after the event, published in a later compilation; not independently adjudicated."
    },
    {
      "id": "or-reid-availability-v1",
      "title": "Hugh Reid: Fifteenth Iowa arrival, report 85",
      "path": "data/raw/shiloh/or-reid-availability-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "b6192040bb437ea469fa67cb8422460ebe8605186524a5c3e890b7e5ec855f03",
      "author": "Hugh T. Reid",
      "publication_date": "1884",
      "document_date": null,
      "source_kind": "contemporary_participant_report",
      "independence_group": "or-prentiss",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "rights": "Public-domain nineteenth/early-twentieth-century government publication; selected passages and tables, not a new critical edition.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered pages. Line-wrap hyphens removed; whitespace normalized; table column labels and selected cells linearized. Section IDs added. Editorial scope is separate from historical passage sections.",
      "limitations": "Participant report written after the event, published in a later compilation; not independently adjudicated."
    },
    {
      "id": "or-rousseau-michigan-v1",
      "title": "Lovell Rousseau: Fifteenth Michigan contingent on April 7, report 91",
      "path": "data/raw/shiloh/or-rousseau-michigan-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "1a5ba21b0cf1aaa8807601e5a02f1bda368df761435031c636526f15cb379fa6",
      "author": "Lovell H. Rousseau",
      "publication_date": "1884",
      "document_date": "1862-04-12",
      "source_kind": "contemporary_participant_report",
      "independence_group": "or-buell",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "rights": "Public-domain nineteenth/early-twentieth-century government publication; selected passages and tables, not a new critical edition.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered pages. Line-wrap hyphens removed; whitespace normalized; table column labels and selected cells linearized. Section IDs added. Editorial scope is separate from historical passage sections.",
      "limitations": "Participant report written after the event, published in a later compilation; not independently adjudicated."
    },
    {
      "id": "or-union-return-detail-v2",
      "title": "Union return: Sixth Division component rows, p.112",
      "path": "data/raw/shiloh/or-union-return-detail-v2.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "70099ece7f07cf264d777f3e9d80e49ec40c230b5c671962e3cdc0dbfd4f2c94",
      "author": "Official Records compilers",
      "publication_date": "1884",
      "document_date": null,
      "source_kind": "government_compiled_return",
      "independence_group": "or-grant",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "rights": "Public-domain nineteenth/early-twentieth-century government publication; selected passages and tables, not a new critical edition.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered pages. Line-wrap hyphens removed; whitespace normalized; table column labels and selected cells linearized. Section IDs added. Editorial scope is separate from historical passage sections.",
      "limitations": "Compiler abstract with explicit unnamed omissions and missing division staffs; no underlying regimental census supplied."
    },
    {
      "id": "reed-1909-union-audit-v1",
      "title": "D. W. Reed: Union returns, detachments and late arrivals, revised 1909",
      "path": "data/raw/shiloh/reed-1909-union-audit-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "87e1da1572aaceb0bb73422f008e411872174de01153d9d80a4659ceabdaee2f",
      "author": "D. W. Reed, Shiloh National Military Park Commission",
      "publication_date": "1909",
      "document_date": null,
      "source_kind": "government_secondary_history",
      "independence_group": "reed-official-records-compilation",
      "edition": "D. W. Reed, The Battle of Shiloh and the Organizations Engaged, 1902 (revised 1909), Shiloh National Military Park Commission, Washington: Government Printing Office, 1909. Printed page + 2 = one-based PDF page.",
      "parent_download_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "parent_sha256": "31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96",
      "rights": "Public-domain nineteenth/early-twentieth-century government publication; selected passages and tables, not a new critical edition.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered pages. Line-wrap hyphens removed; whitespace normalized; table column labels and selected cells linearized. Section IDs added. Editorial scope is separate from historical passage sections.",
      "limitations": "Later compilation explicitly derived from Official Records; overlaps the reports, Force, NPS and Army handbook source families. Contains estimated entries, mixed dates, and an internal Fifteenth Michigan Sunday-presence conflict. Not independent historical adjudication."
    },
    {
      "id": "michigan-ag-1862-fifteenth-v1",
      "title": "Michigan Adjutant General: Fifteenth Infantry arrival and casualties",
      "path": "data/raw/shiloh/michigan-ag-1862-fifteenth-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/annualreportofad00mich/annualreportofad00mich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "c143f241b2d96bc563a01f52f996c86634c5da7643952ee96259468f333fd92b",
      "author": "Michigan Adjutant General's Office",
      "publication_date": "1863",
      "document_date": "1862-12-24",
      "source_kind": "contemporary_government_summary",
      "independence_group": "michigan-adjutant-general",
      "edition": "Annual Report of the Adjutant General of the State of Michigan, for the Year 1862, together with a Supplementary Report, Lansing: John A. Kerr & Co., 1863. Title PDF p.5; report heading PDF p.9; printed p.41 = PDF p.45.",
      "parent_download_url": "https://archive.org/download/annualreportofad00mich/annualreportofad00mich.pdf",
      "parent_sha256": "f25789cebc7cc9af4b9c9c603502f65d1f2165ae6d616fb73db0ccca6eb57fe6",
      "rights": "Public-domain nineteenth/early-twentieth-century government publication; selected passages and tables, not a new critical edition.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered pages. Line-wrap hyphens removed; whitespace normalized; table column labels and selected cells linearized. Section IDs added. Editorial scope is separate from historical passage sections.",
      "limitations": "State report compiled after the battle, published 1863; underlying unit reports and dependence on other casualty accounts untraced. Supports reported arrival and two-day casualties, not Force's Sunday-only casualty allocation."
    },
    {
      "id": "reed-1909-union-p93-facsimile-v1",
      "title": "Reed revised 1909, printed p.93, full-page facsimile",
      "path": "data/raw/shiloh/reed-1909-union-p93-facsimile-v1.png",
      "format": "image",
      "url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "c360e57571cddcc9cde0e69603cb6aad64e82f51adb0b61c7225add59481c339",
      "author": "D. W. Reed, Shiloh National Military Park Commission",
      "publication_date": "1909",
      "source_kind": "government_secondary_history_facsimile",
      "independence_group": "reed-official-records-compilation",
      "parent_download_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "parent_sha256": "31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96",
      "edition": "D. W. Reed, The Battle of Shiloh and the Organizations Engaged, 1902 (revised 1909), Shiloh National Military Park Commission, Washington: Government Printing Office, 1909. Printed page + 2 = one-based PDF page.",
      "locator": "Printed p.93; parent PDF p.95",
      "rights": "Public-domain U.S. government publication, 1909.",
      "snapshot_transform": "Rendered parent PDF page with pypdfium2 at scale 2.2 and rotation 90 for reading; PNG. No historical cells edited.",
      "limitations": "Facsimile of the same source as reed-1909-union-audit-v1, not independent testimony."
    },
    {
      "id": "reed-1909-union-p96-facsimile-v1",
      "title": "Reed revised 1909, printed p.96, full-page facsimile",
      "path": "data/raw/shiloh/reed-1909-union-p96-facsimile-v1.png",
      "format": "image",
      "url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "f44f67c179a4dbb328cbb6d446bae9a28d1ed29fd8f314672a4d08184db20bb1",
      "author": "D. W. Reed, Shiloh National Military Park Commission",
      "publication_date": "1909",
      "source_kind": "government_secondary_history_facsimile",
      "independence_group": "reed-official-records-compilation",
      "parent_download_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "parent_sha256": "31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96",
      "edition": "D. W. Reed, The Battle of Shiloh and the Organizations Engaged, 1902 (revised 1909), Shiloh National Military Park Commission, Washington: Government Printing Office, 1909. Printed page + 2 = one-based PDF page.",
      "locator": "Printed p.96; parent PDF p.98",
      "rights": "Public-domain U.S. government publication, 1909.",
      "snapshot_transform": "Rendered parent PDF page with pypdfium2 at scale 2.2 and rotation 90 for reading; PNG. No historical cells edited.",
      "limitations": "Facsimile of the same source as reed-1909-union-audit-v1, not independent testimony."
    },
    {
      "id": "reed-1909-union-p97-facsimile-v1",
      "title": "Reed revised 1909, printed p.97, full-page facsimile",
      "path": "data/raw/shiloh/reed-1909-union-p97-facsimile-v1.png",
      "format": "image",
      "url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "5a355ac9c6cc6542e4191448f40904d7394a621d8bc855d7aa381caee9385843",
      "author": "D. W. Reed, Shiloh National Military Park Commission",
      "publication_date": "1909",
      "source_kind": "government_secondary_history_facsimile",
      "independence_group": "reed-official-records-compilation",
      "parent_download_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "parent_sha256": "31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96",
      "edition": "D. W. Reed, The Battle of Shiloh and the Organizations Engaged, 1902 (revised 1909), Shiloh National Military Park Commission, Washington: Government Printing Office, 1909. Printed page + 2 = one-based PDF page.",
      "locator": "Printed p.97; parent PDF p.99",
      "rights": "Public-domain U.S. government publication, 1909.",
      "snapshot_transform": "Rendered parent PDF page with pypdfium2 at scale 2.2 and rotation 90 for reading; PNG. No historical cells edited.",
      "limitations": "Facsimile of the same source as reed-1909-union-audit-v1, not independent testimony."
    },
    {
      "id": "reed-1909-union-p98-facsimile-v1",
      "title": "Reed revised 1909, printed p.98, full-page facsimile",
      "path": "data/raw/shiloh/reed-1909-union-p98-facsimile-v1.png",
      "format": "image",
      "url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "f9346df6200f246a7ce80f3ca651a0fecce89775b01cd7d91f5aa50b2229f790",
      "author": "D. W. Reed, Shiloh National Military Park Commission",
      "publication_date": "1909",
      "source_kind": "government_secondary_history_facsimile",
      "independence_group": "reed-official-records-compilation",
      "parent_download_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "parent_sha256": "31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96",
      "edition": "D. W. Reed, The Battle of Shiloh and the Organizations Engaged, 1902 (revised 1909), Shiloh National Military Park Commission, Washington: Government Printing Office, 1909. Printed page + 2 = one-based PDF page.",
      "locator": "Printed p.98; parent PDF p.100",
      "rights": "Public-domain U.S. government publication, 1909.",
      "snapshot_transform": "Rendered parent PDF page with pypdfium2 at scale 2.2 and rotation 90 for reading; PNG. No historical cells edited.",
      "limitations": "Facsimile of the same source as reed-1909-union-audit-v1, not independent testimony."
    },
    {
      "id": "or-nelson-reinforcements-v1",
      "title": "William Nelson: crossing, deployment and strength, report 103",
      "path": "data/raw/shiloh/or-nelson-reinforcements-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "e75987c53540b8ad09b7cf108204b7f7f9e6343b09da01570e862dba309986ed",
      "author": "William Nelson; Official Records compilers",
      "document_date": "1862-04-10",
      "publication_date": "1884",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "source_kind": "contemporary_participant_report_and_compiler_material",
      "independence_group": "or-nelson",
      "rights": "Public-domain government publication; nineteenth-century reports or 1909 history.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered PDF pages. Whitespace normalized and line-wrap hyphens removed; selected table columns linearized with labels. Editorial scope is separate from historical passages.",
      "limitations": "Source-qualified observations, not historical adjudication. Reports share an army reporting environment; Reed explicitly compiles from those records. Document dates do not establish event times or knowledge available before battle."
    },
    {
      "id": "or-ammen-crossing-v1",
      "title": "Jacob Ammen: April 10 report and separately printed diary extracts",
      "path": "data/raw/shiloh/or-ammen-crossing-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "df186eb4f91fdb6dbc87cbf8e86e526f6d3f18c8dcc9730a858e7d3dc4ef9b93",
      "author": "Jacob Ammen",
      "document_date": "1862-04-10",
      "publication_date": "1884",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "source_kind": "contemporary_participant_report_and_compiler_material",
      "independence_group": "or-nelson",
      "rights": "Public-domain government publication; nineteenth-century reports or 1909 history.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered PDF pages. Whitespace normalized and line-wrap hyphens removed; selected table columns linearized with labels. Editorial scope is separate from historical passages.",
      "limitations": "Source-qualified observations, not historical adjudication. Reports share an army reporting environment; Reed explicitly compiles from those records. Document dates do not establish event times or knowledge available before battle."
    },
    {
      "id": "or-grose-crossing-v1",
      "title": "William Grose: Thirty-sixth Indiana Sunday contingent, report 105",
      "path": "data/raw/shiloh/or-grose-crossing-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "45557a169c58c848726a0105e883da9dd682b749c6d603d09d4578209ec09410",
      "author": "William Grose",
      "document_date": "1862-04-08",
      "publication_date": "1884",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "source_kind": "contemporary_participant_report_and_compiler_material",
      "independence_group": "or-nelson",
      "rights": "Public-domain government publication; nineteenth-century reports or 1909 history.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered PDF pages. Whitespace normalized and line-wrap hyphens removed; selected table columns linearized with labels. Editorial scope is separate from historical passages.",
      "limitations": "Source-qualified observations, not historical adjudication. Reports share an army reporting environment; Reed explicitly compiles from those records. Document dates do not establish event times or knowledge available before battle."
    },
    {
      "id": "or-anderson-crossing-v1",
      "title": "Nicholas Anderson: Sixth Ohio landing, report 106",
      "path": "data/raw/shiloh/or-anderson-crossing-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "2b609dc79ebb3d2fcc1d52c97b10271b415d5c7166dfaeb53dcfa3d074f8d725",
      "author": "Nicholas L. Anderson",
      "document_date": "1862-04-09",
      "publication_date": "1884",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "source_kind": "contemporary_participant_report_and_compiler_material",
      "independence_group": "or-nelson",
      "rights": "Public-domain government publication; nineteenth-century reports or 1909 history.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered PDF pages. Whitespace normalized and line-wrap hyphens removed; selected table columns linearized with labels. Editorial scope is separate from historical passages.",
      "limitations": "Source-qualified observations, not historical adjudication. Reports share an army reporting environment; Reed explicitly compiles from those records. Document dates do not establish event times or knowledge available before battle."
    },
    {
      "id": "or-jones-crossing-v1",
      "title": "Frederick Jones: Twenty-fourth Ohio landing, report 107",
      "path": "data/raw/shiloh/or-jones-crossing-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "a64da854998697a6d6d4cd6bfea1850eb26b360d69b5c4f485d75a3624f45edc",
      "author": "Frederick C. Jones",
      "document_date": "1862-04-08",
      "publication_date": "1884",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "source_kind": "contemporary_participant_report_and_compiler_material",
      "independence_group": "or-nelson",
      "rights": "Public-domain government publication; nineteenth-century reports or 1909 history.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered PDF pages. Whitespace normalized and line-wrap hyphens removed; selected table columns linearized with labels. Editorial scope is separate from historical passages.",
      "limitations": "Source-qualified observations, not historical adjudication. Reports share an army reporting environment; Reed explicitly compiles from those records. Document dates do not establish event times or knowledge available before battle."
    },
    {
      "id": "or-edward-mccook-crossing-v1",
      "title": "Edward McCook: Second Indiana Cavalry crossing, report 116",
      "path": "data/raw/shiloh/or-edward-mccook-crossing-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "68d57493f397798415ba132e2e72a4d78013445ca6a6d81c736877f4845a43fa",
      "author": "Edward M. McCook",
      "document_date": "1862-04-10",
      "publication_date": "1884",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "source_kind": "contemporary_participant_report_and_compiler_material",
      "independence_group": "or-nelson",
      "rights": "Public-domain government publication; nineteenth-century reports or 1909 history.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered PDF pages. Whitespace normalized and line-wrap hyphens removed; selected table columns linearized with labels. Editorial scope is separate from historical passages.",
      "limitations": "Source-qualified observations, not historical adjudication. Reports share an army reporting environment; Reed explicitly compiles from those records. Document dates do not establish event times or knowledge available before battle."
    },
    {
      "id": "or-crittenden-reinforcements-v1",
      "title": "Thomas Crittenden: boat arrival and cavalry exclusion, report 117",
      "path": "data/raw/shiloh/or-crittenden-reinforcements-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "235b01590b21cbf161ebe63162db73cf45184bd234f4025deae555040f317391",
      "author": "Thomas L. Crittenden",
      "document_date": "1862-04-15",
      "publication_date": "1884",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "source_kind": "contemporary_participant_report_and_compiler_material",
      "independence_group": "or-buell",
      "rights": "Public-domain government publication; nineteenth-century reports or 1909 history.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered PDF pages. Whitespace normalized and line-wrap hyphens removed; selected table columns linearized with labels. Editorial scope is separate from historical passages.",
      "limitations": "Source-qualified observations, not historical adjudication. Reports share an army reporting environment; Reed explicitly compiles from those records. Document dates do not establish event times or knowledge available before battle."
    },
    {
      "id": "or-alexander-mccook-reinforcements-v1",
      "title": "Alexander McCook: Savannah, landing and staged deployment, report 90",
      "path": "data/raw/shiloh/or-alexander-mccook-reinforcements-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "59ca8b68925fe217897e50272bcc0e2158325389ae5114b4cdfeb275736fe5ea",
      "author": "Alexander McD. McCook",
      "document_date": "1862-04-09",
      "publication_date": "1884",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "source_kind": "contemporary_participant_report_and_compiler_material",
      "independence_group": "or-buell",
      "rights": "Public-domain government publication; nineteenth-century reports or 1909 history.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered PDF pages. Whitespace normalized and line-wrap hyphens removed; selected table columns linearized with labels. Editorial scope is separate from historical passages.",
      "limitations": "Source-qualified observations, not historical adjudication. Reports share an army reporting environment; Reed explicitly compiles from those records. Document dates do not establish event times or knowledge available before battle."
    },
    {
      "id": "or-wood-reinforcements-v1",
      "title": "Thomas Wood: April 7 embarkation and staggered arrival, report 130",
      "path": "data/raw/shiloh/or-wood-reinforcements-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "21570f8903b1535e674efa9d8c478954b69ab7de68c8445d27e2e338641a1357",
      "author": "Thomas J. Wood",
      "document_date": "1862-04-10",
      "publication_date": "1884",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "source_kind": "contemporary_participant_report_and_compiler_material",
      "independence_group": "or-buell",
      "rights": "Public-domain government publication; nineteenth-century reports or 1909 history.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered PDF pages. Whitespace normalized and line-wrap hyphens removed; selected table columns linearized with labels. Editorial scope is separate from historical passages.",
      "limitations": "Source-qualified observations, not historical adjudication. Reports share an army reporting environment; Reed explicitly compiles from those records. Document dates do not establish event times or knowledge available before battle."
    },
    {
      "id": "or-garfield-reinforcements-v1",
      "title": "James Garfield: landing, advance and non-engagement, report 131",
      "path": "data/raw/shiloh/or-garfield-reinforcements-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "950b5b0d8e5a5a34f9b3a7f55efc142091f2373b571955a0f897e8c090981150",
      "author": "James A. Garfield",
      "document_date": "1862-04-09",
      "publication_date": "1884",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "source_kind": "contemporary_participant_report_and_compiler_material",
      "independence_group": "or-buell",
      "rights": "Public-domain government publication; nineteenth-century reports or 1909 history.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered PDF pages. Whitespace normalized and line-wrap hyphens removed; selected table columns linearized with labels. Editorial scope is separate from historical passages.",
      "limitations": "Source-qualified observations, not historical adjudication. Reports share an army reporting environment; Reed explicitly compiles from those records. Document dates do not establish event times or knowledge available before battle."
    },
    {
      "id": "or-buell-reinforcements-v2",
      "title": "Don Carlos Buell: Savannah arrival and artillery transport supplement, report 87",
      "path": "data/raw/shiloh/or-buell-reinforcements-v2.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "57627b0ea1c1e71c61d213fe4c52b692d292a20ae7c45e43677380ade6da4973",
      "author": "Don Carlos Buell",
      "document_date": "1862-04-15",
      "publication_date": "1884",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "source_kind": "contemporary_participant_report_and_compiler_material",
      "independence_group": "or-buell",
      "rights": "Public-domain government publication; nineteenth-century reports or 1909 history.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered PDF pages. Whitespace normalized and line-wrap hyphens removed; selected table columns linearized with labels. Editorial scope is separate from historical passages.",
      "limitations": "Source-qualified observations, not historical adjudication. Reports share an army reporting environment; Reed explicitly compiles from those records. Document dates do not establish event times or knowledge available before battle."
    },
    {
      "id": "reed-1909-ohio-strength-v1",
      "title": "D. W. Reed: Army of the Ohio strength reconstruction and limits",
      "path": "data/raw/shiloh/reed-1909-ohio-strength-v1.txt",
      "format": "text",
      "sectioned": true,
      "url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "9af7a9d42181a4cba1e3f7fffc0d73a3bd26c4b48aced3a9f3241711e939167a",
      "author": "D. W. Reed, Shiloh National Military Park Commission",
      "document_date": null,
      "publication_date": "1909",
      "edition": "D. W. Reed, The Battle of Shiloh and the Organizations Engaged, 1902 (revised 1909), Washington: Government Printing Office, 1909. Printed page + 2 = one-based PDF page.",
      "parent_download_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "parent_sha256": "31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96",
      "source_kind": "government_secondary_history",
      "independence_group": "reed-official-records-compilation",
      "rights": "Public-domain government publication; nineteenth-century reports or 1909 history.",
      "snapshot_transform": "Selected passages manually transcribed from visually inspected rendered PDF pages. Whitespace normalized and line-wrap hyphens removed; selected table columns linearized with labels. Editorial scope is separate from historical passages.",
      "limitations": "Source-qualified observations, not historical adjudication. Reports share an army reporting environment; Reed explicitly compiles from those records. Document dates do not establish event times or knowledge available before battle."
    },
    {
      "id": "or-reinforcement-p326-facsimile-v1",
      "title": "OR printed p.326, reinforcement strength table facsimile",
      "path": "data/raw/shiloh/or-reinforcement-p326-facsimile-v1.png",
      "format": "image",
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "6a16948ba7308e08559143f9e68b45f66ed383779950018109697f1529f7c54f",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "publication_date": "1884",
      "author": "William Nelson; Official Records compilers",
      "source_kind": "government_publication_facsimile",
      "independence_group": "or-nelson",
      "rights": "Public-domain government publication.",
      "locator": "Printed p.326; parent PDF p.350",
      "snapshot_transform": "Full page rendered with pypdfium2 at scale 1.8; no rotation.",
      "limitations": "Same documentary evidence as its transcript, not independent corroboration."
    },
    {
      "id": "or-reinforcement-p327-facsimile-v1",
      "title": "OR printed p.327, reinforcement strength table facsimile",
      "path": "data/raw/shiloh/or-reinforcement-p327-facsimile-v1.png",
      "format": "image",
      "url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "3219c3346da5ad79c292daa33f5f6509c888169b167c181952d5f9d5bb7ddf5a",
      "parent_download_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
      "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
      "edition": "The War of the Rebellion, Series I, Volume X, Part I, Washington: Government Printing Office, 1884. Printed page + 24 = one-based PDF page.",
      "publication_date": "1884",
      "author": "William Nelson; Official Records compilers",
      "source_kind": "government_publication_facsimile",
      "independence_group": "or-nelson",
      "rights": "Public-domain government publication.",
      "locator": "Printed p.327; parent PDF p.351",
      "snapshot_transform": "Full page rendered with pypdfium2 at scale 1.8; no rotation.",
      "limitations": "Same documentary evidence as its transcript, not independent corroboration."
    },
    {
      "id": "reed-reinforcement-p100-facsimile-v1",
      "title": "REED printed p.100, reinforcement strength table facsimile",
      "path": "data/raw/shiloh/reed-reinforcement-p100-facsimile-v1.png",
      "format": "image",
      "url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "c0c4d7dc67e98d427558574f4c7a003d6a40767cc11b2afe8987478b709a92de",
      "parent_download_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "parent_sha256": "31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96",
      "edition": "D. W. Reed, The Battle of Shiloh and the Organizations Engaged, 1902 (revised 1909), Washington: Government Printing Office, 1909. Printed page + 2 = one-based PDF page.",
      "publication_date": "1909",
      "author": "D. W. Reed",
      "source_kind": "government_publication_facsimile",
      "independence_group": "reed-official-records-compilation",
      "rights": "Public-domain government publication.",
      "locator": "Printed p.100; parent PDF p.102",
      "snapshot_transform": "Full page rendered with pypdfium2 at scale 2.2; rotated 90 degrees for reading.",
      "limitations": "Same documentary evidence as its transcript, not independent corroboration."
    },
    {
      "id": "reed-reinforcement-p101-facsimile-v1",
      "title": "REED printed p.101, reinforcement strength table facsimile",
      "path": "data/raw/shiloh/reed-reinforcement-p101-facsimile-v1.png",
      "format": "image",
      "url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "656f866652e3de14f7d61f7ab284eaf1dc05f1fd98f0a9a7e2c8af92375ac5e1",
      "parent_download_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "parent_sha256": "31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96",
      "edition": "D. W. Reed, The Battle of Shiloh and the Organizations Engaged, 1902 (revised 1909), Washington: Government Printing Office, 1909. Printed page + 2 = one-based PDF page.",
      "publication_date": "1909",
      "author": "D. W. Reed",
      "source_kind": "government_publication_facsimile",
      "independence_group": "reed-official-records-compilation",
      "rights": "Public-domain government publication.",
      "locator": "Printed p.101; parent PDF p.103",
      "snapshot_transform": "Full page rendered with pypdfium2 at scale 2.2; rotated 90 degrees for reading.",
      "limitations": "Same documentary evidence as its transcript, not independent corroboration."
    },
    {
      "id": "reed-reinforcement-p102-facsimile-v1",
      "title": "REED printed p.102, reinforcement strength table facsimile",
      "path": "data/raw/shiloh/reed-reinforcement-p102-facsimile-v1.png",
      "format": "image",
      "url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "retrieved_at": "2026-09-20",
      "sha256": "f5a32895999f3ff9b0834a5cd5c9fbf9c3616ad10a87e61325835c8f95212092",
      "parent_download_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
      "parent_sha256": "31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96",
      "edition": "D. W. Reed, The Battle of Shiloh and the Organizations Engaged, 1902 (revised 1909), Washington: Government Printing Office, 1909. Printed page + 2 = one-based PDF page.",
      "publication_date": "1909",
      "author": "D. W. Reed",
      "source_kind": "government_publication_facsimile",
      "independence_group": "reed-official-records-compilation",
      "rights": "Public-domain government publication.",
      "locator": "Printed p.102; parent PDF p.104",
      "snapshot_transform": "Full page rendered with pypdfium2 at scale 2.2; rotated 90 degrees for reading.",
      "limitations": "Same documentary evidence as its transcript, not independent corroboration."
    }
  ]
}
```

## Supplementary image provenance

```json
[
  {
    "id": "review-or-p323",
    "path": "reviews/TN003-a42f063-v1/pages/or-p323.png",
    "sha256": "27e5e98208cba16ac021d54e11b7172bc4e3ae45f8fae8a329b78aa513f743bd",
    "parent_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
    "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
    "printed_page": 323,
    "pdf_page_one_based": 347,
    "parent_metadata_source_id": "or-nelson-reinforcements-v1",
    "transform": "Full PDF page rendered with pypdfium2 at scale 1.6; no cropping or annotation.",
    "role": "Supplementary review copy; not a new independent source or an admitted evidence revision.",
    "snapshot_sections_to_compare": [
      {
        "source_id": "or-nelson-reinforcements-v1",
        "section": "p323-heading"
      },
      {
        "source_id": "or-nelson-reinforcements-v1",
        "section": "p323-crossing"
      },
      {
        "source_id": "or-nelson-reinforcements-v1",
        "section": "pp323-324-action"
      }
    ]
  },
  {
    "id": "review-or-p324",
    "path": "reviews/TN003-a42f063-v1/pages/or-p324.png",
    "sha256": "753e1fb0c41d26f4fb0625fa0a8f4b4d8df4f2988e3bc5fcf0c2823245c685c1",
    "parent_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
    "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
    "printed_page": 324,
    "pdf_page_one_based": 348,
    "parent_metadata_source_id": "or-nelson-reinforcements-v1",
    "transform": "Full PDF page rendered with pypdfium2 at scale 1.6; no cropping or annotation.",
    "role": "Supplementary review copy; not a new independent source or an admitted evidence revision.",
    "snapshot_sections_to_compare": [
      {
        "source_id": "or-nelson-reinforcements-v1",
        "section": "pp323-324-action"
      },
      {
        "source_id": "or-nelson-reinforcements-v1",
        "section": "p324-night"
      },
      {
        "source_id": "or-nelson-reinforcements-v1",
        "section": "p324-morning"
      },
      {
        "source_id": "or-nelson-reinforcements-v1",
        "section": "p324-artillery"
      }
    ]
  },
  {
    "id": "review-or-p328",
    "path": "reviews/TN003-a42f063-v1/pages/or-p328.png",
    "sha256": "13c5f7d87c254102686b669aa3c3d54043c856a099f265e2b86f3634ee12fa3e",
    "parent_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
    "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
    "printed_page": 328,
    "pdf_page_one_based": 352,
    "parent_metadata_source_id": "or-nelson-reinforcements-v1",
    "transform": "Full PDF page rendered with pypdfium2 at scale 1.6; no cropping or annotation.",
    "role": "Supplementary review copy; not a new independent source or an admitted evidence revision.",
    "snapshot_sections_to_compare": [
      {
        "source_id": "or-ammen-crossing-v1",
        "section": "p328-report"
      }
    ]
  },
  {
    "id": "review-or-p329",
    "path": "reviews/TN003-a42f063-v1/pages/or-p329.png",
    "sha256": "034cd7356dac1fd49a1c45babda42ec0adf9f675d0bdf8673451ea006c5803ab",
    "parent_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
    "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
    "printed_page": 329,
    "pdf_page_one_based": 353,
    "parent_metadata_source_id": "or-nelson-reinforcements-v1",
    "transform": "Full PDF page rendered with pypdfium2 at scale 1.6; no cropping or annotation.",
    "role": "Supplementary review copy; not a new independent source or an admitted evidence revision.",
    "snapshot_sections_to_compare": [
      {
        "source_id": "or-ammen-crossing-v1",
        "section": "p329-diary-heading"
      }
    ]
  },
  {
    "id": "review-or-p330",
    "path": "reviews/TN003-a42f063-v1/pages/or-p330.png",
    "sha256": "ebc18e5e242ca58f65c90b82de2b2df0afcdc32311f2c4d8a772439f2cb2791c",
    "parent_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
    "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
    "printed_page": 330,
    "pdf_page_one_based": 354,
    "parent_metadata_source_id": "or-nelson-reinforcements-v1",
    "transform": "Full PDF page rendered with pypdfium2 at scale 1.6; no cropping or annotation.",
    "role": "Supplementary review copy; not a new independent source or an admitted evidence revision.",
    "snapshot_sections_to_compare": [
      {
        "source_id": "or-ammen-crossing-v1",
        "section": "p330-diary"
      }
    ]
  },
  {
    "id": "review-or-p333",
    "path": "reviews/TN003-a42f063-v1/pages/or-p333.png",
    "sha256": "3121fe99b628406d692b2a66ff7d39b27c30b4027ce80a0be7ea34c45fd0d474",
    "parent_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
    "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
    "printed_page": 333,
    "pdf_page_one_based": 357,
    "parent_metadata_source_id": "or-nelson-reinforcements-v1",
    "transform": "Full PDF page rendered with pypdfium2 at scale 1.6; no cropping or annotation.",
    "role": "Supplementary review copy; not a new independent source or an admitted evidence revision.",
    "snapshot_sections_to_compare": [
      {
        "source_id": "or-ammen-crossing-v1",
        "section": "p333-diary"
      }
    ]
  },
  {
    "id": "review-or-p334",
    "path": "reviews/TN003-a42f063-v1/pages/or-p334.png",
    "sha256": "83a0e32b55bb171fc38b9e3d87085d89d53b06f5f9e144f6829c1f7a7070bf14",
    "parent_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
    "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
    "printed_page": 334,
    "pdf_page_one_based": 358,
    "parent_metadata_source_id": "or-nelson-reinforcements-v1",
    "transform": "Full PDF page rendered with pypdfium2 at scale 1.6; no cropping or annotation.",
    "role": "Supplementary review copy; not a new independent source or an admitted evidence revision.",
    "snapshot_sections_to_compare": [
      {
        "source_id": "or-ammen-crossing-v1",
        "section": "p334-diary"
      }
    ]
  },
  {
    "id": "review-or-p337",
    "path": "reviews/TN003-a42f063-v1/pages/or-p337.png",
    "sha256": "8c03bccb04612f26c1db869e8d882efcaae6cef5959eba3b72a3a3239d6b8392",
    "parent_url": "https://archive.org/download/1warofrebellion10secrrich/1warofrebellion10secrrich.pdf",
    "parent_sha256": "86d6a70bf565edc90de15ef15e4037f6ebf9163857ce916c7b6d3386ff337978",
    "printed_page": 337,
    "pdf_page_one_based": 361,
    "parent_metadata_source_id": "or-nelson-reinforcements-v1",
    "transform": "Full PDF page rendered with pypdfium2 at scale 1.6; no cropping or annotation.",
    "role": "Supplementary review copy; not a new independent source or an admitted evidence revision.",
    "snapshot_sections_to_compare": [
      {
        "source_id": "or-grose-crossing-v1",
        "section": "p337-heading"
      },
      {
        "source_id": "or-grose-crossing-v1",
        "section": "p337"
      }
    ]
  },
  {
    "id": "review-reed-p60",
    "path": "reviews/TN003-a42f063-v1/pages/reed-p60.png",
    "sha256": "d0e77982ef2743152e43414ad11d1adf6c96b37d78d0f3a52e43ef1ff6f9ce09",
    "parent_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
    "parent_sha256": "31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96",
    "printed_page": 60,
    "pdf_page_one_based": 62,
    "parent_metadata_source_id": "reed-1909-union-audit-v1",
    "transform": "Full PDF page rendered with pypdfium2 at scale 1.6; no cropping or annotation.",
    "role": "Supplementary review copy; not a new independent source or an admitted evidence revision.",
    "snapshot_sections_to_compare": [
      {
        "source_id": "reed-1909-union-audit-v1",
        "section": "p60-second-brigade"
      },
      {
        "source_id": "reed-1909-union-audit-v1",
        "section": "pp60-61-michigan"
      }
    ]
  },
  {
    "id": "review-reed-p61",
    "path": "reviews/TN003-a42f063-v1/pages/reed-p61.png",
    "sha256": "08b81bdec2e8f47ec07e8f7a16608a2d0e308fcbd94dad0daf181d937ba180d6",
    "parent_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
    "parent_sha256": "31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96",
    "printed_page": 61,
    "pdf_page_one_based": 63,
    "parent_metadata_source_id": "reed-1909-union-audit-v1",
    "transform": "Full PDF page rendered with pypdfium2 at scale 1.6; no cropping or annotation.",
    "role": "Supplementary review copy; not a new independent source or an admitted evidence revision.",
    "snapshot_sections_to_compare": [
      {
        "source_id": "reed-1909-union-audit-v1",
        "section": "pp60-61-michigan"
      },
      {
        "source_id": "reed-1909-union-audit-v1",
        "section": "p61-wisconsin"
      }
    ]
  },
  {
    "id": "review-reed-p111",
    "path": "reviews/TN003-a42f063-v1/pages/reed-p111.png",
    "sha256": "575e5da35bfc7398a1e1d36e64805441d5187beb707ac4206d746066b5738b9d",
    "parent_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
    "parent_sha256": "31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96",
    "printed_page": 111,
    "pdf_page_one_based": 113,
    "parent_metadata_source_id": "reed-1909-union-audit-v1",
    "transform": "Full PDF page rendered with pypdfium2 at scale 1.6; no cropping or annotation.",
    "role": "Supplementary review copy; not a new independent source or an admitted evidence revision.",
    "snapshot_sections_to_compare": [
      {
        "source_id": "reed-1909-union-audit-v1",
        "section": "p111-union-notes"
      },
      {
        "source_id": "reed-1909-ohio-strength-v1",
        "section": "p111-note-j"
      }
    ]
  },
  {
    "id": "review-reed-p112",
    "path": "reviews/TN003-a42f063-v1/pages/reed-p112.png",
    "sha256": "19ee738d07bb6f2d2a6f734def9890919f0937db9b7856364eb188d8f3de681e",
    "parent_url": "https://upload.wikimedia.org/wikipedia/commons/7/7f/The_battle_of_Shiloh_and_the_organizations_engaged_%28IA_battleofshilohor00unit%29.pdf",
    "parent_sha256": "31e0379e56cf87fa4770afddd9c5d0e5f8181d55790e54cb0bbf4bb60362af96",
    "printed_page": 112,
    "pdf_page_one_based": 114,
    "parent_metadata_source_id": "reed-1909-union-audit-v1",
    "transform": "Full PDF page rendered with pypdfium2 at scale 1.6; no cropping or annotation.",
    "role": "Supplementary review copy; not a new independent source or an admitted evidence revision.",
    "snapshot_sections_to_compare": [
      {
        "source_id": "reed-1909-union-audit-v1",
        "section": "p112-note-r"
      }
    ]
  },
  {
    "id": "review-michigan-p41",
    "path": "reviews/TN003-a42f063-v1/pages/michigan-p41.png",
    "sha256": "a85f87b1cc57604458e5572359284e93d973b61dce19cb0486b1d66119105f85",
    "parent_url": "https://archive.org/download/annualreportofad00mich/annualreportofad00mich.pdf",
    "parent_sha256": "f25789cebc7cc9af4b9c9c603502f65d1f2165ae6d616fb73db0ccca6eb57fe6",
    "printed_page": 41,
    "pdf_page_one_based": 45,
    "parent_metadata_source_id": "michigan-ag-1862-fifteenth-v1",
    "transform": "Full PDF page rendered with pypdfium2 at scale 1.6; no cropping or annotation.",
    "role": "Supplementary review copy; not a new independent source or an admitted evidence revision.",
    "snapshot_sections_to_compare": [
      {
        "source_id": "michigan-ag-1862-fifteenth-v1",
        "section": "p41"
      }
    ]
  }
]
```
