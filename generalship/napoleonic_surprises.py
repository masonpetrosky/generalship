"""Browse saved campaign-held-out forecasts; no fitting or historical re-encoding."""

import math

from .sources import digest, read_json

DATA = 'artifacts/napoleonic-benchmark-v1.json'
RUN = 'artifacts/napoleonic-benchmark-run-v1.json'
REPORT = 'docs/research/napoleonic-benchmark-run-v1.md'
NATIONS = {'FR': 'France', 'GB': 'Britain', 'AT': 'Austria', 'PR': 'Prussia', 'RU': 'Russia',
           'ES': 'Spain', 'PT': 'Portugal', 'BAV': 'Bavaria', 'SAX': 'Saxony', 'WUR': 'Württemberg',
           'IT': 'Italy', 'PL': 'Poland', 'DK': 'Denmark', 'SE': 'Sweden', 'TYR': 'Tyrolean forces',
           'ALLIES': 'Allied forces', 'NA': 'Unspecified forces'}


def load_rows(root, frame):
    run, data = read_json(root / RUN), read_json(root / DATA)
    if run['executed_bindings'][DATA] != digest(root / DATA) or run['reserved_final_used'] is not False:
        raise ValueError('Surprises require the unchanged development-only benchmark extract')
    entries = {e['battle_id']: e for e in data['entries']}
    predictions = run['populations']['primary']['leave_campaign_out']['predictions']
    if len({p['battle_id'] for p in predictions}) != len(predictions):
        raise ValueError('Duplicate saved forecasts')
    if {p['battle_id'] for p in predictions} != {e['battle_id'] for e in data['entries'] if e['eligible']}:
        raise ValueError('Saved forecasts and eligible pairs differ')
    rows = []
    for p in predictions:
        e = entries[p['battle_id']]; f = frame[p['battle_id']]
        probability = p['force']; y = p['y']
        if (y not in (0, 1) or y != f['outcome_side_a'] or not math.isfinite(probability)
                or not 0 <= probability <= 1 or p['held_out_group'] != e['campaign_group']):
            raise ValueError('Invalid held-out probability, outcome or campaign')
        winner, other = ('A', 'B') if y else ('B', 'A')
        a, b = e['sides'][winner]['primary_value'], e['sides'][other]['primary_value']
        if not all(type(n) in (int, float) and math.isfinite(n) and n > 0 for n in (a, b)):
            raise ValueError('A surprise card requires both reported personnel totals')
        winner_probability = probability if y else 1 - probability
        nation_names = lambda key: ' + '.join(NATIONS.get(n, n) for n in f[key]) or 'Not named'
        rows.append({'battle_id': p['battle_id'], 'place': e['place'], 'date': e['start_date'],
                     'campaign': e['campaign_group'], 'winner_side': winner,
                     'winner': nation_names('winner_nations'), 'other': nation_names('loser_nations'),
                     'winner_commander': f['winner_commander_text'] or 'Not named',
                     'other_commander': f['loser_commander_text'] or 'Not named',
                     'winner_troops': a, 'other_troops': b, 'winner_probability': winner_probability,
                     'surprise': 1 - winner_probability, 'opponent_ratio': b / a,
                     'a_probability': probability, 'approximate': any(e['sides'][s]['approximate'] for s in ('A', 'B')),
                     'source': e})
    return sorted(rows, key=lambda r: (-r['surprise'], r['date'], r['battle_id']))


