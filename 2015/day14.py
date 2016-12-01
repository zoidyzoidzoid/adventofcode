#!/usr/local/bin/python3

from copy import deepcopy
from pprint import pprint

with open('day14.txt', 'r') as instructions_file:
    strings = instructions_file.read()

# strings = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
# """

strings = [s for s in strings.split('\n') if s]


def add_reindeers(reindeers, string):
    reindeer_name, _, string = string.partition(' can fly ')
    flight_speed, _, string = string.partition(' km/s for ')
    flight_duration, _, string = string.partition(' seconds, but then must rest for ')
    rest_duration, _, string = string.partition(' seconds.')
    flight_speed, flight_duration, rest_duration = map(
        int, (flight_speed, flight_duration, rest_duration))
    reindeers[reindeer_name] = {
        'flight_speed': flight_speed,
        'flight_duration': flight_duration,
        'rest_duration': rest_duration,
        'period': rest_duration + flight_duration,
        'score': 0,
        'current_pos': 0,
    }

reindeers = {}

for s in strings:
    add_reindeers(reindeers, s)

print(reindeers)

duration = 2503
# duration = 1000

print('Optimising', len(reindeers), 'for duration', duration, 'seconds')

maximum = None
msg = ''

for name, reindeer in reindeers.items():
    complete_cycles = duration // reindeer['period']
    left_over_seconds = duration - (complete_cycles * reindeer['period'])
    distance = (complete_cycles * reindeer['flight_duration']) * reindeer['flight_speed']
    if left_over_seconds >= reindeer['flight_duration']:
        distance += reindeer['flight_speed'] * reindeer['flight_duration']
    else:
        distance += reindeer['flight_speed'] * left_over_seconds
    if maximum is None or distance > maximum:
        maximum = distance
        msg = '{} is in the lead at {} km'.format(name, distance)

print(msg)

print('Optimising', len(reindeers), 'for duration', duration, 'seconds with new scoring strategy')

for i in range(duration):
    for name, reindeer in reindeers.items():
        complete_cycles = i // reindeer['period']
        left_over_seconds = i - (complete_cycles * reindeer['period'])
        if left_over_seconds < reindeer['flight_duration']:
            reindeer['current_pos'] += reindeer['flight_speed']
    max_dist = max(reindeer['current_pos'] for reindeer in reindeers.values())
    for name, reindeer in reindeers.items():
        if reindeer['current_pos'] == max_dist:
            reindeer['score'] += 1
            print('{}:'.format(i), name, 'at', reindeer['current_pos'],
                  'score:', reindeer['score'])

maximum = None
msg = ''

for name, reindeer in reindeers.items():
    score = reindeer['score']
    if maximum is None or score > maximum:
        maximum = score
        msg = '{} is in the lead with score of {}'.format(name, score)

print(msg)
