# 15/06/2017
import re

def condense(str):
    return re.sub(r"(\w+)\s\1", r"\1", str)