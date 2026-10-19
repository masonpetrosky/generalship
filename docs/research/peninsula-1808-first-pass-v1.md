# Peninsula 1808: complete campaign first pass

Date: 2026-10-19. Status: **primary-verified drafts**. Scope: all 17 frozen entries of
`peninsula 1808`, including the second Zaragoza siege that ends in February 1809.
The primary session researched, authored and verified the complete group. No subagent,
separate review, second-opinion prompt, feature admission or model job ran.

## Coverage and stopping

This pass adds **231 claims, 68 explicit unknowns and 189 citations**.
Every dossier covers nine dimensions with evidence or explicit unknowns and carries brief v3's
per-side strength population/time, command scope, army-continuity and stopping checklist.
Coverage is now **85/325 entries in 5/16 complete groups**, leaving **240/325** without drafts.
Next is `peninsula 1809` (19 frozen entries). All 34 side-level army-continuity records in this
pass remain unknown; repeated names or formation labels do not establish an army registry.

Each dossier uses Bodart and two other assigned families. **The research effort exceeded the
three-family ceiling at Valencia, and the incidental Medina reading is also recorded as an
overrun:** Foy's extra Valencia comparison was read alongside Toreno and Napoleon; his Bailén
context also mentioned Medina. The additional Valencia observation and the Medina navigation
locator remain in [`campaign-overruns.json`](../../data/raw/napoleonic-peninsula-1808-v1/campaign-overruns.json).
They are excluded from the three-family dossiers, and no validator exception was added.
The dossier screen therefore does not measure all research effort. Moving an observation to
an appendix does not undo the overrun or make this pass fully ceiling-compliant. Future passes
should fix the family assignment before substantive reading. No separate targeted follow-up
cycle was performed; remaining gaps are deferred.

| Entry | Claims | Unknowns | Citations | Dossier families | Main deferred gap |
| --- | ---: | ---: | ---: | ---: | --- |
| B387b Valencia | 12 | 4 | 10 | 3 | Reconcile the city defenders, outlying divisions and French assaulting subset with Moncey’s report and the Valencia Junta papers. |
| B387c Medina-de-Rio-Seco | 13 | 4 | 10 | 3 | Identify the French battlefield subset and the separate Cuesta/Blake returns; Napoleon’s corps-wide estimate is not an engagement muster. |
| B388a Bailén | 13 | 4 | 11 | 3 | Recover dated returns for Dupont’s fighting column and Reding/Goupigny’s engaged divisions; do not import the later surrender counts. |
| B388b Bailén | 12 | 6 | 7 | 3 | Resolve Dupont’s 8,242/8,248 surrender-count alternative against the capitulation returns, separately from Vedel’s force and the battle. |
| B388c Evora | 13 | 4 | 10 | 3 | Establish the Portuguese and Spanish organized troops separately from armed townspeople through Leite/Moretti returns or Portuguese histories. |
| B389a Saragossa | 15 | 5 | 10 | 3 | Recover dated opening and later garrison/besieger returns and the Lefebvre-to-Verdier command transition, using the siege journals and Palafox papers. |
| B389b Roliça | 13 | 4 | 11 | 3 | Resolve Delaborde’s available fighting force after detachments and the Portuguese contingent’s population basis against original returns. |
| B389c Vimeiro | 13 | 2 | 18 | 3 | Reconcile Foy’s sabres/bayonets and total including noncombatants with dated returns and the late reinforcement exclusions; establish the intraday Burrard handover. |
| B390c Zornoza | 14 | 5 | 9 | 3 | Reconcile Toreno’s smaller Spanish battlefield population and larger French estimate with dated reports of the detached divisions. |
| B390d Gamonal | 13 | 3 | 10 | 3 | Separate nominal army, troops near Burgos and the engaged subset; fix effective Soult/Bessières command timing from orders and reports. |
| B391a Espinosa-de-los-Monteros | 12 | 4 | 9 | 3 | Obtain separate morning returns for the two days and trace the detached/rejoining formations; hunger narratives do not measure readiness. |
| B391b Tudela | 13 | 4 | 12 | 3 | Separate Tudela, Cascante and unengaged Tarazona forces; establish the effective Castaños/Palafox/O’Neil authority and French engaged subset. |
| B391c Somosierra | 15 | 4 | 11 | 3 | Reconcile pass defenders versus detached Sepúlveda troops and the differing French dispatch/bulletin estimates; identify the actual Polish charge command from reports. |
| B392a Rosas | 13 | 4 | 11 | 3 | Separate the besiegers from the covering army and count the Trinidad and naval detachments at matching dates using siege returns. |
| B392b Cardedeu | 14 | 3 | 11 | 3 | Resolve Saint-Cyr’s opponent estimate versus Bodart and establish the troops actually present, excluding Milans and Lazan; inspect the Spanish returns. |
| B392c Molins-del-Rey | 15 | 4 | 11 | 3 | Reconcile the reassembled Spanish army and French five-battalion reinforcement with dated returns, and distinguish Vives’s superior authority from Reding/Caldagués on the field. |
| B393c Saragossa | 18 | 4 | 18 | 3 | Reconcile opening, reinforcement and capitulation populations and date Moncey/Junot/Lannes and Palafox/Ric authority changes using siege journals and returns. |

