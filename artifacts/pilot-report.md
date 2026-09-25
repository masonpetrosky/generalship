# Pilot baseline and evidence coverage

**Exploratory pipeline result. No validated general rankings or causal effects.**

The frozen frame contains 127 engagements in 36 campaign groups.
Only 23/127 (18.1%) meet the numerical-strength, decisive-outcome, and grain rules.
All imported historical rows remain unreviewed. A checksum confirms the input bytes, not historical truth.

## Coverage

Exclusion reasons overlap; counts must not be added.

| Reason | Engagements | Share of frame |
|---|---:|---:|
| aggregate_operation | 1 | 0.8% |
| inconclusive_outcome | 35 | 27.6% |
| missing_numeric_strength | 102 | 80.3% |

| Theater | Frame | Eligible |
|---|---:|---:|
| Eastern | 69 | 14 |
| Western | 58 | 9 |

## Campaign-held-out baseline

Each of the 13 eligible campaign groups is held out in full while fitting on the other groups.
Every battle appears once in evaluation. Union win is the positive class; inconclusive cases are excluded, not encoded as half-wins.
Lower Brier score and log loss are better. All baselines use the same eligible rows.

| Model | Battle-weighted Brier | Battle-weighted log loss | Campaign-weighted Brier |
|---|---:|---:|---:|
| strength_logistic | 0.276882 | 0.749509 | 0.276527 |
| equal_odds | 0.250000 | 0.693147 | 0.250000 |
| training_prior | 0.281273 | 0.756087 | 0.274624 |

These are diagnostics on a small, selected subset. They do not establish better generalship measurement.
The source's campaign boundaries may leave dependence between related operations; commanders also recur across folds.
Strength sensitivity varies the held-out range endpoints with a fixed fitted model. It excludes training-data and model uncertainty.

## Draft evidence dossiers

Exact passage checks verify provenance only. These drafts do not modify model inputs. Shiloh's four source-review corrections and the focused validator follow-up are accepted; historical disputes remain open.

