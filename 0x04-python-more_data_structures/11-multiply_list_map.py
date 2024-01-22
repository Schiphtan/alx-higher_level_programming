#!/usr/bin/python3

"""returns list with all values multiplied by number without using loops"""


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
