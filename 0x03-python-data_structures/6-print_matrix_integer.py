#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if not matrix:
        print()
    else:
        for row in matrix:
            for element in row:
                if row.index(element) != len(row) - 1:
                    endspace = " "
                else:
                    endspace = ""
                print("{:d}".format(element), end=endspace)
            print()
