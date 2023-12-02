use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


fn get_gameid(line: &str) -> u32 {
    let gameid_parts: Vec<&str> = line.split(' ').collect();
    gameid_parts[1].parse::<u32>().unwrap()
}

fn get_cubes_color(color: &str, game: &str) -> u32 {
    let parts: Vec<&str> = game.split(", ").collect();

    for p in parts {
        let amount_color: Vec<&str> = p.split_whitespace().collect();
        if color == amount_color[1] {
            return amount_color[0].parse::<u32>().unwrap();
        }
    }

    return 0;
}

fn main() {
    let mut acc = 0;

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            let l = line.unwrap();
            println!("{}", l);

            let parts: Vec<&str> = l.split(": ").collect();

            let gameid = get_gameid(parts[0]);
            println!("gameid {}", gameid);

            let games: Vec<&str> = parts[1].split("; ").collect();

//            let mut possible = true;
//
//            for g in &games {
//                let red = get_cubes_color("red", g);
//                let green = get_cubes_color("green", g);
//                let blue = get_cubes_color("blue", g);
//                if (red > 12) || (green > 13) || (blue > 14) {
//                    println!("not possible");
//                    possible = false;
//                }
//            }
//            if possible {
//                println!("possible");
//                acc += gameid;
//            }
//            println!("acc {}", acc);


            // part 2
            let mut counts: HashMap<&str, u32> = HashMap::new();
            counts.insert("red", 0);
            counts.insert("green", 0);
            counts.insert("blue", 0);

            for g in &games {
                println!("game {}", g);

                let red = get_cubes_color("red", g);
                let green = get_cubes_color("green", g);
                let blue = get_cubes_color("blue", g);

                if red > counts["red"] {
                    counts.entry("red").and_modify(|e| *e = red);
                }
                if green > counts["green"] {
                    counts.entry("green").and_modify(|e| *e = green);
                }
                if blue > counts["blue"] {
                    counts.entry("blue").and_modify(|e| *e = blue);
                }

                println!("counts {:?}", counts);
            }

            let power = counts["red"] * counts["green"] * counts["blue"];
            println!("power {}", power);
            acc += power;
        }
    }
    println!("{}", acc);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
