#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        copy_l = my_list[:]
        return copy_l
    elif idx >= len(my_list):
        copy_l = my_list[:]
        return copy_l
