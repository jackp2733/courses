"""Tests you must make pass.

After Part 0, ONLY `test_starter_runs` should pass.

By the end of Part 3, ALL tests in this file must pass — without your code
opening any file, calling print(), or hitting the network.

The tests below intentionally do not import a specific module from your
project — that is the *point*. Your refactor decides what's importable.

You will need to update the imports below to point at whatever you
named your modules. The function signatures the tests expect are the
contract you have to satisfy. Do not change the test assertions.
"""

import io
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent


# -----------------------------------------------------------------------------
# Part 0 — sanity check that starter runs
# -----------------------------------------------------------------------------

def test_starter_runs():
    """The unrefactored script runs and produces a report on stdout."""
    result = subprocess.run(
        [sys.executable, "src/expense_report.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"starter crashed:\n{result.stderr}"
    assert "Expense Report" in result.stdout
    assert "TOTAL" in result.stdout


# -----------------------------------------------------------------------------
# Parts 1-3 — make these pass with your refactor.
#
# After you refactor, expose these as importable functions/classes.
# Then UPDATE THE IMPORTS BELOW to point at your module(s).
#
# Suggested shape (you decide the names):
#
#     from src.pipeline import build_report
#     from src.parsers import CSVParser, JSONParser
#     from src.categorizer import Categorizer
#
# build_report(parser, categorizer, source) -> dict[str, float]
#
# A `parser` is anything with a .parse(source) method that returns
# an iterable of (date, vendor, amount, note) tuples.
# A `categorizer` is anything with a .categorize(vendor) method that
# returns a category string.
# `source` is whatever the parser knows how to read — bytes, a string,
# a list, a path. Your call.
#
# The reference solution lives in the instructor repo; ask if stuck.
# -----------------------------------------------------------------------------


# Uncomment and adjust once your refactor is in place.
#
# from src.pipeline import build_report
# from src.parsers import CSVParser, JSONParser
# from src.categorizer import Categorizer
#
#
# def _categories():
#     return json.loads((ROOT / "data" / "categories.json").read_text())
#
#
# def test_csv_parsing_no_io():
#     """build_report runs entirely in-memory — no files, no prints."""
#     csv_text = (
#         "date,vendor,amount,note\n"
#         "2026-04-01,Starbucks,4.85,coffee\n"
#         "2026-04-01,Shell,52.30,gas\n"
#     )
#     totals = build_report(CSVParser(), Categorizer(_categories()), csv_text)
#     assert totals["food"] == 4.85
#     assert totals["gas"] == 52.30
#
#
# def test_json_parsing_no_io():
#     """Same shape, JSON input, no files, no prints."""
#     payload = json.dumps([
#         {"date": "2026-04-01", "vendor": "Starbucks", "amount": 4.85, "note": ""},
#         {"date": "2026-04-01", "vendor": "Shell",     "amount": 52.30, "note": ""},
#     ])
#     totals = build_report(JSONParser(), Categorizer(_categories()), payload)
#     assert totals["food"] == 4.85
#     assert totals["gas"] == 52.30
#
#
# def test_swap_categorizer():
#     """Different config -> different categorization, same parser."""
#     csv_text = (
#         "date,vendor,amount,note\n"
#         "2026-04-01,Starbucks,4.85,coffee\n"
#     )
#     strict_cats = {"coffee_shops": ["STARBUCKS"]}
#     totals = build_report(CSVParser(), Categorizer(strict_cats), csv_text)
#     assert totals["coffee_shops"] == 4.85
#     assert "food" not in totals
#
#
# def test_pipeline_does_no_io(monkeypatch, capsys):
#     """No file opens, no prints, no network during build_report."""
#     def boom(*a, **k):
#         raise AssertionError("build_report must not open files")
#
#     monkeypatch.setattr("builtins.open", boom)
#
#     csv_text = "date,vendor,amount,note\n2026-04-01,Starbucks,4.85,c\n"
#     totals = build_report(CSVParser(), Categorizer(_categories()), csv_text)
#     captured = capsys.readouterr()
#
#     assert captured.out == "", "build_report must not print"
#     assert totals["food"] == 4.85
