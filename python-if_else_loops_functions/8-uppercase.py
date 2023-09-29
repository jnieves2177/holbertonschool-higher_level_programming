#!/usr/bin/python3
def uppercase(input_str):
    result = ""
    for char in input_str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            result += "{}".format(uppercase_char)
        else:
            result += "{}".format(char)

    print(result)
