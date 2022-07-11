#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    counter = 1
    for record in matrix:
        for i in record:
            if counter == len(record):
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end=" ")
            counter += 1
        print("")
