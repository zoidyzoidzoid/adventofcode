#!/usr/local/bin/python3

from functools import lru_cache
import operator
from itertools import combinations_with_replacement

ALL_KEYS = set()


def load_ingredients() -> dict:
    with open('day15.txt', 'r') as instructions_file:
        strings = instructions_file.read()

    strings = [s for s in strings.split('\n') if s]

    # strings = [
    #     'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
    #     'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
    # ]

    ingredients = {}
    for s in strings:
        name, _, properties = s.partition(': ')
        properties = [item.split(' ') for item in properties.split(', ')]
        ingredients[name] = {item[0]: int(item[1]) for item in properties}
        global ALL_KEYS
        if not ALL_KEYS:
            ALL_KEYS = {item[0] for item in properties}
    return ingredients

print('Calculating max cookie score')

ingredients = load_ingredients()
# print(ingredients)


def score_cookie(quantities: dict) -> int:
    totals = []
    for property in ALL_KEYS:
        if property == 'calories':
            continue
        property_total = sum(
            ingredients[ingredient][property] * quantity
            for ingredient, quantity in quantities.items())
        if property_total <= 0:
            return 0
        totals.append(property_total)
    product = 1
    for total in totals:
        product *= total
    return product

max = None
max_quantities = None

for combo in combinations_with_replacement(sorted(ingredients.keys()), 100):
    present_ingredients = set(combo)
    quantities = {}
    for ingredient in present_ingredients:
        quantities[ingredient] = combo.count(ingredient)
    score = score_cookie(quantities)
    if max is None or score > max:
        max = score
        max_quantities = quantities

print('Max cookie score:', max, 'with quantities:', max_quantities)


def score_meal_replacement_cookie(quantities: dict) -> int:
    totals = []
    for property in ALL_KEYS:
        property_total = sum(
                ingredients[ingredient][property] * quantity
                for ingredient, quantity in quantities.items())
        if property_total <= 0 or property == 'calories' and property_total != 500:
            return 0

        if property != 'calories':
            totals.append(property_total)
    product = 1
    for total in totals:
        product *= total
    return product


print('Calculating max cookie score with 500 calories')

max = None
max_quantities = None

for combo in combinations_with_replacement(sorted(ingredients.keys()), 100):
    present_ingredients = set(combo)
    quantities = {}
    for ingredient in present_ingredients:
        quantities[ingredient] = combo.count(ingredient)
    score = score_meal_replacement_cookie(quantities)
    if max is None or score > max:
        max = score
        max_quantities = quantities

print('Max cookie score with 500 calories:', max, 'with quantities:', max_quantities)

