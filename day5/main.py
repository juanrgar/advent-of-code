#!/usr/bin/env python

import sys
import md5

def print_usage():
    print "main.py <input-file> <1|2>"

def get_next_char(door_id, index):
    next_char = ""
    hash_found = False

    while not hash_found:
        door_id_index = door_id + str(index)
        m = md5.new(door_id_index)
        digest = m.hexdigest()

        prefix = int(digest[:5], 16)
        if prefix == 0:
            hash_found = True
            next_char = digest[5]
#            print index
#            print digest
        index = index + 1

    return (next_char, index)

def get_password(door_id):
    index = 0
    password = ""
    while len(password) != 8:
        (next_char, index) = get_next_char(door_id, index)
        password = password + next_char

    return password

def main(args):
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(-1)

    filename = sys.argv[1]
    f = open(filename, "r")
    idata = f.readlines()
    f.close()

    for l in idata:
        door_id = l.rstrip()
        password = get_password(door_id)
        print password

if __name__ == "__main__":
    main(sys.argv)
