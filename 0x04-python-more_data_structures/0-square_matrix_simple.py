#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    [new_matrix.append(row) for row in matrix]
    new_matrix = [[x ** 2 for x in row] for row in new_matrix]
    return new_matrix
