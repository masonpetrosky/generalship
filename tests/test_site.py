"""The static explorer (generalship/site.py): it builds offline and every internal link and anchor resolves."""

from html.parser import HTMLParser
from collections import Counter
import html
from pathlib import Path
import re
import tempfile
import unittest
from urllib.parse import unquote, urlsplit

from generalship.site import build_site, markdown, slug
from generalship.sources import read_json

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.add(a['id'])
        for key in ('href', 'src'):
            if a.get(key):
                self.hrefs.append(a[key])


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name).resolve() / 'site'
        cls.result = build_site(ROOT, str(cls.out), 'abc123')
        cls.pages = {}
        for path in cls.out.rglob('*.html'):
            parser = Links()
            parser.feed(path.read_text(encoding='utf-8'))
            cls.pages[path] = parser

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_every_engagement_commander_and_campaign_has_a_page(self):
        cohort = read_json(ROOT / 'data/pilot/cohort-v2.json')['battle_ids']
        for b in cohort:
            self.assertTrue((self.out / f'engagements/{b}.html').is_file(), b)
        credited = {e['sides'][s]['commander_id'] for e in read_json(ROOT / 'data/command/responsibility-v2.json')['engagements']
                    for s in ('US', 'Confederate')} - {None}
        for c in credited:
            self.assertTrue((self.out / f'commanders/{c}.html').is_file(), c)
        self.assertEqual(self.result['pages'], len(self.pages))

    def test_every_internal_link_and_anchor_resolves(self):
        broken = []
        for path, parser in self.pages.items():
            for href in parser.hrefs:
                if href.startswith(('http://', 'https://', 'mailto:', 'data:')):
                    continue
                parsed = urlsplit(href)
                target, frag = unquote(parsed.path), parsed.fragment
                dest = (path.parent / target).resolve() if target else path
                if not dest.is_file():
                    broken.append((str(path.relative_to(self.out)), href))
                elif frag and dest.suffix == '.html' and frag not in self.pages[dest].ids:
                    broken.append((str(path.relative_to(self.out)), href))
        self.assertEqual(broken, [])

    def test_commander_comparison_preserves_negative_result_and_evidence_links(self):
        page = (self.out / 'results/artifacts-commander-comparison-v1.html').read_text()
        self.assertIn('a better ranking is not demonstrated', page)
        self.assertIn('301 scored battles', page)
        self.assertIn('91/313 saved commanders', page)
        self.assertIn('0.656313', page)
        self.assertIn('0.650044', page)
        self.assertEqual(page.count('https://masonpetrosky.github.io/generalship/commanders/'), 91)
        self.assertEqual(page.count(' †</a>'), 19)
        self.assertIn('not_connected', page)

    def test_surprise_explorer_links_only_scored_engagements_and_works_as_static_html(self):
        from generalship.napoleonic_surprises import RUN
        ids = {p['battle_id'] for p in read_json(ROOT / RUN)['populations']['primary']['leave_campaign_out']['predictions']}
        page = (self.out / 'napoleonic/surprises.html').read_text()
        self.assertEqual(set(re.findall('id="battle-([^"]+)"', page)), ids)
        self.assertEqual(page.count('class="sx-battle"'), 194)
        self.assertIn('194/273 development engagements', page)
        self.assertIn('79 lack an eligible pair', page)
        self.assertIn('not validated historical win probabilities', page)
        self.assertIn('<noscript>', page)
        for bid in read_json(ROOT / 'data/napoleonic/cohort-v1.json')['battle_ids']:
            dossier = (self.out / f'napoleonic/engagements/{bid}.html').read_text()
            self.assertEqual(f'../surprises.html?q={bid}#battle-{bid}' in dossier, bid in ids)
        self.assertIn('surprises.html', (self.out / 'napoleonic/index.html').read_text())

    def test_surprise_cards_keep_winner_orientation_and_original_strength_labels(self):
        from generalship.napoleonic_surprises import DATA
        page = (self.out / 'napoleonic/surprises.html').read_text()
        for e in read_json(ROOT / DATA)['entries']:
            if not e['eligible']:
                continue
            card = re.search('<article class="sx-battle" id="battle-' + e['battle_id'] + '"(.*?)</article>', page, re.S).group(1)
            for side in ('A', 'B'):
                self.assertIn(html.escape(e['sides'][side]['printed']), card)
            self.assertIn(f'engagements/{e["battle_id"]}.html#dimension-strength', card)
            self.assertIn(f'engagements/{e["battle_id"]}.html#dimension-outcome', card)
            self.assertIn('/blob/abc123/' + DATA, card)
        self.assertTrue((self.out / 'napoleonic/surprises.css').is_file())
        self.assertTrue((self.out / 'napoleonic/surprises.js').is_file())

    def test_a_claim_shows_its_passage_source_and_hash(self):
        page = (self.out / 'engagements/VA111.html').read_text(encoding='utf-8')
        sha = read_json(ROOT / 'data/sources.json')['sources']
        source = next(s for s in sha if s['id'] == 'arnold-cwsac-forces')
        self.assertIn('<blockquote>8,500</blockquote>', page)
        self.assertIn(source['sha256'][:12], page)
        self.assertIn('https://github.com/masonpetrosky/generalship/blob/abc123/' + source['path'], page)

    def test_napoleonic_cohort_and_complete_groups_are_browsable(self):
        cohort = read_json(ROOT / 'data/napoleonic/cohort-v1.json')
        entries = {e['id']: e for e in read_json(ROOT / 'data/napoleonic/frame-v1.json')['entries']}
        pages = self.out / 'napoleonic'
        self.assertEqual({p.stem for p in (pages / 'engagements').glob('*.html')}, set(cohort['battle_ids']))
        self.assertEqual({p.stem for p in (pages / 'campaigns').glob('*.html')},
                         {slug(group) for group in cohort['campaign_groups']})
        index = (pages / 'engagements.html').read_text()
        for b in cohort['battle_ids']:
            group = entries[b]['campaign_group']
            self.assertIn(f'engagements/{b}.html', index)
            self.assertIn(f'engagements/{b}.html', (pages / 'campaigns' / f'{slug(group)}.html').read_text())
        overview = (pages / 'index.html').read_text()
        self.assertIn('325/325 draft dossiers', overview)
        self.assertIn('16 campaign groups', overview)

    def test_every_napoleonic_claim_preserves_value_rationale_and_passages(self):
        ids = read_json(ROOT / 'data/napoleonic/cohort-v1.json')['battle_ids']
        sources = {s['id']: s for s in read_json(ROOT / 'data/sources.json')['sources']}
        statuses = Counter()
        for b in ids:
            d = read_json(ROOT / f'data/napoleonic/evidence/{b}.json')
            path = self.out / f'napoleonic/engagements/{b}.html'
            rendered = path.read_text()
            self.assertIn('Draft claims are not admitted predictors', rendered)
            self.assertNotIn('Latest Civil War rating run', rendered)
            self.assertIn('Unestablished', rendered)
            for c in d['claims']:
                with self.subTest(battle=b, claim=c['id']):
                    self.assertIn(f'claim-{c["id"]}', self.pages[path].ids)
                    self.assertIn(html.escape(c['rationale']), rendered)
                    if c['value'] is None:
                        self.assertIn('Unknown — not established by the inspected evidence.', rendered)
                    else:
                        self.assertIn(html.escape(c['value']), rendered)
                    for cite in c['citations']:
                        src = sources[cite['source_id']]
                        self.assertIn(html.escape(cite['quote']), rendered)
                        self.assertIn(f'../../sources.html#{cite["source_id"]}', rendered)
                        self.assertIn(src['sha256'], rendered)
                        self.assertIn('/blob/abc123/' + src['path'], rendered)
                statuses[c['status']] += 1
        self.assertEqual(statuses, {'supported': 3621, 'disputed': 140, 'unknown': 1085})

    def test_napoleonic_force_labels_preserve_both_compiler_orientations(self):
        ids = set(read_json(ROOT / 'data/napoleonic/cohort-v1.json')['battle_ids'])
        entries = [e for e in read_json(ROOT / 'data/napoleonic/frame-v1.json')['entries'] if e['id'] in ids]
        for orientation in ['winner', 'loser']:
            e = next(e for e in entries if e['french_side'] == orientation)
            page = (self.out / f'napoleonic/engagements/{e["id"]}.html').read_text()
            self.assertIn('<td>A</td><td>' + html.escape(e[f'{orientation}_text']), page)
            self.assertIn('not resolved identities, selected opening strengths or automatic command credit', page)

    def test_measurement_comparisons_cover_exactly_the_two_complete_pilots(self):
        ids = {'B370c', 'B370d', 'B371a', 'B379c', 'B430a', 'B430b', 'B430c', 'B431a',
               'B431b', 'B432a', 'B432b', 'B441a'}
        pages = self.out / 'napoleonic/comparisons'
        self.assertEqual({p.stem for p in pages.glob('*.html')}, ids | {'index'})
        index = (pages / 'index.html').read_text()
        self.assertIn('12 engagements · 24 sides', index)
        self.assertIn('do not estimate corpus-wide feasibility', index)
        for b in read_json(ROOT / 'data/napoleonic/cohort-v1.json')['battle_ids']:
            dossier = (self.out / f'napoleonic/engagements/{b}.html').read_text()
            self.assertEqual(f'../comparisons/{b}.html' in dossier, b in ids)
            if b in ids:
                self.assertIn(f'{b}.html', index)
                page = (pages / f'{b}.html').read_text()
                self.assertIn('both opening mappings unresolved', page)
                self.assertIn('select no model input or commander credit', page)
                self.assertIn('mapping-A', self.pages[pages / f'{b}.html'].ids)
                self.assertIn('mapping-B', self.pages[pages / f'{b}.html'].ids)
                self.assertNotIn('>None<', page)
        self.assertIn('comparisons/index.html', (self.out / 'napoleonic/index.html').read_text())

    def comparison_card(self, battle, observation):
        page = (self.out / f'napoleonic/comparisons/{battle}.html').read_text()
        match = re.search(r'<article class="observation" id="observation-' + re.escape(observation) + r'">(.*?)</article>',
                          page, re.S)
        self.assertIsNotNone(match, (battle, observation))
        return match.group(1), page

    def test_comparisons_keep_every_strength_population_time_and_explicit_gap(self):
        ledger = read_json(ROOT / 'data/napoleonic/ledger-design-v1/examples.json')
        peninsula = read_json(ROOT / 'data/napoleonic/peninsula-1812-measurement-v1/records.json')
        observations = ledger['strength_records'] + [r for r in peninsula['observations'] if r['kind'] == 'strength']
        unknowns = 0
        for r in observations:
            card, page = self.comparison_card(r['battle_id'], r['id'])
            for key in ('population', 'basis', 'state_description', 'boundary_relation', 'derivation',
                        'population_or_scope', 'reported_time', 'source_role', 'note'):
                if r.get(key):
                    self.assertIn(html.escape(r[key]), card, (r['id'], key))
            missing = r['amount']['kind'] == 'unknown' if 'amount' in r else r['value'] is None
            if missing:
                unknowns += 1
                self.assertIn('<h4>Unknown people</h4>', card)
                self.assertNotIn('<h4>0 people</h4>', card)
            for ref in re.findall(r'href="#(passage-\d+)"', card):
                self.assertIn(ref, self.pages[self.out / f'napoleonic/comparisons/{r["battle_id"]}.html'].ids)
        self.assertEqual(len(observations), 82)
        self.assertEqual(unknowns, 9)
        # Source precision, equipment and inhabitants must survive the shared display path.
        for b, rid, label in [('B370d', 'B370d-A-bunbury-more-than', '&gt; 6,000 people'),
                              ('B371a', 'B371a-A-koch-lacour-bound', '≤ 2,400 people'),
                              ('B371a', 'B371a-B-koch-garrison-bound', '&lt; 6,000 people'),
                              ('B379c', 'B379c-B-koch-guns', '4–5 guns'),
                              ('B432b', 'B432b-A-s02', 'About 48,500 people')]:
            card, _ = self.comparison_card(b, rid)
            self.assertIn(f'<h4>{label}</h4>', card)
        inhabitants, _ = self.comparison_card('B379c', 'B379c-B-colletta-inhabitants')
        self.assertIn('town_population', inhabitants)
        self.assertIn('not established as defenders', inhabitants)

    def test_comparisons_keep_every_authority_scope_and_unresolved_identity(self):
        authority = read_json(ROOT / 'data/napoleonic/authority-v1/mappings.json')
        peninsula = read_json(ROOT / 'data/napoleonic/peninsula-1812-measurement-v1/records.json')
        roles = authority['roles'] + [r for r in peninsula['observations'] if r['kind'] == 'authority']
        self.assertEqual(len(roles), 73)
        for r in roles:
            card, _ = self.comparison_card(r['battle_id'], r['id'])
            for key in ('actor_label', 'authority_type', 'force_scope', 'population_or_scope', 'reported_time', 'note'):
                if key in r:
                    self.assertIn(html.escape(r[key]), card, (r['id'], key))
            self.assertIn('<dt>Resolved person identity</dt><dd><span class="muted">Unestablished</span>', card)
        franceschi, _ = self.comparison_card('B371a', 'B371a-A-capitulation-franceschi')
        self.assertIn('delegated_negotiation', franceschi)
        self.assertIn('do not establish exclusive siege command', franceschi)

    def test_comparison_observations_link_to_their_own_exact_passages_and_hashes(self):
        sources = {s['id']: s for s in read_json(ROOT / 'data/sources.json')['sources']}
        ledger = read_json(ROOT / 'data/napoleonic/ledger-design-v1/examples.json')
        authority = read_json(ROOT / 'data/napoleonic/authority-v1/mappings.json')
        peninsula = read_json(ROOT / 'data/napoleonic/peninsula-1812-measurement-v1/records.json')
        groups = [(ledger['strength_records'], None), (authority['roles'], authority['passages']),
                  (peninsula['observations'], peninsula['passages'])]
        for records, passages in groups:
            indexed = {p['id']: p for p in passages} if passages else None
            for r in records:
                card, page = self.comparison_card(r['battle_id'], r['id'])
                linked = [re.search(r'<article class="passage" id="' + pid + r'">(.*?)</article>', page, re.S).group(1)
                          for pid in re.findall(r'href="#(passage-\d+)"', card)]
                for evidence in r['evidence']:
                    passage = indexed[evidence] if indexed else evidence
                    cite = passage['citation']
                    src = sources[cite['source_id']]
                    matches = [p for p in linked if '<blockquote>' + html.escape(cite['quote']) + '</blockquote>' in p
                               and html.escape(cite['source_id']) in p and html.escape(cite['locator']) in p]
                    self.assertTrue(matches, r['id'])
                    block = matches[0]
                    self.assertIn(src['sha256'], block)
                    self.assertIn('/blob/abc123/' + src['path'], block)
                    image_id = passage.get('facsimile_source_id') or passage.get('image_source_id')
                    if image_id:
                        image = sources[image_id]
                        self.assertIn(image['sha256'], block)
                        self.assertIn('/blob/abc123/' + image['path'], block)
                if not r['evidence']:
                    self.assertIn('Explicit evidence gap; no supporting passage indexed.', card)

    def test_comparison_findings_preserve_disagreements_and_non_admitted_arithmetic(self):
        ledger = read_json(ROOT / 'data/napoleonic/ledger-design-v1/examples.json')
        authority = read_json(ROOT / 'data/napoleonic/authority-v1/mappings.json')
        boundaries = read_json(ROOT / 'data/napoleonic/boundaries-v1/records.json')
        peninsula = read_json(ROOT / 'data/napoleonic/peninsula-1812-measurement-v1/records.json')
        for records in (ledger['discrepancies'], ledger['sum_proposals'], authority['reconciliations'],
                        boundaries['scenarios'], boundaries['membership_cases'], peninsula['co_reports'], peninsula['arithmetic_checks']):
            for r in records:
                path = self.out / f'napoleonic/comparisons/{r["battle_id"]}.html'
                self.assertIn('record-' + r['id'], self.pages[path].ids)
                if r.get('note'):
                    self.assertIn(html.escape(r['note']), path.read_text())
        rodrigo = (self.out / 'napoleonic/comparisons/B430a.html').read_text()
        self.assertIn('Not a candidate strength.', rodrigo)
        self.assertIn('No local strength-role association indexed for this entry.', rodrigo)
        gaeta = (self.out / 'napoleonic/comparisons/B371a.html').read_text()
        self.assertIn('same-side status', gaeta.lower())
        self.assertIn('Source labels', gaeta)

    def outcome_card(self, battle, record, kind):
        page = (self.out / f'napoleonic/outcomes/{battle}.html').read_text()
        match = re.search(r'<article class="observation" id="' + kind + '-' + re.escape(record)
                          + r'">(.*?)</article>', page, re.S)
        self.assertIsNotNone(match, (battle, record))
        return match.group(1), page

    def test_outcome_views_keep_separate_complete_pilots_and_navigation(self):
        loss = read_json(ROOT / 'data/napoleonic/loss-pilot-v1/observations.json')
        objective = read_json(ROOT / 'data/napoleonic/objective-pilot-v1/observations.json')
        loss_ids = {e['battle_id'] for e in loss['entries']}
        objective_ids = set(objective['entry_ids'])
        self.assertFalse(loss_ids & objective_ids)
        pages = self.out / 'napoleonic/outcomes'
        self.assertEqual({p.stem for p in pages.glob('*.html')}, loss_ids | objective_ids | {'index', 'losses', 'objectives'})
        index = (pages / 'index.html').read_text()
        self.assertIn('26 of 325 cohort entries', index)
        self.assertIn('do not estimate corpus-wide feasibility', index)
        self.assertIn('proposition counts are not success counts', index)
        self.assertIn('outcomes/index.html', (self.out / 'napoleonic/index.html').read_text())
        for b in read_json(ROOT / 'data/napoleonic/cohort-v1.json')['battle_ids']:
            dossier = (self.out / f'napoleonic/engagements/{b}.html').read_text()
            self.assertEqual(f'../outcomes/{b}.html' in dossier, b in loss_ids | objective_ids)
            if b in loss_ids | objective_ids:
                page = (pages / f'{b}.html').read_text()
                self.assertIn(f'../engagements/{b}.html', page)
                self.assertIn('side-A', self.pages[pages / f'{b}.html'].ids)
                self.assertIn('side-B', self.pages[pages / f'{b}.html'].ids)
                self.assertNotIn('>None<', page)
                self.assertIn('no common grade or commander credit', page)
        for year, path in [(1805, 'losses'), (1806, 'objectives')]:
            campaign = (self.out / f'napoleonic/campaigns/third-coalition-{year}.html').read_text()
            self.assertIn(f'../outcomes/{path}.html', campaign)

    def test_loss_view_preserves_all_quantities_scopes_unknowns_and_conditions(self):
        data = read_json(ROOT / 'data/napoleonic/loss-pilot-v1/observations.json')
        count = 0
        for e in data['entries']:
            page = (self.out / f'napoleonic/outcomes/{e["battle_id"]}.html').read_text()
            for side, r in e['sides'].items():
                for field in ('time_scope', 'population_scope'):
                    self.assertIn(html.escape(r[field].replace('_', ' ')), page)
                for note in r['notes']:
                    self.assertIn(html.escape(note), page)
                for q in r['quantities']:
                    count += 1
                    card, _ = self.outcome_card(e['battle_id'], q['id'], 'quantity')
                    for field in ('literal', 'population', 'qualifier', 'basis'):
                        value = q[field] if field == 'literal' else q[field].replace('_', ' ')
                        self.assertIn(html.escape(value), card, (q['id'], field))
                    self.assertIn(f'{q["value"]:,} {q["unit"].replace("_", " ")}', card)
                    if q.get('note'):
                        self.assertIn(html.escape(q['note']), card)
                    for field in ('explicit_subset_denominator', 'direct_source_denominator'):
                        if field in q:
                            self.assertIn(html.escape(q[field]['literal']), card)
                            self.assertIn(html.escape(q[field]['population'].replace('_', ' ')), card)
                    for pid in q['evidence']:
                        self.assertIn(f'href="#passage-{pid}"', card)
                condition = r['surrender_condition']
                if condition:
                    self.assertIn(html.escape(condition['kind'].replace('_', ' ')), page)
                    if condition.get('note'):
                        self.assertIn(html.escape(condition['note']), page)
        self.assertEqual(count, 140)
        unknown = (self.out / 'napoleonic/outcomes/B368d.html').read_text()
        self.assertEqual(unknown.count('Unknown numerical loss.'), 2)
        self.assertNotIn('4,000 people</h4>', unknown)
        self.assertIn('conditional free withdrawal no capture count', unknown)
        wertingen = (self.out / 'napoleonic/outcomes/B363a.html').read_text()
        self.assertIn('About 500 people', wertingen)
        self.assertIn('Officer subset: 52 people', wertingen)
        self.assertIn('Guns: 6 guns', wertingen)

    def test_loss_view_preserves_category_denominators_arithmetic_and_dossier_disputes(self):
        index = (self.out / 'napoleonic/outcomes/losses.html').read_text()
        self.assertIn('35/44 sides', index)
        self.assertIn('14/22 pairs', index)
        self.assertIn('<td>Killed and wounded</td><td>16/44</td><td>6/22</td>', index)
        self.assertIn('<td>Prisoners / captured</td><td>15/44</td><td>1/22</td>', index)
        self.assertIn('<td>Killed</td><td>0/44</td><td>0/22</td>', index)
        data = read_json(ROOT / 'artifacts/napoleonic-1805-loss-pilot-v1.json')
        for r in data['profile']['percent_checks']:
            page = (self.out / f'napoleonic/outcomes/{r["battle_id"]}.html').read_text()
            self.assertIn(html.escape(r['interpretation']), page)
            self.assertIn(f'<dt>Printed minus implied (percentage points)</dt><dd>{r["printed_minus_implied_pp"]}</dd>', page)
        for e in data['observations']['entries']:
            page = (self.out / f'napoleonic/outcomes/{e["battle_id"]}.html').read_text()
            for side in e['sides'].values():
                for rule in side['source_arithmetic']:
                    self.assertIn(html.escape(rule['interpretation']), page)
                    for qid in rule['parts'] + [rule['total']]:
                        self.assertIn(f'href="#quantity-{qid}"', page)
            for claim in e['existing_dossier']['outcome_claims']:
                self.assertIn(f'../engagements/{e["battle_id"]}.html#claim-{claim["claim_id"]}', page)
                self.assertIn(f' · {claim["status"]}</li>', page)
        self.assertEqual(len(data['profile']['existing_disputed_outcome_pointers']), 3)

    def test_objective_view_keeps_all_propositions_criteria_windows_and_evidence_roles(self):
        data = read_json(ROOT / 'data/napoleonic/objective-pilot-v1/observations.json')
        missing = 0
        for r in data['components']:
            card, page = self.outcome_card(r['battle_id'], r['id'], 'component')
            for field in ('objective', 'precedence_note', 'criterion_note', 'observed_result', 'result_window'):
                self.assertIn(html.escape(r[field]), card, (r['id'], field))
            for field in ('statement_kind', 'scope_level', 'reported_precedence', 'recording_provenance'):
                self.assertIn(html.escape(r[field].replace('_', ' ')), card, (r['id'], field))
            for limit in r['limits']:
                self.assertIn(html.escape(limit), card)
            if r['success_criterion'] is None:
                missing += 1
                self.assertIn('<dt>Success criterion</dt><dd><span class="muted">Unestablished</span>', card)
            else:
                self.assertIn(html.escape(r['success_criterion']), card)
            for field, heading in [('objective_evidence', 'Intention evidence'), ('result_evidence', None),
                                   ('context_evidence', 'Context evidence')]:
                for pid in r[field]:
                    self.assertIn(f'href="#passage-{pid}"', card)
                if heading and r[field]:
                    self.assertIn(heading, card)
            for battle in r['related_entries']:
                self.assertIn(f'href="{battle}.html"', card)
            self.assertIn('Unknown criteria or achievement are not failures', page)
        self.assertEqual(len(data['components']), 19)
        self.assertEqual(missing, 8)
        index = (self.out / 'napoleonic/outcomes/objectives.html').read_text()
        for text in ('7/8 sides', '1/8 has only inferred disposition', '0/8 has an adopted objective',
                     '8/19 success criteria', '6/39 adopted passages are OCR-only', '33/39 were checked',
                     'December 1806–February 1807'):
            self.assertIn(text, index)
        gaeta = (self.out / 'napoleonic/outcomes/B371a.html').read_text()
        self.assertIn('component-gaeta-early-defence', gaeta)
        self.assertIn('component-gaeta-hold', gaeta)
        self.assertIn('dix4iait jours*', gaeta)

    def test_outcome_passages_retain_exact_quotes_source_locators_renderings_and_hashes(self):
        sources = {s['id']: s for s in read_json(ROOT / 'data/sources.json')['sources']}
        loss = read_json(ROOT / 'data/napoleonic/loss-pilot-v1/observations.json')
        objective = read_json(ROOT / 'data/napoleonic/objective-pilot-v1/observations.json')
        pages = self.out / 'napoleonic/outcomes'
        cases = [('losses', c['id'], c) for c in loss['conventions']]
        cases += [(e['battle_id'], pid, loss['passages'][pid]) for e in loss['entries'] for pid in e['source_passages']]
        seen = set()
        for b in objective['entry_ids']:
            page = (pages / f'{b}.html').read_text()
            for pid in re.findall(r'<article class="passage" id="passage-([^"]+)"', page):
                cases.append((b, pid, objective['passages'][pid]))
                seen.add(pid)
        self.assertEqual(len(seen), 39)
        self.assertEqual(len(loss['passages']), 72)
        self.assertEqual(len(loss['conventions']), 7)
        for name, pid, r in cases:
            page = (pages / f'{name}.html').read_text()
            block = re.search(r'<article class="passage" id="passage-' + re.escape(pid) + r'">(.*?)</article>', page, re.S).group(1)
            c = r.get('citation', r)
            for field in ('quote', 'source_id', 'section', 'locator'):
                self.assertIn(html.escape(c[field]), block, (name, pid, field))
            self.assertIn('<blockquote>' + html.escape(c['quote']) + '</blockquote>', block)
            self.assertIn(r['raw_sha256'], block)
            if r.get('metadata_sha256'):
                self.assertIn(r['metadata_sha256'], block)
            self.assertIn('/blob/abc123/' + sources[c['source_id']]['path'], block)
            if r.get('english_rendering') or r.get('interpretation_en'):
                self.assertIn(html.escape(r.get('english_rendering') or r['interpretation_en']), block)
            images = r.get('images', [])
            if r.get('image_source_id'):
                images = [{'source_id': r['image_source_id'], 'sha256': r['image_sha256']}]
            self.assertEqual('OCR-only passage.' in block, not images)
            for image in images:
                self.assertIn(image['sha256'], block)
                self.assertIn('/blob/abc123/' + sources[image['source_id']]['path'], block)

    def test_prior_objective_citation_statuses_are_not_promoted_to_new_verification(self):
        data = read_json(ROOT / 'data/napoleonic/objective-pilot-v1/observations.json')
        count = 0
        for r in data['prior_objective_claims']:
            page = (self.out / f'napoleonic/outcomes/{r["battle_id"]}.html').read_text()
            self.assertIn(f'../engagements/{r["battle_id"]}.html#claim-{r["claim_id"]}', page)
            for c in r['citations']:
                count += 1
                self.assertIn(f'Citation {c["citation_index"]}: {c["source_id"]}', page)
                self.assertIn(html.escape(c['note']), page)
                self.assertIn(c['disposition'].replace('_', ' '), page)
        self.assertEqual(count, 49)

    def test_source_counts_include_both_research_cohorts(self):
        class SourceRows(HTMLParser):
            def __init__(self):
                super().__init__()
                self.rows, self.row, self.cell = [], None, None

            def handle_starttag(self, tag, attrs):
                if tag == 'tr':
                    self.row = []
                elif tag == 'td':
                    self.cell = []

            def handle_data(self, data):
                if self.cell is not None:
                    self.cell.append(data)

            def handle_endtag(self, tag):
                if tag == 'td':
                    self.row.append(''.join(self.cell))
                    self.cell = None
                elif tag == 'tr' and self.row:
                    self.rows.append(self.row)

        expected = Counter()
        for cohort_path, directory in [('data/pilot/cohort-v2.json', 'data/evidence'),
                                       ('data/napoleonic/cohort-v1.json', 'data/napoleonic/evidence')]:
            for b in read_json(ROOT / cohort_path)['battle_ids']:
                d = read_json(ROOT / directory / f'{b}.json')
                expected.update(c['source_id'] for claim in d['claims'] for c in claim['citations'])
        parsed = SourceRows()
        parsed.feed((self.out / 'sources.html').read_text())
        counts = {row[0]: int(row[4]) for row in parsed.rows}
        for sid, count in expected.items():
            self.assertEqual(counts[sid], count, sid)
        self.assertEqual(sum(counts.values()), sum(expected.values()))


class MarkdownTests(unittest.TestCase):
    def test_tables_lists_and_links(self):
        out = markdown('# T\n\n| A | B |\n| --- | ---: |\n| x | 1 |\n\n- one\n  - two\n- three [l](docs/x.md)\n', lambda t: 'L:' + t)
        self.assertIn('<h1 id="t">T</h1>', out)
        self.assertIn('<td class=n>1</td>', out)
        self.assertIn('<ul><li>one<ul><li>two</li></ul></li><li>three <a href="L:docs/x.md">l</a></li></ul>', out)

    def test_text_is_escaped(self):
        self.assertIn('&lt;script&gt;', markdown('a <script> b', lambda t: t))


if __name__ == '__main__':
    unittest.main()
