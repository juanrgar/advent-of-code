use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut scores_shape: Vec<i32> = Vec::new();
    let mut scores_outcome: Vec<i32> = Vec::new();

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            let l = line.unwrap();
            let mut shapes = l.split_whitespace();
            let other = shapes.next().unwrap();
            let me = shapes.next().unwrap();
            let score_shape = match other {
                "A" => {
                    let s = match me {
                        "X" => 1 + 3,
                        "Y" => 2 + 6,
                        "Z" => 3 + 0,
                        _ => 0
                    };
                    s
                },
                "B" => {
                    let s = match me {
                        "X" => 1 + 0,
                        "Y" => 2 + 3,
                        "Z" => 3 + 6,
                        _ => 0
                    };
                    s
                },
                "C" => {
                    let s = match me {
                        "X" => 1 + 6,
                        "Y" => 2 + 0,
                        "Z" => 3 + 3,
                        _ => 0
                    };
                    s
                },
                _ => 0
            };
            scores_shape.push(score_shape);
            let score_outcome = match other {
                "A" => { // Rock
                    let s = match me {
                        "X" => 3 + 0, // Loose: scissors
                        "Y" => 1 + 3, // Draw: rock
                        "Z" => 2 + 6, // Win: paper
                        _ => 0
                    };
                    s
                },
                "B" => { // Paper
                    let s = match me {
                        "X" => 1 + 0, // Loose: rock
                        "Y" => 2 + 3, // Draw: paper
                        "Z" => 3 + 6, // Win: scissors
                        _ => 0
                    };
                    s
                },
                "C" => { // Scissors
                    let s = match me {
                        "X" => 2 + 0, // Loose: paper
                        "Y" => 3 + 3, // Draw: scissors
                        "Z" => 1 + 6, // Win: rock
                        _ => 0
                    };
                    s
                },
                _ => 0
            };
            scores_outcome.push(score_outcome);
        }
    }
    let s: i32 = scores_shape.iter().sum();
    println!("{}", s);
    let s: i32 = scores_outcome.iter().sum();
    println!("{}", s);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
