#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import sys
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def a(lines):
    grid = dict()
    s = 'A'
    for i, line in enumerate(lines):
        x, y = line.split(", ")
        x, y = int(x), int(y)
        # print(x, y)
        grid[x, y] = s
        if s[-1] == 'Z':
            s += 'A'
        s = s[:-1] + chr(ord(s[-1]) + 1)
    # print(grid)
    dirs = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )
    mx_x, mx_y = max(i[0] for i in grid.keys()), max(i[1] for i in grid.keys())
    dists = dict()
    i, j = 0, 0
    while i <= mx_x:
        j = 0
        while j <= mx_y:
            mn = sys.maxsize
            mn_l = set()
            for x, y in grid.keys():
                dist = abs(j - y) + abs(i - x)
                if dist <= mn:
                    if dist == mn:
                        mn_l.add(grid[x, y].lower())
                    else:
                        mn = dist
                        mn_l = set(grid[x, y].lower())
            if len(mn_l) > 1:
                dists[i, j] = '.'
            else:
                dists[i, j] = ''.join(mn_l)
            j += 1
        i += 1
    inf = set()
    for k, v in dists.items():
        x, y = k
        if x == 0 or y == 0 or x == mx_x or y == mx_y:
            inf.add(v)
    c = Counter(dists.values())
    # print(c)
    for k in inf:
        del c[k]
    print(c.most_common(1)[0][1])



def b(lines):
    grid = dict()
    s = 'A'
    for i, line in enumerate(lines):
        x, y = line.split(", ")
        x, y = int(x), int(y)
        # print(x, y)
        grid[x, y] = s
        if s[-1] == 'Z':
            s += 'A'
        s = s[:-1] + chr(ord(s[-1]) + 1)
    # print(grid)
    mx_x, mx_y = max(i[0] for i in grid.keys()), max(i[1] for i in grid.keys())
    i, j = 0, 0
    dist_sm_sms = 0
    while i <= mx_x:
        j = 0
        while j <= mx_y:
            dist_sm = 0
            for x, y in grid.keys():
                dist_sm += abs(j - y) + abs(i - x)
            if dist_sm < 10000:
                dist_sm_sms += 1
            j += 1
        i += 1
    print(dist_sm_sms)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
