#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def a(lines):
    outputs = dict()
    bots = defaultdict(list)
    result = 0
    for i, line in enumerate(lines):
        line = line.split()
        if line[0] == 'value':
            lines[i] = ' '.join(line[-2:] + ['gets'] + line[:-4])
        else:
            lines[i] = ' '.join(line)

    lines = deque(sorted(lines, key=lambda x: int(x.split()[1])))
    while lines:
        line = lines.popleft()
        # print(line)
        line = line.split()
        if line[2] == 'gets':
            if line[0] != 'bot':
                raise RuntimeError('rip: {}'.format(' '.join(line)))
            bots[int(line[1])].append(int(line[-1]))
            if len(bots[int(line[1])]) == 2:
                low, high = tuple(sorted(bots[int(line[1])]))
                if (low, high) == (2, 5):
                    print('Bot {} compared 2 and 5'.format(line[1]))
                if (low, high) == (17, 61):
                    print('Bot {} compared 17 and 61'.format(line[1]))
        else:
            try:
                low, high = tuple(sorted(bots[int(line[1])]))
            except ValueError:
                lines.append(' '.join(line))
                continue
            del bots[int(line[1])]
            if (low, high) == (2, 5):
                print('Bot {} compared 2 and 5'.format(line[1]))
            if (low, high) == (17, 61):
                print('Bot {} compared 17 and 61'.format(line[1]))
            if line[5] == 'output':
                outputs[int(line[6])] = low
            else:
                bots[int(line[6])].append(low)
            if line[10] == 'output':
                outputs[int(line[11])] = high
            else:
                bots[int(line[11])].append(high)
    return bots, outputs
    # print('Bots:\n', bots, sep='')
    # print('Output bins:\n', outputs, sep='')



def b(lines):
    bots, output = a(lines)
    print(output[0] * output[1] * output[2])


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
