// 11/10/2018

#time

let rng = Seq.unfold (fun state ->
    let next = (state * 22695477UL + 12345UL) % 1073741824UL
    Some(state, next)) 123456789UL

Seq.take 10000000 rng
|> Seq.sortBy (~~~)
|> Seq.take 1000
|> Seq.sum
|> printfn "%d"
