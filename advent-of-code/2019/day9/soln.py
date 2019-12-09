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
        print('  cmd: {} ({})'.format(','.join(blah), r_b))

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
            print('* Adding {} and {} storing it at {}'.format(x, y, z))
            state[z] = x + y
            pos += PARS[op_code] + 1
        elif op_code == 2:
            diag = 0
            x, y, z = parameters
            print('* Multiplying {} and {} storing it at {}'.format(x, y, z))
            state[z] = x * y
            pos += PARS[op_code] + 1
        elif op_code == 3:
            diag = 0
            z = parameters[0]
            print('* Requesting input to store at {}'.format(z))
            state[z] = test_code.pop()
            pos += PARS[op_code] + 1
        elif op_code == 4:
            z = parameters[0]

            diag = z

            print('* Outputting value at {}: {}'.format(state[pos + 1], diag))
            outs.append(diag)
            pos += PARS[op_code] + 1
        elif op_code == 5:
            diag = 0

            x, y = parameters 

            if x != 0:
                print('* Jumping to {}, because x == {}'.format(y, x))
                pos = y
            else:
                print('* x == {} so not jumping to {}'.format(x, y))
                pos += PARS[op_code] + 1
        elif op_code == 6:
            diag = 0

            x, y = parameters 

            if x == 0:
                print('* Jumping to {}, because x != {}'.format(y, x))
                pos = y
            else:
                print('* x != {} so not jumping to {}'.format(x, y))
                pos += PARS[op_code] + 1
        elif op_code == 7:
            diag = 0

            x, y, z = parameters 

            if x < y:
                print('* x < y, {} , {}, so setting z, {}, to 1'.format(x, y, z))
                state[z] = 1
            else:
                print('* x >= y, {} >= {}, so setting z, {}, to 0'.format(x, y, z))
                state[z] = 0
            pos += PARS[op_code] + 1
        elif op_code == 8:
            diag = 0

            x, y, z = parameters 

            if x == y:
                print('* x == y, {} == {}, so setting z, {}, to 1'.format(x, y, z))
                state[z] = 1
            else:
                print('* x != y, {} != {}, so setting z, {}, to 0'.format(x, y, z))
                state[z] = 0

            pos += PARS[op_code] + 1
        elif op_code == 9:
            diag = 0

            z = parameters[0]

            print('* Relative base changing by z, {}, from {} to {}'.format(z, r_b, r_b + z))
            r_b += z
            pos += PARS[op_code] + 1
        elif op_code == 99:
            result = ','.join(str(out) for out in outs)
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

print()
print(' *** ANOTHER TEST *** ')
print()
assert a(['104,1125899906842624,99']) == '1125899906842624'
print()
print(' *** ANOTHER TEST *** ')
print()
assert a(['1102,34915192,34915192,7,4,7,99,0']) == '1219070632396864'
print()
print(' *** ANOTHER TEST *** ')
print()
assert a(['109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99']) == '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
a(lines)
b(lines)

