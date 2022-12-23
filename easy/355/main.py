# 07/04/2018
from itertools import cycle

def encrypt(message, key):
    return ''.join([chr((ord(c)+ord(k)-194)%26+97) for c, k in zip(message, cycle(key))])

def decrypt(message, key):
    return ''.join([chr((ord(c)-ord(k))%26+97) for c, k in zip(message, cycle(key))])