| Battle | Claims | Explicit unknowns | Quantities | Events | Status |
|---|---:|---:|---:|---:|---|
| [AL001](../data/evidence/AL001.json) | 9 | 1 | 0 | 0 | draft |
| [AL002](../data/evidence/AL002.json) | 9 | 1 | 0 | 0 | draft |
| [AL003](../data/evidence/AL003.json) | 9 | 1 | 0 | 0 | draft |
| [AL004](../data/evidence/AL004.json) | 9 | 1 | 0 | 0 | draft |
| [AL005](../data/evidence/AL005.json) | 9 | 1 | 0 | 0 | draft |
| [AL006](../data/evidence/AL006.json) | 9 | 1 | 0 | 0 | draft |
| [AL007](../data/evidence/AL007.json) | 9 | 1 | 0 | 0 | draft |
| [AR001](../data/evidence/AR001.json) | 9 | 1 | 0 | 0 | draft |
| [AR002](../data/evidence/AR002.json) | 10 | 1 | 0 | 0 | draft |
| [AR003](../data/evidence/AR003.json) | 9 | 1 | 0 | 0 | draft |
| [AR004](../data/evidence/AR004.json) | 9 | 1 | 0 | 0 | draft |
| [AR005](../data/evidence/AR005.json) | 9 | 1 | 0 | 0 | draft |
| [AR006](../data/evidence/AR006.json) | 10 | 1 | 0 | 0 | draft |
| [AR007](../data/evidence/AR007.json) | 9 | 1 | 0 | 0 | draft |
| [AR008](../data/evidence/AR008.json) | 9 | 1 | 0 | 0 | draft |
| [AR009](../data/evidence/AR009.json) | 9 | 1 | 0 | 0 | draft |
| [AR010](../data/evidence/AR010.json) | 9 | 1 | 0 | 0 | draft |
| [AR011](../data/evidence/AR011.json) | 9 | 1 | 0 | 0 | draft |
| [AR012](../data/evidence/AR012.json) | 9 | 1 | 0 | 0 | draft |
| [AR013](../data/evidence/AR013.json) | 9 | 1 | 0 | 0 | draft |
| [AR014](../data/evidence/AR014.json) | 9 | 1 | 0 | 0 | draft |
| [AR015](../data/evidence/AR015.json) | 9 | 1 | 0 | 0 | draft |
| [AR016](../data/evidence/AR016.json) | 9 | 1 | 0 | 0 | draft |
| [AR017](../data/evidence/AR017.json) | 9 | 1 | 0 | 0 | draft |
| [CO001](../data/evidence/CO001.json) | 9 | 1 | 0 | 0 | draft |
| [DC001](../data/evidence/DC001.json) | 9 | 1 | 0 | 0 | draft |
| [FL001](../data/evidence/FL001.json) | 9 | 1 | 0 | 0 | draft |
| [FL002](../data/evidence/FL002.json) | 9 | 1 | 0 | 0 | draft |
| [FL003](../data/evidence/FL003.json) | 9 | 1 | 0 | 0 | draft |
| [FL004](../data/evidence/FL004.json) | 9 | 1 | 0 | 0 | draft |
| [FL005](../data/evidence/FL005.json) | 9 | 1 | 0 | 0 | draft |
| [FL006](../data/evidence/FL006.json) | 9 | 1 | 0 | 0 | draft |
| [GA001](../data/evidence/GA001.json) | 9 | 1 | 0 | 0 | draft |
| [GA002](../data/evidence/GA002.json) | 9 | 1 | 0 | 0 | draft |
| [GA003](../data/evidence/GA003.json) | 9 | 1 | 0 | 0 | draft |
| [GA004](../data/evidence/GA004.json) | 9 | 1 | 0 | 0 | draft |
| [GA005](../data/evidence/GA005.json) | 9 | 1 | 0 | 0 | draft |
| [GA006](../data/evidence/GA006.json) | 9 | 1 | 0 | 0 | draft |
| [GA007](../data/evidence/GA007.json) | 9 | 1 | 0 | 0 | draft |
| [GA008](../data/evidence/GA008.json) | 9 | 1 | 0 | 0 | draft |
| [GA009](../data/evidence/GA009.json) | 9 | 1 | 0 | 0 | draft |
| [GA010](../data/evidence/GA010.json) | 9 | 1 | 0 | 0 | draft |
| [GA011](../data/evidence/GA011.json) | 9 | 1 | 0 | 0 | draft |
| [GA012](../data/evidence/GA012.json) | 9 | 1 | 0 | 0 | draft |
| [GA013](../data/evidence/GA013.json) | 9 | 1 | 0 | 0 | draft |
| [GA014](../data/evidence/GA014.json) | 9 | 2 | 0 | 0 | draft |
| [GA015](../data/evidence/GA015.json) | 9 | 1 | 0 | 0 | draft |
| [GA016](../data/evidence/GA016.json) | 9 | 2 | 0 | 0 | draft |
| [GA017](../data/evidence/GA017.json) | 9 | 1 | 0 | 0 | draft |
| [GA018](../data/evidence/GA018.json) | 9 | 1 | 0 | 0 | draft |
| [GA019](../data/evidence/GA019.json) | 9 | 2 | 0 | 0 | draft |
| [GA020](../data/evidence/GA020.json) | 9 | 1 | 0 | 0 | draft |
| [GA021](../data/evidence/GA021.json) | 9 | 1 | 0 | 0 | draft |
| [GA022](../data/evidence/GA022.json) | 9 | 1 | 0 | 0 | draft |
| [GA023](../data/evidence/GA023.json) | 9 | 1 | 0 | 0 | draft |
| [GA025](../data/evidence/GA025.json) | 9 | 1 | 0 | 0 | draft |
| [GA026](../data/evidence/GA026.json) | 9 | 1 | 0 | 0 | draft |
| [GA027](../data/evidence/GA027.json) | 9 | 1 | 0 | 0 | draft |
| [GA028](../data/evidence/GA028.json) | 9 | 1 | 0 | 0 | draft |
| [ID001](../data/evidence/ID001.json) | 9 | 1 | 0 | 0 | draft |
| [IN001](../data/evidence/IN001.json) | 9 | 1 | 0 | 0 | draft |
| [KS001](../data/evidence/KS001.json) | 9 | 1 | 0 | 0 | draft |
| [KS002](../data/evidence/KS002.json) | 9 | 1 | 0 | 0 | draft |
| [KS003](../data/evidence/KS003.json) | 9 | 1 | 0 | 0 | draft |
| [KS004](../data/evidence/KS004.json) | 9 | 1 | 0 | 0 | draft |
| [KY001](../data/evidence/KY001.json) | 9 | 2 | 0 | 0 | draft |
| [KY002](../data/evidence/KY002.json) | 9 | 1 | 0 | 0 | draft |
| [KY003](../data/evidence/KY003.json) | 9 | 1 | 0 | 0 | draft |
| [KY004](../data/evidence/KY004.json) | 9 | 1 | 0 | 0 | draft |
| [KY005](../data/evidence/KY005.json) | 11 | 1 | 0 | 0 | draft |
| [KY006](../data/evidence/KY006.json) | 11 | 2 | 0 | 0 | draft |
| [KY007](../data/evidence/KY007.json) | 11 | 2 | 0 | 0 | draft |
| [KY008](../data/evidence/KY008.json) | 10 | 1 | 0 | 0 | draft |
| [KY009](../data/evidence/KY009.json) | 11 | 1 | 0 | 0 | draft |
| [KY010](../data/evidence/KY010.json) | 9 | 1 | 0 | 0 | draft |
| [KY011](../data/evidence/KY011.json) | 9 | 1 | 0 | 0 | draft |
| [LA001](../data/evidence/LA001.json) | 9 | 1 | 0 | 0 | draft |
| [LA002](../data/evidence/LA002.json) | 9 | 1 | 0 | 0 | draft |
| [LA003](../data/evidence/LA003.json) | 9 | 1 | 0 | 0 | draft |
| [LA004](../data/evidence/LA004.json) | 9 | 1 | 0 | 0 | draft |
| [LA005](../data/evidence/LA005.json) | 9 | 1 | 0 | 0 | draft |
| [LA006](../data/evidence/LA006.json) | 9 | 1 | 0 | 0 | draft |
| [LA007](../data/evidence/LA007.json) | 9 | 1 | 0 | 0 | draft |
| [LA008](../data/evidence/LA008.json) | 9 | 1 | 0 | 0 | draft |
| [LA009](../data/evidence/LA009.json) | 9 | 1 | 0 | 0 | draft |
| [LA010](../data/evidence/LA010.json) | 9 | 1 | 0 | 0 | draft |
| [LA011](../data/evidence/LA011.json) | 9 | 1 | 0 | 0 | draft |
| [LA012](../data/evidence/LA012.json) | 9 | 1 | 0 | 0 | draft |
| [LA013](../data/evidence/LA013.json) | 9 | 1 | 0 | 0 | draft |
| [LA014](../data/evidence/LA014.json) | 10 | 1 | 0 | 0 | draft |
| [LA015](../data/evidence/LA015.json) | 9 | 1 | 0 | 0 | draft |
| [LA016](../data/evidence/LA016.json) | 9 | 1 | 0 | 0 | draft |
| [LA017](../data/evidence/LA017.json) | 9 | 1 | 0 | 0 | draft |
| [LA018](../data/evidence/LA018.json) | 9 | 1 | 0 | 0 | draft |
| [LA019](../data/evidence/LA019.json) | 9 | 1 | 0 | 0 | draft |
| [LA020](../data/evidence/LA020.json) | 9 | 1 | 0 | 0 | draft |
| [LA021](../data/evidence/LA021.json) | 9 | 1 | 0 | 0 | draft |
| [LA022](../data/evidence/LA022.json) | 9 | 1 | 0 | 0 | draft |
| [LA023](../data/evidence/LA023.json) | 9 | 1 | 0 | 0 | draft |
| [MD001](../data/evidence/MD001.json) | 11 | 2 | 0 | 0 | draft |
| [MD002](../data/evidence/MD002.json) | 10 | 1 | 0 | 0 | draft |
| [MD003](../data/evidence/MD003.json) | 9 | 5 | 0 | 0 | draft |
| [MD004](../data/evidence/MD004.json) | 9 | 1 | 0 | 0 | draft |
| [MD006](../data/evidence/MD006.json) | 9 | 1 | 0 | 0 | draft |
| [MD007](../data/evidence/MD007.json) | 9 | 1 | 0 | 0 | draft |
| [MD008](../data/evidence/MD008.json) | 9 | 1 | 0 | 0 | draft |
| [MN001](../data/evidence/MN001.json) | 9 | 1 | 0 | 0 | draft |
| [MN002](../data/evidence/MN002.json) | 9 | 1 | 0 | 0 | draft |
| [MO001](../data/evidence/MO001.json) | 9 | 1 | 0 | 0 | draft |
| [MO002](../data/evidence/MO002.json) | 9 | 1 | 0 | 0 | draft |
| [MO003](../data/evidence/MO003.json) | 9 | 1 | 0 | 0 | draft |
| [MO004](../data/evidence/MO004.json) | 9 | 1 | 0 | 0 | draft |
| [MO005](../data/evidence/MO005.json) | 9 | 1 | 0 | 0 | draft |
| [MO006](../data/evidence/MO006.json) | 9 | 1 | 0 | 0 | draft |
| [MO007](../data/evidence/MO007.json) | 9 | 1 | 0 | 0 | draft |
| [MO008](../data/evidence/MO008.json) | 9 | 1 | 0 | 0 | draft |
| [MO009](../data/evidence/MO009.json) | 9 | 1 | 0 | 0 | draft |
| [MO010](../data/evidence/MO010.json) | 9 | 1 | 0 | 0 | draft |
| [MO011](../data/evidence/MO011.json) | 9 | 1 | 0 | 0 | draft |
| [MO012](../data/evidence/MO012.json) | 11 | 3 | 0 | 0 | draft |
| [MO013](../data/evidence/MO013.json) | 9 | 1 | 0 | 0 | draft |
| [MO014](../data/evidence/MO014.json) | 9 | 1 | 0 | 0 | draft |
| [MO015](../data/evidence/MO015.json) | 9 | 1 | 0 | 0 | draft |
| [MO016](../data/evidence/MO016.json) | 9 | 1 | 0 | 0 | draft |
| [MO017](../data/evidence/MO017.json) | 9 | 1 | 0 | 0 | draft |
| [MO018](../data/evidence/MO018.json) | 9 | 1 | 0 | 0 | draft |
| [MO019](../data/evidence/MO019.json) | 9 | 1 | 0 | 0 | draft |
| [MO020](../data/evidence/MO020.json) | 9 | 1 | 0 | 0 | draft |
| [MO021](../data/evidence/MO021.json) | 9 | 1 | 0 | 0 | draft |
| [MO022](../data/evidence/MO022.json) | 9 | 1 | 0 | 0 | draft |
| [MO023](../data/evidence/MO023.json) | 9 | 1 | 0 | 0 | draft |
| [MO024](../data/evidence/MO024.json) | 9 | 1 | 0 | 0 | draft |
| [MO025](../data/evidence/MO025.json) | 9 | 1 | 0 | 0 | draft |
| [MO026](../data/evidence/MO026.json) | 9 | 1 | 0 | 0 | draft |
| [MO027](../data/evidence/MO027.json) | 9 | 1 | 0 | 0 | draft |
| [MO028](../data/evidence/MO028.json) | 9 | 1 | 0 | 0 | draft |
| [MO029](../data/evidence/MO029.json) | 9 | 1 | 0 | 0 | draft |
| [MS001](../data/evidence/MS001.json) | 9 | 1 | 0 | 0 | draft |
| [MS002](../data/evidence/MS002.json) | 10 | 1 | 0 | 0 | draft |
| [MS003](../data/evidence/MS003.json) | 9 | 1 | 0 | 0 | draft |
| [MS004](../data/evidence/MS004.json) | 9 | 1 | 0 | 0 | draft |
| [MS005](../data/evidence/MS005.json) | 9 | 1 | 0 | 0 | draft |
| [MS006](../data/evidence/MS006.json) | 9 | 1 | 0 | 0 | draft |
| [MS007](../data/evidence/MS007.json) | 9 | 1 | 0 | 0 | draft |
| [MS008](../data/evidence/MS008.json) | 9 | 1 | 0 | 0 | draft |
| [MS009](../data/evidence/MS009.json) | 7 | 3 | 0 | 0 | draft |
| [MS010](../data/evidence/MS010.json) | 9 | 1 | 0 | 0 | draft |
| [MS011](../data/evidence/MS011.json) | 10 | 1 | 0 | 0 | draft |
| [MS012](../data/evidence/MS012.json) | 9 | 1 | 0 | 0 | draft |
| [MS013](../data/evidence/MS013.json) | 9 | 1 | 0 | 0 | draft |
| [MS014](../data/evidence/MS014.json) | 9 | 1 | 0 | 0 | draft |
| [MS015](../data/evidence/MS015.json) | 9 | 1 | 0 | 0 | draft |
| [MS016](../data/evidence/MS016.json) | 12 | 2 | 0 | 0 | draft |
| [NC001](../data/evidence/NC001.json) | 9 | 1 | 0 | 0 | draft |
| [NC002](../data/evidence/NC002.json) | 9 | 1 | 0 | 0 | draft |
| [NC003](../data/evidence/NC003.json) | 9 | 2 | 0 | 0 | draft |
| [NC004](../data/evidence/NC004.json) | 10 | 2 | 0 | 0 | draft |
| [NC005](../data/evidence/NC005.json) | 10 | 2 | 0 | 0 | draft |
| [NC006](../data/evidence/NC006.json) | 9 | 3 | 0 | 0 | draft |
| [NC007](../data/evidence/NC007.json) | 9 | 1 | 0 | 0 | draft |
| [NC008](../data/evidence/NC008.json) | 9 | 2 | 0 | 0 | draft |
| [NC009](../data/evidence/NC009.json) | 10 | 1 | 0 | 0 | draft |
| [NC010](../data/evidence/NC010.json) | 9 | 1 | 0 | 0 | draft |
| [NC011](../data/evidence/NC011.json) | 9 | 1 | 0 | 0 | draft |
| [NC012](../data/evidence/NC012.json) | 9 | 1 | 0 | 0 | draft |
| [NC013](../data/evidence/NC013.json) | 9 | 1 | 0 | 0 | draft |
| [NC014](../data/evidence/NC014.json) | 9 | 1 | 0 | 0 | draft |
| [NC015](../data/evidence/NC015.json) | 9 | 1 | 0 | 0 | draft |
| [NC016](../data/evidence/NC016.json) | 9 | 1 | 0 | 0 | draft |
| [NC017](../data/evidence/NC017.json) | 9 | 1 | 0 | 0 | draft |
| [NC018](../data/evidence/NC018.json) | 9 | 1 | 0 | 0 | draft |
| [NC019](../data/evidence/NC019.json) | 9 | 1 | 0 | 0 | draft |
| [NC020](../data/evidence/NC020.json) | 9 | 1 | 0 | 0 | draft |
| [ND001](../data/evidence/ND001.json) | 9 | 1 | 0 | 0 | draft |
| [ND002](../data/evidence/ND002.json) | 9 | 1 | 0 | 0 | draft |
| [ND003](../data/evidence/ND003.json) | 9 | 1 | 0 | 0 | draft |
| [ND004](../data/evidence/ND004.json) | 9 | 1 | 0 | 0 | draft |
| [ND005](../data/evidence/ND005.json) | 9 | 1 | 0 | 0 | draft |
| [NM001](../data/evidence/NM001.json) | 9 | 1 | 0 | 0 | draft |
| [NM002](../data/evidence/NM002.json) | 9 | 1 | 0 | 0 | draft |
| [OH001](../data/evidence/OH001.json) | 9 | 1 | 0 | 0 | draft |
| [OH002](../data/evidence/OH002.json) | 10 | 1 | 0 | 0 | draft |
| [OK001](../data/evidence/OK001.json) | 9 | 1 | 0 | 0 | draft |
| [OK002](../data/evidence/OK002.json) | 9 | 1 | 0 | 0 | draft |
| [OK003](../data/evidence/OK003.json) | 9 | 1 | 0 | 0 | draft |
| [OK004](../data/evidence/OK004.json) | 9 | 1 | 0 | 0 | draft |
| [OK005](../data/evidence/OK005.json) | 9 | 2 | 0 | 0 | draft |
| [OK006](../data/evidence/OK006.json) | 9 | 1 | 0 | 0 | draft |
| [OK007](../data/evidence/OK007.json) | 9 | 1 | 0 | 0 | draft |
| [PA001](../data/evidence/PA001.json) | 9 | 1 | 0 | 0 | draft |
| [PA002](../data/evidence/PA002.json) | 9 | 1 | 0 | 0 | draft |
| [SC001](../data/evidence/SC001.json) | 9 | 1 | 0 | 0 | draft |
| [SC002](../data/evidence/SC002.json) | 9 | 1 | 0 | 0 | draft |
| [SC003](../data/evidence/SC003.json) | 9 | 1 | 0 | 0 | draft |
| [SC004](../data/evidence/SC004.json) | 9 | 1 | 0 | 0 | draft |
| [SC005](../data/evidence/SC005.json) | 9 | 1 | 0 | 0 | draft |
| [SC006](../data/evidence/SC006.json) | 9 | 2 | 0 | 0 | draft |
| [SC007](../data/evidence/SC007.json) | 9 | 1 | 0 | 0 | draft |
| [SC008](../data/evidence/SC008.json) | 9 | 1 | 0 | 0 | draft |
| [SC009](../data/evidence/SC009.json) | 9 | 1 | 0 | 0 | draft |
| [SC010](../data/evidence/SC010.json) | 9 | 1 | 0 | 0 | draft |
| [SC011](../data/evidence/SC011.json) | 9 | 1 | 0 | 0 | draft |
| [TN001](../data/evidence/TN001.json) | 10 | 1 | 0 | 0 | draft |
| [TN002](../data/evidence/TN002.json) | 11 | 1 | 0 | 0 | draft |
| [TN003](../data/evidence/TN003.json) | 62 | 3 | 40 | 26 | draft |
| [TN004](../data/evidence/TN004.json) | 10 | 2 | 0 | 0 | draft |
| [TN005](../data/evidence/TN005.json) | 10 | 1 | 0 | 0 | draft |
| [TN006](../data/evidence/TN006.json) | 12 | 1 | 0 | 0 | draft |
| [TN007](../data/evidence/TN007.json) | 9 | 1 | 0 | 0 | draft |
| [TN008](../data/evidence/TN008.json) | 10 | 1 | 0 | 0 | draft |
| [TN009](../data/evidence/TN009.json) | 9 | 1 | 0 | 0 | draft |
| [TN010](../data/evidence/TN010.json) | 10 | 1 | 0 | 0 | draft |
| [TN011](../data/evidence/TN011.json) | 9 | 1 | 0 | 0 | draft |
| [TN012](../data/evidence/TN012.json) | 10 | 1 | 0 | 0 | draft |
| [TN013](../data/evidence/TN013.json) | 9 | 1 | 0 | 0 | draft |
| [TN014](../data/evidence/TN014.json) | 9 | 2 | 0 | 0 | draft |
| [TN015](../data/evidence/TN015.json) | 9 | 1 | 0 | 0 | draft |
| [TN016](../data/evidence/TN016.json) | 9 | 2 | 0 | 0 | draft |
| [TN017](../data/evidence/TN017.json) | 9 | 1 | 0 | 0 | draft |
| [TN018](../data/evidence/TN018.json) | 9 | 1 | 0 | 0 | draft |
| [TN019](../data/evidence/TN019.json) | 10 | 1 | 0 | 0 | draft |
| [TN020](../data/evidence/TN020.json) | 9 | 1 | 0 | 0 | draft |
| [TN021](../data/evidence/TN021.json) | 9 | 1 | 0 | 0 | draft |
| [TN022](../data/evidence/TN022.json) | 9 | 1 | 0 | 0 | draft |
| [TN023](../data/evidence/TN023.json) | 9 | 1 | 0 | 0 | draft |
| [TN024](../data/evidence/TN024.json) | 9 | 1 | 0 | 0 | draft |
| [TN025](../data/evidence/TN025.json) | 9 | 1 | 0 | 0 | draft |
| [TN026](../data/evidence/TN026.json) | 9 | 1 | 0 | 0 | draft |
| [TN027](../data/evidence/TN027.json) | 9 | 1 | 0 | 0 | draft |
| [TN028](../data/evidence/TN028.json) | 9 | 1 | 0 | 0 | draft |
| [TN029](../data/evidence/TN029.json) | 9 | 1 | 0 | 0 | draft |
| [TN030](../data/evidence/TN030.json) | 10 | 1 | 0 | 0 | draft |
| [TN031](../data/evidence/TN031.json) | 9 | 1 | 0 | 0 | draft |
| [TN032](../data/evidence/TN032.json) | 10 | 1 | 0 | 0 | draft |
| [TN033](../data/evidence/TN033.json) | 9 | 1 | 0 | 0 | draft |
| [TN034](../data/evidence/TN034.json) | 10 | 1 | 0 | 0 | draft |
| [TN035](../data/evidence/TN035.json) | 9 | 1 | 0 | 0 | draft |
| [TN036](../data/evidence/TN036.json) | 10 | 1 | 0 | 0 | draft |
| [TN037](../data/evidence/TN037.json) | 9 | 1 | 0 | 0 | draft |
| [TN038](../data/evidence/TN038.json) | 10 | 1 | 0 | 0 | draft |
| [TX001](../data/evidence/TX001.json) | 9 | 1 | 0 | 0 | draft |
| [TX002](../data/evidence/TX002.json) | 9 | 1 | 0 | 0 | draft |
| [TX003](../data/evidence/TX003.json) | 10 | 1 | 0 | 0 | draft |
| [TX005](../data/evidence/TX005.json) | 9 | 1 | 0 | 0 | draft |
| [TX006](../data/evidence/TX006.json) | 9 | 1 | 0 | 0 | draft |
| [VA001](../data/evidence/VA001.json) | 9 | 1 | 0 | 0 | draft |
| [VA002](../data/evidence/VA002.json) | 9 | 1 | 0 | 0 | draft |
| [VA003](../data/evidence/VA003.json) | 9 | 1 | 0 | 0 | draft |
| [VA004](../data/evidence/VA004.json) | 9 | 1 | 0 | 0 | draft |
| [VA005](../data/evidence/VA005.json) | 9 | 1 | 0 | 0 | draft |
| [VA006](../data/evidence/VA006.json) | 9 | 1 | 0 | 0 | draft |
| [VA007](../data/evidence/VA007.json) | 9 | 1 | 0 | 0 | draft |
| [VA008](../data/evidence/VA008.json) | 10 | 5 | 0 | 0 | draft |
| [VA009](../data/evidence/VA009.json) | 9 | 2 | 0 | 0 | draft |
| [VA010](../data/evidence/VA010.json) | 9 | 3 | 0 | 0 | draft |
| [VA011](../data/evidence/VA011.json) | 9 | 2 | 0 | 0 | draft |
| [VA012](../data/evidence/VA012.json) | 10 | 2 | 0 | 0 | draft |
| [VA013](../data/evidence/VA013.json) | 9 | 2 | 0 | 0 | draft |
| [VA014](../data/evidence/VA014.json) | 9 | 2 | 0 | 0 | draft |
| [VA015](../data/evidence/VA015.json) | 10 | 3 | 0 | 0 | draft |
| [VA016](../data/evidence/VA016.json) | 10 | 3 | 0 | 0 | draft |
| [VA017](../data/evidence/VA017.json) | 9 | 2 | 0 | 0 | draft |
| [VA018](../data/evidence/VA018.json) | 9 | 2 | 0 | 0 | draft |
| [VA019](../data/evidence/VA019.json) | 10 | 2 | 0 | 0 | draft |
| [VA020](../data/evidence/VA020.json) | 9 | 2 | 0 | 0 | draft |
| [VA020A](../data/evidence/VA020A.json) | 10 | 2 | 0 | 0 | draft |
| [VA020B](../data/evidence/VA020B.json) | 10 | 2 | 0 | 0 | draft |
| [VA021](../data/evidence/VA021.json) | 10 | 3 | 0 | 0 | draft |
| [VA022](../data/evidence/VA022.json) | 10 | 2 | 0 | 0 | draft |
| [VA023](../data/evidence/VA023.json) | 9 | 1 | 0 | 0 | draft |
| [VA024](../data/evidence/VA024.json) | 9 | 1 | 0 | 0 | draft |
| [VA025](../data/evidence/VA025.json) | 9 | 1 | 0 | 0 | draft |
| [VA026](../data/evidence/VA026.json) | 10 | 1 | 0 | 0 | draft |
| [VA027](../data/evidence/VA027.json) | 9 | 1 | 0 | 0 | draft |
| [VA028](../data/evidence/VA028.json) | 10 | 1 | 0 | 0 | draft |
| [VA029](../data/evidence/VA029.json) | 9 | 1 | 0 | 0 | draft |
| [VA030](../data/evidence/VA030.json) | 9 | 1 | 0 | 0 | draft |
| [VA031](../data/evidence/VA031.json) | 12 | 1 | 0 | 0 | draft |
| [VA032](../data/evidence/VA032.json) | 9 | 1 | 0 | 0 | draft |
| [VA033](../data/evidence/VA033.json) | 9 | 1 | 0 | 0 | draft |
| [VA034](../data/evidence/VA034.json) | 9 | 1 | 0 | 0 | draft |
| [VA035](../data/evidence/VA035.json) | 9 | 1 | 0 | 0 | draft |
| [VA036](../data/evidence/VA036.json) | 9 | 1 | 0 | 0 | draft |
| [VA037](../data/evidence/VA037.json) | 9 | 1 | 0 | 0 | draft |
| [VA038](../data/evidence/VA038.json) | 9 | 1 | 0 | 0 | draft |
| [VA039](../data/evidence/VA039.json) | 9 | 1 | 0 | 0 | draft |
| [VA040](../data/evidence/VA040.json) | 9 | 1 | 0 | 0 | draft |
| [VA041](../data/evidence/VA041.json) | 9 | 1 | 0 | 0 | draft |
| [VA042](../data/evidence/VA042.json) | 9 | 1 | 0 | 0 | draft |
| [VA043](../data/evidence/VA043.json) | 9 | 1 | 0 | 0 | draft |
| [VA044](../data/evidence/VA044.json) | 9 | 1 | 0 | 0 | draft |
| [VA045](../data/evidence/VA045.json) | 9 | 1 | 0 | 0 | draft |
| [VA046](../data/evidence/VA046.json) | 10 | 1 | 0 | 0 | draft |
| [VA047](../data/evidence/VA047.json) | 9 | 1 | 0 | 0 | draft |
| [VA048](../data/evidence/VA048.json) | 9 | 1 | 0 | 0 | draft |
| [VA049](../data/evidence/VA049.json) | 9 | 1 | 0 | 0 | draft |
| [VA050](../data/evidence/VA050.json) | 9 | 1 | 0 | 0 | draft |
| [VA051](../data/evidence/VA051.json) | 9 | 2 | 0 | 0 | draft |
| [VA052](../data/evidence/VA052.json) | 9 | 1 | 0 | 0 | draft |
| [VA053](../data/evidence/VA053.json) | 9 | 1 | 0 | 0 | draft |
| [VA054](../data/evidence/VA054.json) | 9 | 3 | 0 | 0 | draft |
| [VA055](../data/evidence/VA055.json) | 9 | 1 | 0 | 0 | draft |
| [VA056](../data/evidence/VA056.json) | 9 | 1 | 0 | 0 | draft |
| [VA057](../data/evidence/VA057.json) | 9 | 1 | 0 | 0 | draft |
| [VA058](../data/evidence/VA058.json) | 9 | 2 | 0 | 0 | draft |
| [VA059](../data/evidence/VA059.json) | 9 | 1 | 0 | 0 | draft |
| [VA062](../data/evidence/VA062.json) | 9 | 1 | 0 | 0 | draft |
| [VA063](../data/evidence/VA063.json) | 9 | 1 | 0 | 0 | draft |
| [VA064](../data/evidence/VA064.json) | 9 | 1 | 0 | 0 | draft |
| [VA065](../data/evidence/VA065.json) | 9 | 1 | 0 | 0 | draft |
| [VA066](../data/evidence/VA066.json) | 9 | 1 | 0 | 0 | draft |
| [VA067](../data/evidence/VA067.json) | 9 | 1 | 0 | 0 | draft |
| [VA068](../data/evidence/VA068.json) | 9 | 1 | 0 | 0 | draft |
| [VA069](../data/evidence/VA069.json) | 9 | 1 | 0 | 0 | draft |
| [VA070](../data/evidence/VA070.json) | 10 | 1 | 0 | 0 | draft |
| [VA071](../data/evidence/VA071.json) | 9 | 1 | 0 | 0 | draft |
| [VA072](../data/evidence/VA072.json) | 9 | 1 | 0 | 0 | draft |
| [VA073](../data/evidence/VA073.json) | 9 | 1 | 0 | 0 | draft |
| [VA074](../data/evidence/VA074.json) | 9 | 2 | 0 | 0 | draft |
| [VA075](../data/evidence/VA075.json) | 9 | 1 | 0 | 0 | draft |
| [VA076](../data/evidence/VA076.json) | 10 | 1 | 0 | 0 | draft |
| [VA077](../data/evidence/VA077.json) | 9 | 3 | 0 | 0 | draft |
| [VA078](../data/evidence/VA078.json) | 9 | 2 | 0 | 0 | draft |
| [VA079](../data/evidence/VA079.json) | 9 | 1 | 0 | 0 | draft |
| [VA080](../data/evidence/VA080.json) | 9 | 1 | 0 | 0 | draft |
| [VA081](../data/evidence/VA081.json) | 9 | 1 | 0 | 0 | draft |
| [VA082](../data/evidence/VA082.json) | 9 | 1 | 0 | 0 | draft |
| [VA083](../data/evidence/VA083.json) | 9 | 1 | 0 | 0 | draft |
| [VA084](../data/evidence/VA084.json) | 9 | 1 | 0 | 0 | draft |
| [VA085](../data/evidence/VA085.json) | 9 | 2 | 0 | 0 | draft |
| [VA086](../data/evidence/VA086.json) | 9 | 1 | 0 | 0 | draft |
| [VA087](../data/evidence/VA087.json) | 9 | 1 | 0 | 0 | draft |
| [VA088](../data/evidence/VA088.json) | 9 | 1 | 0 | 0 | draft |
| [VA089](../data/evidence/VA089.json) | 9 | 1 | 0 | 0 | draft |
| [VA090](../data/evidence/VA090.json) | 9 | 2 | 0 | 0 | draft |
| [VA091](../data/evidence/VA091.json) | 9 | 1 | 0 | 0 | draft |
| [VA092](../data/evidence/VA092.json) | 9 | 1 | 0 | 0 | draft |
| [VA093](../data/evidence/VA093.json) | 9 | 1 | 0 | 0 | draft |
| [VA094](../data/evidence/VA094.json) | 9 | 1 | 0 | 0 | draft |
| [VA095](../data/evidence/VA095.json) | 9 | 1 | 0 | 0 | draft |
| [VA096](../data/evidence/VA096.json) | 9 | 2 | 0 | 0 | draft |
| [VA097](../data/evidence/VA097.json) | 9 | 1 | 0 | 0 | draft |
| [VA098](../data/evidence/VA098.json) | 9 | 2 | 0 | 0 | draft |
| [VA099](../data/evidence/VA099.json) | 9 | 1 | 0 | 0 | draft |
| [VA100](../data/evidence/VA100.json) | 10 | 3 | 0 | 0 | draft |
| [VA101](../data/evidence/VA101.json) | 10 | 2 | 0 | 0 | draft |
| [VA102](../data/evidence/VA102.json) | 9 | 2 | 0 | 0 | draft |
| [VA103](../data/evidence/VA103.json) | 10 | 2 | 0 | 0 | draft |
| [VA104](../data/evidence/VA104.json) | 9 | 2 | 0 | 0 | draft |
| [VA105](../data/evidence/VA105.json) | 10 | 3 | 0 | 0 | draft |
| [VA106](../data/evidence/VA106.json) | 10 | 2 | 0 | 0 | draft |
| [VA107](../data/evidence/VA107.json) | 9 | 1 | 0 | 0 | draft |
| [VA108](../data/evidence/VA108.json) | 9 | 1 | 0 | 0 | draft |
| [VA109](../data/evidence/VA109.json) | 9 | 1 | 0 | 0 | draft |
| [VA110](../data/evidence/VA110.json) | 9 | 1 | 0 | 0 | draft |
| [VA111](../data/evidence/VA111.json) | 9 | 1 | 0 | 0 | draft |
| [VA113](../data/evidence/VA113.json) | 9 | 1 | 0 | 0 | draft |
| [VA114](../data/evidence/VA114.json) | 9 | 1 | 0 | 0 | draft |
| [VA115](../data/evidence/VA115.json) | 9 | 1 | 0 | 0 | draft |
| [VA116](../data/evidence/VA116.json) | 9 | 1 | 0 | 0 | draft |
| [VA117](../data/evidence/VA117.json) | 9 | 1 | 0 | 0 | draft |
| [VA118](../data/evidence/VA118.json) | 9 | 1 | 0 | 0 | draft |
| [VA119](../data/evidence/VA119.json) | 9 | 1 | 0 | 0 | draft |
| [VA120](../data/evidence/VA120.json) | 9 | 1 | 0 | 0 | draft |
| [VA121](../data/evidence/VA121.json) | 9 | 1 | 0 | 0 | draft |
| [VA122](../data/evidence/VA122.json) | 9 | 1 | 0 | 0 | draft |
| [VA123](../data/evidence/VA123.json) | 9 | 1 | 0 | 0 | draft |
| [VA124](../data/evidence/VA124.json) | 9 | 4 | 0 | 0 | draft |
| [VA125](../data/evidence/VA125.json) | 10 | 1 | 0 | 0 | draft |
| [WV001](../data/evidence/WV001.json) | 9 | 1 | 0 | 0 | draft |
| [WV002](../data/evidence/WV002.json) | 9 | 1 | 0 | 0 | draft |
| [WV003](../data/evidence/WV003.json) | 9 | 1 | 0 | 0 | draft |
| [WV004](../data/evidence/WV004.json) | 9 | 1 | 0 | 0 | draft |
| [WV005](../data/evidence/WV005.json) | 9 | 1 | 0 | 0 | draft |
| [WV006](../data/evidence/WV006.json) | 9 | 1 | 0 | 0 | draft |
| [WV007](../data/evidence/WV007.json) | 9 | 1 | 0 | 0 | draft |
| [WV008](../data/evidence/WV008.json) | 9 | 1 | 0 | 0 | draft |
| [WV009](../data/evidence/WV009.json) | 10 | 4 | 0 | 0 | draft |
| [WV010](../data/evidence/WV010.json) | 10 | 1 | 0 | 0 | draft |
| [WV012](../data/evidence/WV012.json) | 9 | 1 | 0 | 0 | draft |
| [WV013](../data/evidence/WV013.json) | 9 | 1 | 0 | 0 | draft |
| [WV014](../data/evidence/WV014.json) | 9 | 1 | 0 | 0 | draft |
| [WV015](../data/evidence/WV015.json) | 9 | 2 | 0 | 0 | draft |
| [WV016](../data/evidence/WV016.json) | 9 | 2 | 0 | 0 | draft |

