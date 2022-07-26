#!/usr/bin/python3
""" using no modules """


def is_kind_of_class(obj, a_class):
    """ function returns true for any existence of obj relative """
    if isinstance(obj, a_class) or issubclass(obj, a_class):
        return True
    else:
        return False
