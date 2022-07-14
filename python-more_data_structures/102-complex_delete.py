#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    for key,value_one in a_dictionary.items():
        if value == value_one:
            del a_dictionary[key]
    return a_dictionary
