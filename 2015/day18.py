#!/usr/local/bin/python3

from copy import deepcopy

ON = '#'
OFF = '.'

SIDE = 100
# SIDE = 6

STEPS = 100
# STEPS = 4

NEIGHBOURS = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),
              (1, 1)}


def get_initial_state() -> list:
    with open('day18.txt', 'r') as instructions_file:
        strings = instructions_file.read()

    strings = [s for s in strings.split('\n') if s]

    # strings = [
    #     '.#.#.#',
    #     '...##.',
    #     '#....#',
    #     '..#...',
    #     '#.#..#',
    #     '####..'
    # ]

    strings = [[y for y in row] for row in strings]

    return strings


def get_neighbours(grid, row, col):
    neighbours = []
    for delta in NEIGHBOURS:
        neighbour_row = row + delta[0]
        neighbour_col = col + delta[1]
        if neighbour_row >= SIDE or neighbour_row < 0:
            continue
        if neighbour_col >= SIDE or neighbour_col < 0:
            continue
        neighbours.append(grid[neighbour_row][neighbour_col])
    return neighbours

grid = get_initial_state()

# print('\n'.join(''.join(row) for row in grid))

for i in range(1, STEPS+1):
    prev_grid = deepcopy(grid)
    # print('Doing step', i)
    for row_number, row in enumerate(grid):
        for col_number, value in enumerate(row):
            neighbours = get_neighbours(prev_grid, row_number, col_number)
            if value == ON:
                stays_on = sum(neighbour == ON for neighbour in neighbours) in {2, 3}
                grid[row_number][col_number] = ON if stays_on else OFF
            else:
                turns_on = sum(neighbour == ON for neighbour in neighbours) == 3
                grid[row_number][col_number] = ON if turns_on else OFF
    # print('\n'.join(''.join(row) for row in grid))

print('Found', sum(sum(light == ON for light in row) for row in grid), 'lights on')

# SIDE = 6
# STEPS = 5
CORNERS = {(0, 0), (0, SIDE - 1), (SIDE - 1, 0), (SIDE - 1, SIDE - 1)}

def get_neighbours_with_broken_lights(grid, row, col):
    neighbours = []
    for delta in NEIGHBOURS:
        neighbour_row = row + delta[0]
        neighbour_col = col + delta[1]
        if neighbour_row >= SIDE or neighbour_row < 0:
            continue
        if neighbour_col >= SIDE or neighbour_col < 0:
            continue
        if (neighbour_row, neighbour_col) in CORNERS:
            neighbours.append(ON)
        else:
            neighbours.append(grid[neighbour_row][neighbour_col])
    return neighbours


print('Calculating lights on with broken corners')

grid = get_initial_state()


for x, y in CORNERS:
    grid[x][y] = ON

# print('\n'.join(''.join(row) for row in grid))


for i in range(1, STEPS+1):
    prev_grid = deepcopy(grid)
    # print('Doing step', i)
    for row_number, row in enumerate(grid):
        for col_number, value in enumerate(row):
            neighbours = get_neighbours_with_broken_lights(prev_grid, row_number, col_number)
            if value == ON:
                stays_on = sum(neighbour == ON for neighbour in neighbours) in {2, 3}
                grid[row_number][col_number] = ON if stays_on else OFF
            else:
                turns_on = sum(neighbour == ON for neighbour in neighbours) == 3
                grid[row_number][col_number] = ON if turns_on else OFF

    for x, y in CORNERS:
        grid[x][y] = ON
    # print('\n'.join(''.join(row) for row in grid))

print('Found', sum(sum(light == ON for light in row) for row in grid), 'lights on with broken lighting grid')

