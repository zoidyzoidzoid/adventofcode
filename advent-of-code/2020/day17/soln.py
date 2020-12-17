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
    mn_x, mx_x, mn_y, mx_y, mn_z, mx_z = 0, len(lines[0]), 0, len(lines), 0, 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                data[x, y, 0] = c
    mn_x, mx_x, mn_y, mx_y, mn_z, mx_z = mn_x-1, mx_x+2, mn_y-1, mx_y+2, mn_z-1, mx_z+2


    for cycle in range(6):
        nxt = data.copy()
        for z in range(mn_z, mx_z):
            for y in range(mn_y, mx_y):
                for x in range(mn_x, mx_x):
                    c = data.get((x, y, z), '.')
                    count = Counter()
                    for d_x, d_y, d_z in DIRS_2D:
                        count[data.get((x + d_x, y + d_y, z + d_z), '.')] += 1
                    if c == '#':
                        if count['#'] in (2, 3):
                            nxt[x, y, z] = '#'
                        else:
                            nxt.pop((x, y, z), None)
                    elif c == '.':
                        if count['#'] == 3:
                            nxt[x, y, z] = '#'
                        else:
                            nxt.pop((x, y, z), None)

        data = nxt
        mn_x = mn_x - 1
        mx_x = mx_x + 2
        mn_y = mn_y - 1
        mx_y = mx_y + 2
        mn_z = mn_z - 1
        mx_z = mx_z + 2

    # result = 0
    # print(result)
    print(len(data))


def b(lines):
    data = {}
    mn_x, mx_x, mn_y, mx_y, mn_z, mx_z, mn_w, mx_w = 0, len(lines[0]), 0, len(lines), 0, 0, 0, 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                data[x, y, 0, 0] = c
    mn_x, mx_x, mn_y, mx_y, mn_z, mx_z, mn_w, mx_w = mn_x-1, mx_x+2, mn_y-1, mx_y+2, mn_z-1, mx_z+2, mn_w-1, mx_w+2


    for cycle in range(6):
        nxt = data.copy()
        for w in range(mn_w, mx_w):
            for z in range(mn_z, mx_z):
                for y in range(mn_y, mx_y):
                    for x in range(mn_x, mx_x):
                        c = data.get((x, y, z, w), '.')
                        count = Counter()
                        for d_x, d_y, d_z, d_w in DIRS:
                            count[data.get((x + d_x, y + d_y, z + d_z, w + d_w), '.')] += 1
                        if c == '#':
                            if count['#'] in (2, 3):
                                nxt[x, y, z, w] = '#'
                            else:
                                nxt.pop((x, y, z, w), None)
                        elif c == '.':
                            if count['#'] == 3:
                                nxt[x, y, z, w] = '#'
                            else:
                                nxt.pop((x, y, z, w), None)

        data = nxt
        mn_x = mn_x - 1
        mx_x = mx_x + 2
        mn_y = mn_y - 1
        mx_y = mx_y + 2
        mn_z = mn_z - 1
        mx_z = mx_z + 2
        mn_w = mn_w - 1
        mx_w = mx_w + 2

    # result = 0
    # print(result)
    print(len(data))


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
