#!/usr/bin/env python

import sys

def print_usage():
    print "main.py <filename> <part>"

def diff_min_max(row):
    max_elem = row[0]
    min_elem = row[0]

    for elem in row[1:]:
        if elem > max_elem:
            max_elem = elem
        if elem < min_elem:
            min_elem = elem

    return max_elem - min_elem

def even_div(row):
    print row
    row_len = len(row)
    for idx, elem_a in enumerate(row):
        if idx < row_len - 1:
            for elem_b in row[idx+1:]:
                rem = elem_a % elem_b
                if rem == 0:
                    print elem_a
                    print elem_b
                    return elem_a / elem_b
                rem = elem_b % elem_a
                if rem == 0:
                    print elem_a
                    print elem_b
                    return elem_b / elem_a
    return 0

def main(args):
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(-1)

    filename = sys.argv[1]
    part = int(sys.argv[2])

    f = open(filename, "r")
    spreadsheet = f.readlines()
    f.close()

    res = 0

    for row_str in spreadsheet:
        row = row_str.split()
        row = [int(x) for x in row]
        if part == 1:
            res += diff_min_max(row)
        elif part == 2:
            res += even_div(row)

    print res

if __name__ == "__main__":
    main(sys.argv)
