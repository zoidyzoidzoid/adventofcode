#!/usr/local/bin/python3

from itertools import combinations

TOTAL = 150
# TOTAL = 25


def load_containers() -> list:
    with open('day17.txt', 'r') as instructions_file:
        strings = instructions_file.read()

    strings = [s for s in strings.split('\n') if s]

    # strings = ['20', '15', '10', '5', '5']

    return list(map(int, strings))


print('Finding the amount of containers that fit exactly', TOTAL, 'litres')

# print('Loading containers from file')
containers = load_containers()

suitable_combos = []

for total_containers in range(1, len(containers) + 1):
    for combo in combinations(containers, total_containers):
        if sum(combo) == TOTAL:
            suitable_combos.append(combo)

print('Found', len(suitable_combos), 'suitable combos for', TOTAL, 'litres')

print('Finding how many combinations use the minimum possible containers for',
      TOTAL, 'litres')

# print('Loading containers from file')
containers = load_containers()

minimum_amount = None
suitable_combos = []

for total_containers in range(1, len(containers) + 1):
    amount = total_containers
    for combo in combinations(containers, total_containers):
        if sum(combo) == TOTAL:
            if minimum_amount is None:
                minimum_amount = amount
            if minimum_amount == amount:
                suitable_combos.append(suitable_combos)
    if minimum_amount:
        break

print('Found', len(suitable_combos), 'suitable combos for', TOTAL, 'litres')

