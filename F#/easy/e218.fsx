// 17/10/2018

open System.Numerics

let rev =
    string >> Array.ofSeq >> Array.rev >> System.String >> BigInteger.Parse
let rec palindromic (x, i) =
    match (x, i) with
    | (x, i) when System.String.Equals(string x, string (rev x)) -> (x, i)
    | (x, i) -> palindromic (x + (rev x), i + 1)

let query = fsi.CommandLineArgs.[1] |> BigInteger.Parse
let result = (query, 0) |> palindromic

printfn "%A gets palindromic after %A steps: %A" query (snd result) (fst result)
