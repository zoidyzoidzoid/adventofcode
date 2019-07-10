#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def a(lines):
    result = 0
    line = lines
    grid = {}
    for y in range(1, 301):
        for x in range(1, 301):
            rack_id = x + 10
            power = rack_id * y
            power += line
            power *= rack_id
            power = int(str(int(power / 100))[-1])
            power -= 5
            grid[x, y] = power
    steps = (
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
    )
    mx = None
    mx_c = 0, 0
    for y in range(1, 301 - 2):
        for x in range(1, 301 - 2):
            power = grid[x, y]
            exited = False
            for d_x, d_y in steps:
                if x + d_x > 300:
                    break
                    exited = True
                elif y + d_y > 300:
                    break
                    exited = True
                power += grid[x + d_x, y + d_y]
            if exited:
                continue
            if mx is None or power > mx:
                mx = power
                mx_c = x, y
    print(mx_c, mx)


def b(lines):
    line = lines
    grid = {}
    for y in range(1, 301):
        for x in range(1, 301):
            rack_id = x + 10
            power = rack_id * y
            power += line
            power *= rack_id
            power = int(str(int(power / 100))[-1])
            power -= 5
            grid[x, y] = power
    mx = None
    mx_c = 0, 0
    l_p = 0
    for y in range(1, 301):
        for x in range(1, 301):
            seen = set()
            s = 0
            power = grid[x, y]
            attempts = 0
            while True:
                if x + s > 300 or y + s > 300:
                    break
                for i in range(s):  
                    for j in range(s):  
                        if i == 0 and j == 0:
                            continue
                        if (i, j) in seen:
                            continue
                        seen.add((i, j))
                        power += grid[x + i, y + j]

                if l_p > power:
                    if attempts > 10:
                        break
                    attempts += 1
                else:
                    if mx is None or power > mx:
                        mx = power
                        mx_c = x, y, s
                l_p = power
                s += 1

    print(mx_c, mx)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


lines = int(lines[0])
a(lines)
b(lines)
