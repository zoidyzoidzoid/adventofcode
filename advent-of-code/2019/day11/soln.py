#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import sys
from os import getenv
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


PARS = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 1,
    99: 0,
}

PS = {
    1: 'rrw',
    2: 'rrw',
    3: 'w',
    4: 'r',
    5: 'rr',
    6: 'rr',
    7: 'rrw',
    8: 'rrw',
    9: 'r',
    99: '',
}

class Memory(defaultdict):
    def __setitem__(self, k, v):
        if k < 0:
            raise KeyError('Invalid memory address')
        return super().__setitem__(k, v)


def solve(state, test_code=None):
    def left(p1, p2):
        return p2, -p1

    def right(p1, p2):
        return -p2, p1

    grid = {}
    grid[0,0] = 'W'
    # output[0]
    # 0 == black
    # 1 == white
    # output[1]
    # 0 == left
    # 1 == right
    seen = set()
    p_x, p_y = 0, 0
    d_x, d_y = 0, -1
    dirs_l = {
        (-1, 0): '<',
        (+1, 0): '>',
        (0, -1): '^',
        (0, +1): 'v',
    }
    state = {
        i: v
        for i, v in enumerate(state)
    }
    state = Memory(int, state)

    def p_s():
        mn = min(state.keys())
        mx = max(state.keys())
        for i in range(mn, mx):
            print(state[i], end=' ')
        print()

    def p_g():
        mn_x = min(i[0] for i in grid.keys())
        mx_x = max(i[0] for i in grid.keys())
        mn_y = min(i[1] for i in grid.keys())
        mx_y = max(i[1] for i in grid.keys())
        for _y in range(mn_y - 1, mx_y + 2):
            row = ''
            for _x in range(mn_x - 1, mx_x + 2):
                if _x == p_x and _y == p_y:
                    row += dirs_l[d_x, d_y]
                    continue
                if grid.get((_x, _y), 'B') == 'B':
                    row += '#'
                else:
                    row += ' '
            print(row)

    test_code = [test_code] or [1]

    diag = 0
    position = 0
    relative_base = 0
    outs = []
    while True:
        command = str(state[position])
        op_code = int(command[-2:])
        # p_s()

        blah = []
        for i in range(position, position + PARS[op_code] + 1):
            blah.append(str(state[i]))
        print('  cmd: {} ({})'.format(','.join(blah), relative_base))

        if op_code not in PARS:
            raise Exception('Unknown op_code: {}'.format(op_code))

        modes = defaultdict(int)
        for i, mode in enumerate(''.join(reversed(command[:-2]))):
            modes[i] = int(mode)

        parameters = []
        for index in range(1, PARS[op_code]):
            p = state[position + index]
            param = None
            if modes[index - 1] == 0:
                param = state[int(p)]
            elif modes[index - 1] == 1:
                param = p
            elif modes[index - 1] == 2:
                param = state[relative_base + int(p)]
            parameters.append(param)
            # print('{}: Fetching param {} ({}): {}'.format(command, index, modes[index - 1], param))

        # Adding final arg
        index = PARS[op_code]
        p = state[position + index]
        param = None
        if index and PS[op_code][index - 1] == 'r':
            if modes[index - 1] == 0:
                param = state[int(p)]
            elif modes[index - 1] == 1:
                param = p
            elif modes[index - 1] == 2:
                param = state[relative_base + int(p)]
        elif index and modes[index - 1] == 2:
            param = relative_base + int(p)
        else:
            param = p
        parameters.append(param)
        # print('{}: Fetching param {} ({}): {}'.format(command, index, modes[index - 1], param))
        # print(parameters)

        if op_code == 1:
            diag = 0
            p1, p2, p3 = parameters
            print('* Adding {} and {} storing it at {}'.format(p1, p2, p3))
            state[p3] = p1 + p2
            position += PARS[op_code] + 1
        elif op_code == 2:
            diag = 0
            p1, p2, p3 = parameters
            print('* Multiplying {} and {} storing it at {}'.format(p1, p2, p3))
            state[p3] = p1 * p2
            position += PARS[op_code] + 1
        elif op_code == 3:
            diag = 0
            p3 = parameters[0]
            print('* Requesting input to store at {}'.format(p3))
            if grid.get((p_x, p_y), 'B') == 'B':
                state[p3] = 0
            else:
                state[p3] = 1
            position += PARS[op_code] + 1
        elif op_code == 4:
            p3 = parameters[0]

            diag = p3

            print('* Outputting value at {}: {}'.format(state[position + 1], diag))
            outs.append(diag)

            if len(outs) % 2 == 0:
                i1, i2 = outs[-2], outs[-1]
                print('New instructions: {}, {}'.format(i1, i2))
                if i1 == 0:
                    print('[Painting black]')
                    grid[p_x, p_y] = 'B'
                else:
                    print('[Painting white]')
                    grid[p_x, p_y] = 'W'
                if i2 == 0:
                    print('[Turning left]')
                    d_x, d_y = left(d_x, d_y)
                else:
                    print('[Turning right]')
                    d_x, d_y = right(d_x, d_y)
                print('[Moving from {},{} to {},{}]'.format(p_x, p_y, p_x + d_x, p_y + d_y))
                seen.add((p_x, p_y))
                p_x, p_y = p_x + d_x, p_y + d_y
                # p_g()

            position += PARS[op_code] + 1
        elif op_code == 5:
            diag = 0

            p1, p2 = parameters 

            if p1 != 0:
                print('* Jumping to {}, because x == {}'.format(p2, p1))
                position = p2
            else:
                print('* x == {} so not jumping to {}'.format(p1, p2))
                position += PARS[op_code] + 1
        elif op_code == 6:
            diag = 0

            p1, p2 = parameters 

            if p1 == 0:
                print('* Jumping to {}, because x != {}'.format(p2, p1))
                position = p2
            else:
                print('* x != {} so not jumping to {}'.format(p1, p2))
                position += PARS[op_code] + 1
        elif op_code == 7:
            diag = 0

            p1, p2, p3 = parameters 

            if p1 < p2:
                print('* x < y, {} , {}, so setting z, {}, to 1'.format(p1, p2, p3))
                state[p3] = 1
            else:
                print('* x >= y, {} >= {}, so setting z, {}, to 0'.format(p1, p2, p3))
                state[p3] = 0
            position += PARS[op_code] + 1
        elif op_code == 8:
            diag = 0

            p1, p2, p3 = parameters 

            if p1 == p2:
                print('* x == y, {} == {}, so setting z, {}, to 1'.format(p1, p2, p3))
                state[p3] = 1
            else:
                print('* x != y, {} != {}, so setting z, {}, to 0'.format(p1, p2, p3))
                state[p3] = 0

            position += PARS[op_code] + 1
        elif op_code == 9:
            diag = 0

            p3 = parameters[0]

            print('* Relative base changing by z, {}, from {} to {}'.format(p3, relative_base, relative_base + p3))
            relative_base += p3
            position += PARS[op_code] + 1
        elif op_code == 99:
            p_g()
            result = len(seen)
            print('**********************************')
            print('* Halting:', result)
            print('**********************************')
            return result
        else:
            raise Exception('Unknown op_code: {}'.format(op_code))



def a(lines, inp=1):


    for _, line in enumerate(lines):
        state = [int(i) for i in line.split(',')]
        return solve(state, inp)

def b(lines, inp=2):
    for _, line in enumerate(lines):
        state = [int(i) for i in line.split(',')]
        return solve(state, inp)


lines = []
for line in fileinput.input():
    lines.append(line.strip())

a(lines)
# b(lines)

