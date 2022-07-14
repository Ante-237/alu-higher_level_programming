#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    copy_d = a_dictionary
    for key,value_one in copy_d.items():
        if value == value_one:
            del copy_d[key]
            break
    a_dictionary = copy_d
    return a_dictionary
