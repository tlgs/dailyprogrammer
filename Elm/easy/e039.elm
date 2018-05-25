-- 25/05/2018
import Html

fizzBuzz : Int -> List String
fizzBuzz n = 
    let 
        fbMap x =
            if x%3 + x%5 == 0 then
                "FizzBuzz"
            else if x%3 == 0 then 
                "Fizz"
            else if x%5 == 0 then 
                "Buzz"
            else
                toString x
    in
        List.range 1 n 
            |> List.map fbMap

main = 
    fizzBuzz 100
        |> List.map Html.text
        |> List.intersperse (Html.br [] [])
        |> Html.div []