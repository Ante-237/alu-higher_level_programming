#!/usr/bin/python3
"""
divides all elements
of a matrix
"""


def matrix_divided(matrix, div):
    """ matrix divide function """
    for temp_one in matrix:
        for temp_two in temp_one:
            if not isinstance(temp_two, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    

    tempCount = -1
    for row in matrix:
        if tempCount != len(row) and tempCount != -1:
            raise TypeError("Each row of the matrix must have the same size")
        tempCount = len(row)


    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for temp_one in matrix:
        for temp_two in temp_one:
            new_matrix.append(round(temp_two/div, 2))
    return new_matrix