class SurprisePages:
    def __init__(self, napoleonic):
        self.nap = napoleonic; self.site = napoleonic.site
        self.rows = load_rows(self.site.root, self.nap.entries) if all(
            (self.site.root / p).is_file() for p in (RUN, DATA)) else []
        self.ids = {r['battle_id'] for r in self.rows}

    def card(self, row):
        from .site import esc
        r = row; bid = r['battle_id']; source = r['source']
        chance = r['winner_probability'] * 100
        share = 100 * r['winner_troops'] / (r['winner_troops'] + r['other_troops'])
        ratio = r['opponent_ratio']
        balance = f'Outnumbered {ratio:.1f}:1' if ratio > 1 else (
            'Equal reported totals' if ratio == 1 else f'{1 / ratio:.1f}× as many troops')
        search = ' '.join(str(r[k]) for k in ('battle_id', 'place', 'date', 'campaign', 'winner', 'other',
                                             'winner_commander', 'other_commander'))
        data_attrs = (f'data-battle="{bid}" data-search="{esc(search)}" data-campaign="{esc(r["campaign"])}" '
                      f'data-surprise="{r["surprise"]:.17g}" data-ratio="{ratio:.17g}"')
        labels = '<span class="sx-tag">Model upset</span>' if chance < 50 else ''
        if r['approximate']:
            labels += '<span class="sx-tag">Approximate source figure</span>'
        return (f'<article class="sx-battle" id="battle-{bid}" {data_attrs} tabindex="-1">'
                '<div class="sx-card-heading"><div>'
                f'<p class="sx-meta">{esc(r["date"])} · {esc(r["campaign"])}</p>'
                f'<h2><a href="engagements/{bid}.html">{esc(r["place"])}</a></h2>'
                f'<p class="sx-result">Recorded winner: <strong>{esc(r["winner"])}</strong> '
                f'<span class="muted">(side {r["winner_side"]})</span></p></div>'
                f'<div class="sx-estimate"><span class="sx-chance">{chance:.0f}%</span>'
                '<span>Model estimate<br>for the recorded winner</span></div></div>'
                f'<div class="sx-tags">{labels}<span class="sx-balance">{balance}</span></div>'
                '<div class="sx-force-labels"><div><span>Winner · ' + esc(r['winner']) + '</span>'
                f'<strong>{r["winner_troops"]:,.0f}</strong></div><div><span>Other side · {esc(r["other"])}</span>'
                f'<strong>{r["other_troops"]:,.0f}</strong></div></div>'
                f'<div class="sx-force-bar" aria-hidden="true"><span style="width:{share:.6f}%"></span></div>'
                '<p class="sx-troop-note">Reported personnel totals in Bodart</p>'
                f'<div class="sx-card-links"><a href="engagements/{bid}.html#dimension-strength">Battle evidence →</a>'
                f'<a href="surprises.html?q={bid}#battle-{bid}">Link to this battle</a></div>'
                '<details class="sx-detail"><summary>Numbers &amp; source</summary><div>'
                f'<p>The saved model put side A (France and allies) at {r["a_probability"]:.1%}. '
                f'Bodart records side {r["winner_side"]} as the winner, giving the recorded winner a model estimate '
                f'of {r["winner_probability"]:.1%}. Lower estimates appear first in “Model surprises.” '
                'The model was fitted without this engagement’s entire campaign group.</p>'
                f'<p>Printed names: <strong>{esc(r["winner_commander"])}</strong> (winning side); '
                f'<strong>{esc(r["other_commander"])}</strong> (other side). Names provide context; '
                'the surprise is assigned to the engagement, with no commander score.</p>'
                + ''.join('<p><strong>Side ' + side + ' — printed strength:</strong> '
                          + esc(source['sides'][side]['printed']) + '</p>' for side in ('A', 'B'))
                + '<p>Source: <a href="../sources.html#bodart-1908-transcription-v1">Bodart (1908)</a>, '
                + esc(source['sides']['A']['citations'][0]['locator']) + '. '
                + f'<a href="{self.site.blob(DATA)}">Frozen extract</a> · '
                + f'<a href="{self.site.blob(RUN)}">Saved predictions</a> · '
                + f'<a href="engagements/{bid}.html#dimension-outcome">Outcome passages and disputes</a></p>'
                + '</div></details></article>')

    def build(self):
        if not self.rows:
            return
        from .site import esc
        count = len(self.rows)
        data = read_json(self.site.root / DATA)
        total = len(data['entries']); missing = total - count
        outnumbered = sum(r['opponent_ratio'] > 1 for r in self.rows)
        options = ''.join(f'<option value="{esc(g)}">{esc(g)}</option>' for g in sorted({r['campaign'] for r in self.rows}))
        body = ('<div class="sx-shell"><p class="sx-kicker">Napoleonic surprise explorer · 1805–1813</p>'
                '<h1 class="sx-title">When troop numbers<br> didn’t tell the story.</h1>'
                '<p class="sx-intro">A small model, a lot of history. Explore battles whose recorded results '
                'surprised a troop-strength model—or victories won with fewer reported troops.</p>'
                '<p class="sx-caution">These are model surprises, not measures of a commander’s skill. '
                'Terrain, tactics, source errors and much else sit outside this simple model.</p>'
                f'<div class="sx-stats"><span><strong>{count}</strong> scored engagements</span>'
                f'<span><strong>{len({r["campaign"] for r in self.rows})}</strong> campaign groups</span>'
                f'<span><strong>{outnumbered}</strong> outnumbered victories</span></div>'
                '<form id="sx-controls" class="sx-controls" hidden role="search" aria-label="Filter battles">'
                '<div class="sx-modes" role="group" aria-label="Browse by">'
                '<button type="button" data-mode="surprise" aria-pressed="true">Model surprises</button>'
                '<button type="button" data-mode="outnumbered" aria-pressed="false">Outnumbered victories</button></div>'
                '<details id="sx-filter-fields" class="sx-filter-fields" open><summary>Search or filter battles</summary>'
                '<div class="sx-fields"><label>Find a battle or name<input id="sx-search" type="search" '
                'placeholder="Try Busaco, 1812, or Wellington…" autocomplete="off"></label>'
                f'<label>Campaign<select id="sx-campaign"><option value="">All campaigns</option>{options}</select></label></div></details>'
                '<div class="sx-actions"><button type="button" id="sx-pick">Pick a battle ↗</button>'
                '<button type="button" id="sx-share">Copy view link</button>'
                '<button type="reset" class="sx-reset">Clear filters</button>'
                '<span id="sx-feedback" role="status"></span></div></form>'
                '<div class="sx-list-heading" id="battles"><h2 id="sx-list-title">Biggest model surprises</h2>'
                f'<p id="sx-count" role="status" aria-live="polite">{count} engagements</p></div>'
                '<p id="sx-order-note" class="muted">Sorted by the model’s estimate for the recorded winner, lowest first.</p>'
                '<noscript><p>JavaScript is off: all scored engagements are listed below in model-surprise order. '
                'Evidence links and source details work without it.</p></noscript>'
                '<div id="sx-empty" class="card" hidden><h3>No matching battles</h3>'
                '<p>Try another spelling or clear the filters.</p></div>'
                '<div id="sx-list">' + ''.join(self.card(r) for r in self.rows) + '</div>'
                '<button id="sx-more" class="sx-more" type="button" hidden>Show 20 more</button>'
                '<details class="sx-method"><summary>How to read this explorer</summary>'
                '<p>“Model surprises” sorts by 1 minus the saved model estimate for the recorded winner. '
                '“Outnumbered victories” keeps winners with fewer reported troops, sorted by the opposing-to-winning '
                'personnel ratio, largest first. They answer different questions: a model upset need not be an outnumbered victory.</p>'
                '<p>The original model uses the balance of the two compiler-reported personnel totals, plus an intercept, '
                'to predict Bodart’s recorded A-side winner. These are the primary saved campaign-held-out predictions. '
                'They describe source records; they are not validated historical win probabilities or an explanation '
                'of why a battle was won. Rounded percentages are for reading; ordering uses the saved precision.</p>'
                f'<p>Coverage: {count}/{total} development engagements; {missing} lack an eligible pair of totals. '
                'Those missing figures are not zeroes. The 52 entries reserved for final evaluation are not scored here. '
                'Reported figures may cover different populations and times. Approximation flags and original strength '
                'labels remain in each card; full qualifiers and eligibility reasons are in the frozen extract.</p>'
                '<p>Bodart’s selection and winner coding can depend on strength. The original forward check to 1813 '
                'is weak and sensitivity-dependent. A surprising result can reflect missing context or coding; '
                'it does not establish extraordinary command performance.</p>'
                f'<p><a href="{self.site.blob(REPORT)}">Read the benchmark report</a> · '
                f'<a href="{self.site.blob(DATA)}">All 273 extracts and exclusions</a> · '
                f'<a href="{self.site.blob(RUN)}">Exact saved forecasts</a></p></details>'
                '<p class="sx-return"><a href="index.html">← Napoleonic evidence explorer</a></p></div>')
        (self.site.out / 'napoleonic/surprises.css').write_text(CSS, encoding='utf-8')
        (self.site.out / 'napoleonic/surprises.js').write_text(JS, encoding='utf-8')
        self.site.write('napoleonic/surprises.html', 'Biggest surprises · Napoleonic Wars', body, 1,
                        styles=('napoleonic/surprises.css',), scripts=('napoleonic/surprises.js',))


