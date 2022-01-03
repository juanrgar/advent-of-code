use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

const NCOLS: usize = 5;
const NROWS: usize = 5;

struct BoardNum {
    number: u32,
    checked: bool
}

struct Board {
    numbers: Vec<BoardNum>,
    won: bool
}

impl Board {
    fn check_num(&mut self, num: u32) -> bool {
        for i in 0..NROWS as usize {
            for j in 0..NCOLS as usize {
                let e = &mut self.numbers[i * NCOLS + j];
                if !e.checked && (e.number == num) {
                    e.checked = true;
                    return true;
                }
            }
        }
        false
    }

    fn check_cols(&mut self) -> bool {
        for j in 0..NCOLS as usize {
            let mut res = true;
            for i in 0..NROWS as usize {
                res = res && self.numbers[i * NCOLS + j].checked;
            }
            if res {
                return true;
            }
        }
        false
    }

    fn check_rows(&mut self) -> bool {
        for i in 0..NROWS as usize {
            let mut res = true;
            for j in 0..NCOLS as usize {
                res = res && self.numbers[i * NCOLS + j].checked;
            }
            if res {
                return true;
            }
        }
        false
    }

    fn sum_unchecked(&self) -> u32 {
        let mut sum = 0;

        for i in 0..NROWS as usize {
            for j in 0..NCOLS as usize {
                let e = &self.numbers[i * NCOLS + j];
                if !e.checked {
                    sum += e.number;
                }
            }
        }

        sum
    }
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
                    numbers: Vec::new(),
                    won: false
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

    for n in numbers {
        for b in boards.iter_mut() {
            if !b.won {
                if b.check_num(n) {
                    if b.check_cols() {
                        println!("full col");
                        let s = b.sum_unchecked() * n;
                        println!("{}", s);
                        b.won = true;
                    }
                    if b.check_rows() {
                        println!("full row");
                        let s = b.sum_unchecked() * n;
                        println!("{}", s);
                        b.won = true;
                    }
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
