use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn ranges_contain(a: (i32, i32), b: (i32, i32)) -> bool {
    if a.0 <= b.0 && a.1 >= b.1 {
        true
    } else if b.0 <= a.0 && b.1 >= a.1 {
        true
    } else {
        false
    }
}

fn ranges_overlap(a: (i32, i32), b: (i32, i32)) -> bool {
    if ranges_contain(a, b) {
        true
    } else if a.1 >= b.0 && a.1 <= b.1 {
        true
    } else if b.1 >= a.0 && b.1 <= a.1 {
        true
    } else {
        false
    }
}

fn main() {
    let mut contained = 0;
    let mut overlapped = 0;

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            let l = line.unwrap();
            let pairs: Vec<&str> = l.split(',').collect();
            let first_pair_nums: Vec<&str> = pairs[0].split('-').collect();
            let first = (first_pair_nums[0].parse::<i32>().unwrap(),
                         first_pair_nums[1].parse::<i32>().unwrap());
            let second_pair_nums: Vec<&str> = pairs[1].split('-').collect();
            let second = (second_pair_nums[0].parse::<i32>().unwrap(),
                         second_pair_nums[1].parse::<i32>().unwrap());

            if ranges_contain(first, second) {
                contained += 1;
            }

            if ranges_overlap(first, second) {
                overlapped += 1;
            }
        }
    }

    println!("{}", contained);
    println!("{}", overlapped);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
