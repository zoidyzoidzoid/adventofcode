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
        x, _, z = line.partition(": ")
        x, _, y = x.partition(" ")
        l, _, r = x.partition("-")
        l, r = int(l), int(r)
        count = Counter(z)[y]
        if count >= l and count <= r:
            result += 1
    print(result)


def b(lines):
    result = 0
    for _, line in enumerate(lines):
        x, _, z = line.partition(": ")
        x, _, y = x.partition(" ")
        l, _, r = x.partition("-")
        l, r = int(l) - 1, int(r) - 1
        if (z[l] == y and z[r] != y) or (z[l] != y and z[r] == y):
            result += 1
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
