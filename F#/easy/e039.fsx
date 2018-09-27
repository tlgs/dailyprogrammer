// 23/09/2018

let fizzBuzz (n : int) : string list =
    [1..n]
    |> List.map (function
        | x when (x % 3 = 0) && (x % 5 = 0) -> "FizzBuzz"
        | x when x % 3 = 0 -> "Fizz"
        | x when x % 5 = 0 -> "Buzz"
        | x -> string x)

fsi.CommandLineArgs.[1]
|> int
|> fizzBuzz
|> List.iter (printfn "%s")
