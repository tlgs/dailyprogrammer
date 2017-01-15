// 16/01/2017
use std::io;
use std::io::Write;

fn main(){
    print!("Input a number: ");
    io::stdout().flush().unwrap();
    let mut n = String::new();
    io::stdin().read_line(&mut n).unwrap();
    let mut n: u32 = n.trim().parse().unwrap();
    while n > 1 {
        match n%3 {
            0 => println!("{} 0", n),
            1 => {println!("{} -1", n); n -= 1}
            _ => {println!("{} 1", n); n += 1}
        }
        n /= 3;
    }
    println!("{}", n);
}
