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
    return
    result = ''
    steps = defaultdict(str)
    lines = deque(lines)
    while lines:
        line = lines.popleft()
        line = line.split(' ')
        steps[line[7]] += line[1]
        if line[1] not in steps:
            steps[line[1]] = ''
    print(steps)
    while steps:
        for step in sorted(steps.keys()):
            print(steps)
            reqs = steps[step]
            if not reqs:
                for k in steps:
                    steps[k] = steps[k].replace(step, '')
                del steps[step]
                result += step
                break

    print(result)


def b(lines):
    steps = defaultdict(str)
    lines = deque(lines)
    while lines:
        line = lines.popleft()
        line = line.split(' ')
        steps[line[7]] += line[1]
        if line[1] not in steps:
            steps[line[1]] = ''
    workers = 5
    t = 60
    work = defaultdict(int)
    result = 0
    while steps:
        # print(steps)
        for step in sorted(steps.keys()):
            reqs = steps[step]
            if not reqs:
                if step in ((v[0]) for v in work.values() if v):
                    continue
                for w_id in range(1, workers + 1):
                    if not work[w_id]:
                        work[w_id] = (step, t + (ord(step) - ord('A') + 1))
                        break
                    else:
                        print('Couldn\'t assign')
        print(dict(work))
        if any((v for v in work.values())):
            mv = min((v[1] for v in work.values() if v))
            result += mv
            for k in list(work.keys()):
                v = work[k]
                if not v:
                    continue
                if v[1] - mv != 0:
                    work[k] = v[0], v[1] - mv
                else:
                    work[k] = None
                    for l in steps:
                        steps[l] = steps[l].replace(v[0], '')
                    del steps[v[0]]
        # ready = False
        # while not ready:
        #     stepped = False
        #     for k, v in list(work.items()):
        #         if v:
        #             s, w = v
        #             work[k] = s, w - 1
        #             stepped = True
        #             if w - 1 == 0:
        #                 work[k] = None
        #                 for k in steps:
        #                     steps[k] = steps[k].replace(s, '')
        #                 del steps[s]
        #         else:
        #             ready = True
        #             continue
        #     if stepped:
        #         result += 1

    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
