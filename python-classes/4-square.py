#!/usr/bin/python3
"""
NO MODULE USED
"""


class Square:
    """
    SQUARE CLASS
    """
    def __init__(self, size=0):
        self.size = size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = value

    def size(self):
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        else:
            return self.size

    def area(self):
        return self.size**2
