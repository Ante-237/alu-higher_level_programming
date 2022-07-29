#!/usr/bin/python3
"""
function  uses the famous binary sort 
to sort integers 
"""


def find_peak(list_of_integers):
    """
    find peak using binary sort
    """
    l = len(list_of_integers)
    if l == 0:
        return
    half = l // 2
    if (half == l - 1 or list_of_integers[half] >= list_of_integers[half + 1] and (half == 0 or list_of_integers[half] >= list_of_integers[half - 1]):
            return (list_of_integers[half])
    elif half != l - 1 and list_of_integers[half + 1] > list_of_integers[half]:
            return (find_peak(list_of_integers[half + 1:]))
    return (find_peak(list_of_integers[:half]))
