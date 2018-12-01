#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def process(lines):
    freq = 0
    seen = set()
    while True:
        for line in lines:
            freq += int(line)
            if freq in seen:
                return freq
            seen.add(freq)


lines = []
for line in fileinput.input():
    lines.append(line.strip())

print(process(lines))
