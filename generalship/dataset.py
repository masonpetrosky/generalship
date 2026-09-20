"""Build a fixed campaign-complete frame before excluding unscorable battles."""

from collections import Counter, defaultdict
from datetime import date
import math

from .sources import read_csv, read_json, verify_sources


def unique(rows, keys, name):
    result = {}
    for row in rows:
        key = tuple(row[k] for k in keys)
        if any(not part for part in key) or key in result:
            raise ValueError(f"Missing or duplicate {name} key: {key}")
        result[key] = row
    return result


def number(value):
    if value == "":
        return None
    result = float(value)
    if not math.isfinite(result) or result < 0:
        raise ValueError(f"Invalid nonnegative number: {value}")
    return result


def build_dataset(root):
    registry = verify_sources(root)
    raw = root / "data/raw"
    battles = read_csv(raw / "cwsac_battles.csv")
    forces = read_csv(raw / "cwsac_forces.csv")
    commanders = read_csv(raw / "cwsac_commanders.csv")
    campaigns = read_csv(raw / "cwsac_campaigns.csv")
    battle_map = unique(battles, ["battle"], "battle")
    campaign_map = unique(campaigns, ["campaign"], "campaign")
    unique(forces, ["battle", "belligerent"], "force")
    unique(commanders, ["battle", "belligerent", "fullname"], "commander listing")
    force_map, command_map = defaultdict(dict), defaultdict(list)
    for row in forces:
        if (row["battle"],) not in battle_map:
            raise ValueError(f"Orphan force: {row['battle']}")
        low, high = number(row["strength_min"]), number(row["strength_max"])
        if (low is None) != (high is None) or (low is not None and low > high):
            raise ValueError(f"Malformed strength interval: {row['battle']}")
        force_map[row["battle"]][row["belligerent"]] = {
            "low": low, "high": high, "unit": "people",
            "basis": "source_reported_forces_engaged",
            "description": row["description"],
            "source_id": "arnold-cwsac-forces",
            "row_key": {"battle": row["battle"], "belligerent": row["belligerent"]},
        }
    for row in commanders:
        if row["belligerent"] not in force_map[row["battle"]]:
            raise ValueError(f"Orphan commander listing: {row['battle']}")
        command_map[row["battle"]].append({"name": row["fullname"], "side": row["belligerent"]})
    for row in battles:
        if (row["campaign"],) not in campaign_map:
            raise ValueError(f"Orphan campaign: {row['battle']}")
        if date.fromisoformat(row["start_date"]) > date.fromisoformat(row["end_date"]):
            raise ValueError(f"Reversed dates: {row['battle']}")
        if row["result"] not in {"Union", "Confederate", "Inconclusive"}:
            raise ValueError(f"Unknown outcome: {row['battle']}")
        if row["operation"] not in {"0", "1"}:
            raise ValueError(f"Unknown grain: {row['battle']}")
    config = read_json(root / "data/pilot/cohort.json")
    selected_campaigns = {
        row["campaign"] for row in battles
        if int(row["start_date"][:4]) in config["anchor_years"]
        and campaign_map[(row["campaign"],)]["theater"] in config["theaters"]
    }
    selected = [row for row in battles if row["campaign"] in selected_campaigns]
    actual_ids = sorted(row["battle"] for row in selected)
    if actual_ids != config["battle_ids"]:
        raise ValueError("Cohort differs from frozen battle IDs; review cohort changes explicitly")
    records = []
    for row in sorted(selected, key=lambda x: (x["start_date"], x["battle"])):
        strengths = force_map[row["battle"]]
        reasons = []
        if set(strengths) != {"US", "Confederate"}:
            reasons.append("unsupported_belligerents")
        if row["operation"] == "1":
            reasons.append("aggregate_operation")
        if row["result"] == "Inconclusive":
            reasons.append("inconclusive_outcome")
        if any(s["low"] is None for s in strengths.values()) or len(strengths) != 2:
            reasons.append("missing_numeric_strength")
        if any(s["low"] == 0 for s in strengths.values()):
            reasons.append("zero_strength_requires_review")
        records.append({
            "battle_id": row["battle"], "name": row["battle_name"],
            "campaign": row["campaign"], "theater": campaign_map[(row["campaign"],)]["theater"],
            "start_date": row["start_date"], "end_date": row["end_date"],
            "source_result": row["result"], "result_text": row["results_text"],
            "strengths": strengths, "listed_commanders": command_map[row["battle"]],
            "source_id": "arnold-cwsac-battles", "row_key": {"battle": row["battle"]},
            "source_url": row["url"], "review_status": "imported_unreviewed",
            "baseline_eligible": not reasons, "exclusion_reasons": reasons,
        })
    counts = Counter(reason for r in records for reason in r["exclusion_reasons"])
    profile = {
        "source_battles": len(battles), "source_forces": len(forces),
        "source_commander_listings": len(commanders), "pilot_battles": len(records),
        "pilot_campaigns": len(selected_campaigns),
        "baseline_eligible": sum(r["baseline_eligible"] for r in records),
        "exclusion_counts_nonexclusive": dict(sorted(counts.items())),
        "outcome_counts": dict(sorted(Counter(r["source_result"] for r in records).items())),
        "coverage_by_theater": {
            t: {"total": sum(r["theater"] == t for r in records),
                "eligible": sum(r["theater"] == t and r["baseline_eligible"] for r in records)}
            for t in sorted(config["theaters"])
        },
        "source_hashes": {key: s["sha256"] for key, s in sorted(registry.items())},
        "warnings": ["Imported records have not been adjudicated by a historian.",
                     "Missing strength is unknown, never zero or an average force.",
                     "The source is a principal-battle frame, not all command opportunities.",
                     "Listed commanders are not verified decision responsibility."],
    }
    return records, profile
