#!/usr/bin/python3
"""
divides all elements
of a matrix
"""

def matrix_divided(matrix, div):
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
        
        
   prevRowLen = -1
    new_matrix = []
    for row in matrix:
        if (prevRowLen != len(row) and prevRowLen != -1):
            raise TypeError("Each row of the matrix must have the same size")
            return matrix
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of" +
                                " integers/floats")
                return matrix
            else:
                new_matrix.append(round(ele / div, 2))
        prevRowLen = len(row)
    return new_matrix
