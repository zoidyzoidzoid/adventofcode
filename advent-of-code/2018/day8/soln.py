#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


class Node(object):
    def __init__(self, children=None, metadata=None):
        self.children = children or []
        self.metadata = metadata or []


def traverse(root):
    return sum(root.metadata) + sum((traverse(child) for child in root.children))

def traverse_b(root):
    result = 0
    if not root.children:
        return sum(root.metadata)
    # print(root, root.metadata, root.children)
    for i in root.metadata:
        if i - 1 < len(root.children):
            result += traverse_b(root.children[i - 1])
    return result


def add(root, line):
    c = int(line.popleft())
    m = int(line.popleft())
    # print(c, m)
    node = Node()
    if root is None:
        root = node
    else:
        root.children.append(node)
    for i in range(c):
        add(node, line)
    for i in range(m):
        node.metadata.append(int(line.popleft()))
    return root, line


def a(lines):
    result = 0
    line = deque(lines[0].split(" "))
    root = None
    while line:
        root, line = add(root, line)

    result = traverse(root)

    print(result)


def b(lines):
    result = 0
    line = deque(lines[0].split(" "))
    root = None
    while line:
        root, line = add(root, line)

    result = traverse_b(root)

    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
