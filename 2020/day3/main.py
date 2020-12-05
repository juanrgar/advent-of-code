#!/usr/bin/env python3

import sys

def build_area_map(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    area_map = list()
    for l in lines:
        area_map.append(list())
        for c in l:
            area_map[-1].append(c)

    return (area_map, len(lines[0]), len(lines))

def count_trees(slope):
    t = 0
    pos = (0, 0)
    t += visit_pos(pos)
    return t

def visit_pos(pos, area_map):
    if get_item(pos) == '#':
        return 1
    return 0

def get_item(pos, area_map):
    return area_map[pos[1]][pos[0]];

def main():
    filename = sys.argv[1]
    (area_map, w, h) = build_area_map(filename)
    trees = count_trees((3, -1))
    print(trees)

if __name__ == "__main__":
    main()
