use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn run() {
    let f = File::open("../input/05.txt").unwrap();
    let file = BufReader::new(&f);

    let mut nice_strings = 0;
    let mut really_nice_strings = 0;
    for (_, line) in file.lines().enumerate() {
        let l = line.unwrap();
        if nice_one(&l) {
            nice_strings += 1;
        }
        if nice_two(&l) {
            really_nice_strings += 1;
        }
    }

    println!("2015:05:1 = {}", nice_strings);
    println!("2015:05:2 = {}", really_nice_strings);
}

pub fn nice_one(line: &String) -> bool {
    // It contains at least three vowels (aeiou only), like aei, xazegov, or
    // aeiouaeiouaeiou.
    let mut vowels = 0;
    for c in line.chars() {
        match c {
            'a' | 'e' | 'i' | 'o' | 'u' => vowels += 1,
            _ => (),
        }
    }
    if vowels < 3 {
        return false;
    }

    // It contains at least one letter that appears twice in a row, like xx,
    // abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    let mut sequence_found = false;
    for (idx, c) in line.chars().enumerate() {
        if idx < line.len() - 1 {
            let c2 = line.chars().nth(idx + 1).unwrap();
            if c2 == c {
                sequence_found = true;
                break;
            }
        }
    }
    if !sequence_found {
        return false;
    }

    // It does not contain the strings ab, cd, pq, or xy, even if they are part
    // of one of the other requirements.
    let illegal = ["ab", "cd", "pq", "xy"];
    for il in illegal {
        if line.contains(il) {
            return false;
        }
    }

    return true;
}

pub fn nice_two(line: &String) -> bool {
    // It contains a pair of any two letters that appears at least twice in the
    // string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not
    // like aaa (aa, but it overlaps).
    let mut pair_found = false;
    for (idx, _) in line.chars().enumerate() {
        if idx + 2 >= line.len() {
            continue;
        }
        let splitter = &line[idx..idx+2];
        let pieces: Vec<&str> = line.split(splitter).collect();
        if pieces.len() >= 3 {
            pair_found = true;
            break;
        }
    }
    if !pair_found {
        return false;
    }

    // It contains at least one letter which repeats with exactly one letter
    // between them, like xyx, abcdefeghi (efe), or even aaa.
    let mut sequence_found = false;
    for (idx, c) in line.chars().enumerate() {
        if idx < line.len() - 2 {
            let c2 = line.chars().nth(idx + 2).unwrap();
            if c2 == c {
                sequence_found = true;
                break;
            }
        }
    }
    if !sequence_found {
        return false;
    }

    return true;
}