#!/usr/local/bin/python3

from copy import deepcopy
from pprint import pprint

with open('day13.txt', 'r') as instructions_file:
    strings = instructions_file.read()

# strings = """Alice would gain 54 happiness units by sitting next to Bob.
# Alice would lose 79 happiness units by sitting next to Carol.
# Alice would lose 2 happiness units by sitting next to David.
# Bob would gain 83 happiness units by sitting next to Alice.
# Bob would lose 7 happiness units by sitting next to Carol.
# Bob would lose 63 happiness units by sitting next to David.
# Carol would lose 62 happiness units by sitting next to Alice.
# Carol would gain 60 happiness units by sitting next to Bob.
# Carol would gain 55 happiness units by sitting next to David.
# David would gain 46 happiness units by sitting next to Alice.
# David would lose 7 happiness units by sitting next to Bob.
# David would gain 41 happiness units by sitting next to Carol.
# """

strings = [s for s in strings.split('.\n') if s]


def add_trip(trips, pos1, pos2, distance):
    if pos1 not in trips:
        trips[pos1] = {}
    trips[pos1][pos2] = int(distance)

    return trips


def add_trips(trips, pos1, pos2, distance):
    trips = add_trip(trips, pos1, pos2, distance)
    return trips


def get_all_possible_destinations(key):
    return trips[key].keys()


def generate_routes(route):
    if len(route) + 1 == len(trips.keys()):
        return [
            route + [next_pos]
            for next_pos in get_all_possible_destinations(route[-1])
            if next_pos not in route
        ]
    else:
        return [
            new_route
            for next_pos in get_all_possible_destinations(route[-1])
            for new_route in generate_routes(route + [next_pos])
            if next_pos not in route
        ]


# print('Calculating arrangement with maximum happiness')

# trips = {}

# for s in strings:
#     phrase, _, person2 = s.partition(' happiness units by sitting next to ')
#     person1, _, happiness_phrase = phrase.partition(' would ')
#     polarity, _, magnitude = happiness_phrase.partition(' ')
#     happiness_delta = int(magnitude)
#     if polarity == 'lose':
#         happiness_delta *= -1
#     trips = add_trips(trips, person1, person2, happiness_delta)

# # pprint(trips)

# all_routes = []

# for start_pos in trips.keys():
#     all_routes.extend(generate_routes([start_pos]))

# # print('\n'.join((str(r) for r in all_routes)))

# maximum = None
# maximum_route = None

# for route in all_routes:
#     route.append(route[0])
#     dir1_happiness = sum((trips[cur_pos][route[cur_loc + 1]]
#                          for cur_loc, cur_pos in enumerate(route[:-1])))
#     route = route[::-1]
#     dir2_happiness = sum((trips[cur_pos][route[cur_loc + 1]]
#                          for cur_loc, cur_pos in enumerate(route[:-1])))
#     current_dist = dir1_happiness + dir2_happiness
#     if maximum is None:
#         maximum = current_dist
#     elif max(maximum, current_dist) == current_dist:
#         maximum = current_dist
#         maximum_route = ' -> '.join(route)

# print(maximum_route, '=', maximum)

print('Calculating arrangement with maximum happiness including yourself')

trips = {}

for s in strings:
    phrase, _, person2 = s.partition(' happiness units by sitting next to ')
    person1, _, happiness_phrase = phrase.partition(' would ')
    polarity, _, magnitude = happiness_phrase.partition(' ')
    happiness_delta = int(magnitude)
    if polarity == 'lose':
        happiness_delta *= -1
    trips = add_trips(trips, person1, person2, happiness_delta)

# pprint(trips)

for trip in list(trips.keys()):
    add_trip(trips, 'Myself', trip, 0)
    add_trip(trips, trip, 'Myself', 0)

all_routes = []

for start_pos in trips.keys():
    all_routes.extend(generate_routes([start_pos]))

maximum = None
maximum_route = None

for route in all_routes:
    route.append(route[0])
    dir1_happiness = sum((trips[cur_pos][route[cur_loc + 1]]
                         for cur_loc, cur_pos in enumerate(route[:-1])))
    route = route[::-1]
    dir2_happiness = sum((trips[cur_pos][route[cur_loc + 1]]
                         for cur_loc, cur_pos in enumerate(route[:-1])))
    current_dist = dir1_happiness + dir2_happiness
    if maximum is None:
        maximum = current_dist
    elif max(maximum, current_dist) == current_dist:
        maximum = current_dist
        maximum_route = ' -> '.join(route)

print(maximum_route, '=', maximum)
