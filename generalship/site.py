"""A static explorer of the evidence and the ratings (roadmap Milestone 4), standard library only.

`python3 -m generalship site --out _site` writes plain HTML pages that trace a commander to their
engagements, an engagement to its ledger entries and dossier claims, and a claim to its quoted passage,
the registered source and the snapshot's SHA-256. Campaigns, sources and the committed reports are
included. The pages only present committed files: nothing here changes evidence, ledgers or results.
Snapshots and documents are linked on GitHub at the build's commit.
"""

from collections import Counter, defaultdict
import html
from pathlib import Path
import posixpath
import re
import shutil

from .sources import read_csv, read_json

REPOSITORY = 'https://github.com/masonpetrosky/generalship'
COHORT = 'data/pilot/cohort-v2.json'
STRENGTH = 'data/estimates/side-strength-v3.json'
COMMAND = 'data/command/responsibility-v2.json'
REGISTRY = 'data/command/commanders-v2.json'
RUNS = ('artifacts/commander-ratings-v4', 'artifacts/commander-ratings-v3')  # the newest present run is shown
REPORTS = (('README.md', 'Overview'),
           ('docs/research/commander-ratings-v4.md', 'Rating run 4: memo'),
           ('artifacts/commander-ratings-v4.md', 'Rating run 4: report'),
           ('docs/commander-ratings-v4.md', 'Rating run 4: design'),
           ('docs/research/commander-ratings-v3.md', 'Rating run 3: memo'),
           ('artifacts/commander-ratings-v3.md', 'Rating run 3: report'),
           ('artifacts/commander-ratings-v3-uncertainty.md', 'Rating run 3: how sure is the verdict?'),
           ('docs/extraction-audit.md', 'Extraction audit'),
           ('docs/methodology.md', 'Methodology'),
           ('docs/evidence-contract.md', 'Evidence contract'),
           ('docs/roadmap.md', 'Roadmap'))
SIDES = ('US', 'Confederate')
CSS = """
:root { --fg: #1d232b; --muted: #5b6573; --bg: #fbfbf9; --card: #ffffff; --line: #dfe2e6; --accent: #1f5f99;
        --quote: #f2f4f7; }
@media (prefers-color-scheme: dark) {
  :root { --fg: #e4e7eb; --muted: #9aa4b1; --bg: #15181c; --card: #1c2026; --line: #2f353d; --accent: #7fb3e6;
          --quote: #222831; } }
* { box-sizing: border-box; }
body { margin: 0; font: 16px/1.55 system-ui, -apple-system, "Segoe UI", sans-serif; color: var(--fg); background: var(--bg); }
header { border-bottom: 1px solid var(--line); background: var(--card); }
nav, main, footer { max-width: 1100px; margin: 0 auto; padding: 0 16px; }
nav { display: flex; flex-wrap: wrap; gap: 4px 18px; padding-top: 12px; padding-bottom: 12px; }
nav a { color: var(--fg); text-decoration: none; } nav a.brand { font-weight: 700; }
main { padding-top: 16px; padding-bottom: 40px; }
a { color: var(--accent); }
h1 { font-size: 1.6rem; line-height: 1.25; } h2 { font-size: 1.25rem; margin-top: 2rem; } h3 { font-size: 1.05rem; }
.muted, footer { color: var(--muted); } footer { font-size: .85rem; padding-top: 16px; padding-bottom: 32px; border-top: 1px solid var(--line); }
.table { overflow-x: auto; } table { border-collapse: collapse; width: 100%; font-size: .92rem; }
th, td { border-bottom: 1px solid var(--line); padding: 6px 8px; text-align: left; vertical-align: top; }
th { font-weight: 600; } td.n, th.n { text-align: right; font-variant-numeric: tabular-nums; }
blockquote { margin: 6px 0; padding: 6px 12px; background: var(--quote); border-left: 3px solid var(--line); }
code { font-size: .88em; overflow-wrap: anywhere; } .card { background: var(--card); border: 1px solid var(--line); border-radius: 6px; padding: 12px 16px; margin: 12px 0; }
.label { display: inline-block; font-size: .78rem; padding: 0 6px; margin: 1px 2px 1px 0; border: 1px solid var(--line); border-radius: 10px; color: var(--muted); }
.claim { border-top: 1px solid var(--line); padding: 10px 0; } .cite { font-size: .9rem; margin: 6px 0 10px; }
"""


