#!/usr/bin/env python3
"""Validate the public REFRAME benchmark release."""

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "reframe.jsonl"
EXPECTED_FIELDS = {
    "prompt_id", "category", "prompt", "phi_star", "r_star", "knowledge_probe"
}
EXPECTED_COUNTS = {
    "Precondition Violation": 50,
    "Physical Structure": 50,
    "Cost-Benefit Analysis": 50,
}


def main() -> None:
    with DATA.open(encoding="utf-8") as f:
        items = [json.loads(line) for line in f if line.strip()]

    assert len(items) == 150, f"Expected 150 items, found {len(items)}"

    for i, item in enumerate(items, start=1):
        missing = EXPECTED_FIELDS - item.keys()
        assert not missing, f"Row {i} missing fields: {sorted(missing)}"
        for field in EXPECTED_FIELDS:
            assert item[field] not in (None, ""), f"Row {i} has empty {field}"

    ids = [item["prompt_id"] for item in items]
    assert len(ids) == len(set(ids)), "prompt_id values must be unique"

    counts = Counter(item["category"] for item in items)
    assert counts == Counter(EXPECTED_COUNTS), f"Unexpected category counts: {dict(counts)}"

    for field in ("prompt", "knowledge_probe"):
        values = [item[field].strip() for item in items]
        duplicates = [value for value, count in Counter(values).items() if count > 1]
        assert not duplicates, f"Duplicate {field} values found: {len(duplicates)}"

    print("REFRAME validation passed.")
    print(f"Items: {len(items)}")
    for category, count in sorted(counts.items()):
        print(f"  {category}: {count}")


if __name__ == "__main__":
    main()
