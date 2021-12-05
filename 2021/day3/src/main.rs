use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut report: Vec<String> = Vec::new();

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            report.push(line.unwrap());
        }
    }

    let mut freq: Vec<i32> = vec![0; report[0].len()];
    let mut i;

    for r in report {
        i = 0;
        for c in r.chars() {
            match c {
                '0' => freq[i] -= 1,
                '1' => freq[i] += 1,
                _ => (),
            }
            i += 1;
        }
    }

    let mut gamma_str : String = String::new();
    let mut epsilon_str : String = String::new();

    for f in freq {
        if f > 0 {
            gamma_str.push('1');
            epsilon_str.push('0');
        } else {
            gamma_str.push('0');
            epsilon_str.push('1');
        }
    }

    println!("{}", gamma_str);
    println!("{}", epsilon_str);

    let gamma = s_to_i32(gamma_str);
    let epsilon = s_to_i32(epsilon_str);

    println!("{}", gamma);
    println!("{}", epsilon);

    println!("{}", gamma * epsilon);
}

fn s_to_i32(s: String) -> i32 {
    let mut ret = 0;
    let mut schars = s.chars();

    for i in 0..s.len() {
        if schars.next().unwrap() == '1' {
            ret |= 1 << (s.len() - i - 1);
        }
    }

    ret
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
