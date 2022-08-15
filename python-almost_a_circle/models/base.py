#!/usr/bin/python3
"""
just module documentation
"""


class Base:
    """ this is a base class
    that keeps track of ids"""
    id = 0
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
