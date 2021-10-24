use std::fs;
use md5;

pub fn run() {
    let contents = fs::read_to_string("../input/04.txt")
        .expect("could not read file");

    let mut num = 1;
    let mut done = false;
    let mut five = 0;
    let mut six = 0;
    while !done {
        let cur = format!("{}{}", contents, num);
        let test = format!("{:x}", md5::compute(cur.as_bytes()));

        if five == 0 && test[..5] == String::from("00000") {
            five = num;
        }
        if test[..6] == String::from("000000") {
            six = num;
            done = true;
        }
        num += 1;
    }


    println!("2015:04:1 = {}", five);
    println!("2015:04:2 = {}", six);
}