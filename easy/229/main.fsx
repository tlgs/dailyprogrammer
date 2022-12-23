// 16/10/2018

let rec dottie = function
    | x when x = cos x -> x
    | x -> dottie (cos x)

fsi.CommandLineArgs.[1]
|> float
|> dottie
|> printfn "%A"
