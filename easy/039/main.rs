// 13/01/2017
use std::io;
use std::io::Write;

fn main(){
    print!("Input a number: ");
    io::stdout().flush().unwrap();
    let mut x = String::new();
    io::stdin().read_line(&mut x).expect("Failed to read number.");
    let x: u32 = x.trim().parse().expect("Please enter a number.");
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
