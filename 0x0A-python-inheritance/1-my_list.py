#!/usr/bin/python3
"""
module for my lists (inherits form list)
"""


class MyList(list):
    """
    elements of the list int type
    return my list and sorted list
    """
    def print_sorted(self):
        # sorted method
        # sorted(iterable[, key][, reverse])
        print(sorted(self))
