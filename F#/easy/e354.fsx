// 12/11/2018

let rec complexity n =
    let stop = uint64 (sqrt (float n)) + 1UL

    seq { for d in 1UL .. stop do if n % d = 0UL then yield d + (n / d) }
    |> Seq.min

# time
fsi.CommandLineArgs.[1]
|> uint64
|> complexity
|> printfn "%d"
