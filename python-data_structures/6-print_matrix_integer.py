#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for columns in range(len(matrix[row])):
            if columns != 0:
                print(" ", end='')
            print("{:d}".format(matrix[row][columns]), end='')
        print()
