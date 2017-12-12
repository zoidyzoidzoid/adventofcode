#!/usr/bin/env python3
# coding: utf-8
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def visit(visited, nodes, src):
    # print('Visting {}. Seen {}'.format(src, ', '.join(visited)))
    if src not in visited:
        # print('Seen {} for the first time'.format(src))
        visited.add(src)
        for dst in nodes[src]:
            visited = visit(visited, nodes, dst)
    return visited


def process(inp):
    nodes = defaultdict(set)
    for line in inp:
        src, dsts = line.split(' <-> ')
        for dst in dsts.split(', '):
            nodes[src].add(dst)
            nodes[dst].add(src)
    print(nodes)
    groups = defaultdict(set)
    for node in nodes:
        if any(node in group for src, group in groups.items()):
            continue
        visit(groups[node], nodes, node)
    print(groups)
    print(len(groups))


lines = []
for line in fileinput.input():
    lines.append(line.strip())

process(lines)
