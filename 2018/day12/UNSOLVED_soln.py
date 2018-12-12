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
    result = 0
    state = dict(enumerate(lines[0].split(': ')[-1]))
    transitions = []
    for line in lines[2:]:
        cond, new = line.split(' => ')
        cond = list(cond)
        transitions.append((cond, new))

    for i in range(1, 5):
        state[-i] = '.'
        state[-i] = '.'
        state[-i] = '.'
    mx = max(state)
    for i in range(mx + 1, mx + 51):
        state[i] = '.'

    from pprint import pprint
    pprint(transitions)
    s = ''
    for k in sorted(state):
        s += state[k]
    print('{:2d}: {}'.format(0, s))
    for i in range(20):
        new_state = state.copy()
        for j in sorted(state):
            s = []
            for k in range(j-2, j+3):
                try:
                    s.append(state[k])
                except KeyError:
                    s.append('.')
            for cond, new in transitions:
                if s == cond:
                    # print('pot {} matched the rule looking for {}'.format(j, ''.join(cond)))
                    new_state[j] = new
                    break
            else:
                new_state[j] = '.'
        state = new_state
        s = ''
        for k in sorted(state):
            s += state[k]
        print('{:2d}: {}'.format(i + 1, s))
    s = ''
    for k in sorted(state):
        s += state[k]
    print(s)
    print(sum((k for k, v in state.items() if v == '#')))


def print_gen(gen, state, l, r):
    s = ''
    for j in range(l, r):
        s += state.get(j, '.')
    s = s.strip('.')
    return s
    print('{:2d}: {}'.format(gen + 1, s))


def b(lines):
    goal = 50000000000
    # goal = 20
    result = 0
    state = dict(enumerate(lines[0].split(': ')[-1]))
    global transitions
    transitions = {}
    for line in lines[2:]:
        cond, new = line.split(' => ')
        transitions[cond] = new

    from pprint import pprint
    pprint(transitions)
    seen = set()
    attempts = 0
    for i in range(goal):
        l = min(state) - 10
        r = max(state) + 10

        new_state = state.copy()
        for j in range(l, r):
            s = ''
            for k in range(j-2, j+3):
                s += state.get(k, '.')
            v = transitions.get(s, '.')

            new_state[j] = v

        s = print_gen(i, state, l, r)

        if s in seen:
            if attempts == 0:
                result = i, sum((k for k, v in state.items() if v == '#'))
            attempts += 1
            if attempts > 10:
                break
        else:
            attempts = 0
            seen.add(s)
        state = new_state
    else:
        result = goal, sum((k for k, v in state.items() if v == '#'))
    l = min(state)
    r = max(state)
    print(l, r)
    s = ''
    for j in range(l, r):
        s += state.get(j, '.')
    print(s.strip('.'))
    print(*result)



lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
