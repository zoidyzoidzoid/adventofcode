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


def b(lines):
    goal = 50000000000
    # goal = 20

    state = dict(enumerate(lines[0].split(': ')[-1]))

    transitions = {}
    for line in lines[2:]:
        cond, new = line.split(' => ')
        transitions[cond] = new

    seen = {}
    attempts = 0

    for gen in range(goal):
        l = min(state) - 10
        r = max(state) + 10

        new_state = state.copy()
        for j in range(l, r):
            s = ''
            for k in range(j-2, j+3):
                s += state.get(k, '.')
            v = transitions.get(s)

            if v is not None:
                new_state[j] = v

        s = ''
        for j in range(l, r):
            s += new_state.get(j, '.')
        s = s.strip('.')
        s = '....' + s + '....'
        if s in seen:
            prev_gen, sm = seen[s]
            diff = sum((k for k, v in new_state.items() if v == '#')) - sm
            print(gen, prev_gen, sm, diff)
            print(((goal - gen) * diff) + sm)
            break
        else:
            seen[s] = gen, sum((k for k, v in new_state.items() if v == '#'))

        state = new_state


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
