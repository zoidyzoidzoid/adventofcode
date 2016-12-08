#!/usr/bin/env python3.6
import fileinput
from copy import deepcopy
from collections import *
from functools import *
from itertools import *
from time import sleep


screen = [[0 for i in range(50)] for i in range(6)]
# screen = [[0 for i in range(7)] for i in range(3)]

for line in fileinput.input():
    new_screen = deepcopy(screen)
    line = line.strip()
    l = line

    if line.startswith('rect'):
        line = line.lstrip('rect ')
        a, x, b = line.partition('x')
        a, b = int(a), int(b)
        for row in range(b):
            for col in range(a):
                new_screen[row][col] = 1
    elif line.startswith('rotate row y='):
        line = line.lstrip('rotate row y=')
        a, by, b = line.partition(' by ')
        a, b = int(a), int(b)
        for x, cell in enumerate(screen[a]):
            if screen[a][x] == 1:
                new_screen[a][x] = 0
        for x, cell in enumerate(screen[a]):
            if screen[a][x] == 1:
                if x + b >= len(screen[a]):
                    new_screen[a][x + b - len(screen[a])] = 1
                else:
                    new_screen[a][x + b] = 1
    elif line.startswith('rotate column x='):
        line = line.lstrip('rotate column x=')
        a, by, b = line.partition(' by ')
        a, b = int(a), int(b)
        for y, row in enumerate(screen):
            for x, cell in enumerate(row):
                if all((x == a, cell == 1)):
                    new_screen[y][a] = 0
        for y, row in enumerate(screen):
            for x, cell in enumerate(row):
                if all((x == a, cell == 1)):
                    if y + b >= len(screen):
                        new_screen[y + b - len(screen)][a] = 1
                    else:
                        new_screen[y + b][a] = 1
    screen = new_screen

    print(f'input: {l}')
    for row in screen:
        print(''.join(['#' if cell else ' ' for cell in row]))
    # sleep(2)

for row in screen:
    print(''.join(['#' if cell else ' ' for cell in row]))

# print(f'hello world')
print('total: {}'.format(sum((sum(row) for row in screen))))
