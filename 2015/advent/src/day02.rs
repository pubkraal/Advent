use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn run() {
    let f = File::open("../input/02.txt").unwrap();
    let file = BufReader::new(&f);

    let mut total_area = 0;
    let mut total_ribbon = 0;

    for line in file.lines() {
        let l = line.unwrap();
        let sides: [i32;3] = line_to_sides(l);
        let surfaces: [i32;3] = sides_to_surfaces(sides);

        total_area += calc_area(surfaces);
        let rib = calc_ribbon(sides);
        total_ribbon += rib;
    }

    println!("2015:02:1 = {:?}", total_area);
    println!("2015:02:2 = {:?}", total_ribbon);
}

fn line_to_sides(line: String) -> [i32;3] {
    let str_sides: Vec<&str> = line.split('x').collect();

    let mut sides: [i32;3] = [0, 0, 0];
    for (idx, side) in str_sides.iter().enumerate() {
        sides[idx] = side.parse::<i32>().unwrap();
    }

    return sides;
}

fn sides_to_surfaces(sides: [i32;3]) -> [i32;3] {
    let l = sides[0];
    let w = sides[1];
    let h = sides[2];

    return [l * w, w * h, h * l];
}

fn calc_area(surfaces: [i32;3]) -> i32 {
    let mut total = 0;
    let spare = surfaces.iter().min().unwrap();

    for n in 0..3 {
        total += surfaces[n] * 2;
    }

    total += spare;
    
    return total;
}

fn calc_ribbon(sides: [i32;3]) -> i32 {
    let bow = sides[0] * sides[1] * sides[2];

    let mut sides2 = vec![0; 3];
    sides2.clone_from_slice(&sides);
    sides2.sort();
    sides2.pop();

    let ribbon = (sides2[0] * 2) + (sides2[1] * 2);
    return ribbon + bow;
}