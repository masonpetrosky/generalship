"""Present the two stopped measurement pilots without selecting or deriving inputs."""

import html
import json

from .sources import read_json

BASE = 'data/napoleonic/'
LEDGER = BASE + 'ledger-design-v1/examples.json'
BOUNDARIES = BASE + 'boundaries-v1/records.json'
AUTHORITY = BASE + 'authority-v1/mappings.json'
PENINSULA = BASE + 'peninsula-1812-measurement-v1/records.json'

CSS = """
.comparison-sides { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px; }
.comparison-sides > section { min-width: 0; }
.observation { border: 1px solid var(--line); border-radius: 6px; background: var(--card); padding: 12px; margin: 12px 0; }
.observation h4 { margin: 0 0 8px; font-size: 1.05rem; }
.observation dl { margin-bottom: 0; }
.observation dd, .comparison-note, .passage { overflow-wrap: anywhere; }
.record-id { font-size: .8rem; color: var(--muted); }
.comparison-note { border-top: 1px solid var(--line); padding: 12px 0; }
.comparison-note h4 { margin: 0 0 8px; }
.comparison-details { border: 1px solid var(--line); border-radius: 6px; padding: 12px; margin: 12px 0; }
.comparison-details summary { cursor: pointer; font-weight: 600; }
.passage { border-top: 1px solid var(--line); padding: 12px 0; scroll-margin-top: 12px; }
:target { outline: 2px solid var(--accent); outline-offset: 4px; }
@media (max-width: 760px) { .comparison-sides { grid-template-columns: 1fr; gap: 4px; } }
"""


def esc(value):
    return html.escape(str(value))


def value_html(value):
    if value is None:
        return '<span class="muted">Unestablished</span>'
    if isinstance(value, dict):
        return facts((key.replace('_', ' ').capitalize(), v) for key, v in value.items())
    if isinstance(value, list):
        return '<ul>' + ''.join(f'<li>{value_html(v)}</li>' for v in value) + '</ul>' if value else 'None recorded'
    return esc(value)


def facts(items):
    return '<dl>' + ''.join(f'<dt>{esc(k)}</dt><dd>{value_html(v)}</dd>' for k, v in items) + '</dl>'


def amount_label(record):
    """Keep units, approximation, one-sided bounds and unknowns intact."""
    if 'amount' not in record:
        number = record['value']
        text = 'Unknown' if number is None else f'{number:,}'
        if record['precision'] == 'approximate':
            text = 'About ' + text
    else:
        amount = record['amount']
        low, high, kind = amount['lower'], amount['upper'], amount['kind']
        if kind == 'unknown':
            text = 'Unknown'
        elif kind == 'lower_bound':
            text = ('≥ ' if amount['lower_inclusive'] else '> ') + f'{low:,}'
        elif kind == 'upper_bound':
            text = ('≤ ' if amount['upper_inclusive'] else '< ') + f'{high:,}'
        elif kind == 'range':
            text = f'{low:,}–{high:,}'
        else:
            text = ('About ' if kind == 'approximate' else '') + f'{low:,}'
    return f'{text} {record["unit"]}'


