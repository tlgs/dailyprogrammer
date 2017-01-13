// 13/01/2017
use std::io;
use std::io::Write;

fn main(){
    let mut x = String::new();
    print!("Input a number: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut x).expect("Failed to read number.");
    let x = x.trim().parse::<u32>().unwrap();
    for i in 1..x+1 {
        if i%3 == 0 && i%5 == 0 {
            println!("FizzBuzz");
        } else if i%3 == 0 {
            println!("Fizz");
        } else if i%5 == 0 {
            println!("Buzz");
        } else{
            println!("{}", i);
        }
    }
}
