#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda x:(lambda y: y**2), matrix))
