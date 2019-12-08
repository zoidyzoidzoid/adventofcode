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
    99: 0,
}

def solve(state, test_code):
    diag = 0
    pos = 0
    while True:
        command = str(state[pos])
        op_code = int(command[-2:])
        # print('cmd:', command)
        if op_code not in PARS:
            raise Exception('Unknown op_code: {}'.format(op_code))
        if diag and op_code != 99:
            raise Exception('diagnostic_code: {}'.format(diag))

        modes = ''.join(reversed(command[:-2]))

        parameters = []
        for index in range(1, PARS[op_code]):
            p = state[pos + index]
            param = int(p)
            if index - 1 >= len(modes) or modes[index - 1] == '0':
                param = state[param]
            parameters.append(param)
        parameters.append(state[pos + PARS[op_code]])

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
            state[z] = test_code
            pos += PARS[op_code] + 1
        elif op_code == 4:
            z = parameters[0]

            if 1 > len(modes) or modes[0] == '0':
                z = state[z]

            diag = z
            print('* Outputting value at {}: {}'.format(z, diag))
            pos += PARS[op_code] + 1
        elif op_code == 5:
            diag = 0

            x, y = parameters 

            if 2 > len(modes) or modes[1] == '0':
                y = state[y]

            if x != 0:
                print('* Jumping to {}, because x == {}'.format(y, x))
                pos = y
            else:
                print('* x == {} so not jumping to {}'.format(x, y))
                pos += PARS[op_code] + 1
        elif op_code == 6:
            diag = 0

            x, y = parameters 

            if 2 > len(modes) or modes[1] == '0':
                y = state[y]

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
        elif op_code == 99:
            print('**********************************')
            print('* Halting:', diag)
            print('**********************************')
            return diag
            break
        else:
            raise Exception('Unknown op_code: {}'.format(op_code))



def a(lines, inp=1):
    result = 0
    for _, line in enumerate(lines):
        state = [int(i) for i in line.split(',')]
        return solve(state, inp)

def b(lines, inp=5):
    print('input:', inp)
    result = 0
    for _, line in enumerate(lines):
        state = [int(i) for i in line.split(',')]
        return solve(state, inp)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


# assert a(lines) == 13978427
# print()

# assert b(['3,9,8,9,10,9,4,9,99,-1,8'], 7) == 0
# assert b(['3,9,8,9,10,9,4,9,99,-1,8'], 8) == 1
# assert b(['3,9,8,9,10,9,4,9,99,-1,8'], 9) == 0
# print()

# assert b(['3,9,7,9,10,9,4,9,99,-1,8'], 6) == 1
# assert b(['3,9,7,9,10,9,4,9,99,-1,8'], 7) == 1
# assert b(['3,9,7,9,10,9,4,9,99,-1,8'], 8) == 0
# assert b(['3,9,7,9,10,9,4,9,99,-1,8'], 9) == 0
# print()

# assert b(['3,3,1108,-1,8,3,4,3,99'], 7) == 0
# assert b(['3,3,1108,-1,8,3,4,3,99'], 8) == 1
# assert b(['3,3,1108,-1,8,3,4,3,99'], 9) == 0
# print()

# assert b(['3,3,1107,-1,8,3,4,3,99'], 6) == 1
# assert b(['3,3,1107,-1,8,3,4,3,99'], 7) == 1
# assert b(['3,3,1107,-1,8,3,4,3,99'], 8) == 0
# assert b(['3,3,1107,-1,8,3,4,3,99'], 9) == 0
# print()

# assert b(['3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'], 0) == 0
# assert b(['3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'], 1) == 1
# assert b(['3,3,1105,-1,9,1101,0,0,12,4,12,99,1'], 0) == 0
# assert b(['3,3,1105,-1,9,1101,0,0,12,4,12,99,1'], 1) == 1
# print()

# assert b(['3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'], 7) == 999
# assert b(['3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'], 8) == 1000
# assert b(['3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'], 9) == 1001

assert b(lines) == 11189491
