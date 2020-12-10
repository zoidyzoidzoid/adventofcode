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
    start = 0
    count = Counter()
    for line in sorted(lines):
        # print(line)
        diff = line - start
        if diff <= 3:
            count[diff] += 1
            start = line
        else:
            break
    print(count[1], count[3] + 1, count[1] * (count[3] + 1))
    return (start+3)


graph = defaultdict(list)

@lru_cache(maxsize=None)
def traverse(pos, goal):
    result = 0
    for nxt in graph[pos]:
        d = traverse(nxt, goal)
        result += d
    if len(graph[pos]) == 0:
        # prefix = '{},({})'.format(prefix, pos + 3)
        # print(prefix)
        if pos + 3 != goal:
            return result
        return result + 1
    return result


def b(lines, goal):
    lines = list(sorted(lines))
    for i, x in enumerate(lines):
        for y in lines[i + 1:]:
            diff = y - x
            if diff <= 3:
                graph[x].append(y)
            else:
                break
    # print(graph)
    print(traverse(0, goal))


lines = []
for line in fileinput.input():
    lines.append(line.strip())


lines = [0] + [int(i) for i in lines]
goal = a(lines)
b(lines, goal)
