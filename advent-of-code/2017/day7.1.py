#!/usr/bin/env python3
import fileinput


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

inp = []
for line in fileinput.input():
    inp.append(line.strip())

nodes = process(inp)

held_up = set(nodes)
for name, node in nodes.items():
    for i in node.holding_up:
        held_up.remove(i)

print(held_up)
