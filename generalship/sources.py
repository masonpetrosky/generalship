"""Pinned, byte-verified inputs. Network access is an explicit CLI operation."""

import csv
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


def verify_sources(root: Path) -> dict:
    registry = source_registry(root)
    for source in registry.values():
        path = safe_path(root, source["path"])
        if not path.is_file() or digest(path) != source["sha256"]:
            raise ValueError(f"Source missing or checksum mismatch: {source['id']}")
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
