#!/usr/bin/env python
# coding: utf-8
from collections import defaultdict


def process(inp):
    regs = defaultdict(int)
    pos = 0
    lst = 0
    while pos < len(inp):
        for reg, val in regs.items():
            print(reg, val, sep=': ')
        line = inp[pos]
        line = line.split(' ')
        op, line = line[0], line[1:]

        try:
            x = int(line[0])
        except:
            x = regs[line[0]]

        if len(line) > 1:
            try:
                y = int(line[1])
            except:
                y = regs[line[1]]

        print('Processing {}: {} {} {}'.format(''.join(inp[pos]), op, line[0], y))
        if op == 'snd':
            lst = x
        elif op == 'set':
            regs[line[0]] = y
        elif op == 'add':
            regs[line[0]] += y
        elif op == 'mul':
            regs[line[0]] *= y
        elif op == 'mod':
            regs[line[0]] = x % y
        elif op == 'rcv' and x > 0:
            return lst
        elif op == 'jgz' and x > 0:
            pos += y
            continue
        pos += 1


print(process("""set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2""".split('\n')))
print(process(open('day18.txt').read().split('\n')))
