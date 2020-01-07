
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

    private class Position {
	private int x;
	private int y;

	public Position(int x, int y) {
	    this.setX(x);
	    this.setY(y);
	}

	public int getX() {
	    return x;
	}

	public void setX(int x) {
	    this.x = x;
	}

	public int getY() {
	    return y;
	}

	public void setY(int y) {
	    this.y = y;
	}
    }

    private List<List<Position>> wires;

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
		List<Position> wire = readPath(line);
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

    private List<Position> readPath(String line) {
	Position curPos = new Position(0, 0);
	List<Position> wire = new ArrayList<>();

	StringTokenizer tokenizer = new StringTokenizer(line, ",");

	while (tokenizer.hasMoreTokens()) {
	    String tok = tokenizer.nextToken();
	    curPos = addPoints(tok, curPos, wire);
	}

	return wire;
    }

    private Position addPoints(final String mov,
			       final Position curPos,
			       List<Position> wire) {
	char dir = mov.charAt(0);
	int len = Integer.parseInt(mov.substring(1));

	return curPos;
    }
}
