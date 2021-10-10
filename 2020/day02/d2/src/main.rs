use regex::Regex;

// I have a feeling I'm going to create a utility function to yoink data out of
// all the input.txt stuff
use std::fs::File;
use std::io::{BufRead, BufReader};

struct Record {
    min: i32,
    max: i32,
    letter: char,
    password: String,
}

fn main() {
    let re = Regex::new(r"(\d+)-(\d+) ([a-zA-Z]{1}): (\w+)").unwrap();
    let mut pwds: Vec<Record> = Vec::new();

    let mut valid_one: i64 = 0;
    let mut valid_two: i64 = 0;

    let f = File::open("../input.txt").unwrap();
    let file = BufReader::new(&f);
    for (_, line) in file.lines().enumerate() {
        let l = line.unwrap();

        let rec = generate_record(&re, &l);
        pwds.push(rec);
    }

    for rec in pwds.iter() {
        if validate_one(rec) {
            valid_one += 1;
        }
        if validate_two(rec) {
            valid_two += 1;
        }
    }

    println!("02:1 = {}", valid_one);
    println!("02:2 = {}", valid_two);
}

fn validate_one(rec: &Record) -> bool {
    let mut count = 0;
    for chr in rec.password.chars() {
        if chr == rec.letter {
            count += 1;
        }
    }

    count >= rec.min && count <= rec.max
}

fn validate_two(rec: &Record) -> bool {
    let mut count = 0;
    for pos in vec![rec.min, rec.max] {
        let chr = rec.password.chars().nth((pos - 1) as usize).unwrap();
        if chr == rec.letter {
            count += 1;
        }
    }

    count == 1
}

fn generate_record(re: &Regex, line: &String) -> Record {
    let captures = re.captures(line).unwrap();

    // populate a new struct
    let min = regex_opt_to_i32(captures.get(1));
    let max = regex_opt_to_i32(captures.get(2));
    let chr = regex_opt_to_char(captures.get(3));
    let pwd = regex_opt_to_string(captures.get(4));

    Record {
        min: min,
        max: max,
        letter: chr,
        password: pwd,
    }
}

fn regex_opt_to_i32(opt: Option<regex::Match>) -> i32 {
    match opt {
        Some(v) => return v.as_str().parse::<i32>().unwrap(),
        None => return 0,
    }
}

fn regex_opt_to_char(opt: Option<regex::Match>) -> char {
    match opt {
        Some(v) => return v.as_str().chars().next().unwrap(),
        None => return 'a',
    }
}

fn regex_opt_to_string(opt: Option<regex::Match>) -> String {
    match opt {
        Some(v) => return String::from(v.as_str()),
        None => return String::new(),
    }
}
