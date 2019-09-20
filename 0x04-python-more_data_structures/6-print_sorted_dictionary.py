#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key_value in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(key_value, a_dictionary[key_value]))

        '''
        list(d) on a dictionary returns a list of all the keys
        used in the dictionary,
        in insertion order (if you want it sorted, just use sorted(d) instead).
        To check whether a single key is in the dictionary, use the in keyword.
        '''
