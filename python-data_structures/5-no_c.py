#!/usr/bin/python3
def no_c(my_string):
    temp = ''
    for i in my_string:
        if (i.lower()) == 'c':
            temp += i
    return temp
