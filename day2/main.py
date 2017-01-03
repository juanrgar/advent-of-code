#!/usr/bin/env python

import sys

class Position:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def compute_rectilinear_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

def print_usage():
    print "main.py <input-file> <1|2>"

def compute_next_position(positions, seq, keypad):
    cur_position = positions[-1]
    cur_x = cur_position.x
    cur_y = cur_position.y
    new_position = Position(cur_x, cur_y)

    for c in seq:
        if keypad == 1:
            compute_next_position_keypad1(new_position, c)
        elif keypad == 2:
            compute_next_position_keypad2(new_position, c)

    positions.append(new_position)

def compute_next_position_keypad1(pos, move):
    if move == 'U':
        if pos.y > 0:
            pos.y = pos.y - 1
    elif move == 'D':
        if pos.y < 2:
            pos.y = pos.y + 1
    elif move == 'L':
        if pos.x > 0:
            pos.x = pos.x - 1
    elif move == 'R':
        if pos.x < 2:
            pos.x = pos.x + 1

def compute_next_position_keypad2(pos, move):
    if move == 'U':
        if pos.x == 1 or pos.x == 3:
            if pos.y > 1:
                pos.y = pos.y - 1
        elif pos.x == 2:
            if pos.y > 0:
                pos.y = pos.y - 1
    elif move == 'D':
        if pos.x == 1 or pos.x == 3:
            if pos.y < 3:
                pos.y = pos.y + 1
        elif pos.x == 2:
            if pos.y < 4:
                pos.y = pos.y + 1
    elif move == 'L':
        if pos.y == 1 or pos.y == 3:
            if pos.x > 1:
                pos.x = pos.x - 1
        elif pos.y == 2:
            if pos.x > 0:
                pos.x = pos.x - 1
    elif move == 'R':
        if pos.y == 1 or pos.y == 3:
            if pos.x < 3:
                pos.x = pos.x + 1
        elif pos.y == 2:
            if pos.x < 4:
                pos.x = pos.x + 1

KEYPAD_1 = "123456789"
KEYPAD_2 = "XX1XXX234X56789XABCXXXDXX"

def positions_to_number(positions, keypad):
    nstr = ""
    if keypad == 1:
        for p in positions:
            nstr = nstr + KEYPAD_1[p.x + p.y * 3]
    elif keypad == 2:
        for p in positions:
            nstr = nstr + KEYPAD_2[p.x + p.y * 5]

    return nstr

def main(args):
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(-1)

    filename = sys.argv[1]
    part = int(sys.argv[2])

    positions = list()
    if part == 1:
        positions.append(Position(1, 1))
    else:
        positions.append(Position(0, 2))

    f = open(filename, "r")
    idata = f.readlines()
    f.close()

    # print idata

    for l in idata:
        compute_next_position(positions, l, part)

    nstr = positions_to_number(positions[1:], part)
    print nstr

if __name__ == "__main__":
    main(sys.argv)