def esc(x):
    return html.escape('' if x is None else str(x))


def slug(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def heading_id(text):
    """The anchor GitHub gives a Markdown heading, so links written for GitHub also work here."""
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text).replace('`', '').replace('*', '')
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')


def labels(xs):
    return ''.join(f'<span class="label">{esc(x)}</span>' for x in xs)


def num(x):
    return f'{x:,}' if isinstance(x, int) else esc(x)


def table(head, rows, numeric=()):
    th = ''.join(f'<th{" class=n" if i in numeric else ""}>{h}</th>' for i, h in enumerate(head))
    body = ''.join('<tr>' + ''.join(f'<td{" class=n" if i in numeric else ""}>{c}</td>' for i, c in enumerate(r)) + '</tr>'
                   for r in rows)
    return f'<div class="table"><table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


# ---------- a small Markdown renderer for the project's own documents ----------

def _inline(text, link):
    out, pos = [], 0
    for m in re.finditer(r'`([^`]+)`|\[([^\]]+)\]\(([^)\s]+)\)|\*\*([^*]+)\*\*|\*([^*\s][^*]*)\*', text):
        out.append(esc(text[pos:m.start()]))
        if m.group(1) is not None:
            out.append(f'<code>{esc(m.group(1))}</code>')
        elif m.group(2) is not None:
            out.append(f'<a href="{esc(link(m.group(3)))}">{_inline(m.group(2), link)}</a>')
        elif m.group(4) is not None:
            out.append(f'<strong>{_inline(m.group(4), link)}</strong>')
        else:
            out.append(f'<em>{_inline(m.group(5), link)}</em>')
        pos = m.end()
    return ''.join(out) + esc(text[pos:])


def markdown(text, link):
    """Headings, paragraphs, nested lists, tables, block quotes and fenced code; enough for this repository's docs."""
    lines, out, i = text.split('\n'), [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif line.startswith('```'):
            j = i + 1
            while j < len(lines) and not lines[j].startswith('```'):
                j += 1
            out.append('<pre><code>' + esc('\n'.join(lines[i + 1:j])) + '</code></pre>')
            i = j + 1
        elif m := re.match(r'(#{1,6})\s+(.*)', line):
            n = len(m.group(1))
            out.append(f'<h{n} id="{heading_id(m.group(2))}">{_inline(m.group(2), link)}</h{n}>')
            i += 1
        elif line.lstrip().startswith('|'):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            body = [r for r in rows[1:] if not all(re.fullmatch(r':?-{3,}:?', c) for c in r)]
            right = [c.endswith(':') and not c.startswith(':') for c in rows[1]] if len(rows) > 1 else []
            out.append(table([_inline(c, link) for c in rows[0]], [[_inline(c, link) for c in r] for r in body],
                             {k for k, v in enumerate(right) if v}))
        elif line.startswith('>'):
            block = []
            while i < len(lines) and lines[i].startswith('>'):
                block.append(lines[i][1:].lstrip())
                i += 1
            out.append('<blockquote>' + markdown('\n'.join(block), link) + '</blockquote>')
        elif re.match(r'\s*([-*]|\d+\.)\s', line):
            block = []
            while i < len(lines) and (re.match(r'\s*([-*]|\d+\.)\s', lines[i]) or (lines[i].startswith('  ') and lines[i].strip())):
                block.append(lines[i])
                i += 1
            out.append(_list(block, link))
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r'(#{1,6}\s|```|\s*\||>|\s*([-*]|\d+\.)\s)', lines[i]):
                para.append(lines[i].strip())
                i += 1
            out.append('<p>' + _inline(' '.join(para), link) + '</p>')
    return '\n'.join(out)


