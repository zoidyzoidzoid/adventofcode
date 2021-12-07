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
from time import time, time_ns


def a(lines):
    result = Counter()
    for i, line in enumerate(lines):
        for f in line.split(","):
            f = int(f)
            result[f] += 1
    print(result)

    for i in range(80):
        new = Counter()
        for k, v in result.items():
            if k == 0:
                new[6] += v
                new[8] += v
            else:
                new[k-1] += v
        #    for i in range(v):
        #         print(k, end=",")
        # print()
        result = new
        if i == 17:
            print(sum(result.values()))
    print(sum(result.values()))


def b(lines):
    result = Counter()
    for i, line in enumerate(lines):
        for f in line.split(","):
            f = int(f)
            result[f] += 1
    print(result)

    for i in range(256):
        new = Counter()
        for k, v in result.items():
            if k == 0:
                new[6] += v
                new[8] += v
            else:
                new[k-1] += v
        result = new
    print(sum(result.values()))


lines = []
for line in fileinput.input():
    lines.append(line.strip())


class Timer(object):
    def __init__(self, description):
        self.description = description
    def __enter__(self):
        self.start = time_ns()
    def __exit__(self, type, value, traceback):
        self.end = time_ns()
        print("{}: {} µ".format(self.description, (self.end - self.start) / 1000))


with Timer("Part 1"):
    a(lines)


with Timer("Part 2"):
    b(lines)

