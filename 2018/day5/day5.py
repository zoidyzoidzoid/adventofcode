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
    line = lines[0]
    l = line
    while True:
        operated = False
        s = ''
        ss = 0
        i = 0
        while i < len(l) - 1:
            # print(l[i])
            c = l[i]
            d = l[i+1]
            if c != d and c.lower() == d.lower():
                s += l[ss:i]
                ss = i + 2
                operated = True
                i += 2
            else:
                i += 1
        print(s)
        l = s + l[ss:]
        if operated == False:
            break
    result = len(l)
    print(result)


def b(lines):
    line = lines[0]
    import sys
    mn = sys.maxsize
    polymers = set(line.lower())
    for polymer in polymers:
        l = line.replace(polymer, '').replace(polymer.upper(), '')
        while True:
            operated = False
            s = ''
            ss = 0
            i = 0
            while i < len(l) - 1:
                # print(l[i])
                c = l[i]
                d = l[i+1]
                if c != d and c.lower() == d.lower():
                    s += l[ss:i]
                    ss = i + 2
                    operated = True
                    i += 2
                else:
                    i += 1
            # print(s)
            l = s + l[ss:]
            if operated == False:
                break
        result = len(l)
        mn = min((mn, result))
    print(mn)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
