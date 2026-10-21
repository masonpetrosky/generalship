# Bodart: names consolidated, same battles

**542 unchanged engagements · 8 supported alias groups · 655 estimated labels · 68 provisional orders.** Bonaparte and Napoleon I now contribute to one scoped identity. This is a bounded cleanup using Bodart’s own index, followed by the same model and evaluation settings.

[Download estimates](bodart-ratings-v2.csv) · [Saved run and folds](bodart-ratings-v2.json) · [Alias evidence](../data/bodart/aliases-v1/aliases.json) · [Migration and coverage](../data/bodart/ratings-v2/cohort.json) · [Fixed design](../docs/bodart-ratings-v2.md) · [First run](bodart-ratings-v1.md)

## What changed?

| Quantity | First run | Alias cleanup |
| --- | ---: | ---: |
| Engagements | 542 | 542 |
| Command labels | 669 | 655 |
| Labels with at least three appearances | 72 | 68 |
| Opponent components | 204 | 201 |
| Labels in largest component | 178 | 176 |
| Checked force pairs | 354 | 354 |

The map covers 111 side appearances; 46 side appearances receive a different canonical key. 12 rows reverse their alphabetic A/B orientation, with forces swapped, log force ratio negated and outcome complemented. No outcome or force reading changes. No excluded row is rescued and all 52 reserved-final entries stay excluded.

| Consolidated name | First-run labels | Included appearances | Old component/orders | New component/order |
| --- | ---: | ---: | --- | --- |
| Napoleon I | 2 | 38 | C1: 1, C1: 2 | C1: 1 |
| Archduke Karl of Austria | 4 | 22 | C1: 12, C1: 7, C1: unranked, C4: unranked | C1: 11 |
| Melas | 2 | 8 | C1: 14, C1: 9 | C1: 7 |
| Prince Josias of Koburg | 3 | 9 | C1: 18, C1: 40, C1: unranked | C1: 17 |
| Gouvion Saint-Cyr | 2 | 10 | C1: 4, C1: unranked | C1: 3 |
| Wellington | 5 | 10 | C1: 8, C1: unranked, C33: unranked, C1: unranked, C1: unranked | C1: 2 |
| Bennigsen | 2 | 4 | C1: 33, C1: unranked | C1: 40 |
| Kray | 2 | 10 | C1: 34, C63: unranked | C1: 38 |

These orders use different label rosters and connected components; the movement is descriptive. Merging labels also changes partial pooling and the effective prior structure. It does not isolate a change in personal skill.

## Same held-out battles and folds

Leave each of the same calendar decades out of training in turn. Lower log loss and Brier score are better. This remains development evaluation: campaigns may cross decade boundaries and it is not a final or forward test.

| Model | Battle log loss | Equal-decade log loss | Battle Brier | Equal-decade Brier |
| --- | ---: | ---: | ---: | ---: |
| Equal odds | 0.693147 | 0.693147 | 0.250000 | 0.250000 |
| Force only | 0.663196 | 0.719430 | 0.234880 | 0.261950 |
| First-run command labels | 0.638346 | 0.701488 | 0.223695 | 0.253022 |
| Consolidated command labels | 0.618308 | 0.696562 | 0.215952 | 0.251044 |

Cleanup minus first-run log loss: **-0.020038 per battle** and **-0.004926 per decade**. The force-only and equal-odds comparators reproduce unchanged losses on the paired rows. These point differences do not establish correct skill ranks or isolate AI’s benefit.

Equal-decade log loss is 0.696562, versus 0.693147 for equal odds.

Held-out labels seen in training (first run → cleanup): both 39 → 54, one 183 → 181, neither 320 → 307, out of 542. Unseen labels use prior mean zero.

## Provisional orders

Order only labels with at least three appearances, within each connected opponent component. θ is a shrunk conditional log-odds association. The 95% intervals are approximate marginal Laplace intervals conditional on the model and recorded inputs. They omit source/OCR, identity, army, campaign and model uncertainty; overlapping intervals do not settle adjacent ranks. Most labels remain unresolved strings despite these eight mappings. There is no cross-component ranking or causal WAR.


### Opponent component 1

