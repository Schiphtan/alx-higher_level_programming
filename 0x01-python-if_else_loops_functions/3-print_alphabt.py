#!/usr/bin/python3

for char_code in range(ord('a'), ord('z') + 1):

    char = chr(char_code)

    if char != 'q' and char != 'e':
        print(char, end='')


print()