## Evidence and remaining limits

- **Populations:** Medina separates territorial corps, active force, projected Benavente
  force and the battlefield estimate. Bailén's fighting column is distinct from the later
  surrender populations: Foy gives Dupont 8,242, Toreno 8,248; both give Vedel's group 9,393.
  Évora keeps organized troops separate from armed townspeople and preserves Foy's 5,000
  against Oman's under 3,000. Roliça retains the Portuguese official/British alternatives.
  Vimeiro distinguishes sabres/bayonets from totals including noncombatants. Tudela keeps
  combined armies, local concentrations and Napoleon's claimed engaged subset separate.
  Second Zaragoza separates initial expectations, later garrison, corps strength and ration
  capacity. No losses are mechanically subtracted, no battalion size is guessed and no
  source alternatives are averaged.
- **Authority:** Reding/Goupigny at Bailén differ from Castaños's army title. Palafox's absence,
  Calvo's civil decisions and San Genis's engineering role remain distinct. Burrard's superior
  authority offshore does not erase Wellesley's field control. Soult's prospective command
  order and Henestrosa's claimed effective authority do not produce an exact Gamonal handover.
  Vives's superior role differs from Reding/Caldagués on the Molins field. Second Zaragoza
  retains Moncey, Junot and Lannes, plus Palafox's late delegation to Ric's junta.
- **Disputes and dates:** Saint-Cyr calls 7 December the day after Rosas's capture, implying
  6 December against the frozen 5 December end date. Napoleon says Lannes is before Zaragoza
  on 11 January; Toreno dates his arrival to 22 January. Planned command, reported presence,
  actual arrival and later appointment remain separate possibilities, not a fabricated
  reconciliation. Somosierra's evening letter and later bulletin give different defender
  estimates. The bulletin's Montbrun attribution and causal language remain attributed claims.
- **Sources:** Foy and Saint-Cyr are interested French participant accounts. Toreno is a
  retrospective Spanish participant/political history. Napoleon's notes, letters and bulletins
  share one official imperial family. Oman is a British synthesis: his Évora footnote transmits
  Neves through Arteche, neither separately inspected. Such transmission is not a separately
  inspected Portuguese original, and shared reports are not independent corroboration.
  Dated own-side field returns remain missing for many sides. No claim is validated by reputation.

## Primary verification

All cited passages and numbers were inspected on retained page images. The registry adds
**175 records**: seven complete unmodified OCR parents, seven metadata captures, six scan-data
maps, **74 image/excerpt pairs**, and seven inspected title images. The count includes the
extra Valencia passage retained in the overrun appendix. Toreno I's scan-map download failed;
no substitute map was invented. Toreno II's XML is the unchanged member extracted from the
archive ZIP. Printed pagination, not archive page-label offsets, controls the locators.

Manual excerpts retain original-language spelling with explicitly documented typography and
line-division normalization, mapped document dates and image/parent SHA bindings. English
renderings are marked in claim rationales; Bodart renderings identify the claim-relevant
portion of the longer contextual quote. OCR served navigation, not number extraction.
Existing source entries, raw inputs and all 68 earlier dossiers retain their bytes.

The primary checked every claim for quote context, number population/time, local/superior
command, coded posture/fortification and source dependence. Corrections before pinning included
an inaccurate recap quotation (replaced with the actual Zaragoza camp list), a spelling error,
claims broader than their excerpts, a missing command-return sentence, and an opening-contact
passage that did not justify `both_attacked`. That posture remains unknown. These fixes are
primary verification, not a separate review or an estimated extraction-error rate.

The new dossiers have **12 reproducible digit-screen flags**. Their dispositions are retained
in [`primary-verification-v1.json`](../../data/raw/napoleonic-peninsula-1808-v1/primary-verification-v1.json):
spelled-out French numbers, abbreviated thousands, mapped document dates, a cross-claim Bodart
comparison and the explicit Rosas date implication. There are no new missing quotes or locator
mismatches. The older dossiers' flags remain unchanged. The three-family dossier screen passes;
the two research-effort deviations above remain separately visible.

Validation: source and Napoleonic evidence checks, research screen, `make reproduce` and
`make check`; the regenerated compact campaign packet and reports were inspected. Frozen
frame/cohort, calibration sample/key and historical/synthetic model results remain unchanged.
The 68 unknowns, missing own-side returns, army identities and unset replacement boundaries
are limits to this first pass. Coverage and verification admit no features.

Usage: **unavailable**. The tools expose no trustworthy complete token meter; no value is
reported as zero or extrapolated from earlier rates. No workflow-efficiency claim is made.
