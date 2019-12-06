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
    orbits = defaultdict(set)
    for i, line in enumerate(lines):
        a, _, b = line.partition(')')
        # print(a, b)
        orbits[a].add(b)

    result = 0
    for planet in orbits.copy():
        work = [planet]
        while work:
            start = work.pop()
            for planet in orbits[start]:
                work.append(planet)
                result += 1
    # print(result)


def route_home(orbits, e):
    s = 'COM'
    route = deque()
    while e != s:
        for k, v in orbits.items():
            if e in v:
                if e not in ('SAN', 'YOU'):
                    route.appendleft(e)
                e = k
                break
    return route


def resolve(orbits, e):
    work = ['COM']
    while work:
        i = work.pop()
        for j in orbits[i]:
            if j == e:
                return route_home(orbits, e)
            work.append(j)


def b(lines):
    orbits = defaultdict(set)
    start = None
    dest = None
    for i, line in enumerate(lines):
        a, _, b = line.partition(')')
        # print(a, b)

        orbits[a].add(b)

        if b == 'YOU':
            start = a
        if b == 'SAN':
            dest = a

    curr = resolve(orbits, 'YOU')
    end = resolve(orbits, 'SAN')
    print(','.join(curr))
    print(','.join(end))
    curr = list(curr)
    end = list(end)
    prefix = ''
    result = 0
    for i, c in enumerate(curr):
        if i < len(end) and c == end[i]:
            continue
        result = len(curr[i:]) + len(end[i:])
        break
    print(result)



lines = []
for line in fileinput.input():
    lines.append(line.strip())


# a(lines)
b(lines)
