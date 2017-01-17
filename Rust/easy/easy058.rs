/* 17/01/2017 */
use std::env;

static ASCII_UPPER: [char; 36] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                                  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                                  'U', 'V', 'W', 'X', 'Y', 'Z'];

fn int_to_string(mut input: u64, radix: u64) -> String {
    if input == 0 { return String::from("0"); }

    let mut output = String::new();

    while input > 0 {
        let c: char = *ASCII_UPPER.get((input%radix) as usize).unwrap();
        output.push(c);
        input /= radix;
    }
    output.as_str().chars().rev().collect()
}

fn main() {
    let num: u64 = env::args().nth(1).unwrap().parse().unwrap();
    let radix: u64 = env::args().nth(2).unwrap().parse().unwrap();
    println!("{}", int_to_string(num, radix));
}
