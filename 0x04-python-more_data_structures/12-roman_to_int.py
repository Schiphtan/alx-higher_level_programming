#!/usr/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }

    result = sum(
            roman_dict[roaman_string[i]] if (i == len(roman_string) - 1 or
            roman_dict[roman_string[i]] >= roman_dict[roman_string[i + 1]])
            else -roman_dict[roman_string[i]]
            for i in range(len(roman_string))
        )

    return result