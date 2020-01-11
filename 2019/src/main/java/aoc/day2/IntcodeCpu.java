
package aoc.day2;

import java.util.ArrayList;
import java.util.List;

public class IntcodeCpu {
    private int pc;
    private List<Integer> memory;
    private boolean halted;

    public IntcodeCpu() {
	this.pc = 0;
	this.memory = new ArrayList<Integer>();
	this.halted = false;
    }

    public void writeMemory(final List<Integer> memory) {
	if (!this.memory.isEmpty()) {
	    this.memory.clear();
	}

	this.memory.addAll(memory);
    }

    public void writeMemory(int pos,
			    int val) {
	if (this.memory.size() > pos) {
	    this.memory.set(pos, val);
	}
    }

    public int readMemory(int pos) {
	int data = -1;

	if (this.memory.size() > pos) {
	    data = this.memory.get(pos);
	}

	return data;
    }

    public int getPc() {
	return this.pc;
    }

    public void incPc() {
	this.pc++;
    }

    public void reset() {
	this.pc = 0;
	this.halted = false;
    }

    public void run() {
	while (!this.isHalted()) {
	    int opcode = this.fetchMemory();
	    switch (opcode) {
	    case 1:
		add();
		break;
	    case 2:
		mul();
		break;
	    case 99:
		halt();
		break;
	    }
	}
    }

    private int fetchMemory() {
	int data = readMemory(this.getPc());
	this.incPc();

	return data;
    }

    public boolean isHalted() {
	return this.halted;
    }

    private void add() {
	int op1 = this.readMemory(this.fetchMemory());
	int op2 = this.readMemory(this.fetchMemory());
	int resPos = this.fetchMemory();

	int res = op1 + op2;

	this.writeMemory(resPos, res);
    }

    private void mul() {
	int op1 = this.readMemory(this.fetchMemory());
	int op2 = this.readMemory(this.fetchMemory());
	int resPos = this.fetchMemory();

	int res = op1 * op2;

	this.writeMemory(resPos, res);
    }

    private void halt() {
	this.halted = true;
    }
}
