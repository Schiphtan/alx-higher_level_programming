#!/usr/bin/python3

"""function replaces all occurrences of an element by another in a new list"""


def search_replace(my_list, search, replace):
    new_list = [replace if item == search else item for item in my_list]
    return new_list
