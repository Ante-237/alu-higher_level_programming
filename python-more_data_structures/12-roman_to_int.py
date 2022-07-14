#!/usr/bin/python3


def roman_to_int(roman_string):
    # check if the data type passed is not string
    if not isinstance(roman_string, str):
        return 0
    total = 0
    num = 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # reverese the roman numerals to start with the tens of units and use each unit
    for r in reversed(roman_string):
        num = digits[r]
        if total < num * 5:
            total += num
        else:
            num -= 1
    return total
