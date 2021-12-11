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
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    }
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x, y] = int(c)

    def print_grid(grid, steps):
        return
        if steps == 0:
            print("Before any steps:")
        else:
            print("After step {}:".format(steps))
        for y in range(0, max(i[1] for i in grid) + 1):
            for x in range(0, max(i[0] for i in grid) + 1):
                print("{:1d}".format(grid[x, y]), end="")
            print()
        print()

    result = 0
    steps = 0
    print_grid(grid, steps)
    while True:
        old = grid
        grid = grid.copy()
        seen = set()
        for (x, y), c in old.items():
            grid[x, y] = c + 1
        for (x, y), c in grid.items():
            if c > 9:
                queue = [(x, y)]
                while queue:
                    x, y = queue.pop()
                    if (x, y) in seen:
                        continue
                    seen.add((x, y))
                    result += 1
                    grid[x, y] = 0
                    for dx, dy in dirs:
                        if (x + dx, y + dy) in old and grid[x + dx, y + dy] != 0:
                            grid[x + dx, y + dy] += 1
                            if grid[x + dx, y + dy] > 9:
                                queue.append((x + dx, y + dy))
        steps += 1
        if steps % 10 == 0:
            print_grid(grid, steps)
        if steps >= 100:
            break
    print(result)


def b(lines):
    dirs = {
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    }
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x, y] = int(c)

    def print_grid(grid, steps):
        return
        if steps == 0:
            print("Before any steps:")
        else:
            print("After step {}:".format(steps))
        for y in range(0, max(i[1] for i in grid) + 1):
            for x in range(0, max(i[0] for i in grid) + 1):
                print("{:1d}".format(grid[x, y]), end="")
            print()
        print()

    steps = 0
    print_grid(grid, steps)
    while True:
        result = 0
        old = grid
        grid = grid.copy()
        seen = set()
        for (x, y), c in old.items():
            grid[x, y] = c + 1
        for (x, y), c in grid.items():
            if c > 9:
                queue = [(x, y)]
                while queue:
                    x, y = queue.pop()
                    if (x, y) in seen:
                        continue
                    seen.add((x, y))
                    result += 1
                    grid[x, y] = 0
                    for dx, dy in dirs:
                        if (x + dx, y + dy) in old and grid[x + dx, y + dy] != 0:
                            grid[x + dx, y + dy] += 1
                            if grid[x + dx, y + dy] > 9:
                                queue.append((x + dx, y + dy))
        steps += 1
        if steps % 10 == 0:
            print_grid(grid, steps)
        if result == len(grid):
            break
    print(steps)


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
