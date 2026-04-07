"""
Lab 18: Working with CSV and JSON Files

Read, write, and convert between CSV and JSON formats.
"""

import csv
import json
from pathlib import Path


def read_csv(filepath: str) -> list[dict]:
    with open(filepath, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def read_json(filepath: str):
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)

def write_csv(filepath: str, data: list[dict], fieldnames: list[str]) -> None:
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def write_json(filepath: str, data) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def csv_to_json(
    csv_path: str,
    json_path: str,
    type_hints: dict[str, type] | None = None,
) -> None:
    data = read_csv(csv_path)

    if type_hints:
        for row in data:
            for key, typ in type_hints.items():
                if key in row:
                    row[key] = typ(row[key])

    write_json(json_path, data)


def json_to_csv(
    json_path: str,
    csv_path: str,
    fieldnames: list[str],
) -> None:
    data = read_json(json_path)

    filtered = []
    for item in data:
        row = {}
        for field in fieldnames:
            row[field] = item.get(field)
        filtered.append(row)

    write_csv(csv_path, filtered, fieldnames)