CSS = """
.sx-shell { --sx-winner: #246a76; --sx-other: #bac6cc; --sx-wash: #eef4f4; --sx-pop: #91502d;
  max-width: 920px; margin: 16px auto 0; }
.sx-kicker { text-transform: uppercase; letter-spacing: .13em; font-size: .76rem; font-weight: 700; color: var(--accent); }
.sx-title { font: 600 clamp(2.1rem, 5vw, 3.8rem)/1.06 Georgia, serif; letter-spacing: -.035em; margin: 24px 0 20px; }
.sx-intro { max-width: 690px; font-size: 1.1rem; line-height: 1.6; }
.sx-caution { max-width: 700px; font-size: .88rem; color: var(--muted); }
.sx-stats { display: flex; flex-wrap: wrap; gap: 12px 30px; padding: 18px 0; margin: 14px 0 20px; border-block: 1px solid var(--line); font-size: .85rem; color: var(--muted); }
.sx-stats strong { color: var(--fg); font-size: 1.25rem; padding-right: 4px; font-variant-numeric: tabular-nums; }
.sx-controls { background: var(--card); border: 1px solid var(--line); padding: 18px; border-radius: 10px; }
.sx-shell button, .sx-shell input, .sx-shell select { font: inherit; color: var(--fg); background: var(--card); border: 1px solid var(--line); border-radius: 6px; min-height: 44px; }
.sx-shell button { cursor: pointer; padding: 9px 14px; }
.sx-shell button:hover { border-color: var(--accent); }
.sx-shell button:focus-visible, .sx-shell input:focus-visible, .sx-shell select:focus-visible, .sx-shell a:focus-visible, .sx-shell summary:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }
.sx-modes { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px; }
.sx-modes button { font-size: .9rem; }
.sx-modes button[aria-pressed="true"] { color: var(--card); background: var(--fg); border-color: var(--fg); }
.sx-fields { display: grid; grid-template-columns: 1.5fr 1fr; gap: 14px; }
.sx-filter-fields > summary { display: none; cursor: pointer; min-height: 44px; padding: 10px 0; font-size: .86rem; }
.sx-fields label { display: grid; gap: 6px; font-size: .8rem; font-weight: 600; min-width: 0; }
.sx-fields input, .sx-fields select { width: 100%; min-width: 0; padding: 8px 10px; font-size: .95rem; font-weight: 400; }
.sx-actions { display: flex; align-items: center; flex-wrap: wrap; gap: 8px; margin-top: 14px; }
.sx-actions button { font-size: .82rem; }
.sx-actions #sx-pick { background: var(--sx-wash); border-color: var(--sx-winner); }
.sx-actions .sx-reset { border-color: transparent; color: var(--muted); }
#sx-feedback { font-size: .8rem; color: var(--muted); }
.sx-list-heading { display: flex; justify-content: space-between; align-items: baseline; gap: 10px; margin-top: 32px; }
.sx-list-heading h2 { margin: 0; font-size: 1.2rem; }
.sx-list-heading p { margin: 0; font-size: .85rem; color: var(--muted); }
#sx-order-note { font-size: .83rem; margin: 7px 0 18px; }
.sx-battle { padding: 24px; background: var(--card); border: 1px solid var(--line); border-radius: 10px; margin: 16px 0; }
.sx-battle:target, .sx-battle.sx-picked { outline: 3px solid var(--accent); outline-offset: 3px; scroll-margin-top: 20px; }
.sx-battle[hidden], .sx-shell [hidden] { display: none !important; }
.sx-card-heading { display: grid; grid-template-columns: 1fr auto; gap: 16px; }
.sx-meta { color: var(--muted); font-size: .78rem; margin: 0 0 8px; }
.sx-card-heading h2 { margin: 0; font-size: 1.65rem; line-height: 1.15; font-family: Georgia, serif; }
.sx-card-heading h2 a { color: var(--fg); text-decoration-thickness: 1px; text-underline-offset: 5px; }
.sx-result { font-size: .88rem; margin: 10px 0 0; }
.sx-estimate { display: flex; flex-direction: column; align-items: flex-end; font-size: .72rem; text-align: right; color: var(--muted); line-height: 1.3; }
.sx-chance { font: 600 2.5rem/1.1 Georgia, serif; color: var(--sx-pop); font-variant-numeric: tabular-nums; margin-bottom: 5px; }
.sx-tags { display: flex; align-items: baseline; gap: 7px 12px; flex-wrap: wrap; margin: 18px 0; font-size: .78rem; }
.sx-tag { border: 1px solid var(--line); border-radius: 20px; padding: 3px 9px; color: var(--muted); }
.sx-balance { color: var(--sx-winner); font-weight: 600; }
.sx-force-labels { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; font-size: .78rem; }
.sx-force-labels div { display: flex; flex-direction: column; min-width: 0; }
.sx-force-labels div:last-child { text-align: right; }
.sx-force-labels span { color: var(--muted); }
.sx-force-labels strong { font-size: 1.1rem; margin: 3px 0 7px; font-variant-numeric: tabular-nums; }
.sx-force-bar { width: 100%; height: 12px; background: var(--sx-other); border-radius: 3px; overflow: hidden; }
.sx-force-bar span { display: block; height: 100%; background: var(--sx-winner); }
.sx-troop-note { color: var(--muted); margin: 6px 0 18px; font-size: .73rem; }
.sx-card-links { display: flex; flex-wrap: wrap; gap: 8px 20px; font-size: .86rem; }
.sx-card-links a { padding: 6px 0; }
.sx-detail { margin-top: 16px; border-top: 1px solid var(--line); font-size: .85rem; overflow-wrap: anywhere; }
.sx-detail summary, .sx-method summary { cursor: pointer; padding: 12px 0; min-height: 44px; }
.sx-detail > div { padding: 0 4px; }
.sx-more { display: block; width: 100%; margin: 20px 0 32px; }
.sx-method { border-block: 1px solid var(--line); margin: 30px 0; padding: 4px 0; font-size: .9rem; }
.sx-method summary { font-weight: 600; }
.sx-return { font-size: .9rem; }
@media (prefers-color-scheme: dark) { .sx-shell { --sx-winner: #8bc3ce; --sx-other: #48555e; --sx-wash: #283d43; --sx-pop: #e4b18d; } }
@media (max-width: 600px) {
  .sx-shell { margin-top: 4px; }
  .sx-title { margin-top: 16px; font-size: 1.85rem; }
  .sx-title br { display: none; }
  .sx-intro { font-size: .95rem; }
  .sx-caution { font-size: .78rem; line-height: 1.45; }
  .sx-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; font-size: .72rem; padding: 12px 0; margin-bottom: 16px; }
  .sx-stats strong { display: block; font-size: 1.1rem; }
  .sx-controls { padding: 12px; }
  .sx-fields { grid-template-columns: 1fr; gap: 10px; }
  .sx-filter-fields > summary { display: list-item; }
  .sx-filter-fields .sx-fields { padding-bottom: 10px; }
  .sx-modes { gap: 6px; margin-bottom: 12px; }
  .sx-modes button { flex: 1; padding: 8px; font-size: .81rem; }
  .sx-actions { gap: 4px; }
  .sx-actions button { padding: 8px; font-size: .76rem; }
  .sx-list-heading { align-items: flex-start; flex-direction: column; gap: 4px; margin-top: 24px; }
  .sx-battle { padding: 17px; }
  .sx-card-heading { gap: 9px; }
  .sx-card-heading h2 { font-size: 1.45rem; }
  .sx-chance { font-size: 2rem; }
  .sx-estimate { font-size: .66rem; max-width: 100px; }
  .sx-meta { font-size: .72rem; }
}
"""


