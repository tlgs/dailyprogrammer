// 15/10/2018

open System.IO

let mean x = Seq.sum x / float (Seq.length x)

let variance x =
    let mx = mean x
    x |> Seq.map (fun a -> pown (a - mx) 2) |> mean

let stdDev x = x |> variance |> sqrt

let values =
    fsi.CommandLineArgs.[1]
    |> File.ReadAllLines
    |> Array.map float

printfn "mean: %A" (mean values)
printfn "variance: %A" (variance values)
printfn "standard deviation: %A" (stdDev values)
