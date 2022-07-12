#!/usr/bin/python3
# delete a key in a dictionary


def simple_delete(a_dictionary, key=""):
    if key == "":
        return a_dictionary
    else:
        del a_dictionary[key]
        return a_dictionary
