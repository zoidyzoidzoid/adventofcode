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


def print_grid(grid):
    print("Grid:")
    for y in range(0, max(i[1] for i in grid) + 1):
        for x in range(0, max(i[0] for i in grid) + 1):
            print(grid.get((x, y), "."), end="")
        print()
    print()


def a(lines):
    grid = {}
    for i, line in enumerate("\n".join(lines).split("\n\n")[0].split("\n")):
        x, _, y = line.partition(",")
        x, y = int(x), int(y)
        grid[x, y] = "#"
    # print_grid(grid)
    for i, line in enumerate("\n".join(lines).split("\n\n")[1].split("\n")):
        c, _, n = line[len("fold along "):].partition("=")
        n = int(n)
        if c == "x":
            for (x, y), c in list(grid.items()):
                if x >= n:
                    # print("{}: from {} to {}".format(n, x, n - (x - n)))
                    grid[n - (x - n), y] = "#"
                    grid.pop((x, y))
        elif c == "y":
            for (x, y), c in list(grid.items()):
                if y >= n:
                    # print("{}: from {} to {}".format(n, y, n - (y - n)))
                    grid[x, n - (y - n)] = "#"
                    grid.pop((x, y))
        # print_grid(grid)

        print(len(grid))
        break


def b(lines):
    grid = {}
    for i, line in enumerate("\n".join(lines).split("\n\n")[0].split("\n")):
        x, _, y = line.partition(",")
        x, y = int(x), int(y)
        grid[x, y] = "#"
    # print_grid(grid)
    for i, line in enumerate("\n".join(lines).split("\n\n")[1].split("\n")):
        c, _, n = line[len("fold along "):].partition("=")
        n = int(n)
        if c == "x":
            for (x, y), c in list(grid.items()):
                if x >= n:
                    # print("{}: from {} to {}".format(n, x, n - (x - n)))
                    grid[n - (x - n), y] = "#"
                    grid.pop((x, y))
        elif c == "y":
            for (x, y), c in list(grid.items()):
                if y >= n:
                    # print("{}: from {} to {}".format(n, y, n - (y - n)))
                    grid[x, n - (y - n)] = "#"
                    grid.pop((x, y))
        # print_grid(grid)

    print_grid(grid)


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
