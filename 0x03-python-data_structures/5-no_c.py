#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters 'c' and 'C' from a string.

    Args:
        my_string (str): The input string.


    Returns:
        str: The new string with 'c' and 'C' removed;

    """

    # Create a mapping table (dictionary) that sets the characters
    # to their replacement values

    char_replacement_dict = {ord(char): None for char in "cC"}

    # Call the translate string method giving it the mapping table
    new_string = my_string.translate(char_replacement_dict)
    return new_string
