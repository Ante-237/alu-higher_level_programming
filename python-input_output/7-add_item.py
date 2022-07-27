#!/usr/bin/python3
import sys
"""This file contains a function that adds
all arguments to a python list and saves
to a file """


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

save_to_json_file(sys.argv[1:],"add_item.json")
load_from_json_file("add_item.json")
