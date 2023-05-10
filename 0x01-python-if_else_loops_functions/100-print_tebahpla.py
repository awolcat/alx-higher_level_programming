#!/usr/bin/python3
i = 122
j = 122
while j >= 97:
    if j % 2 != 0:
        i = chr(j - 32)
        j = j - 1
    else:
        i = chr(j)
        j = j - 1
    print("{}".format(i), end="")
