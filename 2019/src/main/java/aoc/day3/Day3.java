
package aoc.day3;

import aoc.DayX;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Day3 implements DayX {

    private List<List<Integer>> wires;

    public int run(String[] args) {
	this.wires = new ArrayList<>();

	readPaths(args[1]);

	return 0;
    }

    private void readPaths(String filename) {
	try {
	    Reader reader = new FileReader(filename); // throws FileNotFoundException
	    BufferedReader bufReader = new BufferedReader(reader);

	    String line;

	    while ((line = bufReader.readLine()) != null) { // throws IOException
		List<Integer> wire = readPath(line);
		this.wires.add(wire);
	    }

	    bufReader.close();
	} catch (FileNotFoundException e) {
	    System.out.println("File not found: " + filename);
	    System.exit(-2);
	} catch (IOException e) {
	    System.out.println("Error reader line");
	    System.exit(-3);
	}
    }

    private List<Integer> readPath(String line) {
	List<Integer> wire = new ArrayList<>();

	StringTokenizer tokenizer = new StringTokenizer();

	return wire;
    }
}
