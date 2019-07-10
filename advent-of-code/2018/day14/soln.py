#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from functools import lru_cache, wraps
from itertools import combinations, permutations
from math import floor, sqrt


class DoublyLinkedList(object):
    def __init__(self, value, previous_node=None, next_node=None):
        self.value = value
        self.previous = previous_node
        if previous_node is not None:
            self.previous.next = self
        self.next = next_node
        if next_node is not None:
            self.next.previous = self

    def insert_after(self, v):
        node = DoublyLinkedList(v, self, self.next)
        return node

    def remove_after(self):
        self.next = self.next.next
        return self.next


def a(recipes):
    return
    root = DoublyLinkedList(3)
    root.next = root
    root.previous = root
    end = root.insert_after(7)
    loc1 = root
    loc2 = root.next

    left = recipes + 8
    result = ''
    while left >= 0:
        new_score = loc1.value + loc2.value
        for i in str(new_score):
            end = end.insert_after(int(i))
            end.next = root
            root.previous = end
            if 0 < left <= 10:
                result += i
            left -= 1
        for i in range(loc1.value + 1):
            loc1 = loc1.next
        for i in range(loc2.value + 1):
            loc2 = loc2.next

        # loc = root
        # seen = set()
        # s = []
        # while loc not in seen:
        #     seen.add(loc)
        #     if loc == loc1:
        #         s.append('({})'.format(loc.value))
        #     elif loc == loc2:
        #         s.append('[{}]'.format(loc.value))
        #     else:
        #         s.append(' {} '.format(loc.value))
        #     loc = loc.next
        # print(''.join((str(i) for i in s)))

    print(result)


def b(lines):
    root = DoublyLinkedList(3)
    root.next = root
    root.previous = root
    end = root.insert_after(7)
    loc1 = root
    loc2 = root.next

    goal = deque((int(i) for i in str(lines)))
    g_l = len(goal)
    current = deque((int(root.value), int(end.value)))

    recipes = 0
    while True:
        new_score = loc1.value + loc2.value
        for i in str(new_score):
            end = end.insert_after(int(i))
            end.next = root
            root.previous = end
            recipes += 1
            loc = end
            current.append(loc.value)
            if len(current) > g_l:
                current.popleft()
            if current == goal:
                print(goal, recipes - g_l + 2)
                return

        for i in range(loc1.value + 1):
            loc1 = loc1.next
        for i in range(loc2.value + 1):
            loc2 = loc2.next

        # loc = root
        # seen = set()
        # s = []
        # while loc not in seen:
        #     seen.add(loc)
        #     if loc == loc1:
        #         s.append('({})'.format(loc.value))
        #     elif loc == loc2:
        #         s.append('[{}]'.format(loc.value))
        #     else:
        #         s.append(' {} '.format(loc.value))
        #     loc = loc.next
        # print(''.join((str(i) for i in s)))


lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(int(lines[0]))
b(int(lines[0]))
