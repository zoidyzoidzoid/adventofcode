#!/usr/bin/env python3
# coding: utf-8
import fileinput
from collections import defaultdict


def process(inp):
    registers = defaultdict(int)
    for line in inp:
        commands = line.split(' ')
        # print(commands)
        cond = commands[4:]
        x, op, y = cond
        x = registers[x]
        y = int(y)
        if op == '>':
            result = x > y
        elif op == '<':
            result = x < y
        elif op == '>=':
            result = x >= y
        elif op == '<=':
            result = x <= y
        elif op == '==':
            result = x == y
        elif op == '!=':
            result = x != y
        else:
            raise NotImplementedError(op)
        if result:
            reg, op, i = commands[:3]
            i = int(i)
            if op == 'inc':
                registers[reg] += i
            else:
                registers[reg] -= i
    return max(registers.values())


lines = []
for line in fileinput.input():
    lines.append(line.strip())

print(process(lines))
