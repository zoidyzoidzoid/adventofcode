#!/usr/bin/env python
# coding: utf-8


def knot_hash(inp):
    sparse = [x for x in range(256)]
    inp = [ord(c) for c in inp] + [17, 31, 73, 47, 23]
    pos = 0
    skip = 0
    for _ in range(64):
        for length in inp:
            l = pos + length
            if l >= 256:
                while l >= 256:
                    l -= 256
                s = sparse[pos:] + sparse[:l]
                s = list(reversed(s))
                sparse = s[len(s) - l:] + sparse[l:pos] + s[:len(s) - l]
            else:
                sparse = sparse[:pos] + list(reversed(sparse[pos:l])) + sparse[l:]
            pos += length + skip
            while pos >= 256:
                pos -= 256
            skip += 1
    dense = ''
    for i in range(16):
        output = 0
        for k in sparse[i * 16:(i * 16) + 16]:
            output ^= k
        dense += '{:0>2x}'.format(output)
    return dense


directions = {
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0)
}


def process(inp):
    print(inp)
    grid = [['.' for i in range(128)] for i in range(128)]
    total = 0
    for i in range(128):
        key = inp + '-' + str(i)
        hash = knot_hash(key)
        for j, x in enumerate(hash):
            for k, y in enumerate('{:04b}'.format(int(x, base=16))):
                if y == '1':
                    grid[i][(j * 4) + k] = '#'
                    total += 1
    # for row in grid:
    #     print(''.join(row))
    visited = set()
    region = 1
    def visit(grid, x, y):
        if (x, y) in visited:
            return 0
        visited.add((x, y))
        if grid[y][x] != '#':
            return 0
        t = 1
        for d_x, d_y in directions:
            if y + d_y < 0 or y + d_y >= 128:
                continue
            if x + d_x < 0 or x + d_x >= 128:
                continue
            if grid[y + d_y][x + d_x] == '#':
                t += 1
                t += visit(grid, x + d_x, y + d_y)
                # grid[y + d_y][x + d_x] = str(region)
        return t
    for y, col in enumerate(grid):
        for x, _ in enumerate(col):
            if visit(grid, x, y):
                region += 1
    # for row in grid:
    #     print(''.join(row))
    return region - 1


print('Example')
print(process('flqrgnkx'))
print('Puzzle input')
print(process('vbqugkhl'))
