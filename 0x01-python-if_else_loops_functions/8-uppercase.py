#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for a in str:
        if ord(a) >= 97 and ord(a) <= 122:
            a = chr(ord(a) - 32)
        new_str = new_str + a
    print("{}".format(new_str))
