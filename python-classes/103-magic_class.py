#!/usr/bin/python3
import math
""" USING THE MATH MODULE """


class MagicClass:
    """ setup stuff """
    
    def __init__(self, radius=0):
        """ setup stuff """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number"0
        self._MagicClass__radius = radius

    def area(self):
        """ area function """
        return (_MagicClass__radius ** 2 math.pi)

    def circumference(self):
        """ circumference function """
        return ((2* math.pi) * self._MagicClass__radius)
