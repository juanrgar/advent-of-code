
package aoc.day1;

import aoc.DayX;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Day1 implements DayX {

    private final double DIV_FACTOR = 3.0;
    private final double SUB_FACTOR = 2.0;

    public int run(String[] args) {
	List<Double> masses = readMasses(args[1]);

	if (masses == null) {
	    System.exit(-4);
	}

	boolean useFuelMass = Integer.parseInt(args[0]) == 2;

	double fuel = computeFuel(masses, useFuelMass);

	System.out.println(Double.toString(fuel));

	return 0;
    }

    private List<Double> readMasses(final String filename) {
	List<Double> masses = null;

	try {
	    Reader reader = new FileReader(filename); // throws FileNotFoundException
	    BufferedReader bufReader = new BufferedReader(reader);

	    masses = new ArrayList<Double>();
	    String line;

	    while ((line = bufReader.readLine()) != null) { // throws IOException
		masses.add(Double.parseDouble(line));
	    }
	} catch (FileNotFoundException e) {
	    System.out.println("File not found: " + filename);
	    System.exit(-2);
	} catch (IOException e) {
	    System.out.println("Error reader line");
	    System.exit(-3);
	}

	return masses;
    }

    private double computeFuel(final List<Double> masses, boolean useFuelMass) {
	return masses.stream()
	    .map(e -> computeFuelForMass(e, useFuelMass))
	    .reduce(0.0, (e1, e2) -> e1 + e2);
    }

    private double computeFuelForMass(double mass, boolean useFuelMass) {
	double totalFuel = computeFuelForMass(mass);

	if (useFuelMass) {
	    double fuel = 0.0;
	    mass = totalFuel;

	    do {
		totalFuel += fuel;
		fuel = computeFuelForMass(mass);
		mass = fuel;
	    } while (fuel > 0.0);
	}

	return totalFuel;
    }

    private double computeFuelForMass(double mass) {
	return Math.floor(mass / DIV_FACTOR) - SUB_FACTOR;
    }
}
