#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


class Port(object):
    def __init__(self, uid, name, start, end):
        self.uid = uid
        self.name = name
        self.start = start
        self.end = end
    
    def __repr__(self):
        return '<Port(uid={}, name=\'{}\', start={}, end={})>'.format(self.uid, self.name, self.start, self.end)


def get_next_steps(root, ports, seen):
    results = []
    for port in ports:
        if port.uid in seen:
            continue
        if root.end == port.start:
            results.append(port)
        elif root.end == port.end:
            port.start, port.end = port.end, port.start
            results.append(port)
    if results:
        print('Possible steps:')
        for result in results:
            print('{} -> {}'.format(root.name, result.name))
        print()
    return results


def traverse(root, ports, seen, score=0):
    score += root.start + root.end

    print("Exploring {}, score: {})".format(root.name, score))

    seen.add(root.uid)
    results = [(score, seen), ]
    for port in get_next_steps(root, ports, seen):
        results.extend(traverse(port, ports, seen.copy(), score=score))
    return results


def process(lines):
    nodes = defaultdict(list)
    ports = []
    for i, line in enumerate(lines):
        a, b = line.split('/')
        a, b = int(a), int(b)
        if a > b:
            a, b = b, a
        node = Port(i, line, a, b)
        nodes[a].append(node)
        ports.append(node)

    from pprint import pprint
    pprint(nodes)

    for port in ports:
        nodes[port.end].append(port)

    mx = 0
    for root in nodes[0]:
        print()
        print("Found root: {}".format(root.name))
        mx = max((mx, max(i[0] for i in traverse(root, ports, set()))))

    print("Found max path: {}".format(mx))

lines = []
for line in fileinput.input():
    lines.append(line.strip())

process(lines)
