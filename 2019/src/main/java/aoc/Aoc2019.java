
package aoc;

import aoc.DayX;

import aoc.day1.Day1;
import aoc.day2.Day2;

public class Aoc2019 {
    public static void main(String[] args) {
	if (args.length == 0) {
	    System.exit(-1);
	}

	int day = Integer.parseInt(args[0]);

	DayX dayX = null;
	String[] dayArgs = null;
	if (args.length > 0) {
	    dayArgs = new String[args.length - 1];
	    for (int i = 1; i < args.length; i++) {
		dayArgs[i - 1] = args[i];
	    }
	}

	switch (day) {
	case 1:
	    dayX = new Day1();
	    break;
	case 2:
	    dayX = new Day2();
	    break;
	case 3:
	    break;
	default:
	    break;
	}

	if (dayX != null) {
	    dayX.run(dayArgs);
	}
    }
}
