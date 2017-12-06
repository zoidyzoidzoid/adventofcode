#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def process(line):
    configs = set()
    blocks = [0, 2, 7, 0]
    configs.add(tuple(blocks))
    steps = 1
    found = None
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
        if tuple(blocks) in configs:
            if tuple(blocks) == found:
                print('Took {} steps to find {} again'.format(steps, ' '.join((str(i) for i in blocks))))
                break
            elif found is None:
                print('Looking for {} again'.format(' '.join((str(i) for i in blocks))))
                found = tuple(blocks)
                steps = 0
        steps += 1
        configs.add(tuple(blocks))


lines = []
for line in fileinput.input():
    process(line.strip())
