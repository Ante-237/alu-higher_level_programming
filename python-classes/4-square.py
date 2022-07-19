#!/usr/bin/python3
"""
NO MODULE USED
"""


class Square:
    """
    SQUARE CLASS
    """
    def __init__(self, size=0):
        self._Square__size = size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    def area(self):
        return self._Square__size**2
