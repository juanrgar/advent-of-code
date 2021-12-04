use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

enum Direction {
    Forward,
    Down,
    Up
}

struct Command {
    d : Direction,
    n : i32
}

struct Point {
    x : i32,
    y : i32
}

fn main() {
    let mut cmds: Vec<Command> = Vec::new();

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            let lineu = line.unwrap();
            let mut cmd = Command { d : Direction::Forward, n : 0 };
            let mut parts = lineu.split_whitespace();
            cmd.d = match parts.next().unwrap() {
                "forward" => Direction::Forward,
                "down" => Direction::Down,
                "up" => Direction::Up,
                _ => Direction::Forward
            };
            cmd.n = parts.next().unwrap().parse::<i32>().unwrap();
            cmds.push(cmd);
        }
    }

    let mut pos = Point { x : 0, y : 0 };

    for c in cmds {
        match c.d {
            Direction::Forward => pos.x += c.n,
            Direction::Down => pos.y += c.n,
            Direction::Up => pos.y -= c.n,
        }
    }

    println!("{}", pos.x * pos.y);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
