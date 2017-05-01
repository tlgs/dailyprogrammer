##
## This piece of code was used to generate an English stop word list from
## http://snowball.tartarus.org/algorithms/english/stop.txt
##

parse = lambda x: x.partition('|')[0].strip()

with open("stop.txt", "r") as f:
    words = [parse(word) for word in f.readlines() if len(parse(word))]

with open("en_stopwords.txt", "a+") as f:
    f.write('\n'.join(words))
