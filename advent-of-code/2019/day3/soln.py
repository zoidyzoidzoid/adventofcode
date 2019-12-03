#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import math
import sys
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt

DIRS = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0),
}

DRAW = {
    'U': '|',
    'D': '|',
    'R': '-',
    'L': '-',
}


def a(lines):
    grid = {}
    grid[0, 0] = 'o'
    intersections = defaultdict(set)
    min_x, min_y, max_x, max_y = sys.maxsize, sys.maxsize, -sys.maxsize, -sys.maxsize
    for i, line in enumerate(lines):
        # print(line)
        x, y = 0, 0
        for command in line.split(','):
            d, s = command[0], command[1:]
            s = int(s)
            # print(d, s)
            d_x, d_y = DIRS[d]
            for j in range(s):
                x += d_x
                y += d_y
                min_x = min((min_x, x))
                min_y = min((min_y, y))
                max_x = max((max_x, x))
                max_y = max((max_y, y))
                if x != 0 or y != 0:
                    grid[x, y] = DRAW[d]
                intersections[x, y].add(i)
                if len(intersections[x, y]) > 1:
                    grid[x, y] = 'X'
                elif j == s - 1:
                    grid[x, y] = '+'
                if x == 6 and y == 5:
                    print(i, j, d, s)
                    print(intersections[x, y])
    # for y in range(max_y + 1, min_y - 2, - 1):
    #     row = ''
    #     for x in range(min_x - 2, max_x + 3):
    #         row += grid.get((x, y), '.')
    #     print(row)
    min_dist = sys.maxsize
    # print(intersections)
    for x, y in intersections:
        if len(intersections[x, y]) < 2:
            continue
        dist = abs(x) + abs(y)
        # print(dist)
        min_dist = min((dist, min_dist))
    print(min_dist)


def b(lines):
    grid = {}
    grid[0, 0] = 'o'
    intersections = defaultdict(set)
    total_steps = {}
    min_x, min_y, max_x, max_y = sys.maxsize, sys.maxsize, -sys.maxsize, -sys.maxsize
    for i, line in enumerate(lines):
        # print(line)
        x, y = 0, 0
        steps = 0
        for command in line.split(','):
            d, s = command[0], command[1:]
            s = int(s)
            # print(d, s)
            d_x, d_y = DIRS[d]
            for j in range(s):
                total_steps[i, x, y] = steps
                steps += 1
                x += d_x
                y += d_y
                min_x = min((min_x, x))
                min_y = min((min_y, y))
                max_x = max((max_x, x))
                max_y = max((max_y, y))
                if x != 0 or y != 0:
                    grid[x, y] = DRAW[d]
                intersections[x, y].add(i)
                if len(intersections[x, y]) > 1:
                    grid[x, y] = 'X'
                elif j == s - 1:
                    grid[x, y] = '+'
                # if x == 6 and y == 5:
                #     print(i, j, d, s)
                #     print(intersections[x, y])
    # for y in range(max_y + 1, min_y - 2, - 1):
    #     row = ''
    #     for x in range(min_x - 2, max_x + 3):
    #         row += grid.get((x, y), '.')
    #     print(row)
    min_dist = sys.maxsize
    # print(intersections)
    for x, y in intersections:
        if len(intersections[x, y]) < 2:
            continue
        dist = 0
        for wire in intersections[x, y]:
            # print(steps[wire, x, y])
            dist += total_steps[wire, x, y]
        # print(x, y, dist)
        min_dist = min((dist, min_dist))
    print(min_dist)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


# a(lines)
b(lines)
