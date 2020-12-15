use std::collections::HashMap;

fn main() {
    let mut spoken = vec![9,6,0,10,18,2,1];

    let end: i32 = 30000001;
    // let end: i32 = 2021;

    let mut last: HashMap<i32, i32> = HashMap::new();
    for (idx, val) in spoken.iter().enumerate() {
        last.insert(*val as i32, idx as i32);
    }

    let startlen = spoken.len() as i32;
    for x in startlen..end {
        let prev = spoken.last().copied().unwrap();
        if last.contains_key(&prev) {
            let diff = x - last.get(&prev).unwrap() - 1;
            spoken.push(diff);
        } else {
            spoken.push(0);
        }
        last.insert(prev, x-1);
        
        if x == 2020 {
            println!("1: {:?}", prev);
        }
        if x == 30000000 {
            println!("2: {:?}", prev);
        }
    }
}
