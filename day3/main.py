#!/usr/bin/env python

import sys
import re

def print_usage():
    print "main.py <input-file> <1|2>"

def is_possible_triangle(lengths):
    larger = 0

    if lengths[0] + lengths[1] > lengths[2]:
        larger = larger + 1
    if lengths[0] + lengths[2] > lengths[1]:
        larger = larger + 1
    if lengths[1] + lengths[2] > lengths[0]:
        larger = larger + 1

    if larger == 3:
        return True
    else:
        return False

def main(args):
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(-1)

    filename = sys.argv[1]
    part = int(sys.argv[2])

    f = open(filename, "r")
    idata = f.readlines()
    f.close()

    # print idata

    possible_triangles = 0

    if part == 1:
        possible_triangles = do_part_1(idata)
    else:
        possible_triangles = do_part_2(idata)

    print possible_triangles

def do_part_1(idata):
    possible_triangles = 0
    for l in idata:
        l = l.lstrip().rstrip()
        lengths = re.split(" +", l)
        lengths = [int(x) for x in lengths]
        if is_possible_triangle(lengths):
            possible_triangles = possible_triangles + 1

    return possible_triangles

def do_part_2(idata):
    possible_triangles = 0
    col1 = list()
    col2 = list()
    col3 = list()

    for l in idata:
        l = l.lstrip().rstrip()
        lengths = re.split(" +", l)
        lengths = [int(x) for x in lengths]
        col1.append(lengths[0])
        col2.append(lengths[1])
        col3.append(lengths[2])

    cols = [col1, col2, col3]

    for c in cols:
        index = 0
        while index < len(c) - 2:
            triangle = c[index:index + 3]
            if is_possible_triangle(triangle):
                possible_triangles = possible_triangles + 1
            index = index + 3

    return possible_triangles

if __name__ == "__main__":
    main(sys.argv)
