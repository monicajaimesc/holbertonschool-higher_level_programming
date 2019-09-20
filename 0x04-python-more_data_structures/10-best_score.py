#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        # value is an integer
        key_value = sorted(a_dictionary.key_value())
        result = key_value[-1]
        for key_value in a_dictionary:
            if result == a_dictionary[key_value]:
                return key_value
