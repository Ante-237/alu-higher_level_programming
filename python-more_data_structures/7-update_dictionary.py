#!/usr/bin/python3
# replaces or adds key/value in a dictionary


def update_dictionary(a_dictionary, key, value):
    for temp in a_dictionary:
        if key == temp:
            a_dictionary[key] = value
        if key not in a_dictionary.keys():
            a_dictionary[key] = value
