#!/usr/bin/python3

int_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for y in range(len(matrix[i])):
            print("{:d}".format(matrix[i][y]), end="")
            if y != (len(matrix[u]) - 1):
                print(" ", end="")

                print("")
