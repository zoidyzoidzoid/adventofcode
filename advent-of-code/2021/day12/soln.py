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
from time import time_ns


def a(lines):
    nodes = defaultdict(list)
    for i, line in enumerate(lines):
        s, _, e = line.partition("-")
        nodes[s].append(e)
        nodes[e].append(s)
    def next_steps(a, path):
        if a == "end":
            return []
        res = []
        for nxt in nodes[a]:
            if nxt.islower() and nxt in path.split(","):
                continue
            res.append(nxt)
        return res
    # print(nodes)
    paths = [
        "start"
    ]
    old_paths = None
    result = 0
    while paths != old_paths:
        old_paths = paths.copy()
        for path in old_paths:
            # print("Exploring from", path)
            nxts = next_steps(path.split(",")[-1], path)
            if nxts:
                paths.remove(path)
            for next_step in nxts:
                # print("  to", next_step)
                paths.append("{},{}".format(path, next_step))
    # print("\n".join(paths))
    print(len([path for path in paths if path.endswith(",end")]))


def b(lines):
    nodes = defaultdict(list)
    for i, line in enumerate(lines):
        s, _, e = line.partition("-")
        if e != "start":
            nodes[s].append(e)
        if s != "start":
            nodes[e].append(s)
    def next_steps(a, path):
        if a == "end":
            return []
        res = []
        for nxt in nodes[a]:
            chunks = Counter(path.split(","))
            if nxt.islower() and (chunks[nxt] == 2 or (any(chunks[c] == 2 for c in chunks if c.islower()) and chunks[nxt] == 1)):
                continue
            res.append(nxt)
        return res
    # print(nodes)
    paths = {
        "start"
    }
    old_paths = None
    result = 0
    while paths != old_paths:
        old_paths = paths.copy()
        for path in old_paths:
            # print("Exploring from", path)
            nxts = next_steps(path.split(",")[-1], path)
            if nxts:
                paths.discard(path)
            for next_step in nxts:
                # print("  to", next_step)
                paths.add("{},{}".format(path, next_step))
    paths = [path for path in paths if path.endswith(",end")]
    print("\n".join(paths))
    print(len(paths))


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
