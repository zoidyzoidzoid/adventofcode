#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def process(lines):
    grid = defaultdict(str)
    for i, line in enumerate(lines):
        claim, line = line.lstrip("#").split(" @ ")
        coords, size = line.split(": ")
        x, y = coords.split(",")
        x_l, y_l = size.split("x")
        x, y = int(x), int(y)
        x_l, y_l = int(x_l), int(y_l)
        for i in range(x, x + x_l):
            for j in range(y, y + y_l):
                if grid['{},{}'.format(i, j)] == '':
                    grid['{},{}'.format(i, j)] = claim
                else:
                    grid['{},{}'.format(i, j)] = 'X'
    result = 0
    for val in grid.values():
        if val == 'X':
            result += 1
    print(result)
        


lines = []
for line in fileinput.input():
    lines.append(line.strip())


process(lines)
