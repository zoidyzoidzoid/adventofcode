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


# cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
# cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.

DIRS_2D = {
    (1, 1, 1),
    (1, 1, 0),
    (1, 1, -1),
    (1, 0, 1),
    (1, 0, 0),
    (1, 0, -1),
    (1, -1, 1),
    (1, -1, 0),
    (1, -1, -1),
    (0, 1, 1),
    (0, 1, 0),
    (0, 1, -1),
    (0, 0, 1),
    # (0, 0, 0),
    (0, 0, -1),
    (0, -1, 1),
    (0, -1, 0),
    (0, -1, -1),
    (-1, 1, 1),
    (-1, 1, 0),
    (-1, 1, -1),
    (-1, 0, 1),
    (-1, 0, 0),
    (-1, 0, -1),
    (-1, -1, 1),
    (-1, -1, 0),
    (-1, -1, -1),
}

DIRS = {
    (-1, -1, -1, -1),
    (-1, -1, -1, 0),
    (-1, -1, -1, 1),
    (-1, -1, 0, -1),
    (-1, -1, 0, 0),
    (-1, -1, 0, 1),
    (-1, -1, 1, -1),
    (-1, -1, 1, 0),
    (-1, -1, 1, 1),
    (-1, 0, -1, -1),
    (-1, 0, -1, 0),
    (-1, 0, -1, 1),
    (-1, 0, 0, -1),
    (-1, 0, 0, 0),
    (-1, 0, 0, 1),
    (-1, 0, 1, -1),
    (-1, 0, 1, 0),
    (-1, 0, 1, 1),
    (-1, 1, -1, -1),
    (-1, 1, -1, 0),
    (-1, 1, -1, 1),
    (-1, 1, 0, -1),
    (-1, 1, 0, 0),
    (-1, 1, 0, 1),
    (-1, 1, 1, -1),
    (-1, 1, 1, 0),
    (-1, 1, 1, 1),
    (0, -1, -1, -1),
    (0, -1, -1, 0),
    (0, -1, -1, 1),
    (0, -1, 0, -1),
    (0, -1, 0, 0),
    (0, -1, 0, 1),
    (0, -1, 1, -1),
    (0, -1, 1, 0),
    (0, -1, 1, 1),
    (0, 0, -1, -1),
    (0, 0, -1, 0),
    (0, 0, -1, 1),
    (0, 0, 0, -1),
    # (0, 0, 0, 0),
    (0, 0, 0, 1),
    (0, 0, 1, -1),
    (0, 0, 1, 0),
    (0, 0, 1, 1),
    (0, 1, -1, -1),
    (0, 1, -1, 0),
    (0, 1, -1, 1),
    (0, 1, 0, -1),
    (0, 1, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 1, -1),
    (0, 1, 1, 0),
    (0, 1, 1, 1),
    (1, -1, -1, -1),
    (1, -1, -1, 0),
    (1, -1, -1, 1),
    (1, -1, 0, -1),
    (1, -1, 0, 0),
    (1, -1, 0, 1),
    (1, -1, 1, -1),
    (1, -1, 1, 0),
    (1, -1, 1, 1),
    (1, 0, -1, -1),
    (1, 0, -1, 0),
    (1, 0, -1, 1),
    (1, 0, 0, -1),
    (1, 0, 0, 0),
    (1, 0, 0, 1),
    (1, 0, 1, -1),
    (1, 0, 1, 0),
    (1, 0, 1, 1),
    (1, 1, -1, -1),
    (1, 1, -1, 0),
    (1, 1, -1, 1),
    (1, 1, 0, -1),
    (1, 1, 0, 0),
    (1, 1, 0, 1),
    (1, 1, 1, -1),
    (1, 1, 1, 0),
    (1, 1, 1, 1),
}

def a(lines):
    data = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                data[x, y, 0] = c


    for cycle in range(6):
        nxt = data.copy()
        queue = set(data.keys())
        seen = set()
        while queue:
            x, y, z = queue.pop()
            seen.add((x, y, z))

            c = data.get((x, y, z), '.')

            cnt = 0
            for d_x, d_y, d_z in DIRS_2D:
                d = data.get((x + d_x, y + d_y, z + d_z), '.')
                if d == '#':
                    cnt += 1
                if c == '#' and (x + d_x, y + d_y, z + d_z) not in seen:
                    queue.add((x + d_x, y + d_y, z + d_z))
            if c == '#':
                if cnt in (2, 3):
                    nxt[x, y, z] = '#'
                else:
                    nxt.pop((x, y, z), None)
            elif c == '.':
                if cnt == 3:
                    nxt[x, y, z] = '#'
                else:
                    nxt.pop((x, y, z), None)

        data = nxt

    # result = 0
    # print(result)
    print(len(data))


def b(lines):
    data = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                data[x, y, 0, 0] = c


    for cycle in range(6):
        nxt = data.copy()
        queue = set(data.keys())
        seen = set()
        while queue:
            x, y, z, w = queue.pop()
            seen.add((x, y, z, w))
            c = data.get((x, y, z, w), '.')
            cnt = 0
            for d_x, d_y, d_z, d_w in DIRS:
                d = data.get((x + d_x, y + d_y, z + d_z, w + d_w), '.')
                if d == '#':
                    cnt += 1
                if c == '#' and (x + d_x, y + d_y, z + d_z, w + d_w) not in seen:
                    queue.add((x + d_x, y + d_y, z + d_z, w + d_w))
            if cnt == 3:
                nxt[x, y, z, w] = '#'
            elif cnt == 2 and c == '#':
                nxt[x, y, z, w] = '#'
            else:
                nxt.pop((x, y, z, w), None)

        data = nxt

    # result = 0
    # print(result)
    print(len(data))


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
