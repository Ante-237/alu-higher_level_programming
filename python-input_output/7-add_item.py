#!/usr/bin/python3
""" importing json modulel """
import json
""" using sys """
import sys
""" using other external modules """
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file
""" module uses mostly external modules """


""" calling functions to write and load from json file """
save_to_json_file(sys.argv,"add_item.json")
load_from_json_file("add_item.json")
