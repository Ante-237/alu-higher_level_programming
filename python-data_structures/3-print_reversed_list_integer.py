#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if type(my_list) == type([]):

        count = len(my_list) - 1
        if count >= 0:
            for i in my_list:
                print("{:d}".format(my_list[count]))
                count -= 1
