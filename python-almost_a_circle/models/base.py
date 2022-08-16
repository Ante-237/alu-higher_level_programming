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

    @classmethod
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

    @staticmethod
    def from_json_string(json_string):
        """just another function"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        just function play with instances
        """
        if cls.__name__ is "Rectangle":
            tempo = cls(1, 1)
        if cls.__name__ is "Square":
            tempo = cls(1)
        tempo.update(**dictionary)
        return (tempo)

    @classmethod
    def load_from_file(cls):
        """
        load from file
        """
        fn = cls.__name__ + ".json"
        lst = []
        try:
            with open(fn, mode="r", encoding='utf-8') as myFile:
                lst = cls.from_json_string(myFile.read())
            for i, j in enumerate(lst):
                lst[i] = cls.create(**lst[i])
        except:
            pass
        return (lst)
