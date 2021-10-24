use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn run() {
    let f = File::open("../input/01.txt").unwrap();
    let file = BufReader::new(&f);

    let mut floor: i32 = 0;
    let mut first_negative: i32 = 0;

    for (_, line) in file.lines().enumerate() {
        let l = line.unwrap();
        for (idx, c) in l.chars().enumerate() {
            if c == '(' {
                floor += 1;
            } else if c == ')' {
                floor -= 1;
                if floor < 0 && first_negative == 0 {
                    first_negative = idx as i32 + 1;
                }
            }
        }
    }
    println!("2015:01:1 = {:?}", floor);
    println!("2015:01:2 = {:?}", first_negative);
}