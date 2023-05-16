#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ans = 0
    ans2 = 0
    x, y, x1, y1 = 0, 0, 0, 0
    x, y = tuple_a
    x1, y1 = tuple_b
    ans = x + x1
    ans2 = y + y1
    my_tuple = (ans, ans2)
    return my_tuple
