use std::fs::File;
use std::io::{BufRead, BufReader};
use regex::Regex;

pub fn run() {
    let f = File::open("../input/08.txt").unwrap();
    let file = BufReader::new(&f);

    let mut instruction_length: i64 = 0;
    let mut string_length: i64 = 0;
    let mut encode_length: i64 = 0;

    for line in file.lines() {
        let l: String;
        match line {
            Ok(v) => l = v,
            Err(e) => { println!("2015:08:ERR = {}", e); break},
        }

        instruction_length = instruction_length + (l.chars().count() as i64);
        let blabla = parse_string(&l);
        string_length = string_length + (blabla.chars().count() as i64);
        let encoded = encode_string(&l);
        encode_length = encode_length + (encoded.chars().count() as i64);
    }

    println!("2015:08:1 = {}", instruction_length - string_length);
    println!("2015:08:2 = {}", encode_length - instruction_length);
}

fn parse_string(input: &String) -> String {
    // Strip containing quotes
    let end = input.len()-1;
    let mut result: String = input[1..end].to_string();
    result = result.replace("\\\\", "\\");
    result = result.replace("\\\"", "\"");

    let search = Regex::new(r"(\\x([0-9a-f][0-9a-f]))").unwrap();
    for res in search.find_iter(&result.clone()) {
        let repl = res.as_str();

        let mut c = [0; 4];
        let chr = u8::from_str_radix(&repl[2..], 16).map(|n| n as char).unwrap().encode_utf8(&mut c);

        result = result.replace(repl, chr);
    }

    return result;
}

fn encode_string(input: &String) -> String {
    format!("{:?}", input)
}

#[cfg(test)]
mod tests {
    use super::*;

    struct Row {
        input: String,
        expect: String
    }

    #[test]
    fn test_parse_string() {

        let tests = vec![
            Row{input: "\"abc\"".to_string(), expect: "abc".to_string()},
            Row{input: "\"\"".to_string(), expect: "".to_string()},
            Row{input: "\"aaa\\\"aaa\"".to_string(), expect: "aaa\"aaa".to_string()},
            Row{input: "\"\\x27\"".to_string(), expect: "'".to_string()},
        ];

        for test in tests.iter() {
            assert_eq!(parse_string(&test.input), test.expect);
        }
    }

    #[test]
    fn test_encode_string() {
        let tests = vec![
            Row{input: "\"\"".to_string(), expect: "\"\\\"\\\"\"".to_string()},
            Row{input: "\"abc\"".to_string(), expect: "\"\\\"abc\\\"\"".to_string()},
            Row{input: "\\x27".to_string(), expect: "\"\\\\x27\"".to_string()}
        ];

        for test in tests.iter() {
            assert_eq!(encode_string(&test.input), test.expect);
        }
    }
}