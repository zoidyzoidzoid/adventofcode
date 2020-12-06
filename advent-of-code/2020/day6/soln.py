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
    yess = {}
    for i, line in enumerate(lines):
        if line == "":
            result += len(yess)
            yess = {}
        else:
            for c in line:
                yess.setdefault(c, True)

    result += len(yess)
    print(result)


def b(lines):
    result = 0
    yess = None
    for i, line in enumerate(lines):
        if line == "":
            result += len(yess)
            yess = None
        else:
            if yess is None:
                yess = set(line)
            else:
                yess = yess.intersection(set(line))

    result += len(yess)
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
