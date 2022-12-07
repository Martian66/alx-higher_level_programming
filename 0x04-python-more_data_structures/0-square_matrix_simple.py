#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        return [list(map(lamda k: k**2, i)) for i in matrix]
