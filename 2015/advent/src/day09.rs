use std::fs::File;
use std::io::{BufRead, BufReader};
use regex::Regex;
use itertools::Itertools;
use std::collections::{HashMap, HashSet};

pub fn run() {
    let tokenizer = Regex::new(r"([\w]+) to ([\w]+) = ([\d]+)").unwrap();

    let mut cities: HashSet<String> = HashSet::new();
    let mut distances: HashMap<String, i64> = HashMap::new();

    let f = File::open("../input/09.txt").unwrap();
    let file = BufReader::new(&f);

    for line in file.lines() {
        let l: String;
        match line {
            Ok(v) => l = v,
            Err(e) => { println!("2015:09:ERR = {}", e); break},
        }

        let caps = tokenizer.captures(&l).unwrap();
        let city1 = &caps[1];
        let city2 = &caps[2];
        let distance = caps[3].parse::<i64>().unwrap();

        cities.insert(String::from(city1));
        cities.insert(String::from(city2));

        let d1 = format!("{}-{}", city1, city2);
        let d2 = format!("{}-{}", city2, city1);

        distances.insert(d1, distance);
        distances.insert(d2, distance);
    }

    let mut shortest = i64::MAX;
    let mut longest: i64 = 0;
    let num_cities = cities.len();
    let perms = cities.into_iter().permutations(num_cities);
    for perm in perms {
        let d = get_distance(&perm, &distances);
        if d < shortest {
            shortest = d;
        }
        if d > longest {
            longest = d;
        }
    }

    println!("2015:09:1 = {}", shortest);
    println!("2015:09:2 = {}", longest);
}

fn get_distance(route: &Vec<String>, distancemap: &HashMap<String, i64>) -> i64 {
    let mut distance = 0;
    for idx in 0..route.len()-1 {
        if idx == route.len() - 1 {
            break;
        }
        let lookup = format!("{}-{}", route[idx], route[idx+1]);
        distance = distance + distancemap.get(&lookup).unwrap();
    }
    return distance;
}

#[cfg(test)]
mod tests {
    use super::*;

    struct TestRoute<'a> {
        route: Vec<String>,
        map: &'a HashMap<String, i64>,
        expect: i64,
    }

    #[test]
    fn test_get_distance() {
        let mut map: HashMap<String, i64> = HashMap::new();
        map.insert("a-b".to_string(), 1);
        map.insert("b-a".to_string(), 1);
        map.insert("b-c".to_string(), 2);
        map.insert("c-b".to_string(), 2);
        map.insert("a-c".to_string(), 3);
        map.insert("c-a".to_string(), 3);

        let tests = vec![
            TestRoute{
                route: vec!["a".to_string(), "b".to_string(), "c".to_string()],
                map: &map,
                expect: 3,
            },
            TestRoute{
                route: vec!["a".to_string(), "c".to_string(), "b".to_string()],
                map: &map,
                expect: 5,
            },
        ];

        for test in tests {
            assert_eq!(get_distance(&test.route, test.map), test.expect);
        }
    }

}