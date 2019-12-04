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
    for i, line in enumerate(lines):
        print(line)
    print(result)


def b(lines):
    pass


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
