#!/usr/bin/pythone3

""" function that deletes a key in a dictionary"""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary.keys():
        a_dictionary.pop(key)
    return(a_dictionary)
