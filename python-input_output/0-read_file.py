#!/usr/bin/python3


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        out_data = f.read()
        print(out_data)
