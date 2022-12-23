# 29/06/2017
# inspired by /u/Toctave's solution

def talking_clock(time):
    h, m = map(int, time.split(':'))
    gt12, h = divmod(h, 12)

    s = "It's "
    s += ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"][h] + ' '
    s += ["", "oh "][m > 0 and m < 10]
    s += ["\b", "twenty", "thirty", "forty", "fifty"][(m > 19) * (m//10 - 1)] + ' '
    s += ["\b", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][m%10 + 10*(m > 9 and m < 20)]
    s += [" am", " pm"][gt12]

    print(s)