JS = r"""
(() => {
  'use strict';
  const form = document.getElementById('sx-controls');
  const list = document.getElementById('sx-list');
  const cards = Array.from(list.querySelectorAll('.sx-battle'));
  const search = document.getElementById('sx-search');
  const campaign = document.getElementById('sx-campaign');
  const modes = Array.from(form.querySelectorAll('[data-mode]'));
  const more = document.getElementById('sx-more');
  const feedback = document.getElementById('sx-feedback');
  let mode = 'surprise', limit = 20, matches = [];
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase().replace(/ß/g, 'ss');
  const queryMatches = (card, tokens) => {
    const text = normalize(card.dataset.search);
    return tokens.every(token => text.includes(token));
  };
  function render() {
    const tokens = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
    matches = cards.filter(card => (!campaign.value || card.dataset.campaign === campaign.value)
      && (mode !== 'outnumbered' || Number(card.dataset.ratio) > 1) && queryMatches(card, tokens));
    matches.sort((a, b) => {
      const key = mode === 'outnumbered' ? 'ratio' : 'surprise';
      return Number(b.dataset[key]) - Number(a.dataset[key]) || cards.indexOf(a) - cards.indexOf(b);
    });
    const target = location.hash.startsWith('#battle-') ? document.getElementById(location.hash.slice(1)) : null;
    if (target && matches.includes(target)) limit = Math.max(limit, Math.ceil((matches.indexOf(target) + 1) / 20) * 20);
    cards.forEach(card => { card.hidden = true; });
    const batch = document.createDocumentFragment();
    matches.forEach((card, i) => { card.hidden = i >= limit; batch.appendChild(card); });
    list.appendChild(batch);
    document.getElementById('sx-empty').hidden = matches.length !== 0;
    document.getElementById('sx-count').textContent = `${Math.min(limit, matches.length)} of ${matches.length} matches · ${cards.length} scored`;
    document.getElementById('sx-list-title').textContent = mode === 'outnumbered' ? 'Victories against larger reported forces' : 'Biggest model surprises';
    document.getElementById('sx-order-note').textContent = mode === 'outnumbered'
      ? 'Sorted by opposing-to-winning personnel ratio, largest first. Only winners with fewer reported troops are shown.'
      : 'Sorted by the model’s estimate for the recorded winner, lowest first.';
    modes.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.mode === mode)));
    more.hidden = matches.length <= limit;
    more.textContent = `Show ${Math.min(20, Math.max(0, matches.length - limit))} more`;
    document.getElementById('sx-pick').disabled = matches.length === 0;
  }
  function save(push = false) {
    const url = new URL(location.href);
    ['q', 'campaign', 'mode'].forEach(key => url.searchParams.delete(key));
    if (search.value.trim()) url.searchParams.set('q', search.value.trim());
    if (campaign.value) url.searchParams.set('campaign', campaign.value);
    if (mode !== 'surprise') url.searchParams.set('mode', mode);
    url.hash = '';
    const next = url.pathname + url.search;
    if (next !== location.pathname + location.search + location.hash) history[push ? 'pushState' : 'replaceState']({}, '', next);
  }
  function update(push = false) {
    limit = 20; feedback.textContent = '';
    cards.forEach(card => card.classList.remove('sx-picked'));
    save(push); render();
  }
  function restore() {
    const params = new URLSearchParams(location.search);
    feedback.textContent = '';
    cards.forEach(card => card.classList.toggle('sx-picked', '#' + card.id === location.hash));
    search.value = params.get('q') || '';
    campaign.value = Array.from(campaign.options).some(o => o.value === params.get('campaign')) ? params.get('campaign') : '';
    mode = params.get('mode') === 'outnumbered' ? 'outnumbered' : 'surprise';
    document.getElementById('sx-filter-fields').open = !matchMedia('(max-width: 600px)').matches || Boolean(search.value || campaign.value);
    limit = 20; render();
  }
  form.hidden = false;
  form.addEventListener('submit', event => { event.preventDefault(); update(true); });
  form.addEventListener('reset', event => { event.preventDefault(); search.value = ''; campaign.value = ''; mode = 'surprise'; update(true); });
  search.addEventListener('input', () => update());
  campaign.addEventListener('change', () => update(true));
  modes.forEach(button => button.addEventListener('click', () => { mode = button.dataset.mode; update(true); }));
  more.addEventListener('click', () => {
    const next = matches[limit]; limit += 20; render();
    if (next) next.focus({preventScroll: true});
  });
  document.getElementById('sx-pick').addEventListener('click', () => {
    const card = matches[Math.floor(Math.random() * matches.length)];
    if (!card) return;
    cards.forEach(c => c.classList.remove('sx-picked'));
    history.pushState({}, '', location.pathname + location.search + '#' + card.id);
    render(); card.classList.add('sx-picked');
    card.querySelector('details').open = true;
    card.focus({preventScroll: true});
    card.scrollIntoView({behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth', block: 'start'});
    feedback.textContent = 'Picked ' + card.querySelector('h2').textContent + '.';
  });
  document.getElementById('sx-share').addEventListener('click', async () => {
    try { await navigator.clipboard.writeText(location.href); feedback.textContent = 'View link copied.'; }
    catch { feedback.textContent = 'Copy this view’s link from your browser’s address bar.'; }
  });
  addEventListener('popstate', restore);
  matchMedia('(max-width: 600px)').addEventListener('change', event => {
    document.getElementById('sx-filter-fields').open = !event.matches || Boolean(search.value || campaign.value);
  });
  addEventListener('hashchange', restore);
  restore();
})();
"""
