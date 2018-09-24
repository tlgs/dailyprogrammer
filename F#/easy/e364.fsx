// 24/09/2018

open System

let rnd = System.Random()

let getRolls (s : string) =
    let numbers = s.Split('d') |> Array.map int
    List.init numbers.[0] (fun x -> rnd.Next(1, numbers.[1] + 1))

while true do
    let rolls = Console.ReadLine() |> getRolls

    rolls |> List.sum |> printf "%d: "
    rolls |> List.map string |>  String.concat " " |> printfn "%s"
