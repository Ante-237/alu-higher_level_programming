#!/usr/bin/python3
"""
just module documentation
"""


class Base:
    """ this is a base class
    that keeps track of ids"""

    def __init__(self, id=None):
        self.__nb_objects = 0
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
