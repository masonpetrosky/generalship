"""Validate claim provenance, preserving unknowns and alternative accounts."""

from datetime import date
import math

from .sources import digest, read_csv, read_json, safe_path, verify_sources

DIMENSIONS = {"strength", "terrain", "logistics", "information", "objectives", "responsibility", "outcome"}
PHASES = {"inherited", "commander_created", "post_outcome", "unresolved"}
QUANTITY_BASES = {"present_for_duty", "reported_effective", "reported_engaged",
                  "reported_reinforcements", "reported_present"}


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
        text = path.read_text(encoding="utf-8")
        if source.get("sectioned"):
            section = citation.get("section")
            if not isinstance(section, str) or not section or "\n" in section:
                raise ValueError("Sectioned source requires one section ID")
            sections = text.split("\n## ")[1:]
            matches = [s.partition("\n")[2] for s in sections if s.partition("\n")[0] == section]
            if len(matches) != 1:
                raise ValueError("Citation section must resolve exactly once")
            return matches[0]
        return text
    raise ValueError("Unsupported evidence format")


def validate_dossier(root, dossier, sources=None):
    sources = sources or verify_sources(root)
    if dossier.get("schema_version") not in {1, 2} or dossier.get("status") not in {"draft", "reviewed"}:
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
    if dossier["schema_version"] == 2:
        validate_phase_records(root, dossier)
    elif any(key in dossier for key in ("entities", "events", "quantities")):
        raise ValueError("Phase records require schema version 2")
    if dossier["status"] == "reviewed":
        review = dossier.get("review", {})
        if not review.get("reviewer") or not review.get("decision"):
            raise ValueError("Reviewed dossier requires a named review record")
        date.fromisoformat(review["date"])
    return {"battle_id": dossier["battle_id"], "status": dossier["status"],
            "claims": len(claims), "unknown_claims": sum(c["status"] == "unknown" for c in claims),
            "quantities": len(dossier.get("quantities", [])), "events": len(dossier.get("events", [])),
            "note": "Passage matching verifies provenance, not historical truth or entailment."}


def validate_phase_records(root, dossier):
    """Check phase-record integrity without treating research observations as features."""
    def indexed(items, name):
        if not items or any(not isinstance(item.get("id"), str) or not item["id"].strip() for item in items):
            raise ValueError(f"Missing {name} IDs")
        result = {item["id"]: item for item in items}
        if len(result) != len(items):
            raise ValueError(f"Duplicate {name} IDs")
        return result

    claims = {c["id"]: c for c in dossier["claims"]}
    entities = indexed(dossier["entities"], "entity")
    for entity in entities.values():
        if (not entity.get("name") or entity["kind"] not in {"person", "formation"}
                or entity["side"] not in {"US", "CS"}):
            raise ValueError("Invalid entity identity")
    events = indexed(dossier["events"], "event")
    for event in events.values():
        date.fromisoformat(event["date"])
        if not event.get("time_label") or not event.get("note"):
            raise ValueError("Event requires time precision and interpretation")
        if not event["entity_ids"] or not set(event["entity_ids"]).issubset(entities):
            raise ValueError("Event references an unknown entity")
        if not event["claim_ids"] or any(c not in claims or claims[c]["status"] == "unknown" for c in event["claim_ids"]):
            raise ValueError("Event requires evidenced claim references")
    quantities = indexed(dossier["quantities"], "quantity")
    for q in quantities.values():
        if q["entity_id"] not in entities or entities[q["entity_id"]]["kind"] != "formation":
            raise ValueError("Quantity must reference a known formation")
        claim = claims.get(q["claim_id"])
        if claim is None or claim["status"] == "unknown" or claim["dimension"] != "strength":
            raise ValueError("Quantity requires a strength claim with evidence")
        index = q["citation_index"]
        if type(index) is not int or not 0 <= index < len(claim["citations"]):
            raise ValueError("Quantity requires a specific supporting citation")
        if q["unit"] != "people" or q["basis"] not in QUANTITY_BASES:
            raise ValueError("Invalid quantity unit or population basis")
        lo, hi = q["lower"], q["upper"]
        if any(type(n) not in {int, float} or not math.isfinite(n) or n < 0 for n in (lo, hi)) or lo > hi:
            raise ValueError("Invalid quantity bounds")
        kind = q["estimate_kind"]
        if kind not in {"reported_exact", "approximate", "range"} or (kind != "range" and lo != hi):
            raise ValueError("Quantity bounds contradict estimate kind")
        period = q["period"]
        start, end = period["start"], period["end"]
        if (start is None) != (end is None):
            raise ValueError("Unestablished quantity dates require both bounds null")
        if start is not None and date.fromisoformat(start) > date.fromisoformat(end):
            raise ValueError("Quantity period is reversed")
        if not all(q.get(key) for key in ("scope", "location", "note")) or not period.get("label"):
            raise ValueError("Quantity needs explicit time, location and population scope")
        if q["recorded_at"] is not None:
            date.fromisoformat(q["recorded_at"])
    previous = dossier.get("supersedes")
    if previous:
        path = safe_path(root, previous["path"])
        if digest(path) != previous["sha256"]:
            raise ValueError("Archived dossier checksum mismatch")
        if read_json(path)["battle_id"] != dossier["battle_id"]:
            raise ValueError("Archived dossier belongs to another battle")


def validate_all(root):
    sources = verify_sources(root)
    paths = sorted((root / "data/evidence").glob("*.json"))
    if not paths:
        raise ValueError("No evidence dossiers found")
    dossiers = [read_json(path) for path in paths]
    if len({d["battle_id"] for d in dossiers}) != len(dossiers):
        raise ValueError("Duplicate battle dossier")
    return [validate_dossier(root, d, sources) for d in dossiers]
