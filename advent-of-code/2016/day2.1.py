#!/usr/bin/env python3.6
import fileinput

num_pad = (
  (7, 4, 1),
  (8, 5, 2),
  (9, 6, 3),
)

direction = {
  'R': (1, 0),
  'L': (-1, 0),
  'U': (0, 1),
  'D': (0, -1)
}

pos = (1, 1)

for line in fileinput.input():
    line = line.strip()

    for step in line:
        dir_x, dir_y = direction[step]
        new_x = pos[0] + dir_x
        new_y = pos[1] + dir_y
        if 2 >= new_x >= 0 and 2 >= new_y >= 0:
            pos = (new_x, new_y)

    print(num_pad[pos[0]][pos[1]], end='')

print()
