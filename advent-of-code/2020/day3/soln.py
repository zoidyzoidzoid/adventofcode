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


def a(lines):
    result = 1
    lines = [list(i) for i in lines]
    mx_y = len(lines)
    x = 0
    y = 0
    p = 0
    while y + 1 < mx_y:
        x = (x + 3) % len(lines[0])
        y += 1
        if lines[y][x] == "#":
            p += 1
    print(p)


def b(lines):
    result = 1
    lines = [list(i) for i in lines]
    mx_y = len(lines)
    for d_x in [1, 3, 5, 7]:
        x = 0
        y = 0
        p = 0
        while y + 1 < mx_y:
            x = (x + d_x) % len(lines[0])
            y += 1
            if lines[y][x] == "#":
                p += 1
        print(p)
        result *= p
    x = 0
    y = 0
    p = 0
    while y + 2 < mx_y:
        x = (x + 1) % len(lines[0])
        y += 2
        if lines[y][x] == "#":
            p += 1
    print(p)
    result *= p

    # for line in lines:
    #     print(''.join(line))
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
