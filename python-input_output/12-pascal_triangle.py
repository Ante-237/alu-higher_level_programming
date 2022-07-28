#!/usr/bin/python3
""" pascals triangle """


def pascal_triangle(n):
    the_list = []
    if n <= 0:
        return the_list
    else:
        for i in range(0, n):
            the_list.append(1)
