#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    wrap = 0
    length = len(matrix)
    for i in range(length):
        wrap = 0
        for j in matrix[i]:
            wrap = wrap + 1
            print("{:d}".format(j), end="")
            if wrap < len(matrix[i]):
                print("{}".format(" "), end="")
        print("{}".format(""))
