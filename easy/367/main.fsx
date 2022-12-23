// 25/09/2018

let rec subfactorial (n : int) : uint64 =
    match n with
    | 0 -> 1UL
    | 1 -> 0UL
    | _ -> uint64 (n - 1) * (subfactorial (n - 1) + subfactorial (n - 2))

fsi.CommandLineArgs.[1]
|> int
|> subfactorial
|> printfn "%d"
