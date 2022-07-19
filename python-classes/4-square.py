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
        INIT FOR CLASS
        """
        self.__size = size

    @size.setter
    def size(self, value):
        """
        setter method
        raises exceptions
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    @property
    def size(self):
        """
        GETTER METHOD
        RETURNS PRIVATE HIDDEN VALUE
        """
        return self.__size

    def area(self):
        """
        RETURNS THE SQUARE AREA
        """
        return self.__size**2
