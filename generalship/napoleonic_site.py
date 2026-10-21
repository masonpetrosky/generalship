"""Read-only pages for the frozen Napoleonic cohort; no attribution or admission."""

from collections import Counter, defaultdict

from .napoleonic import COHORT, FRAME
from .napoleonic_comparison import ComparisonPages
from .napoleonic_outcomes import OutcomePages
from .sources import read_json


class NapoleonicPages:
    def __init__(self, site):
        self.site = site
        self.cohort = []
        self.entries, self.dossiers = {}, {}
        self.groups = defaultdict(list)
        self.comparisons = None
        self.outcomes = None
        if not (site.root / COHORT).is_file():
            return
        self.cohort = read_json(site.root / COHORT)['battle_ids']
        frame = {e['id']: e for e in read_json(site.root / FRAME)['entries']}
        for b in self.cohort:
            self.entries[b] = frame[b]
            self.dossiers[b] = read_json(site.root / f'data/napoleonic/evidence/{b}.json')
            self.groups[frame[b]['campaign_group']].append(b)
        self.comparisons = ComparisonPages(self)
        self.outcomes = OutcomePages(self)

    def counts(self, ids):
        return Counter(c['status'] for b in ids for c in self.dossiers[b]['claims'])

    def battle_link(self, b, up):
        from .site import esc
        return (f'<a href="{up}napoleonic/engagements/{b}.html">{esc(self.entries[b]["place"])}</a> '
                f'<span class="muted">{b}</span>')

    def campaign_link(self, name, up):
        from .site import esc, slug
        return f'<a href="{up}napoleonic/campaigns/{slug(name)}.html">{esc(name)}</a>'

    def summary(self):
        from .site import num
        counts = self.counts(self.cohort)
        return (f'{len(self.dossiers)}/{len(self.cohort)} draft dossiers · {len(self.groups)} campaign groups · '
                f'{num(sum(counts.values()))} claims · {num(counts["unknown"])} explicit unknowns · '
                f'{num(counts["disputed"])} disputed claims')

    def status(self):
        return ('<div class="research-status">'
                '<div class="card"><strong>Research coverage</strong><p>Draft claims preserve what the inspected '
                'sources say. Supported means passage-backed, not historically adjudicated.</p></div>'
                '<div class="card"><strong>Measurement readiness</strong><p>Timing, population and authority '
                'need their own mappings. Read the boundary notes and open questions.</p></div>'
                '<div class="card"><strong>Model admission</strong><p>Draft claims are not admitted predictors '
                'or commander ratings. Coverage does not establish contribution.</p></div></div>')

    def build(self):
        if not self.cohort:
            return
        self.index()
        self.engagements()
        self.campaigns()
        for b in self.cohort:
            self.engagement(b)
        self.comparisons.build()
        self.outcomes.build()

    def index(self):
        from .site import esc, table
        rows = []
        for name, ids in sorted(self.groups.items(), key=lambda x: (self.entries[x[1][0]]['start_year'], x[0])):
            counts = self.counts(ids)
            rows.append([self.campaign_link(name, '../'), f'{len(ids)}/{len(ids)}', sum(counts.values()),
                         counts['unknown'], counts['disputed']])
        docs = [('docs/research/napoleonic-measurement-feasibility-v1.md', 'Measurement feasibility'),
                ('docs/napoleonic-command-units-v1.md', 'Command and force scope'),
                ('docs/napoleonic-methods-v1.md', 'Methods and evaluation design')]
        body = ('<h1>Napoleonic Wars</h1><p>The frozen 1805–1815 land cohort from Bodart. '
                'Campaign groups organize the source frame; they are not resolved armies or command appointments.</p>'
                f'<div class="card">{self.summary()}</div>'
                + f'<p><a href="engagements.html">Browse all {len(self.cohort)} engagements</a> · '
                + f'<a href="{self.site.blob(COHORT)}">Frozen cohort</a></p>'
                + '<div class="card"><a href="comparisons/index.html"><strong>Compare measurement evidence</strong></a>'
                + '<p>Compare strength, timing and command scope for the 12 engagements in the two completed '
                + 'measurement pilots. Alternatives and unknowns remain explicit.</p></div>'
                + '<div class="card"><a href="outcomes/index.html"><strong>Inspect outcome evidence</strong></a>'
                + '<p>Separate views of the completed 22-entry loss pilot and four-entry Naples objective/result pilot, '
                + 'with source passages, missing values and coverage denominators.</p></div>'
                + self.status()
                + '<h2>Campaign groups</h2>'
                + table(['Campaign group', 'Drafts / entries', 'Claims', 'Unknown', 'Disputed'], rows, {1, 2, 3, 4})
                + '<h2>Research and methods</h2><ul>'
                + ''.join(f'<li><a href="{esc(self.site.blob(path))}">{esc(title)}</a></li>' for path, title in docs)
                + '</ul>')
        self.site.write('napoleonic/index.html', 'Napoleonic Wars', body, 1)

    def engagement_rows(self, ids, up):
        from .site import esc
        rows = []
        for b in sorted(ids, key=lambda b: (self.entries[b]['start_date'] or '', b)):
            e, d = self.entries[b], self.dossiers[b]
            counts = self.counts([b])
            rows.append([self.battle_link(b, up), esc(e['start_date'] or 'Unnormalized'),
                         self.campaign_link(e['campaign_group'], up), esc(d['status']),
                         len(d['claims']), counts['unknown'], counts['disputed']])
        return rows

    def engagements(self):
        from .site import table
        body = ('<h1>Napoleonic engagements</h1><p>All entries in the frozen land cohort, '
                'including incomplete and disputed evidence. Counts describe research records.</p>'
                f'<p>{self.summary()}</p>'
                + table(['Engagement', 'Frame start', 'Campaign group', 'Dossier', 'Claims', 'Unknown', 'Disputed'],
                        self.engagement_rows(self.cohort, '../'), {4, 5, 6}))
        self.site.write('napoleonic/engagements.html', 'Napoleonic engagements', body, 1)

    def campaigns(self):
        from .site import esc, slug, table
        for name, ids in self.groups.items():
            counts = self.counts(ids)
            body = ('<p><a href="../index.html">Napoleonic Wars</a></p>'
                    f'<h1>{esc(name)}</h1><p>Complete frozen source group: {len(ids)} entries, '
                    f'{len(ids)} draft dossiers. {counts["unknown"]} explicit unknowns and '
                    f'{counts["disputed"]} disputed claims remain visible.</p>' + self.status()
                    + ('<p><a href="../comparisons/index.html">Compare this group’s measurement evidence</a></p>'
                       if set(ids) <= self.comparisons.ids else '')
                    + self.outcomes.campaign_link(name)
                    + table(['Engagement', 'Frame start', 'Campaign group', 'Dossier', 'Claims', 'Unknown', 'Disputed'],
                            self.engagement_rows(ids, '../../'), {4, 5, 6}))
            self.site.write(f'napoleonic/campaigns/{slug(name)}.html', name, body, 2)

    def side_notes(self, d):
        from .site import esc
        completion = d.get('research_completion', {})
        if not completion:
            return ('<p class="muted">This older draft has no typed per-side completion notes. '
                    'Its original claims, boundary note and open questions follow.</p>')
        out = ['<h2>Recorded side context</h2>']
        for side, notes in completion['sides'].items():
            out.append(f'<h3>Side {esc(side)}</h3><dl>')
            for key, title in [('strength_population_and_time', 'Strength population and time'),
                               ('command_scope', 'Command scope'), ('army_continuity', 'Army continuity')]:
                out.append(f'<dt>{title}</dt><dd>{esc(notes[key])}</dd>')
            out.append('</dl><p>Recorded claim links: '
                       + ' · '.join(f'<a href="#claim-{esc(cid)}">{esc(cid)}</a>' for cid in dict.fromkeys(
                           notes['strength_claim_ids'] + notes['command_claim_ids'])) + '</p>')
        return ''.join(out)

    def engagement(self, b):
        from .site import esc, labels, table, _group
        e, d, up = self.entries[b], self.dossiers[b], '../../'
        counts = self.counts([b])
        parts = [f'<p><a href="../index.html">Napoleonic Wars</a> · '
                 f'{self.campaign_link(e["campaign_group"], up)}</p>'
                 f'<h1>{esc(e["place"])} <span class="muted">{b}</span></h1>'
                 f'<p>Frame dates: {esc(e["start_date"] or "Unnormalized")} to '
                 f'{esc(e["end_date"] or "Unnormalized")} · printed: {esc(e["date_printed"])} '
                 f'{esc(e["year_printed"])} {labels(e.get("date_flags", []))}</p>'
                 f'<p>Dossier: {esc(d["status"])} · {len(d["claims"])} claims · '
                 f'{counts["unknown"]} explicit unknowns · {counts["disputed"]} disputed claims · '
                 f'<a href="{self.site.blob(f"data/napoleonic/evidence/{b}.json")}">Dossier JSON</a></p>',
                 self.status(), '<h2>Boundary and applicability</h2>',
                 f'<p>{esc(d["boundary_note"])}</p><dl>'
                 f'<dt>Tactical replacement boundary</dt><dd>{esc(d.get("tactical_replacement_at") or "Unestablished")}</dd>'
                 f'<dt>Campaign replacement boundary</dt><dd>{esc(d.get("campaign_replacement_at") or "Unestablished")}</dd></dl>',
                 '<h2>Compiler-listed forces and names</h2><p>Side A is France and its allies; '
                 'side B is the opposing side. These are Bodart’s printed labels, not resolved '
                 'identities, selected opening strengths or automatic command credit.</p>']
        if b in self.comparisons.ids:
            parts.insert(1, '<div class="card"><a href="../comparisons/' + b + '.html">'
                         '<strong>Compare this engagement’s measurement evidence</strong></a>'
                         '<p>Alternative figures, command scopes and unresolved opening mappings, with supporting passages.</p></div>')
        if b in self.outcomes.ids:
            parts.insert(1, '<div class="card"><a href="../outcomes/' + b + '.html">'
                         '<strong>Inspect this engagement’s outcome evidence</strong></a>'
                         '<p>Completed pilot components, unknowns and exact supporting passages.</p></div>')
        a = e['french_side']
        other = 'loser' if a == 'winner' else 'winner'
        parts.append(table(['Side', 'Printed force label', 'Printed commander names'],
                           [[side, esc(e[f'{key}_text'] or 'Not named'),
                             esc(e[f'{key}_commander_text'] or 'Not named')]
                            for side, key in [('A', a), ('B', other)]]))
        frame_cite = {'source_id': 'bodart-1908-transcription-v1', 'section': f'p{e["page"]}',
                      'locator': f'Frozen frame entry {b}, Bodart p. {e["page"]}; see dossier citations for passages.'}
        parts.append(self.site.citation(frame_cite, up))
        parts.append(self.side_notes(d))
        grouped = _group(d['claims'])
        dims = [dim for dim in ['strength', 'responsibility'] if dim in grouped]
        dims += sorted(set(grouped) - set(dims))
        titles = {'strength': 'Strength claims', 'responsibility': 'Command responsibility claims'}
        parts.append('<h2>Dossier evidence</h2><p>Phase labels remain draft hypotheses while replacement '
                     'boundaries are unestablished. Unknowns are missing evidence, not zero values.</p>'
                     '<p class="jump-links">'
                     + ' · '.join(f'<a href="#dimension-{esc(dim)}">{esc(titles.get(dim, dim.title()))}</a>' for dim in dims)
                     + ' · <a href="#open-questions">Open questions</a></p>')
        for dim in dims:
            parts.append(f'<h3 id="dimension-{esc(dim)}">{esc(titles.get(dim, dim.title()))}</h3>')
            for c in grouped[dim]:
                value = esc(c['value']) if c['value'] is not None else 'Unknown — not established by the inspected evidence.'
                parts.append(f'<article class="claim" id="claim-{esc(c["id"])}">'
                             f'<h4><a href="#claim-{esc(c["id"])}">{esc(c["id"])}</a></h4>'
                             f'<p>{labels([c["status"], c["phase"]] + ([c["code"]] if c.get("code") else []))}</p>'
                             f'<p>{value}</p><p class="muted">{esc(c["rationale"])}</p>'
                             + ''.join(self.site.citation(cite, up) for cite in c['citations'])
                             + ('<p class="muted">No cited passage; explicit evidence gap.</p>' if c['status'] == 'unknown' else '')
                             + '</article>')
        parts.append('<h2 id="open-questions">Open questions</h2><ul>'
                     + ''.join(f'<li>{esc(q)}</li>' for q in d['open_questions']) + '</ul>')
        self.site.write(f'napoleonic/engagements/{b}.html', f'{e["place"]} · Napoleonic evidence', ''.join(parts), 2)
