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
from pprint import pprint


def a(lines):
    ns = deque()
    for i, line in enumerate(lines[0].split(",")):
        line = int(line)
        ns.appendleft(line)

    while True:
        t = len(ns) + 1
        if t > 2020:
            print(ns[0])
            break

        last = ns[0]
        try:
            last_index = t - ns.index(last, 1)
        except:
            last_index = None

        if last_index is None:
            new = 0
        else:
            new = t - last_index
        ns.appendleft(new)


def b(lines):
    ns = defaultdict(lambda: deque(maxlen=2))
    for i, line in enumerate(lines[0].split(","), 1):
        line = int(line)
        ns[line].appendleft(i)
        t = i
        last = line
        # print('{}: {}'.format(t, line))
    while True:
        if t >= 30000000:
            print(last)
            break
        t += 1
        if len(ns[last]) != 2:
            nxt = 0
        else:
            nxt = ns[last][0] - ns[last][1]
        # print('{}: {}'.format(t, nxt))
        ns[nxt].appendleft(t)
        last = nxt
        # pprint(ns)

lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
