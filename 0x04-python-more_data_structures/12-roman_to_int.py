#!/usr/python3

def roman_to_int(roman_string):
    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }

    result = 0
    prev_value = 0

    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if roman_dict[roman_string[c]] >= prev_value:
                result += roman_dict[roman_string[c]]
            else:
                result -= roman_dict[roman_string[c]]
            prev_value = roman_dict[roman_string[c]]
    return result