class Passages:
    """Link observations to exact quotations, merging only identical citations."""

    def __init__(self, site, packages):
        self.site, self.packages = site, packages
        self.items = {}

    def add(self, passage):
        citation = passage['citation']
        key = json.dumps(citation, sort_keys=True, ensure_ascii=False)
        if key not in self.items:
            self.items[key] = {'id': f'passage-{len(self.items) + 1}', 'citation': citation,
                               'renderings': [], 'images': []}
        item = self.items[key]
        renderings = passage.get('english_interpretations', []) + ([passage['interpretation_en']]
                                                                  if passage.get('interpretation_en') else [])
        for text in renderings:
            if text not in item['renderings']:
                item['renderings'].append(text)
        image = passage.get('facsimile_source_id') or passage.get('image_source_id')
        if image and image not in item['images']:
            item['images'].append(image)
        return (f'<a href="#{item["id"]}">{esc(citation["source_id"])}'
                + (f' · {esc(citation["section"])}' if citation.get('section') else '') + '</a>')

    def refs(self, package, ids):
        if not ids:
            return '<p class="muted">Explicit evidence gap; no supporting passage indexed.</p>'
        return '<p class="cite">Passages: ' + ' · '.join(
            self.add(self.packages[package][pid]) for pid in ids) + '</p>'

    def ledger_refs(self, records):
        return '<p class="cite">Passages: ' + ' · '.join(dict.fromkeys(self.add(r) for r in records)) + '</p>'

    def render(self):
        out = ['<h2 id="supporting-passages">Supporting passages</h2>'
               '<p>Original wording and previously recorded English interpretations. '
               'Repeated citations share a passage; citation counts do not establish independent sources.</p>']
        for item in self.items.values():
            out.append(f'<article class="passage" id="{item["id"]}"><h3>{item["id"].replace("-", " ").title()}</h3>'
                       + self.site.citation(item['citation'], '../../'))
            out.extend(f'<p>{esc(text)}</p>' for text in item['renderings'])
            for image_id in item['images']:
                source = self.site.sources[image_id]
                out.append(f'<p class="cite"><a href="{esc(self.site.blob(source["path"]))}">Page image</a> · '
                           f'<a href="../../sources.html#{esc(image_id)}">{esc(image_id)}</a> · '
                           f'<code title="SHA-256: {source["sha256"]}">{source["sha256"][:12]}…</code></p>')
            out.append('</article>')
        return ''.join(out)


