#!/usr/bin/python3
""" imports module from another module """


Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """ square class """

    def __init__(self, size):
        """ class init """
        self.integer_validator("size", size)
        self.__size = size
        super().__init_(size, size)
