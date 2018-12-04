#!/usr/bin/env python3
import fileinput
from collections import Counter, defaultdict
from datetime import datetime, timedelta


def a(lines):
    guards = defaultdict(Counter)
    lines = sorted(lines)
    g = None
    s = None
    e = None
    mx_g = None
    mx = 0
    for i, line in enumerate(lines):
        dt, _, line = line.partition("] ")
        if "begins shift" in line:
            g, _, line = line.partition(" #")
            g, _, line = line.partition(" ")
        elif "falls asleep" in line:
            s = dt[1:]
        else:
            e = dt[1:]
            # print("Guard #{} slept from {} until {}".format(g, s, e))
            s = datetime.strptime(s, "%Y-%m-%d %H:%M")
            e = datetime.strptime(e, "%Y-%m-%d %H:%M")
            td = e - s
            ss = s
            for i in range(int(td.total_seconds() / 60)):
                s = ss + timedelta(minutes=i)
                guards[g][s.minute] += 1
            sm = sum(guards[g].values())
            if sm > mx:
                mx_g = g
                mx = sm
    mx_v = max(guards[mx_g].values())
    mx_k = [(k) for k, v in guards[mx_g].items() if v == mx_v]
    # print()
    # print(mx_g)
    # print(mx_k, mx)
    print("1:", int(mx_g) * int(mx_k[0]))


def b(lines):
    guards = defaultdict(Counter)
    lines = sorted(lines)
    g = None
    s = None
    e = None
    for i, line in enumerate(lines):
        dt, _, line = line.partition("] ")
        if "begins shift" in line:
            g, _, line = line.partition(" #")
            g, _, line = line.partition(" ")
        elif "falls asleep" in line:
            s = dt[1:]
        else:
            e = dt[1:]
            s = datetime.strptime(s, "%Y-%m-%d %H:%M")
            e = datetime.strptime(e, "%Y-%m-%d %H:%M")
            td = e - s
            ss = s
            for i in range(int(td.total_seconds() / 60)):
                s = ss + timedelta(minutes=i)
                guards[g][s.minute] += 1

    mx_g = None
    mx_m = None
    mx = 0
    
    for g, m in guards.items():
        for k, v in m.items():
            if v > mx:
                mx_g = g
                mx_m = k
                mx = v
    # print()
    # print(mx_g, mx_m, mx)
    print("2:", int(mx_g) * int(mx_m))



lines = []
for line in fileinput.input():
    lines.append(line.strip())


a(lines)
b(lines)
