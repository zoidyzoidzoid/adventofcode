#!/usr/bin/env python3
import bisect
import fileinput
import heapq
import sys
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt

def breadth_first_search(grid, x, y, dest_x, dest_y):
    open_set = deque()
    closed_set = set()
    meta = dict()

    root = x, y
    meta[root] = None, None
    open_set.appendleft(root)

    dirs = (
      (0, -1),
      (-1, 0),
      (+1, 0),
      (0, +1),
    )

    while open_set:
        x, y = open_set.pop()
        subtree_root = x, y
        
        if (x, y) == (dest_x, dest_y):
          return construct_path((x, y), meta)

        for d_x, d_y in dirs:
            child = x + d_x, y + d_y
          
            if child in closed_set:
                continue
            
            if child == (dest_x, dest_y) or grid.get(child, '#') == '.':
                if child not in open_set:
                    meta[child] = subtree_root, (d_x, d_y)
                    open_set.appendleft(child)           
        
        closed_set.add(subtree_root)

def construct_path(state, meta):
  action_list = list()
  
  # Continue until you reach root meta data (i.e. (None, None))
  while meta[state][0] is not None:
    state, action = meta[state]
    action_list.append(action)
  
  action_list.reverse()
  return action_list


def a(lines):
    return
    result = 0
    empty_grid = {}
    grid = {}
    chars = {}
    counts = defaultdict(int)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                continue
            empty_grid[x, y] = '.'
            grid[x, y] = c
            if c in ('E', 'G'):
                counts[c] += 1
                chars[x, y] = c, 200
    turns = 0
    while True:
        chars_length = len(chars.keys())
        chars_index = 0
        for x, y in (sorted(chars.keys(), key=lambda x: (x[1], x[0]))):
            chars_index += 1
            if (x, y) not in chars:
                continue
            c, hp = chars[x, y]
            enemies = []
            for i, j in (sorted(chars.keys(), key=lambda x: (x[1], x[0]))):
                if chars[i, j][0] != c:
                    enemies.append((i, j))
            mn_e = []
            mn = sys.maxsize
            # print(c, hp, x, y, enemies)
            for enemy in enemies:
                dest_x, dest_y = enemy
                result = breadth_first_search(grid, x, y, dest_x, dest_y)
                if result is None:
                    continue
                dist = len(result)
                if dist == mn:
                    mn_e.append(result)
                elif dist < mn:
                    mn = dist
                    mn_e = [result]
            if mn_e:
                d_x, d_y = mn_e[0][0]
                if mn > 1:
                    grid[x, y] = '.'
                    grid[x + d_x, y + d_y] = c
                    chars[x + d_x, y + d_y] = chars.pop((x, y))
                    x, y = x + d_x, y + d_y
            dirs = (
              (0, -1),
              (-1, 0),
              (+1, 0),
              (0, +1),
            )
            m_x, m_y = None, None
            m_hp = None
            for d_x, d_y in dirs:
                if chars.get((x + d_x, y + d_y), (c, 0))[0] != c:
                    if m_hp is None or chars.get((x + d_x, y + d_y), (c, sys.maxsize))[1] < m_hp:
                        m_x, m_y = (x + d_x), (y + d_y)
                        _, m_hp = chars[x + d_x, y + d_y]
            if m_x is None:
                continue
            e_c, hp = chars[m_x, m_y]
            # print('{} ({},{}) attacks {} ({},{})'.format(c, x, y, e_c, m_x, m_y))
            if hp - 3 <= 0:
                counts[e_c] -= 1
                grid[m_x, m_y] = '.'
                chars.pop((m_x, m_y))
                if counts['E'] == 0 or counts['G'] == 0:
                    x_l = min((i[0] for i in grid.keys())) - 1
                    y_l = min((i[1] for i in grid.keys())) - 1
                    x_r = max((i[0] for i in grid.keys())) + 2
                    y_r = max((i[1] for i in grid.keys())) + 2
                    for y in range(y_l, y_r):
                        for x in range(x_l, x_r):
                            print(grid.get((x, y), '#'), end='')
                        print()
                    if chars_index == chars_length:
                        turns += 1
                    print(turns)
                    for kls, hp in chars.values():
                        print(kls, hp)
                    print((turns) * (sum((x[1] for x in chars.values()))))
                    return
            else:
                chars[m_x, m_y] = e_c, hp - 3
        turns += 1
    # x_l = min((i[0] for i in grid.keys())) - 1
    # y_l = min((i[1] for i in grid.keys())) - 1
    # x_r = max((i[0] for i in grid.keys())) + 2
    # y_r = max((i[1] for i in grid.keys())) + 2
    # for y in range(y_l, y_r):
    #     for x in range(x_l, x_r):
    #         print(grid.get((x, y), '#'), end='')
    #     print()
    #     # break
    # print(result)

