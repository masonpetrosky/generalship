"""Apply the bounded TN003-R1--R4 migration from immutable local snapshots.

No fetching or model calls. Re-running checks identical outputs; divergent live
inputs or prior outputs are rejected before any write.
"""

import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from generalship.sources import digest, read_json, source_metadata_digest, verify_sources

BUNDLE = "TN003-a42f063-v1"
REVIEW = "artifacts/review-results/TN003-a42f063-astra-xhigh-v1"
DOSSIER = "data/evidence/TN003.json"
REGISTRY = "data/sources.json"
ARCHIVE = "data/evidence/history/TN003.v5.json"
LEDGER = "artifacts/migrations/TN003-review-corrections-v1.json"
DOSSIER_SHA = "1107b7149f9aa3877478e003a01ae2383b5d0729a15d6a90106e427350d49780"
REGISTRY_SHA = "a71f16285be84504048826255c0abcb49488c5d96f8e048ca5259ad523cc0e8b"
REVIEW_SHA = "31f77766d967787ae9ca74e7098b8341a59285df9105c8bedbd7c2d0dde46fac"
SOURCE_IDS = {
    "or-ammen-crossing-v1": "or-ammen-crossing-v2",
    "or-nelson-reinforcements-v1": "or-nelson-reinforcements-v2",
    "or-union-return-detail-v2": "or-union-return-detail-v3",
}


