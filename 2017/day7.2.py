#!/usr/bin/env python3
import fileinput
from collections import defaultdict


class Node(object):
    def __init__(self, name, weight, holding_up=None):
        self.name = name
        self.weight = weight
        if holding_up is not None:
            self.holding_up = holding_up


def process(inp):
    nodes = {}
    for line in inp:
        holding_up = []
        if '->' in line:
            line, holding_up = line.split(' -> ')
            holding_up = holding_up.split(', ')
        name, weight = line.split(' (')
        weight = int(weight[:-1])
        nodes[name] = Node(name, weight, holding_up)
    return nodes


def calc_weight(node):
    if not node.holding_up:
        return node.weight
    else:
        return node.weight + sum((calc_weight(nodes[n]) for n in node.holding_up))


inp = []
for line in fileinput.input():
    inp.append(line.strip())

nodes = process(inp)

reported = set()
for name, node in nodes.items():
    if not node.holding_up:
        continue
    sums = defaultdict(list)
    for i in node.holding_up:
        sums[node.weight + calc_weight(nodes[i])].append(i)
    if len(sums) != 1:
        print('We\'re at node:', node.name)
        reported.add(name)
        if reported.intersection(set(node.holding_up)):
            print('We\'ve reported a sub-tower')
            continue
        print('Sums for {}'.format(', '.join(node.holding_up)))
        ss = list(sorted(sums))
        diff = ss[0] - ss[-1]
        problem = sums[ss[-1]][0]
        weight = calc_weight(nodes[problem])
        print('Need {} for {} ({}) to get {}'.format(diff, problem, weight, weight + int(diff)))
        print('Changing its weight to {}'.format(nodes[problem].weight + int(diff)))
        break
