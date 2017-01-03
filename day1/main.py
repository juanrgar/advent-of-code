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

POINTINGS_CW = ["up", "right", "down", "left"]
POINTINGS_CCW = ["up", "left", "down", "right"]

def compute_next_pointing(pointing, turn):
    pointings = None

    if turn == "L":
        pointings = POINTINGS_CW
    elif turn == "R":
        pointings = POINTINGS_CCW

    pointing_index = pointings.index(pointing)
    new_pointing_index = (pointing_index + 1) % 4
    return pointings[new_pointing_index]

def compute_next_position(positions, pointing, count):
    cur_position = positions[-1]
    cur_x = cur_position.x
    cur_y = cur_position.y

    if pointing == "up":
        target_y = cur_y + count
        cur_y = cur_y + 1
        while cur_y <= target_y:
            pos = Position(cur_x, cur_y)
            print pos
            positions.append(pos)
            cur_y = cur_y + 1
    elif pointing == "down":
        target_y = cur_y - count
        cur_y = cur_y - 1
        while cur_y >= target_y:
            pos = Position(cur_x, cur_y)
            print pos
            positions.append(pos)
            cur_y = cur_y - 1
    elif pointing == "right":
        target_x = cur_x + count
        cur_x = cur_x + 1
        while cur_x <= target_x:
            pos = Position(cur_x, cur_y)
            print pos
            positions.append(pos)
            cur_x = cur_x + 1
    elif pointing == "left":
        target_x = cur_x - count
        cur_x = cur_x - 1
        while cur_x >= target_x:
            pos = Position(cur_x, cur_y)
            print pos
            positions.append(pos)
            cur_x = cur_x - 1

def compute_first_revisited_position(positions):
    visited_positions = list()
    for p in positions:
        if p in visited_positions:
            return p
        else:
            visited_positions.append(p)

def main(args):
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(-1)

    positions = list()
    pointing = "up"

    positions.append(Position(0, 0))

    filename = sys.argv[1]
    part = int(sys.argv[2])

    f = open(filename, "r")
    idata = f.read()
    f.close()

    movs = idata.rstrip().split(", ")
    # print movs

    for m in movs:
        d = m[0]
        c = int(m[1:])

        print m

        pointing = compute_next_pointing(pointing, d)
        compute_next_position(positions, pointing, c)

        # print pointing
        # print positions[-1]

    target = None
    if part == 1:
        target = positions[-1]
    elif part == 2:
        target = compute_first_revisited_position(positions)

    if target:
        distance = target.compute_rectilinear_distance(Position(0, 0))
        print distance

if __name__ == "__main__":
    main(sys.argv)
