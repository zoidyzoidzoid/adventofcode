#!/usr/local/bin/python3

from collections import Counter

with open('day5.txt', 'r') as f:
    strings = f.read()

strings = [s for s in strings.split('\n') if s]

VOWELS = Counter('aeiou')
NAUGHTY_COMBOS = {'ab', 'cd', 'pq', 'xy'}


def is_nice(string):
    has_enough_vowels = sum(
        val for key, val in Counter(string).items() if key in VOWELS) > 2
    if not has_enough_vowels:
        return

    has_double_letters = False
    for pos, char in enumerate(string):
        if (pos + 1 < len(string)) and (char == string[pos + 1]):
            has_double_letters = True
            break

    if not has_double_letters:
        return

    has_naughty_combos = any(combo in string for combo in NAUGHTY_COMBOS)
    if has_naughty_combos:
        return
    return True

nice_strings = 0

print('Counting nice strings')

for string in strings:
    if is_nice(string):
        nice_strings += 1

print('Found', nice_strings, 'nice strings')


def is_better_is_nice(string):
    has_non_overlapping_pairs = False
    has_repeated_letter_with_space = False

    for cur_pos, cur_char in enumerate(string[:-2]):
        cur_pair = string[cur_pos:cur_pos + 2]
        if cur_pair in string[cur_pos + 2:]:
            has_non_overlapping_pairs = True

        if cur_char == string[cur_pos + 2]:
            has_repeated_letter_with_space = True

        if has_non_overlapping_pairs and has_repeated_letter_with_space:
            break
    if not has_non_overlapping_pairs:
        return

    if not has_repeated_letter_with_space:
        return

    return True

nice_strings = 0

print('Counting nice strings betterer')

for string in strings:
    if is_better_is_nice(string):
        nice_strings += 1

print('Found', nice_strings, 'better nice strings')
