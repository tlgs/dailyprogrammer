# 12/10/2017
import sys

class Message:
    def __init__(self, message_id, length):
        self.id = message_id
        self.length = length
        self.packets = [None]*length

    def update(self, packet_id, text):
        self.packets[packet_id] = text

    def is_done(self):
        if None not in self.packets:
            for i, text in enumerate(self.packets):
                print("{:<8}{:<4}{:<4}{}".format(self.id, i, self.length, text))

messages = {}
for line in sys.stdin:
    X, Y, Z, *some_text = line.split(maxsplit=3)
    Y, Z = map(int, (Y, Z))
    if X not in messages:
        messages[X] = Message(X, Z)
    messages[X].update(Y, ' '.join(some_text).strip())
    messages[X].is_done()
