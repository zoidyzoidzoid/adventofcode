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


def print_grid(grid):
    for y in range(0, max(i[1] for i in grid) + 1):
        for x in range(0, max(i[0] for i in grid) + 1):
            print(grid.get((x, y), "."), end="")
        print()


def a(lines):
    result = 0
    grid = defaultdict(int)
    for i, line in enumerate(lines):
        one, _, two = line.partition(" -> ")
        x1, y1 = (int(i) for i in one.split(","))
        x2, y2 = (int(i) for i in two.split(","))
        print("{},{} -> {},{}".format(x1, y1, x2, y2))
        if x1 == x2 or y1 == y2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    grid[x, y] += 1

    for v in grid.values():
        if v >= 2:
            result += 1
    print(result)


def b(lines):
    result = 0
    grid = defaultdict(int)
    for i, line in enumerate(lines):
        one, _, two = line.partition(" -> ")
        x1, y1 = (int(i) for i in one.split(","))
        x2, y2 = (int(i) for i in two.split(","))
        print("{},{} -> {},{}".format(x1, y1, x2, y2))
        if x1 == x2 or y1 == y2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    grid[x, y] += 1
        else:
            m = (y2 - y1) / (x2 - x1)
            c = y1 - (m * x1)
            for y in range(min(y1, y2), max(y1, y2) + 1):
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    if y == round((m * x) + c):
                        grid[x, y] += 1


    # print_grid(grid)
    for v in grid.values():
        if v >= 2:
            result += 1
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
