use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;

pub fn run() {
    let f = File::open("../input/07.txt").unwrap();
    let file = BufReader::new(&f);

    let mut calc: HashMap<String, Vec<String>> = HashMap::new();
    let mut results: HashMap<String, i32> = HashMap::new();

    for line in file.lines() {
        let l: String;
        match line {
            Ok(v) => l = v,
            Err(e) => { println!("2015:07:ERR = {}", e); break},
        }

        let spl: Vec<&str> = l.split(" -> ").collect();
        let rops = String::from(spl[0]);
        let ops: Vec<String> = rops.split(" ").map(String::from).collect();
        let res = String::from(spl[1].trim());

        calc.insert(res, ops);
    }

    let aval: i32 = calculate(&calc, &mut results, String::from("a"));
    results.drain();
    results.insert(String::from("b"), aval);
    let bval: i32 = calculate(&calc, &mut results, String::from("a"));

    println!("2015:07:1 = {}", aval);
    println!("2015:07:2 = {}", bval);
}

fn calculate(calc: &HashMap<String, Vec<String>>, results: &mut HashMap<String, i32>, name: String) -> i32 {
    let testval = name.parse::<i32>();
    let res: i32;
    match testval {
        Ok(v) => { return v },
        Err(_) => (),
    }

    let mapv = results.get(&name);
    match mapv {
        Some(v) => { return *v },
        None => (),
    }

    let ops = calc.get(&name).unwrap();
    if ops.len() == 1 {
        res = calculate(calc, results, ops[0].to_string());
    } else if ops.len() == 2 {
        res = !calculate(calc, results, ops[1].to_string());
    } else {
        let op: &String = &ops[1];
        if op == "AND" {
            res = calculate(calc, results, ops[0].to_string()) & calculate(calc, results, ops[2].to_string());
        } else if op == "OR" {
            res = calculate(calc, results, ops[0].to_string()) | calculate(calc, results, ops[2].to_string());
        } else if op == "RSHIFT" {
            res = calculate(calc, results, ops[0].to_string()) >> calculate(calc, results, ops[2].to_string());
        } else if op == "LSHIFT" {
            res = calculate(calc, results, ops[0].to_string()) << calculate(calc, results, ops[2].to_string());
        } else {
            res = 0;
        }
    }

    results.insert(name, res);
    res
}