## Admission proposal checks

The offline validator retains all 127 engagements / 36 campaign groups in its [coverage ledger](admission-check.json).
It checks 40 Shiloh troop observations: 18 blocked, 22 excluded, 0 eligible candidates, and 0 invalid.
There are 0 complete candidate rows and 0 promoted rows. Missing mappings remain unknown; no canonical opening force is inferred.
The ledger separates dossier availability, candidate status, side coverage and baseline eligibility. These counts are mechanical checks, not historical adjudication or forecast improvement.

## Next research action

The frozen v1 cohort is complete: 127/127 engagements have dossiers. The full-war research frame ([cohort v2](../docs/cohort-v2.md)) has 384 engagements; 384 have dossiers. Dossier presence, separate review, baseline eligibility and feature admission are different measures.
The [Operations about Dandridge first pass](../docs/research/dandridge-first-pass-v1.md) adds all three frozen records: 27 claims, 3 explicit unknowns and 145 citations from NPS/CWSAC, Sturgis's, Martin's and Longstreet's Official Records reports. Strength attributions, the Mossy Creek withdrawal, Sturgis's differing loss and capture figures and the frozen/live casualty differences remain visible; its separate Opus review's seven corrections are applied. All frozen campaign groups now have first-pass dossiers. Earlier passes and reviews remain in the [current roadmap](../docs/roadmap.md).
Use the [bounded first-pass protocol](../docs/methodology.md#research-depth-and-coverage): up to three source families per battle and one targeted follow-up for the most consequential gap. Keep unsupported dimensions unknown, move to the next engagement, and review by campaign. Deeper work requires a concrete decision and stopping point or an explicit owner request.
Shiloh's Agate and overnight-provenance investigations are parked. The [completed research and review history](../docs/roadmap.md#milestone-1--first-independently-reviewed-campaign-dossiers-in-progress) retains all findings and unresolved questions; neither further article collation nor original-newspaper recovery is the next task. No historical feature is admitted by this change in research priority.

## Reproduce and inspect

Run `make check` and `make reproduce` from the repository root.
[Evaluation and fold membership](baseline.json), [coverage](quality.json), [run receipt](receipt.json),
[research queue](research-queue.json), [source manifest](../data/sources.json), [methodology](../docs/methodology.md).

Data: Jeffrey B. Arnold, American Civil War Battle Data (CWSAC tables), derived from U.S. National Park Service summaries; CC-BY-4.0 attribution.
[Pinned upstream data](https://github.com/jrnold/acw_battle_data/tree/3a6020dbfcbcfc650a268b10a9f155588472432b/build/acw_battle_data).
