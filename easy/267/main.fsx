// 30/10/2018

let ordinals removed range =
    let exceptions = Set.ofList [11; 12; 13]
    
    seq [1 .. range]
    |> Seq.filter (fun x -> x <> removed)
    |> Seq.map (function
                | special when Set.contains (special % 100) exceptions ->
                    string special + "th"
                | ones when ones % 10 = 1 ->
                    string ones + "st"
                | twos when twos % 10 = 2 ->
                    string twos + "nd"
                | threes when threes % 10 = 3 ->
                    string threes + "rd"
                | other -> string other + "th")

fsi.CommandLineArgs.[1 .. 2]
|> Array.map int
|> (function
    | [|a; b|] -> (a, b)
    | _ -> failwith "not two element Array.")
||> ordinals
|> String.concat ", "
|> printfn "%s"
