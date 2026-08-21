#!/usr/bin/env python3
"""Validate the PFAS tracker starter registers and cross-layer relationships."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = PROJECT_ROOT / "data"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URL_RE = re.compile(r"^https?://")


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_date(value: Any, label: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not DATE_RE.fullmatch(value):
        errors.append(f"{label}: expected YYYY-MM-DD, got {value!r}")
        return
    try:
        date.fromisoformat(value)
    except ValueError:
        errors.append(f"{label}: invalid calendar date {value!r}")


def collect_records(data: dict[str, Any], key: str, errors: list[str]) -> dict[str, dict[str, Any]]:
    records = data.get(key)
    if not isinstance(records, list):
        errors.append(f"{key}: expected a list")
        return {}

    output: dict[str, dict[str, Any]] = {}
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"{key}[{index}]: expected an object")
            continue
        record_id = record.get("id")
        if not isinstance(record_id, str) or not record_id:
            errors.append(f"{key}[{index}]: missing non-empty id")
            continue
        if record_id in output:
            errors.append(f"{key}: duplicate id {record_id}")
        output[record_id] = record
    return output


def validate_common_record(record: dict[str, Any], label: str, layer_ids: set[str], jurisdiction_ids: set[str], source_ids: set[str], errors: list[str]) -> None:
    required = ["id", "title", "record_type", "layer_id", "jurisdiction_id", "status", "review_state", "last_verified"]
    for field in required:
        if field not in record:
            errors.append(f"{label}: missing {field}")

    if record.get("layer_id") not in layer_ids:
        errors.append(f"{label}: unknown layer_id {record.get('layer_id')!r}")
    if record.get("jurisdiction_id") not in jurisdiction_ids:
        errors.append(f"{label}: unknown jurisdiction_id {record.get('jurisdiction_id')!r}")

    for field in ("publication_date", "effective_date", "compliance_date", "last_verified"):
        if field in record and record[field] is not None:
            validate_date(record[field], f"{label}.{field}", errors)

    record_sources = record.get("source_ids", [])
    if not isinstance(record_sources, list) or not record_sources:
        errors.append(f"{label}: source_ids must be a non-empty list")
    else:
        for source_id in record_sources:
            if source_id not in source_ids:
                errors.append(f"{label}: unknown source_id {source_id}")


def main() -> int:
    errors: list[str] = []

    try:
        layers_data = load_json(DATA_ROOT / "layers.json")
        jurisdictions_data = load_json(DATA_ROOT / "jurisdictions.json")
        sources_data = load_json(DATA_ROOT / "sources.json")
        events_data = load_json(DATA_ROOT / "events.json")
        relationships_data = load_json(DATA_ROOT / "relationships.json")
        obligations_data = load_json(DATA_ROOT / "obligations.json")
        schema_data = load_json(PROJECT_ROOT / "schema" / "record-schema.json")
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: unable to load project registers: {exc}")
        return 1

    layer_records = collect_records(layers_data, "layers", errors)
    jurisdiction_records = collect_records(jurisdictions_data, "jurisdictions", errors)
    source_records = collect_records(sources_data, "sources", errors)
    event_records = collect_records(events_data, "events", errors)
    relationship_records = collect_records(relationships_data, "relationships", errors)
    obligation_records = collect_records(obligations_data, "obligations", errors)

    layer_ids = set(layer_records)
    jurisdiction_ids = set(jurisdiction_records)
    source_ids = set(source_records)
    event_ids = set(event_records)
    obligation_ids = set(obligation_records)

    expected_layers = [
        "us-federal",
        "oebgd",
        "fgs",
        "sofa-agreement",
        "host-nation",
        "installation-obligation",
    ]
    actual_layers = [layer.get("id") for layer in sorted(layer_records.values(), key=lambda item: item.get("sequence", 999))]
    if layers_data.get("core_model") != expected_layers:
        errors.append(f"layers.core_model: expected {expected_layers}, got {layers_data.get('core_model')}")
    if actual_layers != expected_layers:
        errors.append(f"layers.sequence: expected {expected_layers}, got {actual_layers}")

    if schema_data.get("title") != "PFAS Environmental Law and Regulatory Tracker record contract":
        errors.append("schema: unexpected title")

    for source_id, source in source_records.items():
        url = source.get("source_url")
        if not isinstance(url, str) or not URL_RE.match(url):
            errors.append(f"sources[{source_id}]: source_url must be an http(s) URL")
        if source.get("officiality") == "unverified_public_copy" and source.get("source_status") != "discovery_only":
            errors.append(f"sources[{source_id}]: unverified public copies must be discovery_only")
        if "last_verified" in source:
            validate_date(source["last_verified"], f"sources[{source_id}].last_verified", errors)

    for event_id, event in event_records.items():
        validate_common_record(event, f"events[{event_id}]", layer_ids, jurisdiction_ids, source_ids, errors)
        if event.get("layer_id") == "fgs" and not event.get("fgs_version"):
            errors.append(f"events[{event_id}]: FGS records require fgs_version")
        if event.get("status") in {"effective", "effective_under_litigation"} and not event.get("effective_date"):
            errors.append(f"events[{event_id}]: effective records require effective_date")
        if event.get("review_state") == "discovery_only" and event.get("status") != "discovery_only":
            errors.append(f"events[{event_id}]: discovery_only review state requires discovery_only status")
        for parent_id in event.get("parent_ids", []):
            if parent_id not in event_ids:
                errors.append(f"events[{event_id}]: unknown parent_id {parent_id}")

    for obligation_id, obligation in obligation_records.items():
        validate_common_record(obligation, f"obligations[{obligation_id}]", layer_ids, jurisdiction_ids, source_ids, errors)
        if obligation.get("layer_id") != "installation-obligation":
            errors.append(f"obligations[{obligation_id}]: obligations must use installation-obligation layer")
        for trigger_id in obligation.get("trigger_event_ids", []):
            if trigger_id not in event_ids:
                errors.append(f"obligations[{obligation_id}]: unknown trigger_event_id {trigger_id}")

    all_endpoints = {
        "event": event_ids,
        "obligation": obligation_ids,
        "source": source_ids,
        "jurisdiction": jurisdiction_ids,
        "layer": layer_ids,
    }
    for relationship_id, relationship in relationship_records.items():
        for endpoint in ("from", "to"):
            endpoint_type = relationship.get(f"{endpoint}_type")
            endpoint_id = relationship.get(f"{endpoint}_id")
            if endpoint_type not in all_endpoints:
                errors.append(f"relationships[{relationship_id}]: unknown {endpoint}_type {endpoint_type!r}")
            elif endpoint_id not in all_endpoints[endpoint_type]:
                errors.append(f"relationships[{relationship_id}]: unknown {endpoint}_id {endpoint_id!r}")
        for source_id in relationship.get("source_ids", []):
            if source_id not in source_ids:
                errors.append(f"relationships[{relationship_id}]: unknown source_id {source_id}")

    required_seed_ids = {
        "OEBGD-V1-CHANGE1-2026",
        "FGS-ROK-KEGS-2024",
        "FGS-JPN-JEGS-2024",
        "FGS-DEU-GFGS-2019-PUBLIC",
        "JPN-PFAS-DRINKING-WATER-2026",
        "DEU-PFAS-DRINKING-WATER-2026",
        "EU-REACH-PFAS-FOAM-2025",
        "US-CERCLA-PFOA-PFOS-2024",
    }
    missing_seeds = sorted(required_seed_ids - event_ids)
    if missing_seeds:
        errors.append(f"events: missing required seed records {missing_seeds}")

    if errors:
        print("FAIL: PFAS tracker validation")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: PFAS tracker validation")
    print(f"  layers: {len(layer_records)}")
    print(f"  jurisdictions: {len(jurisdiction_records)}")
    print(f"  sources: {len(source_records)}")
    print(f"  events: {len(event_records)}")
    print(f"  relationships: {len(relationship_records)}")
    print(f"  obligations: {len(obligation_records)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

