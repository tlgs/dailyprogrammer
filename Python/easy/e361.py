# 18/05/2018

def tally(series):
    scores = {}
    for char in series:
        if char.lower() not in scores:
            scores[char.lower()] = 0
        scores[char.lower()] += (-1)**char.isupper()
    scores = sorted(scores.items(), key=lambda x: (-x[1], x[0]))

    return ", ".join(["{}:{}".format(k, v) for k, v in scores])

def one_liner_tally(s):
    return ", ".join(["{}:{}".format(k, v) for k, v in sorted([[c, s.count(c) - s.count(c.upper())] for c in set(s.lower())], key=lambda x: (-x[1], x[0]))])


if __name__ == "__main__":
    assert tally("abcde") == "a:1, b:1, c:1, d:1, e:1"
    assert tally("dbbaCEDbdAacCEAadcB") == "b:2, d:2, a:1, c:0, e:-2"
    assert tally("EbAAdbBEaBaaBBdAccbeebaec") == "c:3, d:2, a:1, e:1, b:0"

    assert tally("abcde") == one_liner_tally("abcde")
    assert tally("dbbaCEDbdAacCEAadcB") == one_liner_tally("dbbaCEDbdAacCEAadcB")
    assert tally("EbAAdbBEaBaaBBdAccbeebaec") == one_liner_tally("EbAAdbBEaBaaBBdAccbeebaec")
