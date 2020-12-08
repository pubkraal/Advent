use regex::Regex;

use std::fs::File;
use std::io::{BufRead, BufReader};

#[derive(PartialEq, Eq, Copy, Clone)]
enum Action {
    ACC = 1,
    JMP,
    NOP,
}

struct Instruction {
    act: Action,
    val: i32,
    cnt: i32,
}

fn main() {
    let re = Regex::new(r"(\w+) ([+\-]\w+)").unwrap();
    let mut is: Vec<Instruction> = Vec::new();
    let mut swappos: Vec<i32> = Vec::new();

    let f = File::open("input.txt").unwrap();
    let file = BufReader::new(&f);
    for (idx, line) in file.lines().enumerate() {
        let l = line.unwrap();

        let i = from_string(&re, &l);
        let act: Action = i.act;
        is.push(i);
        if act == Action::JMP || act == Action::NOP {
            swappos.push(idx as i32);
        }
    }

    let acc = run(is, -1);
    println!("Step 1: {:?}", acc);

    let mut acc2: i32 = 0;
    for pos in swappos {
        acc2 = run(is, pos);
        if acc2 != 0 {
            break;
        }
    }
    println!("Step 2: {:?}", acc2);
}

fn run(mut is: Vec<Instruction>, modify: i32) -> i32 {
    let mut acc: i32 = 0;
    let mut ip: i32 = 0;

    loop {
        if ip >= is.len() as i32 || ip < 0 {
            break;
        }

        let i = &mut is[ip as usize];
        if i.cnt > 0 {
            if modify >= 0 {
                return 0;
            }
            break;
        }

        let act: Action;
        if ip == modify {
            if i.act == Action::JMP {
                act = Action::NOP;
            } else if i.act == Action::NOP {
                act = Action::JMP;
            } else {
                act = Action::ACC;
            }
        } else {
            act = i.act;
        }

        if act == Action::ACC {
            acc += i.val;
            ip += 1;
        } else if act == Action::JMP {
            ip += i.val;
        } else if act == Action::NOP {
            ip += 1;
        }
        i.cnt += 1;
    }

    acc
}

fn from_string(re: &Regex, line: &String) -> Instruction {
    let caps = re.captures(line).unwrap();
    let capact = caps.get(1).unwrap().as_str();

    let action = match capact {
        "jmp" => Action::JMP,
        "nop" => Action::NOP,
        "acc" => Action::ACC,
        _ => Action::NOP,   // Actually this should error out
    };

    let value = caps.get(2).unwrap().as_str().parse().unwrap();

    Instruction {
        act: action,
        val: value,
        cnt: 0
    }
}
