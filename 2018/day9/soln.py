#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


class DLL(object):
    def __init__(self, val, prv=None, nxt=None):
        self.val = val
        self.prv = prv
        self.nxt = nxt

    def insert(self, v):
        node = DLL(v, self, self.nxt)
        self.nxt.prv = node
        self.nxt = node
        return node

    def remove(self):
        n = self.nxt
        self.nxt.prv = self.prv
        self.prv.nxt = self.nxt
        return n


def a(players, marbles):
    ps, ms = players, marbles
    root = DLL(0)
    root.nxt = root
    root.prv = root
    loc = root
    p = 1
    scores = defaultdict(int)
    for m in range(1, ms + 1):
        if m % 23 == 0:
            loc = loc.prv.prv.prv.prv.prv.prv.prv
            scores[p] += m
            scores[p] += loc.val
            loc = loc.remove()
        else:
            loc = loc.nxt
            loc = loc.insert(m)
        p = (p % ps) + 1

        # r = root
        # s = []
        # seen = set()
        # while r.val not in seen:
        #     seen.add(r.val)
        #     s.append(r.val)
        #     r = r.nxt
        # print(' '.join((str(i) for i in s)))
    print(max(scores.values()))


def b(ps, ms):
    a(ps, ms * 100)


lines = []
for line in fileinput.input():
    lines.append(line.strip())

line = lines[0].split(' ')
ps, ms = line[0], line[6]
ps, ms = int(ps), int(ms)

a(ps, ms)
b(ps, ms)
