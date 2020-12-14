#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import sys
import math
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import cache, lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def a(lines):
    start = int(lines[0])
    buses = []
    for bus_id in lines[1].split(','):
        if bus_id == 'x':
            continue
        buses.append(int(bus_id))
    mn, when = 0, 0
    data = {}
    for bus_id in buses:
        nxt = (((start - 1) // bus_id) + 1) * bus_id
        data[bus_id] = nxt, nxt - start
    # for bus_id in sorted(buses):
    #     print(bus_id, *data[bus_id])
    mn = min(data.items(), key=lambda x: x[1][1])
    bus_id, (_, wait) = mn
    print(bus_id * wait)


def b(lines):
    buses = {}
    for c, bus_id in enumerate(lines[1].split(',')):
        if bus_id == 'x':
            continue
        buses[int(bus_id)] = c
    d = 1
    t = 0
    buses = list(buses.items())
    for i, (bus_id, c) in enumerate(buses[1:]):
        d *= buses[i][0]
        while (t + c) % bus_id != 0:
            t += d
    print(t)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
