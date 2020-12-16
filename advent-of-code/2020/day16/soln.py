#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import sys
import math
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def a(lines):
    lines = '\n'.join(lines).split('\n\n')
    limits = lines[0].split('\n')
    your_ticket = [int(i) for i in lines[1].split('\n')[1].split(',')]
    nearby_tickets = [[int(j) for j in i.split(',')] for i in lines[2].split('\n')[1:]]
    # print(limits)
    # print(your_ticket)
    # print(nearby_tickets)
    data = defaultdict(list)
    for limit in limits:
        f, _, intervals = limit.partition(': ')
        for interval in intervals.split(' or '):
            l, _, r = interval.partition('-')
            l, r = int(l), int(r)
            data[f].append((l, r))
            # print(f, l, r)
    # for i, line in enumerate(lines):
    #     print(line)
    result = 0
    for ticket in nearby_tickets:
        for value in ticket:
            valid = False
            for _, intervals in data.items():
                for l, r in intervals:
                    if l <= value <= r:
                        valid = True
                        break
                if valid:
                    break
            if not valid:
                result += value
    print(result)


def b(lines):
    lines = '\n'.join(lines).split('\n\n')
    limits = lines[0].split('\n')
    your_ticket = [int(i) for i in lines[1].split('\n')[1].split(',')]
    nearby_tickets = [tuple(int(j) for j in i.split(',')) for i in lines[2].split('\n')[1:]]
    # print(limits)
    # print(your_ticket)
    # print(nearby_tickets)
    data = defaultdict(list)
    for limit in limits:
        f, _, intervals = limit.partition(': ')
        for interval in intervals.split(' or '):
            l, _, r = interval.partition('-')
            l, r = int(l), int(r)
            data[f].append((l, r))
            # print(f, l, r)
    # for i, line in enumerate(lines):
    #     print(line)
    guesses = defaultdict(set)
    for ticket in nearby_tickets:
        for pos, value in enumerate(ticket):
            valid = False
            possible = set()
            for f, intervals in data.items():
                for l, r in intervals:
                    if l <= value <= r:
                        valid = True
                        possible.add(f)
                        break
            if valid:
                if len(guesses[pos]) == 0:
                    guesses[pos] = possible
                else:
                    guesses[pos].intersection_update(possible)
    while any(len(v) > 1 for v in guesses.values()):
        for k, v in guesses.items():
            if len(v) == 1:
                for l, w in guesses.items():
                    if l != k:
                        try:
                            guesses[l].difference_update(v)
                        except KeyError:
                            pass
    # print(guesses)
    # print(your_ticket)
    # print(nearby_tickets)
    result = 1
    for pos, guess in guesses.items():
        if all((i.startswith('departure') for i in guess)):
            result *= your_ticket[pos]
    print(result)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
