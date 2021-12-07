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

    let freq = count_freq(&report, 0);

    let mut gamma_str : String = String::new();
    let mut epsilon_str : String = String::new();

    for f in &freq {
        if *f > 0 {
            gamma_str.push('1');
            epsilon_str.push('0');
        } else {
            gamma_str.push('0');
            epsilon_str.push('1');
        }
    }

    println!("{}", gamma_str);
    println!("{}", epsilon_str);

    let gamma = s_to_i32(&gamma_str);
    let epsilon = s_to_i32(&epsilon_str);

    println!("{}", gamma);
    println!("{}", epsilon);

    println!("{}", gamma * epsilon);

    let mut r0 = clone_vector(&report);
    let mut i = 0;
    while r0.len() > 1 {
        let freq = count_freq(&r0, i);
        if freq[0] >= 0 {
            clean_vector(&mut r0, i, b'1');
        } else {
            clean_vector(&mut r0, i, b'0');
        }
        i += 1;
    }

    let mut r1 = clone_vector(&report);
    let mut i = 0;
    while r1.len() > 1 {
        let freq = count_freq(&r1, i);
        if freq[0] >= 0 {
            clean_vector(&mut r1, i, b'0');
        } else {
            clean_vector(&mut r1, i, b'1');
        }
        i += 1;
    }

    let o2_str: String = r0[0].clone();
    let co2_str: String = r1[0].clone();

    println!("{}", o2_str);
    println!("{}", co2_str);

    let o2 = s_to_i32(&o2_str);
    let co2 = s_to_i32(&co2_str);

    println!("{}", o2);
    println!("{}", co2);
    println!("{}", o2 * co2);
}

fn count_freq(report: &Vec<String>, start: usize) -> Vec<i32> {
    let mut freq: Vec<i32> = vec![0; report[0].len() - start];
    let mut i;
    let mut j;

    for r in report {
        i = start;
        j = 0;
        let b = r.as_bytes();
        while i < b.len() {
            match b[i] {
                b'0' => freq[j] -= 1,
                b'1' => freq[j] += 1,
                _ => (),
            }
            i += 1;
            j += 1;
        }
    }

    freq
}

fn clone_vector(v: &Vec<String>) -> Vec<String> {
    let mut ret: Vec<String> = Vec::new();

    for e in v {
        ret.push(e.clone());
    }

    ret
}

fn clean_vector(report: &mut Vec<String>, i: usize, c: u8) {
    report.retain(|x| x.as_bytes()[i] == c);
}

fn s_to_i32(s: &String) -> i32 {
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
