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
from time import time_ns


def a(lines):
    result = 0
    x, y = defaultdict(list), []
    for i, line in enumerate(lines):
        if not line:
            continue
        elif "|" in line:
            i, _, j = line.partition("|")
            i, j = int(i), int(j)
            x[j].append(i)
        else:
            y.append(line)
    # print(x)
    for line in y:
        line = line.split(",")
        updates = deque([int(i) for i in line])
        after = set()
        broken = False
        while updates:
            c = updates.pop()
            if any(i in after for i in x[c]):
                broken = True
                break
            after.add(c)
        if not broken:
            result += int(line[len(line) // 2])
            # print(line)
            # print(int(line[len(line) // 2]))
    print(result)


def dfs_rec(adj, visited, s, path):
    # Mark the current vertex as visited
    visited.add(s)

    # Print the current vertex
    path.append(s)

    # Recursively visit all adjacent vertices
    # that are not visited yet
    for i in adj[s]:
        if i not in visited:
            dfs_rec(adj, visited, i, path)
    return path


def dfs(adj, s):
    visited = set()
    # Call the recursive DFS function
    return dfs_rec(adj, visited, s, path=[])


def b(lines):
    result = 0
    x, y = defaultdict(list), []
    for i, line in enumerate(lines):
        if not line:
            continue
        elif "|" in line:
            i, _, j = line.partition("|")
            i, j = int(i), int(j)
            x[i].append(j)
        else:
            y.append(line)
    # from pprint import pprint
    # pprint(x)
    for line in y:
        line = [int(i) for i in line.split(",")]
        updates = deque(line)
        after = set()
        broken = False
        while updates:
            c = updates.pop()
            if any(i in after for i in x[c]):
                broken = True
                break
            after.add(c)
        if broken:
            from pprint import pprint
            # pprint(x)
            for i in line:
                tmp = dfs(x, i)
                if all(i in tmp for i in line):
                    print(line)
                    print(tmp)
                    print(tmp[len(tmp) // 2])
                    result += tmp[len(tmp) // 2]
                    break
            else:
                raise Exception("No brute force solution")
            return
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


class Timer(object):
    def __init__(self, description):
        self.description = description
    def __enter__(self):
        self.start = time_ns()
    def __exit__(self, type, value, traceback):
        self.end = time_ns()
        d = self.end - self.start
        if d > 1_000_000_000:
            d /= 1_000_000_000
            u = "s"
        elif d > 1_000_000:
            d /= 1_000_000
            u = "ms"
        elif d > 1_000:
            d /= 1_000
            u = "µs"
        else:
            u = "ns"
        print("{}: {} {}".format(self.description, d, u))


def main():
    # with Timer("Part 1"):
    #     a(lines)

    with Timer("Part 2"):
        b(lines)


if __name__ == "__main__":
    main()
