use std::fs::File;
use std::io::{self, BufRead};
use std::collections::HashMap;
use std::path::Path;

fn find_common_item_type(rucksacks: &Vec<String>) -> char {
    let mut freqs: HashMap<char, u32> = HashMap::new();

    for r in rucksacks {
        for c in r.chars() {
            freqs.entry(c).and_modify(|f| *f += 1).or_insert(1);
        }
    }

    for (k, v) in freqs {
        if v == rucksacks.len() as u32 {
            return k;
        }
    }

    return 'a'
}

fn main() {
    let mut priorities: Vec<i32> = Vec::new();

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            let l = line.unwrap();
            let parts = l.split_at(l.len() / 2);
            let rucksacs = vec![parts.0.to_string(), parts.1.to_string()];
            let c = find_common_item_type(&rucksacs);
            let pri;
            if c.is_lowercase() {
                pri = c as i32 - 'a' as i32 + 1;
            } else {
                pri = c as i32 - 'A' as i32 + 27;
            }
            priorities.push(pri);
        }
    }
    let sum: i32 = priorities.iter().sum();
    println!("{}", sum);

    let mut priorities: Vec<i32> = Vec::new();

    if let Ok(lines) = read_lines("input.txt") {
        let mut rucksacs: Vec<String> = Vec::new()
        for line in lines {
            let l = line.unwrap();
            let parts = l.split_at(l.len() / 2);
            if rucksacs.len() < 6 {
                rucksacs.push(vec![parts.0.to_string(), parts.1.to_string()]);
            } else {
                let c = find_common_item_type(&rucksacs);
                let pri;
                if c.is_lowercase() {
                    pri = c as i32 - 'a' as i32 + 1;
                } else {
                    pri = c as i32 - 'A' as i32 + 27;
                }
                priorities.push(pri);
                rucksacs.clear();
            }
        }
    }
    let sum: i32 = priorities.iter().sum();
    println!("{}", sum);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
