#!/usr/bin/env python3

import sys

class AreaMap(object):
    pass

def build_area_map(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    area_map = list()
    for l in lines:
        area_map.append(list())
        for c in l:
            area_map[-1].append(c)

    return (area_map, len(lines[0]), len(lines))

def count_trees(area_map, w, h, slope):
    t = 0
    pos = (0, 0)

    while pos[1] <= h:
        t += visit_pos(area_map, pos)
        pos = next_pos(pos, slope)

    return t

def visit_pos(area_map, pos):
    if get_item(pos) == '#':
        return 1
    return 0

def get_item(area_map, pos):
    # TODO

    return area_map[pos[1]][pos[0]]

def next_pos(pos, slope):
    return (pos[0] + slope[0], pos[1] + slope[1])

def main():
    filename = sys.argv[1]
    (area_map, w, h) = build_area_map(filename)
    print(w)
    print(h)
    trees = count_trees((3, -1))
    print(trees)

if __name__ == "__main__":
    main()
