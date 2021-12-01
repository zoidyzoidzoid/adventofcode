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
    result = 0
    last = None
    for i, line in enumerate(lines):
        line = int(line)
        if last is not None and line > last:
            result += 1
        last = line
    print(result)


def b(lines):
    result = 0
    last = None
    last1 = None
    last2 = None
    last3 = None
    for i, line in enumerate(lines):
        line = int(line)
        if last is not None and (line + last1 + last2) > last:
            result += 1
        last1, last2, last3 = (line, last1, last2)
        if all(i is not None for i in (last1, last2, last3)):
            last = last1 + last2 + last3
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
