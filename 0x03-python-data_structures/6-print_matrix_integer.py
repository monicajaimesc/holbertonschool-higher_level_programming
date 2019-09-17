#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # acces to the row content
        for i in range(len(row)):
            # deleting last space
            if i is len(row) - 1:
                print("{:d}".format(row[i]), end="")
            else:
                # space between numbers
                print("{:d} ".format(row[i]), end="")
        print()