class ComparisonPages:
    def __init__(self, napoleonic):
        self.napoleonic, self.site = napoleonic, napoleonic.site
        self.ledger, self.boundaries, self.authority, self.peninsula = (
            read_json(self.site.root / path) for path in (LEDGER, BOUNDARIES, AUTHORITY, PENINSULA))
        self.naples_ids = {r['battle_id'] for r in self.ledger['side_records']}
        self.ids = self.naples_ids | {r['battle_id'] for r in self.peninsula['entries']}
        self.packages = {name: {p['id']: p for p in data['passages']} for name, data in (
            ('boundary', self.boundaries), ('authority', self.authority), ('peninsula', self.peninsula))}

    def observations(self, battle, kind):
        if battle in self.naples_ids:
            records = self.ledger['strength_records'] if kind == 'strength' else self.authority['roles']
        else:
            records = [r for r in self.peninsula['observations'] if r['kind'] == kind]
        return [r for r in records if r['battle_id'] == battle]

    def build(self):
        from .site import table
        rows = []
        for b in sorted(self.ids, key=lambda b: (self.napoleonic.entries[b]['start_date'], b)):
            self.engagement(b)
            entry = self.napoleonic.entries[b]
            counts = [sum(r['side'] == side for r in self.observations(b, kind))
                      for side in ('A', 'B') for kind in ('strength', 'authority')]
            rows.append([f'<a href="{b}.html">{esc(entry["place"])}</a> <span class="muted">{b}</span>',
                         esc(entry['campaign_group']), *counts])
        body = ('<p><a href="../index.html">Napoleonic Wars</a></p><h1>Compare measurement evidence</h1>'
                '<p>12 engagements · 24 sides · two complete development campaign groups. '
                'These purposive pilots cover 12 of the 325 cohort entries; they do not estimate corpus-wide feasibility.</p>'
                '<div class="card"><strong>Read the figures with their scope.</strong> '
                'The 82 strength observations include nine unknown counts and one gun count. '
                'The 73 command-role observations describe different levels, tasks and phases. '
                'All 24 joint opening force-and-authority mappings remain unresolved.</div>'
                '<p>Compare population, time and authority before comparing values. These pages retain '
                'the existing primary-verified records and their unresolved alternatives. '
                'Observation counts include explicit unknowns and are not admitted inputs.</p>'
                + table(['Engagement', 'Campaign group', 'A strength', 'A roles', 'B strength', 'B roles'], rows, {2, 3, 4, 5})
                + '<p><a href="' + esc(self.site.blob('docs/research/napoleonic-measurement-feasibility-v1.md'))
                + '">Measurement-feasibility checkpoint</a></p>')
        self.site.write('napoleonic/comparisons/index.html', 'Compare measurement evidence', body, 2)

    @staticmethod
    def record(record_id, title, items, evidence='', extra=''):
        return (f'<article class="comparison-note" id="record-{esc(record_id)}">'
                f'<h4>{esc(title)}</h4>{facts(items)}{extra}{evidence}</article>')

    @staticmethod
    def observation_links(ids, kind='observation'):
        return '<p>' + ' · '.join(f'<a href="#{kind}-{esc(i)}">{esc(i)}</a>' for i in ids) + '</p>'

    def strength(self, r, passages):
        if 'amount' in r:
            fields = [('As transcribed', r['printed_value']), ('Precision', r['amount']['kind']),
                      ('Population', r['population']), ('Personnel or equipment basis', r['basis']),
                      ('Reported state and time', r['state_description']), ('Boundary relation', r['boundary_relation']),
                      ('Source role', r['source_role']), ('Derivation', r['derivation'])]
            evidence = passages.ledger_refs(r['evidence'])
            claims = list(dict.fromkeys(e['claim_id'] for e in r['evidence']))
        else:
            fields = [('Precision', r['precision']), ('Population', r['population_or_scope']),
                      ('Reported time', r['reported_time']), ('Source role', r['source_role'])]
            evidence = passages.refs('peninsula', r['evidence'])
            claims = [r['claim_id']]
        return (f'<article class="observation" id="observation-{esc(r["id"])}">'
                f'<h4>{esc(amount_label(r))}</h4><p class="record-id">{esc(r["id"])}</p>'
                + facts(fields) + (f'<p>{esc(r["note"])}</p>' if r['note'] else '')
                + self.claim_links(r['battle_id'], claims) + evidence + '</article>')

    def role(self, r, passages):
        fields = [('Authority type', r['authority_type']),
                  ('Force or task scope', r.get('force_scope', r.get('population_or_scope'))),
                  ('Reported time', r['reported_time']), ('Resolved person identity', r['resolved_person_id'])]
        if 'appointment_start' in r:
            fields += [('Appointment start', r['appointment_start']), ('Appointment end', r['appointment_end']),
                       ('Effective transfer', r['effective_transfer_at'])]
            evidence = passages.refs('authority', r['evidence'])
            origin = next((c for c in self.ledger['command_records'] if c['id'] == r['original_observation_id']), None)
            claims = list(dict.fromkeys(e['claim_id'] for e in origin['evidence'])) if origin else []
        else:
            fields += [('Source role', r['source_role'])]
            evidence = passages.refs('peninsula', r['evidence'])
            claims = [r['claim_id']]
        return (f'<article class="observation" id="observation-{esc(r["id"])}">'
                f'<h4>{esc(r["actor_label"])}</h4><p class="record-id">{esc(r["id"])}</p>'
                + facts(fields) + f'<p>{esc(r["note"])}</p>'
                + self.claim_links(r['battle_id'], claims) + evidence + '</article>')

    @staticmethod
    def claim_links(b, ids):
        return '<p class="cite">Dossier: ' + ' · '.join(
            f'<a href="../engagements/{b}.html#claim-{esc(cid)}">{esc(cid)}</a>' for cid in ids) + '</p>' if ids else ''

    def readiness(self, b):
        out = ['<h2 id="mapping">Opening comparison: unresolved</h2><div class="comparison-sides">']
        for side in ('A', 'B'):
            out.append(f'<section id="mapping-{side}"><h3>Side {side}</h3>')
            if b in self.naples_ids:
                r = next(r for r in self.authority['forces'] if r['battle_id'] == b and r['side'] == side)
                boundary = next(r for r in self.boundaries['sides'] if r['battle_id'] == b and r['side'] == side)
                fields = [('Reported scopes', r['reported_scopes']), ('Selected boundary', r['selected_boundary']),
                          ('Selected strength', r['selected_strength']), ('Selected person', r['selected_person_id']),
                          ('Army identity', r['army_id']), ('Remaining gaps', boundary['unknowns']), ('Scope note', r['note'])]
            else:
                r = next(r for r in self.peninsula['side_records'] if r['battle_id'] == b and r['side'] == side)
                fields = [('Selected boundary', r['selected_boundary']), ('Selected strength', r['selected_strength']),
                          ('Selected person', r['selected_person_id']), ('Army identity', r['army_id']),
                          ('Remaining gaps', r['blockers'])]
            out.append(facts(fields) + '</section>')
        return ''.join(out) + '</div>'

    def findings(self, b, passages):
        out = ['<h2 id="compatibility">Recorded compatibility findings</h2>']
        if b in self.naples_ids:
            for r in self.ledger['discrepancies']:
                if r['battle_id'] == b:
                    out.append(self.record(r['id'], f'Side {r["side"]}: {r["kind"].replace("_", " ")}',
                                           [('Resolution', r['resolution']), ('Finding', r['note'])],
                                           extra=self.observation_links(r['observation_ids'])))
            for r in self.ledger['sum_proposals']:
                if r['battle_id'] == b:
                    out.append(self.record(r['id'], 'Arithmetic only: ' + r['id'],
                                           [('Recorded sum', r['arithmetic_sum']), ('Disjoint membership', r['disjoint_membership']),
                                            ('Same state and time', r['same_state_time']), ('Complete target', r['complete_target']),
                                            ('Limitation', r['note'])], extra=self.observation_links(r['input_ids'])))
            for r in self.authority['reconciliations']:
                if r['battle_id'] == b:
                    out.append(self.record(r['id'], 'Authority: ' + r['finding'].replace('_', ' '),
                                           [('Finding', r['note']), ('Effective transfer', r['effective_transfer_at'])],
                                           passages.refs('authority', r['evidence']), self.observation_links(r['role_ids'])))
        else:
            entry = next(r for r in self.peninsula['entries'] if r['battle_id'] == b)
            for i, r in enumerate(entry['findings']):
                out.append(self.record(f'finding-{i}', 'Population and boundary', [('Finding', r['text'])],
                                       passages.refs('peninsula', r['evidence'])))
            co_reports = [r for r in self.peninsula['co_reports'] if r['battle_id'] == b]
            out.append('<h3>Locally associated strength and role</h3><p>Co-reporting retains a local association; '
                       'it does not establish a complete opening force or exclusive authority.</p>')
            if not co_reports:
                out.append('<p>No local strength-role association indexed for this entry.</p>')
            for r in co_reports:
                out.append(self.record(r['id'], r['status'].replace('_', ' '), [('Basis', r['basis']), ('Finding', r['note'])],
                                       extra=self.observation_links([r['strength_id'], r['authority_id']])))
            for r in self.peninsula['arithmetic_checks']:
                if r['battle_id'] == b:
                    out.append(self.record(r['id'], 'Arithmetic only: ' + r['kind'].replace('_', ' '),
                                           [('Recorded terms', r['terms']), ('Recorded result', r['result']),
                                            ('Unit', r['unit']), ('Opening feature', r['opening_feature']), ('Limitation', r['note'])],
                                           passages.refs('peninsula', r['evidence'])))
        return ''.join(out)

    def context(self, b, passages):
        out = ['<h2 id="boundary-context">Boundary and area evidence</h2>'
               '<details class="comparison-details"><summary>Inspect recorded boundary candidates and membership</summary>']
        if b in self.naples_ids:
            for r in self.boundaries['scenarios']:
                if r['battle_id'] != b:
                    continue
                anchor = next(e for e in self.boundaries['events'] if e['id'] == r['anchor_event_id'])
                out.append(self.record(r['id'], r['label'], [('Contact status', r['contact_status']),
                                       ('Anchor event', anchor['assertion_en']), ('Source date', anchor['date_label']),
                                       ('Source time', anchor['time_label']), ('Area', r['area']), ('Unknowns', r['unknowns'])],
                                       passages.refs('boundary', r['evidence'])))
            for r in self.boundaries['membership_cases']:
                if r['battle_id'] == b:
                    out.append(self.record(r['id'], f'Side {r["side"]}: {r["label"]}',
                                           [(key.replace('_', ' ').capitalize(), r[key]) for key in
                                            ('scenario_id', 'timing', 'area', 'assignment', 'decision', 'note')],
                                           passages.refs('boundary', r['evidence'])))
        else:
            entry = next(r for r in self.peninsula['entries'] if r['battle_id'] == b)
            out.append(facts([('Proposed area', entry['area']), ('Stopping reason', entry['stopping_reason'])]))
            for r in entry['boundary_candidates']:
                out.append(self.record(r['id'], r['label'], [('Reported time', r['reported_time']), ('Status', r['status'])],
                                       passages.refs('peninsula', r['evidence'])))
        out.append('</details>')
        if b in self.naples_ids:
            out.append('<details class="comparison-details"><summary>Inspect identity and army-continuity notes</summary>')
            for r in self.authority['identity_links']:
                if not any(b in self.packages['authority'][m['passage_id']]['battle_ids'] for m in r['mentions']):
                    continue
                out.append(self.record(r['id'], r['status'].replace('_', ' '),
                                       [('Source labels', [m['label'] for m in r['mentions']]), ('Basis', r['basis']),
                                        ('Resolved person', r['resolved_person_id']), ('Finding', r['note'])],
                                       passages.refs('authority', [m['passage_id'] for m in r['mentions']])))
            for r in self.authority['organization_context'] + self.authority['continuity_pairs']:
                if any(fid.startswith(b + '-') for fid in r['force_ids']):
                    out.append(self.record(r['id'], 'Organization and continuity',
                                           [(key.replace('_', ' ').capitalize(), r[key]) for key in
                                            ('force_ids', 'assertion_en', 'status', 'army_id', 'missing_evidence', 'note') if key in r],
                                           passages.refs('authority', r['evidence'])))
            out.append('</details>')
        return ''.join(out)

    def engagement(self, b):
        entry = self.napoleonic.entries[b]
        passages = Passages(self.site, self.packages)
        out = ['<p><a href="index.html">All 12 comparisons</a> · '
               f'<a href="../engagements/{b}.html">Full dossier</a></p>'
               f'<h1>Compare sources: {esc(entry["place"])} <span class="muted">{b}</span></h1>'
               f'<p>{self.napoleonic.campaign_link(entry["campaign_group"], "../../")} · '
               f'Frozen frame: {esc(entry["start_date"])} to {esc(entry["end_date"])}</p>'
               '<p>Side A is France and its allies; side B is the opponent. Figures retain their source-specific '
               'population and phase. Differences can concern scope or timing as well as value. '
               'Unknown counts remain unknown; equipment counts remain equipment.</p>'
               '<p class="jump-links"><a href="#strength">Strength observations</a> · '
               '<a href="#authority">Command roles</a> · <a href="#compatibility">Compatibility findings</a> · '
               '<a href="#mapping">Opening comparison</a> · <a href="#boundary-context">Boundary evidence</a> · '
               '<a href="#supporting-passages">Supporting passages</a></p>'
               '<div class="card">The existing pilot leaves both opening mappings unresolved. '
               'These primary-verified research records select no model input or commander credit. '
               'Wider extraction remains paused.</div>']
        for kind, title, render in [('strength', 'Strength observations', self.strength),
                                    ('authority', 'Command roles', self.role)]:
            out.append(f'<h2 id="{kind}">{title}</h2><div class="comparison-sides">')
            for side in ('A', 'B'):
                records = [r for r in self.observations(b, kind) if r['side'] == side]
                out.append(f'<section data-side="{side}" data-kind="{kind}"><h3>Side {side} · {len(records)} observations</h3>')
                out.extend(render(r, passages) for r in records)
                out.append('</section>')
            out.append('</div>')
        out.extend([self.findings(b, passages), self.readiness(b), self.context(b, passages), passages.render()])
        paths = (LEDGER, BOUNDARIES, AUTHORITY) if b in self.naples_ids else (PENINSULA,)
        out.append('<h2>Versioned measurement records</h2><ul>' + ''.join(
            f'<li><a href="{esc(self.site.blob(path))}">{esc(path.removeprefix(BASE))}</a></li>' for path in paths) + '</ul>')
        self.site.write(f'napoleonic/comparisons/{b}.html', f'Compare sources: {entry["place"]}', ''.join(out), 2)
