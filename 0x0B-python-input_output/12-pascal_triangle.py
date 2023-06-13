#!/usr/bin/python3
"""
    This module defines a single function
"""


def pascal_triangle(n):
    """This function creates and returns
        a pascal triangle of size n
        in form of a list of lists
    """
    triangle = []

    if n <= 0:
        return triangle
    for i in range(1, n + 1):
        sub = [1]
        if i >= 2:
            [sub.append(pre[x] + pre[x + 1]) for x in range(0, len(pre) - 1)]
            sub.append(1)
        pre = sub[:]
        triangle.append(sub)
    return triangle
