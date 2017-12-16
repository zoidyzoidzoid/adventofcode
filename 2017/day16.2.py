#!/usr/bin/env python3
# coding: utf-8


def do_work(output, inp):
    for i in inp:
        if i[0] == 's':
            pos = int(i[1:])
            output = output[-pos:] + output[:-pos]
        elif i[0] == 'x':
            l, r = i[1:].split('/')
            l, r = int(l), int(r)
            output[l], output[r] = output[r], output[l]
        elif i[0] == 'p':
            l, r = i[1:].split('/')
            l, r = output.index(l), output.index(r)
            output[l], output[r] = output[r], output[l]
    return output



def process(inp):
    inp = inp.split(',')
    orig = [chr(ord('a') + i) for i in range(16)]
    output = [chr(ord('a') + i) for i in range(16)]
    for c in range(1000000000):
        output = do_work(output, inp)
        if output == orig:
            loop = c + 1
            break
    output = [chr(ord('a') + i) for i in range(16)]
    for c in range(1000000000 % loop):
        output = do_work(output, inp)
    return ''.join(output)


# print(process('s1'))
# print(process('x3/4'))
# print(process('pe/b'))
print(process(open('day16.txt').read()))
