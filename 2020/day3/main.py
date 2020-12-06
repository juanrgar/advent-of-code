#!/usr/bin/env python3

import sys

def build_area_map(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    area_map = list()
    for l in lines:
        l = l.strip()
        area_map.append(list())
        for c in l:
            area_map[-1].append(c)

    return (area_map, len(area_map[0]), len(lines))

def count_trees(area_map, w, h, slope):
    t = 0
    pos = (0, 0)

    while pos[1] < h:
        t += visit_pos(area_map, w, h, pos)
        pos = next_pos(pos, slope)

    return t

def visit_pos(area_map, w, h, pos):
    if get_item(area_map, w, h, pos) == '#':
        return 1
    return 0

def get_item(area_map, w, h, pos):
    x = pos[0] % w
    return area_map[pos[1]][x]

def next_pos(pos, slope):
    return (pos[0] + slope[0], pos[1] + slope[1])

def print_area_map(area_map, w, h):
    for r in area_map:
        for c in r:
            print(c, end='')
        print('')

def main():
    filename = sys.argv[1]
    (area_map, w, h) = build_area_map(filename)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    acc = 1
    for s in slopes:
        trees = count_trees(area_map, w, h, s)
        acc *= trees
    print(acc)

if __name__ == "__main__":
    main()
