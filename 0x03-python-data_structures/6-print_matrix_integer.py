#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    for i in range(0, length):
        for j in matrix[i]:
            print("{:d}".format(j:), end="")
        print()
