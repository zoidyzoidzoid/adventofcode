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
from time import time, time_ns


def a(lines):
    positions = []
    for i, line in enumerate(lines):
        for c in line.split(","):
            positions.append(int(c))

    # 2n - 1
    pos = 0
    fuel = None
    for goal in range(min(positions), max(positions)):
        cr = 0
        for p in positions:
            cr += abs(goal - p)
        if fuel is None or cr < fuel:
            pos = goal
            fuel = cr
    print(pos, fuel)


def old_b(lines):
    positions = []
    for i, line in enumerate(lines):
        for c in line.split(","):
            positions.append(int(c))

    # 2n - 1
    pos = 0
    fuel = None
    for goal in range(min(positions), max(positions)):
        cr = 0
        for p in positions:
            steps = abs(goal - p)
            cr += sum(range(1, steps+1))
        if fuel is None or cr < fuel:
            pos = goal
            fuel = cr
    print(pos, fuel)


def b(lines):
    positions = []
    for i, line in enumerate(lines):
        for c in line.split(","):
            positions.append(int(c))

    # 2n - 1
    pos = 0
    fuel = None
    for goal in range(min(positions), max(positions)):
        cr = 0
        for p in positions:
            steps = abs(goal - p)
            cr += (steps * (steps + 1)) / 2
        if fuel is None or cr < fuel:
            pos = goal
            fuel = cr
    print(pos, fuel)


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

with Timer("Part 2 (Old)"):
    old_b(lines)

with Timer("Part 2"):
    b(lines)
