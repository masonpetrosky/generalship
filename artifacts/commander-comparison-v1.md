# Civil War: Arsht-style scores versus commander estimates

**Result: a better ranking is not demonstrated.** The full commander model has slightly lower held-out log loss per battle, but slightly higher loss when campaigns count equally. The saved simpler commander variant has lower point losses under both weightings, with campaign uncertainty spanning no improvement.

**301 battles · 108 campaign groups · 91 provisional commander orders.** Primary-verified, using saved results; no new fit. These are within-side descriptions, not verified skill ranks or causal wins above replacement.

[Union orders](#union) · [Confederate orders](#confederate) · [Methods](#what-is-compared) · [Coverage](#coverage)

## Does the commander model predict better?

Each campaign was held out as a whole. Every model shown predicts the identical 301 battles. Lower log loss and Brier score are better. This tests prediction of recorded outcomes, not the historical truth of a commander ranking.

| Model | Battle log loss | Campaign log loss | Battle Brier | Campaign Brier |
| --- | ---: | ---: | ---: | ---: |
| Strength-only baseline | 0.656313 | 0.667838 | 0.232002 | 0.237419 |
| Full commander model (θ below) | 0.650044 | 0.668521 | 0.229584 | 0.238044 |
| Simpler commander variant (saved diagnostic) | 0.644558 | 0.662931 | 0.226713 | 0.235476 |

Differences below are commander minus strength-only log loss, with the saved 95% campaign-bootstrap intervals. Negative favors the commander model.

| Comparison | Battle difference [95%] | Campaign difference [95%] |
| --- | ---: | ---: |
| Full commander model (θ below) | -0.006269 [-0.027247, +0.016054] | +0.000682 [-0.024527, +0.026263] |
| Simpler commander variant (saved diagnostic) | -0.011754 [-0.023158, -0.000521] | -0.004907 [-0.020257, +0.011407] |

These comparisons reuse the October 6 development results, not a new final test. The simpler variant was inspected alongside other variants and does not establish a new winner. No historical ranking ground truth exists here. Force size can itself reflect a commander’s preparation, and remaining army, assignment, documentation and source errors can affect every estimate.

## What changes in the ordering?

- Union: raw leader Ulysses S. Grant; model leader Ulysses S. Grant. 12/49 retain the same point position. Largest shifts: William S. Rosecrans 8 → 20; George H. Thomas 12 → 23.
- Confederate: raw leader Nathan Bedford Forrest; model leader Nathan Bedford Forrest. 8/42 retain the same point position. Largest shifts: Robert E. Lee 7 → 19; John Hunt Morgan 29 → 18.

These shifts describe the models’ choices. They do not establish that the new order is more accurate.

## Provisional commander orders

Both orders use the same commanders with at least two credited battles, separately within each side. **Raw order** sorts cumulative residuals; **model order** sorts the stored θ point estimates. Exact ties share an order. The raw mean is also shown to expose the effect of battle count. Intervals for θ and model rank are the saved model-based approximations, conditional on its assumptions. Raw-score uncertainty was not estimated. Broad overlapping rank intervals make fine ordinal differences unreliable.

The opponent network has disconnected components. Comparing θ across them depends on shared model priors, rather than an identified chain of opponents. **† marks 19 commanders with no other eligible same-side commander in their component**, preserving the saved run’s `not_connected` flag. The displayed point order should not be read as an established comparison between components.

### Union

| Model order | Commander | W–L | Modelled strength battles | Raw order | Raw total / battle | θ [95%] | Rank [80%] |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | [Ulysses S. Grant](https://masonpetrosky.github.io/generalship/commanders/us-ulysses-s-grant.html) | 9–1 | 2/10 | 1 | +2.562 / +0.256 | +0.469 [-0.480, +1.435] | 2–30 |
| 2 | [G.K. Warren](https://masonpetrosky.github.io/generalship/commanders/us-g-k-warren.html) | 4–0 | 1/4 | 2 | +1.505 / +0.376 | +0.462 [-0.580, +1.502] | 2–33 |
| 3 | [George B. McClellan](https://masonpetrosky.github.io/generalship/commanders/us-george-b-mcclellan.html) | 3–0 | 0/3 | 4 | +1.152 / +0.384 | +0.409 [-0.648, +1.479] | 2–35 |
| 4 | [John McNeil](https://masonpetrosky.github.io/generalship/commanders/us-john-mcneil.html) | 3–0 | 1/3 | 3 | +1.490 / +0.497 | +0.407 [-0.681, +1.441] | 2–35 |
| 5 | [William W. Averell †](https://masonpetrosky.github.io/generalship/commanders/us-william-w-averell.html) | 3–0 | 1/3 | 6 | +1.074 / +0.358 | +0.342 [-0.734, +1.414] | 3–37 |
| 6 | [Philip Sheridan](https://masonpetrosky.github.io/generalship/commanders/us-philip-sheridan.html) | 6–2 | 1/8 | 13 | +0.786 / +0.098 | +0.291 [-0.671, +1.268] | 4–36 |
| 7 | [John G. Foster †](https://masonpetrosky.github.io/generalship/commanders/us-john-g-foster.html) | 2–0 | 2/2 | 18 | +0.653 / +0.326 | +0.257 [-0.834, +1.338] | 3–40 |
| 8 | [Frederick Steele](https://masonpetrosky.github.io/generalship/commanders/us-frederick-steele.html) | 3–0 | 2/3 | 5 | +1.084 / +0.361 | +0.256 [-0.821, +1.344] | 3–39 |
| 9 | [Edward O.C. Ord](https://masonpetrosky.github.io/generalship/commanders/us-edward-o-c-ord.html) | 2–0 | 1/2 | 9 | +0.879 / +0.440 | +0.252 [-0.844, +1.353] | 3–39 |
| 10 | [Alfred Torbert †](https://masonpetrosky.github.io/generalship/commanders/us-alfred-torbert.html) | 2–0 | 1/2 | 17 | +0.682 / +0.341 | +0.234 [-0.889, +1.341] | 3–40 |
| 11 | [George Stoneman](https://masonpetrosky.github.io/generalship/commanders/us-george-stoneman.html) | 2–0 | 1/2 | 10 | +0.879 / +0.439 | +0.230 [-0.875, +1.341] | 3–40 |
| 12 | [Benjamin M. Prentiss †](https://masonpetrosky.github.io/generalship/commanders/us-benjamin-m-prentiss.html) | 2–0 | 0/2 | 7 | +0.906 / +0.453 | +0.222 [-0.880, +1.329] | 3–40 |
| 13 | [John G. Parke †](https://masonpetrosky.github.io/generalship/commanders/us-john-g-parke.html) | 2–0 | 1/2 | 20 | +0.633 / +0.316 | +0.220 [-0.865, +1.326] | 4–40 |
| 14 | [David G. Farragut †](https://masonpetrosky.github.io/generalship/commanders/us-david-g-farragut.html) | 2–0 | 2/2 | 14 | +0.757 / +0.379 | +0.193 [-0.931, +1.298] | 4–41 |
| 15 | [James Negley †](https://masonpetrosky.github.io/generalship/commanders/us-james-negley.html) | 2–0 | 1/2 | 11 | +0.877 / +0.439 | +0.183 [-0.915, +1.303] | 4–41 |
| 16 | [George G. Meade](https://masonpetrosky.github.io/generalship/commanders/us-george-g-meade.html) | 3–1 | 0/4 | 23 | +0.361 / +0.090 | +0.176 [-0.868, +1.212] | 4–40 |
| 17 | [Ambrose E. Burnside](https://masonpetrosky.github.io/generalship/commanders/us-ambrose-e-burnside.html) | 5–2 | 3/7 | 15 | +0.702 / +0.100 | +0.161 [-0.799, +1.132] | 5–40 |
| 18 | [Joseph A. Mower](https://masonpetrosky.github.io/generalship/commanders/us-joseph-a-mower.html) | 2–0 | 1/2 | 16 | +0.691 / +0.346 | +0.154 [-0.963, +1.257] | 4–42 |
| 19 | [A.J. Smith †](https://masonpetrosky.github.io/generalship/commanders/us-a-j-smith.html) | 2–0 | 1/2 | 19 | +0.634 / +0.317 | +0.149 [-0.964, +1.259] | 4–42 |
| 20 | [William S. Rosecrans](https://masonpetrosky.github.io/generalship/commanders/us-william-s-rosecrans.html) | 4–1 | 0/5 | 8 | +0.903 / +0.181 | +0.130 [-0.885, +1.164] | 5–41 |
| 21 | [James G. Blunt](https://masonpetrosky.github.io/generalship/commanders/us-james-g-blunt.html) | 4–2 | 4/6 | 21 | +0.591 / +0.099 | +0.088 [-0.928, +1.078] | 6–41 |
| 22 | [Cuvier Grover](https://masonpetrosky.github.io/generalship/commanders/us-cuvier-grover.html) | 2–1 | 3/3 | 24 | +0.298 / +0.099 | +0.083 [-0.993, +1.173] | 5–43 |
| 23 | [George H. Thomas](https://masonpetrosky.github.io/generalship/commanders/us-george-h-thomas.html) | 4–1 | 2/5 | 12 | +0.821 / +0.164 | +0.067 [-0.970, +1.110] | 6–43 |
| 24 | [John M. Schofield](https://masonpetrosky.github.io/generalship/commanders/us-john-m-schofield.html) | 3–1 | 2/4 | 22 | +0.545 / +0.136 | +0.027 [-1.026, +1.098] | 6–43 |
| 25 | [Alfred Pleasonton](https://masonpetrosky.github.io/generalship/commanders/us-alfred-pleasonton.html) | 2–1 | 2/3 | 25 | +0.248 / +0.083 | +0.011 [-1.071, +1.094] | 7–44 |
| 26 | [Samuel R. Curtis](https://masonpetrosky.github.io/generalship/commanders/us-samuel-r-curtis.html) | 2–1 | 1/3 | 26 | +0.167 / +0.056 | +0.007 [-1.059, +1.083] | 7–44 |
| 27 | [David Hunter](https://masonpetrosky.github.io/generalship/commanders/us-david-hunter.html) | 1–1 | 0/2 | 34 | -0.258 / -0.129 | -0.024 [-1.094, +1.068] | 7–45 |
| 28 | [James M. Williams †](https://masonpetrosky.github.io/generalship/commanders/us-james-m-williams.html) | 1–1 | 1/2 | 28 | -0.110 / -0.055 | -0.032 [-1.138, +1.069] | 7–45 |
| 29 | [George Crook](https://masonpetrosky.github.io/generalship/commanders/us-george-crook.html) | 1–1 | 0/2 | 31 | -0.206 / -0.103 | -0.034 [-1.119, +1.057] | 7–45 |
| 30 | [Horatio G. Wright](https://masonpetrosky.github.io/generalship/commanders/us-horatio-g-wright.html) | 1–1 | 0/2 | 32 | -0.211 / -0.105 | -0.035 [-1.113, +1.053] | 7–45 |
| 31 | [Jacob D. Cox](https://masonpetrosky.github.io/generalship/commanders/us-jacob-d-cox.html) | 1–1 | 1/2 | 29 | -0.151 / -0.075 | -0.040 [-1.149, +1.071] | 7–45 |
| 32 | [E. R. S. Canby](https://masonpetrosky.github.io/generalship/commanders/us-e-r-s-canby.html) | 2–1 | 1/3 | 27 | -0.024 / -0.008 | -0.052 [-1.109, +1.025] | 8–45 |
| 33 | [Fitz John Porter](https://masonpetrosky.github.io/generalship/commanders/us-fitz-john-porter.html) | 2–2 | 2/4 | 38 | -0.617 / -0.154 | -0.066 [-1.102, +0.966] | 8–45 |
| 34 | [Nathaniel Lyon](https://masonpetrosky.github.io/generalship/commanders/us-nathaniel-lyon.html) | 1–1 | 0/2 | 33 | -0.233 / -0.117 | -0.069 [-1.175, +1.037] | 8–45 |
| 35 | [Nathaniel P. Banks](https://masonpetrosky.github.io/generalship/commanders/us-nathaniel-p-banks.html) | 4–3 | 1/7 | 36 | -0.309 / -0.044 | -0.088 [-1.074, +0.908] | 9–44 |
| 36 | [John T. Wilder †](https://masonpetrosky.github.io/generalship/commanders/us-john-t-wilder.html) | 1–1 | 2/2 | 30 | -0.158 / -0.079 | -0.113 [-1.197, +0.992] | 9–46 |
| 37 | [James Shackelford](https://masonpetrosky.github.io/generalship/commanders/us-james-shackelford.html) | 1–1 | 1/2 | 35 | -0.302 / -0.151 | -0.154 [-1.275, +0.943] | 9–46 |
| 38 | [Benjamin Franklin Butler](https://masonpetrosky.github.io/generalship/commanders/us-benjamin-franklin-butler.html) | 2–3 | 2/5 | 46 | -1.389 / -0.278 | -0.166 [-1.182, +0.850] | 11–46 |
| 39 | [H. Judson Kilpatrick](https://masonpetrosky.github.io/generalship/commanders/us-h-judson-kilpatrick.html) | 2–2 | 3/4 | 37 | -0.505 / -0.126 | -0.238 [-1.286, +0.795] | 12–47 |
| 40 | [Irvin McDowell](https://masonpetrosky.github.io/generalship/commanders/us-irvin-mcdowell.html) | 0–2 | 0/2 | 44 | -1.228 / -0.614 | -0.239 [-1.341, +0.866] | 11–47 |
| 41 | [James H. Wilson](https://masonpetrosky.github.io/generalship/commanders/us-james-h-wilson.html) | 1–3 | 0/4 | 47 | -1.472 / -0.368 | -0.248 [-1.279, +0.778] | 13–47 |
| 42 | [Samuel D. Sturgis](https://masonpetrosky.github.io/generalship/commanders/us-samuel-d-sturgis.html) | 2–2 | 3/4 | 39 | -0.724 / -0.181 | -0.249 [-1.305, +0.793] | 13–47 |
| 43 | [Erastus Tyler](https://masonpetrosky.github.io/generalship/commanders/us-erastus-tyler.html) | 0–2 | 1/2 | 43 | -1.176 / -0.588 | -0.268 [-1.367, +0.820] | 12–47 |
| 44 | [Robert Milroy](https://masonpetrosky.github.io/generalship/commanders/us-robert-milroy.html) | 0–2 | 0/2 | 42 | -1.163 / -0.582 | -0.273 [-1.374, +0.828] | 12–47 |
| 45 | [Franz Sigel](https://masonpetrosky.github.io/generalship/commanders/us-franz-sigel.html) | 0–2 | 0/2 | 41 | -1.134 / -0.567 | -0.283 [-1.382, +0.825] | 13–47 |
| 46 | [Joseph Hooker](https://masonpetrosky.github.io/generalship/commanders/us-joseph-hooker.html) | 1–2 | 1/3 | 40 | -0.906 / -0.302 | -0.308 [-1.404, +0.752] | 13–47 |
| 47 | [William T. Sherman](https://masonpetrosky.github.io/generalship/commanders/us-william-t-sherman.html) | 5–5 | 5/10 | 45 | -1.286 / -0.129 | -0.377 [-1.295, +0.541] | 18–47 |
| 48 | [Quincy A. Gillmore †](https://masonpetrosky.github.io/generalship/commanders/us-quincy-a-gillmore.html) | 1–3 | 1/4 | 48 | -1.647 / -0.412 | -0.383 [-1.442, +0.651] | 16–48 |
| 49 | [Winfield Scott Hancock](https://masonpetrosky.github.io/generalship/commanders/us-winfield-scott-hancock.html) | 0–4 | 3/4 | 49 | -2.484 / -0.621 | -0.567 [-1.609, +0.474] | 22–49 |

### Confederate

| Model order | Commander | W–L | Modelled strength battles | Raw order | Raw total / battle | θ [95%] | Rank [80%] |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | [Nathan Bedford Forrest](https://masonpetrosky.github.io/generalship/commanders/cs-nathan-bedford-forrest.html) | 9–3 | 4/12 | 1 | +4.471 / +0.373 | +0.964 [+0.086, +1.835] | 1–13 |
| 2 | [P.G.T. Beauregard](https://masonpetrosky.github.io/generalship/commanders/cs-p-g-t-beauregard.html) | 6–1 | 2/7 | 2 | +3.130 / +0.447 | +0.636 [-0.331, +1.606] | 2–23 |
| 3 | [Patrick R. Cleburne](https://masonpetrosky.github.io/generalship/commanders/cs-patrick-r-cleburne.html) | 2–0 | 0/2 | 8 | +1.277 / +0.639 | +0.431 [-0.649, +1.537] | 2–30 |
| 4 | [Joseph E. Johnston](https://masonpetrosky.github.io/generalship/commanders/cs-joseph-e-johnston.html) | 5–4 | 3/9 | 4 | +1.570 / +0.174 | +0.392 [-0.567, +1.352] | 3–29 |
| 5 | [William C. Quantrill †](https://masonpetrosky.github.io/generalship/commanders/cs-william-c-quantrill.html) | 2–0 | 2/2 | 5 | +1.365 / +0.682 | +0.389 [-0.720, +1.485] | 2–31 |
| 6 | [John B. Magruder †](https://masonpetrosky.github.io/generalship/commanders/cs-john-b-magruder.html) | 2–0 | 1/2 | 6 | +1.341 / +0.670 | +0.362 [-0.732, +1.453] | 2–32 |
| 7 | [Thomas J. Jackson](https://masonpetrosky.github.io/generalship/commanders/cs-thomas-j-jackson.html) | 6–2 | 1/8 | 3 | +2.700 / +0.338 | +0.359 [-0.608, +1.340] | 3–30 |
| 8 | [James Longstreet](https://masonpetrosky.github.io/generalship/commanders/cs-james-longstreet.html) | 4–3 | 4/7 | 9 | +1.259 / +0.180 | +0.338 [-0.613, +1.315] | 3–31 |
| 9 | [Wade Hampton](https://masonpetrosky.github.io/generalship/commanders/cs-wade-hampton.html) | 2–0 | 0/2 | 10 | +1.224 / +0.612 | +0.324 [-0.769, +1.416] | 3–33 |
| 10 | [Nathan Evans †](https://masonpetrosky.github.io/generalship/commanders/cs-nathan-evans.html) | 2–1 | 1/3 | 11 | +1.027 / +0.342 | +0.257 [-0.808, +1.313] | 3–34 |
| 11 | [John C. Breckinridge †](https://masonpetrosky.github.io/generalship/commanders/cs-john-c-breckinridge.html) | 3–2 | 1/5 | 12 | +0.889 / +0.178 | +0.234 [-0.766, +1.219] | 4–33 |
| 12 | [James R. Chalmers](https://masonpetrosky.github.io/generalship/commanders/cs-james-r-chalmers.html) | 2–1 | 1/3 | 14 | +0.555 / +0.185 | +0.233 [-0.830, +1.303] | 4–34 |
| 13 | [Tom Green](https://masonpetrosky.github.io/generalship/commanders/cs-tom-green.html) | 3–2 | 3/5 | 13 | +0.819 / +0.164 | +0.184 [-0.831, +1.197] | 4–34 |
| 14 | [George A. Anderson †](https://masonpetrosky.github.io/generalship/commanders/cs-george-a-anderson.html) | 1–1 | 1/2 | 16 | +0.427 / +0.214 | +0.137 [-0.967, +1.252] | 4–37 |
| 15 | [John S. Bowen](https://masonpetrosky.github.io/generalship/commanders/cs-john-s-bowen.html) | 1–2 | 2/3 | 23 | -0.041 / -0.014 | +0.118 [-0.965, +1.208] | 5–36 |
| 16 | [George Pickett](https://masonpetrosky.github.io/generalship/commanders/cs-george-pickett.html) | 1–1 | 1/2 | 17 | +0.344 / +0.172 | +0.111 [-0.987, +1.213] | 5–37 |
| 17 | [John C. Pemberton](https://masonpetrosky.github.io/generalship/commanders/cs-john-c-pemberton.html) | 1–2 | 2/3 | 26 | -0.131 / -0.044 | +0.094 [-1.004, +1.179] | 5–37 |
| 18 | [John Hunt Morgan](https://masonpetrosky.github.io/generalship/commanders/cs-john-hunt-morgan.html) | 2–4 | 1/6 | 29 | -0.363 / -0.060 | +0.072 [-0.926, +1.087] | 6–36 |
| 19 | [Robert E. Lee](https://masonpetrosky.github.io/generalship/commanders/cs-robert-e-lee.html) | 8–10 | 5/18 | 7 | +1.325 / +0.074 | +0.046 [-0.762, +0.849] | 9–35 |
| 20 | [Richard H. Anderson †](https://masonpetrosky.github.io/generalship/commanders/cs-richard-h-anderson.html) | 1–1 | 1/2 | 20 | +0.173 / +0.087 | +0.038 [-1.054, +1.115] | 6–38 |
| 21 | [Richard S. Ewell](https://masonpetrosky.github.io/generalship/commanders/cs-richard-s-ewell.html) | 2–2 | 1/4 | 15 | +0.528 / +0.132 | +0.038 [-0.995, +1.083] | 6–37 |
| 22 | [Humphrey Marshall](https://masonpetrosky.github.io/generalship/commanders/cs-humphrey-marshall.html) | 1–1 | 2/2 | 21 | +0.137 / +0.069 | +0.035 [-1.076, +1.145] | 6–38 |
| 23 | [John B. Floyd](https://masonpetrosky.github.io/generalship/commanders/cs-john-b-floyd.html) | 1–1 | 1/2 | 18 | +0.296 / +0.148 | +0.028 [-1.080, +1.149] | 6–38 |
| 24 | [Robert Hoke](https://masonpetrosky.github.io/generalship/commanders/cs-robert-hoke.html) | 1–1 | 1/2 | 19 | +0.228 / +0.114 | +0.013 [-1.075, +1.115] | 6–38 |
| 25 | [Sterling Price](https://masonpetrosky.github.io/generalship/commanders/cs-sterling-price.html) | 4–6 | 5/10 | 30 | -0.564 / -0.056 | +0.001 [-0.927, +0.936] | 8–37 |
| 26 | [Douglas H. Cooper](https://masonpetrosky.github.io/generalship/commanders/cs-douglas-h-cooper.html) | 1–1 | 0/2 | 22 | +0.061 / +0.030 | -0.009 [-1.106, +1.093] | 6–39 |
| 27 | [J.E.B. Stuart](https://masonpetrosky.github.io/generalship/commanders/cs-j-e-b-stuart.html) | 1–2 | 1/3 | 24 | -0.078 / -0.026 | -0.064 [-1.129, +1.000] | 8–39 |
| 28 | [Braxton Bragg](https://masonpetrosky.github.io/generalship/commanders/cs-braxton-bragg.html) | 1–4 | 1/5 | 35 | -0.835 / -0.167 | -0.089 [-1.121, +0.953] | 8–39 |
| 29 | [Henry Heth](https://masonpetrosky.github.io/generalship/commanders/cs-henry-heth.html) | 1–2 | 2/3 | 27 | -0.144 / -0.048 | -0.111 [-1.160, +0.968] | 9–39 |
| 30 | [Jubal A. Early](https://masonpetrosky.github.io/generalship/commanders/cs-jubal-a-early.html) | 3–5 | 1/8 | 25 | -0.107 / -0.013 | -0.115 [-1.075, +0.835] | 10–39 |
| 31 | [A.P. Hill](https://masonpetrosky.github.io/generalship/commanders/cs-a-p-hill.html) | 1–2 | 0/3 | 28 | -0.204 / -0.068 | -0.125 [-1.200, +0.945] | 9–39 |
| 32 | [John S. Williams](https://masonpetrosky.github.io/generalship/commanders/cs-john-s-williams.html) | 0–2 | 1/2 | 34 | -0.707 / -0.354 | -0.143 [-1.266, +0.962] | 8–40 |
| 33 | [William T. Martin](https://masonpetrosky.github.io/generalship/commanders/cs-william-t-martin.html) | 0–2 | 2/2 | 31 | -0.659 / -0.329 | -0.169 [-1.289, +0.949] | 9–40 |
| 34 | [Earl Van Dorn](https://masonpetrosky.github.io/generalship/commanders/cs-earl-van-dorn.html) | 1–4 | 3/5 | 39 | -1.299 / -0.260 | -0.208 [-1.223, +0.822] | 11–40 |
| 35 | [John S. Marmaduke](https://masonpetrosky.github.io/generalship/commanders/cs-john-s-marmaduke.html) | 3–7 | 2/10 | 38 | -1.206 / -0.121 | -0.221 [-1.154, +0.704] | 13–40 |
| 36 | [Thomas C. Hindman †](https://masonpetrosky.github.io/generalship/commanders/cs-thomas-c-hindman.html) | 0–2 | 0/2 | 37 | -0.971 / -0.485 | -0.235 [-1.330, +0.886] | 10–41 |
| 37 | [John B. Gordon †](https://masonpetrosky.github.io/generalship/commanders/cs-john-b-gordon.html) | 0–2 | 0/2 | 33 | -0.671 / -0.336 | -0.245 [-1.338, +0.859] | 11–41 |
| 38 | [Lawrence O'Bryan Branch](https://masonpetrosky.github.io/generalship/commanders/cs-lawrence-obryan-branch.html) | 0–2 | 0/2 | 32 | -0.664 / -0.332 | -0.249 [-1.333, +0.848] | 11–41 |
| 39 | [D. H. Hill](https://masonpetrosky.github.io/generalship/commanders/cs-d-h-hill.html) | 0–2 | 2/2 | 36 | -0.895 / -0.447 | -0.249 [-1.360, +0.836] | 11–41 |
| 40 | [Richard Taylor](https://masonpetrosky.github.io/generalship/commanders/cs-richard-taylor.html) | 1–6 | 3/7 | 40 | -1.850 / -0.264 | -0.408 [-1.416, +0.602] | 16–41 |
| 41 | [John Bell Hood](https://masonpetrosky.github.io/generalship/commanders/cs-john-bell-hood.html) | 1–8 | 4/9 | 42 | -2.753 / -0.306 | -0.424 [-1.382, +0.550] | 17–41 |
| 42 | [Joseph Wheeler](https://masonpetrosky.github.io/generalship/commanders/cs-joseph-wheeler.html) | 0–5 | 2/5 | 41 | -2.126 / -0.425 | -0.437 [-1.456, +0.616] | 16–41 |

## What is compared

The [Arsht notebook](https://github.com/ethanarsht/military_rankings/blob/d2d77e89c054b2eae45320c0e5c69f0821f85ffa/battle_project.ipynb) adds each commander’s outcome-minus-model-expectation residuals. Here the same scoring idea uses total personnel and the saved strength-only forecasts for campaigns excluded from training. For a Union side: residual = recorded Union outcome − predicted Union outcome; the Confederate residual is its negative. We show both the cumulative total and the mean per battle.

The shrunk estimate θ comes from the existing force + context + commander model: it adjusts for opponent commander and theater/period and pulls sparse estimates toward zero. θ is in log-odds units; raw residual totals are in residual-outcome units. Their numerical sizes cannot be subtracted or interpreted as the same quantity. Order changes also reflect exposure, opponent/context adjustments and different units, not shrinkage alone.

**This is an Arsht-style adaptation on our Civil War data, not a reproduction of his published rankings.** His notebook uses multiple force categories, in-sample fitting, different missing-data rules and attribution. Our comparison uses the same saved battles and attribution for both columns. Its strength-only baseline already includes AI-researched ledger inputs; this does not isolate the benefit of AI versus his source data. Rating run 4 and its unsuccessful pre-registered verdict remain unchanged.

## Coverage

- 384 engagements in the frozen cohort; 79 outside the two-sided decisive ledger.
- 305 ledger engagements minus 4 nested records = 301 scored battles across 108 source campaign groups.
- 120/301 battles use at least one modelled strength, rather than two usable ledger estimates.
- 91/313 saved commanders have at least two credited battles: 49 Union and 42 Confederate. The 211 single-battle and 11 zero-battle commanders remain in the downloadable data with no assigned order.
- 26 battle-sides receive no commander credit under the saved attribution rules; joint command is not automatically assigned to every named officer.

## Reproduce and inspect

`python3 -m generalship.commander_comparison --write` regenerates this comparison offline from saved results. With no flag it checks the committed JSON and this report. Neither command fits a model, fetches sources or changes frozen inputs.

[Download all commander and battle rows](commander-comparison-v1.json). [Original rating run](commander-ratings-v4.md). [Strength and command evidence](../docs/ledgers-v3.md). [Source conventions](../docs/sources.md#audit-of-the-original-project).

The JSON retains exact input SHA-256 bindings, exclusions, battle-level residuals, all 313 saved commanders and the unchanged original verdict. The computational reference is `arsht-military-rankings-notebook-d2d77e8`, SHA-256 `85500155549b0aa432530a9eed9d086c3664ddf21a50ce76411a81710a02f5a3`, zero-based notebook cells 159–167 and 196–198, inspected 2026-10-21. The external notebook is referenced, not redistributed.
