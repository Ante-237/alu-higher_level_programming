#!/usr/bin/python3


def search_replace(my_list, search, replace):
    for i in range(0, len(my_list)):
        if search == my_list[i]:
            my_list[i] = replace
