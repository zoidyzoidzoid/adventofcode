#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import sys
import math
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


def a(lines):
    all_ingredients = set()
    guesses = defaultdict(set)
    for i, line in enumerate(lines):
        ingredients, _, confirmed_allergens = line.partition(' (contains ')
        ingredients = set(ingredients.split(' '))
        all_ingredients.update(ingredients)
        confirmed_allergens = confirmed_allergens[:-1].split(', ')
        for allergen in confirmed_allergens:
            if len(guesses[allergen]) == 0:
                guesses[allergen] = ingredients.copy()
            else:
                guesses[allergen].intersection_update(ingredients)
        # print(ingredients, confirmed_allergens)
    while any(len(v) > 1 for v in guesses.values()):
        for k, v in guesses.items():
            if len(v) == 1:
                for l, w in guesses.items():
                    if l != k:
                        try:
                            guesses[l].difference_update(v)
                        except KeyError:
                            pass
    no_allergens = all_ingredients.difference(set(i.pop() for i in guesses.values()))
    result = 0
    for i, line in enumerate(lines):
        ingredients, _, confirmed_allergens = line.partition(' (contains ')
        ingredients = set(ingredients.split(' '))
        result += len(no_allergens.intersection(ingredients))
    # # print(guesses)
    # # print(your_ticket)
    # # print(nearby_tickets)
    # result = 1
    # for pos, guess in guesses.items():
    #     if all((i.startswith('departure') for i in guess)):
    #         result *= your_ticket[pos]
    # for pos, guess in guesses.items():
    #     print(pos, guess)
    print(result)



def b(lines):
    all_ingredients = set()
    guesses = defaultdict(set)
    for i, line in enumerate(lines):
        ingredients, _, confirmed_allergens = line.partition(' (contains ')
        ingredients = set(ingredients.split(' '))
        all_ingredients.update(ingredients)
        confirmed_allergens = confirmed_allergens[:-1].split(', ')
        for allergen in confirmed_allergens:
            if len(guesses[allergen]) == 0:
                guesses[allergen] = ingredients.copy()
            else:
                guesses[allergen].intersection_update(ingredients)
    while any(len(v) > 1 for v in guesses.values()):
        for k, v in guesses.items():
            if len(v) == 1:
                for l, w in guesses.items():
                    if l != k:
                        try:
                            guesses[l].difference_update(v)
                        except KeyError:
                            pass
    result = []
    for k in sorted(guesses):
        result.append(guesses[k].pop())
    print(','.join(result))


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
