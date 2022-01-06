use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

struct Point {
    x: u32,
    y: u32
}

struct Segment {
    start: Point,
    end: Point
}

fn main() {
    let mut segments: Vec<Segment> = Vec::new();

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            let segment_line = line.unwrap();
            let mut segment_parts = segment_line.split_whitespace();
            let p0_str = segment_parts.next().unwrap();
            segment_parts.next().unwrap();
            let p1_str = segment_parts.next().unwrap();
            let mut p0_parts = p0_str.split(',');
            let p0 = Point { x: p0_parts.next().unwrap().parse::<u32>().unwrap(),
                             y: p0_parts.next().unwrap().parse::<u32>().unwrap() };
            let mut p1_parts = p1_str.split(',');
            let p1 = Point { x: p1_parts.next().unwrap().parse::<u32>().unwrap(),
                             y: p1_parts.next().unwrap().parse::<u32>().unwrap() };
            segments.push(Segment { start: p0, end: p1 });
        }
    }

    for s in &segments {
        println!("{},{} -> {},{}", s.start.x, s.start.y, s.end.x, s.end.y);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
