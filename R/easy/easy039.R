fizzbuzz <- function(n){
    for(i in 1:n){
        a <- if(i%%3 == 0 && i%%5 == 0){
            "FizzBuzz"
        } else if(i%%3 == 0){
            "Fizz"
        } else if(i%%5 == 0){
            "Buzz"
        } else{
            i
        }
        print(a, quote = FALSE)
    }
}
