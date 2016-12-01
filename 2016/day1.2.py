#!/usr/bin/env python3
import fileinput
from sys import exit

steps = fileinput.input().readline().strip().split(', ')

print('{} steps found'.format(len(steps)))

dir_x, dir_y = (0, 1)
pos_x, pos_y = (0, 0)
locs = set((pos_x, pos_y),)

print('Current position:', pos_x, pos_y)

for step in steps:
    print('Found step:', step)
    rot, n = step[0], int(step[1:])

    if rot == 'L':
        dir_x, dir_y = -dir_y, dir_x
    else:
        dir_x, dir_y = dir_y, -dir_x

    for i in range(n):
        pos_x, pos_y = pos_x + dir_x, pos_y + dir_y

        if (pos_x, pos_y) in locs:
            print("We've been here before", pos_x, pos_y)
            print('Distance:', abs(pos_x) + abs(pos_y))
            exit(0)
        locs.add((pos_x, pos_y))

    print('New position:', pos_x, pos_y)

print('Final position:', pos_x, pos_y)
print('Distance:', abs(pos_x) + abs(pos_y))
