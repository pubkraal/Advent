use std::fs;

pub fn run() {
    let mut current = fs::read_to_string("../input/10.txt").unwrap();

    let mut part1: String = "not found".to_string();
    let mut part2: String = "not found".to_string();

    for idx in 0..50 {
        current = generate_next(current);
        println!("{}: {}", idx+1, current.len());
        if idx == 39 {
            part1 = current.clone();
        }
        if idx == 49 {
            part2 = current.clone();
        }
    }

    println!("2015:10:1 = {}", part1.len());
    println!("2015:10:2 = {}", part2.len());
}

fn generate_next(input: String) -> String {
    let mut counter = 1;

    let num_chars = input.len();
    let mut current = input.chars().nth(0).unwrap();
    if num_chars == 1 {
        // Kind of a special case
        return format!("1{}", current);
    }

    let mut output = "".to_string();

    let chars = input.chars();

    for test in chars {
    // for idx in 1..num_chars {
        // let test = input.chars().nth(idx).unwrap();
        if current == test {
            counter += 1;
        } else {
            output = format!("{}{}{}", output, counter, current);
            current = test;
            counter = 1;
        }
    }
    // Add last range
    output = format!("{}{}{}", output, counter, current);

    return output
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_generate_next() {
        assert_eq!(generate_next("1".to_string()), "11".to_string());
        assert_eq!(generate_next("11".to_string()), "21".to_string());
        assert_eq!(generate_next("21".to_string()), "1211".to_string());
        assert_eq!(generate_next("1211".to_string()), "111221".to_string());
        assert_eq!(generate_next("3113322113".to_string()), "132123222113".to_string());
    }
}