# 25/04/2017

mapping = {'A': '4', 'B': '6', 'E': '3', 'I': '1', 'L': '1', 'M': '(V)',
           'N': '(\\)', 'O': '0', 'S': '5', 'T': '7', 'V':'\\/', 'W': '`//'}

def from_l33t(string):
    for k, v in mapping.items():
        string = string.replace(v, k)
    return string[0].upper() + string[1:].lower()

def to_l33t(string):
    return ''.join([c if c.upper() not in mapping else mapping[c.upper()] for c in string]).upper()
