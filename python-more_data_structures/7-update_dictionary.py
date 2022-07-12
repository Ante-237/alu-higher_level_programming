#!/usr/bin/python3
# replaces or adds key/value in a dictionary


def update_dictionary(a_dictionary, key, value):
    temp_list = list(a_dictionary.keys())
    for temp in a_dictionary:
        if key == temp:
            a_dictionary[key] = value
        if key not in temp_list:
            a_dictionary[key] = value
