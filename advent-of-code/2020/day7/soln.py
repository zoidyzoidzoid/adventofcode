#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import json
import sys
import math
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


data = defaultdict(dict)


def traverse_a(start, seen=set()):
    for x, v in data.get(start, {}).items():
        # print('Starting at {} going to {}'.format(start, x))
        if x not in seen:
            seen = seen.union(traverse_a(x, seen))
            seen.add(x)
    return seen


def a(lines):

    for i, line in enumerate(lines):
        line = line.rstrip(".")
        a, _, b = line.partition(" contain ")
        if b == "no other bags":
            continue
        b = b.split(", ")
        for c in b:
            if not c.endswith("s"):
                c += "s"
            n, c = c.split(" ", 1)
            data[a][c] = int(n)
    # print(json.dumps(data, indent=2))

    result = 0
    for x, v in data.items():
        if "shiny gold bags" in traverse_a(x):
            result += 1
    print(result)


def traverse_b(start, n=0):
    for x, v in data.get(start, {}).items():
        # print('Starting at {} going to {}'.format(start, x))
        n += v * traverse_b(x, 1)
    return n


def b(lines):
    for i, line in enumerate(lines):
        line = line.rstrip(".")
        a, _, b = line.partition(" contain ")
        if b == "no other bags":
            continue
        b = b.split(", ")
        for c in b:
            if not c.endswith("s"):
                c += "s"
            n, c = c.split(" ", 1)
            data[a][c] = int(n)
    print(json.dumps(data, indent=2))

    result = 0
    result = traverse_b("shiny gold bags")
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
