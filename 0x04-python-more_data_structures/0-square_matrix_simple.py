#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # map can be applied to more than on list
    # the list don't have to have the same lengh
    # map() will apply its lambda funtion to the list elements
    return [list(map((lambda x: x * x), row)) for row in matrix]
