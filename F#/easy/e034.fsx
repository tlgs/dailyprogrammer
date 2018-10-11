// 11/10/2018

let f x y z =
    let smaller = Array.min [|x; y; z|]
    x * x + y * y + z * z - smaller * smaller

fsi.CommandLineArgs.[1..3]
|> Array.map float
|> (function
    | [|a; b; c|] -> (a, b, c)
    | _ -> failwith "not a three element Array.")
|||> f
|> printfn "%A"
