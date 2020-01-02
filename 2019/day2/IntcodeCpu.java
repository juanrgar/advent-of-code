
package aoc;

import java.util.ArrayList;
import java.util.List;

public class IntcodeCpu {
    private int pc;
    private List<Integer> progMemory;
    private boolean halted;

    public IntcodeCpu() {
	this.pc = 0;
	this.progMemory = null;
	this.halted = false;
    }

    public void writeProgMemory(final List<Integer> memory) {
	this.progMemory = new ArrayList<Integer>(memory);
    }

    public int readProgMemory(int pos) {
	int data = -1;

	if (this.progMemory != null) {
	    if (this.progMemory.size() > pos) {
		data = this.progMemory.get(pos);
	    }
	}

	return data;
    }

    public void writeProgMemory(int pos, int val) {
	if (this.progMemory.size() > pos) {
	    this.progMemory.set(pos, val);
	}
    }

    public int getPc() {
	return this.pc;
    }

    public void incPc() {
	this.pc++;
    }

    public void reset() {
	this.pc = 0;
    }

    public void run() {
	while (!this.isHalted()) {
	    int opcode = this.fetchProgMemory();
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

    private int fetchProgMemory() {
	int data = readProgMemory(this.getPc());
	this.incPc();

	return data;
    }

    public boolean isHalted() {
	return this.halted;
    }

    private void add() {
	int op1 = this.readProgMemory(this.fetchProgMemory());
	int op2 = this.readProgMemory(this.fetchProgMemory());
	int resPos = this.fetchProgMemory();

	int res = op1 + op2;

	this.writeProgMemory(resPos, res);
    }

    private void mul() {
	int op1 = this.readProgMemory(this.fetchProgMemory());
	int op2 = this.readProgMemory(this.fetchProgMemory());
	int resPos = this.fetchProgMemory();

	int res = op1 * op2;

	this.writeProgMemory(resPos, res);
    }

    private void halt() {
	this.halted = true;
    }
}
