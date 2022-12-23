// 10/01/2019

let upc number = 
    let digits =
        ("00000000000" |> Seq.toList) @ (number |> Seq.toList)
        |> Seq.skip (Seq.length number)
        |> Seq.map (fun x -> int x - 48)
    
    let even = 
        digits
        |> Seq.mapi (fun i e -> e, i)
        |> Seq.filter (fun (_, i) -> i % 2 = 0)
        |> Seq.map fst

    let odd =
        digits
        |> Seq.mapi (fun i e -> e, i)
        |> Seq.filter (fun (_, i) -> i % 2 = 1)
        |> Seq.map fst

    ((Seq.sum even) * 3 + (Seq.sum odd)) % 10
    |> (function
        | 0 -> 0
        | x -> 10 - x)

fsi.CommandLineArgs.[1]
|> upc
|> printfn "%A"
