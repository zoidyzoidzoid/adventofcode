#!/usr/bin/env python3.6
import fileinput
from copy import deepcopy


total_rows = []
rows = [
    [],
    [],
    []
]

for line in fileinput.input():
    line = [int(c) for c in line.strip().split()]

    for i, c in enumerate(line):
        rows[i].append(c)

    if len(rows[0]) == 3:
        total_rows.extend(rows)
        rows = [[] for i in range(3)]

impossible = 0
total = 0

for line in total_rows:
    total += 1

    for i in range(len(line)):
        tmp = line.copy()
        tmp.pop(i)
        print(f'testing {tmp} vs {line[i]}')
        if sum(tmp) <= line[i]:
            impossible += 1
            break

print(f'{impossible} impossible triangles found.')
print(f'{total - impossible} possible triangles found.')
