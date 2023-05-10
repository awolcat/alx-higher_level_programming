#!/usr/bin/python3
def remove_char_at(str, n):
    indx = 0
    new_str = ""
    for i in str:
        if indx == n:
            new_str += ""
        else:
            new_str += i
        indx = indx + 1
    return new_str
