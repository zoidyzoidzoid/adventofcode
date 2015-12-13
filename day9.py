#!/usr/local/bin/python3

from collections import deque
from copy import deepcopy

with open('day9.txt', 'r') as instructions_file:
    strings = instructions_file.read()

strings = [s for s in strings.split('\n') if s]

# strings = [
#     'London to Dublin = 464',
#     'London to Belfast = 518',
#     'Dublin to Belfast = 141'
# ]


def add_trip(trips, pos1, pos2, distance):
    if pos1 not in trips:
        trips[pos1] = {}
    trips[pos1][pos2] = int(distance)

    return trips


def add_trips(trips, pos1, pos2, distance):
    trips = add_trip(trips, pos1, pos2, distance)
    trips = add_trip(trips, pos2, pos1, distance)
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

print('Calculating route with minimum route')

trips = {}

for s in strings:
    route, _, distance = s.partition(' = ')
    pos1, _, pos2 = route.partition(' to ')
    trips = add_trips(trips, pos1, pos2, distance)

# print(trips)

all_routes = []

for start_pos in trips.keys():
    all_routes.extend(generate_routes([start_pos]))

# print(all_routes)

minimum = None
minimum_route = None

for route in all_routes:
    current_dist = sum((
        trips[cur_pos][route[cur_loc + 1]]
        for cur_loc, cur_pos in enumerate(route[:-1])))
    if minimum is None:
        minimum = current_dist
    elif min(minimum, current_dist) == current_dist:
        minimum = current_dist
        minimum_route = ' -> '.join(route)

print (minimum_route, '=', minimum)

print('Calculating route with maximum distance')

maximum = None
maximum_route = None

for route in all_routes:
    current_dist = sum((
        trips[cur_pos][route[cur_loc + 1]]
        for cur_loc, cur_pos in enumerate(route[:-1])))
    if maximum is None:
        maximum = current_dist
    elif max(maximum, current_dist) == current_dist:
        maximum = current_dist
        maximum_route = ' -> '.join(route)

print (maximum_route, '=', maximum)
