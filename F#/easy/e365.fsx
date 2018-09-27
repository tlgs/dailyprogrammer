// 27/09/2018

let rec arrow (a : int) (b : int) (n : int) : int =
    if n = 1 then pown a b
    elif b = 0 && n >= 1 then 1
    else arrow a (arrow a (b - 1) n) (n - 1)

fsi.CommandLineArgs.[1..3]
|> Array.map int
|> (function
    | [| a; b; n |] -> (a, b, n)
    | _ -> failwith "not a three element Array.")
|||> arrow
|> printfn "%A"
