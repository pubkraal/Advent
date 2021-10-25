use std::fs::File;
use std::io::{BufRead, BufReader};
use regex::Regex;

pub fn run() {
    let mut lights = vec![[0u8; 1000]; 1000].into_boxed_slice();
    let mut lights2 = vec![[0i32; 1000]; 1000].into_boxed_slice();

    let f = File::open("../input/06.txt").unwrap();
    let file = BufReader::new(&f);

    let tokenizer = Regex::new(r"^([\w\s]+) ([\d]+),([\d]+) through ([\d]+),([\d]+)$").unwrap();

    for line in file.lines() {
        let l: String;
        match line {
            Ok(v) => l = v,
            Err(e) => { println!("2015:06:ERR = {}", e); break},
        }

        let caps = tokenizer.captures(&l).unwrap();
        let startx = *&caps[2].parse::<i32>().unwrap() as usize;
        let starty = *&caps[3].parse::<i32>().unwrap() as usize;
        let endx = *&caps[4].parse::<i32>().unwrap() as usize;
        let endy = *&caps[5].parse::<i32>().unwrap() as usize;

        if &caps[1] == "toggle" {
            for x in startx..(endx + 1) {
                for y in starty..(endy + 1) {
                    lights[x][y] ^= 1;
                    lights2[x][y] += 2;
                }
            }
        } else if &caps[1] == "turn off" {
            for x in startx..(endx + 1) {
                for y in starty..(endy + 1) {
                    lights[x][y] = 0;
                    lights2[x][y] -= 1;
                    if lights2[x][y] < 0 {
                        lights2[x][y] = 0;
                    }
                }
            }
        } else if &caps[1] == "turn on" {
            for x in startx..(endx + 1) {
                for y in starty..(endy + 1) {
                    lights[x][y] = 1;
                    lights2[x][y] += 1;
                }
            }
        }
    }

    let mut lit = 0;
    let mut brightness: u64 = 0;
    for x in 0..1000 {
        for y in 0..1000 {
            if lights[x][y] == 1 {
                lit += 1;
            }
            brightness += lights2[x][y] as u64;
        }
    }

    println!("2015:06:1 = {}", lit);
    println!("2015:06:2 = {}", brightness);
}