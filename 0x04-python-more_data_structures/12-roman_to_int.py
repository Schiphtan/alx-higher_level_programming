#!/usr/bin/python3

def roman_to_int(roman_string):
    rom_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0
    prev_value = 0

    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if rom_d[roman_string[c]] >= prev_value:
                result += rom_d[roman_string[c]]
            else:
                result -= rom_d[roman_string[c]]
            prev_value = rom_d[roman_string[c]]
    return result
