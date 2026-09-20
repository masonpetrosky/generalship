"""Package the frozen Shiloh review handoff offline; no model or network calls."""

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import sys
import zipfile

BUNDLE_ID = "TN003-a42f063-v1"
RECIPE = f"reviews/{BUNDLE_ID}"
OUTPUT = f"artifacts/review/{BUNDLE_ID}"


def sha(blob):
    return hashlib.sha256(blob).hexdigest()


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode()


def read(root, name):
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"Bundle path escapes repository: {name}")
    return path.read_bytes()


def coverage_template(dossier, sources, config):
    result = {
        "bundle_id": BUNDLE_ID,
        "dossier_sha256": config["expected_input_sha256"][config["dossier_path"]],
        "review_completed": False,
        "reviewer": {"identity": None, "type": None, "model_label": None, "date": None},
        "coverage_is_partial": None,
        "hash_verification": "not_performed",
        "findings": [],
        "additional_sources_inspected": [],
        "required_corrections": [],
        "unresolved_disputes": [],
        "further_review_needed": [],
        "feature_admission_design_recommendation": None,
    }
    for category in ("claims", "quantities", "events"):
        result[category] = [
            {"id": row["id"], "decision": "not_reviewed", "inspected_evidence": [],
             "finding_ids": [], "note": None} for row in dossier[category]
        ]
    scans = [{"id": s["id"], "path": s["path"], "sha256": s["sha256"],
              "snapshot_sections_to_compare": config["table_scan_sections"][s["id"]],
              "kind": "pinned_table_facsimile"}
             for s in sources if s["format"] in {"png", "image"}]
    scans += [{"id": s["id"], "path": s["path"], "sha256": s["sha256"],
               "snapshot_sections_to_compare": s["snapshot_sections_to_compare"],
               "kind": "supplementary_review_page"} for s in config["supplementary_pages"]]
    result["scan_checks"] = [dict(s, decision="not_reviewed", checked_sections_or_cells=[],
                                  finding_ids=[], note=None) for s in scans]
    result["coverage_totals"] = {
        category: {"total": len(result[category]), "checked": 0,
                   "partially_checked": 0, "not_reviewed": len(result[category]),
                   "cannot_verify": 0}
        for category in ("claims", "quantities", "events", "scan_checks")
    }
    return result


def context_text(payload, dossier, sources, config):
    cited = {c["source_id"] for claim in dossier["claims"] for c in claim["citations"]}
    lines = ["# Shiloh review context", "", "**Draft evidence; no review performed.**", "",
             f"Bundle: `{BUNDLE_ID}`. Evidence commit: `{config['evidence_commit']}`.",
             f"Dossier SHA-256: `{sha(payload[config['dossier_path']])}`.", "",
             "This text companion is complete for supplied claim/text comparison. Image-level",
             "transcription review requires opening the PNGs in the ZIP. All 50 registered",
             "source files are bundled, including uncited baseline/context files; they are",
             "not 50 independent historical witnesses. Full parent PDFs are not included.", "",
             "## Review index", "", "| Claim ID | Draft status | Quantity IDs | Event IDs |",
             "|---|---|---|---|"]
    for claim in dossier["claims"]:
        quantities = ", ".join(q["id"] for q in dossier["quantities"] if q["claim_id"] == claim["id"])
        events = ", ".join(e["id"] for e in dossier["events"] if claim["id"] in e["claim_ids"])
        lines.append(f"| {claim['id']} | {claim['status']} | {quantities or '-'} | {events or '-'} |")
    lines += ["", "## Current dossier", "", "```json", payload[config["dossier_path"]].decode().rstrip(),
              "```", "", "## Cited source snapshots", "",
              "Full selected-text snapshots follow, including their editorial scope notes.",
              "CSV evidence includes the complete cited row. Full original CSVs remain in the ZIP."]
    for source in sources:
        if source["id"] not in cited:
            continue
        lines += ["", f"### {source['id']}", "", f"Path: `{source['path']}`.",
                  f"SHA-256: `{source['sha256']}`.", ""]
        text = payload[source["path"]].decode()
        if source["format"] == "csv":
            rows = list(csv.DictReader(io.StringIO(text)))
            keys = [c["row_key"] for claim in dossier["claims"] for c in claim["citations"]
                    if c["source_id"] == source["id"]]
            selected = []
            for key in keys:
                matches = [r for r in rows if all(r[k] == v for k, v in key.items())]
                if len(matches) != 1:
                    raise ValueError(f"Unresolved CSV row in {source['id']}")
                if matches[0] not in selected:
                    selected.append(matches[0])
            lines += ["```json", json_bytes(selected).decode().rstrip(), "```"]
        else:
            lines += ["````text", text.rstrip(), "````"]
    lines += ["", "## Scan index", "", config["sampling_note"], "",
              "| ID | Image path from bundle root | Locator |", "|---|---|---|"]
    for source in sources:
        if source["format"] in {"png", "image"}:
            lines.append(f"| {source['id']} | `{source['path']}` | {source.get('locator', source['title'])} |")
    for page in config["supplementary_pages"]:
        lines.append(f"| {page['id']} | `{page['path']}` | Printed p.{page['printed_page']}; PDF p.{page['pdf_page_one_based']} |")
    lines += ["", "## Source registry", "", "```json", payload["data/sources.json"].decode().rstrip(),
              "```", "", "## Supplementary image provenance", "", "```json",
              json_bytes(config["supplementary_pages"]).decode().rstrip(), "```", ""]
    return "\n".join(lines).encode()


