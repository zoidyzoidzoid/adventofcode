#!/usr/local/bin/python3

with open('day7.txt', 'r') as instructions_file:
    inss = instructions_file.read()

# inss = """123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i"""

inss = [ins for ins in inss.split('\n') if ins]


outputs = {}

print('Running circuit')

for ins in inss:
    command, _, result = ins.upper().partition(' -> ')
    command = command.replace('NOT', '~').replace('AND', '&').replace(
        'OR', '|').replace('LSHIFT', '<<').replace('RSHIFT', '>>')
    args = command.split(' ')
    outputs[result] = command


def complex_eval(key):
    command = key
    if key in outputs:
        command = outputs[key]

    args = str(command).split(' ')
    if len(args) == 1:
        res = args[0]
        if args[0] in outputs:
            res = complex_eval(args[0])
    elif len(args) == 2:
        if args[1] in outputs:
            res = ~ complex_eval(args[1])
    elif len(args) == 3:
        res = eval('{} {} {}'.format(
            complex_eval(args[0]),
            args[1],
            complex_eval(args[2])))
    if command != key:
        outputs[key] = res
    return int(res)

from copy import deepcopy

orig_outputs = deepcopy(outputs)

result = 'a'

print('Calculating original A')

output = int(complex_eval('A'))
if output < 0:
    output = 65536 + output
print('{}: {}'.format(result.lower(), output))


outputs = orig_outputs
outputs['B'] = 46065

print('Calculating A with new B signal')

output = int(complex_eval('A'))
if output < 0:
    output = 65536 + output
print('{}: {}'.format(result.lower(), output))
