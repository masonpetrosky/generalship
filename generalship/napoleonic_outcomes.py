"""Read-only views of the two completed outcome pilots; no grading or admission."""

from .napoleonic_comparison import esc, facts
from .napoleonic_losses import ARTIFACT as LOSS_ARTIFACT, BASE as LOSS_BASE, REPORT as LOSS_REPORT
from .napoleonic_objectives import ARTIFACT as OBJECTIVE_ARTIFACT, BASE as OBJECTIVE_BASE, REPORT as OBJECTIVE_REPORT
from .sources import read_json

CATEGORIES = {
    'killed': 'Killed', 'wounded': 'Wounded', 'killed_and_wounded': 'Killed and wounded',
    'captured': 'Prisoners / captured', 'missing': 'Missing',
    'reported_personnel_total': 'Reported personnel total', 'personnel_percent': 'Printed personnel percentage',
    'officer_subset': 'Officer subset', 'guns': 'Guns', 'flags': 'Flags / eagles', 'other_material': 'Other material',
}
RELATIONS = {
    'reported_action_executed': 'Reported action carried out',
    'reported_effect_observed': 'Reported effect observed',
    'reported_effect_not_observed': 'Stated effect not observed in checked window',
    'reported_incomplete_or_mixed': 'Partial or qualified correspondence',
    'not_established': 'Achievement unestablished', 'not_assessable': 'Criterion unestablished',
}


def words(value):
    return value.replace('_', ' ') if isinstance(value, str) else value


def links(ids, prefix):
    return ' · '.join(f'<a href="#{prefix}-{esc(i)}">{esc(i)}</a>' for i in ids)


class OutcomePassages:
    """Retain each pilot's passage IDs, renderings, image limits and source bindings."""

    def __init__(self, site, records):
        self.site, self.records, self.used = site, records, {}

    def refs(self, ids):
        for pid in ids:
            self.used[pid] = self.records[pid]
        return '<p class="cite">Passages: ' + links(ids, 'passage') + '</p>' if ids else ''

    def render(self):
        out = ['<h2 id="supporting-passages">Supporting passages</h2>'
               '<p>Exact quotations from the completed pilot. Source families, page images and hashes '
               'remain attached to each passage. Repeated references are not independent witnesses.</p>']
        for pid, p in self.used.items():
            citation = p.get('citation') or {k: p[k] for k in ('source_id', 'section', 'locator', 'quote')}
            source = self.site.sources[citation['source_id']]
            images = p.get('images', [])
            if p.get('image_source_id'):
                images = [{'source_id': p['image_source_id'], 'sha256': p['image_sha256']}]
            out.append(f'<article class="passage" id="passage-{esc(pid)}"><h3>{esc(pid)}</h3>'
                       + self.site.citation(citation, '../../'))
            rendering = p.get('english_rendering') or p.get('interpretation_en')
            if rendering:
                out.append('<p><strong>Recorded English rendering:</strong> ' + esc(rendering) + '</p>')
            if p.get('note'):
                out.append('<p>' + esc(p['note']) + '</p>')
            if not images:
                out.append('<p class="muted"><strong>OCR-only passage.</strong> '
                           'No page image was inspected for this adopted passage in the pilot.</p>')
            image_bindings = []
            for image in images:
                meta = self.site.sources[image['source_id']]
                out.append(f'<p class="cite"><a href="{esc(self.site.blob(meta["path"]))}">Page image</a> · '
                           f'<a href="../../sources.html#{esc(image["source_id"])}">{esc(image["source_id"])}</a> · '
                           f'<code title="SHA-256: {esc(image["sha256"])}">{esc(image["sha256"][:12])}…</code></p>')
                image_bindings.append((image['source_id'] + ' SHA-256', image['sha256']))
                if image.get('metadata_sha256'):
                    image_bindings.append((image['source_id'] + ' metadata SHA-256', image['metadata_sha256']))
            out.append('<details class="comparison-details"><summary>Source provenance and hashes</summary>'
                       + facts([('Source family', source['independence_group']),
                                ('Raw SHA-256', p['raw_sha256']), ('Metadata SHA-256', p.get('metadata_sha256'))]
                               + ([('Section character range', p['character_range'])] if 'character_range' in p else [])
                               + image_bindings) + '</details></article>')
        return ''.join(out)


