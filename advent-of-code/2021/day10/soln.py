#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import sys
import math
import statistics
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt
from time import time_ns


def a(lines):
    ss = {
        "[": "]",
        "(": ")",
        "{": "}",
        "<": ">",
    }
    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    result = 0
    for i, line in enumerate(lines):
        stack = []
        for c in line:
            if c in ss:
                stack.append(ss[c])
            elif c == stack[-1]:
                stack.pop()
            else:
                # print("Expected: {}, Found: {}".format(stack[-1], c))
                result += scores[c]
                break

    print(result)


def b(lines):
    ss = {
        "[": "]",
        "(": ")",
        "{": "}",
        "<": ">",
    }
    scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    results = []
    for i, line in enumerate(lines):
        stack = []
        tmp = 0
        for c in line:
            if c in ss:
                stack.append(ss[c])
            elif c == stack[-1]:
                stack.pop()
            else:
                break
        else:
            for c in reversed(stack):
                tmp *= 5
                tmp += scores[c]
            results.append(tmp)

    print(statistics.median(sorted(results)))


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
        d = self.end - self.start
        if d > 1_000_000_000:
            d /= 1_000_000_000
            u = "s"
        elif d > 1_000_000:
            d /= 1_000_000
            u = "ms"
        elif d > 1_000:
            d /= 1_000
            u = "µs"
        else:
            u = "ns"
        print("{}: {} {}".format(self.description, d, u))


with Timer("Part 1"):
    a(lines)


with Timer("Part 2"):
    b(lines)
