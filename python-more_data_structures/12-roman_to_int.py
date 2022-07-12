#!/usr/bin/python3


def roman_to_int(roman_string):
    final_value = 0
    if type(roman_string) != type("") or roman_string is None:
        return final_value
    else:
        for i in roman_string:
            if i == "M":
                final_value += 1000
            elif i == "D":
                final_value += 500
            elif i == "C":
                final_value += 100
            elif i == "L":
                final_value += 50
            elif i == "X":
                final_value += 10
            elif i == "V":
                final_value += 5
            elif i == "I":
                final_value += 1
        return final_value
