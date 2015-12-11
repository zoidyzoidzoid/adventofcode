#!/usr/local/bin/python3

with open('day6.txt', 'r') as f:
    inss = f.read()

inss = [ins for ins in inss.split('\n') if ins]

grid = [[False for i in range(1000)] for j in range(1000)]


print('Turning lighs off and on')


for ins in inss:
    breakdown = ins.split(' through ')

    start_x, start_y = breakdown[0].split()[-1].split(',')
    start_x, start_y = int(start_x), int(start_y)

    end_x, end_y = breakdown[1].split(',')
    end_x, end_y = int(end_x), int(end_y)

    command = ' '.join(breakdown[0].split()[:-1])

    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            if command == 'toggle':
                grid[i][j] = not grid[i][j]
            elif command == 'turn on':
                grid[i][j] = True
            elif command == 'turn off':
                grid[i][j] = False

print('Lights on:', sum(sum(ys) for ys in grid))


grid = [[0 for i in range(1000)] for j in range(1000)]


print('Calculating total brightness')


for ins in inss:
    breakdown = ins.split(' through ')

    start_x, start_y = breakdown[0].split()[-1].split(',')
    start_x, start_y = int(start_x), int(start_y)

    end_x, end_y = breakdown[1].split(',')
    end_x, end_y = int(end_x), int(end_y)

    command = ' '.join(breakdown[0].split()[:-1])

    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            if command == 'toggle':
                grid[i][j] += 2
            elif command == 'turn on':
                grid[i][j] += 1
            elif command == 'turn off':
                grid[i][j] = max(grid[i][j] - 1, 0)

print('Total brightness:', sum(sum(ys) for ys in grid))
