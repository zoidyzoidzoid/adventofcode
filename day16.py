#!/usr/local/bin/python3

from itertools import combinations_with_replacement


def load_sues() -> dict:
    with open('day16.txt', 'r') as instructions_file:
        strings = instructions_file.read()

    strings = [s for s in strings.split('\n') if s]

    sues = {}
    for s in strings:
        sue_id, _, properties = s.partition(': ')
        sue, _, uid = sue_id.partition(' ')
        uid = int(uid)
        properties = properties.split(', ')
        sues[uid] = {}
        for prop in properties:
            prop = prop.split(': ')
            sues[uid][prop[0]] = int(prop[1])
    return sues

print('Finding the right Aunt Sue')

print('Loading sues from file')
sues = load_sues()
# print(sues)

seeked_sue = {
    'akitas': 0,
    'cars': 2,
    'cats': 7,
    'children': 3,
    'goldfish': 5,
    'perfumes': 1,
    'pomeranians': 3,
    'samoyeds': 2,
    'trees': 3,
    'vizslas': 0
}

for sue_id, cur_sue in sues.items():
    looking_good = True
    for cur_sue_property, value in cur_sue.items():
        seeked_value = seeked_sue.get(cur_sue_property)
        if seeked_value is None:
            continue
        if seeked_value != value:
            looking_good = False
            break
    if looking_good:
        print('Found a sue with id:', sue_id, 'values: ', cur_sue)

print('Done!')



print('Finding the right Aunt Sue with new algorithm')

print('Loading sues from file')
sues = load_sues()
# print(sues)

seeked_sue = {
    'akitas': 0,
    'cars': 2,
    'cats': 7,
    'children': 3,
    'goldfish': 5,
    'perfumes': 1,
    'pomeranians': 3,
    'samoyeds': 2,
    'trees': 3,
    'vizslas': 0
}

for sue_id, cur_sue in sues.items():
    looking_good = True
    for cur_sue_property, value in cur_sue.items():
        seeked_value = seeked_sue.get(cur_sue_property)
        if seeked_value is None:
            continue
        if cur_sue_property in {'cats', 'trees'}:
            looking_good = value > seeked_value
        elif cur_sue_property in {'pomeranians', 'goldfish'}:
            looking_good = value < seeked_value
        else:
            looking_good = value == seeked_value
        if not looking_good:
            break

    if looking_good:
        print('Found a sue with id:', sue_id, 'values: ', cur_sue)

print('Done!')
