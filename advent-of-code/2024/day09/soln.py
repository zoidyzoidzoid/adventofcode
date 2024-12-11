#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import sys
import math
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt
from time import time_ns


def a(lines):
    return
    queue = deque((int(i) for i in lines[0]))
    mode = "normal"
    id = 0
    offset = 0
    intervals = deque()
    candidates = deque()
    while queue:
        c = queue.popleft()
        # print(f"{mode}: {c}")
        if mode == "normal":
            intervals.append((offset, offset+c, id))
            id += 1
            mode = "free"
        else:
            for i in range(offset, offset+c):
                # print(i)
                candidates.append(i)
            mode = "normal"
        offset += c
    def p(intervals):
        queue = sorted(deque(intervals))
        for i in range(len(queue)):
            start, end, id = queue[i]
            if i+1 >= len(queue):
                next_v = 0
            else:
                next_v = queue[i+1][0]
            print(str(id) * (end - start), end="")
            print("." * (next_v - end), end="")
        print()
    while candidates:
        # p(intervals)
        # print(sorted(intervals))
        # print(sorted(candidates))
        last = max(intervals)
        start, end, id = last
        intervals.remove(last)
        if start == end:
            continue
        elif candidates[0] > end:
            intervals.append(last)
            candidates.popleft()
            continue
        intervals.append((start, end-1, id))
        new_spot = candidates.popleft()
        intervals.append((new_spot, new_spot + 1, id))
    result = 0
    queue = sorted(deque(intervals))
    for i in range(len(queue)):
        start, end, id = queue[i]
        for i in range(start, end):
            result += id * i
    print(result)



def b(lines):
    queue = deque((int(i) for i in lines[0]))
    mode = "normal"
    id = 0
    offset = 0
    intervals = deque()
    candidates = deque()
    while queue:
        c = queue.popleft()
        # print(f"{mode}: {c}")
        if mode == "normal":
            intervals.append((offset, offset+c, id))
            id += 1
            mode = "free"
        else:
            if c != 0:
                candidates.append((offset, offset+c))
            mode = "normal"
        offset += c
    def p(intervals):
        queue = sorted(deque(intervals))
        for i in range(len(queue)):
            start, end, id = queue[i]
            if i+1 >= len(queue):
                next_v = 0
            else:
                next_v = queue[i+1][0]
            print(str(id) * (end - start), end="")
            print("." * (next_v - end), end="")
        print()
    while True:
        updated = False
        # p(intervals)
        for item in (sorted(intervals, reverse=True)):
            for item2 in (sorted(candidates)):
                if item2[0] >= item[0]:
                    continue
                needed = item[1] - item[0]
                avail = item2[1] - item2[0]
                if avail >= needed:
                    intervals.remove(item)
                    candidates.remove(item2)
                    intervals.append((item2[0], item2[0] + needed, item[2]))
                    if item2[1] != item2[0] + needed:
                        candidates.append((item2[0] + needed, item2[1]))
                    updated = True
                    break
            if updated:
                break
        if not updated:
            break
    result = 0
    queue = sorted(deque(intervals))
    for i in range(len(queue)):
        start, end, id = queue[i]
        for i in range(start, end):
            result += id * i
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


class Timer(object):
    def __init__(self, description):
        self.description = description
    def __enter__(self):
        self.start = time_ns()
    def __exit__(self, type, value, traceback):
        self.end = time_ns()
        d = self.end - self.start
        if d > 1_000_000_000:
            d /= 1_000_000_000
            u = "s"
        elif d > 1_000_000:
            d /= 1_000_000
            u = "ms"
        elif d > 1_000:
            d /= 1_000
            u = "µs"
        else:
            u = "ns"
        print("{}: {} {}".format(self.description, d, u))


def main():
    with Timer("Part 1"):
        a(lines)

    with Timer("Part 2"):
        b(lines)


if __name__ == "__main__":
    main()
