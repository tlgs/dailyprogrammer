// 02/10/2018

open System

let isAnagram (a : string) (b : string) : bool =
    let normalize (str : string) : string =
        str.ToLower()
        |> Seq.filter (fun c -> c >= 'a' && c <= 'z')
        |> Seq.sort
        |> String.Concat

    String.Equals(normalize a, normalize b, StringComparison.OrdinalIgnoreCase)

while true do
    printf ">> "
    let query = Console.ReadLine()

    let r = 
        query.Split('?')
        |> (function
            | [| a; b |] -> (a, b)
            | _ -> failwith "not a two element Array.")
        ||> isAnagram
    
    let replacement = "is " + (if r then "" else "NOT ") + "an anagram of"
    printfn "%s" (query.Replace("?", replacement))
