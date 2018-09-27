// 27/09/2018

let rec arrow a b n =
    if n = 1 then pown a b
    elif b = 0 && n >= 1 then 1
    else arrow a (arrow a (b - 1) n) (n - 1)

assert (arrow 2 4 1 = 16)
assert (arrow 2 4 2 = 65536)
assert (arrow 2 3 3 = 65536)

fsi.CommandLineArgs.[1..3]
|> Array.map int
|> (fun arr ->
    match arr with
    | [| a; b; n |] -> (a, b, n)
    | _ -> failwith "not a three element Array.")
|||> arrow
|> printfn "%A"
