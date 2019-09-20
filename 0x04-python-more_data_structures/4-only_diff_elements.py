#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # letters in a or b but not both
    return (set_1 ^ (set_2))
