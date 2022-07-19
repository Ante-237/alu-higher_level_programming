#!/usr/bin/python3
"""
NO MODULE USED
"""


class Square:
    """
    SQUARE CLASS
    """
    def __init__(self, size=0):
        """
        INSTANCE INIT
        """
        self._size = size

    def size(self, value):
        """
        A SETTER
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def size(self):
        """
        A GETTER
        """
            return self._size

    def area(self):
        """
        CALCULATE AREA
        """
        return self._size**2