def encode(value):
    return (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")


def citation(source_id, section, quote):
    return {"source_id": source_id, "section": section, "locator": section, "quote": quote}


def expected_outputs(root):
    config = read_json(root / f"reviews/{BUNDLE}/config.json")
    old_dossier_path = root / config["snapshot_copies"][DOSSIER]
    old_registry_path = root / config["snapshot_copies"][REGISTRY]
    if digest(old_dossier_path) != DOSSIER_SHA or digest(old_registry_path) != REGISTRY_SHA:
        raise ValueError("Frozen migration input checksum mismatch")
    old = read_json(old_dossier_path)
    dossier = copy.deepcopy(old)
    registry = read_json(old_registry_path)
    review_path = root / REVIEW / "review-result.json"
    # Hash in the original completed dispatch binds the actual response.
    dispatch = read_json(root / REVIEW / "dispatch.json")
    if digest(review_path) != REVIEW_SHA or REVIEW_SHA != dispatch["outputs"]["review-result.json"]["sha256"]:
        raise ValueError("Original review response checksum mismatch")
    review = read_json(review_path)
    if review["dossier_sha256"] != DOSSIER_SHA or review["review_completed"] is not True:
        raise ValueError("Migration requires the completed review of the exact prior dossier")
    findings = {f["id"]: f for f in review["findings"]}
    sources = {s["id"]: s for s in registry["sources"]}
    revisions = []
    for old_id, new_id in SOURCE_IDS.items():
        source = copy.deepcopy(sources[old_id])
        source["id"] = new_id
        source["supersedes"] = {"source_id": old_id, "metadata_sha256": source_metadata_digest(sources[old_id])}
        source["revision_kind"] = "metadata_only"
        source["revision_note"] = "TN003-R2: section-scoped document dates; same pinned raw bytes."
        if old_id == "or-union-return-detail-v2":
            source["revision_note"] = "TN003-R3: same OR p.112 return and facsimile; same pinned raw bytes."
            proposals = findings["TN003-R3"]["proposed_replacements"]
        else:
            source["editorial_sections"] = ["transcription-scope"]
            proposals = findings["TN003-R2"]["proposed_replacements"]
        for change in proposals:
            if change["source_id"] == old_id:
                if source.get(change["field"]) != change["current"]:
                    raise ValueError("Reviewed source field no longer matches migration input")
                source[change["field"]] = copy.deepcopy(change["proposed"])
        registry["sources"].append(source)
        revisions.append({"previous_id": old_id, "new_id": new_id,
                          "previous_metadata_sha256": source_metadata_digest(sources[old_id]),
                          "new_metadata_sha256": source_metadata_digest(source),
                          "raw_path": source["path"], "raw_sha256": source["sha256"]})

    claims = {c["id"]: c for c in dossier["claims"]}
    r4 = findings["TN003-R4"]["proposed_replacements"][0]
    if claims["crittenden-arrival-phases"]["value"] != r4["current"]:
        raise ValueError("Reviewed Crittenden claim no longer matches migration input")
    claims["crittenden-arrival-phases"]["value"] = r4["proposed"]
    explicit = {
        "force-sunday-engaged", "force-buell", "force-other", "handbook-nelson-leading",
        "rousseau-michigan-contingent", "grose-sunday-eight-companies", "reed-wagner-late-estimate",
    }
    reviewed_status = {
        p["field"].split("id=", 1)[1].split("]", 1)[0]: p["proposed"]
        for p in findings["TN003-R1"]["proposed_replacements"]
    }
    union_id = "reed-1909-union-audit-v1"
    ohio_id = "reed-1909-ohio-strength-v1"
    estimated = citation(union_id, "p97", "* Estimated.")
    approximated = citation(ohio_id, "p101", "* Approximated. Note j.")
    wagner = citation(ohio_id, "p102", "† Arrived at Shiloh just before the battle ended. Estimated.")
    extra = {
        "reed-eighteenth-wisconsin-estimate": [estimated],
        "reed-sixth-reconstruction": [citation(union_id, "p96", "18th Wisconsin* (note d) | 35 | 700 | 735"), estimated],
        "reed-mccook-detail-engaged": [approximated],
        "reed-mccook-recap-engaged": [citation(ohio_id, "p111-note-j", "I estimate McCook's present for duty at 7,552.")],
        "reed-crittenden-engaged": [approximated],
        "reed-wagner-late-estimate": [wagner],
        "reed-ohio-total-engaged": [citation(ohio_id, "p111-note-j", "The Second, Fifth, and Sixth Divisions are estimated from returns of March 20, March 31, and April 30, 1862."), wagner],
    }
    notes = {
        "explicit_estimate": "The cited wording or linked table note explicitly qualifies this observation as an estimate, approximation or probable range. Printed bounds are retained; no statistical error interval is inferred.",
        "aggregate_includes_estimates": "The printed total includes explicitly estimated components identified in the linked passages. Retain the printed total and mixed-date/overlap warnings; this is not a common-time census.",
        "reported_without_explicit_estimation_qualifier": "No explicit estimation qualifier for this particular observation appears in the inspected cited passage and its table notes. This describes the supplied evidence only, not measurement accuracy or the absence of estimation in underlying records.",
    }
    quantities = []
    for q in dossier["quantities"]:
        status = reviewed_status.get(q["id"], "explicit_estimate" if q["id"] in explicit else "reported_without_explicit_estimation_qualifier")
        q["estimation_status"] = status
        q["estimation_note"] = notes[status]
        if q["id"] == "force-wallace":
            q["estimation_note"] += " Force's 'sixty-five hundred' clause lacks the 'about' used for the adjacent contingents; the existing approximate precision label is retained separately."
        primary = copy.deepcopy(claims[q["claim_id"]]["citations"][q["citation_index"]])
        q["estimation_citations"] = [primary] + copy.deepcopy(extra.get(q["id"], []))
        quantities.append({"id": q["id"], "estimation_status": status})

    citation_updates = []
    for claim in dossier["claims"]:
        for index, c in enumerate(claim["citations"]):
            if c["source_id"] in SOURCE_IDS:
                before = c["source_id"]
                c["source_id"] = SOURCE_IDS[before]
                citation_updates.append({"claim_id": claim["id"], "citation_index": index,
                                         "previous_source_id": before, "new_source_id": c["source_id"]})
    for q in dossier["quantities"]:
        for c in q["estimation_citations"]:
            c["source_id"] = SOURCE_IDS.get(c["source_id"], c["source_id"])
    dossier["schema_version"] = 3
    dossier["revision"] = "shiloh-review-corrections-2026-09-20"
    dossier["supersedes"] = {"path": ARCHIVE, "sha256": DOSSIER_SHA}
    ledger = {
        "schema_version": 1, "migration_id": "TN003-review-corrections-v1",
        "command": "python3 scripts/migrate_shiloh_review_corrections.py",
        "basis_review_path": f"{REVIEW}/review-result.json",
        "basis_review_sha256": digest(review_path),
        "prior_dossier_sha256": DOSSIER_SHA, "prior_registry_sha256": REGISTRY_SHA,
        "dossier_sha256": hashlib.sha256(encode(dossier)).hexdigest(),
        "registry_sha256": hashlib.sha256(encode(registry)).hexdigest(),
        "archived_dossier": ARCHIVE, "source_metadata_revisions": revisions,
        "claim_source_id_updates": citation_updates,
        "quantity_estimation_classification": quantities,
        "claim_wording_change": {"claim_id": "crittenden-arrival-phases", "before": r4["current"], "after": r4["proposed"]},
        "resolved_implementation_findings": list(findings),
        "review_status": "implementation_only_focused_review_recorded_separately",
        "unchanged": ["all previously registered source records and raw files", "all printed quantity bounds and precision labels", "all events", "three null unknown claims", "all historical disputes and replacement boundaries", "frozen source review and bundle", "baseline model and cohort inputs"],
        "limits": "Estimation classification covers supplied passages, not unseen underlying records. This migration does not establish historical truth, resolve force alternatives or admit model features.",
    }
    return {DOSSIER: encode(dossier), REGISTRY: encode(registry),
            ARCHIVE: old_dossier_path.read_bytes(), LEDGER: encode(ledger)}


def migrate(root):
    verify_sources(root)
    outputs = expected_outputs(root)
    # Validate the entire write set before modifying any file.
    originals = {DOSSIER: DOSSIER_SHA, REGISTRY: REGISTRY_SHA}
    pending = []
    for relative, content in outputs.items():
        path = root / relative
        if path.exists():
            if path.read_bytes() == content:
                continue
            if relative not in originals or digest(path) != originals[relative]:
                raise ValueError(f"Refusing to replace divergent migration input/output: {relative}")
        elif relative in originals:
            raise ValueError(f"Required live migration input missing: {relative}")
        pending.append((path, content))
    for path, content in pending:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    return {"migration": "TN003-review-corrections-v1", "files_written": len(pending)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    print(json.dumps(migrate(args.root), indent=2))
