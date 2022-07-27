#!/usr/bin/python3
"""
convert class to json
"""
import json


def class_to_json(obj):
    return json.dumps(obj.__dict__)
