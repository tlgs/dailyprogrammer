// 15/10/2018

let sleepSort (x : int list) =
    let sleep n = async {
        do! Async.Sleep (n * 1000)
        printfn "%A" n
        }

    x
    |> List.map sleep
    |> Async.Parallel
    |> Async.RunSynchronously

fsi.CommandLineArgs.[1..]
|> Array.toList
|> List.map int
|> sleepSort
