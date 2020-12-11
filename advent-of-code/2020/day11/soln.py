#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import sys
import math
from collections import Counter, defaultdict, deque
from copy import deepcopy
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def print_grid(data):
    print("=" * mx_x)
    print("=" * mx_x)
    for j in range(mx_y):
        for i in range(mx_x):
            print(data[i, j], end='')
        print()
    print("=" * mx_x)
    print("=" * mx_x)

dirs = {
    (1, 1),
    (1, 0),
    (1, -1),
    (0, 1),
    (0, -1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
}

def a(lines):
    data = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            data[x, y] = c
    # print(data)
    # print_grid(data)
    while True:
        nxt = deepcopy(data)
        for y in range(mx_y):
            for x in range(mx_x):
                c = data[x, y]
                cnt = Counter()
                for d_x, d_y in dirs:
                    d = data.get((x + d_x, y + d_y))
                    cnt[d] += 1
                if c == 'L' and cnt['#'] == 0:
                    nxt[x, y] = '#'
                elif c == '#' and cnt['#'] >= 4:
                    nxt[x, y] = 'L'
        if data == nxt:
            break
        data = nxt
    # print_grid(data)
    print(Counter(data.values())['#'])


def b(lines):
    data = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            data[x, y] = c
    # print(data)
    # print_grid(data)
    while True:
        nxt = deepcopy(data)
        for y in range(mx_y):
            for x in range(mx_x):
                c = data[x, y]
                cnt = Counter()
                for d_x, d_y in dirs:
                    d = data.get((x + d_x, y + d_y))
                    cnt[d] += 1
                    i = 1
                    while d not in (None, '#', 'L'):
                        i += 1
                        d = data.get((x + (d_x * i), y + (d_y * i)))
                        cnt[d] += 1
                if c == 'L' and cnt['#'] == 0:
                    nxt[x, y] = '#'
                elif c == '#' and cnt['#'] >= 5:
                    nxt[x, y] = 'L'
        if data == nxt:
            break
        data = nxt
    # print_grid(data)
    print(Counter(data.values())['#'])


lines = []
for line in fileinput.input():
    lines.append(line.strip())

mx_x = len(lines[0])
mx_y = len(lines)


a(lines)
b(lines)
