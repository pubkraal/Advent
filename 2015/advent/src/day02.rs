use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn run() {
    let f = File::open("../input/02.txt").unwrap();
    let file = BufReader::new(&f);

    for line in file.lines() {
        let l = line.unwrap();
        let sides: Vec<&str> = l.split('x').collect();
        println!("{:?}", sides);
    }

    println!("2015:02:1 = {:?}", 0);
    println!("2015:02:2 = {:?}", 0);
}