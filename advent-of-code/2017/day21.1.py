#!/usr/bin/env python3
# coding: utf-8

class TraceDict(dict):
    def __contains__(self, key):
        # print('Looked up:\n' + '\n'.join(key.split('/')))
        # print(key)
        return super().__contains__(key)


def process(inp, iterations=5):
    convs = TraceDict()
    for line in inp:
        line = line.split(' => ')
        convs[line[0]] = line[1]

    def rotate(square):
        square = square.split('/')
        result = flip_y('/'.join(
            ''.join(square[j][i] for j, c in enumerate(row))
            for i, row in enumerate(square)))
        return result

    def flip_x(square):
        square = square.split('/')
        result = []
        if len(square) == 3:
            result.extend((square[-1], square[1], square[0]))
        else:
            result.extend((square[-1], square[0]))
        return '/'.join(result)

    def flip_y(square):
        square = square.split('/')
        result = []
        for row in square:
            row = list(row)
            row[0], row[-1] = row[-1], row[0]
            row = ''.join(row)
            result.append(row)
        return '/'.join(result)

    grid = ['.#.', '..#', '###']

    print('\n'.join(grid))
    for _ in range(iterations):
        if len(grid) % 2 == 0:
            new_grid = ['' for i in range(len(grid) // 2 * 3)]
            for i in range(len(grid) // 2):
                for j in range(len(grid[0]) // 2):
                    square = [
                        row[i * 2:(i + 1) * 2]
                        for row in grid[j * 2:(j + 1) * 2]
                    ]
                    match = '/'.join(square)
                    print('Looking for match for', match)
                    if match in convs:
                        new = convs[match]
                    elif flip_x(match) in convs:
                        new = convs[flip_x(match)]
                    elif flip_y(match) in convs:
                        new = convs[flip_y(match)]
                    elif rotate(match) in convs:
                        new = convs[rotate(match)]
                    elif rotate(rotate(match)) in convs:
                        new = convs[rotate(rotate((match)))]
                    elif rotate(rotate(rotate(match))) in convs:
                        new = convs[rotate(rotate(rotate(match)))]
                    elif flip_y(rotate(match)) in convs:
                        new = convs[flip_y(rotate((match)))]
                    elif flip_y(rotate(rotate(rotate(match)))) in convs:
                        new = convs[flip_y(rotate(rotate(rotate(match))))]
                    else:
                        for k, v in convs.items():
                            if match.count('#') == k.count('#'):
                                print('Tried', match, '==', k)

                    print('Converting {} to {}'.format(match, new))
                    new = new.split('/')
                    new_grid[(j * 3)] += (new[0])
                    new_grid[(j * 3) + 1] += (new[1])
                    new_grid[(j * 3) + 2] += (new[2])
                    print('\n'.join(new_grid))
        else:
            new_grid = ['' for i in range(len(grid) // 3 * 4)]
            for i in range(len(grid) // 3):
                for j in range(len(grid[0]) // 3):
                    square = [
                        row[i * 3:(i + 1) * 3]
                        for row in grid[j * 3:(j + 1) * 3]
                    ]
                    match = '/'.join(square)
                    if match in convs:
                        new = convs[match]
                    elif flip_x(match) in convs:
                        new = convs[flip_x(match)]
                    elif flip_y(match) in convs:
                        new = convs[flip_y(match)]
                    elif rotate(match) in convs:
                        new = convs[rotate(match)]
                    elif rotate(rotate(match)) in convs:
                        new = convs[rotate(rotate((match)))]
                    elif rotate(rotate(rotate(match))) in convs:
                        new = convs[rotate(rotate(rotate(match)))]
                    elif flip_y(rotate(match)) in convs:
                        new = convs[flip_y(rotate((match)))]
                    elif flip_y(rotate(rotate(rotate(match)))) in convs:
                        new = convs[flip_y(rotate(rotate(rotate(match))))]
                    else:
                        for k, v in convs.items():
                            if match.count('#') == k.count('#'):
                                print('Tried', match, '==', k)
                    print('Converting {} to {}'.format(match, new))
                    new = new.split('/')
                    new_grid[(j * 4)] += (new[0])
                    new_grid[(j * 4) + 1] += (new[1])
                    new_grid[(j * 4) + 2] += (new[2])
                    new_grid[(j * 4) + 3] += (new[3])
                    del new

        print('\n'.join(new_grid))
        grid = new_grid

    total = 0
    for row in grid:
        total += row.count('#')
    return total

# eg_inp = """../.# => ##./#../...
# .#./..#/### => #..#/..../..../#..#""".split('\n')
# print(process(eg_inp, 2))
print(process(open('day21.txt').read().strip().split('\n')))
