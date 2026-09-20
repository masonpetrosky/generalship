"""Validate claim provenance, preserving unknowns and alternative accounts."""

from datetime import date
import math

from .sources import read_csv, read_json, safe_path, verify_sources

DIMENSIONS = {"strength", "terrain", "logistics", "information", "objectives", "responsibility", "outcome"}
PHASES = {"inherited", "commander_created", "post_outcome", "unresolved"}


def citation_text(root, sources, citation):
    source = sources[citation["source_id"]]
    path = safe_path(root, source["path"])
    if source["format"] == "csv":
        key = citation["row_key"]
        if not key or set(key) != set(source["primary_key"]):
            raise ValueError("Citation must identify one full primary key")
        matches = [r for r in read_csv(path) if all(r.get(k) == v for k, v in key.items())]
        if len(matches) != 1:
            raise ValueError("Citation must resolve to exactly one source row")
        return matches[0][citation["column"]]
    if source["format"] == "text":
        if not citation.get("locator"):
            raise ValueError("Text citation requires a human-readable locator")
        return path.read_text(encoding="utf-8")
    raise ValueError("Unsupported evidence format")


def validate_dossier(root, dossier, sources=None):
    sources = sources or verify_sources(root)
    if dossier.get("schema_version") != 1 or dossier.get("status") not in {"draft", "reviewed"}:
        raise ValueError("Invalid dossier version or status")
    if dossier["battle_id"] not in read_json(root / "data/pilot/cohort.json")["battle_ids"]:
        raise ValueError("Dossier battle not in the pilot")
    for boundary in ("tactical_replacement_at", "campaign_replacement_at"):
        if dossier[boundary] is not None:
            date.fromisoformat(dossier[boundary])
    if not dossier.get("open_questions"):
        raise ValueError("Dossier needs explicit unresolved research questions")
    claims = dossier["claims"]
    if not claims or len({c["id"] for c in claims}) != len(claims):
        raise ValueError("Empty claims or duplicate claim IDs")
    if {c["dimension"] for c in claims} != DIMENSIONS:
        raise ValueError("Every research dimension must be populated or explicitly unknown")
    for claim in claims:
        if claim["phase"] not in PHASES or not claim.get("rationale"):
            raise ValueError("Claim requires phase and rationale")
        if claim["status"] not in {"supported", "unknown", "disputed"}:
            raise ValueError("Invalid claim status")
        if claim["status"] == "unknown":
            if claim["value"] is not None or claim["citations"]:
                raise ValueError("Unknown claims require null value and no invented evidence")
            continue
        if claim["value"] is None or not claim["citations"]:
            raise ValueError("Known or disputed claims require a value and citations")
        if isinstance(claim["value"], (int, float)) and not math.isfinite(claim["value"]):
            raise ValueError("Nonfinite claim value")
        for citation in claim["citations"]:
            quote = citation["quote"]
            if not quote.strip() or quote not in citation_text(root, sources, citation):
                raise ValueError(f"Supporting passage not found: {claim['id']}")
    if dossier["status"] == "reviewed":
        review = dossier.get("review", {})
        if not review.get("reviewer") or not review.get("decision"):
            raise ValueError("Reviewed dossier requires a named review record")
        date.fromisoformat(review["date"])
    return {"battle_id": dossier["battle_id"], "status": dossier["status"],
            "claims": len(claims), "unknown_claims": sum(c["status"] == "unknown" for c in claims),
            "note": "Passage matching verifies provenance, not historical truth or entailment."}


def validate_all(root):
    sources = verify_sources(root)
    paths = sorted((root / "data/evidence").glob("*.json"))
    if not paths:
        raise ValueError("No evidence dossiers found")
    dossiers = [read_json(path) for path in paths]
    if len({d["battle_id"] for d in dossiers}) != len(dossiers):
        raise ValueError("Duplicate battle dossier")
    return [validate_dossier(root, d, sources) for d in dossiers]
