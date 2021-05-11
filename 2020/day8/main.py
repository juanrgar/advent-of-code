#!/usr/bin/env python3

import copy
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
    pc_hist = list()
    pc = 0
    acc = 0
    while True:
        pc_hist.append(pc)
        i = prog[pc]
        if i.opcode == 'nop':
            pc += 1
        elif i.opcode == 'acc':
            acc += i.arg
            pc += 1
        elif i.opcode == 'jmp':
            pc += i.arg
        if pc in pc_hist:
            print('Infinite loop ' + str(acc))
            return
        if pc >= len(prog):
            print('Program finished ' + str(acc))
            return

def create_alt_programs(prog):
    inst_changed = list()
    progs = list()
    for pc in range(len(prog)):
        if prog[pc].opcode == 'nop':
            p = copy.deepcopy(prog)
            p[pc].opcode = 'jmp'
            progs.append(p)
        elif prog[pc].opcode == 'jmp':
            p = copy.deepcopy(prog)
            p[pc].opcode = 'nop'
            progs.append(p)
    return progs

def main():
    filename = sys.argv[1]
    prog = read_program(filename)
    exec_program(prog)
    progs = create_alt_programs(prog)
    for p in progs:
        exec_program(p)

if __name__ == "__main__":
    main()
