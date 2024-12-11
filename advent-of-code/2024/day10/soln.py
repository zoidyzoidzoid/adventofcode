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
    dirs = {
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
    }
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
        # print(line)
    result = 0

    def calculate_score(x, y, seen=None):
        seen = seen or set()
        seen.add((x, y))
        if grid[(x, y)] == 9:
            # print(f"x={x}, y={y}, c={grid[x, y]}")
            return 1
        result = 0
        for dx, dy in dirs:
            if (x + dx, y + dy) in grid and grid[(x + dx, y + dy)] - 1 == grid[x, y]:
                if (x + dx, y + dy) in seen:
                    continue
                result += calculate_score(x + dx, y + dy, seen=seen)
        return result

    for (x, y), c in grid.items():
        if c == 0:
            diff = calculate_score(x, y)
            # print(f"x={x},y={y}: {diff}")
            result += diff
    print(result)


def b(lines):
    dirs = {
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
    }
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
        # print(line)
    result = 0

    def calculate_score(x, y):
        if grid[(x, y)] == 9:
            # print(f"x={x}, y={y}, c={grid[x, y]}")
            nonlocal result
            result += 1
        for dx, dy in dirs:
            if (x + dx, y + dy) in grid and grid[(x + dx, y + dy)] - 1 == grid[x, y]:
                calculate_score(x + dx, y + dy)

    for (x, y), c in grid.items():
        if c == 0:
            old = result
            calculate_score(x, y)
            print(f"x={x},y={y}: {result - old}")
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
