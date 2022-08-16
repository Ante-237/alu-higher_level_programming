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
        b = self.height
        c = self.x
        e = self.y
        return ("[Square] ({}) {}/{} - {}".format(d, c, e, b))

    @property
    def size(self):
        """just size function"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
