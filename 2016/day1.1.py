#!/usr/bin/env python3.6
import fileinput

steps = fileinput.input().readline().strip().split(', ')

print(f'{len(steps)} steps found')

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

    pos_x, pos_y = pos_x + (dir_x * n), pos_y + (dir_y * n)

    print('New position:', pos_x, pos_y)

print('Final position:', pos_x, pos_y)
print('Distance:', abs(pos_x) + abs(pos_y))