def _list(block, link):
    indent = len(block[0]) - len(block[0].lstrip())
    tag = 'ol' if re.match(r'\s*\d+\.', block[0]) else 'ul'
    items = []
    for line in block:
        lead = len(line) - len(line.lstrip())
        if lead == indent and re.match(r'\s*([-*]|\d+\.)\s', line):
            items.append([re.sub(r'^\s*([-*]|\d+\.)\s+', '', line)])
        else:
            items[-1].append(line)
    out = []
    for item in items:
        text, rest = [item[0]], []
        for line in item[1:]:
            (rest if rest or re.match(r'\s*([-*]|\d+\.)\s', line) else text).append(line)
        inner = _inline(' '.join(t.strip() for t in text), link)
        if rest:
            inner += _list(rest, link) if re.match(r'\s*([-*]|\d+\.)\s', rest[0]) else '<p>' + _inline(' '.join(r.strip() for r in rest), link) + '</p>'
        out.append(f'<li>{inner}</li>')
    return f'<{tag}>' + ''.join(out) + f'</{tag}>'


# ---------- the site ----------

class Site:
    def __init__(self, root, out, commit):
        self.root, self.out, self.commit = Path(root), Path(out), commit
        self.battles = {r['battle']: r for r in read_csv(self.root / 'data/raw/cwsac_battles.csv')}
        self.campaigns = {r['campaign']: r for r in read_csv(self.root / 'data/raw/cwsac_campaigns.csv')}
        self.cohort = read_json(self.root / COHORT)['battle_ids']
        self.sources = {s['id']: s for s in read_json(self.root / 'data/sources.json')['sources']}
        self.strength = {e['battle_id']: e for e in read_json(self.root / STRENGTH)['engagements']}
        command = read_json(self.root / COMMAND)
        self.command = {e['battle_id']: e for e in command['engagements']}
        self.nesting = command['nesting']
        self.registry = {c['id']: c for c in read_json(self.root / REGISTRY)['commanders']}
        self.dossiers = {b: read_json(p) for b in self.cohort if (p := self.root / f'data/evidence/{b}.json').is_file()}
        self.run_path = next((p for p in RUNS if (self.root / f'{p}.json').is_file()), None)
        self.run = read_json(self.root / f'{self.run_path}.json') if self.run_path else None
        self.by_campaign = defaultdict(list)
        for b in self.cohort:
            self.by_campaign[self.battles[b]['campaign']].append(b)
        self.attributed, self.named = defaultdict(list), defaultdict(list)
        for b, e in self.command.items():
            for s in SIDES:
                side = e['sides'][s]
                if side['commander_id']:
                    self.attributed[side['commander_id']].append((b, s))
                for role, ids in (('candidate', side['candidates']), ('successor', [side['successor']]),
                                  ('superior directing', [side.get('superior')])):
                    for c in ids:
                        if c and c != side['commander_id']:
                            self.named[c].append((b, s, role))
        self.reports = [(p, t) for p, t in REPORTS if (self.root / p).is_file()]
        self.pages = 0

    # links
    def blob(self, path):
        return f'{REPOSITORY}/blob/{self.commit}/{path}'

    def doc_link(self, source_path):
        """Resolve a link in a rendered document: reports become site pages, other repository paths GitHub pages."""
        def link(target):
            if re.match(r'[a-z]+:', target) or target.startswith('#'):
                return target
            path, _, frag = target.partition('#')
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source_path), path))
            for p, _ in self.reports:
                if p == resolved:
                    return f'../results/{self.report_name(p)}.html' + (f'#{frag}' if frag else '')
            return self.blob(resolved) + (f'#{frag}' if frag else '')
        return link

    @staticmethod
    def report_name(path):
        return slug(path.rsplit('.', 1)[0])

    def write(self, rel, title, body, depth):
        up = '../' * depth
        nav = (f'<a class="brand" href="{up}index.html">Generalship</a><a href="{up}commanders/index.html">Commanders</a>'
               f'<a href="{up}campaigns/index.html">Campaigns</a><a href="{up}engagements/index.html">Engagements</a>'
               f'<a href="{up}sources.html">Sources</a><a href="{up}results/index.html">Results</a><a href="{REPOSITORY}">GitHub</a>')
        page = (f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
                f'<meta name="viewport" content="width=device-width, initial-scale=1">'
                f'<title>{esc(title)} · Generalship</title><link rel="stylesheet" href="{up}style.css"></head>'
                f'<body><header><nav>{nav}</nav></header><main>{body}</main>'
                f'<footer>Built from commit <a href="{REPOSITORY}/tree/{esc(self.commit)}"><code>{esc(self.commit[:12])}</code></a>. '
                'Exploratory research: no rating here is a measure of skill, a causal effect or a ranking of record. '
                'Every claim links to its quoted passage and pinned source.</footer></body></html>\n')
        path = self.out / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(page, encoding='utf-8')
        self.pages += 1

    def citation(self, c, up):
        src = self.sources.get(c['source_id'], {})
        where = c.get('locator') or (', '.join(f'{k} {v}' for k, v in c['row_key'].items()) + f"; column {c['column']}"
                                     if c.get('row_key') else '')
        snap = (f' · <a href="{esc(self.blob(src["path"]))}">snapshot</a> <code>{esc(src["sha256"][:12])}…</code>'
                if src.get('path') else '')
        return (f'<div class="cite"><blockquote>{esc(c.get("quote"))}</blockquote>'
                f'<a href="{up}sources.html#{esc(c["source_id"])}">{esc(c["source_id"])}</a>'
                f'{", " + esc(where) if where else ""}{snap}</div>')

    def input_ref(self, inp, up):
        ref = inp.get('ref') or {}
        if 'citation' in ref:
            return self.citation(ref['citation'], up)
        if 'dossier' in ref:
            claim = ref['dossier']['claim_id']
            return f'<a href="#claim-{esc(claim)}">dossier claim {esc(claim)}</a>'
        kinds = ', '.join(a['kind'] for a in inp['adjustments'])
        return f'<span class="muted">derived ({esc(kinds or "no passage")}): {esc(inp.get("note"))}</span>'

    def battle_link(self, b, up):
        return f'<a href="{up}engagements/{b}.html">{esc(self.battles[b]["battle_name"])}</a> <span class="muted">{b}</span>'

    def commander_link(self, c, up):
        return f'<a href="{up}commanders/{esc(c)}.html">{esc(self.registry[c]["name"])}</a>' if c else '<span class="muted">none</span>'

    def campaign_link(self, name, up):
        return f'<a href="{up}campaigns/{slug(name)}.html">{esc(name)}</a>'

    # pages
    def build(self):
        if self.out.exists():
            shutil.rmtree(self.out)
        self.out.mkdir(parents=True)
        (self.out / 'style.css').write_text(CSS.lstrip(), encoding='utf-8')
        (self.out / '.nojekyll').write_text('', encoding='utf-8')
        self.home()
        self.results()
        self.commanders()
        self.campaign_pages()
        self.engagements()
        self.source_page()
        return {'pages': self.pages, 'output': str(self.out), 'commit': self.commit, 'run': self.run_path}

    def verdict_box(self, up):
        if not self.run:
            return ''
        if self.run.get('run_version') == 4:
            v = self.run['verdict']
            text = ('lower held-out log loss than the context model, beyond campaign-resampling noise, under both weightings'
                    if v['improved'] else 'no improvement over the context model under the pre-registered rule; no ordered ranking is given')
        else:
            text = 'lower held-out log loss under both weightings' if self.run['heldout_test']['improved'] else 'no held-out improvement'
        name = self.run_path.rsplit('/', 1)[-1]
        return (f'<div class="card"><strong>Latest rating run ({self.run.get("run_version")}):</strong> {esc(text)}. '
                f'<a href="{up}results/{self.report_name(self.run_path + ".md")}.html">Report</a> · '
                f'<a href="{esc(self.blob(self.run_path + ".json"))}">{esc(name)}.json</a></div>')

    def home(self):
        claims = sum(len(d['claims']) for d in self.dossiers.values())
        cites = sum(len(c['citations']) for d in self.dossiers.values() for c in d['claims'])
        stats = (f'<div class="card">{len(self.cohort)} engagements in {len(self.by_campaign)} campaign groups · '
                 f'{len(self.dossiers)} dossiers · {claims:,} claims · {cites:,} citations · {len(self.sources):,} registered sources · '
                 f'{len(self.strength)} engagements in the strength and command ledgers · {len(self.attributed)} commanders credited</div>')
        readme = (self.root / 'README.md').read_text(encoding='utf-8')
        self.write('index.html', 'Overview', stats + self.verdict_box('') + markdown(readme, self.home_link), 0)

    def home_link(self, target):
        link = self.doc_link('README.md')(target)
        return link.replace('../results/', 'results/', 1) if link.startswith('../results/') else link

    def results(self):
        items = []
        for p, title in self.reports:
            name = self.report_name(p)
            body = (f'<p class="muted">From <a href="{esc(self.blob(p))}"><code>{esc(p)}</code></a>.</p>'
                    + markdown((self.root / p).read_text(encoding='utf-8'), self.doc_link(p)))
            self.write(f'results/{name}.html', title, body, 1)
            items.append(f'<li><a href="{name}.html">{esc(title)}</a> <span class="muted"><code>{esc(p)}</code></span></li>')
        self.write('results/index.html', 'Results and documents',
                   '<h1>Results and documents</h1>' + self.verdict_box('../') + '<ul>' + ''.join(items) + '</ul>', 1)

    def rating_of(self, c):
        return (self.run or {}).get('commanders', {}).get(c)

    def commanders(self):
        theta = 'theta' if self.run and self.run.get('run_version') == 4 else 'theta_pooled'
        rows = []
        for c in sorted(set(self.attributed) | set(self.named), key=lambda c: (self.registry[c]['side'], self.registry[c]['name'])):
            r = self.rating_of(c) or {}
            est = (f"{r[theta]:+.2f}" if theta in r else '')
            iv = (f"{r['interval_80'][0]:+.2f} to {r['interval_80'][1]:+.2f}" if 'interval_80' in r else '')
            rows.append([self.commander_link(c, '../'), esc(self.registry[c]['side']), len(self.attributed[c]),
                         r.get('battles_modelled', 0), est, iv, labels(r.get('labels', []))])
            self.commander_page(c, r, theta)
        intro = ('<h1>Commanders</h1><p>Every commander the command ledger credits with an in-scope engagement or names as '
                 'a candidate, successor or superior, alphabetical '
                 'within each side. θ is the latest run\'s pooled residual rating: how a commander\'s battles went relative to '
                 'what the run\'s comparator predicts, pulled towards zero. It is not skill, and the order here is not a ranking.</p>')
        self.write('commanders/index.html', 'Commanders', intro + self.verdict_box('../') + table(
            ['Commander', 'Side', 'Battles credited', 'Battles modelled', 'θ', '80% interval', 'Labels'], rows, {2, 3, 4}), 1)

    def commander_page(self, c, r, theta):
        reg = self.registry[c]
        rows = []
        for b, s in sorted(self.attributed[c], key=lambda x: self.battles[x[0]]['start_date']):
            side = self.command[b]['sides'][s]
            rows.append([self.battle_link(b, '../'), esc(self.battles[b]['start_date']), esc(s), esc(side['grade']),
                         esc(side['rule']), esc(side['echelon']), labels(side['labels'])])
        est = ''
        if theta in r:
            est = (f'<div class="card">Latest run: θ {r[theta]:+.2f}, 80% interval {r["interval_80"][0]:+.2f} to '
                   f'{r["interval_80"][1]:+.2f}, 95% interval {r["interval_95"][0]:+.2f} to {r["interval_95"][1]:+.2f}; '
                   f'{r["battles_modelled"]} battles modelled ({r.get("wins_in_model", 0)}–{r.get("losses_in_model", 0)})'
                   + (f'; within-side 80% rank interval {r["rank_80"][0]}–{r["rank_80"][1]}' if r.get('rank_80') else '')
                   + f'. {labels(r.get("labels", []))}</div>')
        elif r:
            est = f'<div class="card">Latest run: no modelled battle. {labels(r.get("labels", []))}</div>'
        named = [[self.battle_link(b, '../'), esc(self.battles[b]['start_date']), esc(s), esc(role),
                  self.commander_link(self.command[b]['sides'][s]['commander_id'], '../')]
                 for b, s, role in sorted(self.named.get(c, []), key=lambda x: self.battles[x[0]]['start_date'])]
        body = (f'<h1>{esc(reg["name"])}</h1><p class="muted">{esc(reg["side"])} · <code>{esc(c)}</code> · CWSAC names: '
                f'{esc(", ".join(reg.get("cwsac_names", [])))}</p>{est}<h2>Engagements credited by the command ledger</h2>'
                + (table(['Engagement', 'Start', 'Side', 'Grade', 'Rule', 'Echelon', 'Labels'], rows) if rows else '<p>None.</p>')
                + ('<h2>Named in another role</h2>' + table(['Engagement', 'Start', 'Side', 'Role', 'Credited commander'], named)
                   if named else ''))
        self.write(f'commanders/{c}.html', reg['name'], body, 1)

    def campaign_pages(self):
        rows = []
        for name in sorted(self.by_campaign, key=lambda n: (int(self.campaigns[n]['start_year']), int(self.campaigns[n]['start_month']), n)):
            info = self.campaigns[name]
            bs = sorted(self.by_campaign[name], key=lambda b: self.battles[b]['start_date'])
            rows.append([self.campaign_link(name, '../'), esc(info['theater']), esc(info['start_year']), len(bs)])
            body = (f'<h1>{esc(name)}</h1><p class="muted">{esc(info["theater"])} theater · CWSAC campaign group</p>'
                    + table(['Engagement', 'Start', 'End', 'Result', 'In the ledgers'],
                            [[self.battle_link(b, '../'), esc(self.battles[b]['start_date']), esc(self.battles[b]['end_date']),
                              esc(self.battles[b]['result']), 'yes' if b in self.strength else 'no'] for b in bs]))
            self.write(f'campaigns/{slug(name)}.html', name, body, 1)
        self.write('campaigns/index.html', 'Campaigns', '<h1>Campaigns</h1>' + table(
            ['Campaign', 'Theater', 'Start year', 'Engagements'], rows, {2, 3}), 1)

    def engagements(self):
        rows = []
        for b in sorted(self.cohort, key=lambda b: (self.battles[b]['start_date'], b)):
            d = self.dossiers.get(b)
            rows.append([self.battle_link(b, '../'), esc(self.battles[b]['start_date']), self.campaign_link(self.battles[b]['campaign'], '../'),
                         esc(self.battles[b]['result']), len(d['claims']) if d else 0, 'yes' if b in self.strength else 'no'])
            self.engagement_page(b)
        self.write('engagements/index.html', 'Engagements', '<h1>Engagements</h1><p>Every engagement in the frozen CWSAC frame '
                   '(cohort v2), by start date. "In the ledgers" marks the decisive, two-sided engagements that the strength '
                   'and command ledgers cover.</p>' + table(['Engagement', 'Start', 'Campaign', 'Result', 'Claims', 'In the ledgers'], rows, {4}), 1)

    def engagement_page(self, b):
        rec, up = self.battles[b], '../'
        parts = [f'<h1>{esc(rec["battle_name"])} <span class="muted">{b}</span></h1>',
                 f'<p class="muted">{esc(rec["start_date"])} to {esc(rec["end_date"])} · {esc(rec["state"])} · '
                 f'{self.campaign_link(rec["campaign"], up)} · frozen result: <strong>{esc(rec["result"])}</strong> · '
                 f'<a href="{esc(rec["url"])}">NPS summary (as listed)</a></p>']
        if rec.get('description'):
            parts.append(f'<div class="card"><span class="muted">CWSAC description</span><blockquote>{esc(rec["description"])}</blockquote></div>')
        if b in self.command:
            parts.append('<h2>Command responsibility (ledger v2)</h2>')
            for s in SIDES:
                side = self.command[b]['sides'][s]
                parts.append(f'<h3>{esc(s)}: {self.commander_link(side["commander_id"], up)}</h3>'
                             f'<p>Grade {esc(side["grade"])} under rule {esc(side["rule"])}; echelon {esc(side["echelon"])}. '
                             f'{labels(side["labels"])}</p>'
                             + (f'<p>Other candidates: {", ".join(self.commander_link(c, up) for c in side["candidates"])}</p>' if side['candidates'] else '')
                             + f'<p class="muted">{esc(side.get("rationale"))}</p>'
                             + ''.join(self.citation(c, up) for c in side['citations']))
        if b in self.strength:
            parts.append('<h2>Side strength (ledger v3)</h2>')
            for s in SIDES:
                side = self.strength[b]['sides'][s]
                est = side['estimate']
                head = (f'grade {esc(est["grade"])}, {num(est["point"])} ({num(est["low"])}–{num(est["high"])})'
                        if est['point'] is not None else f'grade {esc(est["grade"])}: no usable figure (modelled in the rating runs)')
                rows = [[esc(i['id']), esc(i.get('class')), esc(f'{i["printed"]["lower"]:,}' if i['printed']['lower'] == i['printed']['upper']
                                                              else f'{i["printed"]["lower"]:,}–{i["printed"]["upper"]:,}'),
                         esc(i['basis']), esc(i.get('bound') or ''), labels(i['codes']),
                         self.input_ref(i, up)] for i in side['inputs']]
                parts.append(f'<h3>{esc(s)}: {head}</h3><p>{labels(est["labels"])}</p>'
                             + (table(['Input', 'Class', 'Printed', 'Basis', 'Bound', 'Codes', 'Passage'], rows) if rows else ''))
        nest = [n for n in self.nesting if b in (n['containing'], n['contained'])]
        if nest:
            parts.append('<h2>Nested records</h2>' + table(['Containing', 'Contained', 'Outcome', 'Reason'],
                         [[self.battle_link(n['containing'], up), self.battle_link(n['contained'], up), esc(n['outcome']), esc(n.get('reason'))]
                          for n in nest]))
        d = self.dossiers.get(b)
        if d:
            parts.append(f'<h2>Dossier claims</h2><p class="muted">Draft dossier, revision <code>{esc(d.get("revision"))}</code>. '
                         f'Claims are extraction records with their quoted passages, not historical adjudication. '
                         f'<a href="{esc(self.blob(f"data/evidence/{b}.json"))}">JSON</a></p>')
            for dim, claims in sorted(_group(d['claims']).items()):
                parts.append(f'<h3>{esc(dim)}</h3>')
                for c in claims:
                    parts.append(f'<div class="claim" id="claim-{esc(c["id"])}"><p><span class="label">{esc(c["status"])}</span>'
                                 f'<span class="label">{esc(c.get("phase"))}</span> {esc(c["value"])}</p>'
                                 + (f'<p class="muted">{esc(c["rationale"])}</p>' if c.get('rationale') else '')
                                 + ''.join(self.citation(x, up) for x in c['citations']) + '</div>')
            if d.get('open_questions'):
                parts.append('<h2>Open questions</h2><ul>' + ''.join(f'<li>{esc(q)}</li>' for q in d['open_questions']) + '</ul>')
        self.write(f'engagements/{b}.html', rec['battle_name'], ''.join(parts), 1)

    def source_page(self):
        cited = Counter(c['source_id'] for d in self.dossiers.values() for cl in d['claims'] for c in cl['citations'])
        rows = [[f'<span id="{esc(s["id"])}"><code>{esc(s["id"])}</code></span>', esc(s.get('title')), esc(s.get('source_kind')),
                 esc(s.get('independence_group')), cited[s['id']],
                 (f'<a href="{esc(self.blob(s["path"]))}">snapshot</a> <code>{esc(s["sha256"][:12])}…</code>' if s.get('path') else ''),
                 (f'<a href="{esc(s["url"])}">origin</a>' if s.get('url') else '')]
                for s in sorted(self.sources.values(), key=lambda s: s['id'])]
        self.write('sources.html', 'Sources', '<h1>Registered sources</h1><p>Every source in <code>data/sources.json</code> '
                   'with its pinned snapshot and SHA-256 (the first 12 hex digits shown). Copies and reprints share an '
                   'independence group and are not independent families.</p>'
                   + table(['ID', 'Title', 'Kind', 'Independence group', 'Dossier citations', 'Snapshot', 'Origin'], rows, {4}), 0)


def _group(claims):
    out = defaultdict(list)
    for c in claims:
        out[c['dimension']].append(c)
    return out


def build_site(root, out='_site', commit='main'):
    return Site(root, Path(root) / out if not Path(out).is_absolute() else Path(out), commit).build()
