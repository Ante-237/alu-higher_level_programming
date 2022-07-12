#!/usr/bin/python3


def roman_to_int(roman_string):
    final_value = 0
    counter = 0
    if isinstance(roman_string, str) == False or roman_string is None:
        return final_value
    else:
        for i in roman_string:
            if i == "M":
                final_value += 1000
                counter += 1
            elif i == "D":
                final_value += 500
                counter += 1
            elif i == "C":
                final_value += 100
                counter += 1
            elif i == "L":
                final_value += 50
                counter += 1
            elif i == "X":
                final_value += 10
                counter += 1
            elif i == "V":
                final_value += 5
                counter += 1
            elif i == "I" and counter == 0:
                final_value += 1
            elif i == "I" and counter > 0:
                final_value -= 1
        return final_value
