#!/usr/bin/env python3

import sys

def part1(args):
    filename = sys.argv[1]

    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    count_two_occur = 0
    count_three_occur = 0

    for l in lines:
        letter_count = dict()
        for c in l.strip():
            if c in letter_count:
                letter_count[c] += 1
            else:
                letter_count[c] = 1
        count_two = False
        count_three = False
        for c, count in letter_count.items():
            if count == 2 and not count_two:
                count_two = True
            elif count == 3 and not count_three:
                count_three = True
        if count_two:
            count_two_occur += 1
        if count_three:
            count_three_occur += 1

    print(str(count_two_occur))
    print(str(count_three_occur))

    chk = count_two_occur * count_three_occur
    print(str(chk))

def part2_distance(id1, id2):
    d = 0
    pos = list()

    id1len = len(id1)
    id2len = len(id2)

    if id1len == id2len:
        for i in range(id1len):
            if id1[i] != id2[i]:
                d += 1
                pos.append(i)

    return (d, pos)

def part2(args):
    filename = sys.argv[1]

    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    lines_len = len(lines)
    id_found = False
    i = 0
    j = 0

    while (not id_found) and (i < lines_len):
        j = i + 1
        while (not id_found) and (j < lines_len):
            w1 = lines[i].strip()
            w2 = lines[j].strip()
            (d, pos) = part2_distance(w1, w2)
            if d == 1:
                id = w1[:pos[0]] + w1[pos[0]+1:]
                print(w1)
                print(w2)
                print(id)
                id_found = True
            j += 1
        i += 1

if __name__ == "__main__":
    # part1(sys.argv)
    part2(sys.argv)