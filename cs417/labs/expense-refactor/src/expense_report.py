"""Expense Report — starter code.

This script works. It reads transactions.csv, categorizes the rows,
and prints a report showing per-category totals.

It also has all of its logic crammed into one big main() function with
hard-coded filenames, a hard-coded category dict, and print() statements
woven into the calculations.

Your job is to refactor this code IN PLACE, by moving the right logic
into the four helper shapes below, in response to the change requests in
the README. Keep everything in this one file.

When you're done, the script should produce the SAME output (TOTAL = $613.87)
on the original inputs — the change requests should not change observable
behavior on the starting CSV.

DO NOT add any external libraries. Standard library only.
"""

import json
from pathlib import Path


# -----------------------------------------------------------------------------
# Part 1 — Parsing
# -----------------------------------------------------------------------------

def _make_row(date, vendor, amount, note):
    """Shared helper to avoid duplication between CSV + JSON."""
    try:
        return {
            "date": date,
            "vendor": vendor,
            "amount": float(amount),  # ✅ FIX: always convert to float
            "note": note,
        }
    except Exception:
        return None


def parse_csv(text: str) -> list[dict]:
    rows = []
    lines = text.strip().splitlines()

    for line in lines[1:]:  # skip header
        parts = line.split(",")
        if len(parts) != 4:
            continue

        row = _make_row(*parts)
        if row:
            rows.append(row)

    return rows


def parse_json(text: str) -> list[dict]:
    rows = []
    try:
        data = json.loads(text)
    except Exception:
        return rows

    for item in data:
        try:
            row = _make_row(
                item["date"],
                item["vendor"],
                item["amount"],  # will be cast to float in helper
                item.get("note", ""),
            )
            if row:
                rows.append(row)
        except Exception:
            continue

    return rows


# -----------------------------------------------------------------------------
# Part 2 — Categorizer
# -----------------------------------------------------------------------------

def categorize(vendor: str, categories: dict) -> str:
    vendor_upper = vendor.upper()

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in vendor_upper:
                return category

    return "other"


# -----------------------------------------------------------------------------
# Part 3 — Pure pipeline
# -----------------------------------------------------------------------------

def build_report(rows: list[dict], categories: dict) -> dict:
    totals = {}

    for row in rows:
        cat = categorize(row["vendor"], categories)
        totals[cat] = totals.get(cat, 0.0) + row["amount"]  # ✅ now always float

    return totals


# -----------------------------------------------------------------------------
# main() — I/O shell
# -----------------------------------------------------------------------------

def main():
    # read CSV
    text = Path("data/transactions.csv").read_text()
    rows = parse_csv(text)

    # read categories config
    categories = json.loads(Path("data/categories.json").read_text())

    # build report
    totals = build_report(rows, categories)

    # print
    print("=== Expense Report ===")
    for cat, total in sorted(totals.items()):
        print(f"  {cat:<15} ${total:>8.2f}")
    print(f"  {'TOTAL':<15} ${sum(totals.values()):>8.2f}")


if __name__ == "__main__":
    main()