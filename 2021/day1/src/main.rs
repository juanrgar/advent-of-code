use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut depths: Vec<i32> = Vec::new();

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            let depth = line.unwrap().parse::<i32>().unwrap();
            depths.push(depth);
        }
    }

    let mut inc_count = 0;
    let mut prev_depth = -1;

    for d in &depths {
        if prev_depth > 0 && *d > prev_depth {
            inc_count += 1;
        }
        prev_depth = *d;
    }

    println!("{}", inc_count);

    let mut depths3: Vec<i32> = Vec::new();

    let mut i = 0;
    while i < depths.len() {
        if (i + 2) >= depths.len() {
            break;
        }

        depths3.push(depths[i] + depths[i+1] + depths[i+2]);

        i += 1;
    }

    inc_count = 0;
    prev_depth = -1;

    for d in &depths3 {
        if prev_depth > 0 && *d > prev_depth {
            inc_count += 1;
        }
        prev_depth = *d;
    }

    println!("{}", inc_count);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
