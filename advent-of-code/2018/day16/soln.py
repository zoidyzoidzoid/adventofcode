#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt

def addr(reg_a, val_a, reg_b, val_b):
    # addr (add register) stores into register C the result of adding register A and register B.
    return reg_a + reg_b


def addi(reg_a, val_a, reg_b, val_b):
    # addi (add immediate) stores into register C the result of adding register A and value B.
    return reg_a + val_b


def mulr(reg_a, val_a, reg_b, val_b):
    # mulr (multiply register) stores into register C the result of multiplying register A and register B.
    return reg_a * reg_b


def muli(reg_a, val_a, reg_b, val_b):
    # muli (multiply immediate) stores into register C the result of multiplying register A and value B.
    return reg_a * val_b


def banr(reg_a, val_a, reg_b, val_b):
    # banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
    return reg_a & reg_b


def bani(reg_a, val_a, reg_b, val_b):
    # bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
    return reg_a & val_b


def borr(reg_a, val_a, reg_b, val_b):
    # borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
    return reg_a | reg_b


def bori(reg_a, val_a, reg_b, val_b):
    # bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
    return reg_a | val_b


def setr(reg_a, val_a, reg_b, val_b):
    # setr (set register) copies the contents of register A into register C. (Input B is ignored.)
    return reg_a


def seti(reg_a, val_a, reg_b, val_b):
    # seti (set immediate) stores value A into register C. (Input B is ignored.)
    return val_a


def gtir(reg_a, val_a, reg_b, val_b):
    # gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
    return int(val_a > reg_b)


def gtri(reg_a, val_a, reg_b, val_b):
    # gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
    return int(reg_a > val_b)


def gtrr(reg_a, val_a, reg_b, val_b):
    # gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
    return int(reg_a > reg_b)

def eqir(reg_a, val_a, reg_b, val_b):
    # eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
    return int(val_a == reg_b)


def eqri(reg_a, val_a, reg_b, val_b):
    # eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
    return int(reg_a == val_b)


def eqrr(reg_a, val_a, reg_b, val_b):
    # eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
    return int(reg_a == reg_b)


OPERATIONS = {
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr,
}


def a(lines):
    return
    result = 0
    lines = deque(lines)
    i = 0
    def all_ops():
        return set(OPERATIONS.keys())
    ops_by_code = defaultdict(all_ops)
    ops_by_code_examples = defaultdict(list)
    while lines:
        line = lines.popleft()
        if line.startswith('Before: '):
            before = line
            regs = lines.popleft()
            after = lines.popleft()
            _ = lines.popleft()
            before = before.lstrip('Before:  [').rstrip(']').replace(', ', ' ')
            after = after.lstrip('After:  [').rstrip(']').replace(', ', ' ')
            before_regs = {
                    x: int(i) for x, i in enumerate(before.split(' '))
            }
            op = [
                    int(i) for i in regs.split(' ')
            ]
            after_regs = {
                    x: int(i) for x, i in enumerate(after.split(' '))
            }
            print(before_regs)
            op_code, a, b, c = op
            print(op_code, a, b, c)
            print(after_regs)
            valid_ops = set()
            for op_name, op_func in OPERATIONS.items():
                if after_regs[c] == op_func(before_regs[a], a, before_regs[b], b):
                    valid_ops.add(op_name)
            if len(valid_ops) >= 3:
                result += 1
    print(result)


def b(lines):
    lines = deque(lines)
    i = 0
    def all_ops():
        return set(OPERATIONS.keys())
    ops_by_code = defaultdict(all_ops)
    ops_by_code_examples = defaultdict(list)
    test_program = deque()
    while lines:
        line = lines.popleft()
        if line.startswith('Before: '):
            before = line
            regs = lines.popleft()
            after = lines.popleft()
            _ = lines.popleft()
            before = before.lstrip('Before:  [').rstrip(']').replace(', ', ' ')
            after = after.lstrip('After:  [').rstrip(']').replace(', ', ' ')
            before_regs = {
                    x: int(i) for x, i in enumerate(before.split(' '))
            }
            op = [
                    int(i) for i in regs.split(' ')
            ]
            after_regs = {
                    x: int(i) for x, i in enumerate(after.split(' '))
            }
            print(before_regs)
            op_code, a, b, c = op
            print(op_code, a, b, c)
            print(after_regs)
            valid_ops = set()
            for op_name, op_func in OPERATIONS.items():
                if after_regs[c] == op_func(before_regs[a], a, before_regs[b], b):
                    valid_ops.add(op_name)
                    ops_by_code_examples[op_code].append(
                        {
                            'before': before_regs,
                            'operation': (op_code, a, b, c),
                            'after': after_regs,
                        }
                    )
            ops_by_code[op_code] = ops_by_code[op_code].intersection(valid_ops)
        else:
            if not line:
                continue
            line = [
                    int(i) for i in line.split(' ')
            ]
            test_program.append(line)

    ocs = {}

    while any((len(x) > 1) for x in ops_by_code.values()):
        for ops_code, ops_funcs in ops_by_code.items():
            if len(ops_funcs) == 1:
                ops_func = ops_funcs.copy().pop()
                ocs[ops_code] = ops_func
                for ops_code2 in ops_by_code:
                    if ops_code2 != ops_code and ops_func in ops_by_code[ops_code2]:
                        ops_by_code[ops_code2].remove(ops_func)

    print(dict(ops_by_code))
    print(ocs)
    regs = [0, 0, 0, 0]
    for op_code, a, b, c in test_program:
        regs[c] = OPERATIONS[ocs[op_code]](regs[a], a, regs[b], b)
    print(regs)


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
