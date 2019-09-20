#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # coudnt use [:] for copy
    new_dictionary = a_dictionary.copy()
    for i in new_dictionary:
        new_dictionary[i] = new_dictionary[i] * 2
    return new_dictionary
