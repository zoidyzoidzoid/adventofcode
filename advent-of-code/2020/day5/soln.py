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
    result = 0
    for _, line in enumerate(lines):
        l = 0
        r = 127
        for i in range(6):
            # print(i, line[i], l, r)
            m = (l + r) // 2
            if line[i] == "F":
                r = m
            else:
                l = m + 1
        if line[6] == "F":
            row = l
        else:
            row = r
        l = 0
        r = 7
        for i in range(7, 9):
            # print(i, line[i], l, r)
            m = (l + r) // 2
            if line[i] == "L":
                r = m
            else:
                l = m + 1
        if line[9] == "L":
            col = l
        else:
            col = r
        i = (row * 8) + col
        # print(row, col, i)
        result = max((result, i))
    print(result)


def b(lines):
    result = {}
    for _, line in enumerate(lines):
        l = 0
        r = 127
        for i in range(6):
            # print(i, line[i], l, r)
            m = (l + r) // 2
            if line[i] == "F":
                r = m
            else:
                l = m + 1
        if line[6] == "F":
            row = l
        else:
            row = r
        l = 0
        r = 7
        for i in range(7, 9):
            # print(i, line[i], l, r)
            m = (l + r) // 2
            if line[i] == "L":
                r = m
            else:
                l = m + 1
        if line[9] == "L":
            col = l
        else:
            col = r
        i = (row * 8) + col
        # print(row, col, i)
        result[i] = True
    result = list(sorted(result))
    for i, k in enumerate(result[:-1]):
        if k + 1 != result[i + 1]:
            print(k + 1)
    # print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
