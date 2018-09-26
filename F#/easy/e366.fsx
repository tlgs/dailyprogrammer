// 26/09/2018

open System.Net

let funnel (x : string) (y : string) : bool =

    let removeOneLetter (x : string) : string list =
        let n = x.Length - 1
        [ for i in 0 .. n -> x.[0 .. (i - 1)] + x.[(i + 1) .. n] ]

    removeOneLetter x
    |> List.contains y

let bonus1 (x : string) : string list =
    let enable1URL = @"https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt"
    let wc = new WebClient()

    let words = enable1URL |> wc.DownloadString

    words.Split '\n'
    |> Array.filter (fun y -> funnel x y)
    |> Array.toList

fsi.CommandLineArgs.[1]
|> bonus1
|> printfn "%A"
