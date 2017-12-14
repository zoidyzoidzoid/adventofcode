#!/usr/bin/env python3
# coding: utf-8
import fileinput


def process(inp):
    layers = []
    for line in inp:
        layer, depth = line.split(': ')
        layer, depth = int(layer), int(depth)
        layers.append('(x + {}) % {}'.format(layer, (depth - 1) * 2))
    pico = 0
    while True:
        # print(layers)
        # print('x =', pico)
        # print(total)
        if any(eval(layer.replace('x', str(pico))) == 0 for layer in layers):
            pico += 1
            continue
        return pico

print(process(['0: 3', '1: 2', '4: 4', '6: 4']))


lines = []
for line in fileinput.input():
    lines.append(line.strip())

print(process(lines))