class OutcomePages:
    def __init__(self, napoleonic):
        self.napoleonic, self.site = napoleonic, napoleonic.site
        self.loss_bundle = read_json(self.site.root / LOSS_ARTIFACT)
        self.objective_bundle = read_json(self.site.root / OBJECTIVE_ARTIFACT)
        self.loss, self.objective = (b['observations'] for b in (self.loss_bundle, self.objective_bundle))
        self.loss_ids = {e['battle_id'] for e in self.loss['entries']}
        self.objective_ids = set(self.objective['entry_ids'])
        self.ids = self.loss_ids | self.objective_ids

    def write(self, name, title, body):
        self.site.write('napoleonic/outcomes/' + name + '.html', title, body, 2)

    def record_links(self, kind):
        base, report, artifact = ((LOSS_BASE, LOSS_REPORT, LOSS_ARTIFACT) if kind == 'loss' else
                                  (OBJECTIVE_BASE, OBJECTIVE_REPORT, OBJECTIVE_ARTIFACT))
        paths = [(report, 'Pilot report and stopping decision'), (base + 'observations.json', 'Observation record'),
                 (base + 'scope.json', 'Frozen scope'), (base + 'protocol.json', 'Measurement protocol'),
                 (artifact, 'Reproduced pilot bundle')]
        return '<h2>Versioned pilot records</h2><ul>' + ''.join(
            f'<li><a href="{esc(self.site.blob(p))}">{esc(title)}</a></li>' for p, title in paths) + '</ul>'

    def campaign_link(self, group):
        for bundle, path, label in ((self.loss_bundle, 'losses', 'Inspect this group’s loss evidence'),
                                    (self.objective_bundle, 'objectives', 'Inspect this group’s objectives and results')):
            if group == bundle['scope']['campaign_group']:
                return f'<p><a href="../outcomes/{path}.html">{label}</a></p>'
        return ''

    def battle_link(self, b):
        return f'<a href="{b}.html">{esc(self.napoleonic.entries[b]["place"])}</a> <span class="muted">{b}</span>'

    def build(self):
        self.write('index', 'Outcome evidence',
                   '<p><a href="../index.html">Napoleonic Wars</a></p><h1>Outcome evidence</h1>'
                   '<p>Two completed pilots, with separate evidence and denominators. '
                   'These 26 of 325 cohort entries were selected by complete development group; '
                   'they do not estimate corpus-wide feasibility.</p>'
                   '<div class="card"><h2><a href="losses.html">1805 loss evidence</a></h2>'
                   '<p>22 engagements · 44 sides · 140 typed quantities. '
                   'Inspect personnel categories, equipment, subsets, surrender terms and unknowns.</p></div>'
                   '<div class="card"><h2><a href="objectives.html">Naples objectives and results</a></h2>'
                   '<p>4 engagements · 8 sides · 19 source-qualified propositions. '
                   'Inspect stated intentions, their timing, reported results and unresolved criteria.</p></div>'
                   '<p>Both pilots retain useful descriptive components. Neither supports one common numerical grade. '
                   'Unknown is not zero or failure; proposition counts are not success counts. '
                   'Local results do not establish campaign contribution or commander credit.</p>'
                   '<p>These pages present existing primary-verified records. The pilots have stopped; '
                   'their coverage does not admit model inputs or authorize wider extraction.</p>')
        self.loss_index()
        self.objective_index()
        for entry in self.loss['entries']:
            self.loss_entry(entry)
        for b in self.objective['entry_ids']:
            self.objective_entry(b)

    def loss_index(self):
        from .site import table
        p = self.loss_bundle['profile']
        coverage = p['category_coverage']
        rows = [[CATEGORIES[c], f'{r["sides"]}/{r["side_denominator"]}',
                 f'{r["pairs"]}/{r["entry_denominator"]}'] for c, r in coverage.items()]
        entries = []
        missing = {tuple(k) for k in p['no_numeric_side_keys']}
        for e in self.loss['entries']:
            b = e['battle_id']
            entries.append([self.battle_link(b), esc(e['type_printed']),
                            *['Unknown personnel loss' if (b, s) in missing else 'Some personnel loss recorded'
                              for s in ('A', 'B')]])
        conventions = {c['id']: c for c in self.loss['conventions']}
        passages = OutcomePassages(self.site, conventions)
        body = ('<p><a href="index.html">Outcome evidence</a></p><h1>1805 loss evidence</h1>'
                '<p>Complete frozen third-coalition 1805 group: 22 engagements · 44 sides · '
                '140 typed quantities · one Bodart source family.</p>'
                '<div class="card"><strong>A common loss-based grade is unsupported across this group.</strong> '
                f'Some personnel-loss figure is recorded for {p["numeric_personnel_sides"]}/44 sides and '
                f'{p["any_numeric_pairs"]}/22 pairs. Numerical presence does not supply a common definition. '
                'Only 1/22 pairs has a source-declared killed/wounded-plus-prisoner total on both sides.</div>'
                '<h2>All-ranks category coverage</h2><p>Counts describe figures for the whole source side. '
                'Officer and national subsets, equipment and percentages are separate. '
                'Paired figures still need compatible population and time definitions.</p>'
                + table(['Category', 'Sides with a figure / 44', 'Paired entries / 22'], rows)
                + '<h2>All 22 engagements</h2><p>Side A is France and its allies; side B is the opponent. '
                'Every entry remains listed, including those without numerical losses. '
                'Printed winner/loser columns are provenance, not casualty-based outcome judgments.</p>'
                + table(['Engagement', 'Printed type', 'Side A', 'Side B'], entries)
                + '<h2 id="source-conventions">Source conventions</h2><p>Selection, winner coding, rounding and '
                'denominators limit interpretation of the entry tables. These seven passages share the same source family.</p>'
                + passages.refs(list(conventions)) + passages.render() + self.record_links('loss'))
        self.write('losses', '1805 loss evidence', body)

    def objective_index(self):
        from .site import table
        p = self.objective_bundle['profile']
        rows = []
        for b in self.objective['entry_ids']:
            components = [r for r in self.objective['components'] if r['battle_id'] == b]
            rows.append([self.battle_link(b), *[sum(r['side'] == s for r in components) for s in ('A', 'B')],
                         sum(r['success_criterion'] is None for r in components)])
        self.write('objectives', 'Naples objectives and results',
                   '<p><a href="index.html">Outcome evidence</a></p><h1>Naples objectives and results</h1>'
                   '<p>Complete frozen third-coalition 1806 group: 4 engagements · 8 sides · 19 propositions. '
                   'Amantea retains December 1806–February 1807. This source group is not one command appointment.</p>'
                   '<div class="card"><strong>Retain descriptive components; a common numerical grade is unsupported.</strong> '
                   f'{p["reported_before_action_sides"]}/8 sides have source-reported intent before the relevant action; '
                   f'{p["inferred_only_sides"]}/8 has only inferred disposition. '
                   '0/8 has an adopted objective supported by a supplied, dated pre-action document. '
                   'This concerns the inspected evidence; retrospective accounts can still support descriptive history.</div>'
                   f'<p>{len(p["missing_success_criteria"])}/19 success criteria remain unknown. '
                   f'{len(p["ocr_only_passage_ids"])}/{p["passages"]} adopted passages are OCR-only; '
                   f'{p["image_checked_passages"]}/{p["passages"]} were checked against pinned images. '
                   'Gaëta’s early refusal and late council intention stay separate. '
                   'Local capture, deployment, delay and pacification are different propositions and windows.</p>'
                   + table(['Engagement', 'Side A propositions', 'Side B propositions', 'Unknown criteria'], rows, {1, 2, 3})
                   + '<p>Relation labels are descriptive, not ordinal scores. Unknown is not failure, '
                   'and more propositions do not mean more success, opportunity or contribution. '
                   'Cross-entry references do not create extra battle weights.</p>' + self.record_links('objective'))

    def entry_header(self, b, kind, title):
        e = self.napoleonic.entries[b]
        index, label = ('losses', 'All 22 loss entries') if kind == 'loss' else ('objectives', 'All 4 objective entries')
        return (f'<p><a href="{index}.html">{label}</a> · '
                f'<a href="../engagements/{b}.html">Full dossier</a>'
                + (f' · <a href="../comparisons/{b}.html">Measurement comparison</a>'
                   if b in self.napoleonic.comparisons.ids else '') + '</p>'
                f'<h1>{esc(title)}: {esc(e["place"])} <span class="muted">{b}</span></h1>'
                f'<p>{self.napoleonic.campaign_link(e["campaign_group"], "../../")} · '
                f'Frozen frame: {esc(e["start_date"])} to {esc(e["end_date"])}</p>'
                '<p>Side A is France and its allies; side B is the opponent. '
                'Existing primary-verified pilot records; descriptive components, with no common grade or commander credit.</p>'
                '<p class="jump-links"><a href="#side-A">Side A evidence</a> · '
                '<a href="#side-B">Side B evidence</a> · <a href="#supporting-passages">Supporting passages</a></p>')

    def quantity(self, q, passages):
        fields = [('As printed', q['literal']), ('Population', words(q['population'])),
                  ('Precision', words(q['qualifier'])), ('Source basis', words(q['basis']))]
        extra = ''
        if q.get('applies_to'):
            extra += '<p>Percentage applies to: ' + links([q['applies_to']], 'quantity') + '</p>'
        for key in ('explicit_subset_denominator', 'direct_source_denominator'):
            if key in q:
                r = q[key]
                fields += [('Denominator use', words(key)), ('Printed denominator', r['literal']),
                           ('Denominator population', words(r['population']))]
                extra += passages.refs(r['evidence'])
        return (f'<article class="observation" id="quantity-{esc(q["id"])}">'
                f'<h4>{esc(CATEGORIES[q["category"]])}: {"About " if q["qualifier"] == "approximate" else ""}'
                f'{q["value"]:,} {esc(words(q["unit"]))}</h4><p class="record-id">{esc(q["id"])}</p>'
                + facts(fields) + (f'<p>{esc(q["note"])}</p>' if q.get('note') else '')
                + extra + passages.refs(q['evidence']) + '</article>')

    def loss_entry(self, e):
        b, p = e['battle_id'], self.loss_bundle['profile']
        passages = OutcomePassages(self.site, self.loss['passages'])
        out = [self.entry_header(b, 'loss', 'Loss evidence'),
               '<p>Combined counts are not split; subsets and equipment are not additional personnel. '
               'Printed sums and percentages retain their source discrepancies. Unknown is not zero.</p>'
               '<div class="comparison-sides">']
        for side, r in e['sides'].items():
            out.append(f'<section id="side-{side}"><h2>Side {side}</h2>'
                       + facts([('Printed source column', r['source_column']), ('Time scope', words(r['time_scope'])),
                                ('Population scope', words(r['population_scope']))]))
            out.extend('<p>' + esc(note) + '</p>' for note in r['notes'])
            out.append('<h3>Unknown all-ranks categories</h3><p>'
                       + ', '.join(CATEGORIES[c] for c in r['unstated_all_ranks_categories']) + '.</p>')
            if not r['quantities']:
                out.append('<p class="muted"><strong>Unknown numerical loss.</strong> No typed quantity is supplied for this side.</p>')
            out.extend(self.quantity(q, passages) for q in r['quantities'])
            if r['surrender_condition']:
                condition = r['surrender_condition']
                out.append('<h3>Surrender / release conditions</h3>'
                           + facts([('Reported condition', words(condition['kind'])), ('Limit', condition.get('note'))])
                           + passages.refs(condition['evidence']))
            for rule in r['source_arithmetic']:
                out.append('<details class="comparison-details"><summary>Printed sum and its limits</summary>'
                           '<p>Parts: ' + links(rule['parts'], 'quantity') + '. Total: '
                           + links([rule['total']], 'quantity') + '.</p><p>' + esc(rule['interpretation']) + '</p></details>')
            for check in p['percent_checks']:
                if (check['battle_id'], check['side']) == (b, side):
                    out.append('<details class="comparison-details"><summary>Printed percentage arithmetic</summary>'
                               + '<p>' + links([check['quantity_id']], 'quantity') + '</p>'
                               + facts([('Numerator (people)', check['numerator_people']),
                                        ('Denominator (people)', check['denominator_people']),
                                        ('Denominator basis', words(check['denominator_basis'])),
                                        ('Printed percent', check['printed_percent']), ('Implied percent', check['implied_percent']),
                                        ('Printed minus implied (percentage points)', check['printed_minus_implied_pp']),
                                        ('Interpretation', check['interpretation'])]) + '</details>')
            out.append('</section>')
        out.append('</div><h2>Existing outcome claims and disputes</h2>'
                   '<p>These are unchanged dossier pointers, not re-adjudicated evidence from this loss pilot.</p><ul>')
        out.extend(f'<li><a href="../engagements/{b}.html#claim-{esc(c["claim_id"])}">{esc(c["claim_id"])}</a>'
                   f' · {esc(c["status"])}</li>' for c in e['existing_dossier']['outcome_claims'])
        out.append('</ul><h2>Complete entry and footnote passages</h2>' + passages.refs(e['source_passages'])
                   + passages.render() + '<p><a href="losses.html#source-conventions">Read the seven source conventions</a></p>'
                   + self.record_links('loss'))
        self.write(b, 'Loss evidence: ' + e['place'], ''.join(out))

    def component(self, r, passages):
        fields = [('Statement kind', words(r['statement_kind'])), ('Scope', words(r['scope_level'])),
                  ('Reported timing', words(r['reported_precedence'])), ('Timing limit', r['precedence_note']),
                  ('Recording provenance', words(r['recording_provenance'])),
                  ('Supplied dated pre-action document', 'None supplied in the adopted evidence'),
                  ('Success criterion', r['success_criterion']), ('Criterion note', r['criterion_note']),
                  ('Literal criterion', r['criterion_literal']), ('Normalized duration (days)', r['normalized_duration_days'])]
        out = [f'<article class="observation" id="component-{esc(r["id"])}"><h3>{esc(r["objective"])}</h3>'
               f'<p class="record-id">{esc(r["id"])}</p>', facts(fields),
               '<h4>Intention evidence</h4>', passages.refs(r['objective_evidence']),
               '<h4>' + esc(RELATIONS[r['attainment']]) + '</h4><p>' + esc(r['observed_result']) + '</p>',
               facts([('Result window', r['result_window'])]), passages.refs(r['result_evidence']),
               '<h4>Limits</h4><ul>' + ''.join('<li>' + esc(limit) + '</li>' for limit in r['limits']) + '</ul>']
        if r['context_evidence']:
            out += ['<h4>Context evidence</h4>', passages.refs(r['context_evidence'])]
        if r['related_entries']:
            out.append('<p>Related entries: ' + ' · '.join(self.battle_link(b) for b in r['related_entries'])
                       + '. References retain context; they do not add engagement weights or establish causal credit.</p>')
        return ''.join(out) + '</article>'

    def objective_entry(self, b):
        passages = OutcomePassages(self.site, self.objective['passages'])
        out = [self.entry_header(b, 'objective', 'Objectives and results'),
               '<p>Reported earlier intent and the date of its recording are different. '
               'Unknown criteria or achievement are not failures. Relation labels have no numerical order.</p>'
               '<div class="comparison-sides">']
        for side in ('A', 'B'):
            rows = [r for r in self.objective['components'] if (r['battle_id'], r['side']) == (b, side)]
            label = 'proposition' if len(rows) == 1 else 'propositions'
            out.append(f'<section id="side-{side}"><h2>Side {side} · {len(rows)} {label}</h2>')
            out.extend(self.component(r, passages) for r in rows)
            out.append('</section>')
        out.append('</div><details class="comparison-details"><summary>Prior objective claims and citation dispositions</summary>'
                   '<p>The eight prior claims retain their dossier statuses. Prior-reference-only pointers are not '
                   'newly verified propositions. Citation indices below are zero-based, as in the saved record.</p>')
        for r in self.objective['prior_objective_claims']:
            if r['battle_id'] != b:
                continue
            out.append(f'<h3><a href="../engagements/{b}.html#claim-{esc(r["claim_id"])}">{esc(r["claim_id"])}</a>'
                       f' · {esc(r["status"])}</h3>')
            for c in r['citations']:
                out.append(f'<p>Citation {c["citation_index"]}: {esc(c["source_id"])} · {esc(c["section"])} · '
                           f'{esc(words(c["disposition"]))}. {esc(c["note"])}</p>' + passages.refs(c['adopted_passages']))
        out.append('</details>' + passages.render() + self.record_links('objective'))
        self.write(b, 'Objectives and results: ' + self.napoleonic.entries[b]['place'], ''.join(out))
