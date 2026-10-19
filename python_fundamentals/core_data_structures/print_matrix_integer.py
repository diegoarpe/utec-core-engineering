#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for value in range(len(row)):
            sep = "" if value == len(row) - 1 else " "
            print("{:d}".format(row[value]), end=sep)
        print()
