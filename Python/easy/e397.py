# 06/07/2021


def numcompare(x, y):
    m = dict(zip("MDCLXVI", "🟥🟧🟨🟩🟦🟪🟫"))
    return x.translate(m) < y.translate(m)


assert numcompare("I", "I") == False
assert numcompare("I", "II") == True
assert numcompare("II", "I") == False
assert numcompare("V", "IIII") == False
assert numcompare("MDCLXV", "MDCLXVI") == True
assert numcompare("MM", "MDCCCCLXXXXVIIII") == False
