#!/usr/bin/python3
"""
module contains good stuff
imports module from another module 
"""


Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """
    square class that makes use of parent class
    """

    def __init__(self, size):
        """
        class init which class parent init
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init_(size, size)

    def area(self):
        """
        area cal
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        output representation
        """
        return("[Square] {:d}/{:d}".format(self.__size, self.__size))
