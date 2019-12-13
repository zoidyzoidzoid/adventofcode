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
    def left(x, y):
        return y, -x

    def right(x, y):
        return -y, x

    grid = {}
    result = 0
    state = {
        i: v
        for i, v in enumerate(state)
    }
    state = Memory(int, state)
    state[0] = 2
    joystick = 0
    score = None
    b_x, b_y, p_x, p_y = None, None, None, None
    o_b_x, o_b_y = None, None

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
        rows = [
                'Score: {}'.format(score)
        ]
        for _y in range(mn_y, mx_y + 1):
            row = ''
            for _x in range(mn_x, mx_x + 2):
                c = str(grid.get((_x, _y), '0'))
                if c == '0':
                    row += ' '
                elif c == '1':
                    row += 'X'
                elif c == '2':
                    row += '#'
                elif c == '3':
                    row += '-'
                elif c == '4':
                    row += 'o'
            rows.append(row)
        import subprocess
        subprocess.call('clear', shell=True)
        print('\n'.join(rows))

    test_code = [test_code] or [1]

    diag = 0
    pos = 0
    r_b = 0
    outs = []
    while True:
        command = str(state[pos])
        op_code = int(command[-2:])
        # p_s()

        blah = []
        for i in range(pos, pos + PARS[op_code] + 1):
            blah.append(str(state[i]))
        # print('  cmd: {} ({})'.format(','.join(blah), r_b))

        if op_code not in PARS:
            raise Exception('Unknown op_code: {}'.format(op_code))

        modes = defaultdict(int)
        for i, mode in enumerate(''.join(reversed(command[:-2]))):
            modes[i] = int(mode)

        parameters = []
        for index in range(1, PARS[op_code]):
            p = state[pos + index]
            param = None
            if modes[index - 1] == 0:
                param = state[int(p)]
            elif modes[index - 1] == 1:
                param = p
            elif modes[index - 1] == 2:
                param = state[r_b + int(p)]
            parameters.append(param)
            # print('{}: Fetching param {} ({}): {}'.format(command, index, modes[index - 1], param))

        # Adding final arg
        index = PARS[op_code]
        p = state[pos + index]
        param = None
        if index and PS[op_code][index - 1] == 'r':
            if modes[index - 1] == 0:
                param = state[int(p)]
            elif modes[index - 1] == 1:
                param = p
            elif modes[index - 1] == 2:
                param = state[r_b + int(p)]
        elif index and modes[index - 1] == 2:
            param = r_b + int(p)
        else:
            param = p
        parameters.append(param)
        # print('{}: Fetching param {} ({}): {}'.format(command, index, modes[index - 1], param))
        # print(parameters)

        if op_code == 1:
            diag = 0
            x, y, z = parameters
            # print('* Adding {} and {} storing it at {}'.format(x, y, z))
            state[z] = x + y
            pos += PARS[op_code] + 1
        elif op_code == 2:
            diag = 0
            x, y, z = parameters
            # print('* Multiplying {} and {} storing it at {}'.format(x, y, z))
            state[z] = x * y
            pos += PARS[op_code] + 1
        elif op_code == 3:
            diag = 0
            z = parameters[0]
            # print('* Requesting input to store at {}'.format(z))
            joystick = 0
            if b_y < o_b_y:
                if b_x < p_x:
                    # print('[Tilting left]')
                    joystick = -1
                elif b_x > p_x:
                    # print('[Tilting right]')
                    joystick = 1
                # else:
                #     print('[Staying neutral]')
            else:
                m = (b_y - o_b_y) / (b_x - o_b_x)
                # print('m:', m)
                c = b_y - (m * b_x)
                next_b_x =  round((p_y - 1 - c) / m)
                if next_b_x > p_x:
                    # print('[Tilting right]')
                    joystick = 1
                elif next_b_x < p_x:
                    # print('[Tilting left]')
                    joystick = -1
                # else:
                #     print('[Staying neutral]')
            state[z] = joystick
            pos += PARS[op_code] + 1
        elif op_code == 4:
            z = parameters[0]

            diag = z

            # print('* Outputting value at {}: {}'.format(state[pos + 1], diag))
            outs.append(diag)

            if len(outs) % 3 == 0:
                i1, i2, i3 = outs[-3], outs[-2], outs[-1]
                if i1 == -1 and i2 == 0:
                    score = i3
                    # print('Updating score to {}'.format(score))
                else:
                    grid[i1, i2] = i3
                if i3 == 3:
                    p_x, p_y = i1, i2
                if i3 == 4:
                    o_b_x, o_b_y = b_x, b_y
                    if o_b_x is None:
                        o_b_x, o_b_y = i1 - 1, i2 + 1
                    b_x, b_y = i1, i2
                if i3 in (3, 4):
                    p_g()

            pos += PARS[op_code] + 1
        elif op_code == 5:
            diag = 0

            x, y = parameters 

            if x != 0:
                # print('* Jumping to {}, because x == {}'.format(y, x))
                pos = y
            else:
                # print('* x == {} so not jumping to {}'.format(x, y))
                pos += PARS[op_code] + 1
        elif op_code == 6:
            diag = 0

            x, y = parameters 

            if x == 0:
                # print('* Jumping to {}, because x != {}'.format(y, x))
                pos = y
            else:
                # print('* x != {} so not jumping to {}'.format(x, y))
                pos += PARS[op_code] + 1
        elif op_code == 7:
            diag = 0

            x, y, z = parameters 

            if x < y:
                # print('* x < y, {} , {}, so setting z, {}, to 1'.format(x, y, z))
                state[z] = 1
            else:
                # print('* x >= y, {} >= {}, so setting z, {}, to 0'.format(x, y, z))
                state[z] = 0
            pos += PARS[op_code] + 1
        elif op_code == 8:
            diag = 0

            x, y, z = parameters 

            if x == y:
                # print('* x == y, {} == {}, so setting z, {}, to 1'.format(x, y, z))
                state[z] = 1
            else:
                # print('* x != y, {} != {}, so setting z, {}, to 0'.format(x, y, z))
                state[z] = 0

            pos += PARS[op_code] + 1
        elif op_code == 9:
            diag = 0

            z = parameters[0]

            # print('* Relative base changing by z, {}, from {} to {}'.format(z, r_b, r_b + z))
            r_b += z
            pos += PARS[op_code] + 1
        elif op_code == 99:
            result = list(grid.values()).count(2)
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

