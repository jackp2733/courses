"""Expense Report — starter code.

This is one big main() that works. You will refactor it across three
change requests in the lab README. Don't change behavior on the original
inputs — you should be able to run this script and get the same report
you got at the end of Part 0.

DO NOT add any external libraries. Standard library only.
"""


def main():
    rows = []
    with open("data/transactions.csv") as f:
        for line in f.readlines()[1:]:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            rows.append(parts)

    categories = {
        "STARBUCKS": "food",
        "DUNKIN": "food",
        "WHOLEFOODS": "food",
        "WHOLE FOODS": "food",
        "SHELL": "gas",
        "EXXON": "gas",
        "AMAZON": "shopping",
        "TARGET": "shopping",
        "NETFLIX": "entertainment",
        "SPOTIFY": "entertainment",
        "HARDWARE": "home",
    }

    totals = {}
    for date, vendor, amount, _ in rows:
        cat = "other"
        for key, c in categories.items():
            if key in vendor.upper():
                cat = c
        totals[cat] = totals.get(cat, 0.0) + float(amount)

    print("=== Expense Report ===")
    for cat, total in sorted(totals.items()):
        print(f"  {cat:<15} ${total:>8.2f}")
    print(f"  {'TOTAL':<15} ${sum(totals.values()):>8.2f}")


if __name__ == "__main__":
    main()
