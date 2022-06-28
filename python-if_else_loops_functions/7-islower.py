#!/usr/bin/python3
def is_lower(c):
    value = ord(c)
    if value >= 97 and value <= 122:
        return True
    elif value >= 48 and value <= 57:
        return False
    elif value >= 65 and value <= 90:
        return False
