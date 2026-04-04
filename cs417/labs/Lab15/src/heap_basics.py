"""
Lab 15: Heap Basics — Getting comfortable with heapq

Tasks 1 and 2: Explore the heapq API and work with tuple priorities.
"""

import heapq


# ── Task 1: Heap Basics ─────────────────────────────────────────────


def push_and_pop(values):
    h = []
    for v in values:
        heapq.heappush(h, v)

    result = []
    while h:
        result.append(heapq.heappop(h))

    return result


def heapify_and_peek(values):
    h = list(values)
    heapq.heapify(h)
    return h[0]


def top_k_smallest(values, k):
    h = list(values)
    heapq.heapify(h)

    result = []
    for _ in range(k):
        result.append(heapq.heappop(h))

    return result


# ── Task 2: Tuple Priorities ────────────────────────────────────────


def sort_by_priority(tasks):
    h = []
    count = 0

    for priority, desc in tasks:
        heapq.heappush(h, (priority, count, desc))
        count += 1

    result = []
    while h:
        result.append(heapq.heappop(h)[2])

    return result