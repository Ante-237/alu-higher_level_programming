#!/usr/bin/python3
""" just another module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """just a module"""
    def __init__(self, size, x=0, y=0, id=None):
        """just using the super class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ just string form """
        d = self.id
        b = self.__height
        c = self.__x
        e = self.__y
        return ("[Square] ({}) {}/{} - {}".format(d, c, e, b))
