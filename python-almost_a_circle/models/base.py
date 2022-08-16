#!/usr/bin/python3
"""
just module documentation
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns json strings
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    def save_to_file(cls, list_objs):
        """ writing to file
        """
        s_name = cls.__name__ + ".json"
        ob = []
        if list_objs is not None:
            for i in list_objs:
                ob.append(cls.to_dictionary(i))
        with open(s_name, mode="w", encoding='utf-8') as mFile:
            mFile.write(cls.to_json_string(ob))
