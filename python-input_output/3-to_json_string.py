#!/usr/bin/python3
import json
""" returns json representation of object """


def to_json_string(my_obj):
    """ converts object to json object """
    try:
        return json.dump(my_obj)
    except ValueError as e:
        print(e)
