#!/usr/bin/env python3

import sys

class Instruction(object):
    def __init__(self) -> None:
        super().__init__()
        self.opcode = ''
        self.arg = 0

    def __str__(self) -> str:
        return self.opcode + ' ' + str(self.arg)

def read_program(filename):
    prog = list()
    with open(filename, 'r') as f:
        for l in f.readlines():
            op_parts = l.split(' ')
            i = Instruction()
            i.opcode = op_parts[0]
            i.arg = int(op_parts[1])
            prog.append(i)

    return prog

def exec_program(prog):
    for i in prog:
        print(i)

def main():
    filename = sys.argv[1]
    prog = read_program(filename)
    exec_program(prog)

if __name__ == "__main__":
    main()
