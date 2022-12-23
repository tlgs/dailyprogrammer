// 29/10/2018

let rec change = function
    | 0 -> 1
    | n -> change (n / 2) + change (n / 3) + change (n / 4)

fsi.CommandLineArgs.[1]
|> int
|> change
|> printfn "%A"
