#!/usr/bin/python3

def islower(char):
    """Checks for lowercase characters."""
    if ord(char) >= 97 and ord(char) <= 122:
        return True
    else:
        return False