def b(lines):
    att = 4
    while True:
        try:
            soln(lines, att)
        except:
            att += 1
        else:
            return att



def soln(lines, attack_power):
    result = 0
    empty_grid = {}
    grid = {}
    chars = {}
    counts = defaultdict(int)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                continue
            empty_grid[x, y] = '.'
            grid[x, y] = c
            if c in ('E', 'G'):
                counts[c] += 1
                chars[x, y] = c, 200
    turns = 0
    while True:
        chars_length = len(chars.keys())
        chars_index = 0
        for x, y in (sorted(chars.keys(), key=lambda x: (x[1], x[0]))):
            chars_index += 1
            if (x, y) not in chars:
                continue
            c, hp = chars[x, y]
            enemies = []
            for i, j in (sorted(chars.keys(), key=lambda x: (x[1], x[0]))):
                if chars[i, j][0] != c:
                    enemies.append((i, j))
            mn_e = []
            mn = sys.maxsize
            # print(c, hp, x, y, enemies)
            for enemy in enemies:
                dest_x, dest_y = enemy
                result = breadth_first_search(grid, x, y, dest_x, dest_y)
                if result is None:
                    continue
                dist = len(result)
                if dist == mn:
                    mn_e.append(result)
                elif dist < mn:
                    mn = dist
                    mn_e = [result]
            if mn_e:
                d_x, d_y = mn_e[0][0]
                if mn > 1:
                    grid[x, y] = '.'
                    grid[x + d_x, y + d_y] = c
                    chars[x + d_x, y + d_y] = chars.pop((x, y))
                    x, y = x + d_x, y + d_y
            dirs = (
              (0, -1),
              (-1, 0),
              (+1, 0),
              (0, +1),
            )
            m_x, m_y = None, None
            m_hp = None
            for d_x, d_y in dirs:
                if chars.get((x + d_x, y + d_y), (c, 0))[0] != c:
                    if m_hp is None or chars.get((x + d_x, y + d_y), (c, sys.maxsize))[1] < m_hp:
                        m_x, m_y = (x + d_x), (y + d_y)
                        _, m_hp = chars[x + d_x, y + d_y]
            if m_x is None:
                continue
            e_c, hp = chars[m_x, m_y]
            # print('{} ({},{}) attacks {} ({},{})'.format(c, x, y, e_c, m_x, m_y))
            if e_c == 'E':
                att = 3
            else:
                att = attack_power
            if hp - att <= 0:
                if e_c == 'E':
                    raise AssertionError('Elf died!')
                counts[e_c] -= 1
                grid[m_x, m_y] = '.'
                chars.pop((m_x, m_y))
                if counts['E'] == 0 or counts['G'] == 0:
                    x_l = min((i[0] for i in grid.keys())) - 1
                    y_l = min((i[1] for i in grid.keys())) - 1
                    x_r = max((i[0] for i in grid.keys())) + 2
                    y_r = max((i[1] for i in grid.keys())) + 2
                    for y in range(y_l, y_r):
                        for x in range(x_l, x_r):
                            print(grid.get((x, y), '#'), end='')
                        print()
                    if chars_index == chars_length:
                        turns += 1
                    print(turns)
                    for kls, hp in chars.values():
                        print(kls, hp)
                    print((turns) * (sum((x[1] for x in chars.values()))))
                    return
            else:
                chars[m_x, m_y] = e_c, hp - att
        turns += 1


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
