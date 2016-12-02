#!/usr/bin/env python3.6
import fileinput

num_pad = (
  (0, 0, 5, 0, 0),
  (0, 'A', 6, 2, 0),
  ('D', 'B', 7, 3, 1),
  (0, 'C', 8, 4, 0),
  (0, 0, 9, 0, 0)
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
        if 4 >= new_x >= 0 and 4 >= new_y >= 0 and num_pad[new_x][new_y] != 0:
            pos = (new_x, new_y)

    print(num_pad[pos[0]][pos[1]], end='')

print()
