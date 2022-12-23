# 01/02/2017
import re

def get_inputs(inputFile="encoded.txt"):
    f = open(inputFile, 'r')
    temp = f.readline().strip().split()
    key = {}
    for x, y in zip(temp[::2], temp[1::2]):
        key[y] = x
    return (f.read(), key)

def decode(args):
    message, key, output = args[0], args[1], []
    start, finish, keys = 0, 1, key.keys()
    while finish <= len(message):
        if message[start:finish] in keys:
            output.append(key[message[start:finish]])
            start = finish
        elif not message[start] in "gG":
            output.append(message[start])
            start = finish
        finish += 1
    return ''.join(output)

def encode(inputFile="input.txt", outputFile="encoded.txt"):
    fi = open(inputFile, 'r')
    text = fi.read()
    nbits, key = len(set(re.sub("\W", "", text))).bit_length(), {}
    outputText, outputCode = [], []

    for char in text:
        if (not char in key.keys()) and (char.isalpha()):
            key[char] = '{:0{length}b}'.format(len(key.keys()),
                        length = nbits).replace("0", "g").replace("1", "G")
        outputText.append(char if not char.isalpha() else key[char])
    outputText = ''.join(outputText)

    for alpha, code in key.items():
        outputCode.append("{} {} ".format(alpha, code))
    outputCode = ''.join(outputCode + ['\n'])

    fo = open(outputFile, 'w')
    fo.write(''.join((outputCode, outputText)))
