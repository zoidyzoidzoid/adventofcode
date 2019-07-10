#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def process(line):
    blocks = [int(i) for i in line.split()]
    # I originally did this with a set but moved it to a dict for part 2, and
    # that could give you both solutions
    seen = {}
    seen[tuple(blocks)] = 0
    steps = 1
    while True:
        # print('Step {}: {}'.format(steps - 1, ' '.join((str(i) for i in blocks))))
        fullest = blocks.index(max(blocks)) - len(blocks)
        bucket = blocks[fullest]
        blocks[fullest] = 0
        ideal = round(bucket / len(blocks))
        index = fullest
        while bucket:
            index += 1
            blocks[index] += min(ideal, bucket)
            bucket -= min(ideal, bucket)
        if tuple(blocks) in seen:
            print('Took {} steps to find {} again'.format(steps, ' '.join((str(i) for i in blocks))))
            print('Last seen {} steps ago'.format(steps - seen[tuple(blocks)]))
            break
        seen[tuple(blocks)] = steps
        steps += 1


lines = []
for line in fileinput.input():
    print(process(line.strip()))
