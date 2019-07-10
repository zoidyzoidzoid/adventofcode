#!/usr/local/bin/python3

import json

def sum_of_values(data, ignore_red=False):
    if isinstance(data, int):
        return data
    elif isinstance(data, str):
        return 0
    elif isinstance(data, dict):
        if ignore_red and any(value == 'red' for value in data.values()):
            return 0
        return sum_of_values(data.values(), ignore_red=ignore_red)
    else:
        return sum(sum_of_values(item, ignore_red=ignore_red) for item in data)

def get_total(json_string, ignore_red=False):
    data = json.loads(json_string)
    return sum_of_values(data, ignore_red=ignore_red)

with open('day12.txt', 'r') as instructions_file:
    strings = instructions_file.read()

custom_input = strings.split('\n')[0]

print('Counting items with objects')

test_strings = [
    ('[1,2,3]', 6),
    ('{"a":2,"b":4}', 6),
    ('[[[3]]]', 3),
    ('{"a":{"b":4},"c":-1}', 3),
    ('{"a":[-1,1]}', 0),
    ('[-1,{"a":1}]', 0),
    ('[]', 0),
    ('{}', 0)
]

for s, expected_total in test_strings:
    total = get_total(s)
    assert total == expected_total, 'Sum of {} was {} instead of {}'.format(
        s, total, expected_total)

print('Total:', get_total(custom_input))


print('Counting items with objects with "red" values ignored')

test_strings = [
    ('[1,2,3]', 6),
    ('[1,{"c":"red","b":2},3]', 4),
    ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
    ('[1,"red",5]', 6)
]

for s, expected_total in test_strings:
    total = get_total(s, ignore_red=True)
    assert total == expected_total, 'Sum of {} was {} instead of {}'.format(
        s, total, expected_total)

print('Total:', get_total(custom_input, ignore_red=True))