48 ordered out of 176 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | Napoleon I | 1796–1813 | 38 (36) | 38 | +2.263 (+1.305, +3.221) | 1 / 1 |
| 2 | Wellington | 1808–1813 | 10 (10) | 10 | +1.567 (+0.232, +2.902) | 2 / 2 |
| 3 | Gouvion Saint-Cyr | 1799–1812 | 10 (9) | 10 | +1.230 (-0.045, +2.505) | 3 / 5 |
| 4 | gf suworow | 1773–1799 | 5 (5) | 4 | +1.216 (-0.245, +2.677) | 4 / 3 |
| 5 | gf wittgenstein | 1812–1813 | 7 (5) | 7 | +1.114 (-0.208, +2.436) | 7 / 4 |
| 6 | davoust | 1805–1812 | 7 (6) | 7 | +0.996 (-0.340, +2.332) | 6 / 6 |
| 7 | Melas | 1799–1800 | 8 (7) | 8 | +0.990 (-0.389, +2.368) | 8 / 7 |
| 8 | moreau | 1796–1800 | 16 (12) | 16 | +0.901 (-0.151, +1.953) | 5 / 9 |
| 9 | lannes | 1800–1806 | 3 (3) | 3 | +0.794 (-0.812, +2.400) | 9 / 8 |
| 10 | richepanse | 1800–1800 | 4 (4) | 4 | +0.729 (-0.862, +2.321) | 10 / 10 |
| 11 | Archduke Karl of Austria | 1793–1809 | 22 (11) | 22 | +0.659 (-0.273, +1.592) | 12 / 11 |
| 12 | gf wurmser | 1793–1796 | 7 (4) | 7 | +0.593 (-0.811, +1.996) | 15 / 12 |
| 13 | baron beaulieu | 1793–1796 | 4 (2) | 4 | +0.501 (-1.099, +2.102) | 18 / 13 |
| 14 | victor | 1797–1812 | 6 (4) | 6 | +0.465 (-0.911, +1.841) | 17 / 14 |
| 15 | ney | 1799–1812 | 8 (6) | 8 | +0.453 (-0.839, +1.744) | 11 / 22 |
| 16 | soult | 1799–1813 | 13 (7) | 13 | +0.446 (-0.646, +1.538) | 14 / 15 |
| 17 | Prince Josias of Koburg | 1793–1794 | 9 (6) | 9 | +0.427 (-0.805, +1.659) | 13 / 17 |
| 18 | fürst schwarzenberg | 1805–1813 | 4 (3) | 4 | +0.418 (-1.142, +1.979) | 19 / 16 |
| 19 | fh v elsnitz | 1799–1800 | 3 (2) | 3 | +0.321 (-1.226, +1.869) | 21 / 24 |
| 20 | lecourbe | 1799–1800 | 8 (5) | 8 | +0.288 (-0.954, +1.530) | 20 / 26 |
| 21 | macdonald | 1794–1813 | 5 (3) | 5 | +0.287 (-1.140, +1.715) | 23 / 20 |
| 22 | lefebvre | 1796–1809 | 5 (3) | 5 | +0.263 (-1.180, +1.706) | 22 / 25 |
| 23 | jourdan | 1793–1799 | 8 (4) | 8 | +0.245 (-0.998, +1.489) | 26 / 21 |
| 24 | desaix | 1796–1798 | 3 (2) | 3 | +0.216 (-1.346, +1.778) | 24 / 29 |
| 25 | erzhz johann v österreich | 1800–1809 | 6 (3) | 6 | +0.216 (-1.182, +1.613) | 27 / 18 |
| 26 | suchet | 1800–1813 | 11 (7) | 11 | +0.199 (-1.002, +1.400) | 16 / 38 |
| 27 | erzhz ferdinand v österreich | 1805–1809 | 3 (2) | 3 | +0.192 (-1.382, +1.767) | 25 / 36 |
| 28 | fh v hiller | 1809–1809 | 3 (1) | 3 | +0.178 (-1.491, +1.848) | 31 / 19 |
| 29 | colli | 1793–1796 | 3 (1) | 3 | +0.168 (-1.448, +1.784) | 28 / 23 |
| 30 | masséna | 1794–1811 | 23 (12) | 23 | +0.138 (-0.767, +1.043) | 29 / 27 |
| 31 | barclay de tolly | 1807–1813 | 4 (2) | 4 | +0.099 (-1.456, +1.654) | 30 / 33 |
| 32 | baron davidovich | 1796–1796 | 3 (1) | 3 | +0.092 (-1.629, +1.813) | 32 / 31 |
| 33 | dumouriez | 1792–1793 | 4 (2) | 4 | +0.057 (-1.425, +1.539) | 33 / 32 |
| 34 | championnet | 1798–1799 | 3 (1) | 3 | +0.039 (-1.580, +1.658) | 34 / 35 |
| 35 | vizekönig pz eugen beauharnais | 1809–1813 | 6 (3) | 6 | +0.003 (-1.404, +1.410) | 35 / 30 |
| 36 | gf sztarray | 1796–1800 | 4 (1) | 4 | -0.006 (-1.539, +1.527) | 37 / 28 |
| 37 | grenier | 1799–1799 | 3 (1) | 3 | -0.018 (-1.675, +1.640) | 36 / 37 |
| 38 | Kray | 1794–1800 | 10 (4) | 10 | -0.061 (-1.242, +1.120) | 38 / 39 |
| 39 | gf latour | 1794–1796 | 4 (1) | 4 | -0.087 (-1.606, +1.433) | 39 / 34 |
| 40 | Bennigsen | 1806–1807 | 4 (1) | 4 | -0.159 (-1.731, +1.413) | 42 / 41 |
| 41 | oudinot | 1799–1813 | 5 (2) | 5 | -0.164 (-1.577, +1.249) | 40 / 40 |
| 42 | schérer | 1795–1799 | 3 (1) | 3 | -0.270 (-1.816, +1.277) | 41 / 42 |
| 43 | fürst bagration | 1799–1812 | 4 (1) | 4 | -0.342 (-1.897, +1.213) | 43 / 44 |
| 44 | fh v hotze | 1799–1799 | 6 (2) | 6 | -0.352 (-1.699, +0.995) | 44 / 43 |
| 45 | pichegru | 1794–1795 | 8 (3) | 8 | -0.474 (-1.789, +0.840) | 45 / 45 |
| 46 | gf clerfayt | 1794–1795 | 7 (2) | 7 | -0.527 (-1.856, +0.803) | 46 / 46 |
| 47 | fh v ott | 1800–1800 | 3 (0) | 3 | -0.841 (-2.422, +0.740) | 47 / 48 |
| 48 | blake | 1808–1811 | 8 (1) | 8 | -0.937 (-2.297, +0.423) | 48 / 47 |

