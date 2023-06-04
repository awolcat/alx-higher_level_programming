#!/usr/bin/python3

"""
    This module 2-matrix_divide contains one function

    The function matrix_divide is defined below
"""


def matrix_divided(matrix, div):
    """
        This function divides foats and ints
        in the lists in the list matrix

        div will be rounded to 2 d.p. if it is a float
        and so will the result
    """

    if isinstance(matrix, list) is False:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    list_of_lists = [isinstance(row, list) for row in matrix]
    if all(list_of_lists) is False:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    if len(matrix) <= 1:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    std_len = len(matrix[0])
    for row in matrix:
        if len(row) != std_len:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    sub_list = []
    new_list = []
    if isinstance(div, float):
        div = round(div, 2)
        new_list = [[round(i / div, 2) for i in row] for row in matrix]

    if all(list_of_lists) and isinstance(div, int):
        for row in matrix:
            for i in row:
                tmp = round(i / div, 2)
                sub_list.append(tmp)
            new_list.append(sub_list)
            sub_list = []

    return new_list
