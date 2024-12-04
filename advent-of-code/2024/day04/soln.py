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

DIRECTIONS = {
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
}

D2 = {
    ((-1, -1), (1, 1)),
    ((-1, 1), (1, -1)),
    ((1, -1), (-1, 1)),
    ((1, 1), (-1, -1)),

    ((-1, -1), (-1, 1)),
    ((-1, 1), (1, 1)),
    ((1, 1), (1, -1)),
    ((1, -1), (-1, -1)),
}


def a(lines):
    grid = {}
    result = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    for (x, y), c in grid.items():
        if c != "X":
            continue
        for dx, dy in DIRECTIONS:
            state = ""
            for i in range(4):
                state += grid.get((x + (dx * i), y + (dy * i)), ".")
            if state == "XMAS":
                result += 1
    print(result)


def b(lines):
    grid = {}
    result = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    for (x, y), c in grid.items():
        if c != "A":
            continue
        for (dx, dy), (dx2, dy2) in D2:
            state = ""
            state2 = ""
            for i in range(-1, 2):
                state += grid.get((x + (dx * i), y + (dy * i)), ".")
            for i in range(-1, 2):
                state2 += grid.get((x + (dx2 * i), y + (dy2 * i)), ".")
            if state == "MAS" and state2 == "MAS":
                result += 1
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
