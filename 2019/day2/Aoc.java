
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
	List<Integer> program = readProgram(args[1]);
	System.out.println("Program size: " + program.size());

	IntcodeCpu cpu = new IntcodeCpu();

	cpu.writeProgMemory(program);

	/* before running the program, replace position 1 with the
	   value 12 and replace position 2 with the value 2. */
	cpu.writeProgMemory(1, 12);
	cpu.writeProgMemory(2, 2);

	cpu.run();

	System.out.println(Integer.toString(cpu.readProgMemory(0)));
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
}
