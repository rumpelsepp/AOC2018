#!/usr/bin/python3

import sys


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def nearest_point(points, a):
    dists = []
    for point in points:
        dists.append(distance(a, point))

    n = 0
    min_dist = min(dists)
    for dist in dists:
        if dist == min_dist:
            n += 1

    if n == 1:
        return dists.index(min_dist)
    return None


def dist_sum(points, a):
    dists = []
    for point in points:
        dists.append(distance(a, point))
    return sum(dists)


def calc_occurences(points, start=-500, end=500):
    occurences = {}

    for i in range(start, end):
        for j in range(start, end):
            p = nearest_point(points, (i, j))
            if p:
                if p in occurences:
                    occurences[p] += 1
                else:
                    occurences[p] = 1

    return occurences


def calc_safe_sum(points, start=-500, end=500):
    res = [[dist_sum(points, (i, j)) for j in range(start, end)] for i in range(start, end)]
    sum_ = 0

    for i in range(start, end):
        for j in range(start, end):
            if res[i][j] < 10000:
                sum_ += 1

    return sum_


# This is my awesome parser.
points = list(map(lambda x: (int(x[0]), int(x[1])), [line.strip().replace(' ', '').split(',') for line in sys.stdin.readlines()]))

# No idea how to exactly determine infinite areas.
# Experiments gives me this.
o1 = calc_occurences(points)
o2 = calc_occurences(points, start=-600, end=600)
o_res = {}

for k in o1.keys():
    if o1[k] == o2[k]:
        o_res[k] = o1[k]

print(o_res[max(o_res, key=o_res.get)])
print(calc_safe_sum(points))
