// 09/10/2018

open System.Text.RegularExpressions

let rule (word: string) : bool =
    Regex.Match(word, @"cie|(^|[^c])ei").Success
    |> not

fsi.CommandLineArgs.[1]
|> rule
|> printfn "%A"
