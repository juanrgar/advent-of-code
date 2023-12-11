use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


struct Pos {
    row: u32,
    col: u32
}

struct NumPos {
    num: u32,
    pos: Pos,
    len: u32
}

fn main() {
    let mut acc = 0;

    let mut numbers: Vec<NumPos> = Vec::new();
    let mut symbols: Vec<Pos> = Vec::new();

    let mut row: u32 = 0;

    let mut in_number: bool = false;
    let mut number_str: String = String::new();

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            let l = line.unwrap();
            println!("{}", l);

            // End of line
            if in_number && number_str.len() > 0 {
                println!("{}", number_str);
                let n = NumPos{
                    num: number_str.parse::<u32>().unwrap(),
                    pos: Pos{row: row - 1, col: (l.len() - number_str.len()) as u32},
                    len: number_str.len() as u32
                };
                println!("pushing {} (row: {}, col: {})", n.num, n.pos.row, n.pos.col);
                numbers.push(n);
                number_str.clear();
            }

            for (i, c) in l.char_indices() {
                if c.is_digit(10) {
                    if !in_number {
                        number_str.clear();
                        in_number = true;
                    }
                    number_str.push(c);
                } else if c != '.' {
                    symbols.push(Pos{
                        row: row,
                        col: i as u32
                    });
                    in_number = false;
                } else {
                    in_number = false;
                }

                if !in_number && number_str.len() > 0 {
                    let n = NumPos{
                        num: number_str.parse::<u32>().unwrap(),
                        pos: Pos{row: row, col: (i - number_str.len()) as u32},
                        len: number_str.len() as u32
                    };
                    println!("pushing {} (row: {}, col: {})", n.num, n.pos.row, n.pos.col);
                    numbers.push(n);
                    number_str.clear();
                }
            }
            row += 1;
        }

        let mut part_numbers: Vec<u32> = Vec::new();

        for num in &numbers {
            println!("num = {}", num.num);
            println!("num.pos.col = {}, num.pos.row = {}", num.pos.col, num.pos.row);
            for sym in &symbols {
                println!("sym.col = {}, sym.row = {}", sym.col, sym.row);
                if sym.row == num.pos.row {
                    if (num.pos.col > 0 && sym.col == (num.pos.col - 1)) ||
                        sym.col == (num.pos.col + num.len) {
                        part_numbers.push(num.num);
                        break;
                    }
                }
                if num.pos.row > 0 {
                    if sym.row == (num.pos.row - 1) {
                        let mut start: u32 = 0;
                        if num.pos.col > 0 {
                            start = num.pos.col - 1;
                        }
                        if (sym.col >= start) && (sym.col <= (num.pos.col + num.len)) {
                            part_numbers.push(num.num);
                            break;
                        }
                    }
                }
                if sym.row == (num.pos.row + 1) {
                    let mut start: u32 = 0;
                    if num.pos.col > 0 {
                        start = num.pos.col - 1;
                    }
                    if (sym.col >= start) && (sym.col <= (num.pos.col + num.len)) {
                        part_numbers.push(num.num);
                        break;
                    }
                }
            }
        }

        acc = part_numbers.iter().sum();
        println!("{}", symbols.len());
        println!("{}", numbers.len());
        println!("{}", part_numbers.len());
        println!("{:?}", part_numbers);
    }
    println!("{}", acc);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
