# 19/02/2017

with open('input.txt', 'r') as f:
    data = f.readlines()

data = list(filter(None, list(map(lambda x: x.rstrip(), data))))
maxlen = len(max(data, key=len))
data = ['{0:<{fill}}'.format(text, fill = str(maxlen)) for text in data]

output = [ [] for j in range(maxlen)]
for i in range(len(data)):
    for j, char in enumerate(data[i]):
        output[j].append(char)
for line in output:
    print(''.join(line))
