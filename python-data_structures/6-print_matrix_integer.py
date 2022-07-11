#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    counter = 1
    for record in matrix:
        for i in record:
            if counter%3 == 0:
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end=" ")
            counter += 1
        print("")
