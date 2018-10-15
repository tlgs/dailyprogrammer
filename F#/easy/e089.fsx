// 15/10/2018

open System
open System.IO

let mean (x : float list) : float =
    (List.sum x) / (float (List.length x))

let variance (x : float list) : float =
    x
    |> List.map (fun a -> pown (a - (mean x)) 2)
    |> mean

let stdDev =
    variance >> Math.Sqrt 

let values =
    fsi.CommandLineArgs.[1]
    |> File.ReadAllLines
    |> Array.toList
    |> List.map float

printfn "mean: %A" (mean values)
printfn "variance: %A" (variance values)
printfn "standard deviation: %A" (stdDev values)
