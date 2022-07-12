#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    the_list = list(map(my_list, key=lambda x: x * number))
    return the_list
