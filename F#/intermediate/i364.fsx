// 05/10/2018

let _ducci (element, seen) =
    let onlyZeroes = (Set.ofList element = Set.singleton 0)
    let alreadySeen = Set.contains element seen

    let next =
        List.zip element (element.[1 ..] @ [element.[0]])
        |> List.map (fun x -> abs (fst x - snd x))
    
    if onlyZeroes || alreadySeen then None
    else Some(next, (next, (Set.add element seen)))
    
let initial = 
    fsi.CommandLineArgs.[1..]
    |> Array.toList
    |> List.map int

let ducci = Seq.unfold _ducci (initial, Set.empty)
printfn "%A" initial
for x in ducci do printfn "%A" x
