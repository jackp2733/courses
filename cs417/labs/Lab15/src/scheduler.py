"""
Lab 15: Task Scheduler — A priority queue in action

Task 3: Build a TaskScheduler class using heapq.
"""

import heapq


class TaskScheduler:
    """A priority-based task scheduler.

    Tasks are added with a priority (lower number = more urgent).
    Tasks with the same priority are processed in FIFO order.
    """

    def __init__(self):
        self.heap = []
        self.count = 0

    def add_task(self, priority, description):
        heapq.heappush(self.heap, (priority, self.count, description))
        self.count += 1

    def next_task(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)[2]

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0][2]

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0