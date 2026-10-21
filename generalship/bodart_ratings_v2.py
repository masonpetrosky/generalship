"""One explicit alias-cleanup rerun using the frozen v1 solver and evaluation rules."""

import argparse
from pathlib import Path
import subprocess

from . import bodart_aliases as aliases
from . import bodart_ratings as v1
from .sources import digest, read_json, write_json

RUN = 'artifacts/bodart-ratings-v2.json'
REPORT = 'artifacts/bodart-ratings-v2.md'
CSV = 'artifacts/bodart-ratings-v2.csv'


def execute(root, cohort):
    v1.require(not (root / RUN).exists(), 'v2 run already exists; preserve it')
    rows = cohort['rows']
    model = v1.fit(rows)
    folds, predictions = [], []
    for decade in sorted({r['decade'] for r in rows}):
        train, test = [r for r in rows if r['decade'] != decade], [r for r in rows if r['decade'] == decade]
        joint, force = v1.fit(train), v1.fit(train, commanders=False)
        folds.append({'decade': decade, 'train_ids': [r['id'] for r in train], 'test_ids': [r['id'] for r in test],
                      'commander': joint, 'force_only': force})
        predictions += [{'id': r['id'], 'decade': decade, 'y': r['y'], 'commander': v1.predict(joint, r),
                         'force_only': v1.predict(force, r), 'equal_odds': .5,
                         'seen_labels': sum(u in joint['theta'] for u in (r['a'], r['b']))} for r in test]
    sensitivities = {}
    for name, rr, sd in [('prior_sd_0.5', rows, .5), ('prior_sd_2', rows, 2.),
                         ('checked_personnel_only', [r for r in rows if r['personnel_checked']], 1.)]:
        fitted = v1.fit(rr, theta_sd=sd)
        sensitivities[name] = {'rows': len(rr), 'ids': [r['id'] for r in rr], 'model': fitted,
                               'estimates': v1.estimates(rr, fitted)}
    return {'kind': 'bodart-provisional-ratings', 'version': 2, 'status': 'primary_verified_exploratory',
            'base_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip(),
            'input_sha256': {**cohort['input_sha256'], aliases.COHORT: digest(root / aliases.COHORT)},
            'model': model, 'estimates': v1.estimates(rows, model, intervals=True), 'folds': folds,
            'predictions': sorted(predictions, key=lambda r: r['id']), 'metrics': v1.metrics(predictions),
            'sensitivities': sensitivities}


def verify(root, cohort, run):
    v1.require(run['version'] == 2 and run['kind'] == 'bodart-provisional-ratings', 'v2 identity')
    v1.require(run['input_sha256'] == {**cohort['input_sha256'], aliases.COHORT: digest(root / aliases.COHORT)},
               'v2 binding population')
    for path, sha in run['input_sha256'].items():
        v1.require(digest(root / path) == sha, 'v2 changed bound file: ' + path)
    rows = cohort['rows']
    original = read_json(root / v1.COHORT)['rows']
    old_run = read_json(root / v1.RUN)
    v1.require([r['id'] for r in rows] == [r['id'] for r in original], 'v2 row population changed')
    v1.require(not {r['id'] for r in rows} & set(read_json(root / v1.RESERVATION)['reserved_final']), 'v2 final leak')
    models = [(rows, run['model'], True, 1.)]
    v1.require(v1.estimates(rows, run['model'], intervals=True) == run['estimates'], 'v2 estimate/interval accounting')
    predictions, heldout = [], []
    old_folds = {f['decade']: f for f in old_run['folds']}
    for fold in run['folds']:
        decade = fold['decade']
        train, test = [r for r in rows if r['decade'] != decade], [r for r in rows if r['decade'] == decade]
        v1.require(fold['train_ids'] == old_folds[decade]['train_ids'] == [r['id'] for r in train], 'v2 training scope')
        v1.require(fold['test_ids'] == old_folds[decade]['test_ids'] == [r['id'] for r in test], 'v2 holdout scope')
        models += [(train, fold['commander'], True, 1.), (train, fold['force_only'], False, 1.)]
        for r in test:
            heldout.append(r['id'])
            predictions.append({'id': r['id'], 'decade': decade, 'y': r['y'],
                                'commander': v1.predict(fold['commander'], r),
                                'force_only': v1.predict(fold['force_only'], r), 'equal_odds': .5,
                                'seen_labels': sum(u in fold['commander']['theta'] for u in (r['a'], r['b']))})
    v1.require(sorted(heldout) == sorted(r['id'] for r in rows), 'v2 missing/duplicate forecast')
    v1.require(sorted(predictions, key=lambda r: r['id']) == run['predictions'], 'v2 forecast mismatch')
    v1.require(v1.metrics(predictions) == run['metrics'], 'v2 metric mismatch')
    # Side reversal must leave force-only losses and squared errors invariant.
    for weighting in run['metrics']:
        for model in ('force_only', 'equal_odds'):
            for metric, value in run['metrics'][weighting][model].items():
                v1.require(abs(value - old_run['metrics'][weighting][model][metric]) < 1e-12, 'changed comparator')
    for name, sd in [('prior_sd_0.5', .5), ('prior_sd_2', 2.), ('checked_personnel_only', 1.)]:
        rr = rows if name != 'checked_personnel_only' else [r for r in rows if r['personnel_checked']]
        s = run['sensitivities'][name]
        v1.require(s['ids'] == [r['id'] for r in rr] and s['rows'] == len(rr), 'v2 sensitivity scope')
        v1.require(v1.estimates(rr, s['model']) == s['estimates'], 'v2 sensitivity accounting')
        models.append((rr, s['model'], True, sd))
    for rr, model, commanders, sd in models:
        v1.require(model['theta_sd'] == sd, 'v2 prior changed')
        v1.require(set(model['theta']) == ({r[s] for r in rr for s in ('a', 'b')} if commanders else set()),
                   'v2 model labels')
        v1.verify_model(rr, model)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument('--prepare', action='store_true')
    action.add_argument('--run', action='store_true')
    action.add_argument('--write', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    cohort = aliases.prepare(root)
    if args.prepare:
        if (root / RUN).exists():
            v1.require(cohort == read_json(root / aliases.COHORT), 'cannot revise fitted v2 cohort')
        write_json(root / aliases.COHORT, cohort)
        print('Alias preparation:', cohort['before'], '->', cohort['after'], '; no fit')
        return
    v1.require(cohort == read_json(root / aliases.COHORT), 'v2 prepared migration changed')
    if args.run:
        write_json(root / RUN, execute(root, cohort))
    run = read_json(root / RUN)
    verify(root, cohort, run)
    from .bodart_alias_report import report
    md, csv_data = report(root, cohort, run), v1.csv_text(run)
    if args.write or args.run:
        (root / REPORT).write_text(md, encoding='utf-8')
        (root / CSV).write_text(csv_data, encoding='utf-8')
    else:
        v1.require((root / REPORT).read_text(encoding='utf-8') == md, 'v2 report differs')
        v1.require((root / CSV).read_text(encoding='utf-8') == csv_data, 'v2 CSV differs')
    print(f'Bodart v2: {len(cohort["rows"])} rows; eight scoped alias groups; saved run primary-verified.')


if __name__ == '__main__':
    main()
