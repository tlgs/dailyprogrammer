// 24/20/2018

let guess (heard, seen) =
    // 0 -> even number of 1s
    // 1 -> odd number of 1s
    if Seq.isEmpty heard
    then (Seq.sum seen) % 2
    else ((Seq.sum seen + Seq.sum (Seq.tail heard)) % 2) ^^^ (Seq.head heard)

let hats =
    fsi.CommandLineArgs.[1 .. ]
    |> Array.map (function
                  | "Black" -> 0
                  | "White" -> 1
                  | _ -> failwith "invalid input")
    |> Array.toList
        
// each person sees a number of hats;
// based on what each person has seen/heard, they make a guess;
// the last person has heard all previous guesses (and makes its own);
let guesses =
    seq [ for i in 0 .. (Seq.length hats - 1) -> Seq.skip (i + 1) hats ]
    |> Seq.scan (fun h s -> Seq.append h [ guess (h, s) ]) Seq.empty
    |> Seq.last
    |> Seq.toList

hats    |> printfn "actual:  %A"
guesses |> printfn "guesses: %A"

match List.tail hats = List.tail guesses with
| true -> printfn "\nThe group wins!"
| false -> printfn "\nThe group loses!"
