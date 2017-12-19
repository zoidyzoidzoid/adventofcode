#!/usr/bin/env python3
# coding: utf-8


def process(rows):
    pos_x, pos_y = rows[0].index('|'), 0
    direction = 0, 1

    collected = []
    while True:
        new_y = pos_y + direction[1]
        new_x = pos_x + direction[0]
        # print('Trying {},{}'.format(new_x, new_y))
        if 0 < new_y < len(rows) and 0 < new_x < len(rows[new_y]) and rows[new_y][new_x] != ' ':
            # print('Visited {},{}: {}'.format(new_x, new_y, rows[new_y][new_x]))
            pos_y, pos_x = new_y, new_x
            if rows[pos_y][pos_x] not in '-+|':
                collected.append(rows[pos_y][pos_x])
        else:
            if direction[0] == 0:
                directions = (
                    (1, 0),
                    (-1, 0)
                )
            else:
                directions = (
                    (0, 1,),
                    (0, -1)
                )
            for dir_x, dir_y in directions:
                new_y = pos_y + dir_y
                new_x = pos_x + dir_x
                if 0 < new_y < len(rows) and 0 < new_x < len(rows[new_y]) and rows[new_y][new_x] != ' ':
                    direction = dir_x, dir_y
                    break
            else:
                return ''.join(collected)


eg_inp = """     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+ """.split('\n')
print(process(eg_inp))
rows = open('day19.txt').read().split('\n')
print(process(rows))
