// 22/20/2018

let fibonacci = Seq.unfold (fun (a, b) -> Some(a + b, (b, a + b))) (1, 1)

let encode d fibSeq =
    let rec decompose (d, curr, fibSeq) =
        let value =
            fibSeq
            |> Seq.pick (fun x -> if x <= d then Some x else None)

        match value with
        | v when v = d -> Seq.append curr [v]
        | v -> decompose(d - v, Seq.append curr [v], fibSeq)

    let decomposed = decompose (int d, seq [], fibSeq)

    let coded =
        fibSeq
        |> Seq.map (fun x -> if Seq.contains x decomposed then "1" else "0")

    Seq.append coded ["0"]
    |> String.concat ""

let decode s fibSeq=
    Seq.zip fibSeq s
    |> Seq.sumBy (function
                  | (x, '1') -> x
                  | (_, _) -> 0)
    |> string

let main =
    let mode = fsi.CommandLineArgs.[1]
    let query = fsi.CommandLineArgs.[2]

    let nTake =
        match String.length query with
        | x when (x - 2 < 0) -> 0
        | x -> x - 2 

    let fibSeq =
        match mode with
        | "10" -> (Seq.takeWhile (fun x -> x < int query) fibonacci
                   |> Seq.append [1]
                   |> Seq.rev)
        | "F"  -> (Seq.take nTake fibonacci
                   |> Seq.append [1; 1]
                   |> Seq.rev)
        | _    -> failwith "invalid action"

    //printfn "%A" fibSeq

    match mode with
    | "10" -> (encode query fibSeq |> printfn "%s")
    | "F"  -> (decode query fibSeq |> printfn "%s")
    | _    -> failwith "invalid action"
