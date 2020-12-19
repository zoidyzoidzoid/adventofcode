#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import math
import re
import sys
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def expand_a(v, k):
    opts = []
    for a in v[k]:
        sub = ''
        for b in a:
            if b.startswith("\""):
                sub += b[1:-1]
            else:
                sub += expand_a(v, b)
        opts.append(sub)
    if len(opts) == 1:
        return opts[0]
    return '({})'.format('|'.join(opts))


def a(lines):
    rules, messages = '\n'.join(lines).split('\n\n')
    v = {}
    for rule in rules.split('\n'):
        a, _, b = rule.partition(': ')
        v[a] = [i.split(' ') for i in b.split(' | ')]
    pattern = expand_a(v, '0')
    result = 0
    for msg in messages.split('\n'):
        if re.fullmatch(pattern, msg) is not None:
            result += 1
    print(result)


nodes = {}


class Node(object):
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

    def __repr__(self):
        # return '({})'.format(self.node_id)
        return '<Node id={}>'.format(self.node_id)
        # return '<Node id={}, children={}>'.format(self.node_id, self.children)

# def valid(self, b, nxt=None):
#     nxt = nxt or []
#     # print(self, b)
#     if len(self.children) == 1 and len(self.children[0]) == 1 and not isinstance(self.children[0][0], Node):
#         if b.startswith(self.children[0][0]):
#             return True, b[len(self.children[0][0]):]
#         return False, b
#     for nodes in (self.children):
#         nodes += nxt
#         left = b
#         valid = False
#         node = nodes[0]
#         res, left = node.valid(left, nodes[1:])
#         if res == False:
#             break
#         if valid:
#             return True, left
#     return False, b

def bfs(graph, initial, msg):
    queue = deque(((initial, msg, []), ))
    while queue:
        node, msg, nxt = queue.popleft()
        # print(node, msg, nxt)
        neighbours = graph[node.node_id]
        for nodes in neighbours.children:
            nodes = nodes + nxt
            # print('{} -> {} {}'.format(node, nodes[0], nodes[1:]))
            if not isinstance(nodes[0], Node):
                if len(msg) >= 1 and nodes[0] == msg[0]:
                    if len(nodes) <= 1 and len(msg) <= 1:
                        return True
                    elif len(nodes) >= 2 and len(msg) >= 1:
                        queue.append((nodes[1], msg[1:], nodes[2:]))
            else:
                queue.append((nodes[0], msg, nodes[1:]))
    return None



def b(lines):
    rules, messages = '\n'.join(lines).split('\n\n')
    for rule in rules.split('\n'):
        a, _, b = rule.partition(': ')
        if a == '8':
            b = '42 | 42 8'
        elif a == '11':
            b = '42 31 | 42 11 31'
        children = []
        for i in b.split(' | '):
            child = []
            for j in i.split(' '):
                if j.startswith("\""):
                    child.append(j[1:-1])
                else:
                    nodes.setdefault(j, Node(j))
                    node = nodes[j]
                    child.append(node)
            children.append(child)
        nodes.setdefault(a, Node(a))
        nodes[a].children = children

    result = 0
    for msg in messages.split('\n'):
        res = bfs(nodes, nodes['0'], msg)
        print(msg, res)
        if res:
            result += 1
        # break
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


# a(lines)
b(lines)
