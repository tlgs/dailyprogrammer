// 13/11/2018

// Makes use of a global Map to cache previous results (ugly side effects?)
// Note: Breaks if tries to compute the complexity of a large number upfront

let mutable lookup = Map.ofList [1, 1;]

let rec complexity n =
    let ans =
        match n with
        | n when Map.containsKey n lookup -> Map.find n lookup
        | n -> Seq.min [ productPair n; sumPair n ]

    lookup <- Map.add n ans lookup
    ans

and productPair n =
    seq { for d in 2 .. int (sqrt (float n)) do
            if n % d = 0 then
              yield complexity d + complexity (n / d) }
    |> Seq.append [ System.Int32.MaxValue ]
    |> Seq.min

and sumPair n =
    if n < 353942783
    then 1 + complexity(n - 1)
    else Seq.min [ for d in 1 .. (n / 2) do
                     yield complexity d + complexity (n - d) ]

# time
[ 1 .. 1000000 ]
|> Seq.map complexity
|> Seq.sum
|> printfn "Bonus 1: %A"
# time

printf "\n"
fsi.CommandLineArgs.[1 .. ]
|> Seq.map int 
|> Seq.map complexity
|> Seq.zip fsi.CommandLineArgs.[1 .. ]
|> Seq.iter (fun (a, b) -> printfn "complexity(%s) = %A" a b)
