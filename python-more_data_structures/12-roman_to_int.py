#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for i in range(len(roman_string)):
        if roman_dict.get(roman_string[i]) == 0:
            return 0
    if roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
        num += roman_dict[roman_string[i]]
    return num
