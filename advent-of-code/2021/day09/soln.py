#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import sys
import math
from collections import Counter, OrderedDict, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from heapq import nlargest
from itertools import combinations, permutations
from math import floor, sqrt
from time import time_ns


def a(lines):
    grid = OrderedDict()
    mx, my = 0, 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x, y] = int(c)
            mx = max((mx, x))
            my = max((my, y))
    dirs = [
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1),
    ]
    result = 0
    for (x, y), c in grid.items():
        for dx, dy in dirs:
            if not mx >= x + dx >= 0:
                continue
            if not my >= y + dy >= 0:
                continue
            if grid[x + dx, y + dy] <= c:
                break
        else:
            result += c + 1
    print(result)


def b(lines):
    grid = OrderedDict()
    mx, my = 0, 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x, y] = int(c)
            mx = max((mx, x))
            my = max((my, y))
    dirs = [
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1),
    ]
    # print(grid)
    result = []
    for (x, y), c in grid.items():
        for dx, dy in dirs:
            if not mx >= x + dx >= 0:
                continue
            if not my >= y + dy >= 0:
                continue
            if grid[x + dx, y + dy] <= c:
                break
        else:
            # print("Found low point:", c)
            # for dy in range(-1, 2):
            #     for dx in range(-1, 2):
            #         print(grid.get((x + dx, y + dy), " "), end="")
            #     print()
            # print()
            seen = set()
            basin_size = 0
            queue = [(x, y)]
            while queue:
                item = queue.pop()
                if item in seen:
                    continue
                # print(item)
                seen.add(item)
                basin_size += 1
                # print(seen)
                x, y = item
                for dx, dy in dirs:
                    if not mx >= x + dx >= 0:
                        # print("Skipping: {},{}".format(x + dx, y + dy))
                        continue
                    if not my >= y + dy >= 0:
                        # print("Skipping: {},{}".format(x + dx, y + dy))
                        continue
                    if grid[x + dx, y + dy] == 9:
                        # print("Skipping: {},{} because 9".format(x + dx, y + dy))
                        continue
                    if grid[x + dx, y + dy] >= c:
                        # print("Found point to explore: {},{}".format(x + dx, y + dy))
                        queue.append((x + dx, y + dy))
            # print("basin starting at:", c, "size:", basin_size, "seen:", seen)
            result.append(basin_size)
            result = nlargest(3, result)
    print("{} * {} * {}".format(result[0], result[1], result[2]))
    print(result[0] * result[1] * result[2])


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


with Timer("Part 1"):
    a(lines)


with Timer("Part 2"):
    b(lines)
