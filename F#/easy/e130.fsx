// 29/10/2018

let rnd = System.Random()

let getRolls (s : string) =
    let numbers = Array.map int (s.Split 'd')
    Seq.init numbers.[0] (fun x -> rnd.Next(1, numbers.[1] + 1))

fsi.CommandLineArgs.[1]
|> getRolls
|> Seq.map string
|> String.concat " "
|> printfn "%s"
