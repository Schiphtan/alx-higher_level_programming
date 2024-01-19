#!/usr/bin/python3

"""function adds all unique integers in a list (only once for each integer)"""


def uniq_add(my_list=[]):
    # use set to store unique integers, then sum them up
    unique_integers = set(my_list)
    result = sum(unique_integers)
    return result
