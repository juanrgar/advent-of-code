use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

struct BoardNum {
    number: u32,
    checked: bool
}

struct Board {
    numbers: Vec<BoardNum>
}

fn main() {
    let mut numbers: Vec<u32> = Vec::new();
    let mut boards: Vec<Board> = Vec::new();
//    let mut boards: Vec<Vec<u32>> = Vec::new();

    if let Ok(mut lines) = read_lines("input.txt") {
        let numbers_line = lines.next().unwrap().unwrap();
        let numbers_str = numbers_line.split(',');
        for n in numbers_str {
            numbers.push(n.parse::<u32>().unwrap());
        }

        loop {
            let lit = lines.next();
            if lit.is_none() {
                boards.pop();
                break;
            }

            let line = lit.unwrap().unwrap();
            if line.len() == 0 {
                boards.push(Board {
                    numbers: Vec::new()
                });
            } else {
                let board_numbers = line.split_whitespace();
                for n in board_numbers {
                    let board = boards.last_mut().unwrap();
                    board.numbers.push(BoardNum {
                        number: n.parse::<u32>().unwrap(),
                        checked: false
                    });
                }
            }
        }
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
