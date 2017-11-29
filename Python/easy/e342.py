# 27/11/2017
import json
import requests

AppID = "YOUR-APPID"

def wolfram_poly_div(num, denom):
    expr = '(' + num + ")/(" + denom + ')'
    expr = expr.replace(' ', "%2B")

    query = "http://api.wolframalpha.com/v2/query?input=" + expr
    query += "&appid=" + AppID
    query += "&format=plaintext&output=JSON"
    query += "&includepodid=QuotientAndRemainder"

    r = requests.get(query)
    result = json.loads(r.text)["queryresult"]["pods"][0]["subpods"][0]["plaintext"]

    quotient, remainder = result.split(' = ')[1].split('×', maxsplit=1)
    remainder = remainder.split('+')[1]

    return {"quotient" : quotient.rstrip().strip("()"),
            "remainder": remainder.strip()}
