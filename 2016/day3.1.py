#!/usr/bin/env python3.6
import fileinput
from itertools import permutations

impossible = 0
total = 0

for line in fileinput.input():
    total +=1

    line = line.strip().split()
    line = [int(c) for c in line]

    for i in range(len(line)):
        tmp = line.copy()
        tmp.pop(i)
        print(f'testing {tmp} vs {line[i]}')
        if sum(tmp) <= line[i]:
            impossible += 1
            break


print(f'{impossible} impossible triangles found.')
print(f'{total - impossible} possible triangles found.')
