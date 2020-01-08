
package aoc.day3;

import aoc.DayX;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Day3 implements DayX {

    private class Position {
        private int x;
        private int y;

        public Position(int x, int y) {
            this.setX(x);
            this.setY(y);
        }

        public Position(final Position pos) {
            this.setX(pos.getX());
            this.setY(pos.getY());
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

        public int modX(int dx) {
            this.setX(this.getX() + dx);

            return this.getX();
        }

        public int modY(int dy) {
            this.setY(this.getY() + dy);

            return this.getY();
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }

            if (o == null) {
                return false;
            }

            if (this.getClass() != o.getClass()) {
                return false;
            }

            Position pos = (Position) o;

            return (this.getX() == pos.getX()) && (this.getY() == pos.getY());
        }

        @Override
        public String toString() {
            return "(" + this.getX() + ", " + this.getY() + ")";
        }
    }

    private List<List<Position>> wires;

    public int run(String[] args) {
        this.wires = new ArrayList<>();

        this.readPaths(args[1]);

        List<Position> intersect = this.findIntersections();
        System.out.println("Intersections: " + intersect.size());

        List<Integer> intersectDist = this.getManhattanDistances(intersect);

        int minValue = 0;
        int minIndex = -1;

        for (int i = 0; i < intersectDist.size(); i++) {
            int val = intersectDist.get(i);
            if (minIndex < 0) {
                minValue = val;
                minIndex = i;
            } else if (val < minValue) {
                minValue = val;
                minIndex = i;
            }
        }

        System.out.println(Integer.toString(minValue));

        return 0;
    }

    private void readPaths(String filename) {
        try {
            Reader reader = new FileReader(filename); // throws FileNotFoundException
            BufferedReader bufReader = new BufferedReader(reader);

            String line;

            while ((line = bufReader.readLine()) != null) { // throws IOException
                List<Position> wire = this.readPath(line);
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

        System.out.println("Initialized wire");

        StringTokenizer tokenizer = new StringTokenizer(line, ",");

        while (tokenizer.hasMoreTokens()) {
            String tok = tokenizer.nextToken();
            curPos = this.moveWire(tok, curPos, wire);
        }

        return wire;
    }

    private Position moveWire(final String mov,
                              final Position curPos,
                              List<Position> wire) {
        char dir = mov.charAt(0);
        int len = Integer.parseInt(mov.substring(1));
        Position endPos = new Position(curPos);

        System.out.println("dir: " + dir + "; len: " + Integer.toString(len));

        switch (dir) {
        case 'U':
            endPos.modY(len);
            break;
        case 'D':
            endPos.modY(-1 * len);
            break;
        case 'L':
            endPos.modX(-1 * len);
            break;
        case 'R':
            endPos.modX(len);
            break;
        default:
            break;
        }

        System.out.println("Departing pos: " + curPos.toString());
        System.out.println("Ending pos: " + endPos.toString());

        this.addPointsInBetween(curPos, endPos, wire);
        System.out.println("New wire length: " + wire.size());

        wire.add(endPos);

        System.out.println("New wire length: " + wire.size());

        return endPos;
    }

    private void addPointsInBetween(final Position p1,
                                    final Position p2,
                                    List<Position> wire) {
        if (p1.getX() == p2.getX()) {
            if (p1.getY() < p2.getY()) {
                for (int y = p1.getY() + 1; y != p2.getY(); y++) {
                    Position p = new Position(p1.getX(), y);
                    System.out.println(p);
                    wire.add(p);
                }
            } else {
                for (int y = p1.getY() - 1; y != p2.getY(); y--) {
                    Position p = new Position(p1.getX(), y);
                    System.out.println(p);
                    wire.add(p);
                }
            }
        } else if (p1.getY() == p2.getY()) {
            if (p1.getX() < p2.getX()) {
                for (int x = p1.getX() + 1; x != p2.getX(); x++) {
                    Position p = new Position(x, p1.getY());
                    System.out.println(p);
                    wire.add(p);
                }
            } else {
                for (int x = p1.getX() - 1; x != p2.getX(); x--) {
                    Position p = new Position(x, p1.getY());
                    System.out.println(p);
                    wire.add(p);
                }
            }
        }
    }

    private List<Position> findIntersections() {
        List<Position> intersect = new ArrayList<Position>();
        int nbWires = this.wires.size();
        boolean wireMatches = true;
        int i = 0;

        List<Position> refWire = this.wires.get(0);
        System.out.println("Ref wire length " + refWire.size());
        for (Position p : refWire) {
            System.out.println("Comparing against " + p);
            i = 1;
            while (wireMatches && (i < nbWires)) {
                List<Position> wire = this.wires.get(i);
                wireMatches = false;
                System.out.println("Wire length " + wire.size());
                for (Position pp : wire) {
                    System.out.println(p + " <> " + pp);
                    if (p.equals(pp)) {
                        wireMatches = true;
                        break;
                    }
                }

                if (wireMatches) {
                    i++;
                }
            }

            if (i == nbWires) {
                intersect.add(p);
            }
        }

        return intersect;
    }

    private List<Integer> getManhattanDistances(final List<Position> positions) {
        return positions
            .stream()
            .map(p -> Math.abs(p.getX()) + Math.abs(p.getY()))
            .collect(Collectors.toList());
    }
}
