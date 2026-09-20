"""Pinned, byte-verified inputs. Network access is an explicit CLI operation."""

import csv
from datetime import date
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")


def safe_path(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes project: {relative}")
    return path


def source_registry(root: Path) -> dict:
    manifest = read_json(root / "data/sources.json")
    sources = manifest["sources"]
    if len({s["id"] for s in sources}) != len(sources):
        raise ValueError("Duplicate source IDs")
    return {s["id"]: s for s in sources}


def source_metadata_digest(source: dict) -> str:
    """Bind a metadata revision to the complete previous registry entry."""
    blob = json.dumps(source, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def text_sections(text: str) -> dict[str, str]:
    sections = [part.partition("\n") for part in text.split("\n## ")[1:]]
    names = [name for name, _, _ in sections]
    if not names or any(not name.strip() for name in names) or len(names) != len(set(names)):
        raise ValueError("Sectioned source needs unique nonempty section IDs")
    return {name: body for name, _, body in sections}


def _section_date_map(source: dict) -> dict | None:
    # Standalone document_date_note is also used by legacy single-date sources.
    if not {"document_dates_by_section", "editorial_sections"}.intersection(source):
        return None
    dates = source.get("document_dates_by_section")
    if not isinstance(dates, dict):
        raise ValueError("Section-date metadata requires a document_dates_by_section map")
    return dates


def source_document_date(source: dict, section: str | None = None) -> str | None:
    """Return the date of the cited document, never its event or knowledge date.

    A mapped null is authoritative: do not fall back to a nearby report date.
    Editorial sections have no historical document date.
    """
    dates = _section_date_map(source)
    if dates is not None:
        if section in source.get("editorial_sections", []):
            return None
        if section not in dates:
            raise ValueError("A section-specific document date requires a mapped section")
        return dates[section]
    return source.get("document_date")


def validate_source_metadata(root: Path, registry: dict) -> None:
    for source in registry.values():
        dates = _section_date_map(source)
        if dates is not None:
            if source["format"] != "text" or source.get("sectioned") is not True:
                raise ValueError("Section dates require a sectioned text source")
            if "document_date" not in source or source["document_date"] is not None:
                raise ValueError("Section dates require a null source-wide document date")
            note = source.get("document_date_note")
            if not isinstance(note, str) or not note.strip():
                raise ValueError("Section dates require an explanatory date note")
            sections = text_sections(safe_path(root, source["path"]).read_text(encoding="utf-8"))
            editorial = source.get("editorial_sections", [])
            if (not isinstance(editorial, list) or any(not isinstance(x, str) for x in editorial)
                    or len(editorial) != len(set(editorial)) or not set(editorial) <= sections.keys()):
                raise ValueError("Invalid editorial section IDs")
            if set(dates) != sections.keys() - set(editorial):
                raise ValueError("Document dates must cover every historical section exactly")
            for value in dates.values():
                if value is not None and (not isinstance(value, str) or date.fromisoformat(value).isoformat() != value):
                    raise ValueError("Section date must be an ISO calendar date or null")
        revision_fields = {"supersedes", "revision_kind", "revision_note"}
        if revision_fields.intersection(source):
            if not revision_fields <= source.keys():
                raise ValueError("Source metadata revision requires supersedes, revision_kind and revision_note together")
            previous = source["supersedes"]
            old = registry.get(previous.get("source_id")) if isinstance(previous, dict) else None
            if old is None or old["id"] == source["id"]:
                raise ValueError("Source revision requires a different registered predecessor")
            if previous.get("metadata_sha256") != source_metadata_digest(old):
                raise ValueError("Superseded source metadata checksum mismatch")
            note = source.get("revision_note")
            if source["revision_kind"] != "metadata_only" or not isinstance(note, str) or not note.strip():
                raise ValueError("Source revision requires a documented metadata-only migration")
            if any(source.get(key) != old.get(key) for key in ("path", "sha256", "parent_sha256", "format")):
                raise ValueError("Metadata-only source revision cannot replace raw evidence")
        if "facsimile_source_id" in source:
            facsimile = registry.get(source["facsimile_source_id"])
            if facsimile is None or facsimile["format"] != "png":
                raise ValueError("Facsimile link requires a registered image")
            if (source.get("parent_sha256") != facsimile.get("parent_sha256")
                    or source["independence_group"] != facsimile["independence_group"]):
                raise ValueError("A transcript and its facsimile must share parent and dependence group")


def verify_sources(root: Path) -> dict:
    registry = source_registry(root)
    for source in registry.values():
        path = safe_path(root, source["path"])
        if not path.is_file() or digest(path) != source["sha256"]:
            raise ValueError(f"Source missing or checksum mismatch: {source['id']}")
    validate_source_metadata(root, registry)
    return registry


def fetch_sources(root: Path) -> int:
    """Restore pinned raw tables only; do not silently refresh evidence snapshots."""
    count = 0
    for source in source_registry(root).values():
        if source.get("download_url") is None:
            continue
        path = safe_path(root, source["path"])
        if path.is_file() and digest(path) == source["sha256"]:
            continue
        request = Request(source["download_url"], headers={"User-Agent": "generalship-research/0.1"})
        with urlopen(request, timeout=30) as response:
            blob = response.read()
        if hashlib.sha256(blob).hexdigest() != source["sha256"]:
            raise ValueError(f"Downloaded source changed: {source['id']}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(blob)
        count += 1
    return count


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames is None or len(set(reader.fieldnames)) != len(reader.fieldnames):
            raise ValueError(f"Invalid CSV header: {path.name}")
        rows = list(reader)
    if any(None in row or None in row.values() for row in rows):
        raise ValueError(f"Malformed CSV row: {path.name}")
    return rows
