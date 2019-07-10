#!/usr/bin/env python3
# coding: utf-8
import fileinput


def process(inp):
    layers = {}
    for line in inp:
        layer, depth = line.split(': ')
        layer, depth = int(layer), int(depth)
        layers[layer] = ['[ ]' for i in range(depth)]
    pico = 0
    severity = 0
    positions = {}
    for num, layer in layers.items():
        for index, item in enumerate(layer):
            if index == pico % len(layer):
                positions[num] = index, 1
                layers[num][index] = '[S]'
            else:
                layers[num][index] = '[ ]'
    # print('Pico', pico)
    # for i, row in layers.items():
    #     print('{}: {}'.format(i, ' '.join(row)))
    while pico <= max(layers):
        if layers.get(pico) is not None:
            if layers[pico][0] == '[S]':
                print('Caught on layer {}, added {}'.format(pico, len(layers[pico]) * pico))
                severity += (len(layers[pico]) * pico)
                layers[pico][0] = '(S)'
            else:
                layers[pico][0] = '( )'
        # print('Pico', pico)
        # for i, row in layers.items():
        #     print('{}: {}'.format(i, ' '.join(row)))
        for num, layer in layers.items():
            positions[num] = positions[num][0] + positions[num][1], positions[num][1]
            if positions[num][0] == len(layer):
                positions[num] = positions[num][0] - 2, -1
            elif positions[num][0] == -1:
                positions[num] = positions[num][0] + 2, 1
            for index, item in enumerate(layer):
                if index == positions[num][0]:
                    if layers[num][index] == '( )':
                        layers[num][index] = '(S)'
                    else:
                        layers[num][index] = '[S]'
                else:
                    layers[num][index] = '[ ]'
        # print(positions)
        pico += 1
    return severity


print(process(['0: 3', '1: 2', '4: 4', '6: 4']))

lines = []
for line in fileinput.input():
    lines.append(line.strip())

print(process(lines))
