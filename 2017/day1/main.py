#!/usr/bin/env python

import sys

class WrapAroundArray(object):
    def __init__(self, items):
        self._items = items
        self._nb_items = len(items)

    def __getitem__(self, key):
        while key >= self._nb_items:
            key -= self._nb_items
        return self._items[key]

def main(args):
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(-1)

    filename = sys.argv[1]
    part = int(sys.argv[2])

    f = open(filename, "r")
    data = f.read().rstrip()
    f.close()

    data_list = [int(x) for x in list(data)]
    darray = WrapAroundArray(data_list)

    darray_idx = 0
    darray_sum = 0
    offset = 1

    while darray_idx < len(data_list):
        a = darray[darray_idx]
        b = darray[darray_idx + offset]

        if a == b:
            darray_sum += a

        darray_idx += 1

    print darray_sum

if __name__ == "__main__":
    main(sys.argv)
