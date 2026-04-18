#!/usr/bin/python3
def uppercase(str):
    for char in str:
        code = ord(char)
        if 97 <= code <= 122:
            char = chr(code - 32)
        print("{}".format(char), end="")
    print("")
