#!/usr/bin/env python
# coding: utf-8
from collections import defaultdict, deque


def process(inp):
    regs = {
        0: defaultdict(int, p=0),
        1: defaultdict(int, p=1),
    }
    buffers = {
        0: deque(),
        1: deque()
    }
    poss = {
        0: 0,
        1: 0
    }
    p = 0
    count = 0
    while poss[p] < len(inp) or poss[p ^ 1] < len(inp):
        if poss[p] >= len(inp):
            p ^= 1
            continue
        line = inp[poss[p]]
        line = line.split(' ')
        op, line = line[0], line[1:]

        try:
            x = int(line[0])
        except:
            x = regs[p][line[0]]

        if len(line) > 1:
            try:
                y = int(line[1])
            except:
                y = regs[p][line[1]]

        if op == 'snd':
            if p == 1:
                count += 1
            buffers[p ^ 1].append(x)
        elif op == 'set':
            regs[p][line[0]] = y
        elif op == 'add':
            regs[p][line[0]] += y
        elif op == 'mul':
            regs[p][line[0]] *= y
        elif op == 'mod':
            regs[p][line[0]] = x % y
        elif op == 'rcv':
            if not buffers[p]:
                p ^= 1
                if not buffers[p]:
                    return count
                continue
            regs[p][line[0]] = buffers[p].popleft()
        elif op == 'jgz' and x > 0:
            poss[p] += y
            continue
        poss[p] += 1


print(process(open('day18.txt').read().split('\n')))
