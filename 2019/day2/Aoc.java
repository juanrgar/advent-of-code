
package day2;

import java.io.FileReader;
import java.io.StreamTokenizer;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;

import aoc.IntcodeCpu;

public class Aoc {

    public static void main(String[] args) {
	if (args.length != 2) {
	    Aoc.printUsage();
	    System.exit(-1);
	}

	Aoc aoc = new Aoc();
	aoc.run(args);
    }

    private static void printUsage() {
	System.out.println("aoc <1|2> <input_file>");
    }

    private void run(String[] args) {
	int part = Integer.parseInt(args[0]);
	List<Integer> program = readProgram(args[1]);

	IntcodeCpu cpu = new IntcodeCpu();

	if (part == 1) {
	    int res = runWithNounAndVerb(cpu, program, 12, 2);

	    System.out.println(res);
	} else if (part == 2) {
	    for (int noun = 0; noun < 100; noun++) {
		for (int verb = 0; verb < 100; verb++) {
		    int res = runWithNounAndVerb(cpu, program, noun, verb);
		    if (res == 19690720) {
			System.out.println("Found; noun = " + noun + " verb = " + verb);
			break;
		    }
		}
	    }
	}
    }

    private List<Integer> readProgram(final String filename) {
	List<Integer> program = null;

	try {
	    Reader reader = new FileReader(filename); // throws FileNotFoundException
	    StreamTokenizer tokenizer = new StreamTokenizer(reader);

	    program = new ArrayList<Integer>();

	    while (tokenizer.nextToken() != StreamTokenizer.TT_EOF) {
		if (tokenizer.ttype == StreamTokenizer.TT_NUMBER) {
		    program.add((int) tokenizer.nval);
		}
	    }
	} catch (FileNotFoundException e) {
	    System.out.println("File not found: " + filename);
	    System.exit(-2);
	} catch (IOException e) {
	    System.out.println("Error reader line");
	    System.exit(-3);
	}

	return program;
    }

    private int runWithNounAndVerb(IntcodeCpu cpu,
				   final List<Integer> program,
				   int noun,
				   int verb) {
	cpu.writeMemory(program);

	cpu.writeMemory(1, noun);
	cpu.writeMemory(2, verb);

	cpu.reset();
	cpu.run();

	return cpu.readMemory(0);
    }
}
