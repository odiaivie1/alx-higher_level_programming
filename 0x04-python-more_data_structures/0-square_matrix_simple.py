#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    squared = []
    for line in matrix:
        squared.append([c**2 for c in line])

        return (squared)