### Opponent component 2

2 ordered out of 9 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | bern | 1849–1849 | 3 (1) | 0 | -0.155 (-1.738, +1.428) | 1 / 1 |
| 2 | görgey | 1849–1849 | 4 (1) | 0 | -0.448 (-1.945, +1.048) | 2 / 2 |

### Opponent component 3

3 ordered out of 8 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | sir abercrombie | 1799–1801 | 4 (4) | 4 | +0.867 (-0.704, +2.437) | 1 / 1 |
| 2 | brune | 1799–1799 | 4 (2) | 4 | +0.184 (-1.327, +1.695) | 3 / 2 |
| 3 | hz v york | 1793–1799 | 5 (3) | 5 | +0.178 (-1.269, +1.625) | 2 / 3 |

### Opponent component 4

2 ordered out of 7 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | j b hood | 1864–1864 | 3 (1) | 0 | -0.160 (-1.749, +1.429) | 1 / 1 |
| 2 | j johnston | 1864–1866 | 4 (1) | 0 | -0.194 (-1.734, +1.345) | 2 / 2 |

### Opponent component 5

1 ordered out of 6 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | friedrich ii | 1742–1760 | 5 (4) | 0 | +0.799 (-0.642, +2.240) | 1 / 1 |

### Opponent component 6

2 ordered out of 5 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | don ricardos | 1793–1793 | 4 (3) | 4 | +0.496 (-1.002, +1.995) | 1 / 1 |
| 2 | b g daoust | 1793–1793 | 3 (1) | 3 | -0.276 (-1.859, +1.306) | 2 / 2 |

### Opponent component 8

1 ordered out of 5 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | g garibaldi | 1860–1867 | 4 (2) | 0 | -0.004 (-1.475, +1.466) | 1 / 1 |

### Opponent component 9

