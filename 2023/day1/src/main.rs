use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut acc = 0;

    let numbers_words = vec!["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            let l = line.unwrap();
            println!("{}", l);
            // let nums: String = l.chars().filter(|c| c.is_digit(10)).collect();
            //let nums: String = l.chars().filter(|c| c.is_digit(10)).collect();
            //let num = nums.chars().next().unwrap().to_digit(10).unwrap() * 10 +
            //    nums.chars().last().unwrap().to_digit(10).unwrap();
            //acc += num;

            let mut nums: Vec<u32> = Vec::new();
            for (i, c) in l.char_indices() {
                if c.is_digit(10) {
                    nums.push(c.to_digit(10).unwrap());
                } else {
                    for w in &numbers_words {
                        let rem = l.len() - i;
                        let mut len = w.len();
                        if len > rem {
                            len = rem;
                        }
                        let s = &l[i..i + len];
                        if *w == s {
                            println!("{}", *w);
                            nums.push(match *w {
                                "one" => 1,
                                "two" => 2,
                                "three" => 3,
                                "four" => 4,
                                "five" => 5,
                                "six" => 6,
                                "seven" => 7,
                                "eight" => 8,
                                "nine" => 9,
                                _ => 0
                            });
                        }
                    }
                }
            }
            println!("{:?}", nums);
            let num = nums[0] * 10 + nums.last().unwrap();
            acc += num;
        }
    }
    println!("{}", acc);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
