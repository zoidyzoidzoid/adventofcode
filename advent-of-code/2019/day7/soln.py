#!/usr/bin/env python3
import asyncio
import bisect
import fileinput
import heapq
import sys
from collections import Counter, defaultdict, deque
from copy import deepcopy
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt
from os import getenv


import logging 
logging.basicConfig(level=logging.DEBUG)


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


class Halt(Exception):
    pass


async def solve(state, inp, out, last):
    state = deepcopy(state)
    diag = 0
    pos = 0
    l = None
    while True:
        command = str(state[pos])
        op_code = int(command[-2:])
        # print('cmd:', command)
        if op_code not in PARS:
            raise Excektion('Unknown op_code: {}'.format(op_code))

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
            state[z] = await inp.get()
            inp.task_done()
            pos += PARS[op_code] + 1
        elif op_code == 4:
            z = parameters[0]

            if 1 > len(modes) or modes[0] == '0':
                z = state[z]

            diag = z

            print('* Outputting value at {}: {}'.format(z, diag))
            l = diag
            await out.put(diag)
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
            if last:
                return l
            else:
                return diag
        else:
            raise Exception('Unknown op_code: {}'.format(op_code))



def a(lines):
    """THIS IS BROKEN CUZ OF ASYNCIO STUFF"""


async def b(lines):
    for _, line in enumerate(lines):
        state = [int(i) for i in line.split(',')]
        mx = 0

        out = None
        mx_p = None
        mx = 0
        for phases in permutations('56789', 5):
            ans = phases
            print('Starting up the phase cannon: ', ''.join(ans))
            phases = deque(phases)
            loop = asyncio.get_event_loop()
            result = None
            first = True
            tasks = []

            queues = [
                asyncio.Queue(),
                asyncio.Queue(),
                asyncio.Queue(),
                asyncio.Queue(),
                asyncio.Queue(),
            ]

            inp = queues[0]
            out = queues[1]
            i = 0

            last = False
            while phases:
                p = phases.popleft()
                if phases:
                    inp, out = queues[i], queues[i + 1]
                else:
                    inp, out = queues[i], queues[0]
                    last = True
                i += 1

                await inp.put(int(p))

                if first:
                    await inp.put(0)
                    first = False

                task = asyncio.create_task(solve(state, inp, out, last))
                tasks.append(task)

            try:
                await asyncio.gather(*tasks)
            except Halt:
                pass

            out = tasks[-1].result()
            if max((out, mx)) == out:
                mx = out
                mx_p = ''.join(ans)
        result = (mx, mx_p)
        print(result)
        return result


lines = []
for line in fileinput.input():
    lines.append(line.strip())


# assert a(['3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0']) == (43210, '43210')
# assert a(['3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0']) == (54321, '01234')
# assert a(['3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0']) == (65210, '10432')
# 
# assert a(lines) == (18812, '23041')

assert asyncio.run(b(['3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5']), debug=True) == (139629729, '98765')
assert asyncio.run(b(['3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10']), debug=True) == (18216, '97856')
assert asyncio.run(b(lines)) == (25534964, '69875')
