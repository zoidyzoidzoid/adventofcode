#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def a(lines):
    s = deque()
    e = deque(lines[0])
    while e:
        y = e.popleft()
        if s:
            x = s.pop()
        else:
            x, y = y, e.popleft()
        if x != y and x.lower() == y.lower():
            continue
        else:
            s.append(x)
            s.append(y)
    print(len(s))
    return len(s)


def b(lines):
    line = lines[0]
    import sys
    mn = sys.maxsize
    polymers = set(line.lower())
    for polymer in polymers:
        l = line.replace(polymer, '').replace(polymer.upper(), '')
        s = deque()
        e = deque(l)
        while e:
            y = e.popleft()
            if s:
                x = s.pop()
            else:
                x, y = y, e.popleft()
            if x != y and x.lower() == y.lower():
                continue
            else:
                s.append(x)
                s.append(y)
        result = len(s)
        mn = min((mn, result))
    print(mn)
    return mn


lines = []
for line in fileinput.input():
    lines.append(line.strip())


# assert a(lines) == 10
# assert a(lines) == 11118
assert b(lines) == 6948
