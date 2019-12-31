
package aoc;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Aoc {
    public static void main(String[] args) {
	if (args.length != 1) {
	    return;
	}

	String filename = args[0];

	System.out.println("Reading file " + filename);

	try {
	    Reader reader = new FileReader(filename);

	    BufferedReader bufReader = new BufferedReader(reader);

	    List<Double> masses = new ArrayList<Double>();
	    String line;

	    while ((line = bufReader.readLine()) != null) {
		masses.add(Double.parseDouble(line));
	    }

	    System.out.println("Read " + Integer.toString(masses.size()) + " masses");

	    Double m = masses
		.stream()
		.map((e) -> Math.floor(e / 3.0) - 2.0)
		.reduce(0.0, (e1, e2) -> e1 + e2);
	    System.out.println("Result: " + m);
	} catch (FileNotFoundException e) {
	    System.out.println("File not found: " + filename);
	    return;
	} catch (IOException e) {
	    System.out.println("Error reader line");
	    return;
	}
    }
}
