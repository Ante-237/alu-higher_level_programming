#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for record in matrix:
        for i in record:
            print("{:d}".format(i))
        print("")
