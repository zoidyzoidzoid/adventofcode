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
    a = deque()
    pre = 25
    for line in lines:
        if len(a) < pre:
            a.append(line)
        else:
            found = False
            for i, x in enumerate(a):
                for y in range(i, pre):
                    y = a[y]
                    if x + y == line:
                        found = True
                        break
                if found: break
            if not found:
                print(line)
                return line
                break
            a.popleft()
            a.append(line)


def b(lines, goal):
    for start, x in enumerate(lines):
        sm = x
        mn = x
        mx = x
        for y in lines[start+1:]:
            sm += y
            mn = min((mn, y))
            mx = max((mx, y))
            if sm == goal:
                print(mn, mx, mn + mx)
                break


lines = []
for line in fileinput.input():
    lines.append(line.strip())


lines = [int(line) for line in lines]
goal = a(lines)
b(lines, goal)
