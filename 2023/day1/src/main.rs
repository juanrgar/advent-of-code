use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut cur_calories = 0;
    let mut calories: Vec<i32> = Vec::new();

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            let l = line.unwrap();
            if l.len() > 0 {
                cur_calories += l.parse::<i32>().unwrap();
            } else {
                calories.push(cur_calories);
                cur_calories = 0;
            }
        }
    }
    calories.sort();
    calories.reverse();
    println!("{}", calories[0]);
    let top_calories = calories[0] + calories[1] + calories[2];
    println!("{}", top_calories);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
