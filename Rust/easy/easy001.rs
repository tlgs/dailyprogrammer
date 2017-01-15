// 15/01/2017
use std::io;
#[allow(unused_must_use)]

fn main(){
    let (mut name, mut age, mut user) = (String::new(), String::new(), String::new());
    println!("What is your name?");
    io::stdin().read_line(&mut name);
    println!("What is your age?");
    io::stdin().read_line(&mut age);
    println!("What is your Reddit username?");
    io::stdin().read_line(&mut user);
    println!("\nYour name is {}, you are {} and your Reddit username is /u/{}.",
            name.trim(), age.trim(), user.trim());
}
