use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;

pub fn run() {
    let f = File::open("../input/03.txt").unwrap();
    let file = BufReader::new(&f);

    let mut posx = 0;
    let mut posy = 0;
    let mut santaposx = 0;
    let mut santaposy = 0;
    let mut roboposx = 0;
    let mut roboposy = 0;
    let mut houses = HashMap::new();
    let mut robohouses = HashMap::new();

    houses.insert((posx, posy), 1);
    robohouses.insert((0, 0), 1);

    for (_, line) in file.lines().enumerate() {
        let l = line.unwrap();
        for (idx, c) in l.chars().enumerate() {
            if c == '>' {
                posx += 1;
                match idx as i32 % 2 {
                    0 => santaposx += 1,
                    1 => roboposx += 1,
                    _ => (),
                }
            } else if c == '<' {
                posx -= 1;
                match idx as i32 % 2 {
                    0 => santaposx -= 1,
                    1 => roboposx -= 1,
                    _ => (),
                }
            } else if c == '^' {
                posy += 1;
                match idx as i32 % 2 {
                    0 => santaposy += 1,
                    1 => roboposy += 1,
                    _ => (),
                }
            } else if c == 'v' {
                posy -= 1;
                match idx as i32 % 2 {
                    0 => santaposy -= 1,
                    1 => roboposy -= 1,
                    _ => (),
                }
            }

            houses.insert((posx, posy), 1);
            if idx % 2 == 0 {
                robohouses.insert((santaposx, santaposy), 1);
            } else {
                robohouses.insert((roboposx, roboposy), 1);
            }
        }
    }

    println!("2015:03:1 = {}", houses.len());
    println!("2015:03:2 = {}", robohouses.len());
}