def verifier_bytes():
    return f'''"""Verify extracted bundle byte integrity; does not validate historical claims."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
manifest_path = "{OUTPUT}/MANIFEST.json"
manifest = json.loads((root / manifest_path).read_text())
for name, expected in manifest["payload_sha256"].items():
    path = (root / name).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise SystemExit("Missing or unsafe payload path: " + name)
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        raise SystemExit("Checksum mismatch: " + name)
print("Verified", len(manifest["payload_sha256"]), "files; no historical review implied.")
'''.encode()


def build(root, output=None):
    root = Path(root).resolve()
    output = Path(output) if output is not None else root / OUTPUT
    config_blob = read(root, f"{RECIPE}/config.json")
    config = json.loads(config_blob)
    if config["bundle_id"] != BUNDLE_ID:
        raise ValueError("Unexpected bundle recipe")
    payload = {}
    for name, expected in config["expected_input_sha256"].items():
        origin = config.get("snapshot_copies", {}).get(name, name)
        blob = read(root, origin)
        if sha(blob) != expected:
            raise ValueError(f"Frozen input changed: {name}; prepare a new version, do not relabel v1")
        payload[name] = blob
        if origin != name:
            payload[origin] = blob
    for page in config["supplementary_pages"]:
        blob = read(root, page["path"])
        if sha(blob) != page["sha256"]:
            raise ValueError(f"Review page checksum mismatch: {page['id']}")
        payload[page["path"]] = blob
    dossier = json.loads(payload[config["dossier_path"]])
    sources = json.loads(payload["data/sources.json"])["sources"]
    for source in sources:
        if source["path"] not in payload or sha(payload[source["path"]]) != source["sha256"]:
            raise ValueError(f"Source missing or changed: {source['id']}")
    if (len(dossier["claims"]), len(dossier["quantities"]), len(dossier["events"])) != (62, 40, 26):
        raise ValueError("Review scope differs from frozen assignment")
    prompt = read(root, f"{RECIPE}/prompt.md").decode().replace(
        "{{DOSSIER_SHA256}}", sha(payload[config["dossier_path"]]))
    template = coverage_template(dossier, sources, config)
    registry = {s["id"]: s for s in sources}
    for scan in template["scan_checks"]:
        for section in scan["snapshot_sections_to_compare"]:
            source = registry[section["source_id"]]
            marker = "\n## " + section["section"] + "\n"
            if payload[source["path"]].decode().count(marker) != 1:
                raise ValueError(f"Unresolved scan comparison section: {section}")
    start = f'''# Shiloh review bundle: start here

Prepared on {config['prepared_date']}; **review not yet performed**.

1. In a fresh review conversation, attach `{BUNDLE_ID}.zip` and paste the complete
   text of `PROMPT.md` (also available alongside the ZIP).
2. Ask the reviewer to open this archive. If ZIP access is unavailable, extract it
   locally and provide `CONTEXT.md`, `PROMPT.md`, `REVIEW-COVERAGE.json`, the source
   metadata and the 26 PNGs. Text-only access cannot complete the visual audit.
3. The prompt, context and blank coverage template live under `{OUTPUT}/`.
   Paths elsewhere in the bundle retain their repository layout. No repository,
   account, network fetch or paid job is needed to inspect the supplied evidence.
4. Optional byte verification: run `python3 verify_bundle.py` from the extracted root.
   Its standard-library check is not a signature or proof of historical truth.
5. Return the review narrative and completed `review-result.json` to the owner.
   Save the actual response and identity before reconciling individual findings.
   Do not promote the dossier or overwrite pinned inputs based on this template.

Contents: {len(sources)} registry entries and source files; 62 claims, 40 quantities,
26 events; 13 pinned table images and 13 supplementary page images; four prior
dossiers; methodology, source contract, research memos and baseline context.

{config['sampling_note']}

The parent PDFs are not bundled. The 13 additional PNGs are page copies rendered
from checksum-verified local parents, with printed/PDF locators in MANIFEST.json.
They do not add independent testimony or change the historical source registry.
The review remains incomplete wherever necessary passages or original images
cannot be inspected. A separate AI review is not human historical adjudication.

Rebuild in the source repository: `make review-bundle`. Inputs are pinned to the
recorded hashes. Mutable dossier/context files have frozen copies so later work
does not break reproduction. New evidence requires a separately versioned handoff.
'''
    generated = {"PROMPT.md": prompt.encode(), "CONTEXT.md": context_text(payload, dossier, sources, config),
                 "REVIEW-COVERAGE.json": json_bytes(template), "START-HERE.md": start.encode()}
    for name, blob in generated.items():
        payload[f"{OUTPUT}/{name}"] = blob
    payload["START-HERE.md"] = start.encode()
    payload["verify_bundle.py"] = verifier_bytes()
    payload[f"{RECIPE}/config.json"] = config_blob
    payload[f"{RECIPE}/prompt.md"] = read(root, f"{RECIPE}/prompt.md")
    payload["scripts/prepare_shiloh_review.py"] = read(root, "scripts/prepare_shiloh_review.py")
    manifest = {
        "bundle_id": BUNDLE_ID, "status": "prepared_only_review_not_performed",
        "evidence_commit": config["evidence_commit"], "dossier_revision": dossier["revision"],
        "dossier_sha256": sha(payload[config["dossier_path"]]),
        "source_registry_sha256": sha(payload["data/sources.json"]),
        "counts": {"claims": 62, "quantities": 40, "events": 26, "explicit_unknowns": 3,
                   "sources": len(sources), "table_scans": 13, "supplementary_pages": 13},
        "sampling_note": config["sampling_note"], "supplementary_pages": config["supplementary_pages"],
        "payload_sha256": {name: sha(blob) for name, blob in sorted(payload.items())},
        "manifest_note": "Hashes detect byte changes, not historical error or independent review. This manifest excludes itself to avoid a circular hash.",
    }
    generated["MANIFEST.json"] = json_bytes(manifest)
    payload[f"{OUTPUT}/MANIFEST.json"] = generated["MANIFEST.json"]
    archive = io.BytesIO()
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, blob in sorted(payload.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 9, 20, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, blob)
    archive_blob = archive.getvalue()
    archive_name = f"{BUNDLE_ID}.zip"
    generated[archive_name] = archive_blob
    generated["bundle.sha256"] = f"{sha(archive_blob)}  {archive_name}\n".encode()
    # Validate everything before writing any output; mismatch leaves the previous handoff intact.
    output.mkdir(parents=True, exist_ok=True)
    for name, blob in generated.items():
        (output / name).write_bytes(blob)
    return {"bundle": str(output / archive_name), "bytes": len(archive_blob),
            "sha256": sha(archive_blob), "payload_files": len(payload),
            "status": "prepared_only_review_not_performed"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.root, args.output), indent=2))
    except (OSError, ValueError, KeyError) as exc:
        print(f"review-bundle: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
