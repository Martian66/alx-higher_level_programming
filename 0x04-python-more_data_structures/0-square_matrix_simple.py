#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [list(map(lambda j: j ** 2, row)) for row in matrix]
