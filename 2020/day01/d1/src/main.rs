use std::fs::File;
use std::io::{BufReader, BufRead};
use itertools::Itertools;

fn main() {
    // Core array to do shit on.
    let mut numbers: [i32; 200] = [0; 200];

    // Input reading
    let f = File::open("../input.txt").unwrap();
    let file = BufReader::new(&f);
    for (idx, line) in file.lines().enumerate() {
        let l = line.unwrap();
        let num = l.as_str().parse::<i32>();
        match num {
            Ok(n) => numbers[idx] = n,
            Err(e) => println!("woops: {}", e),
        }
    }

    // Sanity test
    println!("Number of numbers: {} - {}", numbers.len(), numbers[199]);

    // Iterate through combinations, find the first "2020" sum hit
    for comb in numbers.iter().combinations(2) {
        if comb[0] + comb[1] == 2020 {
            println!("01:1 = {}", comb[0] * comb[1]);
            break;
        }
    }

    for comb in numbers.iter().combinations(3) {
        if comb[0] + comb[1] + comb[2] == 2020 {
            println!("01:2 = {}", comb[0] * comb[1] * comb[2]);
            break;
        }
    }
}