1 ordered out of 5 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | gf tilly | 1622–1632 | 3 (1) | 0 | -0.166 (-1.737, +1.406) | 1 / 1 |

### Opponent component 11

1 ordered out of 4 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | mqs de la roche jacquelin | 1793–1793 | 4 (3) | 4 | +0.179 (-1.355, +1.713) | 1 / 1 |

### Opponent component 12

1 ordered out of 4 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | kosciuszko | 1792–1794 | 3 (2) | 3 | +0.307 (-1.257, +1.871) | 1 / 1 |

### Opponent component 13

2 ordered out of 4 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | gf radetzky | 1848–1848 | 3 (3) | 0 | +0.774 (-0.879, +2.427) | 1 / 1 |
| 2 | könig carlo alberto von sardinien | 1848–1848 | 3 (1) | 0 | -0.399 (-2.013, +1.215) | 2 / 2 |

### Opponent component 14

1 ordered out of 4 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | hoche | 1793–1797 | 3 (2) | 3 | +0.145 (-1.431, +1.721) | 1 / 1 |

### Opponent component 16

1 ordered out of 4 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | könig karl xii | 1701–1708 | 3 (3) | 1 | +0.975 (-0.627, +2.577) | 1 / 1 |

### Opponent component 23

1 ordered out of 3 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | rosecrans | 1862–1863 | 3 (2) | 0 | +0.165 (-1.449, +1.779) | 1 / 1 |

### Opponent component 28

1 ordered out of 3 estimated labels.

| Order | Name or printed label | Years | Battles (wins) | Checked force pairs | θ (95% interval) | Prior SD 0.5 / 2 orders |
| ---: | --- | --- | ---: | ---: | --- | --- |
| 1 | gf lambert | 1812–1812 | 3 (3) | 3 | +0.651 (-1.006, +2.308) | 1 / 1 |

## Evidence for the eight mappings

Primary-verified against eight retained index images and nine selected passages. These are all one Bodart source family. Index co-reference supports scoped compiler identity, not independent biographical truth or verified command responsibility. The alias download retains all original labels, exact row/side occurrences, citations and hashes.

### Napoleon I

Explicit Bonaparte/Napoleon cross-reference; Jérôme and Joseph stay separate. Scope is the original 1796–1813 model records.

Original units: `napoleon i`, `bonaparte`.

> Bonaparte, Jérôme, franz. Gen. 378 „ Joseph, König v. Spanien 410, 452 „ Napoleon, siehe Napoleon I.

[printed p.920, Alphabetisches Register, bonaparte entry](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n921/mode/1up); [source and SHA-256](https://masonpetrosky.github.io/generalship/sources.html#bodart-1908-alias-p920-manual-v1).

### Archduke Karl of Austria

The single Archduke-of-Austria index entry groups title and v./von variants at the cited battle pages; other Karls are not merged.

Original units: `erzhz karl v österreich`, `erzhz karl von österreich`, `erzherzog karl`, `generalissimus erzhz karl v österreich`.

> Karl, Erzhzg. v. Österreich 272, 308, 310, 311, 315, 317, 320, 321, 328, 329, 336, 342, 367, 397, 399, 400, 405, 409, 410, 789

[printed p.933, Alphabetisches Register, karl entry](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n934/mode/1up); [source and SHA-256](https://masonpetrosky.github.io/generalship/sources.html#bodart-1908-alias-p933-manual-v1).

Index page-reference omissions: B312c, B312d. The scoped same-literal mapping is retained; the omission is not silently repaired.

### Melas

The Melas index entry groups pages using Fh. v. and Baron. Marengo p.355 is omitted from this index entry; its same normalized Baron-Melas literal is retained within this scoped mapping, with the omission visible.

Original units: `baron melas`, `fh v melas`.

> Melas, österr. Gen. 342, 346, 347, 348, 349, 350, 351

[printed p.939, Alphabetisches Register, melas entry](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n940/mode/1up); [source and SHA-256](https://masonpetrosky.github.io/generalship/sources.html#bodart-1908-alias-p939-manual-v1).

Index page-reference omissions: B355c. The scoped same-literal mapping is retained; the omission is not silently repaired.

### Prince Josias of Koburg

One Josias-of-Koburg index entry links the pages printing Coburg/Koburg and v./von variants.

Original units: `pz v coburg`, `pz v koburg`, `pz von koburg`.

> Koburg, Pz. Josias, öst. Gen. 263, 264, 265, 272, 273, 277, 281, 282, 286, 287, 289, 290, 293, 788

[printed p.934, Alphabetisches Register, koburg entry](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n935/mode/1up); [source and SHA-256](https://masonpetrosky.github.io/generalship/sources.html#bodart-1908-alias-p934-manual-v1).

### Gouvion Saint-Cyr

Index groups the St.-Cyr/Saint-Cyr pages and explicitly redirects Saint-Cyr to Gouvion.

Original units: `gouvion st cyr`, `gouvion saint cyr`.

> Gouvion St.-Cyr, fz. Gen. 346, 347, 348, 353, 369, 392, 394, 413, 415, 435, 440, 465

[printed p.929, Alphabetisches Register, gouvion entry](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n930/mode/1up); [source and SHA-256](https://masonpetrosky.github.io/generalship/sources.html#bodart-1908-alias-p929-manual-v1).

> Saint-Cyr, siehe Gouvion

[printed p.947, Alphabetisches Register, saint-cyr entry](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n948/mode/1up); [source and SHA-256](https://masonpetrosky.github.io/generalship/sources.html#bodart-1908-alias-p947-manual-v1).

### Wellington

Wellington index explicitly lists all ten scoped pages/records using Wellesley and Wellington titles. This follows compiler identity, not an adjudication of the printed Marquis-Wellesley title; original title strings remain.

Original units: `sir wellesley`, `marquis wellesley`, `mqs wellesley`, `lord wellington`, `generalissimus lord wellington`.

> Wellington, engl. Gen. 389, 403, 410, 420, 423, 424, 430, 431, 432, 411, 452, 453, 457, 458, 460, 464, 467, 474, 481, 486, 487, 790, 814, 815, 823, 830

[printed p.954, Alphabetisches Register, wellington entry](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n955/mode/1up); [source and SHA-256](https://masonpetrosky.github.io/generalship/sources.html#bodart-1908-alias-p954-manual-v1).

### Bennigsen

One Bennigsen index entry groups the pages printing Fh. v. and von variants.

Original units: `fh v bennigsen`, `von bennigsen`.

> Bennigsen, russ. Gen. 377, 380, 382, 383, 483

[printed p.920, Alphabetisches Register, bennigsen entry](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n921/mode/1up); [source and SHA-256](https://masonpetrosky.github.io/generalship/sources.html#bodart-1908-alias-p920-manual-v1).

### Kray

One Kray index entry groups pages printing Fh. v. and Baron variants.

Original units: `fh v kray`, `baron kray`.

> Kray, österr. Gen. 282, 285, 309, 312, 330, 331, 333, 339, 347, 352, 353, 354, 356

[printed p.935, Alphabetisches Register, kray entry](https://archive.org/details/bub_gb_A0kNAAAAYAAJ/page/n936/mode/1up); [source and SHA-256](https://masonpetrosky.github.io/generalship/sources.html#bodart-1908-alias-p935-manual-v1).

## Limits and verification

587 labels have fewer than three appearances and receive no order. Source/force coverage is unchanged: 354/542 force pairs checked. OCR names and years remain uncertain; no new per-battle historical check is implied. Title strings including “Marquis Wellesley” remain as printed.

The fixed personnel-checked sensitivity uses 354 rows, 337 labels and 57 orders, on a different cohort. Prior sensitivity columns are alternative point orders, not rank confidence intervals. All settings, priors and folds match v1; no post-result tuning was performed.

The saved run records base commit `9e2fd32e374b7490fd1408fd0f76cb59506218b7` and SHA-256s for the fixed mapping, source snapshots, prepared migration, protocol and reused fitting engine. Primary verification checks exact source passages and scope, orientation, identical battle/fold membership, penalized gradients, inverse-Hessian intervals, saved predictions and paired metrics without refitting historical outcomes. Army confounding and the fact that force advantages can be commander-created remain.

`python3 -m generalship.bodart_ratings_v2 --write` rebuilds this report and estimates CSV from the saved run. The default verifies them. Ordinary reproduction does not run the historical fitting job. The first report and all frozen inputs remain available.
